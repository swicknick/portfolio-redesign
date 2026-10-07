"""Build the resume in three styles from one content source.

    python3 career/resume-styles/build.py

Writes <style>.html next to this file. Print them to PDF with Chrome
(or see the README in this folder).
"""

from html import escape
from pathlib import Path

OUT = Path(__file__).parent

NAME = "Nicholas Rode"
TITLE = "Product & Interactive Motion Designer"
CONTACT = ["theniceguynick@gmail.com", "281.794.1242", "Vancouver, WA"]
LINKS = [("Portfolio", "https://nicholasrode.framer.website/"), ("Motion Reel", "https://vimeo.com/1189183155")]

SUMMARY = (
    "AI-native motion engineer and interactive motion designer with 5+ years of experience shipping motion "
    "for B2B SaaS and tech brands. I turn complex products into clear, engaging motion and work AI-first every "
    "day, using Claude Code to prototype, build, and ship work that is production-ready, fast, and accessible. "
    "I also build AI-powered tools that remove friction between design and development."
)

SKILLS = [
    ("AI workflow", "Claude Code (daily, AI-first), AI-assisted prototyping and production code, building AI skills and Figma plugins, design-to-code automation"),
    ("Motion & interaction", "Rive (state machines, interactive components), After Effects, Lottie/Bodymovin, UI animation, 2D/3D animation, compositing"),
    ("Design", "Figma (including motion), Illustrator, UI/UX design, design systems, interactive prototyping"),
    ("Production & performance", "Rive web runtimes (React, Canvas, WebGL2), Lottie JSON delivery, WebGL shaders, Lighthouse performance tuning, reduced-motion accessibility, developer handoff"),
]

JOBS = [
    {
        "role": "Motion Engineer",
        "org": "Webstacks",
        "note": "B2B web design and development agency · Promoted from Motion Designer, Oct 2026",
        "dates": "Jan 2025 – Present",
        "bullets": [
            "Shipped interactive motion, animation, and illustration for Gong and Fireworks AI, including product UI motion for Fireworks AI",
            "Work AI-first with Claude Code every day to prototype interactions, write production animation code, and automate design-to-dev handoff",
            "Built 4 interactive Rive product demos for Deepgram's AI voice platform: voice-to-text, voice avatars, assistant states, and a Slack integration walkthrough",
            "Designed a 10-piece Rive animation system for Shep's rebrand, turning automation, security, and scale into one visual language",
            "Choose and optimize animation runtimes for mobile web performance",
        ],
    },
    {
        "role": "Junior Designer (Product UI & Motion)",
        "org": "Variable Medium",
        "note": "",
        "dates": "Jan 2021 – Dec 2024",
        "bullets": [
            "Designed the desktop and mobile peer-to-peer trading app for Evaluate, from interactive prototypes for user testing through launch, plus its marketing site and onboarding video",
            "Designed trade and chat flows, including asynchronous offers with expiry dates so traders don't need to be online at the same time",
            "Contributed to design system development and created motion that clarified complex product flows",
        ],
    },
    {
        "role": "Freelance Motion Designer & Illustrator",
        "org": "Self-employed",
        "note": "",
        "dates": "2022 – Present",
        "bullets": [
            "Deliver motion graphics, illustration, and web and mobile design for tech, SaaS, and B2B clients",
        ],
    },
]

TOOLS = [
    ("Stroke Center (Figma Community)", "Plugin that converts inside/outside strokes to center for clean Lottie export."),
    ("Design to Webpage", "AI skill that turns Figma designs into working HTML prototypes with interactions and motion."),
    ("Sequence to Shader", "AI-built pipeline that turns After Effects renders into lightweight WebGL shaders."),
    ("Figma → React", "Figma plugin that generates reliable React code from designs."),
]

EDUCATION = [("Art Institute of Seattle", ""), ("Nucamp, Full Stack Web Design", "2020")]

COURSES = [
    ("Rive Masterclass", "advanced interactive animation and state machine design"),
    ("TheMotionMagic, Ultimate Rive Animation Course", "production-level Rive workflows"),
    ("School of Motion, A Motion Design Masterpiece", "principles, process, and motion craft"),
]


def e(s):
    return escape(s)


def links_html():
    return " · ".join(f'<a href="{e(u)}">{e(t)}</a>' for t, u in LINKS)


