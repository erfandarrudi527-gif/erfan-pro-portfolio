# -*- coding: utf-8 -*-
"""
Generate the Master Hub UI (index.html) with:
- Engineering OS Dashboard style
- Live stats connected to localStorage across all 5 tracks (HTML, CSS, JS, React, Next.js)
- Global Search / Command Palette (⌘K)
- Audio feedback (tactile click)
- Linear/Raycast dark minimalism
"""
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ERFAN.DEV | مرکز یادگیری جامع توسعه وب</title>
<style>
@font-face {
  font-family: 'IRANYekan';
  src: url('fonts/IRANYekanXFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('fonts/IRANYekanXFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('fonts/IRANYekanXFaNum-Black.ttf') format('truetype');
  font-weight: 900;
}

:root {
  --bg-deep: #030508;
  --bg-card: #090e17;
  --bg-card-hover: #0d1522;
  --border: rgba(255, 255, 255, 0.07);
  --border-focus: rgba(56, 189, 248, 0.45);
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --sky: #38bdf8;
  --emerald: #10b981;
  --amber: #f59e0b;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
  background-color: var(--bg-deep);
  background-image: 
    linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 32px 32px;
  color: var(--text-primary);
  direction: rtl;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  -webkit-font-smoothing: antialiased;
}

/* Master Navigation */
.header-nav {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(3, 5, 8, 0.85);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 12px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}
.brand-logo {
  width: 34px;
  height: 34px;
  border-radius: 9px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.02));
  border: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 17px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}
.brand-name {
  font-size: 16px;
  font-weight: 900;
  letter-spacing: -0.4px;
}
.brand-sub {
  font-size: 11px;
  color: var(--sky);
  background: rgba(56, 189, 248, 0.1);
  padding: 2px 8px;
  border-radius: 6px;
  border: 1px solid rgba(56, 189, 248, 0.25);
  font-weight: 700;
}

.search-trigger {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 12.5px;
  font-family: inherit;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  transition: all 0.15s;
}
.search-trigger:hover {
  background: rgba(255, 255, 255, 0.07);
  border-color: rgba(255, 255, 255, 0.18);
  color: #fff;
}
.kbd-tag {
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 10px;
  font-family: monospace;
}

/* Hero Section */
.hero-container {
  max-width: 1240px;
  margin: 40px auto 30px;
  padding: 0 24px;
  text-align: center;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 14px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border);
  border-radius: 99px;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-secondary);
  margin-bottom: 18px;
}
.hero-title {
  font-size: 40px;
  font-weight: 900;
  letter-spacing: -1px;
  line-height: 1.3;
  margin-bottom: 12px;
  background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-p {
  font-size: 16px;
  color: var(--text-secondary);
  max-width: 680px;
  margin: 0 auto 30px;
  line-height: 1.8;
}

/* Live Global Stats Grid */
.stats-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  max-width: 960px;
  margin: 0 auto 45px;
}
.stat-box {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 14px 18px;
  text-align: right;
  transition: all 0.2s;
}
.stat-box:hover {
  border-color: rgba(255, 255, 255, 0.15);
  transform: translateY(-1px);
}
.stat-num {
  font-size: 24px;
  font-weight: 900;
  color: #fff;
  font-family: monospace;
}
.stat-label {
  font-size: 12px;
  color: var(--text-muted);
  font-weight: 700;
  margin-top: 2px;
}

/* Track Cards Grid */
.tracks-grid {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 24px 80px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
  gap: 24px;
}

.track-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  transition: all 0.25s ease;
}
.track-card:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-focus);
  box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
  transform: translateY(-3px);
}
.track-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
  opacity: 0;
  transition: opacity 0.2s;
}
.track-card:hover::before {
  opacity: 1;
}

.card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 16px;
}
.track-icon-badge {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.03);
}
.track-count-chip {
  font-size: 11px;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: 99px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border);
  color: var(--text-secondary);
}

