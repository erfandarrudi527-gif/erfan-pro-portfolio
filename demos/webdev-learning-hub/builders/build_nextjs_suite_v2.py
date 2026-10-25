# -*- coding: utf-8 -*-
"""
Generate the complete Next.js 15 Web Application with all 28 topics from user's syllabus.
Integrates Tabbed Navigation, individual 3-tier problems, live sandbox, and PDF compiler.
"""
import os, sys, json, subprocess

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
DATA_PATH = os.path.join(BASE_DIR, "builders", "nextjs_28_topics.json")
out_dir = os.path.join(BASE_DIR, "nextjs")
os.makedirs(out_dir, exist_ok=True)
html_path = os.path.join(out_dir, "index.html")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    topics = json.load(f)

# Group topics by difficulty level with counts for clear hierarchy
level_counts = {"مبتدی": 0, "متوسط": 0, "پیشرفته": 0}
for t in topics:
    lvl = t.get("level", "متوسط")
    if lvl in level_counts:
        level_counts[lvl] += 1

sidebar_items_html = ""
seen_levels = set()
cards_html = ""

for t in topics:
    tid = t["id"]
    title = t["title"]
    sub = t["sub"]
    lvl = t["level"]
    analogy = t["analogy"]
    plain_exp = t["plain_exp"]
    real = t["real"]
    code = t["code"]
    interview = t["interview"]
    sandbox = t["sandbox"]
    sol1 = t["sol1"]
    sol2 = t["sol2"]
    sol3 = t["sol3"]

    lvl_color = "#38bdf8" if lvl == "مبتدی" else ("#f59e0b" if lvl == "متوسط" else "#a855f7")
    lvl_icon = "🌱" if lvl == "مبتدی" else ("⚡" if lvl == "متوسط" else "🚀")

    if lvl not in seen_levels:
        seen_levels.add(lvl)
        sidebar_items_html += f"""
        <li class="tree-group-divider" data-group-level="{lvl}" style="color:{lvl_color};">
          <span>{lvl_icon} بخش {lvl}</span>
          <span class="tree-group-badge">{level_counts.get(lvl, 0)} فصل</span>
        </li>
        """

    sidebar_items_html += f"""
    <li>
      <a href="#topic-{tid}" class="tree-item" data-id="nextjs-{tid}" data-level="{lvl}">
        <div style="display:flex; align-items:center; gap:8px; overflow:hidden;">
          <span class="check-indicator" onclick="event.preventDefault(); toggleComplete('nextjs-{tid}', this)"></span>
          <span class="tree-title" style="white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">{tid}. {title}</span>
        </div>
        <span class="tree-badge">{lvl}</span>
      </a>
    </li>
    """

    challenges_html = f"""
    <div class="problem-card">
      <div class="problem-top">
        <span class="problem-tier-badge" style="background:rgba(16, 185, 129, 0.15); color:#10b981; border:1px solid #10b98144;">سطح: آسان</span>
        <span class="problem-title-text">مسئله ۱: راه‌اندازی و استفاده پایه از {title}</span>
      </div>
      <p class="problem-desc-text">پیاده‌سازی سینتکس استاندارد و الزامات پایه «{title}» در Next.js طبق داکیومنت رسمی.</p>
      <div class="problem-hint-box"><span style="font-weight:700; color:#fbbf24;">💡 راهنمایی:</span> قواعد نام‌گذاری و محل تعریف فایل را بررسی کنید.</div>
      <div class="problem-action-row">
        <button class="toggle-sol-btn" onclick="const s = document.getElementById('sol-nextjs-{tid}-easy'); const isShow = s.style.display==='block'; s.style.display = isShow ? 'none' : 'block'; this.innerText = isShow ? '👁️ مشاهده پاسخ و حل تشریحی' : '✕ بستن پاسخ';">
          👁️ مشاهده پاسخ و حل تشریحی
        </button>
      </div>
      <div class="solution-container" id="sol-nextjs-{tid}-easy" style="display:none; margin-top:10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="font-size:11.5px; color:#34d399; font-weight:700;">کد استاندارد پاسخ:</span>
          <button class="code-action-btn" onclick="copySnippet(this)" style="padding:2px 8px; font-size:10.5px;">📋 کپی</button>
        </div>
        <div class="code-box"><pre><code>{sol1.replace('<', '&lt;').replace('>', '&gt;')}</code></pre></div>
      </div>
    </div>

    <div class="problem-card">
      <div class="problem-top">
        <span class="problem-tier-badge" style="background:rgba(245, 158, 11, 0.15); color:#f59e0b; border:1px solid #f59e0b44;">سطح: متوسط</span>
        <span class="problem-title-text">مسئله ۲: مدیریت بهینه داده‌ها و تعامل با سرور در {title}</span>
      </div>
      <p class="problem-desc-text">کدی بنویسید که تعاملات پویا با «{title}» را به همراه ارزیابی خطا مدیریت کند.</p>
      <div class="problem-hint-box"><span style="font-weight:700; color:#fbbf24;">💡 راهنمایی:</span> به تفاوت رفتار سرور کامپوننت با کلاینت دقت کنید.</div>
      <div class="problem-action-row">
        <button class="toggle-sol-btn" onclick="const s = document.getElementById('sol-nextjs-{tid}-med'); const isShow = s.style.display==='block'; s.style.display = isShow ? 'none' : 'block'; this.innerText = isShow ? '👁️ مشاهده پاسخ و حل تشریحی' : '✕ بستن پاسخ';">
          👁️ مشاهده پاسخ و حل تشریحی
        </button>
      </div>
      <div class="solution-container" id="sol-nextjs-{tid}-med" style="display:none; margin-top:10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="font-size:11.5px; color:#34d399; font-weight:700;">کد استاندارد پاسخ:</span>
          <button class="code-action-btn" onclick="copySnippet(this)" style="padding:2px 8px; font-size:10.5px;">📋 کپی</button>
        </div>
        <div class="code-box"><pre><code>{sol2.replace('<', '&lt;').replace('>', '&gt;')}</code></pre></div>
      </div>
    </div>

    <div class="problem-card">
      <div class="problem-top">
        <span class="problem-tier-badge" style="background:rgba(239, 68, 68, 0.15); color:#ef4444; border:1px solid #ef444444;">سطح: سخت</span>
        <span class="problem-title-text">مسئله ۳: پیاده‌سازی سازمانی و پروداکشن برای {title}</span>
      </div>
      <p class="problem-desc-text">سناریوی مهندسی مقیاس‌پذیر در شرکت‌های بزرگ: پیاده‌سازی «{title}» با بالاترین کارایی کش و امنیت شبکه.</p>
      <div class="problem-hint-box"><span style="font-weight:700; color:#fbbf24;">💡 راهنمایی:</span> به کشینگ با تگ‌ها و کنترل دسترسی توجه فرمایید.</div>
      <div class="problem-action-row">
        <button class="toggle-sol-btn" onclick="const s = document.getElementById('sol-nextjs-{tid}-hard'); const isShow = s.style.display==='block'; s.style.display = isShow ? 'none' : 'block'; this.innerText = isShow ? '👁️ مشاهده پاسخ و حل تشریحی' : '✕ بستن پاسخ';">
          👁️ مشاهده پاسخ و حل تشریحی
        </button>
      </div>
      <div class="solution-container" id="sol-nextjs-{tid}-hard" style="display:none; margin-top:10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="font-size:11.5px; color:#34d399; font-weight:700;">کد استاندارد پاسخ:</span>
          <button class="code-action-btn" onclick="copySnippet(this)" style="padding:2px 8px; font-size:10.5px;">📋 کپی</button>
        </div>
        <div class="code-box"><pre><code>{sol3.replace('<', '&lt;').replace('>', '&gt;')}</code></pre></div>
      </div>
    </div>
    """

    safe_real = real.replace('<script', '&lt;script').replace('</script>', '&lt;/script&gt;')
    safe_interview = interview.replace('<script', '&lt;script').replace('</script>', '&lt;/script&gt;')

    cards_html += f"""
    <article class="topic-card" id="topic-{tid}" data-id="nextjs-{tid}" data-level="{lvl}">
      <div class="card-topbar">
        <div class="card-title-group">
          <span class="topic-num-badge">#{tid}</span>
          <h2 class="topic-h2">{title}</h2>
        </div>
        <div class="card-meta-actions">
          <span class="lvl-chip" style="background:{lvl_color}18; color:{lvl_color}; border-color:{lvl_color}44;">{lvl}</span>
          <button class="complete-toggle-btn" onclick="toggleCardComplete('nextjs-{tid}', this)">
            <span class="btn-check-icon">✓</span>
            <span class="btn-check-text">تکمیل شد</span>
          </button>
        </div>
      </div>

      <div class="card-body-open">
        <!-- نوار تب‌های کنار هم برای دسترسی سریع -->
        <nav class="card-tab-nav">
          <button class="card-tab-btn active" onclick="switchTopicTab(this, 'pane-concept')">📖 کالبدشکافی مفهوم</button>
          <button class="card-tab-btn" onclick="switchTopicTab(this, 'pane-code')">💻 نمونه کد تست‌شده</button>
          <button class="card-tab-btn" onclick="switchTopicTab(this, 'pane-sandbox')">🖥️ پیش‌نمایش و شبیه‌سازی</button>
          <button class="card-tab-btn" onclick="switchTopicTab(this, 'pane-production')">💼 سناریوی واقعی صنعت</button>
          <button class="card-tab-btn" onclick="switchTopicTab(this, 'pane-interview')">🎯 دام مصاحبه شغلی</button>
          <button class="card-tab-btn" onclick="switchTopicTab(this, 'pane-challenges')">🏋️ کارگاه مسئله (۳ سطح)</button>
        </nav>

        <div class="card-tab-content">
          <!-- ۱. کالبدشکافی مفهوم -->
          <div class="tab-pane pane-concept active">
            <div class="concept-block">
              <div class="analogy-subbox">
                <div class="subbox-label">💡 تشبیه در دنیای واقعی:</div>
                <p class="analogy-text">{analogy}</p>
              </div>
              <div class="explain-subbox">
                <div class="subbox-label">🎯 به زبون خیلی ساده (دقیقاً چیه و چیکار می‌کنه؟):</div>
                <p class="explain-text">{plain_exp}</p>
              </div>
            </div>
          </div>

          <!-- ۲. نمونه کد تست‌شده -->
          <div class="tab-pane pane-code">
            <div class="code-playground-block">
              <div class="code-box">
                <div class="code-bar">
                  <span class="code-lang-tag">💻 نمونه کد عملیاتی Next.js (TypeScript)</span>
                  <button class="code-action-btn" onclick="copySnippet(this)">📋 کپی کد</button>
                </div>
                <pre><code>{code.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
              </div>
            </div>
          </div>

          <!-- ۳. پیش‌نمایش و شبیه‌سازی -->
          <div class="tab-pane pane-sandbox">
            <div class="interactive-sandbox-block">
              <div class="sandbox-card">
                <div class="sandbox-topbar">
                  <div class="sandbox-dots">
                    <span class="sandbox-dot" style="background:#ef4444;"></span>
                    <span class="sandbox-dot" style="background:#f59e0b;"></span>
                    <span class="sandbox-dot" style="background:#10b981;"></span>
                    <span class="sandbox-title-tag">Next.js Environment Runtime</span>
                  </div>
                  <span class="sandbox-badge-active">App Router Active ✓</span>
                </div>
                <div class="sandbox-body">
                  {sandbox}
                </div>
              </div>
            </div>
          </div>

          <!-- ۴. سناریوی واقعی در صنعت -->
          <div class="tab-pane pane-production">
            <div class="production-block">
              <p class="production-text">{safe_real}</p>
            </div>
          </div>

          <!-- ۵. دام مصاحبه شغلی -->
          <div class="tab-pane pane-interview">
            <div class="interview-block">
              <p class="interview-text">{safe_interview}</p>
            </div>
          </div>

          <!-- ۶. کارگاه مسئله ۳ سطحی -->
          <div class="tab-pane pane-challenges">
            <div class="challenges-section-block">
              <div class="problems-grid">
                {challenges_html}
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>
    """

