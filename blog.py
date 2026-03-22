"""CLI tool to scaffold new blog posts for the PySV website."""

import re
import sys
from datetime import date
from pathlib import Path

CONTENT_DIR = Path(__file__).parent / "content" / "blog"

TEMPLATE_DE = """\
title: {title}
---
pub_date: {pub_date}
---
author: {author}
---
tags:
---
teaser_text:

Kurze Zusammenfassung des Beitrags (1-2 Sätze). Wird in der Blog-Übersicht angezeigt.

---
teaser_image: preview.jpg
---
cta: Weiterlesen
---
show_on_homepage: False
---
highlighted: False
---
_discoverable: yes
---
body:

#### Überschrift

Hier den Inhalt des Blogposts schreiben. Markdown wird unterstützt.

Um Bilder einzufügen, lege die Bilddateien in diesen Ordner und verweise so darauf:

![Bildbeschreibung für Barrierefreiheit](./mein-bild.jpg)
"""

TEMPLATE_EN = """\
title: {title}
---
pub_date: {pub_date}
---
author: {author}
---
tags:
---
teaser_text:

Short summary of the post (1-2 sentences). Shown in the blog overview.

---
teaser_image: preview.jpg
---
cta: Read more
---
show_on_homepage: False
---
highlighted: False
---
_discoverable: yes
---
body:

#### Heading

Write your blog post content here. Markdown is supported.

To include images, place the image files in this directory and reference them like this:

![Descriptive alt text for accessibility](./my-image.jpg)
"""


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def prompt(label: str, default: str = "") -> str:
    """Prompt the user for input with an optional default."""
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def add() -> None:
    """Interactive flow to create a new blog post."""
    print("\n── New Blog Post ──\n")

    title = prompt("Title (e.g. 'PyCon DE 2026')")
    if not title:
        print("Error: title is required.")
        sys.exit(1)

    today = date.today().isoformat()
    pub_date = prompt("Publication date (YYYY-MM-DD)", default=today)

    try:
        year = date.fromisoformat(pub_date).year
    except ValueError:
        print(f"Error: '{pub_date}' is not a valid date (expected YYYY-MM-DD).")
        sys.exit(1)

    author = prompt("Author name", default="PySV")

    slug = f"{year}-{slugify(title)}"
    post_dir = CONTENT_DIR / slug

    print(f"\n── Summary ──")
    print(f"  Title:    {title}")
    print(f"  Date:     {pub_date}")
    print(f"  Author:   {author}")
    print(f"  Directory: content/blog/{slug}/")
    print(f"  Files:     contents.lr (DE), contents+en.lr (EN)\n")

    confirm = input("Create this blog post? [Y/n] ").strip().lower()
    if confirm and confirm != "y":
        print("Cancelled.")
        sys.exit(0)

    post_dir.mkdir(parents=True, exist_ok=False)

    fields = {"title": title, "pub_date": pub_date, "author": author}
    (post_dir / "contents.lr").write_text(TEMPLATE_DE.format(**fields))
    (post_dir / "contents+en.lr").write_text(TEMPLATE_EN.format(**fields))

    print(f"\nBlog post created at: content/blog/{slug}/")
    print("\nNext steps:")
    print(f"  1. Edit content/blog/{slug}/contents.lr (German)")
    print(f"  2. Edit content/blog/{slug}/contents+en.lr (English)")
    print(f"  3. Add a preview.jpg image to the directory")
    print(f"  4. Run 'make run' and check http://localhost:5001/blog/{slug}/")


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] != "add":
        print("Usage: uv run python blog.py add")
        sys.exit(1)
    add()


if __name__ == "__main__":
    main()
