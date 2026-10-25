# -*- coding: utf-8 -*-
import os, subprocess, sys

sys.path.append(os.path.dirname(__file__))
from react_data_1 import REACT_TOPICS_1 as mod1
from react_data_2 import REACT_TOPICS_2 as mod2
from react_data_3 import REACT_TOPICS_3 as mod3

all_topics = mod1 + mod2 + mod3
print(f"Total React Topics Loaded: {len(all_topics)}")

out_dir = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub/react"
os.makedirs(out_dir, exist_ok=True)
html_path = os.path.join(out_dir, "index.html")

cards_html = ""
for t in all_topics:
    tid = t["id"]
    title = t["title"]
    lvl = t["level"]
    what = t["what"]
    does = t["does"]
    real = t["real"]
    code = t["code"]

    lvl_color = "#38bdf8" if lvl == "مبتدی" else ("#f59e0b" if lvl == "متوسط" else "#a855f7")

    cards_html += f"""
    <article class="topic-card" data-level="{lvl}">
      <div class="card-header">
        <div>
          <span class="level-badge" style="background:{lvl_color}22; color:{lvl_color}; border-color:{lvl_color}44;">{lvl}</span>
          <h3 class="topic-title">{tid}. {title}</h3>
        </div>
        <button class="copy-btn" onclick="copyCode(this)" title="کپی کد">📋 کپی کد</button>
      </div>

      <div class="box what-box">
        <div class="box-tag">🔍 دقیقاً چیه؟</div>
        <p>{what}</p>
      </div>

      <div class="box does-box">
        <div class="box-tag">⚙️ چیکار می‌کنه و چه مشکلی رو حل می‌کنه؟</div>
        <p>{does}</p>
      </div>

      <div class="box real-box">
        <div class="box-tag">💼 مثال در دنیای واقعی (سناریوی عملی)</div>
        <p>{real}</p>
      </div>

      <div class="code-wrapper">
        <div class="code-header"><span>React JSX</span><span>Modern React</span></div>
        <pre><code>{code.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
      </div>
    </article>
    """

full_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>دانشنامه جامع و عمیق React (۶۵ سرفصل کامل از صفر تا پیشرفته)</title>
<style>
@font-face {{
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
}}
@font-face {{
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
}}
@font-face {{
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Black.ttf') format('truetype');
  font-weight: 900;
}}

:root {{
  --bg: #07090e;
  --surface: #0e1526;
  --surface-border: #1e293b;
  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --accent: #61dafb;
  --accent-soft: rgba(97, 218, 251, 0.12);
  --code-bg: #020612;
  --blue: #38bdf8;
  --amber: #f59e0b;
  --green: #10b981;
  --purple: #a855f7;
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: 'IRANYekan', system-ui, Tahoma, sans-serif;
  background-color: var(--bg);
  color: var(--text-main);
  line-height: 1.85;
  padding: 30px 20px;
}}

.container {{
  max-width: 1100px;
  margin: 0 auto;
}}