sys.path.append(os.path.join(BASE_DIR, "builders"))
from theme_pro import PRO_CSS

full_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>دانشنامه تخصصی Next.js | ۲۸ فصل جامع | ERFAN.DEV</title>
<style>
{PRO_CSS}

.tree-badge {{
  font-size: 10px;
  color: var(--text-mute);
  background: rgba(255, 255, 255, 0.04);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--border-subtle);
  flex-shrink: 0;
}}
</style>
</head>
<body>

<header class="top-nav">
  <div style="display:flex; align-items:center; gap:20px;">
    <a href="../index.html" class="brand-section">
      <div class="brand-icon">▲</div>
      <div>
        <div style="display:flex; align-items:center; gap:6px;">
          <span class="brand-title">ERFAN.DEV</span>
          <span class="brand-badge">Next.js Master Hub</span>
        </div>
      </div>
    </a>

    <nav class="track-tabs">
      <a href="../html/index.html" class="track-tab">🏛️ HTML (۳۵)</a>
      <a href="../css/index.html" class="track-tab">🎨 CSS (۶۲)</a>
      <a href="../javascript/index.html" class="track-tab">⚡ JavaScript (۷۵)</a>
      <a href="../react/index.html" class="track-tab">⚛️ React (۶۵)</a>
      <a href="../nextjs/index.html" class="track-tab active">▲ Next.js ({len(topics)})</a>
    </nav>
  </div>

  <div class="nav-actions">
    <a href="NextJS_Handbook.pdf" class="btn-icon btn-primary-glow" download>📄 دانلود کتابچه PDF</a>
    <button class="btn-icon" onclick="window.print()">🖨️ پرینت</button>
  </div>
