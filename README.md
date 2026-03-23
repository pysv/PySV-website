# Python Software Verband

This is the repository for the [Python Software Verband](https://python-verband.org) website. It is built with [Lektor](https://www.getlektor.com/), a static site generator, and supports both German and English content.

## Prerequisites

- Python (version specified in `.python-version`)
- [uv](https://docs.astral.sh/uv/) for environment and dependency management

> **Note:** We use `uv` as our sole tool for environment and dependency management. We do not support `pip`, `conda`, `poetry`, or other alternatives. `uv` is fast, broadly accepted in the Python community, and keeping a single tool avoids complexity and inconsistencies across contributor setups.

## Local Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.
2. Sync the project (this creates the virtual environment and installs dependencies):
   ```bash
   uv sync
   ```
3. Create the local build directory:
   ```bash
   mkdir tmp
   ```
4. Start the development server:
   ```bash
   uv run lektor server -O tmp -p 5001
   ```
5. Visit the website at [http://localhost:5001](http://localhost:5001).

## Contributing Blog Posts

Blog posts live in `content/blog/`. Each post has its own directory containing the content file(s) and any associated images.

### Creating a New Blog Post

The easiest way to create a new blog post is with the CLI tool:

```bash
uv run python blog.py add
```

This will prompt you for the title, publication date, and author name, then generate the directory with template files for both German and English.

Alternatively, you can create the files manually:

1. Create a new directory under `content/blog/` with a descriptive slug, e.g.:
   ```
   content/blog/2026-pycon-de/
   ```

2. Create a `contents.lr` file inside. This is the **German** version (the primary language). Use the following format:

   ```
   title: PyCon DE 2026
   ---
   pub_date: 2026-10-15
   ---
   author: Your Name
   ---
   tags: community, conference
   ---
   teaser_text: Eine kurze Beschreibung des Beitrags für die Übersicht.

   ---
   teaser_image: preview.jpg
   ---
   cta: Mehr erfahren
   ---
   show_on_homepage: False
   ---
   highlighted: False
   ---
   _discoverable: yes
   ---
   body:

   Your markdown content goes here.
   ```

   **Field reference:**

   | Field             | Required | Description                                                         |
   |-------------------|----------|---------------------------------------------------------------------|
   | `title`           | yes      | Post title                                                          |
   | `pub_date`        | yes      | Publication date (`YYYY-MM-DD`)                                     |
   | `author`          | no       | Author name                                                         |
   | `tags`            | no       | Comma-separated tags                                                |
   | `teaser_text`     | no       | Short summary shown in post listings                                |
   | `teaser_image`    | no       | Filename of the image shown in post listings (stored in same dir)   |
   | `cta`             | no       | Call-to-action text for the homepage                                |
   | `body`            | yes      | The main post content in Markdown                                   |
   | `show_on_homepage`| no       | Set to `True` to feature this post on the homepage as a USP         |
   | `highlighted`     | no       | Set to `True` to display as the larger/left USP on the homepage     |
   | `_discoverable`   | no       | Set to `yes` to make the post discoverable                          |

### Adding an English Translation

To provide an English version, create a `contents+en.lr` file in the same directory. It uses the same format as `contents.lr` but with English text:

```
content/blog/2026-pycon-de/
├── contents.lr        # German (primary)
├── contents+en.lr     # English translation
├── preview.jpg
└── ...
```

The English version will be served under the `/en/` URL prefix automatically.

### Including Images

Place image files directly in the blog post directory alongside `contents.lr`:

```
content/blog/2026-pycon-de/
├── contents.lr
├── preview.jpg
├── session-photo.jpg
└── group-photo.png
```

Reference them in the body using standard Markdown image syntax with a relative path:

```markdown
![Attendees networking during the coffee break](./session-photo.jpg)
```

**Image guidelines:**

- Use descriptive alt text for accessibility.
- Optimize images before committing — aim for a reasonable file size (resize large photos to ~850px wide).
- Supported formats: `.jpg`, `.png`.
- The `teaser_image` field should reference an image in the same directory by filename (no path prefix needed).

## Available Commands

| Command            | Description                                    |
|-------------------|------------------------------------------------|
| `uv run python blog.py add` | Scaffold a new blog post interactively         |
| `make run`         | Start the development server on port 5001      |
| `make build`       | Build the static site into the `tmp/` directory |

## Deployment

See [docs/deployment.md](docs/deployment.md) for deployment instructions (S3 hosting setup).