def jobs_html():
    out = []
    for j in JOBS:
        note = f'<p class="note">{e(j["note"])}</p>' if j["note"] else ""
        items = "".join(f"<li>{e(b)}</li>" for b in j["bullets"])
        out.append(
            f'<div class="job"><div class="job-head"><h3>{e(j["role"])}, <span class="org">{e(j["org"])}</span></h3>'
            f'<span class="dates">{e(j["dates"])}</span></div>{note}<ul>{items}</ul></div>'
        )
    return "".join(out)


def skills_html():
    return "".join(f'<p class="skill"><strong>{e(k)}:</strong> {e(v)}</p>' for k, v in SKILLS)


def tools_html():
    return "".join(f'<p class="tool"><strong>{e(k)}:</strong> {e(v)}</p>' for k, v in TOOLS)


def edu_html():
    return "".join(
        f'<p class="edu"><strong>{e(k)}</strong><span class="dates">{e(v)}</span></p>'
        for k, v in EDUCATION
    )


def courses_html():
    return "".join(f'<p class="course">{e(k)}</p>' for k, _ in COURSES)


BASE_CSS = """
@page { size: letter; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; }
body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 8.5in; min-height: 11in; }
h1, h2, h3, p, ul { margin: 0; }
ul { padding-left: 1.1em; }
a { color: inherit; text-decoration: none; }
"""


def single_column(css, fonts):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{NAME} Resume</title>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>{BASE_CSS}{css}</style></head><body><div class="page">
<header>
  <h1>{e(NAME)}</h1>
  <p class="title">{e(TITLE)}</p>
  <p class="contact">{" · ".join(e(c) for c in CONTACT)} · {links_html()}</p>
</header>
<section><h2>Summary</h2><p class="summary">{e(SUMMARY)}</p></section>
<section><h2>Experience</h2>{jobs_html()}</section>
<section><h2>Tools I've Built</h2>{tools_html()}</section>
<section><h2>Skills</h2>{skills_html()}</section>
<section class="split">
  <div><h2>Education</h2>{edu_html()}</div>
  <div><h2>Courses</h2>{courses_html()}</div>
</section>
</div></body></html>"""


def two_column(css, fonts):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{NAME} Resume</title>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>{BASE_CSS}{css}</style></head><body><div class="page">
<header>
  <h1>{e(NAME)}</h1>
  <p class="title">{e(TITLE)}</p>
</header>
<div class="cols">
  <aside>
    <section><h2>Contact</h2>{"".join(f"<p>{e(c)}</p>" for c in CONTACT)}<p>{links_html()}</p></section>
    <section><h2>Skills</h2>{"".join(f'<div class="skill"><h4>{e(k)}</h4><p>{e(v)}</p></div>' for k, v in SKILLS)}</section>
    <section><h2>Education</h2>{edu_html()}</section>
  </aside>
  <main>
    <section><p class="summary">{e(SUMMARY)}</p></section>
    <section><h2>Experience</h2>{jobs_html()}</section>
    <section><h2>Tools I've Built</h2>{tools_html()}</section>
    <section><h2>Courses</h2>{courses_html()}</section>
  </main>
</div>
</div></body></html>"""


# 1. Swiss minimal: single column, ATS-safe, black + purple accent (your current resume's color)
SWISS = """
body { font-family: 'Inter', Arial, sans-serif; color: #18181b; font-size: 9.2pt; line-height: 1.38; }
.page { padding: 0.45in 0.6in; }
header { border-bottom: 2px solid #18181b; padding-bottom: 12px; margin-bottom: 4px; }
h1 { font-size: 30pt; font-weight: 700; letter-spacing: -0.025em; line-height: 1; }
.title { font-size: 12.5pt; color: #5b21b6; font-weight: 600; margin-top: 6px; }
.contact { color: #52525b; margin-top: 6px; font-size: 9pt; }
.contact a { color: #5b21b6; }
section { margin-top: 10px; }
h2 { font-size: 8.5pt; font-weight: 700; text-transform: uppercase; color: #5b21b6; margin-bottom: 5px; }
.summary { color: #27272a; }
.skill, .tool { margin-bottom: 2px; }
.job { margin-bottom: 6px; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; }
h3 { font-size: 10.5pt; font-weight: 600; }
.org { font-weight: 600; color: #5b21b6; }
.dates { color: #71717a; font-size: 9pt; white-space: nowrap; }
.note { color: #71717a; font-style: italic; font-size: 9pt; }
li { margin-top: 1px; }
.split { display: grid; grid-template-columns: 1fr 1.5fr; gap: 24px; }
.split ul { padding-left: 1em; }
"""

