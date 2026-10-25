# -*- coding: utf-8 -*-
import os, json

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
hub_html_path = os.path.join(BASE_DIR, "index.html")
catalog_path = os.path.join(BASE_DIR, "catalog.json")

with open(catalog_path, "r", encoding="utf-8") as f:
    catalog = json.load(f)

catalog_embedded = [
    {
        "id": item["id"],
        "track": item["track"],
        "title": item["title"],
        "level": item["level"],
        "sub": item.get("sub", "")
    }
    for item in catalog
]
embedded_json_str = json.dumps(catalog_embedded, ensure_ascii=False)

hub_code = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ERFAN.DEV | پلتفرم مرجع و سیستم‌عامل یادگیری وب (۲۳۷ سرفصل کامل)</title>
<style>
@font-face {{
  font-family: 'IRANYekan';
  src: url('fonts/IRANYekanXFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
}}
@font-face {{
  font-family: 'IRANYekan';
  src: url('fonts/IRANYekanXFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
}}
@font-face {{
  font-family: 'IRANYekan';
  src: url('fonts/IRANYekanXFaNum-Black.ttf') format('truetype');
  font-weight: 900;
}}

:root {{
  --bg-deep: #06080d;
  --bg-surface: #0b0f19;
  --bg-card: #0f1523;
  --border: #1a2234;
  --border-light: rgba(255, 255, 255, 0.08);
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --accent-html: #f97316;
  --accent-css: #38bdf8;
  --accent-js: #facc15;
  --accent-react: #67e8f9;
  --success: #10b981;
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
  background-color: var(--bg-deep);
  color: var(--text-primary);
  direction: rtl;
  line-height: 1.8;
  -webkit-font-smoothing: antialiased;
}}

.top-nav {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(11, 15, 25, 0.9);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border);
  padding: 14px 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

.brand-section {{
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--text-primary);
}}
.brand-badge {{
  font-size: 11px;
  font-weight: 900;
  background: rgba(255, 255, 255, 0.07);
  padding: 3px 8px;
  border-radius: 6px;
  border: 1px solid var(--border-light);
  color: var(--text-secondary);
}}
.brand-title {{
  font-size: 18px;
  font-weight: 900;
  letter-spacing: -0.3px;
}}

.container {{
  max-width: 1240px;
  margin: 0 auto;
  padding: 40px 24px 80px;
}}

.hero {{
  background: radial-gradient(circle at 50% 0%, #151d30 0%, #06080d 75%);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 60px 40px;
  margin-bottom: 45px;
  text-align: center;
  position: relative;
  overflow: hidden;
}}

.hero-tag {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(56, 189, 248, 0.1);
  color: #38bdf8;
  padding: 6px 18px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  border: 1px solid rgba(56, 189, 248, 0.25);
  margin-bottom: 20px;
}}

h1.hero-title {{
  font-size: 40px;
  font-weight: 900;
  letter-spacing: -1px;
  margin-bottom: 16px;
  background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

p.hero-desc {{
  font-size: 16px;
  color: var(--text-secondary);
  max-width: 820px;
  margin: 0 auto 35px;
  line-height: 1.9;
}}

.search-command-bar {{
  max-width: 680px;
  margin: 0 auto 35px;
  position: relative;
}}
.search-command-input {{
  width: 100%;
  background: rgba(11, 15, 25, 0.95);
  border: 1px solid var(--border-light);
  color: #fff;
  padding: 16px 24px 16px 110px;
  border-radius: 14px;
  font-size: 15px;
  font-family: inherit;
  outline: none;
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.8);
  transition: border-color 0.2s;
}}
.search-command-input:focus {{
  border-color: #38bdf8;
}}
.kbd-hint {{
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--text-muted);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 12px;
  font-family: monospace;
}}

.stats-grid {{
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}}
.stat-pill {{
  background: rgba(15, 21, 35, 0.8);
  border: 1px solid var(--border);
  padding: 12px 28px;
  border-radius: 14px;
  min-width: 170px;
}}
.stat-value {{
  font-size: 28px;
  font-weight: 900;
  color: #fff;
}}
.stat-name {{
  font-size: 12px;
  color: var(--text-muted);
}}

/* Tracks Grid */
.tracks-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
  margin-bottom: 50px;
}}

