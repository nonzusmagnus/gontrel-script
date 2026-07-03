from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

CORNFLOWER = HexColor('#6495ED')
WHITE = white

output = r'C:\Users\chuks\Desktop\Gontrel\Gontrel_Shes_Still_Scrolling_Script.pdf'
W, H = letter

c = canvas.Canvas(output, pagesize=letter)
c.setTitle("Gontrel \u2014 She's Still Scrolling?")
c.setAuthor("Magnus Forever")
c.setSubject("Cinematic Commercial Script")

def gradient_rect():
    for i in range(int(H)):
        ratio = i / H
        r = 0.39 + ratio * 0.05
        g = 0.58 + ratio * 0.05
        b = 0.93 - ratio * 0.05
        c.setFillColorRGB(r, g, b)
        c.rect(0, i, W, 1, fill=1, stroke=0)

# ─── PAGE 1: COVER ───
gradient_rect()
c.setFillColor(WHITE)
c.setFont('Helvetica-Bold', 9)
c.drawCentredString(W/2, H - 1.8*inch, 'CINEMATIC COMMERCIAL')
c.setFont('Helvetica-Bold', 72)
c.drawCentredString(W/2, H - 3.2*inch, 'GONTREL')
c.setFont('Helvetica', 11)
c.drawCentredString(W/2, H - 3.65*inch, 'A RESTAURANT APP THAT SHOWS YOU WHERE TO EAT')
c.setStrokeColor(WHITE)
c.setLineWidth(1.5)
c.line(W/2 - 30, H - 4.0*inch, W/2 + 30, H - 4.0*inch)
c.setFillColor(WHITE)
c.setFont('Helvetica-Bold', 28)
c.drawCentredString(W/2, H - 4.6*inch, '\u201cShe\u2019s Still Scrolling?\u201d')
meta_y = H - 5.3*inch
for i, (label, val) in enumerate([
    ('CAST', '3 Female Talent'),
    ('RUNTIME', '~40 sec (45 sec max)'),
    ('LOCATIONS', 'Office \u00b7 Exterior \u00b7 Restaurant'),
]):
    c.setFillColorRGB(1, 1, 1, alpha=0.6)
    c.setFont('Helvetica-Bold', 8)
    c.drawCentredString(W/2 - 60, meta_y - i*22, label)
    c.setFillColor(WHITE)
    c.setFont('Helvetica', 10)
    c.drawCentredString(W/2 + 20, meta_y - i*22, val)
box_top = H - 6.6*inch
c.setStrokeColorRGB(1, 1, 1, alpha=0.25)
c.setLineWidth(1)
c.rect(W/2 - 1.8*inch, box_top, 3.6*inch, 0.7*inch, fill=0, stroke=1)
c.setFillColor(WHITE)
c.setFont('Helvetica-Bold', 16)
c.drawCentredString(W/2, box_top + 0.35*inch, '\u201cStop scrolling. Start eating.\u201d')
c.setFont('Helvetica', 9)
c.drawCentredString(W/2, 0.8*inch, 'MAGNUS FOREVER \u00b7 PRODUCTION SCRIPT')
c.showPage()

# ─── PAGE 2+: SCRIPT ───
gradient_rect()
c.setFillColor(WHITE)
c.setFont('Helvetica-Bold', 16)
c.drawCentredString(W/2, H - 0.7*inch, 'GONTREL \u2014 \u201cShe\u2019s Still Scrolling?\u201d')
c.setFont('Helvetica', 9)
c.drawCentredString(W/2, H - 1.0*inch, 'PRODUCTION SCRIPT')
c.setStrokeColorRGB(1, 1, 1, alpha=0.2)
c.line(0.8*inch, H - 1.15*inch, W - 0.8*inch, H - 1.15*inch)

left = 0.85*inch
right = W - 0.85*inch
tw = right - left