.track-heading {
  font-size: 20px;
  font-weight: 900;
  color: #fff;
  margin-bottom: 8px;
}
.track-desc {
  font-size: 13.5px;
  color: var(--text-secondary);
  line-height: 1.75;
  margin-bottom: 20px;
}

.track-progress-row {
  margin-bottom: 20px;
  background: rgba(255, 255, 255, 0.02);
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.04);
}
.prog-info {
  display: flex;
  justify-content: space-between;
  font-size: 11.5px;
  color: var(--text-muted);
  font-weight: 700;
  margin-bottom: 6px;
}
.prog-track {
  height: 5px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 99px;
  overflow: hidden;
}
.prog-fill {
  height: 100%;
  width: 0%;
  border-radius: 99px;
  transition: width 0.3s;
}

.card-actions {
  display: flex;
  gap: 10px;
}
.btn-enter {
  flex: 1;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  color: #fff;
  padding: 9px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 800;
  text-decoration: none;
  text-align: center;
  transition: all 0.15s;
}
.btn-enter:hover {
  background: #fff;
  color: #020617;
  border-color: #fff;
}
.btn-pdf {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 9px 14px;
  border-radius: 8px;
  font-size: 12.5px;
  text-decoration: none;
  transition: all 0.15s;
}
.btn-pdf:hover {
  background: rgba(255, 255, 255, 0.08);
  color: #fff;
}

/* Modal Search */
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(14px);
  z-index: 999;
  align-items: flex-start;
  justify-content: center;
  padding-top: 12vh;
}
.modal-overlay.open { display: flex; }
.modal-content {
  width: 100%;
  max-width: 620px;
  background: #090e17;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 14px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
  overflow: hidden;
}
.modal-input {
  width: 100%;
  padding: 16px 20px;
  background: transparent;
  border: none;
  border-bottom: 1px solid var(--border);
  color: #fff;
  font-size: 15px;
  font-family: inherit;
  outline: none;
}
.modal-results {
  max-height: 380px;
  overflow-y: auto;
  list-style: none;
  padding: 8px;
}
.modal-item {
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-decoration: none;
  color: inherit;
  transition: 0.12s;
}
.modal-item:hover {
  background: rgba(255, 255, 255, 0.05);
}
.modal-item-title {
  font-size: 13.5px;
  font-weight: 700;
  color: #fff;
}
.modal-item-track {
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-muted);
}
</style>
</head>
<body>

<header class="header-nav">
  <div class="brand-wrap">
    <div class="brand-logo">⚡</div>
    <div>
      <span class="brand-name">ERFAN.DEV</span>
      <span class="brand-sub">Master Learning Hub</span>
    </div>
  </div>

  <button class="search-trigger" onclick="openSearch()">
    <span>🔍 جستجوی سریع در ۲۴۲ سرفصل...</span>
    <span class="kbd-tag">⌘K / Ctrl+K</span>
  </button>
</header>

<section class="hero-container">
  <div class="hero-badge">
    <span>💎 پلتفرم جامع و سیستم‌عامل آموزشی فرانت‌اند</span>
  </div>
  <h1 class="hero-title">دانشنامه مرجع مهندسی وب</h1>
  <p class="hero-p">
    مفاهیم کالبدشکافی‌شده، تست‌کیس‌های واقعی شرکت‌های بزرگ، ویجت‌های تعاملی، مسائل ۳ سطحی با حل تشریحی، و خروجی‌های استاندارد PDF.
  </p>

  <div class="stats-bar">
    <div class="stat-box">
      <div class="stat-num">۲۴۲</div>
      <div class="stat-label">کل سرفصل‌های تخصصی</div>
    </div>
    <div class="stat-box">
      <div class="stat-num" id="globalCompleted">۰</div>
      <div class="stat-label">سرفصل‌های تکمیل‌شده</div>
    </div>
    <div class="stat-box">
      <div class="stat-num">۷۲۶</div>
      <div class="stat-label">مسئله عملی با جواب تشریحی</div>
    </div>
    <div class="stat-box">
      <div class="stat-num" id="globalPercent">۰٪</div>
      <div class="stat-label">پیشرفت کل دوره‌ها</div>
    </div>
  </div>
