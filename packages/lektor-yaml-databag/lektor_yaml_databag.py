"""Adds YAML (.yaml / .yml) databag support to Lektor.

Lektor's built-in ``Databags`` class only discovers and loads ``.ini`` and
``.json`` files. This plugin patches both the discovery loop and the
``load_databag`` dispatch so that YAML files placed in ``databags/`` are
picked up by ``bag('name')`` exactly the same way as JSON files.
"""

import os
from collections import OrderedDict

import yaml

from lektor import databags as _databags
from lektor.pluginsystem import Plugin

_YAML_EXTS = (".yaml", ".yml")
_ORIGINAL_LOAD = _databags.load_databag
_ORIGINAL_INIT = _databags.Databags.__init__


def _load_yaml(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if data is None:
        return OrderedDict()
    return data


def _load_databag_with_yaml(filename):
    if filename.endswith(_YAML_EXTS):
        return _load_yaml(filename)
    return _ORIGINAL_LOAD(filename)


def _patched_init(self, env):
    _ORIGINAL_INIT(self, env)
    try:
        for filename in os.listdir(self.root_path):
            if filename.endswith(_YAML_EXTS):
                name = os.path.splitext(filename)[0]
                self._known_bags.setdefault(name, []).append(filename)
    except OSError:
        pass


class YamlDatabagPlugin(Plugin):
    name = "YAML databag"
    description = "Loads .yaml / .yml files as Lektor databags via bag()."

    def on_setup_env(self, **extra):
        _databags.load_databag = _load_databag_with_yaml
        _databags.Databags.__init__ = _patched_init