header.main-header {{
  background: linear-gradient(135deg, #0e1526 0%, #172554 100%);
  border: 1px solid var(--surface-border);
  border-radius: 20px;
  padding: 35px 30px;
  margin-bottom: 30px;
  text-align: center;
}}

.header-badge {{
  display: inline-block;
  background: var(--accent-soft);
  color: var(--accent);
  padding: 4px 16px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 12px;
  border: 1px solid rgba(97, 218, 251, 0.3);
}}

h1.page-title {{
  font-size: 32px;
  font-weight: 900;
  color: #fff;
  margin-bottom: 10px;
}}

p.header-desc {{
  font-size: 15px;
  color: var(--text-muted);
  max-width: 800px;
  margin: 0 auto 20px;
}}

.header-actions {{
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}}

.btn {{
  padding: 10px 22px;
  border-radius: 12px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}}

.btn-primary {{
  background: var(--accent);
  color: #04101e;
}}
.btn-primary:hover {{
  background: #a5f3fc;
  transform: translateY(-2px);
}}

.btn-outline {{
  background: rgba(255,255,255,0.05);
  color: var(--text-main);
  border-color: var(--surface-border);
}}
.btn-outline:hover {{
  background: rgba(255,255,255,0.1);
  transform: translateY(-2px);
}}

/* Controls */
.controls-bar {{
  background: var(--surface);
  border: 1px solid var(--surface-border);
  border-radius: 16px;
  padding: 16px 20px;
  margin-bottom: 25px;
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}}

.search-input {{
  flex: 1;
  min-width: 250px;
  background: var(--code-bg);
  border: 1px solid var(--surface-border);
  color: #fff;
  padding: 10px 16px;
  border-radius: 10px;
  font-family: inherit;
  font-size: 14px;
  outline: none;
}}
.search-input:focus {{
  border-color: var(--accent);
}}

.filters {{
  display: flex;
  gap: 8px;
}}

.filter-btn {{
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--surface-border);
  padding: 8px 16px;
  border-radius: 8px;
  font-family: inherit;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.15s ease;
}}
.filter-btn.active, .filter-btn:hover {{
  background: var(--accent-soft);
  color: var(--accent);
  border-color: var(--accent);
}}

/* Cards */
.topic-card {{
  background: var(--surface);
  border: 1px solid var(--surface-border);
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 24px;
  transition: border-color 0.2s ease;
}}
.topic-card:hover {{
  border-color: rgba(97, 218, 251, 0.4);
}}

.card-header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 15px;
  margin-bottom: 16px;
}}

.level-badge {{
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 99px;
  border: 1px solid;
  margin-bottom: 6px;
}}

.topic-title {{
  font-size: 21px;
  font-weight: 900;
  color: #fff;
}}

.copy-btn {{
  background: rgba(255,255,255,0.05);
  color: var(--text-muted);
  border: 1px solid var(--surface-border);
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  transition: 0.15s;
}}
.copy-btn:hover {{
  color: #fff;
  border-color: var(--accent);
}}

.box {{
  border-radius: 0 10px 10px 0;
  padding: 12px 16px;
  margin-bottom: 12px;
}}

.box-tag {{
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 4px;
}}

