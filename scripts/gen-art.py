#!/usr/bin/env python3
"""Generate the SLOP8815 hero and social card as two-ink SVGs."""

INK1 = "#b97d1c"  # slop primary
INK2 = "#8a5c13"  # slop secondary, used as the misregistered second pass
BG = "#111010"


def browser(x, y, w, h, stroke, sw, dots=True):
    """One flat browser window outline."""
    bar = max(10.0, h * 0.09)
    p = [
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{h*0.035:.1f}" '
        f'fill="none" stroke="{stroke}" stroke-width="{sw:.1f}"/>',
        f'<line x1="{x:.1f}" y1="{y+bar:.1f}" x2="{x+w:.1f}" y2="{y+bar:.1f}" '
        f'stroke="{stroke}" stroke-width="{sw:.1f}"/>',
    ]
    if dots and bar > 16:
        r = bar * 0.16
        for i in range(3):
            cx = x + bar * 0.55 + i * bar * 0.5
            p.append(f'<circle cx="{cx:.1f}" cy="{y+bar/2:.1f}" r="{r:.1f}" fill="{stroke}"/>')
    return "".join(p)


def nest(cx, cy, w, h, levels, stroke, sw):
    """Concentric browser windows, each inset inside the last."""
    out = []
    for i in range(levels):
        k = 0.72**i
        ww, hh = w * k, h * k
        # sit each child just below its parent's title bar
        oy = sum((h * 0.72**j) * 0.045 for j in range(i))
        out.append(
            browser(cx - ww / 2, cy - hh / 2 + oy, ww, hh, stroke, max(1.2, sw * (0.86**i)))
        )
    return "".join(out)


def hero(path, w=2560, h=1086):
    cx, cy = w / 2, h / 2
    bw, bh = 1580, 760
    body = (
        f'<g opacity="0.85" transform="translate(14,11)">{nest(cx, cy, bw, bh, 7, INK2, 7)}</g>'
        f"{nest(cx, cy, bw, bh, 7, INK1, 7)}"
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
        f'<rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>'
    )
    open(path, "w").write(svg)


def card(path, w=1200, h=630):
    cx, cy = w * 0.70, h * 0.52
    art = (
        f'<g opacity="0.8" transform="translate(7,6)">{nest(cx, cy, 620, 420, 6, INK2, 4)}</g>'
        f"{nest(cx, cy, 620, 420, 6, INK1, 4)}"
    )
    text = (
        f'<text x="72" y="250" font-family="JetBrains Mono" font-size="70" font-weight="700" '
        f'fill="{INK1}">SLOP8815</text>'
        f'<text x="72" y="320" font-family="JetBrains Mono" font-size="35" fill="#e8e4dc">'
        f"How to Run Anything</text>"
        f'<text x="72" y="368" font-family="JetBrains Mono" font-size="35" fill="#e8e4dc">'
        f"in the Browser</text>"
        f'<text x="72" y="452" font-family="JetBrains Mono" font-size="23" fill="#6b6154">'
        f"Slop University</text>"
        f'<line x1="72" y1="180" x2="205" y2="180" stroke="{INK1}" stroke-width="7"/>'
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
        f'<rect width="{w}" height="{h}" fill="{BG}"/>{art}{text}</svg>'
    )
    open(path, "w").write(svg)


hero("/tmp/opencode/hero.svg")
card("/tmp/opencode/card.svg")
print("ok")
