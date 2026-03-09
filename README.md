# BAOBAB


# BAOBAB

```text
██████╗    █████╗    ██████╗    ██████╗    █████╗    ██████╗
██╔══██╗  ██╔══██╗  ██╔═══██╗  ██╔══██╗  ██╔══██╗  ██╔══██╗
██████╔╝  ███████║  ██║   ██║  ██████╔╝  ███████║  ██████╔╝
██╔══██╗  ██╔══██║  ██║   ██║  ██╔══██╗  ██╔══██║  ██╔══██╗
███████║  ██║  ██║  ╚██████╔╝  ███████║  ██║  ██║  ███████║
╚══════╝  ╚═╝  ╚═╝   ╚═════╝   ╚══════╝  ╚═╝  ╚═╝  ╚══════╝

plant a tree, parse a tree


---

BAOBAB prints a directory tree and dumps file contents in a markdown-friendly format.

Useful for:

- repository inspection
- debugging
- project snapshots
- LLM ingestion

---

## Install

```bash
git clone https://github.com/Elder-Lele/baobab
cd baobab
```

## Usage

Scan current directory:

python baobab.py

Scan another folder:

python baobab.py ./project

Export repo snapshot:

python baobab.py . > repo_dump.md

Tree only:

python baobab.py --tree-only

Parse files only:

python baobab.py --parse-only

---



MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2026 Elder Lele / Lele Labs