</section>

<main class="tracks-grid">
  <!-- HTML -->
  <article class="track-card" style="--accent: #f97316;">
    <div>
      <div class="card-top">
        <div class="track-icon-badge" style="color: #f97316;">🏛️</div>
        <span class="track-count-chip">۳۵ سرفصل کامل</span>
      </div>
      <h2 class="track-heading">دانشنامه HTML5</h2>
      <p class="track-desc">
        اسکلت وب، تگ‌های سمانتیک، فرم‌ها و اعتبارسنجی زنده، سئو و استانداردهای نوین ساختار سند.
      </p>
    </div>
    <div>
      <div class="track-progress-row">
        <div class="prog-info">
          <span>میزان تسلط</span>
          <span id="prog-text-html">۰ از ۳۵</span>
        </div>
        <div class="prog-track">
          <div class="prog-fill" id="prog-bar-html" style="background:#f97316;"></div>
        </div>
      </div>
      <div class="card-actions">
        <a href="html/index.html" class="btn-enter" onclick="playClick()">🌐 ورود به وب‌اپلیکیشن</a>
        <a href="html/HTML_Handbook.pdf" class="btn-pdf" download>📄 دانلود PDF</a>
      </div>
    </div>
  </article>

  <!-- CSS -->
  <article class="track-card" style="--accent: #38bdf8;">
    <div>
      <div class="card-top">
        <div class="track-icon-badge" style="color: #38bdf8;">🎨</div>
        <span class="track-count-chip">۶۲ سرفصل کامل</span>
      </div>
      <h2 class="track-heading">دانشنامه CSS3</h2>
      <p class="track-desc">
        باکس‌مدل، Flexbox، گرید پیشرفته، انیمیشن‌ها، Subgrid، لایه‌های Cascade و معماری مدرن استایل‌دهی.
      </p>
    </div>
    <div>
      <div class="track-progress-row">
        <div class="prog-info">
          <span>میزان تسلط</span>
          <span id="prog-text-css">۰ از ۶۲</span>
        </div>
        <div class="prog-track">
          <div class="prog-fill" id="prog-bar-css" style="background:#38bdf8;"></div>
        </div>
      </div>
      <div class="card-actions">
        <a href="css/index.html" class="btn-enter" onclick="playClick()">🌐 ورود به وب‌اپلیکیشن</a>
        <a href="css/CSS_Handbook.pdf" class="btn-pdf" download>📄 دانلود PDF</a>
      </div>
    </div>
  </article>

  <!-- JavaScript -->
  <article class="track-card" style="--accent: #facc15;">
    <div>
      <div class="card-top">
        <div class="track-icon-badge" style="color: #facc15;">⚡</div>
        <span class="track-count-chip">۷۵ سرفصل کامل</span>
      </div>
      <h2 class="track-heading">دانشنامه JavaScript</h2>
      <p class="track-desc">
        موتور V8، پرامیس‌ها، Event Loop، کلوژرها، وب‌ورکرها، ساختارهای داده و بهینه‌سازی حافظه با کنسول زنده.
      </p>
    </div>
    <div>
      <div class="track-progress-row">
        <div class="prog-info">
          <span>میزان تسلط</span>
          <span id="prog-text-javascript">۰ از ۷۵</span>
        </div>
        <div class="prog-track">
          <div class="prog-fill" id="prog-bar-javascript" style="background:#facc15;"></div>
        </div>
      </div>
      <div class="card-actions">
        <a href="javascript/index.html" class="btn-enter" onclick="playClick()">🌐 ورود به وب‌اپلیکیشن</a>
        <a href="javascript/JavaScript_Handbook.pdf" class="btn-pdf" download>📄 دانلود PDF</a>
      </div>
    </div>
  </article>

  <!-- React -->
  <article class="track-card" style="--accent: #06b6d4;">
    <div>
      <div class="card-top">
        <div class="track-icon-badge" style="color: #06b6d4;">⚛️</div>
        <span class="track-count-chip">۶۵ سرفصل + راهنمای معماری</span>
      </div>
      <h2 class="track-heading">دانشنامه React</h2>
      <p class="track-desc">
        هوک‌ها، مدیریت استیت با Zustand و Redux، الگوهای ترکیب، React 19، و راهنمای کامل معماری و پوشه‌بندی.
      </p>
    </div>
    <div>
      <div class="track-progress-row">
        <div class="prog-info">
          <span>میزان تسلط</span>
          <span id="prog-text-react">۰ از ۶۵</span>
        </div>
        <div class="prog-track">
          <div class="prog-fill" id="prog-bar-react" style="background:#06b6d4;"></div>
        </div>
      </div>
      <div class="card-actions">
        <a href="react/index.html" class="btn-enter" onclick="playClick()">🌐 ورود به وب‌اپلیکیشن</a>
        <a href="react/React_Handbook.pdf" class="btn-pdf" download>📄 دانلود PDF</a>
      </div>
    </div>
  </article>

  <!-- Next.js 15 Specialist -->
  <article class="track-card" style="--accent: #ffffff;">
    <div>
      <div class="card-top">
        <div class="track-icon-badge" style="color: #ffffff;">▲</div>
        <span class="track-count-chip">۵ سرفصل تخصصی سرور</span>
      </div>
      <h2 class="track-heading">دانشنامه Next.js 15</h2>
      <p class="track-desc">
        معماری App Router، اکشن‌های سمت سرور ('use server')، میدل‌ورهای Edge، توربوپک و پیش‌رندر جزئی (PPR).
      </p>
    </div>
    <div>
      <div class="track-progress-row">
        <div class="prog-info">
          <span>میزان تسلط</span>
          <span id="prog-text-nextjs">۰ از ۵</span>
        </div>
        <div class="prog-track">
          <div class="prog-fill" id="prog-bar-nextjs" style="background:#ffffff;"></div>
        </div>
      </div>
      <div class="card-actions">
        <a href="nextjs/index.html" class="btn-enter" onclick="playClick()">🌐 ورود به وب‌اپلیکیشن</a>
        <a href="nextjs/NextJS_Handbook.pdf" class="btn-pdf" download>📄 دانلود PDF</a>
      </div>
    </div>
  </article>