# 2. Product / tech: single column, ATS-safe, mono metadata, navy accent
TECH = """
body { font-family: 'Inter', Arial, sans-serif; color: #0a0a0a; font-size: 9.4pt; line-height: 1.38; }
.page { padding: 0.4in 0.6in 0.35in; }
header { margin-bottom: 6px; }
h1 { font-size: 26pt; font-weight: 700; letter-spacing: -0.025em; line-height: 1; }
.title { font-size: 12pt; color: #1e3a8a; font-weight: 600; margin-top: 6px; }
.contact { font-family: 'JetBrains Mono', monospace; font-size: 8.2pt; color: #27272a; margin-top: 8px; }
.contact a { color: #1e3a8a; font-weight: 500; }
section { margin-top: 9px; padding-top: 8px; border-top: 1px solid #d4d4d8; }
h2 { font-family: 'JetBrains Mono', monospace; font-size: 8pt; font-weight: 500; text-transform: uppercase; color: #3f3f46; margin-bottom: 6px; }
.summary { font-size: 9.8pt; }
.skill, .tool { margin-bottom: 2px; }
.job { margin-bottom: 6px; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; }
h3 { font-size: 10.5pt; font-weight: 600; }
.org { color: #1e3a8a; }
.dates { font-family: 'JetBrains Mono', monospace; font-size: 8pt; color: #3f3f46; white-space: nowrap; }
.note { color: #3f3f46; font-size: 9pt; }
li { margin-top: 1px; }
li::marker { color: #1e3a8a; }
.split { display: grid; grid-template-columns: 1fr 1.5fr; gap: 24px; }
"""

# 3. Editorial two-column: serif display + sidebar. For sending directly to people, not ATS forms.
EDITORIAL = """
body { font-family: 'DM Sans', Arial, sans-serif; color: #1c1917; font-size: 8.8pt; line-height: 1.4; background: #fff; }
.page { display: flex; flex-direction: column; }
header { background: #1c1917; color: #fafaf9; padding: 0.42in 0.6in 0.3in; }
h1 { font-family: 'Instrument Serif', Georgia, serif; font-weight: 400; font-size: 44pt; line-height: 0.95; letter-spacing: -0.01em; }
.title { font-size: 11pt; color: #fdba74; margin-top: 8px; }
.cols { display: grid; grid-template-columns: 2.35in 1fr; flex: 1; }
aside { background: #f5f5f4; padding: 0.3in 0.3in 0.3in 0.6in; }
main { padding: 0.3in 0.6in 0.3in 0.35in; }
section { margin-bottom: 11px; }
h2 { font-family: 'Instrument Serif', Georgia, serif; font-weight: 400; font-size: 15pt; color: #c2410c; margin-bottom: 5px; }
aside p { margin-bottom: 2px; }
aside a { color: #c2410c; }
.skill { margin-bottom: 6px; }
h4 { margin: 0; font-size: 8.8pt; }
aside ul { padding-left: 1em; }
aside li { margin-bottom: 3px; }
.summary { font-family: 'Instrument Serif', Georgia, serif; font-size: 12.5pt; line-height: 1.28; }
.job { margin-bottom: 9px; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }
h3 { font-size: 10.2pt; font-weight: 700; }
.org { color: #c2410c; }
.dates { font-size: 8.4pt; color: #78716c; white-space: nowrap; }
.note { color: #78716c; font-style: italic; }
li { margin-top: 1px; }
.tool { margin-bottom: 4px; }
"""

ROWS_CSS = """
.edu { display: flex; justify-content: space-between; gap: 8px; }
.course { margin-bottom: 1px; }
"""

STYLES = {
    "1-swiss-minimal": single_column(SWISS + ROWS_CSS, "family=Inter:wght@400;600;700"),
    "2-product-tech": single_column(TECH + ROWS_CSS, "family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500"),
    "3-editorial-two-column": two_column(EDITORIAL + ROWS_CSS, "family=DM+Sans:wght@400;700&family=Instrument+Serif"),
}

if __name__ == "__main__":
    for name, html in STYLES.items():
        (OUT / f"{name}.html").write_text(html)
        print("wrote", name)
