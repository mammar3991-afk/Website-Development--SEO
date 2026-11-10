#!/usr/bin/env python3
"""Measure WCAG contrast for every colour theme defined in src/assets/css/site.css.

Text pairs must reach 4.5:1 (WCAG 1.4.3). UI boundaries and focus rings must reach 3:1 (1.4.11).
    python3 tools/contrast.py          print a table per theme, exit 1 on any failure
The build imports report() to print the same numbers on /theme-preview/.
"""
import re, sys
from pathlib import Path

CSS = Path(__file__).resolve().parent.parent / "src" / "assets" / "css" / "site.css"
NAMES = {"a": "Current blue", "b": "Indigo and amber", "c": "Teal", "d": "Graphite and orange"}
WHITE, RED, MOCK_GREEN, RED_BTN = "#FFFFFF", "#B42318", "#7EE2B8", "#B42318"


def lum(h):
    h = h.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def themes():
    css = CSS.read_text()
    blocks = {}
    for m in re.finditer(r'(:root,\[data-theme="a"\]|\[data-theme="([bcd])"\])\{(.*?)\}', css, re.S):
        key = "a" if m.group(1).startswith(":root") else m.group(2)
        blocks[key] = dict(re.findall(r"--([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})", m.group(3)))
    base = blocks["a"]
    return {k: {**base, **v} for k, v in blocks.items()}


def pairs(t):
    T, U = 4.5, 3.0
    return [
        # (label, foreground, background, required)
        ("Body text on white", t["ink"], WHITE, T),
        ("Body text on grey sections", t["ink"], t["surface"], T),
        ("Body text on tinted sections", t["ink"], t["tint"], T),
        ("Secondary text on white", t["slate"], WHITE, T),
        ("Secondary text on grey sections", t["slate"], t["surface"], T),
        ("Secondary text on tinted sections", t["slate"], t["tint"], T),
        ("Links on white", t["blue"], WHITE, T),
        ("Links on grey sections", t["blue"], t["surface"], T),
        ("Eyebrow labels on tint", t["blue-dark"], t["tint"], T),
        ("Link hover on white", t["blue-dark"], WHITE, T),
        ("Primary button text", WHITE, t["blue"], T),
        ("Primary button hover text", WHITE, t["blue-dark"], T),
        ("Secondary button text", t["ink"], WHITE, T),
        ("'Included' ticks and text on white", t["ok"], WHITE, T),
        ("'Included' ticks on highlighted column", t["ok"], t["tint"], T),
        ("Headings on dark sections", WHITE, t["dark"], T),
        ("Body text on dark sections", t["muted-dark"], t["dark"], T),
        ("Links on dark sections", t["link-dark"], t["dark"], T),
        ("Headings on dark cards", WHITE, t["dark-2"], T),
        ("Body text on dark cards", t["muted-dark"], t["dark-2"], T),
        ("Links on dark cards", t["link-dark"], t["dark-2"], T),
        ("Product mock: text on dark panel", t["muted-dark"], t["ink"], T),
        ("Product mock: 'Connected' label", MOCK_GREEN, t["ink"], T),
        ("Product mock: button labels", WHITE, t["dark-2"], T),
        ("Footer: headings and links", WHITE, t["footer-bg"], T),
        ("Footer: body text", t["muted-dark"], t["footer-bg"], T),
        ("Footer: small print", t["footer-muted"], t["footer-bg"], T),
        ("Form errors on white", RED, WHITE, T),
        ("End-call button text (mock)", WHITE, RED_BTN, T),
        # UI components (3:1)
        ("Form field borders", t["input-line"], WHITE, U),
        ("Secondary button borders", t["line-strong"], WHITE, U),
        ("Focus ring on white", t["blue"], WHITE, U),
        ("Focus ring on tint", t["blue"], t["tint"], U),
        ("Focus ring on dark sections", t["link-dark"], t["dark"], U),
        ("Focus ring in footer", t["link-dark"], t["footer-bg"], U),
        ("Outline button border on dark", t["dark-line-strong"], t["dark"], U),
    ]


def report():
    out = {}
    for key, t in themes().items():
        rows = []
        for label, fg, bg, need in pairs(t):
            r = ratio(fg, bg)
            rows.append((label, fg, bg, r, need, r >= need))
        out[key] = rows
    return out


if __name__ == "__main__":
    bad = 0
    for key, rows in report().items():
        fails = [r for r in rows if not r[5]]
        print(f"Option {key.upper()} · {NAMES[key]}: {len(rows) - len(fails)}/{len(rows)} pass; lowest {min(r[3] for r in rows):.2f}:1")
        for label, fg, bg, r, need, ok in fails:
            bad += 1
            print(f"   FAIL {label}: {fg} on {bg} = {r:.2f}:1 (need {need})")
    print(f"\n{bad} failing pair(s)")
    sys.exit(1 if bad else 0)
