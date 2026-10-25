# -*- coding: utf-8 -*-
import os, sys, json, subprocess

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
catalog_path = os.path.join(BASE_DIR, "catalog.json")

with open(catalog_path, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Compact catalog for embedding (id, track, title, level, what)
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

TRACK_INFO = {
    "html": {
        "title": "دانشنامه جامع HTML5",
        "subtitle": "۳۵ سرفصل کامل از استخوان‌بندی و فرم‌ها تا سمانتیک، سئو، دسترسی‌پذیری و وب‌کامپوننت‌ها",
        "icon": "🏛️",
        "color": "#f97316",
        "color_soft": "rgba(249, 115, 22, 0.12)",
        "pdf_name": "HTML_Handbook.pdf"
    },
    "css": {
        "title": "دانشنامه جامع CSS3",
        "subtitle": "۶۲ سرفصل کامل از سلکتورها و باکس مدل تا فلکس‌باکس، گرید، انیمیشن، :has و معماری مدرن",
        "icon": "🎨",
        "color": "#38bdf8",
        "color_soft": "rgba(56, 189, 248, 0.12)",
        "pdf_name": "CSS_Handbook.pdf"
    },
    "javascript": {
        "title": "دانشنامه مهندسی JavaScript",
        "subtitle": "۷۵ سرفصل کامل از متغیرها و انواع داده تا کلوژر، ایونت‌لوپ، پرامیس‌ها، الگوهای شی‌گرایی و وب‌ورکرها",
        "icon": "⚡",
        "color": "#facc15",
        "color_soft": "rgba(250, 204, 21, 0.12)",
        "pdf_name": "JavaScript_Handbook.pdf"
    },
    "react": {
        "title": "دانشنامه جامع React & Next.js",
        "subtitle": "۶۵ سرفصل کامل از کامپوننت‌ها و هوک‌های پایه تا استیت منیجمنت، هوک‌های React 19، رندرینگ سرور و استقرار",
        "icon": "⚛️",
        "color": "#67e8f9",
        "color_soft": "rgba(103, 232, 249, 0.12)",
        "pdf_name": "React_Handbook.pdf"
    }
}

SHARED_CSS = """
@font-face {
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Black.ttf') format('truetype');
  font-weight: 900;
}

:root {
  --bg-deep: #06080d;
  --bg-surface: #0b0f19;
  --bg-card: #0f1523;
  --bg-code: #030509;
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
  --amber: #f59e0b;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
  background-color: var(--bg-deep);
  color: var(--text-primary);
  direction: rtl;
  line-height: 1.8;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* Master Top Bar */
.top-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(11, 15, 25, 0.92);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border);
  padding: 10px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--text-primary);
}
.brand-badge {
  font-size: 11px;
  font-weight: 900;
  background: rgba(255, 255, 255, 0.07);
  padding: 3px 8px;
  border-radius: 6px;
  border: 1px solid var(--border-light);
  color: var(--text-secondary);
}
.brand-title {
  font-size: 16px;
  font-weight: 900;
  letter-spacing: -0.3px;
}

.track-tabs {
  display: flex;
  gap: 6px;
  background: rgba(6, 8, 13, 0.6);
  padding: 4px;
  border-radius: 10px;
  border: 1px solid var(--border);
}
.track-tab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: var(--text-secondary);
  transition: all 0.15s ease;
}
.track-tab:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.05);
}
.track-tab.active {
  background: var(--bg-card);
  color: #fff;
  border: 1px solid var(--border-light);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.cmd-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: inherit;
  transition: all 0.2s;
}
.cmd-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--border-light);
  color: var(--text-primary);
}
.cmd-kbd {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 10px;
  font-family: monospace;
}

.btn-icon {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 13px;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s;
}
.btn-icon:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  transform: translateY(-1px);
}
.btn-primary-glow {
  background: #38bdf8;
  color: #04101e !important;
  font-weight: 700;
  border: none;
}
.btn-primary-glow:hover {
  background: #7dd3fc;
}

/* App Main Layout */
.app-layout {
  display: flex;
  max-width: 1440px;
  margin: 0 auto;
  position: relative;
}

.sidebar {
  width: 340px;
  flex-shrink: 0;
  position: sticky;
  top: 57px;
  height: calc(100vh - 57px);
  border-left: 1px solid var(--border);
  background: var(--bg-surface);
  overflow-y: auto;
  padding: 20px 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.sidebar::-webkit-scrollbar { width: 5px; }
.sidebar::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

.main-content {
  flex: 1;
  min-width: 0;
  padding: 30px 40px 100px;
}

/* Progress Block */
.progress-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 14px 16px;
}
.progress-meta {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 8px;
}
.progress-bar-bg {
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 99px;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #10b981, #38bdf8);
  transition: width 0.3s ease;
  border-radius: 99px;
}

/* Sidebar Search & Filter */
.sidebar-search {
  width: 100%;
  background: var(--bg-deep);
  border: 1px solid var(--border);
  color: #fff;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 13px;
  font-family: inherit;
  outline: none;
}
.sidebar-search:focus {
  border-color: #38bdf8;
}

.level-filters {
  display: flex;
  gap: 4px;
}
.l-btn {
  flex: 1;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-muted);
  padding: 4px 6px;
  border-radius: 6px;
  font-size: 11px;
  font-family: inherit;
  cursor: pointer;
  transition: 0.15s;
}
.l-btn.active, .l-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  color: #fff;
  border-color: var(--border-light);
}

/* Sidebar Tree */
.tree-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.tree-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 8px 10px;
  border-radius: 8px;
  font-size: 12.5px;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.15s;
  border: 1px solid transparent;
}
.tree-item:hover {
  background: rgba(255, 255, 255, 0.03);
  color: #fff;
}
.tree-item.active-spy {
  background: rgba(56, 189, 248, 0.08);
  color: #38bdf8;
  border-color: rgba(56, 189, 248, 0.2);
  font-weight: 700;
}
.tree-item.is-completed .tree-title {
  text-decoration: line-through;
  opacity: 0.6;
}
.check-indicator {
  width: 16px;
  height: 16px;
  border-radius: 4px;
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  flex-shrink: 0;
  cursor: pointer;
}
.check-indicator.checked {
  background: var(--success);
  border-color: var(--success);
  color: #000;
  font-weight: 900;
}

/* Header Banner */
.topic-page-header {
  margin-bottom: 35px;
  padding-bottom: 25px;
  border-bottom: 1px solid var(--border);
}
.track-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 99px;
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 12px;
  border: 1px solid;
}
.topic-page-title {
  font-size: 32px;
  font-weight: 900;
  margin-bottom: 10px;
  letter-spacing: -0.5px;
}
.topic-page-desc {
  font-size: 15px;
  color: var(--text-secondary);
  max-width: 820px;
}

/* Topic Card */
.topic-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  margin-bottom: 35px;
  overflow: hidden;
  transition: border-color 0.25s, box-shadow 0.25s;
  scroll-margin-top: 80px;
}
.topic-card:hover {
  border-color: rgba(255, 255, 255, 0.15);
  box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.6);
}
.topic-card.completed-card {
  border-color: rgba(16, 185, 129, 0.4);
}

.card-topbar {
  padding: 18px 24px;
  background: rgba(255, 255, 255, 0.015);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}
.card-title-group {
  display: flex;
  align-items: center;
  gap: 12px;
}
.topic-num-badge {
  background: rgba(255, 255, 255, 0.06);
  color: var(--text-primary);
  font-size: 12px;
  font-weight: 900;
  padding: 3px 10px;
  border-radius: 6px;
  border: 1px solid var(--border-light);
}
.topic-h2 {
  font-size: 20px;
  font-weight: 900;
  color: #fff;
}
.card-meta-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}
.lvl-chip {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 99px;
  border: 1px solid;
}
.complete-toggle-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 5px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: 0.15s;
}
.complete-toggle-btn.is-active {
  background: rgba(16, 185, 129, 0.15);
  color: var(--success);
  border-color: var(--success);
}

/* Card Tabs */
.card-tab-nav {
  display: flex;
  border-bottom: 1px solid var(--border);
  background: rgba(0, 0, 0, 0.2);
  padding: 0 16px;
}
.card-tab-btn {
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--text-muted);
  padding: 12px 16px;
  font-size: 13px;
  font-weight: 700;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s;
}
.card-tab-btn:hover {
  color: var(--text-primary);
}
.card-tab-btn.active {
  color: #38bdf8;
  border-bottom-color: #38bdf8;
}

.card-tab-content {
  padding: 24px;
}
.tab-pane {
  display: none;
}
.tab-pane.active {
  display: block;
}

.section-label {
  font-size: 12px;
  font-weight: 900;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}
.desc-text {
  font-size: 15px;
  color: #cbd5e1;
  line-height: 1.9;
  margin-bottom: 18px;
}

.production-box {
  background: rgba(16, 185, 129, 0.05);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-right: 4px solid var(--success);
  border-radius: 8px;
  padding: 16px 20px;
  margin-bottom: 16px;
}
.production-box h4 {
  color: #6ee7b7;
  font-size: 14px;
  font-weight: 900;
  margin-bottom: 6px;
}
.production-box p {
  color: #a7f3d0;
  font-size: 14px;
  line-height: 1.8;
}

.interview-box {
  background: rgba(245, 158, 11, 0.05);
  border: 1px solid rgba(245, 158, 11, 0.2);
  border-right: 4px solid var(--amber);
  border-radius: 8px;
  padding: 16px 20px;
}
.interview-box h4 {
  color: #fde047;
  font-size: 14px;
  font-weight: 900;
  margin-bottom: 6px;
}
.interview-box p {
  color: #fef08a;
  font-size: 14px;
  line-height: 1.8;
}

/* Code Playground Box */
.code-box {
  background: var(--bg-code);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 14px;
}
.code-bar {
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--border);
  padding: 8px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.code-lang-tag {
  font-family: monospace;
  font-size: 11px;
  color: var(--text-muted);
}
.code-action-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  transition: 0.15s;
}
.code-action-btn:hover {
  background: rgba(255, 255, 255, 0.12);
  color: #fff;
}
.code-box pre {
  padding: 16px 20px;
  overflow-x: auto;
  direction: ltr;
  text-align: left;
}
.code-box code {
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 13.5px;
  line-height: 1.65;
  color: #93c5fd;
}

.run-actions-bar {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}
.run-btn {
  background: #10b981;
  color: #022c22;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 13px;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: 0.2s;
}
.run-btn:hover {
  background: #34d399;
  transform: translateY(-1px);
}
.preview-btn {
  background: #38bdf8;
  color: #04101e;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 13px;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: 0.2s;
}
.preview-btn:hover {
  background: #7dd3fc;
  transform: translateY(-1px);
}

.terminal-console {
  display: none;
  background: #020408;
  border: 1px solid #1e293b;
  border-radius: 8px;
  padding: 14px 18px;
  margin-top: 12px;
  font-family: 'Fira Code', monospace;
  font-size: 12.5px;
  color: #4ade80;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
  line-height: 1.7;
}

.live-dom-preview {
  display: none;
  background: #111827;
  border: 1px solid #374151;
  border-radius: 8px;
  padding: 20px;
  margin-top: 12px;
  direction: rtl;
}

/* Command Palette Modal */
.cmd-modal-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 999;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(10px);
  align-items: flex-start;
  justify-content: center;
  padding-top: 12vh;
}
.cmd-modal-backdrop.open {
  display: flex;
}
.cmd-modal {
  width: 100%;
  max-width: 650px;
  background: var(--bg-surface);
  border: 1px solid var(--border-light);
  border-radius: 16px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
  overflow: hidden;
}
.cmd-search-input {
  width: 100%;
  padding: 18px 22px;
  background: transparent;
  border: none;
  border-bottom: 1px solid var(--border);
  color: #fff;
  font-size: 16px;
  font-family: inherit;
  outline: none;
}
.cmd-results-list {
  max-height: 400px;
  overflow-y: auto;
  padding: 10px;
  list-style: none;
}
.cmd-result-item {
  padding: 12px 16px;
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  transition: 0.15s;
}
.cmd-result-item:hover, .cmd-result-item.selected {
  background: rgba(255, 255, 255, 0.05);
}
.cmd-item-title {
  font-weight: 700;
  font-size: 14px;
  color: #fff;
}
.cmd-item-sub {
  font-size: 12px;
  color: var(--text-muted);
}

/* Toast */
.toast-notice {
  position: fixed;
  bottom: 24px;
  left: 24px;
  background: #10b981;
  color: #022c22;
  font-weight: 700;
  padding: 10px 18px;
  border-radius: 10px;
  font-size: 13px;
  display: none;
  z-index: 1000;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
}

/* Print Rules */
@media print {
  body { background: #fff !important; color: #000 !important; }
  .top-nav, .sidebar, .card-tab-nav, .card-meta-actions, .run-actions-bar, .terminal-console, .live-dom-preview { display: none !important; }
  .app-layout { display: block !important; }
  .main-content { padding: 0 !important; }
  .topic-card { page-break-inside: avoid; border: 1px solid #ccc !important; background: #fff !important; margin-bottom: 30px; }
  .topic-h2 { color: #000 !important; }
  .tab-pane { display: block !important; margin-bottom: 14px; }
  .production-box { background: #f0fdf4 !important; border: 1px solid #86efac !important; color: #000 !important; }
  .production-box p, .production-box h4 { color: #064e3b !important; }
  .interview-box { background: #fffbeb !important; border: 1px solid #fde68a !important; color: #000 !important; }
  .interview-box p, .interview-box h4 { color: #78350f !important; }
  .code-box { background: #f8fafc !important; border-color: #cbd5e1 !important; }
  .code-box code { color: #0f172a !important; }
  .desc-text { color: #1e293b !important; }
}
"""

def generate_track_html(track_key):
    info = TRACK_INFO[track_key]
    track_topics = [t for t in catalog if t["track"] == track_key]
    
    sidebar_items_html = ""
    for t in track_topics:
        tid = t["id"]
        title = t["title"]
        lvl = t["level"]
        sidebar_items_html += f"""
        <li>
          <a href="#topic-{tid}" class="tree-item" data-id="{track_key}-{tid}" data-level="{lvl}">
            <div style="display:flex; align-items:center; gap:8px; overflow:hidden;">
              <span class="check-indicator" onclick="event.preventDefault(); toggleComplete('{track_key}-{tid}', this)"></span>
              <span class="tree-title" style="white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">{tid}. {title}</span>
            </div>
            <span style="font-size:10px; color:var(--text-muted);">{lvl[:2]}</span>
          </a>
        </li>
        """

    cards_html = ""
    for t in track_topics:
        tid = t["id"]
        title = t["title"]
        sub = t.get("sub", "")
        lvl = t["level"]
        what = t.get("what", "")
        does = t.get("does", "")
        real = t.get("real", "")
        code = t.get("code", "")
        interview = t.get("interview", "")
        can_run = t.get("can_run", False)
        has_preview = (track_key in ["html", "css"])

        lvl_color = "#38bdf8" if lvl == "مبتدی" else ("#f59e0b" if lvl == "متوسط" else "#a855f7")

        action_buttons_html = ""
        if can_run:
            action_buttons_html += f"""
            <button class="run-btn" onclick="executeSnippet(this)">▶ اجرای زنده در کنسول</button>
            """
        if has_preview:
            action_buttons_html += f"""
            <button class="preview-btn" onclick="toggleDOMPreview(this)">👁️ پیش‌نمایش المان در صفحه</button>
            """

        bottom_playground_html = ""
        if action_buttons_html:
            bottom_playground_html = f"""
            <div class="run-actions-bar">
              {action_buttons_html}
            </div>
            <div class="terminal-console"></div>
            <div class="live-dom-preview"></div>
            """

        cards_html += f"""
        <article class="topic-card" id="topic-{tid}" data-id="{track_key}-{tid}" data-level="{lvl}">
          <div class="card-topbar">
            <div class="card-title-group">
              <span class="topic-num-badge">#{tid}</span>
              <h2 class="topic-h2">{title}</h2>
            </div>
            <div class="card-meta-actions">
              <span class="lvl-chip" style="background:{lvl_color}18; color:{lvl_color}; border-color:{lvl_color}44;">{lvl}</span>
              <button class="complete-toggle-btn" onclick="toggleCardComplete('{track_key}-{tid}', this)">
                <span class="btn-check-icon">✓</span>
                <span class="btn-check-text">تکمیل شد</span>
              </button>
            </div>
          </div>

          <nav class="card-tab-nav">
            <button class="card-tab-btn active" onclick="switchTab(this, 'tab-concept')">📖 ۱. کالبدشکافی مفهوم</button>
            <button class="card-tab-btn" onclick="switchTab(this, 'tab-real')">💼 ۲. سناریوی واقعی در صنعت</button>
            <button class="card-tab-btn" onclick="switchTab(this, 'tab-code')">💻 ۳. کد و آزمایشگاه</button>
            <button class="card-tab-btn" onclick="switchTab(this, 'tab-interview')">🎯 ۴. دام مصاحبه شغلی</button>
          </nav>

          <div class="card-tab-content">
            <!-- TAB 1: CONCEPT -->
            <div class="tab-pane tab-concept active">
              <div class="section-label">دقیقاً چیه؟</div>
              <p class="desc-text">{what}</p>

              <div class="section-label">چیکار می‌کنه و چه مشکلی رو حل می‌کنه؟</div>
              <p class="desc-text">{does}</p>
            </div>

            <!-- TAB 2: PRODUCTION REAL WORLD -->
            <div class="tab-pane tab-real">
              <div class="production-box">
                <h4>💼 سناریوی صنعتی در دنیای واقعی:</h4>
                <p>{real}</p>
              </div>
            </div>

            <!-- TAB 3: CODE & PLAYGROUND -->
            <div class="tab-pane tab-code">
              <div class="code-box">
                <div class="code-bar">
                  <span class="code-lang-tag">{track_key.upper()} SNIPPET</span>
                  <button class="code-action-btn" onclick="copySnippet(this)">📋 کپی کد</button>
                </div>
                <pre><code>{code.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
              </div>
              {bottom_playground_html}
            </div>

            <!-- TAB 4: INTERVIEW TRAP -->
            <div class="tab-pane tab-interview">
              <div class="interview-box">
                <h4>🎯 دام مصاحبه استخدامی (Interview Pitfall):</h4>
                <p>{interview}</p>
              </div>
            </div>
          </div>
        </article>
        """

    full_page = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{info["title"]} | پلتفرم تخصصی یادگیری فرانت‌اند</title>
<style>
{SHARED_CSS}
</style>
</head>
<body>

<!-- Master Navigation -->
<header class="top-nav">
  <div style="display:flex; align-items:center; gap:20px;">
    <a href="../index.html" class="brand-section">
      <span style="font-size:22px;">{info["icon"]}</span>
      <div>
        <div style="display:flex; align-items:center; gap:6px;">
          <span class="brand-title">ERFAN.DEV</span>
          <span class="brand-badge">Learning OS</span>
        </div>
      </div>
    </a>

    <nav class="track-tabs">
      <a href="../html/index.html" class="track-tab {'active' if track_key == 'html' else ''}">🏛️ HTML (۳۵)</a>
      <a href="../css/index.html" class="track-tab {'active' if track_key == 'css' else ''}">🎨 CSS (۶۲)</a>
      <a href="../javascript/index.html" class="track-tab {'active' if track_key == 'javascript' else ''}">⚡ JavaScript (۷۵)</a>
      <a href="../react/index.html" class="track-tab {'active' if track_key == 'react' else ''}">⚛️ React (۶۵)</a>
    </nav>
  </div>

  <div class="nav-actions">
    <button class="cmd-btn" onclick="openCmdPalette()">
      <span>🔍 جستجوی سریع</span>
      <span class="cmd-kbd">⌘K</span>
    </button>
    <a href="{info['pdf_name']}" class="btn-icon btn-primary-glow" download>📄 دانلود PDF</a>
    <button class="btn-icon" onclick="window.print()">🖨️ پرینت</button>
  </div>
</header>

<div class="app-layout">
  <!-- Right Sticky Sidebar -->
  <aside class="sidebar">
    <div class="progress-card">
      <div class="progress-meta">
        <span>میزان پیشرفت شما</span>
        <span id="progressText">۰ از {len(track_topics)} (۰٪)</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" id="progressBar"></div>
      </div>
    </div>

    <input type="text" id="sidebarSearch" class="sidebar-search" placeholder="🔍 فیلتر سریع در عناوین...">

    <div class="level-filters">
      <button class="l-btn active" data-filter="all">همه</button>
      <button class="l-btn" data-filter="مبتدی">مبتدی</button>
      <button class="l-btn" data-filter="متوسط">متوسط</button>
      <button class="l-btn" data-filter="پیشرفته">پیشرفته</button>
    </div>

    <ul class="tree-list" id="treeList">
      {sidebar_items_html}
    </ul>
  </aside>

  <!-- Main Topic Content -->
  <main class="main-content">
    <div class="topic-page-header">
      <span class="track-pill" style="background:{info['color_soft']}; color:{info['color']}; border-color:{info['color']}44;">
        {info['icon']} مسار یادگیری {track_key.upper()}
      </span>
      <h1 class="topic-page-title">{info['title']}</h1>
      <p class="topic-page-desc">{info['subtitle']}</p>
    </div>

    <section id="cardsContainer">
      {cards_html}
    </section>
  </main>
</div>

<!-- Command Palette Modal -->
<div class="cmd-modal-backdrop" id="cmdBackdrop" onclick="if(event.target === this) closeCmdPalette()">
  <div class="cmd-modal">
    <input type="text" id="cmdInput" class="cmd-search-input" placeholder="جستجو در کل ۲۳۷ سرفصل (HTML, CSS, JS, React)...">
    <ul class="cmd-results-list" id="cmdResults"></ul>
  </div>
</div>

<div class="toast-notice" id="toastNotice"></div>

<script>
const currentTrack = '{track_key}';
// 100% Offline Embedded Catalog Data for instant zero-latency search
const catalogData = {embedded_json_str};

// LocalStorage Progress Management
function getCompleted() {{
  try {{
    return JSON.parse(localStorage.getItem('erfan_dev_completed') || '{{}}');
  }} catch(e) {{
    return {{}};
  }}
}}

function saveCompleted(data) {{
  localStorage.setItem('erfan_dev_completed', JSON.stringify(data));
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

    card.classList.toggle('completed-card', isDone);
    const cardBtn = card.querySelector('.complete-toggle-btn');
    if (cardBtn) {{
      cardBtn.classList.toggle('is-active', isDone);
      cardBtn.querySelector('.btn-check-text').innerText = isDone ? 'تکمیل شد ✓' : 'علامت به عنوان خوانده شده';
    }}

    const treeItem = document.querySelector(`.tree-item[data-id="${{id}}"]`);
    if (treeItem) {{
      treeItem.classList.toggle('is-completed', isDone);
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

// Tab Switcher inside Cards
function switchTab(btn, tabClass) {{
  const card = btn.closest('.topic-card');
  card.querySelectorAll('.card-tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  card.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  card.querySelector('.' + tabClass).classList.add('active');
}}

// Toast helper
function showToast(msg) {{
  const toast = document.getElementById('toastNotice');
  toast.innerText = msg;
  toast.style.display = 'block';
  setTimeout(() => {{ toast.style.display = 'none'; }}, 1800);
}}

// Copy snippet with fallback
function copySnippet(btn) {{
  const code = btn.closest('.code-box').querySelector('pre code').innerText;
  if (navigator.clipboard && navigator.clipboard.writeText) {{
    navigator.clipboard.writeText(code).then(() => {{
      const old = btn.innerText;
      btn.innerText = '✅ کپی شد!';
      showToast('کد در کلیپ‌بورد کپی شد.');
      setTimeout(() => {{ btn.innerText = old; }}, 1600);
    }}).catch(() => fallbackCopy(code, btn));
  }} else {{
    fallbackCopy(code, btn);
  }}
}}

function fallbackCopy(text, btn) {{
  const ta = document.createElement('textarea');
  ta.value = text;
  document.body.appendChild(ta);
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);
  const old = btn.innerText;
  btn.innerText = '✅ کپی شد!';
  showToast('کد در کلیپ‌بورد کپی شد.');
  setTimeout(() => {{ btn.innerText = old; }}, 1600);
}}

// Live JS snippet runner
function executeSnippet(btn) {{
  const card = btn.closest('.topic-card');
  const code = card.querySelector('.code-box pre code').innerText;
  const consoleBox = card.querySelector('.terminal-console');
  consoleBox.style.display = 'block';
  consoleBox.innerText = '⏳ در حال اجرای کد...\\n';

  let logs = [];
  const customConsole = {{
    log: (...args) => logs.push(args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a)).join(' ')),
    error: (...args) => logs.push('[ERROR] ' + args.join(' ')),
    warn: (...args) => logs.push('[WARN] ' + args.join(' '))
  }};

  try {{
    // Strip external import/export statements that fail in Function constructor
    let executableCode = code
      .replace(/^\\s*import\\s+.*?;/gm, '// $&')
      .replace(/^\\s*export\\s+(default\\s+)?/gm, '');

    const runner = new Function('console', executableCode);
    runner(customConsole);
    consoleBox.innerText = logs.length > 0 ? logs.join('\\n') : '✅ کد بدون خطا اجرا شد (هیچ console.log فراخوانی نشد).';
  }} catch(err) {{
    consoleBox.innerText = '❌ خطای زمان اجرا:\\n' + err.message;
  }}
}}

// Live DOM visual preview for HTML/CSS
function toggleDOMPreview(btn) {{
  const card = btn.closest('.topic-card');
  const code = card.querySelector('.code-box pre code').innerText;
  const previewBox = card.querySelector('.live-dom-preview');
  
  if (previewBox.style.display === 'block') {{
    previewBox.style.display = 'none';
    btn.innerText = '👁️ پیش‌نمایش المان در صفحه';
    return;
  }}

  previewBox.style.display = 'block';
  btn.innerText = '✕ بستن پیش‌نمایش';
  
  // Clean snippet for DOM injection
  let domContent = code;
  if (code.includes('<!DOCTYPE') || code.includes('<html')) {{
    // Extract body if full document
    const match = code.match(/<body[^>]*>([\\s\\S]*?)<\\/body>/i);
    if (match) domContent = match[1];
  }}

  previewBox.innerHTML = `
    <div style="font-size:11px; color:#94a3b8; margin-bottom:8px; border-bottom:1px solid #374151; padding-bottom:4px;">
      ✨ پیش‌نمایش رندر واقعی المان در مرورگر:
    </div>
    <div style="padding:10px; background:#1e293b; border-radius:6px; color:#fff;">
      ${{domContent}}
    </div>
  `;
}}

// Sidebar Search and Filter
const sidebarSearch = document.getElementById('sidebarSearch');
const levelBtns = document.querySelectorAll('.l-btn');

function applySidebarFilter() {{
  const q = sidebarSearch.value.toLowerCase().trim();
  const activeLvl = document.querySelector('.l-btn.active').dataset.filter;

  document.querySelectorAll('#treeList li').forEach(li => {{
    const a = li.querySelector('.tree-item');
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

// Scrollspy
window.addEventListener('scroll', () => {{
  const cards = document.querySelectorAll('.topic-card');
  let currentId = '';

  cards.forEach(card => {{
    const rect = card.getBoundingClientRect();
    if (rect.top <= 140 && rect.bottom >= 140) {{
      currentId = card.id;
    }}
  }});

  if (currentId) {{
    document.querySelectorAll('.tree-item').forEach(item => {{
      item.classList.toggle('active-spy', item.getAttribute('href') === '#' + currentId);
    }});
  }}
}});

// Command Palette (Ctrl+K)
function openCmdPalette() {{
  document.getElementById('cmdBackdrop').classList.add('open');
  const inp = document.getElementById('cmdInput');
  inp.value = '';
  inp.focus();
  renderCmdResults('');
}}

function closeCmdPalette() {{
  document.getElementById('cmdBackdrop').classList.remove('open');
}}

document.addEventListener('keydown', (e) => {{
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {{
    e.preventDefault();
    openCmdPalette();
  }}
  if (e.key === 'Escape') {{
    closeCmdPalette();
  }}
}});

const cmdInput = document.getElementById('cmdInput');
const cmdResults = document.getElementById('cmdResults');

cmdInput.addEventListener('input', (e) => {{
  renderCmdResults(e.target.value.toLowerCase().trim());
}});

function renderCmdResults(q) {{
  const filtered = catalogData.filter(item => {{
    if (!q) return true;
    return item.title.toLowerCase().includes(q) || 
           item.track.toLowerCase().includes(q) ||
           (item.sub && item.sub.toLowerCase().includes(q));
  }}).slice(0, 10);

  if (filtered.length === 0) {{
    cmdResults.innerHTML = '<li style="padding:15px; color:#64748b; text-align:center;">موردی یافت نشد.</li>';
    return;
  }}

  cmdResults.innerHTML = filtered.map((item, idx) => `
    <li class="cmd-result-item" onclick="jumpToTopic('${{item.track}}', ${{item.id}})">
      <div>
        <div class="cmd-item-title">${{item.id}}. ${{item.title}}</div>
        <div class="cmd-item-sub">${{item.track.toUpperCase()}} • ${{item.level}}</div>
      </div>
      <span style="font-size:12px; color:var(--text-muted);">↵ پرش</span>
    </li>
  `).join('');
}}

function jumpToTopic(track, id) {{
  closeCmdPalette();
  if (track === currentTrack) {{
    const el = document.getElementById('topic-' + id);
    if (el) el.scrollIntoView({{ behavior: 'smooth' }});
  }} else {{
    window.location.href = `../${{track}}/index.html#topic-${{id}}`;
  }}
}}

// Initialize
updateUIProgress();
</script>

</body>
</html>
"""
    dest_path = os.path.join(BASE_DIR, track_key, "index.html")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_page)
    print(f"Generated High-End Interactive Web App for {track_key}: {dest_path}")

    # Compile PDF via Chrome
    pdf_dest = os.path.join(BASE_DIR, track_key, info["pdf_name"])
    desktop_pdf = os.path.join("C:/Users/erfan/Desktop", info["pdf_name"])
    cmd = [
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=10000",
        f"--print-to-pdf={pdf_dest}",
        dest_path
    ]
    subprocess.run(cmd, check=True)
    
    # Copy to Desktop
    with open(pdf_dest, "rb") as rf:
        with open(desktop_pdf, "wb") as wf:
            wf.write(rf.read())
    print(f"Compiled and copied to Desktop: {desktop_pdf} ({os.path.getsize(desktop_pdf)} bytes)")

# Run for all 4 tracks
for k in ["html", "css", "javascript", "react"]:
    generate_track_html(k)

print("ALL 4 ENHANCED APPS & DESKTOP PDFS COMPILED SUCCESSFULLY!")
