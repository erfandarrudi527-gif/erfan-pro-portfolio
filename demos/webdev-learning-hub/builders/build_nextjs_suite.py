# -*- coding: utf-8 -*-
"""
Generate the standalone Next.js 15 App Router & Server Architecture Handbook & Web App.
Fully independent with its own topics, problems, solutions, sandbox, and Desktop PDF.
"""
import os, sys, json, subprocess

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
BUILDERS_DIR = os.path.join(BASE_DIR, "builders")
sys.path.append(BASE_DIR)
sys.path.append(BUILDERS_DIR)

from nextjs_specialist_suite import NEXTJS_TOPICS

out_dir = os.path.join(BASE_DIR, "nextjs")
os.makedirs(out_dir, exist_ok=True)
html_path = os.path.join(out_dir, "index.html")

sidebar_items_html = ""
cards_html = ""

for t in NEXTJS_TOPICS:
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
    problems = t["problems"]

    lvl_color = "#38bdf8" if lvl == "مبتدی" else ("#f59e0b" if lvl == "متوسط" else "#a855f7")

    sidebar_items_html += f"""
    <li>
      <a href="#topic-{tid}" class="tree-item" data-id="nextjs-{tid}" data-level="{lvl}">
        <div style="display:flex; align-items:center; gap:8px; overflow:hidden;">
          <span class="check-indicator" onclick="event.preventDefault(); toggleComplete('nextjs-{tid}', this)"></span>
          <span class="tree-title" style="white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">{tid}. {title}</span>
        </div>
        <span style="font-size:10px; color:var(--text-muted);">{lvl[:2]}</span>
      </a>
    </li>
    """

    challenges_html = ""
    for ch in problems:
        tier = ch["tier"]
        tier_col = ch["tier_color"]
        tier_bg = ch["tier_bg"]
        ch_title = ch["title"]
        ch_desc = ch["desc"]
        ch_hint = ch["hint"]
        ch_sol = ch["solution"]
        ch_id = f"sol-nextjs-{tid}-{tier}"

        challenges_html += f"""
        <div class="problem-card">
          <div class="problem-top">
            <span class="problem-tier-badge" style="background:{tier_bg}; color:{tier_col}; border:1px solid {tier_col}44;">
              سطح: {tier}
            </span>
            <span class="problem-title-text">{ch_title}</span>
          </div>
          <p class="problem-desc-text">{ch_desc}</p>
          
          <div class="problem-hint-box">
            <span style="font-weight:700; color:#fbbf24;">💡 راهنمایی:</span> {ch_hint}
          </div>

          <div class="problem-action-row">
            <button class="toggle-sol-btn" onclick="const s = document.getElementById('{ch_id}'); const isShow = s.style.display==='block'; s.style.display = isShow ? 'none' : 'block'; this.innerText = isShow ? '👁️ مشاهده پاسخ و حل تشریحی' : '✕ بستن پاسخ';">
              👁️ مشاهده پاسخ و حل تشریحی
            </button>
          </div>

          <div class="solution-container" id="{ch_id}" style="display:none; margin-top:10px;">
            <div style="font-size:11.5px; color:#34d399; font-weight:700; margin-bottom:4px;">کد استاندارد و بهینه پاسخ:</div>
            <div class="code-box">
              <pre><code>{ch_sol.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
            </div>
          </div>
        </div>
        """

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
                  <span class="code-lang-tag">💻 نمونه کد عملیاتی Next.js 15 (TypeScript)</span>
                  <button class="code-action-btn" onclick="copySnippet(this)">📋 کپی کد</button>
                </div>
                <pre><code>{code.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
              </div>
            </div>
          </div>

          <!-- ۳. پیش‌نمایش و آزمایشگاه زنده -->
          <div class="tab-pane pane-sandbox">
            <div class="interactive-sandbox-block">
              <div class="sandbox-card">
                <div class="sandbox-topbar">
                  <div class="sandbox-dots">
                    <span class="sandbox-dot" style="background:#ef4444;"></span>
                    <span class="sandbox-dot" style="background:#f59e0b;"></span>
                    <span class="sandbox-dot" style="background:#10b981;"></span>
                    <span class="sandbox-title-tag">Next.js 15 Server Environment</span>
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
              <p class="production-text">{real}</p>
            </div>
          </div>

          <!-- ۵. دام مصاحبه شغلی -->
          <div class="tab-pane pane-interview">
            <div class="interview-block">
              <p class="interview-text">{interview}</p>
            </div>
          </div>

          <!-- ۶. کارگاه مسئله و تمرین عملی ۳ سطحی -->
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

full_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>دانشنامه تخصصی Next.js 15 | پلتفرم ERFAN.DEV</title>
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
  --bg-deep: #030712;
  --bg-surface: #0b0f19;
  --bg-card: #0f172a;
  --bg-code: #020617;
  --border: #1e293b;
  --border-light: rgba(255, 255, 255, 0.08);
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --accent-next: #ffffff;
  --success: #10b981;
  --amber: #f59e0b;
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
  background-color: var(--bg-deep);
  background-image: 
    radial-gradient(at 0% 0%, rgba(255, 255, 255, 0.04) 0px, transparent 50%),
    radial-gradient(at 100% 100%, rgba(56, 189, 248, 0.04) 0px, transparent 50%),
    linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
  color: var(--text-primary);
  direction: rtl;
  line-height: 1.8;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}}

