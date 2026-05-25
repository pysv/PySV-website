from setuptools import setup

setup(
    name="lektor-yaml-databag",
    version="0.1.0",
    description="Adds YAML (.yaml / .yml) databag support to Lektor.",
    py_modules=["lektor_yaml_databag"],
    install_requires=["PyYAML>=6.0"],
    entry_points={
        "lektor.plugins": [
            "yaml-databag = lektor_yaml_databag:YamlDatabagPlugin",
        ],
    },
)