scene_data = [
    ('scene_num', 'SCENE 1'),
    ('heading', 'Office (Int.) \u2014 End of Day'),
    ('action', 'Desks, laptops closing, that \u201cday\u2019s done\u201d energy \u2014 bags being packed, one girl stretching, casual post-work chat as they wind down.'),
    ('char', 'GIRL A  (white, packing up, a little tired/wistful)'),
    ('dialogue', '\u201cI really want to go somewhere nice to eat.\u201d'),
    ('char', 'GIRL B  (Black, glancing over from her desk)'),
    ('dialogue', '\u201cJust check TikTok.\u201d'),
    ('action', 'Girl A opens TikTok, starts scrolling. Quick flash-cut of her still scrolling \u2014 no lingering.'),
    ('char', 'GIRL C  (white, grabbing her bag, noticing)'),
    ('dialogue', '\u201cShe has\u2026 been scrolling for the past 30 minutes!\u201d'),
    ('char', 'GIRL B'),
    ('dialogue', '\u201cWhat about Gontrel?\u201d'),
    ('char', 'GIRL A  (not looking up)'),
    ('dialogue', '\u201cWhat\u2019s that?\u201d'),
    ('char', 'GIRL C'),
    ('dialogue', '\u201cOh, it\u2019s the app that shows you exactly where to eat. No scrolling forever.\u201d'),
    ('char', 'GIRL A  (genuinely surprised)'),
    ('dialogue', '\u201cHow have I never heard of this before?\u201d'),
    ('action', '3D screen projection moment: the app UI floats up from the phone, scrolling through four restaurant options in space. Low-angle close-up on all three girls\u2019 faces, lit by the screen glow \u2014 gasp lands as the projection hits, not after.'),
    ('char', 'GIRL A'),
    ('dialogue', '\u201cThat\u2019s it, that\u2019s the one.\u201d'),
    ('spacer', None),
    ('scene_num', 'SCENE 2'),
    ('heading', 'Office / Transition (Int.) \u2014 Quick Montage'),
    ('action', 'Quick cuts: grabbing bags, coats, mirror check, heading for the door \u2014 fast, energetic, minimal dialogue.'),
    ('spacer', None),
    ('scene_num', 'SCENE 3'),
    ('heading', 'Exterior \u2192 Restaurant Entrance'),
    ('action', 'Walking up together, straight to the door. Kept minimal \u2014 a beat or two, no dialogue.'),
    ('spacer', None),
    ('scene_num', 'SCENE 4'),
    ('heading', 'Interior Restaurant'),
    ('char', 'OWNER / WAITRESS / CHEF'),
    ('dialogue', '\u201cWe\u2019re doing a survey \u2014 how did you find us?\u201d'),
    ('char', 'ALL THREE  (in unison)'),
    ('dialogue', '\u201cGontrel!\u201d'),
    ('action', '(mildly confused, polite) \u201cOh, nice.\u201d'),
    ('spacer', None),
    ('scene_num', 'CLOSING SHOT'),
    ('heading', 'Restaurant Table'),
    ('action', 'They settle into their seats, laughing, relaxed. Foreground composition: phone resting on the table, Gontrel app visible on screen, restaurant scene softly out of focus behind it.'),
    ('char', '\u201cStop scrolling. Start eating.\u201d'),
    ('spacer', None),
    ('note', None),
]

y = H - 1.5*inch

def new_page():
    global y
    c.showPage()
    gradient_rect()
    c.setFillColor(WHITE)
    c.setFont('Helvetica-Bold', 16)
    c.drawCentredString(W/2, H - 0.7*inch, 'GONTREL \u2014 \u201cShe\u2019s Still Scrolling?\u201d (cont.)')
    c.setStrokeColorRGB(1, 1, 1, alpha=0.2)
    c.line(0.8*inch, H - 1.0*inch, W - 0.8*inch, H - 1.0*inch)
    y = H - 1.4*inch

for stype, text in scene_data:
    if y < 0.9*inch:
        new_page()

    if stype == 'spacer':
        y -= 0.15*inch
    elif stype == 'note':
        y -= 0.15*inch
        note_lines = [
            'Production note: Scene 1 relocated to an office end-of-day',
            'setting per client direction \u2014 gives Girl A\u2019s opening line',
            'natural motivation and sets up a wardrobe contrast (office',
            'wear \u2192 going-out look) heading into Scene 2.',
            'Pacing tightened throughout to land at ~40s scripted,',
            'keeping buffer under the 45s hard cap once edited.',
        ]
        c.setFillColorRGB(0, 0, 0, alpha=0.1)
        c.roundRect(left - 0.15*inch, y - len(note_lines)*11 - 0.2*inch, tw + 0.3*inch, len(note_lines)*11 + 0.35*inch, 6, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica', 8.5)
        for line in note_lines:
            c.drawString(left, y, line)
            y -= 11
        y -= 0.15*inch
        c.setFont('Helvetica-Bold', 8.5)
        c.drawCentredString(W/2, y, 'MAGNUS FOREVER \u00b7 PRODUCTION SCRIPT')
        y -= 0.2*inch
    elif stype == 'scene_num':
        c.setFillColorRGB(1, 1, 1, alpha=0.5)
        c.setFont('Helvetica-Bold', 7.5)
        c.drawString(left, y, text)
        y -= 12
    elif stype == 'heading':
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 9.5)
        c.drawString(left, y, text.upper())
        c.setStrokeColorRGB(1, 1, 1, alpha=0.15)
        c.setLineWidth(1)
        c.line(left, y - 4, right, y - 4)
        y -= 16
    elif stype == 'action':
        c.setFillColorRGB(1, 1, 1, alpha=0.85)
        c.setFont('Helvetica', 9)
        lines = simpleSplit(text, 'Helvetica', 9, tw)
        for line in lines:
            c.drawString(left, y, line)
            y -= 12
        y -= 2
    elif stype == 'char':
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 9.5)
        c.setStrokeColorRGB(1, 1, 1, alpha=0.3)
        c.setLineWidth(2)
        c.line(left - 0.1*inch, y - 1, left - 0.1*inch, y + 8)
        c.drawString(left, y, text)
        y -= 14
    elif stype == 'dialogue':
        c.setFillColorRGB(1, 1, 1, alpha=0.85)
        c.setFont('Helvetica', 9)
        lines = simpleSplit(text, 'Helvetica', 9, tw - 0.4*inch)
        for line in lines:
            c.drawString(left + 0.3*inch, y, line)
            y -= 12
        y -= 1

c.save()
print("PDF created successfully")
