#!/usr/bin/env python3
# ============================================================
#
#  ██████╗   █████╗   ██████╗  ██████╗   █████╗   ██████╗
#  ██╔══██╗ ██╔══██╗ ██╔═══██╗ ██╔══██╗ ██╔══██╗ ██╔══██╗
#  ██████╔╝ ███████║ ██║   ██║ ██████╔╝ ███████║ ██████╔╝
#  ██╔══██╗ ██╔══██║ ██║   ██║ ██╔══██╗ ██╔══██║ ██╔══██╗
#  ███████║ ██║  ██║ ╚██████╔╝ ███████║ ██║  ██║ ███████║
#  ╚══════╝ ╚═╝  ╚═╝  ╚═════╝  ╚══════╝ ╚═╝  ╚═╝ ╚══════╝
#
#  "plant a tree, parse a tree"
#
#  BAOBAB
#  Print a directory tree and dump file contents in markdown.
#
# ============================================================

import os
import sys
import argparse


IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "node_modules",
    ".mypy_cache",
    ".idea",
}

IGNORE_FILES = {
    ".DS_Store",
}

VALID_EXTENSIONS = {
    ".py",
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".txt",
    ".toml",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".html",
    ".css",
}

MAX_FILE_LINES = 400
MAX_FILE_SIZE_KB = 512


EXT_LANG = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".jsx": "javascript",
    ".json": "json",
    ".md": "markdown",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".html": "html",
    ".css": "css",
    ".txt": "",
    ".toml": "toml",
}


def detect_lang(path):

    ext = os.path.splitext(path)[1].lower()

    return EXT_LANG.get(ext, "")


def should_parse(path):

    name = os.path.basename(path)

    if name in IGNORE_FILES:
        return False

    if name.startswith("."):
        return False

    ext = os.path.splitext(name)[1].lower()

    if ext not in VALID_EXTENSIONS:
        return False

    try:

        size_kb = os.path.getsize(path) / 1024

        if size_kb > MAX_FILE_SIZE_KB:
            return False

    except Exception:
        return False

    return True


def print_tree(root, prefix=""):

    try:
        items = sorted(os.listdir(root), key=str.lower)
    except Exception:
        return

    for i, name in enumerate(items):

        path = os.path.join(root, name)

        connector = "└── " if i == len(items) - 1 else "├── "

        print(prefix + connector + name)

        if os.path.isdir(path):

            if name in IGNORE_DIRS or name.startswith("."):
                continue

            extension = "    " if i == len(items) - 1 else "│   "

            print_tree(path, prefix + extension)


def print_file(path):

    lang = detect_lang(path)

    print(f"\n### FILE: {path}\n")

    print(f"```{lang}")

    try:

        with open(path, "r", encoding="utf-8", errors="ignore") as f:

            for i, line in enumerate(f):

                if i >= MAX_FILE_LINES:
                    print("... [TRUNCATED]")
                    break

                print(line.rstrip())

    except Exception as e:

        print(f"[ERROR: {e}]")

    print("```")
    print()


def parse_files(root):

    for dirpath, dirnames, filenames in os.walk(root):

        dirnames[:] = [
            d for d in dirnames
            if d not in IGNORE_DIRS and not d.startswith(".")
        ]

        for file in filenames:

            path = os.path.join(dirpath, file)

            if should_parse(path):

                print_file(path)


def main():

    parser = argparse.ArgumentParser(
        description="BAOBAB: print a directory tree and dump file contents."
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="root directory to inspect",
    )

    parser.add_argument(
        "--tree-only",
        action="store_true",
        help="print directory tree only",
    )

    parser.add_argument(
        "--parse-only",
        action="store_true",
        help="print file contents only",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="BAOBAB 0.1"
    )

    args = parser.parse_args()

    if args.tree_only and args.parse_only:
        print("Choose only one: --tree-only OR --parse-only")
        sys.exit(1)

    root = args.path

    if not args.parse_only:

        print("\n================ TREE ================\n")

        print_tree(root)

    if not args.tree_only:

        print("\n================ FILE CONTENT ================\n")

        parse_files(root)


if __name__ == "__main__":
    main()