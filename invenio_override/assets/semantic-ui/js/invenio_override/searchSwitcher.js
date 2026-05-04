// Copyright (C) 2020-2026 Graz University of Technology.
// invenio-override is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import $ from "jquery";

const STORAGE_KEY = "search-switcher-q";

function saveQuery(q) {
  try { sessionStorage.setItem(STORAGE_KEY, q); } catch (_) {}
}

function getStoredQuery() {
  try { return sessionStorage.getItem(STORAGE_KEY) || ""; } catch (_) { return ""; }
}

function queryFromURL(urlStr) {
  try {
    const search = (urlStr || "").includes("?") ? urlStr.split("?")[1] : "";
    return new URLSearchParams(search).get("q") || "";
  } catch (_) {
    return "";
  }
}

export function initSearchSwitcher() {
  const form = document.getElementById("search-switcher-form");
  if (!form) return;

  const sel = document.getElementById("search-switcher-type");
  const inp = document.getElementById("search-switcher-input");
  const clr = document.getElementById("search-switcher-clear");
  const $sel = $(sel);

  function getValue() { return $sel.dropdown("get value") || ""; }
  function syncAction() { form.action = getValue(); }
  function syncClear() { clr.style.display = inp.value ? "flex" : "none"; }

  function syncFromURL(urlStr) {
    const q = queryFromURL(urlStr);
    inp.value = q;
    saveQuery(q);
    syncClear();
  }

  if (!inp.value) inp.value = getStoredQuery();

  let initializing = true;
  $sel.dropdown({
    onChange: function (value) {
      if (initializing) return;
      form.action = value;
      saveQuery(inp.value);
      form.submit();
    },
  });

  const activeItem = sel.querySelector(".item.active");
  const firstItem  = sel.querySelector(".item");
  const initValue  = (activeItem || firstItem || {}).dataset.value;
  if (initValue) $sel.dropdown("set selected", initValue);
  initializing = false;

  const origPushState = history.pushState.bind(history);
  history.pushState = function (state, title, url) {
    origPushState(state, title, url);
    if (url) syncFromURL(url);
  };
  window.addEventListener("popstate", function () { syncFromURL(location.href); });

  form.addEventListener("submit", function () { saveQuery(inp.value); syncAction(); });

  clr.addEventListener("click", function () {
    inp.value = "";
    saveQuery("");
    syncAction();
    form.submit();
  });

  inp.addEventListener("input", function () { saveQuery(inp.value); syncClear(); });

  syncAction();
  syncClear();
}