.what-box {{
  background: rgba(56, 189, 248, 0.07);
  border-right: 3px solid var(--blue);
}}
.what-box .box-tag {{ color: var(--blue); }}
.what-box p {{ font-size: 14.5px; color: #e2e8f0; }}

.does-box {{
  background: rgba(245, 158, 11, 0.07);
  border-right: 3px solid var(--amber);
}}
.does-box .box-tag {{ color: var(--amber); }}
.does-box p {{ font-size: 14px; color: #fde68a; }}

.real-box {{
  background: rgba(16, 185, 129, 0.07);
  border-right: 3px solid var(--green);
}}
.real-box .box-tag {{ color: var(--green); }}
.real-box p {{ font-size: 14px; color: #a7f3d0; }}

.code-wrapper {{
  background: var(--code-bg);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  padding: 14px 18px;
  direction: ltr;
  text-align: left;
  overflow-x: auto;
}}
.code-header {{
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text-muted);
  margin-bottom: 8px;
  font-family: monospace;
}}
.code-wrapper pre code {{
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 13px;
  color: #7dd3fc;
  line-height: 1.6;
}}

@media print {{
  body {{ background: #fff !important; color: #000 !important; padding: 0 !important; }}
  header.main-header, .controls-bar, .copy-btn {{ display: none !important; }}
  .topic-card {{ page-break-inside: avoid; border: 1px solid #ccc !important; background: #fff !important; margin-bottom: 20px; }}
  .topic-title {{ color: #000 !important; }}
  .what-box {{ background: #f0f9ff !important; color: #000 !important; border-color: #0284c7 !important; }}
  .what-box p {{ color: #0c4a6e !important; }}
  .does-box {{ background: #fffbeb !important; color: #000 !important; border-color: #d97706 !important; }}
  .does-box p {{ color: #78350f !important; }}
  .real-box {{ background: #ecfdf5 !important; border-color: #059669 !important; }}
  .real-box p {{ color: #064e3b !important; }}
  .code-wrapper {{ background: #f8fafc !important; border-color: #cbd5e1 !important; }}
  .code-wrapper code {{ color: #0f172a !important; }}
}}
</style>
</head>
<body>

<div class="container">
  <header class="main-header">
    <span class="header-badge">⚛️ مرجع جامع و مهندسی React</span>
    <h1 class="page-title">دانشنامه ۶۵ مفهوم کلیدی اکوسیستم React</h1>
    <p class="header-desc">
      از کامپوننت‌ها و هوک‌های پایه تا ریداکس، زاستند، تن‌استک کوئری، ری‌اکت ۱۹، کامپوننت‌های سروری، نکست جی‌اس، و استقرار با کدهای واقعی و پروژه‌محور.
    </p>
    <div class="header-actions">
      <a href="../index.html" class="btn btn-outline">🏠 بازگشت به هاب اصلی</a>
      <a href="React_Handbook.pdf" class="btn btn-primary" download>📄 دانلود کتابچه PDF (A4)</a>
      <button onclick="window.print()" class="btn btn-outline">🖨️ پرینت مستقیم</button>
    </div>
  </header>

  <section class="controls-bar">
    <input type="text" id="searchInput" class="search-input" placeholder="🔍 جستجوی مفهوم (مثلا useState, useEffect, redux, react 19, nextjs)...">
    <div class="filters">
      <button class="filter-btn active" data-filter="all">همه ({len(all_topics)})</button>
      <button class="filter-btn" data-filter="مبتدی">مبتدی (۱۳)</button>
      <button class="filter-btn" data-filter="متوسط">متوسط (۲۵)</button>
      <button class="filter-btn" data-filter="پیشرفته">پیشرفته (۲۷)</button>
    </div>
  </section>

  <main id="topicsGrid">
    {cards_html}
  </main>
</div>

<script>
function copyCode(btn) {{
  const code = btn.closest('.topic-card').querySelector('pre code').innerText;
  navigator.clipboard.writeText(code).then(() => {{
    const old = btn.innerText;
    btn.innerText = '✅ کپی شد!';
    btn.style.borderColor = '#10b981';
    setTimeout(() => {{
      btn.innerText = old;
      btn.style.borderColor = '';
    }}, 1800);
  }});
}}

const searchInput = document.getElementById('searchInput');
const filterBtns = document.querySelectorAll('.filter-btn');
const cards = document.querySelectorAll('.topic-card');

function applyFilters() {{
  const q = searchInput.value.toLowerCase().trim();
  const activeLevel = document.querySelector('.filter-btn.active').dataset.filter;

  cards.forEach(card => {{
    const level = card.dataset.level;
    const text = card.innerText.toLowerCase();
    const matchFilter = (activeLevel === 'all' || level === activeLevel);
    const matchSearch = (!q || text.includes(q));

    if (matchFilter && matchSearch) {{
      card.style.display = 'block';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}

searchInput.addEventListener('input', applyFilters);

filterBtns.forEach(btn => {{
  btn.addEventListener('click', () => {{
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    applyFilters();
  }});
}});
</script>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print("React HTML page successfully generated:", html_path)

# Compile PDF
pdf_path = os.path.join(out_dir, "React_Handbook.pdf")
cmd = [
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--virtual-time-budget=10000",
    f"--print-to-pdf={pdf_path}",
    html_path
]
subprocess.run(cmd, check=True)
print("React PDF compiled:", pdf_path, "Size:", os.path.getsize(pdf_path))

# Copy directly to Desktop
desktop_pdf = "C:/Users/erfan/Desktop/React_Handbook.pdf"
with open(pdf_path, "rb") as rf:
    with open(desktop_pdf, "wb") as wf:
        wf.write(rf.read())
print("Updated Desktop PDF:", desktop_pdf)
