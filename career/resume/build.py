"""Build the resume from this one content source.

    python3 career/resume/build.py

Writes Nicholas-Rode-Resume.html and exports Nicholas-Rode-Resume.pdf next to it
(headless Chrome). Edit the text below, rerun, and both stay in sync.
"""

import subprocess
from html import escape
from pathlib import Path

OUT = Path(__file__).parent

NAME = "Nicholas Rode"
TITLE = "Motion Designer & Engineer"
CONTACT = ["theniceguynick@gmail.com", "281.794.1242", "Vancouver, WA 98683"]
LINKS = [("Portfolio", "https://nicholasrode.com"), ("Reel", "https://nicholasrode.com/reel")]

SUMMARY = (
    "Motion designer and engineer with 5+ years of experience shipping motion for B2B SaaS and tech brands. "
    "I turn complex products into clear, engaging motion and build it production-ready, fast, and accessible "
    "in Rive, Lottie, and code. An AI-first workflow lets me prototype, iterate, and ship faster, and I build "
    "my own tools to close the gap between design and development."
)

SKILLS = [
    ("Motion & interaction", "Rive (state machines, interactive components), After Effects, Lottie/Bodymovin, UI animation, micro-interactions, transitions, motion systems, visual storytelling, 2D/3D animation"),
    ("Design", "Figma (including motion), Illustrator, UI/UX design, design systems, interactive prototyping"),
    ("Production & performance", "Rive web runtimes (React, Canvas, WebGL2), Lottie JSON delivery, WebGL shaders, Lighthouse performance tuning, reduced-motion accessibility, developer handoff"),
    ("AI workflow", "Claude Code, AI-assisted prototyping and production code, Figma plugin and AI tool development"),
]

JOBS = [
    {
        "role": "Motion Engineer",
        "org": "Webstacks",
        "note": "B2B web design and development agency · Promoted from Motion Designer, Oct 2026",
        "dates": "Jan 2025 – Present",
        "bullets": [
            "Shipped interactive motion, animation, and illustration for Gong and Fireworks AI, including product UI motion for Fireworks AI",
            "Built 4 interactive Rive product demos for Deepgram's AI voice platform: voice-to-text, voice avatars, assistant states, and a Slack integration walkthrough",
            "Designed a 10-piece Rive motion system for Shep's rebrand and raised the hero's Lighthouse score from 40 to 99 by switching its Rive runtime from WebGL2 to Canvas",
            "Built AI-powered tools with Claude Code, including Sequence to Shader (below) and a Figma plugin that generates reliable React code",
            "Use AI daily to prototype interactions and write production animation code, speeding up design-to-dev handoff",
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

# A third item is an optional link, shown after the description.
TOOLS = [
    ("Sequence to Shader (open-source Claude skill)",
     "Turns animated gradients into live WebGL backgrounds: 17.1 MB of video became 200 KB, matched frame by frame.",
     "https://github.com/swicknick/sequence-to-shader"),
    ("Stroke Center (Figma Community)", "Plugin that converts inside/outside strokes to center for clean Lottie export."),
    ("Design to Webpage", "AI skill that turns Figma designs into working HTML prototypes with interactions and motion; used on client projects."),
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
    out = []
    for k, v, *link in TOOLS:
        url = f' <a href="{e(link[0])}">{e(link[0].replace("https://", ""))}</a>' if link else ""
        out.append(f'<p class="tool"><strong>{e(k)}:</strong> {e(v)}{url}</p>')
    return "".join(out)


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
ROWS_CSS = """
.edu { display: flex; justify-content: space-between; gap: 8px; }
.course { margin-bottom: 1px; }
"""

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
NAME_OUT = "Nicholas-Rode-Resume"

if __name__ == "__main__":
    html_path = OUT / f"{NAME_OUT}.html"
    html_path.write_text(
        single_column(TECH + ROWS_CSS, "family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500")
    )
    print("wrote", html_path.name)
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=3000",
         f"--print-to-pdf={OUT / (NAME_OUT + '.pdf')}", html_path.resolve().as_uri()],
        check=True, capture_output=True,
    )
    print("wrote", NAME_OUT + ".pdf")