</main>

<!-- Command Palette Modal -->
<div class="modal-overlay" id="searchModal" onclick="if(event.target===this) closeSearch();">
  <div class="modal-content">
    <input type="text" class="modal-input" id="globalSearchInput" placeholder="نام مفهوم مورد نظر را جستجو کنید (مثال: Flexbox, useState, Promise)..." oninput="doGlobalSearch(this.value)">
    <ul class="modal-results" id="modalResults">
      <li style="padding:16px; color:var(--text-muted); font-size:12.5px; text-align:center;">برای شروع تایپ کنید...</li>
    </ul>
  </div>
</div>

<script>
// Web Audio API Synthesized Click (Zero External Libs)
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playClick() {
  if (audioCtx.state === 'suspended') audioCtx.resume();
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.type = 'sine';
  osc.frequency.setValueAtTime(800, audioCtx.currentTime);
  osc.frequency.exponentialRampToValueAtTime(400, audioCtx.currentTime + 0.03);
  gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.03);
  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start();
  osc.stop(audioCtx.currentTime + 0.03);
}

function openSearch() {
  document.getElementById('searchModal').classList.add('open');
  const inp = document.getElementById('globalSearchInput');
  inp.focus();
  inp.select();
}
function closeSearch() {
  document.getElementById('searchModal').classList.remove('open');
}