.top-nav {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(11, 15, 25, 0.92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 10px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
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
  font-size: 16px;
  font-weight: 900;
  letter-spacing: -0.3px;
}}

.track-tabs {{
  display: flex;
  gap: 6px;
  background: rgba(6, 8, 13, 0.6);
  padding: 4px;
  border-radius: 10px;
  border: 1px solid var(--border);
}}
.track-tab {{
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
}}
.track-tab:hover {{
  color: #fff;
  background: rgba(255, 255, 255, 0.05);
}}
.track-tab.active {{
  background: var(--bg-card);
  color: #fff;
  border: 1px solid var(--border-light);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}}

.btn-icon {{
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
}}
.btn-icon:hover {{
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  transform: translateY(-1px);
}}
.btn-primary-glow {{
  background: #ffffff;
  color: #000000 !important;
  font-weight: 900;
  border: none;
}}
.btn-primary-glow:hover {{
  background: #e2e8f0;
}}

/* App Layout */
.app-layout {{
  display: flex;
  max-width: 1440px;
  margin: 0 auto;
  position: relative;
}}

.sidebar {{
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
}}

.main-content {{
  flex: 1;
  min-width: 0;
  padding: 30px 40px 100px;
}}

.progress-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 14px 16px;
}}
.progress-meta {{
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 8px;
}}
.progress-bar-bg {{
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 99px;
  overflow: hidden;
}}
.progress-bar-fill {{
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #10b981, #ffffff);
  border-radius: 99px;
  transition: width 0.3s;
}}

.tree-list {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.tree-item {{
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
}}
.tree-item:hover {{
  background: rgba(255, 255, 255, 0.04);
  color: #fff;
}}
.check-indicator {{
  width: 16px;
  height: 16px;
  border-radius: 4px;
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  cursor: pointer;
}}
.check-indicator.checked {{
  background: var(--success);
  border-color: var(--success);
  color: #000;
}}

.topic-page-header {{
  margin-bottom: 35px;
  padding-bottom: 25px;
  border-bottom: 1px solid var(--border);
}}
.track-pill {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 14px;
  border-radius: 99px;
  font-size: 12px;
  font-weight: 800;
  margin-bottom: 12px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.2);
}}
.topic-page-title {{
  font-size: 32px;
  font-weight: 900;
  margin-bottom: 10px;
  letter-spacing: -0.5px;
}}
.topic-page-desc {{
  font-size: 15px;
  color: var(--text-secondary);
  max-width: 820px;
}}

/* Bento Open Card */
.topic-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 20px;
  margin-bottom: 40px;
  overflow: hidden;
  transition: all 0.25s ease;
  scroll-margin-top: 80px;
  position: relative;
}}
.topic-card:hover {{
  border-color: rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
  transform: translateY(-2px);
}}
.card-topbar {{
  padding: 18px 24px;
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}}
.card-title-group {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.topic-num-badge {{
  background: rgba(255, 255, 255, 0.08);
  color: var(--text-primary);
  font-size: 13px;
  font-weight: 900;
  padding: 4px 12px;
  border-radius: 8px;
}}
.topic-h2 {{
  font-size: 20px;
  font-weight: 900;
  color: #fff;
}}
.complete-toggle-btn {{
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 12.5px;
  font-family: inherit;
  cursor: pointer;
}}
.complete-toggle-btn.is-active {{
  background: rgba(16, 185, 129, 0.15);
  color: var(--success);
  border-color: var(--success);
}}

/* Tabbed Architecture */
.card-tab-nav {{
  display: flex;
  gap: 6px;
  background: rgba(2, 6, 23, 0.7);
  padding: 4px;
  border-radius: 10px;
  border: 1px solid var(--border);
  margin-bottom: 14px;
  flex-wrap: wrap;
}}
.card-tab-btn {{
  flex: 1 1 auto;
  min-width: 130px;
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-secondary);
  padding: 8px 12px;
  border-radius: 7px;
  font-size: 12.5px;
  font-family: inherit;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.15s ease;
}}
.card-tab-btn:hover {{
  color: #fff;
  background: rgba(255, 255, 255, 0.04);
}}
.card-tab-btn.active {{
  background: var(--bg-card);
  color: #38bdf8;
  border-color: rgba(56, 189, 248, 0.35);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}}
