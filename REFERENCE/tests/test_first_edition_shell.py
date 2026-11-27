from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "first_edition_shell"


class ShellParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chapter_ids: list[str] = []
        self.external_assets: list[str] = []
        self.inline_scripts = 0
        self.search_input = False

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        element_id = values.get("id", "")
        if element_id.startswith("chapter-") and tag == "section":
            self.chapter_ids.append(element_id)
        if tag in {"script", "link"}:
            target = values.get("src") or values.get("href", "")
            if target.startswith(("http://", "https://", "//")):
                self.external_assets.append(target)
            if tag == "script" and not values.get("src"):
                self.inline_scripts += 1
        if tag == "input" and values.get("id") == "chapter-search":
            self.search_input = values.get("type") == "search"


def test_shell_has_exactly_nineteen_chapters_and_two_parts():
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = ShellParser()
    parser.feed(page)
    assert len(parser.chapter_ids) == 19
    assert parser.chapter_ids == [f"chapter-{number}" for number in range(1, 20)]
    assert 'id="part-i"' in page
    assert 'id="part-ii"' in page
    assert parser.search_input


def test_shell_is_offline_local_and_has_no_inline_script():
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = ShellParser()
    parser.feed(page)
    assert not parser.external_assets
    assert parser.inline_scripts == 0
    assert 'href="reader.css"' in page
    assert 'src="reader.js"' in page
    assert "default-src 'none'" in page
    assert "img-src 'self' data:" in page


def test_every_chapter_discloses_unpublished_content_state():
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    assert page.count("Материалы готовятся · публикационно допущенных статей пока нет") == 19
    assert "не является публичным изданием" in page
    assert "публикационно допущенных статей" in page


def test_search_script_uses_safe_text_and_numeric_part_grouping():
    script = (ROOT / "reader.js").read_text(encoding="utf-8")
    assert 'addEventListener("input", update)' in script
    assert "textContent" in script
    assert "innerHTML" not in script
    assert "Number(chapter.id.replace" in script
    assert "visibleParts.add(chapterNumber <= 10 ? \"part-i\" : \"part-ii\")" in script


def test_stylesheet_supports_mobile_and_reduced_motion():
    css = (ROOT / "reader.css").read_text(encoding="utf-8")
    assert "@media (max-width: 820px)" in css
    assert "@media (max-width: 460px)" in css
    assert "@media (prefers-reduced-motion: reduce)" in css