.track-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.25s ease;
  position: relative;
  overflow: hidden;
}}
.track-card:hover {{
  transform: translateY(-6px);
  border-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
}}

.track-header {{
  margin-bottom: 25px;
}}
.track-icon {{
  width: 56px;
  height: 56px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  margin-bottom: 20px;
  border: 1px solid var(--border);
}}
.track-h2 {{
  font-size: 22px;
  font-weight: 900;
  margin-bottom: 8px;
}}
.track-badge {{
  font-size: 12.5px;
  font-weight: 700;
  margin-bottom: 14px;
  display: inline-block;
}}
.track-description {{
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.8;
}}

.track-actions {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.btn-track {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 18px;
  border-radius: 12px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  font-family: inherit;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}}
.btn-open {{
  background: rgba(255, 255, 255, 0.06);
  color: #fff;
  border-color: var(--border);
}}
.btn-open:hover {{
  background: rgba(255, 255, 255, 0.12);
  transform: translateY(-2px);
}}
.btn-dl {{
  background: #38bdf8;
  color: #04101e !important;
  font-weight: 900;
}}
.btn-dl:hover {{
  background: #7dd3fc;
  transform: translateY(-2px);
}}

.card-html .track-icon {{ background: rgba(249, 115, 22, 0.12); color: var(--accent-html); }}
.card-html .track-badge {{ color: var(--accent-html); }}

.card-css .track-icon {{ background: rgba(56, 189, 248, 0.12); color: var(--accent-css); }}
.card-css .track-badge {{ color: var(--accent-css); }}

.card-js .track-icon {{ background: rgba(250, 204, 21, 0.12); color: var(--accent-js); }}
.card-js .track-badge {{ color: var(--accent-js); }}

.card-react .track-icon {{ background: rgba(103, 232, 249, 0.12); color: var(--accent-react); }}
.card-react .track-badge {{ color: var(--accent-react); }}

/* Search Results Popup */
.search-results-popup {{
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 8px;
  background: var(--bg-surface);
  border: 1px solid var(--border-light);
  border-radius: 14px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.9);
  max-height: 400px;
  overflow-y: auto;
  z-index: 200;
  list-style: none;
  display: none;
  text-align: right;
}}
.search-result-row {{
  padding: 12px 18px;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: 0.15s;
}}
.search-result-row:hover {{
  background: rgba(255, 255, 255, 0.05);
}}
.search-result-title {{
  font-weight: 700;
  font-size: 14px;
  color: #fff;
}}
.search-result-track {{
  font-size: 11px;
  color: var(--text-muted);
}}

footer {{
  text-align: center;
  padding: 30px 0;
  border-top: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 13px;
}}
</style>
</head>
<body>

<header class="top-nav">
  <a href="index.html" class="brand-section">
    <span style="font-size:24px;">⚡</span>
    <div>
      <div style="display:flex; align-items:center; gap:6px;">
        <span class="brand-title">ERFAN.DEV</span>
        <span class="brand-badge">Enterprise Learning OS</span>
      </div>
    </div>
  </a>

  <div style="display:flex; align-items:center; gap:12px;">
    <span id="globalProgressPill" style="font-size:12px; font-weight:700; color:#38bdf8; background:rgba(56,189,248,0.1); padding:4px 12px; border-radius:99px; border:1px solid rgba(56,189,248,0.2);">
      پیشرفت کل: ۰ از ۲۳۷ (۰٪)
    </span>
  </div>
</header>

