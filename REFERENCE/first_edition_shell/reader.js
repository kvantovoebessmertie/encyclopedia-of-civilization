"use strict";

(() => {
  const input = document.getElementById("chapter-search");
  const status = document.getElementById("search-status");
  const chapters = Array.from(document.querySelectorAll(".chapter"));
  const links = Array.from(document.querySelectorAll("#chapter-links a[href^='#chapter-']"));
  const partHeadings = Array.from(document.querySelectorAll(".part-heading"));

  if (!input || !status || chapters.length !== 19) {
    if (status) status.textContent = "Навигация не прошла проверку структуры.";
    return;
  }

  const normalize = (value) => String(value || "")
    .normalize("NFKC")
    .toLocaleLowerCase("ru")
    .replace(/ё/g, "е")
    .trim();

  const chapterById = new Map(chapters.map((chapter) => [chapter.id, chapter]));
  const initialCount = chapters.length;

  function update() {
    const query = normalize(input.value);
    let visible = 0;
    const visibleParts = new Set();

    for (const chapter of chapters) {
      const searchable = normalize(
        chapter.textContent + " " + (chapter.getAttribute("data-search") || "")
      );
      const match = !query || searchable.includes(query);
      chapter.hidden = !match;
      if (match) {
        visible += 1;
        visibleParts.add(chapter.id <= "chapter-10" ? "part-i" : "part-ii");
      }
    }

    for (const link of links) {
      const targetId = link.getAttribute("href").slice(1);
      const target = chapterById.get(targetId);
      link.hidden = !target || target.hidden;
    }

    for (const part of partHeadings) {
      part.hidden = Boolean(query) && !visibleParts.has(part.id);
    }

    status.textContent = query
      ? "Найдено глав: " + visible + " из " + initialCount
      : initialCount + " глав · 2 части";
  }

  input.addEventListener("input", update);
  update();
})();
