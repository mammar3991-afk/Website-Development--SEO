/* Octavebytes v2 prototype. No dependencies. */
(function () {
  "use strict";
  var CFG = window.OB_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- analytics layer (events fire into dataLayer; GA4 loads only after consent) ---------- */
  window.dataLayer = window.dataLayer || [];
  function track(name, params) {
    var p = params || {}; p.event = name; p.page_path = location.pathname;
    window.dataLayer.push(p);
    if (window.gtag) { var g = Object.assign({}, p); delete g.event; window.gtag("event", name, g); } // GA4 (set up after consent)
  }
  function loadAnalytics() {
    if (window.__obGA) return;
    window.__obGA = true;
    if (CFG.portalId) { // HubSpot tracking (attributes visits to contacts); loads only after consent
      var h = document.createElement("script"); h.async = true; h.defer = true;
      h.src = "https://js.hs-scripts.com/" + encodeURIComponent(CFG.portalId) + ".js"; document.head.appendChild(h);
    }
    if (CFG.clarityId) { // Microsoft Clarity session replays; loads only after consent
      (function (c, l, a, r, i, t, y) { c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); }; t = l.createElement(r); t.async = 1; t.src = "https://www.clarity.ms/tag/" + i; y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y); })(window, document, "clarity", "script", CFG.clarityId);
    }
    if (!CFG.ga4Id) return;
    var s = document.createElement("script"); s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(CFG.ga4Id);
    document.head.appendChild(s);
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date()); window.gtag("config", CFG.ga4Id, { anonymize_ip: true });
  }

  /* ---------- consent ---------- */
  var consentEl = $("#consent");
  var choice = store.get("ob_consent");
  if (choice === "all") loadAnalytics();
  if (!choice && consentEl) consentEl.hidden = false;
  function setConsent(v) {
    store.set("ob_consent", v); if (consentEl) consentEl.hidden = true;
    if (v === "all") loadAnalytics();
  }
  var a = $("#consentAllow"), d = $("#consentDeny");
  if (a) a.addEventListener("click", function () { setConsent("all"); });
  if (d) d.addEventListener("click", function () { setConsent("essential"); });

  /* ---------- review mode (prototype only) ---------- */
  var bar = $("#reviewbar"), toggle = $("#reviewToggle");
  var qs = new URLSearchParams(location.search);
  var mode = qs.get("review") || store.get("ob_review") || "on";
  if (bar && toggle) {
    bar.hidden = false;
    $("#flagcount").textContent = $$("[data-flag]").length;
    var apply = function (on) { document.body.classList.toggle("review-off", !on); toggle.checked = on; store.set("ob_review", on ? "on" : "off"); };
    apply(mode !== "off");
    toggle.addEventListener("change", function () { apply(toggle.checked); });
  }

  /* ---------- colour option switcher (prototype only) ---------- */
  var themeSel = $("#themeSel");
  if (themeSel) {
    var setTheme = function (t) { document.documentElement.setAttribute("data-theme", t); themeSel.value = t; store.set("ob_theme", t); };
    themeSel.value = document.documentElement.getAttribute("data-theme") || "a";
    themeSel.addEventListener("change", function () { setTheme(themeSel.value); });
    $$("[data-apply]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); setTheme(b.getAttribute("data-apply")); window.scrollTo({ top: 0, behavior: "smooth" }); }); });
  }

  /* ---------- navigation ---------- */
  var menuBtn = $("#menuBtn"), nav = $("#primaryNav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open"); menuBtn.setAttribute("aria-expanded", open);
    });
  }
  var toggles = $$(".nav__toggle");
  function closeAll(except) { toggles.forEach(function (t) { if (t !== except) t.setAttribute("aria-expanded", "false"); }); }
  toggles.forEach(function (t) {
    t.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = t.getAttribute("aria-expanded") === "true";
      closeAll(t); t.setAttribute("aria-expanded", String(!open));
    });
    t.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); t.setAttribute("aria-expanded", "true"); var f = $("a", t.nextElementSibling); if (f) f.focus(); }
    });
  });
  $$(".nav__menu").forEach(function (m) {
    m.addEventListener("keydown", function (e) {
      var links = $$("a", m), i = links.indexOf(document.activeElement);
      if (e.key === "ArrowDown") { e.preventDefault(); (links[i + 1] || links[0]).focus(); }
      if (e.key === "ArrowUp") { e.preventDefault(); (links[i - 1] || links[links.length - 1]).focus(); }
      if (e.key === "Escape") { var t = m.previousElementSibling; t.setAttribute("aria-expanded", "false"); t.focus(); }
    });
  });
  document.addEventListener("click", function () { closeAll(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeAll(); });

  /* ---------- click tracking ---------- */
  document.addEventListener("click", function (e) {
    var el = e.target.closest("a,button"); if (!el) return;
    if (el.hasAttribute("data-cta")) track("cta_click", { label: el.getAttribute("data-cta"), text: (el.textContent || "").trim().slice(0, 60) });
    if (el.hasAttribute("data-marketplace")) track("marketplace_click", { marketplace: el.getAttribute("data-marketplace") });
    if (el.tagName === "A" && /\/resources\/docs\//.test(el.getAttribute("href") || "")) track("docs_click", {});
  });
  if (document.body.classList.contains("page-pricing")) track("pricing_view", {});

  /* ---------- forms ---------- */
  function utm() {
    var o = {}; ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"].forEach(function (k) { var v = qs.get(k); if (v) o[k] = v; });
    return o;
  }
  var EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  function validate(form) {
    var ok = true, first = null;
    $$(".field", form).forEach(function (f) {
      var inp = $("input,select,textarea", f); if (!inp) return;
      var bad = false;
      if (inp.type === "checkbox" && inp.required) bad = !inp.checked;
      else if (inp.required && !String(inp.value).trim()) bad = true;
      else if (inp.type === "email" && inp.value && !EMAIL.test(inp.value)) bad = true;
      f.classList.toggle("is-invalid", bad);
      if (bad) { ok = false; if (!first) first = inp; }
    });
    if (first) first.focus();
    return ok;
  }
  $$("form[data-form]").forEach(function (form) {
    var name = form.getAttribute("data-form"), started = false;
    form.addEventListener("focusin", function () { if (!started) { started = true; track("form_start", { form_id: name }); } });
    form.setAttribute("novalidate", "");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if ($(".trap input", form) && $(".trap input", form).value) return; // honeypot
      if (!validate(form)) return;
      var fd = new FormData(form), fields = [], plain = {};
      fd.forEach(function (v, k) {
        if (k === "website") return;
        plain[k] = plain[k] ? plain[k] + ";" + v : v; // multi-checkbox values joined with ";" (HubSpot format)
      });
      Object.keys(plain).forEach(function (k) {
        if (k === "consent" || plain[k] === "") return; // consent goes via legalConsentOptions; empty values are omitted
        fields.push({ name: k, value: String(plain[k]) });
      });
      var ctx = Object.assign({ source_page: location.pathname, referrer: document.referrer || "" }, utm());
      Object.keys(ctx).forEach(function (k) { fields.push({ name: k, value: ctx[k] }); });
      var defs = (CFG.formDefaults || {})[name] || {};
      Object.keys(defs).forEach(function (k) { if (!plain[k]) fields.push({ name: k, value: defs[k] }); });
      var intent = plain.intent || name;
      track("form_submit", { form_id: name, intent: intent });
      var trackLead = function () { // counted only after HubSpot accepts the submission
        track("generate_lead", { form_id: name, intent: intent });
        if (name === "trial" || name === "estimate") track(name === "estimate" ? "estimate_request" : "trial_request", {});
        if (name === "aws") track("aws_opportunity", {});
        if (name === "partner") track("partner_enquiry", {});
      };
      var guid = (CFG.formGuids || {})[name];
      var done = function (live) { showThanks(form, live, { form: name, fields: plain, context: ctx }); };
      var btn = $("button[type=submit]", form); if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      if (CFG.portalId && guid) {
        fetch("https://api.hsforms.com/submissions/v3/integration/submit/" + CFG.portalId + "/" + guid, {
          method: "POST", headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            fields: fields, context: { pageUri: location.href, pageName: document.title },
            legalConsentOptions: { consent: { consentToProcess: true, text: "I agree to be contacted about this request." } }
          })
        }).then(function (r) {
          if (!r.ok) throw new Error("HTTP " + r.status);
          trackLead();
          done(true);
        }).catch(function () {
          if (btn) { btn.disabled = false; btn.textContent = "Try again"; }
          var err = $(".form-error", form); if (err) { err.hidden = false; }
        });
      } else {
        done(false); // prototype: no HubSpot form GUID configured yet
      }
    });
  });
  function showThanks(form, live, payload) {
    var t = document.getElementById(form.getAttribute("data-thanks"));
    form.hidden = true;
    if (t) {
      t.hidden = false;
      var first = $("[data-first-name]", t); if (first && payload.fields.firstname) first.textContent = payload.fields.firstname;
      if (!live) {
        var box = document.createElement("div"); box.className = "mockbox";
        box.innerHTML = "<strong>Prototype mode:</strong> nothing was sent. Once a HubSpot form GUID is added to <code>site.json</code>, this same submit posts to HubSpot and creates the contact and deal. Payload that would be sent:<pre></pre>";
        $("pre", box).textContent = JSON.stringify(payload, null, 2);
        t.appendChild(box);
      }
      t.setAttribute("tabindex", "-1"); t.focus(); t.scrollIntoView({ block: "center" });
    }
  }
  // preselect from query string (?intent=estimate, ?crm=Other)
  var trial = $('form[data-form="trial"]');
  if (trial) {
    var intent = qs.get("intent"); if (intent && $('[name="intent"]', trial)) $('[name="intent"]', trial).value = intent;
    var addon = qs.get("addon"); if (addon === "call-intelligence") { var ciBox = $('input[name="channels"][value="Transcripts and AI summaries"]', trial); if (ciBox) ciBox.checked = true; }
    var crm = qs.get("crm"); if (crm && $('[name="crm_used"]', trial)) $('[name="crm_used"]', trial).value = crm;
  }

  var contact = $('form[data-form="contact"]');
  if (contact && qs.get("topic") && $('[name="topic"]', contact)) $('[name="topic"]', contact).value = qs.get("topic");

  /* ---------- pricing estimator ---------- */
  var est = $("#estimator");
  if (est) {
    var P = { price: +est.dataset.price, addon: +est.dataset.addon, setup: +est.dataset.setup, cap: +est.dataset.cap };
    var agents = $("#est-agents"), addonBox = $("#est-addon"), out = $("#est-out"), msg = $("#est-msg");
    var money = function (n) { return "$" + n.toLocaleString("en-US"); };
    var calc = function () {
      var n = Math.max(1, Math.min(1000, parseInt(agents.value, 10) || 0));
      var perAgent = P.price + (addonBox.checked ? P.addon : 0);
      var monthly = n * perAgent;
      var setup = n <= P.cap ? P.setup : null;
      var rateLine = addonBox.checked
        ? money(P.price) + " + " + money(P.addon) + " call intelligence"
        : money(P.price);
      out.innerHTML =
        "<dl>" +
        "<dt>" + n + (n === 1 ? " agent" : " agents") + " × " + rateLine + "</dt><dd>" + money(monthly) + " / month</dd>" +
        "<dt>Guided setup (one time)</dt><dd>" + (setup !== null ? money(setup) : "Quoted") + "</dd>" +
        "<dt class='est__total'>First-year total</dt><dd class='est__total'>" + (setup !== null ? money(monthly * 12 + setup) : money(monthly * 12) + " + setup") + "</dd></dl>";
      msg.textContent = n >= 50 ? "50 or more agents: volume pricing is available. Ask us." : (n > P.cap ? "Setup for more than " + P.cap + " agents is quoted before we start." : "");
    };
    est.addEventListener("input", calc); calc();
  }
})();