<div class="container">
  <section class="hero">
    <span class="hero-tag">🚀 مرجع بزرگ و فوق‌تخصصی وب مدرن</span>
    <h1 class="hero-title">سیستم‌عامل یادگیری عمیق فرانت‌اند</h1>
    <p class="hero-desc">
      ۲۳۷ مفهوم کلیدی دنیای فرانت‌اند (HTML5, CSS3, JavaScript, React & Next.js) کالبدشکافی شده به ۴ لایه: تعریف ساده، کاربرد در پروژه واقعی، نمونه کد استاندارد همراه با اجرای زنده در مرورگر، و دام مصاحبه‌های استخدامی ارشد.
    </p>

    <div class="search-command-bar">
      <input type="text" id="masterSearch" class="search-command-input" placeholder="جستجوی سریع در تمام ۲۳۷ سرفصل (مثلا Event Loop, flexbox, useState, :has, Web Workers)...">
      <span class="kbd-hint">جستجو آنلاین</span>
      <ul class="search-results-popup" id="searchResultsPopup"></ul>
    </div>

    <div class="stats-grid">
      <div class="stat-pill">
        <div class="stat-value">۲۳۷</div>
        <div class="stat-name">مفهوم کلیدی مهندسی‌شده</div>
      </div>
      <div class="stat-pill">
        <div class="stat-value">۴</div>
        <div class="stat-name">وب‌اپلیکیشن تعاملی مستقل</div>
      </div>
      <div class="stat-pill">
        <div class="stat-value">۴</div>
        <div class="stat-name">کتابچه رسمی PDF در دسکتاپ</div>
      </div>
      <div class="stat-pill">
        <div class="stat-value">۱۰۰٪</div>
        <div class="stat-name">آفلاین با فونت ایران‌یکان</div>
      </div>
    </div>
  </section>

  <main class="tracks-grid">
    <!-- HTML -->
    <div class="track-card card-html">
      <div class="track-header">
        <div class="track-icon">🏛️</div>
        <h2 class="track-h2">دانشنامه HTML5</h2>
        <span class="track-badge">۳۵ سرفصل کامل (مبتدی تا پیشرفته)</span>
        <p class="track-description">
          اسکلت‌بندی، فرم‌ها، تگ‌های سمانتیک، سئو، تصاویر واکنش‌گرا با picture، دسترسی‌پذیری ARIA، وب‌کامپوننت‌ها و امنیت CSP.
        </p>
      </div>
      <div class="track-actions">
        <a href="html/index.html" class="btn-track btn-open">🌐 ورود به وب‌اپلیکیشن HTML</a>
        <a href="html/HTML_Handbook.pdf" class="btn-track btn-dl" download>📄 دانلود کتابچه PDF</a>
      </div>
    </div>

    <!-- CSS -->
    <div class="track-card card-css">
      <div class="track-header">
        <div class="track-icon">🎨</div>
        <h2 class="track-h2">دانشنامه CSS3</h2>
        <span class="track-badge">۶۲ سرفصل کامل (مبتدی تا پیشرفته)</span>
        <p class="track-description">
          باکس مدل، فلکس‌باکس، گرید، مدیاکوئری‌ها، انیمیشن‌ها، کوئری‌های کانتینر، سلکتور :has، لایه‌های @layer، دارک‌مود و راست‌چین.
        </p>
      </div>
      <div class="track-actions">
        <a href="css/index.html" class="btn-track btn-open">🌐 ورود به وب‌اپلیکیشن CSS</a>
        <a href="css/CSS_Handbook.pdf" class="btn-track btn-dl" download>📄 دانلود کتابچه PDF</a>
      </div>
    </div>

    <!-- JS -->
    <div class="track-card card-js">
      <div class="track-header">
        <div class="track-icon">⚡</div>
        <h2 class="track-h2">دانشنامه JavaScript</h2>
        <span class="track-badge">۷۵ سرفصل کامل (مبتدی تا پیشرفته)</span>
        <p class="track-description">
          موتور V8، متدهای آرایه، اسکوپ، کلوژر، this، ایونت‌لوپ، پرامیس‌ها، الگوهای شی‌گرایی، وب‌ورکرها، وب‌سوکت و بهینه‌سازی عملکرد.
        </p>
      </div>
      <div class="track-actions">
        <a href="javascript/index.html" class="btn-track btn-open">🌐 ورود به وب‌اپلیکیشن JS</a>
        <a href="javascript/JavaScript_Handbook.pdf" class="btn-track btn-dl" download>📄 دانلود کتابچه PDF</a>
      </div>
    </div>

    <!-- React -->
    <div class="track-card card-react">
      <div class="track-header">
        <div class="track-icon">⚛️</div>
        <h2 class="track-h2">دانشنامه React & Next.js</h2>
        <span class="track-badge">۶۵ سرفصل کامل (مبتدی تا پیشرفته)</span>
        <p class="track-description">
          کامپوننت‌ها، هوک‌های پایه، ریداکس، زاستند، تن‌استک کوئری، ری‌اکت ۱۹، کامپوننت‌های سروری RSC، نکست جی‌اس، و استقرار در پروداکشن.
        </p>
      </div>
      <div class="track-actions">
        <a href="react/index.html" class="btn-track btn-open">🌐 ورود به وب‌اپلیکیشن React</a>
        <a href="react/React_Handbook.pdf" class="btn-track btn-dl" download>📄 دانلود کتابچه PDF</a>
      </div>
    </div>
  </main>

  <footer>
    طراحی و توسعه اختصاصی برای عرفان | تمامی فایل‌های HTML و PDF در پوشه WebDev_Master_Learning_Hub و روی دسکتاپ در دسترس هستند.
  </footer>
