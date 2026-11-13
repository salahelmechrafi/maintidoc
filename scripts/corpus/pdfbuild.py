# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
                                TableStyle, Image, PageBreak, ListFlowable, ListItem, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", F + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", F + "DejaVuSans-Oblique.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVB")

S = {
    "p": ParagraphStyle("p", fontName="DV", fontSize=9.5, leading=13.5, spaceAfter=5),
    "h1": ParagraphStyle("h1", fontName="DVB", fontSize=14, leading=18, spaceBefore=4, spaceAfter=8, textColor=colors.HexColor("#1b3a5c")),
    "h2": ParagraphStyle("h2", fontName="DVB", fontSize=11, leading=14, spaceBefore=6, spaceAfter=4, textColor=colors.HexColor("#1b3a5c")),
    "cap": ParagraphStyle("cap", fontName="DVI", fontSize=8.5, leading=11, alignment=1, spaceAfter=8),
    "cell": ParagraphStyle("cell", fontName="DV", fontSize=8, leading=10),
    "cellb": ParagraphStyle("cellb", fontName="DVB", fontSize=8, leading=10, textColor=colors.white),
    "warn": ParagraphStyle("warn", fontName="DVB", fontSize=9, leading=12, textColor=colors.HexColor("#7a0000")),
}


def _flow(b):
    k = b[0]
    if k in ("h1", "h2", "p"):
        return [Paragraph(b[1], S[k])]
    if k in ("ul", "ol"):
        items = [ListItem(Paragraph(t, S["p"]), leftIndent=12) for t in b[1]]
        return [ListFlowable(items, bulletType="bullet" if k == "ul" else "1", start=None if k == "ul" else 1,
                             bulletFontName="DV", bulletFontSize=8, leftIndent=14)]
    if k == "table":
        cap, head, rows = b[1], b[2], b[3]
        widths = b[4] if len(b) > 4 else None
        data = [[Paragraph(h, S["cellb"]) for h in head]] + [[Paragraph(str(c), S["cell"]) for c in r] for r in rows]
        t = Table(data, colWidths=widths, repeatRows=1)
        t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1b3a5c")),
                               ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                               ("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f1f4f8")])]))
        out = [t]
        if cap:
            out.append(Paragraph(cap, S["cap"]))
        return [KeepTogether(out)] if len(rows) < 14 else out
    if k == "fig":
        path, cap = b[1], b[2]
        wcm = b[3] if len(b) > 3 else 14
        w, h = PILImage.open(path).size
        img = Image(path, width=wcm * cm, height=wcm * cm * h / w)
        return [KeepTogether([img, Paragraph(cap, S["cap"])])]
    if k == "warn":
        t = Table([[Paragraph("⚠ " + b[1], S["warn"])]], colWidths=[17 * cm])
        t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1.2, colors.HexColor("#c00000")),
                               ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fdecea")),
                               ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
        return [t, Spacer(1, 6)]
    if k == "sp":
        return [Spacer(1, b[1])]
    if k == "pb":
        return [PageBreak()]
    raise ValueError(k)


def build(doc, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    npages = 1 + sum(1 for b in doc["blocks"] if b[0] == "pb")
    lang = doc.get("lang", "fr")
    head = doc.get("entete", "FICTIA Industrie — documentation technique" if lang == "fr" else "FICTIA Industrie — technical documentation")
    synth = "Document synthétique à usage pédagogique (projet MaintiDoc) — marque et données fictives" if lang == "fr" \
        else "Synthetic document for teaching purposes (MaintiDoc project) — fictitious brand and data"

    def deco(c, d):
        c.saveState()
        c.setFillColor(colors.HexColor("#1b3a5c")); c.rect(0, A4[1] - 1.3 * cm, A4[0], 1.3 * cm, fill=1, stroke=0)
        c.setFillColor(colors.white); c.setFont("DVB", 9)
        c.drawString(1.5 * cm, A4[1] - 0.85 * cm, head)
        c.setFont("DV", 8); c.drawRightString(A4[0] - 1.5 * cm, A4[1] - 0.85 * cm, doc["ref"])
        c.setFillColor(colors.grey); c.setFont("DVI", 7)
        c.drawString(1.5 * cm, 1.0 * cm, synth)
        c.setFillColor(colors.black); c.setFont("DV", 8)
        pg = "Page" if lang == "fr" else "Page"
        c.drawRightString(A4[0] - 1.5 * cm, 1.0 * cm, f"{doc['ref_court']} — {pg} {d.page} / {npages}")
        c.restoreState()

    d = BaseDocTemplate(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=1.8 * cm,
                        title=doc["titre"], author="FICTIA (fictif) - corpus MaintiDoc", subject=doc["id"])
    fr = Frame(d.leftMargin, d.bottomMargin, d.width, d.height, id="f")
    d.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=deco)])
    story = []
    for b in doc["blocks"]:
        story += _flow(b)
    d.build(story)
    return npages