window.addEventListener('keydown', (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault();
    openSearch();
  }
  if (e.key === 'Escape') closeSearch();
});

// Calculate Stats from localStorage
const TRACK_MAP = {
  html: { key: 'erfan_html_completed', total: 35 },
  css: { key: 'erfan_css_completed', total: 62 },
  javascript: { key: 'erfan_javascript_completed', total: 75 },
  react: { key: 'erfan_react_completed', total: 65 },
  nextjs: { key: 'erfan_nextjs_completed', total: 5 }
};

let globalDone = 0;
const globalTotal = 242;

for (const [track, conf] of Object.entries(TRACK_MAP)) {
  try {
    const raw = localStorage.getItem(conf.key);
    const data = raw ? JSON.parse(raw) : {};
    const count = Object.values(data).filter(Boolean).length;
    globalDone += count;
    const pct = Math.round((count / conf.total) * 100);
    
    const txt = document.getElementById(`prog-text-${track}`);
    const bar = document.getElementById(`prog-bar-${track}`);
    if (txt) txt.innerText = `${count} از ${conf.total} (${pct}٪)`;
    if (bar) bar.style.width = `${pct}%`;
  } catch(e) {}
}

document.getElementById('globalCompleted').innerText = globalDone;
document.getElementById('globalPercent').innerText = `${Math.round((globalDone / globalTotal) * 100)}٪`;

function doGlobalSearch(q) {
  q = q.trim().toLowerCase();
  const resBox = document.getElementById('modalResults');
  if (!q) {
    resBox.innerHTML = '<li style="padding:16px; color:var(--text-muted); font-size:12.5px; text-align:center;">برای شروع تایپ کنید...</li>';
    return;
  }
  
  // Sample quick shortcuts
  const items = [
    { title: 'ساختار پایه سند HTML5', track: 'HTML', url: 'html/index.html#topic-1' },
    { title: 'فرم‌ها و انواع Input', track: 'HTML', url: 'html/index.html#topic-11' },
    { title: 'Box Model و Box-sizing', track: 'CSS', url: 'css/index.html#topic-8' },
    { title: 'Flexbox تراز و توزیع', track: 'CSS', url: 'css/index.html#topic-26' },
    { title: 'CSS Grid چیدمان دوسطحی', track: 'CSS', url: 'css/index.html#topic-27' },
    { title: 'Promises و Async/Await', track: 'JavaScript', url: 'javascript/index.html#topic-43' },
    { title: 'Event Loop و Microtasks', track: 'JavaScript', url: 'javascript/index.html#topic-47' },
    { title: 'هوک useState و استیت', track: 'React', url: 'react/index.html#topic-10' },
    { title: 'هوک useEffect و لایف‌سایکل', track: 'React', url: 'react/index.html#topic-14' },
    { title: 'معماری App Router و پوشه‌بندی', track: 'Next.js 15', url: 'nextjs/index.html#topic-1' },
    { title: 'اکشن‌های سمت سرور Server Actions', track: 'Next.js 15', url: 'nextjs/index.html#topic-3' },
    { title: 'Partial Prerendering (PPR)', track: 'Next.js 15', url: 'nextjs/index.html#topic-5' },
  ];
  
  const filtered = items.filter(i => i.title.toLowerCase().includes(q) || i.track.toLowerCase().includes(q));
  if (filtered.length === 0) {
    resBox.innerHTML = '<li style="padding:16px; color:var(--text-muted); font-size:12.5px; text-align:center;">مفهومی یافت نشد.</li>';
    return;
  }
  
  resBox.innerHTML = filtered.map(i => `
    <li>
      <a href="${i.url}" class="modal-item" onclick="playClick()">
        <span class="modal-item-title">${i.title}</span>
        <span class="modal-item-track">${i.track}</span>
      </a>
    </li>
  `).join('');
}
</script>
</body>
</html>
"""

with open("C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub/index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Updated Index Hub with Luxury Precision Dark UI and Live LocalStorage stats!")