</div>

<script>
const catalogData = {embedded_json_str};

// Update progress
try {{
  const store = JSON.parse(localStorage.getItem('erfan_dev_completed') || '{{}}');
  const doneCount = Object.values(store).filter(Boolean).length;
  const pct = Math.round((doneCount / 237) * 100);
  document.getElementById('globalProgressPill').innerText = `پیشرفت کل: ${{doneCount}} از ۲۳۷ (${{pct}}٪)`;
}} catch(e) {{}}

// Live Master Search on Home Page
const searchInput = document.getElementById('masterSearch');
const popup = document.getElementById('searchResultsPopup');

searchInput.addEventListener('input', (e) => {{
  const q = e.target.value.toLowerCase().trim();
  if (!q) {{
    popup.style.display = 'none';
    return;
  }}

  const results = catalogData.filter(item => 
    item.title.toLowerCase().includes(q) || 
    item.track.toLowerCase().includes(q) ||
    (item.sub && item.sub.toLowerCase().includes(q))
  ).slice(0, 8);

  if (results.length === 0) {{
    popup.innerHTML = '<li style="padding:15px; color:#64748b; text-align:center;">موردی با این عبارت یافت نشد.</li>';
  }} else {{
    popup.innerHTML = results.map(item => `
      <li class="search-result-row" onclick="window.location.href='${{item.track}}/index.html#topic-${{item.id}}'">
        <div>
          <div class="search-result-title">${{item.id}}. ${{item.title}}</div>
          <div class="search-result-track">${{item.track.toUpperCase()}} • ${{item.level}}</div>
        </div>
        <span style="font-size:12px; color:#38bdf8;">ورود ↗</span>
      </li>
    `).join('');
  }}
  popup.style.display = 'block';
}});

document.addEventListener('click', (e) => {{
  if (!e.target.closest('.search-command-bar')) {{
    popup.style.display = 'none';
  }}
}});
</script>

</body>
</html>
"""

with open(hub_html_path, "w", encoding="utf-8") as f:
    f.write(hub_code)
print("Hub updated with 100% offline embedded search:", hub_html_path)
