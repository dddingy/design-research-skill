#!/usr/bin/env python3
"""Validate a generated Design Definition HTML document."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


def validate(path: Path) -> tuple[list[str], list[str]]:
    if not path.is_file():
        return [f"File not found: {path}"], []

    source = path.read_text(encoding="utf-8")
    class_tokens = {
        token
        for value in re.findall(r'class\s*=\s*["\']([^"\']*)["\']', source)
        for token in value.split()
    }
    errors: list[str] = []
    warnings: list[str] = []

    for class_name in (
        "hero", "hero-inner", "topline", "materials", "section-group"
    ):
        if class_name not in class_tokens:
            errors.append(f"Missing template class '.{class_name}'.")

    required_sections = (
        "Materials", "Project Background", "Design Goal", "User Flow", "Design Direction"
    )
    positions = []
    for heading in required_sections:
        match = re.search(
            rf"<h2\b[^>]*>\s*{re.escape(heading)}\s*</h2>", source, flags=re.IGNORECASE
        )
        if match is None:
            errors.append(f"Missing required section '{heading}'.")
        else:
            positions.append(match.start())
    if len(positions) == len(required_sections) and positions != sorted(positions):
        errors.append("Required sections are not in template order.")

    if re.search(
        r'data-user-flow-type\s*=\s*["\']page-structure["\']', source, flags=re.IGNORECASE
    ):
        page_section = re.search(
            r'<section\b[^>]*data-user-flow-type\s*=\s*["\']page-structure["\'][^>]*>.*?</section>',
            source,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if "wireframe-page" not in class_tokens:
            errors.append("Page-structure User Flow must contain a '.wireframe-page' layout.")
        if class_tokens.intersection({"flow-map", "lane-flow", "parallel-flow", "phase-flow", "handoff"}):
            errors.append("Page-structure User Flow must not use sequential flow components.")
        if page_section and any(
            phrase in page_section.group(0)
            for phrase in ("用页面结构表达", "不强行串成", "流程类型：", "判断依据：", "组件选择：")
        ):
            errors.append("User Flow contains generation rationale instead of requirement content.")

    heading_matches = list(
        re.finditer(r"<h2\b[^>]*>(.*?)</h2>", source, flags=re.IGNORECASE | re.DOTALL)
    )
    content_owners: dict[str, set[str]] = {}
    for block in re.finditer(
        r"<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>", source, flags=re.IGNORECASE | re.DOTALL
    ):
        owner = next(
            (
                re.sub(r"<[^>]+>", "", heading.group(1)).strip()
                for heading in reversed(heading_matches)
                if heading.start() < block.start()
            ),
            "",
        )
        text = html.unescape(re.sub(r"<[^>]+>", "", block.group(1)))
        normalized = re.sub(r"[\W_]+", "", text, flags=re.UNICODE).casefold()
        if owner and len(normalized) >= 12:
            content_owners.setdefault(normalized, set()).add(owner)
    if any(len(owners) > 1 for owners in content_owners.values()):
        warnings.append("Repeated content appears in multiple review sections.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="Path to the Design Definition HTML file")
    args = parser.parse_args()
    errors, warnings = validate(args.html.expanduser())
    if errors:
        print("Design Definition validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Design Definition validation passed.")
    for warning in warnings:
        print(f"Warning: {warning}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