</header>

<div class="app-layout">
  <aside class="sidebar">
    <div class="progress-card">
      <div class="progress-meta">
        <span>میزان پیشرفت شما</span>
        <span id="progressText">۰ از {len(topics)} (۰٪)</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" id="progressBar"></div>
      </div>
    </div>

    <input type="text" id="sidebarSearch" class="sidebar-search" placeholder="🔍 فیلتر سریع در عناوین...">

    <div class="level-filters">
      <button class="l-btn active" data-filter="all">همه ({len(topics)})</button>
      <button class="l-btn" data-filter="مبتدی">مبتدی ({level_counts.get('مبتدی', 0)})</button>
      <button class="l-btn" data-filter="متوسط">متوسط ({level_counts.get('متوسط', 0)})</button>
      <button class="l-btn" data-filter="پیشرفته">پیشرفته ({level_counts.get('پیشرفته', 0)})</button>
    </div>

    <ul class="tree-list" id="treeList">
      {sidebar_items_html}
    </ul>
  </aside>

  <main class="main-content">
    <div class="topic-page-header">
      <span class="track-pill" style="background:rgba(255,255,255,0.08); color:#fff; border-color:rgba(255,255,255,0.2);">
        ▲ دانشنامه جامع NEXT.JS (۲۸ فصل مرجع)
      </span>
      <h1 class="topic-page-title">دانشنامه مرجع و جامع Next.js</h1>
      <p class="topic-page-desc">
        سیستم مسیریابی App Router، کامپوننت‌های سروری RSC، رندرینگ هیبریدی و پیش‌رندر جزئی PPR، اکشن‌های سرور، میدل‌ورهای Edge، دیتابیس، کش چندلایه و سئو تخصصی.
      </p>
    </div>

    <section id="cardsContainer">
      {cards_html}
    </section>
  </main>
