"use strict";

const form = document.getElementById("contribution-form");
const sourcesRoot = document.getElementById("sources");
const relationsRoot = document.getElementById("relations");
const status = document.getElementById("status");

function addFromTemplate(templateId, root) {
  const template = document.getElementById(templateId);
  const fragment = template.content.cloneNode(true);
  const entry = fragment.querySelector(".source-entry, .relation-entry");
  entry.querySelector("[data-remove]").addEventListener("click", () => entry.remove());
  root.appendChild(fragment);
}

function value(id) {
  return document.getElementById(id).value.trim();
}

function splitLines(text) {
  return text.split(/\r?\n/).map(item => item.trim()).filter(Boolean);
}

function readSources() {
  return [...sourcesRoot.querySelectorAll(".source-entry")].map(entry => {
    const result = {};
    for (const field of entry.querySelectorAll("[data-field]")) {
      const raw = field.value.trim();
      if (!raw) continue;
      if (field.dataset.field === "creators") {
        const creators = splitLines(raw);
        if (creators.length) result.creators = creators;
      } else {
        result[field.dataset.field] = raw;
      }
    }
    return result;
  }).filter(item => Object.keys(item).length > 0);
}

function readRelations() {
  return [...relationsRoot.querySelectorAll(".relation-entry")].map(entry => {
    const result = {};
    for (const field of entry.querySelectorAll("[data-field]")) {
      result[field.dataset.field] = field.value.trim();
    }
    return result;
  });
}

function showError(message) {
  status.textContent = message;
  status.focus?.();
}

document.getElementById("add-source").addEventListener("click", () => {
  if (sourcesRoot.querySelectorAll(".source-entry").length >= 100) {
    showError("По контракту можно добавить не более 100 источников.");
    return;
  }
  addFromTemplate("source-template", sourcesRoot);
});

document.getElementById("add-relation").addEventListener("click", () => {
  if (relationsRoot.querySelectorAll(".relation-entry").length >= 100) {
    showError("По контракту можно добавить не более 100 связей.");
    return;
  }
  addFromTemplate("relation-template", relationsRoot);
});

form.addEventListener("reset", () => {
  window.setTimeout(() => {
    sourcesRoot.replaceChildren();
    relationsRoot.replaceChildren();
    addFromTemplate("source-template", sourcesRoot);
    status.textContent = "";
  }, 0);
});

form.addEventListener("submit", event => {
  event.preventDefault();
  status.textContent = "";

  if (!form.reportValidity()) return;

  const submissionType = value("submission_type");
  const relatedIds = [...new Set(splitLines(value("related_record_ids")))];
  const sources = readSources();
  const proposedRelations = readRelations();
  const riskFlags = [...document.querySelectorAll('input[name="risk_flags"]:checked')].map(item => item.value);

  if (relatedIds.length > 100 || sources.length > 100 || proposedRelations.length > 100) {
    showError("Превышен лимит элементов в одном из списков (максимум 100).");
    return;
  }
  if (relatedIds.some(id => id.length > 300)) {
    showError("Каждый ID связанной записи должен содержать не более 300 символов.");
    return;
  }
  if (sources.some(source => (source.creators || []).length > 50 ||
    (source.creators || []).some(creator => creator.length > 300)
  )) {
    showError("У источника можно указать не более 50 авторов/создателей, по 300 символов на каждого.");
    return;
  }
  if (relatedIds.length !== splitLines(value("related_record_ids")).length) {
    showError("В списке связанных ID есть дубликаты. Оставьте каждый ID только один раз.");
    return;
  }
  if (sources.some(source => !source.title || source.title.length < 2 || !source.supports || source.supports.length < 5)) {
    showError("У каждого добавленного источника должны быть название и описание того, что он подтверждает.");
    return;
  }
  if (submissionType === "correction" && relatedIds.length < 1) {
    showError("Для исправления укажите минимум один ID существующей записи.");
    return;
  }
  if (submissionType === "contradiction" && relatedIds.length < 2) {
    showError("Для противоречия укажите минимум два ID связанных записей.");
    return;
  }
  if (submissionType === "source" && relatedIds.length < 1) {
    showError("Для предложения источника укажите минимум один ID связанной записи.");
    return;
  }
  if (submissionType === "source" && sources.length < 1) {
    showError("Для предложения источника добавьте минимум один источник.");
    return;
  }
  if (submissionType === "relation" && proposedRelations.length < 1) {
    showError("Для предложения связи добавьте минимум одну связь.");
    return;
  }
  if (proposedRelations.some(relation =>
    !relation.source_record_id || !relation.target_record_id ||
    !relation.relation_type || relation.relation_type.length < 2 ||
    !relation.rationale || relation.rationale.length < 10
  )) {
    showError("Проверьте предлагаемую связь: нужны исходный и целевой ID, тип связи и обоснование не короче 10 символов.");
    return;
  }

  const payload = {
    schema_version: "1.0",
    submission_type: submissionType,
    subject_area: value("subject_area"),
    title: value("title"),
    proposal_text: value("proposal_text"),
    rationale: value("rationale"),
    sources,
    evidence_notes: value("evidence_notes"),
    applicability: value("applicability"),
    limitations: value("limitations"),
    uncertainty: value("uncertainty"),
    related_record_ids: relatedIds,
    proposed_relations: proposedRelations,
    contributor_role: value("contributor_role"),
    rights_and_terms_acknowledged: document.getElementById("rights_ack").checked,
    risk_flags: riskFlags
  };
  const topic = value("topic");
  if (topic) payload.topic = topic;

  const blob = new Blob([JSON.stringify(payload, null, 2) + "\n"], {type: "application/json;charset=utf-8"});
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "encyclopedia-contribution-v1.json";
  link.textContent = "Скачать JSON";
  link.style.display = "none";
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
  status.textContent = "JSON сформирован и передан браузеру для скачивания. Это не отправка в редакцию и не подтверждение приёма. Передайте файл по утверждённому каналу, когда он будет опубликован.";
});

addFromTemplate("source-template", sourcesRoot);
