#!/usr/bin/env python3
"""Validate a generated Feature Benchmarking Source Pack HTML file."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


class SourcePackParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.current_text: list[str] = []
        self.capture_tag: str | None = None
        self.h2: list[str] = []
        self.scope_values: list[str] = []
        self.summary_points = 0
        self.in_summary_box = False
        self.summary_box_depth = 0
        self.in_summary_ul = False
        self.in_article = False
        self.in_sources = False
        self.current_article: dict[str, object] | None = None
        self.articles: list[dict[str, object]] = []
        self.img_srcs: list[str] = []
        self.has_stageb_recommendations = False
        self.has_copy_output = False
        self.has_copy_button = False
        self.has_stageb_table = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        classes = set((attr.get("class") or "").split())
        self.stack.append(tag)

        if tag in {"h2", "dd", "li"}:
            self.capture_tag = tag
            self.current_text = []

        if tag == "section" and "summary" in classes:
            self.in_summary_box = True
            self.summary_box_depth = len(self.stack)

        if self.in_summary_box and tag == "ul":
            self.in_summary_ul = True

        if tag == "article" and "card" in classes:
            self.in_article = True
            self.current_article = {"id": attr.get("id", ""), "sources": []}

        if self.in_article and tag == "ul" and "sources" in classes:
            self.in_sources = True

        if tag == "img":
            src = attr.get("src")
            if src:
                self.img_srcs.append(src)

        if tag == "table" and self.stack and self._has_open_stageb_section:
            self.has_stageb_table = True

        if tag == "table" and "stageb-recommendations" in classes:
            self.has_stageb_recommendations = True

        if tag == "textarea" and "copy-output" in classes:
            self.has_copy_output = True

        if tag == "button" and ("copy-button" in classes or attr.get("id") == "copy-canvas-reply"):
            self.has_copy_button = True

    @property
    def _has_open_stageb_section(self) -> bool:
        # HTMLParser does not expose parent attrs, so this is set by class text checks later.
        return True

    def handle_endtag(self, tag: str) -> None:
        text = " ".join("".join(self.current_text).split())
        if self.capture_tag == tag:
            if tag == "h2":
                self.h2.append(text)
            elif tag == "dd":
                self.scope_values.append(text)
            elif tag == "li":
                if self.in_summary_ul:
                    self.summary_points += 1
                if self.in_sources and self.current_article is not None:
                    self.current_article["sources"].append(text)
            self.capture_tag = None
            self.current_text = []

        if tag == "ul" and self.in_sources:
            self.in_sources = False

        if tag == "ul" and self.in_summary_ul:
            self.in_summary_ul = False

        if tag == "article" and self.in_article:
            if self.current_article is not None:
                self.articles.append(self.current_article)
            self.current_article = None
            self.in_article = False

        if self.in_summary_box and len(self.stack) == self.summary_box_depth:
            self.in_summary_box = False

        if self.stack:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.capture_tag:
            self.current_text.append(data)


def validate(path: Path) -> list[str]:
    parser = SourcePackParser()
    html = path.read_text(encoding="utf-8")
    parser.feed(html)

    errors: list[str] = []

    if "调研范围与假设" in parser.h2:
        errors.append("Use heading '调研范围', not '调研范围与假设'.")
    if "调研范围" not in parser.h2:
        errors.append("Missing heading '调研范围'.")
    if "画布分析建议" in parser.h2:
        errors.append("Use next-step product recommendation table, not legacy heading '画布分析建议'.")

    for value in parser.scope_values[:3]:
        if len(value) > 40:
            errors.append(f"Scope field is too long: {value[:36]}...")

    summary_match = re.search(r"<h2>\s*关键结论\s*</h2>.*?<ul>(.*?)</ul>", html, re.S)
    summary_points = len(re.findall(r"<li\b", summary_match.group(1))) if summary_match else 0
    if not 3 <= summary_points <= 5:
        errors.append(f"Executive Summary must have 3-5 bullets; found {summary_points}.")

    if not parser.has_stageb_recommendations or not parser.has_copy_output or not parser.has_copy_button:
        errors.append("Next-step section must use a product recommendation table, a copyable reply textarea, and a copy button.")

    for article in parser.articles:
        sources = article["sources"]
        source_count = len(sources)
        article_id = article.get("id") or "(missing id)"
        if not 3 <= source_count <= 5:
            errors.append(f"Product card '{article_id}' must have 3-5 sources; found {source_count}.")
        has_official = any("官方" in source for source in sources)
        has_non_official = any(("非官方" in source or "第三方" in source) for source in sources)
        if not has_official:
            errors.append(f"Product card '{article_id}' needs at least one official source.")
        if not has_non_official:
            errors.append(f"Product card '{article_id}' needs at least one non-official/third-party source.")

    for src in parser.img_srcs:
        if src.startswith(("http://", "https://")):
            errors.append(f"Image must be local, found hotlink: {src}")
        elif not (path.parent / src).exists():
            errors.append(f"Missing local image asset: {src}")

    return errors


def main() -> int:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("html", type=Path)
    args = arg_parser.parse_args()

    errors = validate(args.html)
    if errors:
        print("Source Pack validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Source Pack validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