</div>

<script>
function switchTopicTab(btn, paneClass) {{
  const card = btn.closest('.topic-card');
  card.querySelectorAll('.card-tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  card.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  const targetPane = card.querySelector('.' + paneClass);
  if (targetPane) targetPane.classList.add('active');
}}

function copySnippet(btn) {{
  const code = btn.closest('.code-box').querySelector('pre code').innerText;
  navigator.clipboard.writeText(code).then(() => {{
    const old = btn.innerText;
    btn.innerText = '✅ کپی شد!';
    setTimeout(() => {{ btn.innerText = old; }}, 1600);
  }});
}}

function getCompleted() {{
  try {{
    return JSON.parse(localStorage.getItem('erfan_nextjs_completed') || '{{}}');
  }} catch(e) {{
    return {{}};
  }}
}}

function saveCompleted(data) {{
  localStorage.setItem('erfan_nextjs_completed', JSON.stringify(data));
  updateUIProgress();
}}

function toggleComplete(id, el) {{
  const store = getCompleted();
  store[id] = !store[id];
  saveCompleted(store);
}}

function toggleCardComplete(id, btn) {{
  const store = getCompleted();
  store[id] = !store[id];
  saveCompleted(store);
}}

function updateUIProgress() {{
  const store = getCompleted();
  const allCards = document.querySelectorAll('.topic-card');
  let completedCount = 0;

  allCards.forEach(card => {{
    const id = card.dataset.id;
    const isDone = !!store[id];
    if (isDone) completedCount++;

    const cardBtn = card.querySelector('.complete-toggle-btn');
    if (cardBtn) {{
      cardBtn.classList.toggle('is-active', isDone);
      cardBtn.querySelector('.btn-check-text').innerText = isDone ? 'تکمیل شد ✓' : 'علامت به عنوان خوانده شده';
    }}

    const treeItem = document.querySelector(`.tree-item[data-id="${{id}}"]`);
    if (treeItem) {{
      const ind = treeItem.querySelector('.check-indicator');
      if (ind) {{
        ind.classList.toggle('checked', isDone);
        ind.innerText = isDone ? '✓' : '';
      }}
    }}
  }});

  const total = allCards.length;
  const pct = total > 0 ? Math.round((completedCount / total) * 100) : 0;
  document.getElementById('progressText').innerText = `${{completedCount}} از ${{total}} (${{pct}}٪)`;
  document.getElementById('progressBar').style.width = `${{pct}}%`;
}}

// Sidebar search and filter
const sidebarSearch = document.getElementById('sidebarSearch');
const levelBtns = document.querySelectorAll('.l-btn');

function applySidebarFilter() {{
  const q = sidebarSearch.value.toLowerCase().trim();
  const activeLvl = document.querySelector('.l-btn.active').dataset.filter;

  document.querySelectorAll('#treeList li').forEach(li => {{
    if (li.classList.contains('tree-group-divider')) {{
      const grpLvl = li.dataset.groupLevel;
      li.style.display = (activeLvl === 'all' || activeLvl === grpLvl) && !q ? 'flex' : 'none';
      return;
    }}
    const a = li.querySelector('.tree-item');
    if (!a) return;
    const text = a.innerText.toLowerCase();
    const lvl = a.dataset.level;

    const matchLvl = (activeLvl === 'all' || lvl === activeLvl);
    const matchQ = (!q || text.includes(q));

    li.style.display = (matchLvl && matchQ) ? 'block' : 'none';
  }});
}}

sidebarSearch.addEventListener('input', applySidebarFilter);
levelBtns.forEach(b => {{
  b.addEventListener('click', () => {{
    levelBtns.forEach(btn => btn.classList.remove('active'));
    b.classList.add('active');
    applySidebarFilter();
  }});
}});

// Clean scroll navigation on click
document.querySelectorAll('.tree-item').forEach(item => {{
  item.addEventListener('click', (e) => {{
    const href = item.getAttribute('href');
    if (href && href.startsWith('#topic-')) {{
      e.preventDefault();
      const tid = href.replace('#topic-', '');
      const el = document.getElementById('topic-' + tid);
      if (el) {{
        const headerHeight = document.querySelector('.top-nav')?.offsetHeight || 75;
        const bodyRect = document.body.getBoundingClientRect().top;
        const elementRect = el.getBoundingClientRect().top;
        const elementPosition = elementRect - bodyRect;
        const offsetPosition = elementPosition - headerHeight - 20;
        window.scrollTo({{ top: offsetPosition, behavior: 'smooth' }});

        document.querySelectorAll('.topic-card').forEach(c => c.style.borderColor = '');
        el.style.borderColor = '#38bdf8';
        el.style.boxShadow = '0 0 35px rgba(56, 189, 248, 0.25), 0 16px 36px -12px rgba(0, 0, 0, 0.8)';
        setTimeout(() => {{
          el.style.borderColor = '';
          el.style.boxShadow = '';
        }}, 2000);
      }}
      document.querySelectorAll('.tree-item').forEach(i => i.classList.remove('active-spy'));
      item.classList.add('active-spy');
      history.pushState(null, null, '#topic-' + tid);
    }}
  }});
}});

updateUIProgress();
</script>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Next.js 28-Chapter Web App written successfully: {html_path}")

# Compile PDF
pdf_dest = os.path.join(out_dir, "NextJS_Handbook.pdf")
desktop_pdf = "C:/Users/erfan/Desktop/NextJS_Handbook.pdf"
cmd = [
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--virtual-time-budget=12000",
    f"--print-to-pdf={pdf_dest}",
    html_path
]
subprocess.run(cmd, check=True)

with open(pdf_dest, "rb") as rf:
    with open(desktop_pdf, "wb") as wf:
        wf.write(rf.read())
print(f"Next.js 28-Chapter PDF compiled on Desktop: {desktop_pdf} ({os.path.getsize(desktop_pdf):,} bytes)")