.card-tab-content {{
  position: relative;
  min-height: 120px;
}}
.tab-pane {{
  display: none;
  animation: fadeInPane 0.2s ease-in-out;
}}
.tab-pane.active {{
  display: block;
}}
@keyframes fadeInPane {{
  from {{ opacity: 0; transform: translateY(4px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

.card-body-open {{
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}}

.concept-block {{
  display: flex;
  flex-direction: column;
  gap: 12px;
}}
.analogy-subbox {{
  background: rgba(245, 158, 11, 0.08);
  border-right: 4px solid var(--amber);
  border-radius: 10px;
  padding: 14px 18px;
}}
.analogy-subbox .subbox-label {{
  font-size: 13px;
  font-weight: 900;
  color: #fbbf24;
  margin-bottom: 4px;
}}
.analogy-text {{
  font-size: 15px;
  color: #fef3c7;
  line-height: 1.85;
}}
.explain-subbox {{
  background: rgba(56, 189, 248, 0.06);
  border-right: 4px solid #38bdf8;
  border-radius: 10px;
  padding: 14px 18px;
}}
.explain-subbox .subbox-label {{
  font-size: 13px;
  font-weight: 900;
  color: #38bdf8;
  margin-bottom: 4px;
}}
.explain-text {{
  font-size: 14.5px;
  color: #cbd5e1;
  line-height: 1.85;
}}

.block-title {{
  font-size: 14px;
  font-weight: 900;
  margin-bottom: 4px;
}}
.title-blue {{ color: #38bdf8; }}
.title-green {{ color: #34d399; }}
.title-amber {{ color: #fbbf24; }}

.code-box {{
  background: var(--bg-code);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}}
.code-bar {{
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--border);
  padding: 8px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.code-lang-tag {{
  font-family: monospace;
  font-size: 11px;
  color: var(--text-muted);
}}
.code-action-btn {{
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
}}
.code-box pre {{
  padding: 18px 22px;
  overflow-x: auto;
  direction: ltr;
  text-align: left;
}}
.code-box code {{
  font-family: 'Fira Code', monospace;
  font-size: 13.5px;
  line-height: 1.65;
  color: #93c5fd;
}}

.sandbox-card {{
  background: #090d16;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 14px;
  overflow: hidden;
}}
.sandbox-topbar {{
  background: rgba(255, 255, 255, 0.025);
  border-bottom: 1px solid var(--border);
  padding: 8px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.sandbox-dots {{
  display: flex;
  gap: 6px;
}}
.sandbox-dot {{
  width: 9px;
  height: 9px;
  border-radius: 50%;
}}
.sandbox-title-tag {{
  font-size: 11px;
  color: var(--text-muted);
  margin-right: 8px;
}}
.sandbox-badge-active {{
  font-size: 11px;
  color: #10b981;
  font-weight: 700;
}}
.sandbox-body {{
  padding: 20px;
  background: rgba(15, 23, 42, 0.35);
}}

.production-block {{
  background: rgba(16, 185, 129, 0.05);
  border: 1px solid rgba(16, 185, 129, 0.25);
  border-right: 4px solid var(--success);
  border-radius: 10px;
  padding: 16px 20px;
}}
.production-text {{
  font-size: 14.5px;
  color: #a7f3d0;
  line-height: 1.95;
  white-space: pre-line;
}}

.interview-block {{
  background: rgba(245, 158, 11, 0.05);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-right: 4px solid var(--amber);
  border-radius: 10px;
  padding: 16px 20px;
}}
.interview-text {{
  font-size: 14.5px;
  color: #fde68a;
  line-height: 1.85;
}}

.problems-grid {{
  display: flex;
  flex-direction: column;
  gap: 14px;
}}
.problem-card {{
  background: rgba(15, 23, 42, 0.45);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 16px 20px;
}}
.problem-top {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}}
.problem-tier-badge {{
  font-size: 11px;
  font-weight: 900;
  padding: 2px 10px;
  border-radius: 99px;
}}
.problem-title-text {{
  font-size: 14px;
  font-weight: 700;
  color: #fff;
}}
.problem-desc-text {{
  font-size: 13.5px;
  color: #cbd5e1;
  line-height: 1.8;
  margin-bottom: 8px;
}}
.problem-hint-box {{
  font-size: 12.5px;
  color: #94a3b8;
  background: rgba(2, 6, 23, 0.5);
  padding: 8px 12px;
  border-radius: 6px;
  border-right: 3px solid #f59e0b;
  margin-bottom: 10px;
}}
.toggle-sol-btn {{
  background: rgba(168, 85, 247, 0.12);
  border: 1px solid rgba(168, 85, 247, 0.3);
  color: #c084fc;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  font-family: inherit;
  font-weight: 700;
  cursor: pointer;
}}
</style>
</head>
<body>

<header class="top-nav">
  <div style="display:flex; align-items:center; gap:20px;">
    <a href="../index.html" class="brand-section">
      <span style="font-size:22px;">▲</span>
      <div>
        <div style="display:flex; align-items:center; gap:6px;">
          <span class="brand-title">ERFAN.DEV</span>
          <span class="brand-badge">Next.js 15 Specialist</span>
        </div>
      </div>
    </a>

    <nav class="track-tabs">
      <a href="../html/index.html" class="track-tab">🏛️ HTML</a>
      <a href="../css/index.html" class="track-tab">🎨 CSS</a>
      <a href="../javascript/index.html" class="track-tab">⚡ JavaScript</a>
      <a href="../react/index.html" class="track-tab">⚛️ React</a>
      <a href="../nextjs/index.html" class="track-tab active">▲ Next.js 15</a>
    </nav>
  </div>

  <div>
    <a href="NextJS_Handbook.pdf" class="btn-icon btn-primary-glow" download>📄 دانلود PDF اختصاصی Next.js 15</a>
    <button class="btn-icon" onclick="window.print()">🖨️ پرینت</button>
  </div>
</header>

<div class="app-layout">
  <aside class="sidebar">
    <div class="progress-card">
      <div class="progress-meta">
        <span>میزان پیشرفت شما</span>
        <span id="progressText">۰ از {len(NEXTJS_TOPICS)} (۰٪)</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" id="progressBar"></div>
      </div>
    </div>

    <ul class="tree-list" id="treeList">
      {sidebar_items_html}
    </ul>
  </aside>

  <main class="main-content">
    <div class="topic-page-header">
      <span class="track-pill">
        ▲ مسار تخصصی NEXT.JS 15 APP ROUTER
      </span>
      <h1 class="topic-page-title">دانشنامه جامع و تخصصی Next.js 15</h1>
      <p class="topic-page-desc">
        معماری سرور، اکشن‌های فرم، میدل‌ورهای Edge، کامپوننت‌های سروری (RSC)، و پیش‌رندر ناقص (PPR) در یک مستند مجزا و فوق‌العاده ساده.
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

// Sidebar click navigation
document.querySelectorAll('.tree-item').forEach(item => {{
  item.addEventListener('click', (e) => {{
    const href = item.getAttribute('href');
    if (href && href.startsWith('#topic-')) {{
      const tid = href.replace('#topic-', '');
      const el = document.getElementById('topic-' + tid);
      if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
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
print("Next.js 15 Standalone Web App written successfully:", html_path)

# Compile PDF
pdf_path = os.path.join(out_dir, "NextJS_Handbook.pdf")
desktop_pdf = "C:/Users/erfan/Desktop/NextJS_Handbook.pdf"
cmd = [
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--virtual-time-budget=6000",
    f"--print-to-pdf={pdf_path}",
    html_path
]
subprocess.run(cmd, check=True)

with open(pdf_path, "rb") as rf:
    with open(desktop_pdf, "wb") as wf:
        wf.write(rf.read())
print(f"Next.js 15 PDF compiled and placed on Desktop: {desktop_pdf} ({os.path.getsize(desktop_pdf):,} bytes)")
