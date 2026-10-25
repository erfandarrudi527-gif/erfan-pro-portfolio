# -*- coding: utf-8 -*-
import os, sys, json, subprocess

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
BUILDERS_DIR = os.path.join(BASE_DIR, "builders")
sys.path.append(BASE_DIR)
sys.path.append(BUILDERS_DIR)

from generate_html_suite import html_topics
from generate_css_suite import css_topics
from enrich_html_data import HTML_ENRICHED
from enrich_css_data import CSS_ENRICHED
from analogies_data import JS_ANALOGIES, REACT_ANALOGIES
from generate_sandbox_previews import get_html_preview, get_react_preview
from generate_sandbox_previews_css import get_css_preview_all
from react_dynamic_widgets import generate_react_widget
from react_architecture_guide import REACT_STRUCTURE_HTML
from nextjs_widgets import get_nextjs_widget
from challenges_data import generate_challenge_set
from js_data_1 import JS_TOPICS as js1
from js_data_2 import JS_TOPICS_2 as js2
from js_data_3 import JS_TOPICS_3 as js3
from react_data_1 import REACT_TOPICS_1 as r1
from react_data_2 import REACT_TOPICS_2 as r2
from react_data_3 import REACT_TOPICS_3 as r3
from exam_data import get_track_exams, render_exam_card
from project_data import render_project_section

# 1. HTML Topics (35)
full_html_list = []
for i, t in enumerate(html_topics, start=1):
    num_title, sub, lvl, ana, exp, code, tip = t
    clean_title = num_title.split(".", 1)[-1].strip() if "." in num_title else num_title
    enr = HTML_ENRICHED.get(i, {})
    full_html_list.append({
        "id": i,
        "track": "html",
        "title": clean_title,
        "sub": sub,
        "level": lvl,
        "analogy": ana,
        "plain_exp": exp,
        "real": enr.get("real", "استفاده در معماری استاندارد فرانت‌اند صفحات وب."),
        "code": code,
        "interview": enr.get("interview", tip),
        "has_dom_preview": True,
        "can_run": False
    })

# 2. CSS Topics (62)
full_css_list = []
for i, t in enumerate(css_topics, start=1):
    num_title, sub, lvl, ana, exp, code, tip = t
    clean_title = num_title.split(".", 1)[-1].strip() if "." in num_title else num_title
    enr = CSS_ENRICHED.get(i, {})
    full_css_list.append({
        "id": i,
        "track": "css",
        "title": clean_title,
        "sub": sub,
        "level": lvl,
        "analogy": ana,
        "plain_exp": exp,
        "real": enr.get("real", "پیاده‌سازی در رابط کاربری اپلیکیشن‌های وب مدرن."),
        "code": code,
        "interview": enr.get("interview", tip),
        "has_dom_preview": True,
        "can_run": False
    })

# 3. JavaScript Topics (75)
all_js_raw = js1 + js2 + js3
full_js_list = []
for item in all_js_raw:
    tid = item["id"]
    js_scenario = f"""🏢 پروژه و سامانه واقعی: هسته پردازشی فرانت‌اند در اپلیکیشن‌های مقیاس‌بزرگ (دیجی‌کالا، اسنپ، صرافی نوبیتکس، تلگرام‌وب)
⚠️ چالش فنی و سناریوی بیزینس: {item['does']}
💡 پیاده‌سازی مهندسی در پروداکشن: {item['real']}"""

    full_js_list.append({
        "id": tid,
        "track": "javascript",
        "title": item["title"],
        "sub": "JavaScript ES6+ / V8 Engine",
        "level": item["level"],
        "analogy": JS_ANALOGIES.get(tid, "تشبیه ملموس و روزمره در دنیای واقعی."),
        "plain_exp": item['what'],
        "real": js_scenario,
        "code": item["code"],
        "interview": "در مصاحبه‌های استخدامی ارشد: روی این مفهوم سوالات تریکی پیرامون نحوه مدیریت حافظه در Call Stack و Heap، رفرنس مشترک اشیاء، و تفاوت صف Microtask با Macrotask پرسیده می‌شود تا تسلط عمیق شما روی موتور V8 سنجیده شود.",
        "has_dom_preview": False,
        "can_run": True
    })

# 4. React Topics (65)
all_react_raw = r1 + r2 + r3
full_react_list = []
for item in all_react_raw:
    tid = item["id"]
    react_scenario = f"""🏢 پروژه و سامانه واقعی: سیستم‌های تک‌صفحه‌ای سازمانی و پنل‌های ادمین پرترافیک (Next.js 15 & React 19)
⚠️ چالش فنی و سناریوی بیزینس: {item['does']}
💡 پیاده‌سازی مهندسی در پروداکشن: {item['real']}"""

    full_react_list.append({
        "id": tid,
        "track": "react",
        "title": item["title"],
        "sub": "React 19 / Modern Architecture",
        "level": item["level"],
        "analogy": REACT_ANALOGIES.get(tid, "تشبیه ملموس و روزمره در دنیای واقعی."),
        "plain_exp": f"{item['what']}\n\nنحوه کارکرد فنی: {item['does']}",
        "real": react_scenario,
        "code": item["code"],
        "interview": f"دام مصاحبه فنی برای {item['title']}: در پروژه‌های پروداکشن، بهینه‌سازی رندر و جلوگیری از نشتی حافظه به دقت توسط مهندس معمار ارزیابی می‌شود.",
        "has_dom_preview": False,
        "can_run": False
    })

# 5. Next.js Topics (28)
full_nextjs_list = []
nextjs_json_path = os.path.join(BUILDERS_DIR, "nextjs_28_topics.json")
if os.path.exists(nextjs_json_path):
    with open(nextjs_json_path, "r", encoding="utf-8") as nf:
        _nextjs_raw = json.load(nf)
        for item in _nextjs_raw:
            full_nextjs_list.append({
                "id": item["id"],
                "track": "nextjs",
                "title": item["title"],
                "sub": item.get("sub", "Next.js 15 App Router & React 19"),
                "level": item.get("level", "متوسط"),
                "analogy": item.get("analogy", "تشبیه ملموس و صنعتی در دنیای واقعی."),
                "plain_exp": item.get("plain_exp", ""),
                "real": item.get("real", "پیاده‌سازی در فروشگاه‌ها و سامانه‌های بزرگ تک‌صفحه‌ای"),
                "code": item.get("code", ""),
                "interview": item.get("interview", ""),
                "has_dom_preview": False,
                "can_run": False
            })

ALL_TRACKS = {
    "html": full_html_list,
    "css": full_css_list,
    "javascript": full_js_list,
    "react": full_react_list,
    "nextjs": full_nextjs_list
}

# Create compact catalog for search
search_catalog = []
for track_name, items in ALL_TRACKS.items():
    for it in items:
        search_catalog.append({
            "id": it["id"],
            "track": track_name,
            "title": it["title"],
            "level": it["level"],
            "sub": it.get("sub", "")
        })

catalog_json_str = json.dumps(search_catalog, ensure_ascii=False).replace('</script>', '<\\/script>')

# Track metadata
TRACK_INFO = {
    "html": {
        "title": "دانشنامه جامع HTML5",
        "subtitle": "۳۵ سرفصل کامل همراه با سناریوهای واقعی در شرکت‌ها و پیش‌نمایش زنده المان‌ها",
        "icon": "🏛️",
        "color": "#f97316",
        "color_soft": "rgba(249, 115, 22, 0.12)",
        "pdf_name": "HTML_Handbook.pdf"
    },
    "css": {
        "title": "دانشنامه جامع CSS3",
        "subtitle": "۶۲ سرفصل کامل همراه با سناریوهای صنعتی و کدهای عملیاتی فرانت‌اند",
        "icon": "🎨",
        "color": "#38bdf8",
        "color_soft": "rgba(56, 189, 248, 0.12)",
        "pdf_name": "CSS_Handbook.pdf"
    },
    "javascript": {
        "title": "دانشنامه مهندسی JavaScript",
        "subtitle": "۷۵ سرفصل کامل همراه با سناریوهای واقعی و کنسول اجرای زنده کدهای JS",
        "icon": "⚡",
        "color": "#facc15",
        "color_soft": "rgba(250, 204, 21, 0.12)",
        "pdf_name": "JavaScript_Handbook.pdf"
    },
    "react": {
        "title": "دانشنامه جامع React 19",
        "subtitle": "۶۵ سرفصل کامل همراه با سناریوهای کاربردی در پروژه‌های واقعی و استقرار",
        "icon": "⚛️",
        "color": "#67e8f9",
        "color_soft": "rgba(103, 232, 249, 0.12)",
        "pdf_name": "React_Handbook.pdf"
    },
    "nextjs": {
        "title": "دانشنامه مهندسی Next.js 15",
        "subtitle": "۲۸ سرفصل فوق‌تخصصی همراه با شبیه‌سازهای تعاملی App Router، کامپوننت‌های RSC، سرور اکشن‌ها و استقرار پروداکشن",
        "icon": "▲",
        "color": "#e2e8f0",
        "color_soft": "rgba(226, 232, 240, 0.12)",
        "pdf_name": "NextJS_Handbook.pdf"
    }
}

from theme_pro import PRO_CSS

from theme_pro import PRO_CSS
SHARED_CSS = PRO_CSS

def generate_track_html(track_key):
    info = TRACK_INFO[track_key]
    track_topics = ALL_TRACKS[track_key]
    track_exams = get_track_exams(track_key)
    exams_by_after_topic = {ex["after_topic"]: ex for ex in track_exams}
    
    # Group topics by difficulty level with counts for clear hierarchy
    level_counts = {"مبتدی": 0, "متوسط": 0, "پیشرفته": 0}
    for t in track_topics:
        lvl = t.get("level", "متوسط")
        if lvl in level_counts:
            level_counts[lvl] += 1

    sidebar_items_html = ""
    seen_levels = set()
    for t in track_topics:
        tid = t["id"]
        title = t["title"]
        lvl = t["level"]

        # Insert stylish group category header on level change
        if lvl not in seen_levels:
            seen_levels.add(lvl)
            lvl_color = "#38bdf8" if lvl == "مبتدی" else ("#f59e0b" if lvl == "متوسط" else "#a855f7")
            lvl_icon = "🌱" if lvl == "مبتدی" else ("⚡" if lvl == "متوسط" else "🚀")
            sidebar_items_html += f"""
            <li class="tree-group-divider" data-group-level="{lvl}" style="color:{lvl_color};">
              <span>{lvl_icon} بخش {lvl}</span>
              <span class="tree-group-badge">{level_counts.get(lvl, 0)} سرفصل</span>
            </li>
            """

        sidebar_items_html += f"""
        <li>
          <a href="#topic-{tid}" class="tree-item" data-id="{track_key}-{tid}" data-level="{lvl}">
            <div style="display:flex; align-items:center; gap:8px; overflow:hidden;">
              <span class="check-indicator" onclick="event.preventDefault(); event.stopPropagation(); toggleComplete('{track_key}-{tid}', this, event)"></span>
              <span class="tree-title" style="white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">{tid}. {title}</span>
            </div>
            <span class="tree-badge">{lvl}</span>
          </a>
        </li>
        """

        if tid in exams_by_after_topic:
            ex_item = exams_by_after_topic[tid]
            sidebar_items_html += f"""
            <li class="tree-exam-wrapper" style="margin:4px 0;">
              <a href="#{ex_item['id']}" class="tree-item tree-exam-pill" style="background:rgba(168,85,247,0.08); border:1px dashed rgba(168,85,247,0.3); color:#c084fc; font-weight:800;">
                <div style="display:flex; align-items:center; gap:6px; overflow:hidden;">
                  <span>🏆</span>
                  <span class="tree-title" style="white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">{ex_item['title']}</span>
                </div>
                <span class="tree-badge" style="color:#c084fc; border-color:rgba(168,85,247,0.35);">آزمون</span>
              </a>
            </li>
            """

    cards_html = ""
    for t in track_topics:
        tid = t["id"]
        title = t["title"]
        sub = t.get("sub", "")
        lvl = t["level"]
        analogy = t.get("analogy", "")
        plain_exp = t.get("plain_exp", "")
        real = t.get("real", "")
        code = t.get("code", "")
        interview = t.get("interview", "")
        can_run = t.get("can_run", False)
        has_dom_preview = t.get("has_dom_preview", False)

        lvl_color = "#38bdf8" if lvl == "مبتدی" else ("#f59e0b" if lvl == "متوسط" else "#a855f7")

        if track_key == "html":
            live_sandbox_html = get_html_preview(tid, code)
        elif track_key == "css":
            live_sandbox_html = get_css_preview_all(tid, title, code)
        elif track_key == "javascript":
            live_sandbox_html = f"""
            <div class="terminal-os-window" style="background:#010409; border:1px solid #1e293b; border-radius:12px; overflow:hidden; box-shadow:0 12px 30px rgba(0,0,0,0.8);">
              <div class="terminal-os-topbar" style="background:rgba(255,255,255,0.02); border-bottom:1px solid #1e293b; padding:8px 14px; display:flex; justify-content:space-between; align-items:center;">
                <div style="display:flex; align-items:center; gap:6px;">
                  <span style="width:10px; height:10px; border-radius:50%; background:#ef4444; display:inline-block;"></span>
                  <span style="width:10px; height:10px; border-radius:50%; background:#f59e0b; display:inline-block;"></span>
                  <span style="width:10px; height:10px; border-radius:50%; background:#10b981; display:inline-block;"></span>
                  <span style="font-family:monospace; font-size:11px; color:#64748b; margin-right:8px;">v8-repl // node-env</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px;">
                  <span class="term-status-badge" style="font-family:monospace; font-size:10px; color:#10b981; background:rgba(16,185,129,0.1); padding:2px 8px; border-radius:4px; border:1px solid rgba(16,185,129,0.25);">IDLE</span>
                  <button class="run-btn" onclick="executeSnippet(this)" style="background:linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color:#fff; border:1px solid rgba(255,255,255,0.15); padding:5px 14px; border-radius:6px; font-weight:700; font-size:11.5px; cursor:pointer; font-family:inherit; transition:all 0.15s;">
                    ⚡ اجرای زنده کد
                  </button>
                </div>
              </div>
              <div class="terminal-body-wrap" style="padding:14px 18px; font-family:'Fira Code', monospace; font-size:12.5px; min-height:85px; direction:ltr; text-align:left; background:rgba(2,6,23,0.7);">
                <div class="term-prompt-line" style="color:#64748b; margin-bottom:6px; display:flex; gap:8px;">
                  <span style="color:#38bdf8;">erfan@dev:~$</span>
                  <span style="color:#94a3b8;">node snippet.js</span>
                </div>
                <div class="terminal-console" style="color:#4ade80; line-height:1.7; white-space:pre-wrap;">
<span style="color:#475569;">// آماده برای ارزیابی. روی «⚡ اجرای زنده کد» کلیک کنید.</span>
                </div>
              </div>
              <div class="terminal-os-footer" style="background:rgba(255,255,255,0.015); border-top:1px solid #1e293b; padding:6px 14px; display:flex; justify-content:space-between; font-family:monospace; font-size:10.5px; color:#475569;">
                <span class="term-time-tag">EXEC_TIME: --</span>
                <span>STATUS: 0 (OK)</span>
              </div>
            </div>
            """
        elif track_key == "react":
            live_sandbox_html = generate_react_widget(tid, title)
        elif track_key == "nextjs":
            live_sandbox_html = get_nextjs_widget(tid, title)

        # Generate 3-tiered problems (آسان / متوسط / سخت)
        challenges = generate_challenge_set(tid, title, track_key, code)
        challenges_cards_html = ""
        for ch in challenges:
            tier = ch.get("tier", "آسان")
            tier_col = ch.get("tier_color", "#10b981" if tier=="آسان" else ("#f59e0b" if tier=="متوسط" else "#ef4444"))
            tier_bg = ch.get("tier_bg", "rgba(16, 185, 129, 0.15)" if tier=="آسان" else ("rgba(245, 158, 11, 0.15)" if tier=="متوسط" else "rgba(239, 68, 68, 0.15)"))
            ch_title = ch.get("title", f"مسئله {tier}")
            ch_desc = ch.get("desc", "")
            ch_hint = ch.get("hint", "")
            ch_sol = ch.get("solution", "")
            ch_id = f"sol-{track_key}-{tid}-{tier}"

            challenges_cards_html += f"""
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
                <button class="toggle-sol-btn" onclick="playAudioClick(); const s = document.getElementById('{ch_id}'); const isShow = s.style.display==='block'; s.style.display = isShow ? 'none' : 'block'; this.innerText = isShow ? '👁️ مشاهده پاسخ و حل تشریحی' : '✕ بستن پاسخ';">
                  👁️ مشاهده پاسخ و حل تشریحی
                </button>
              </div>

              <div class="solution-container" id="{ch_id}" style="display:none; margin-top:10px;">
                  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                    <span style="font-size:11.5px; color:#34d399; font-weight:700;">کد استاندارد و بهینه پاسخ:</span>
                    <button class="code-action-btn" onclick="copySnippet(this)" style="padding:2px 8px; font-size:10.5px;">📋 کپی پاسخ</button>
                  </div>
                <div class="code-box">
                  <pre><code>{ch_sol.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
                </div>
              </div>
            </div>
            """

        # Safe escape for real and interview to avoid unclosed script tags in body
        safe_real = real.replace('<script', '&lt;script').replace('</script>', '&lt;/script&gt;')
        safe_interview = interview.replace('<script', '&lt;script').replace('</script>', '&lt;/script&gt;')

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

          <div class="card-body-open">
            <!-- نوار تب‌های کنار هم برای دسترسی سریع -->
            <nav class="card-tab-nav">
              <button class="card-tab-btn active" onclick="switchTopicTab(this, 'pane-concept')">📖 کالبدشکافی مفهوم</button>
              <button class="card-tab-btn" onclick="switchTopicTab(this, 'pane-code')">💻 نمونه کد تست‌شده</button>
              <button class="card-tab-btn" onclick="switchTopicTab(this, 'pane-sandbox')">🖥️ پیش‌نمایش و المان زنده</button>
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
                      <span class="code-lang-tag">💻 نمونه کد عملیاتی و تست‌شده ({track_key.upper()})</span>
                      <button class="code-action-btn" onclick="copySnippet(this)">📋 کپی کد</button>
                    </div>
                    <pre><code>{code.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
                  </div>
                </div>
              </div>

              <!-- ۳. پیش‌نمایش زنده تعاملی -->
              <div class="tab-pane pane-sandbox">
                <div class="interactive-sandbox-block">
                  <div class="sandbox-card">
                    <div class="sandbox-topbar">
                      <div class="sandbox-dots">
                        <span class="sandbox-dot" style="background:#ef4444;"></span>
                        <span class="sandbox-dot" style="background:#f59e0b;"></span>
                        <span class="sandbox-dot" style="background:#10b981;"></span>
                        <span class="sandbox-title-tag">Live Sandbox ({track_key.upper()})</span>
                      </div>
                      <span class="sandbox-badge-active">رندر فعال در DOM ✓</span>
                    </div>
                    <div class="sandbox-body">
                      {live_sandbox_html}
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

              <!-- ۶. کارگاه مسئله و تمرین عملی ۳ سطحی به عنوان تب اختصاصی -->
              <div class="tab-pane pane-challenges">
                <div class="challenges-section-block">
                  <div class="block-title" style="color:#a855f7; margin-bottom:12px;">
                    <span>🏋️ کارگاه مسئله و تمرین عملی (۳ سطح دشواری با حل کامل و اختصاصی):</span>
                  </div>
                  <div class="problems-grid">
                    {challenges_cards_html}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </article>
        """

        if tid in exams_by_after_topic:
            cards_html += render_exam_card(exams_by_after_topic[tid])

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
  <div style="display:flex; align-items:center; gap:16px;">
    <button class="mobile-toggle-btn" onclick="toggleMobileSidebar()" aria-label="منوی سرفصل‌ها">
      <span>☰</span>
      <span>سرفصل‌ها</span>
    </button>
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
      <a href="../nextjs/index.html" class="track-tab {'active' if track_key == 'nextjs' else ''}">▲ Next.js (۲۸)</a>
      <a href="#real-project-{track_key}" class="track-tab" style="background:rgba(56,189,248,0.12); color:#38bdf8; border:1px solid rgba(56,189,248,0.35);">🚀 پروژه خط به خط</a>
      <a href="#{track_exams[0]['id'] if track_exams else ''}" class="track-tab" style="background:rgba(168,85,247,0.12); color:#c084fc; border:1px solid rgba(168,85,247,0.35);">🏆 آزمون‌ها ({len(track_exams)})</a>
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

<!-- Backdrop for Mobile Sidebar Drawer -->
<div class="sidebar-backdrop" id="sidebarBackdrop" onclick="toggleMobileSidebar()"></div>

<div class="app-layout">
  <!-- Right Sticky Sidebar -->
  <aside class="sidebar" id="appSidebar">
    <button class="sidebar-close-btn" onclick="toggleMobileSidebar()">✕ بستن منو</button>
    <div class="progress-card">
      <div class="progress-meta">
        <span>میزان پیشرفت شما</span>
        <span id="progressText">۰ از {len(track_topics)} (۰٪)</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" id="progressBar"></div>
      </div>
    </div>

    <div class="sidebar-special-links">
      <a href="#real-project-{track_key}" class="sidebar-action-pill pill-project" onclick="playAudioClick()">
        <span>🚀 پروژه جامع و تحلیل خط به خط</span>
        <span>▶</span>
      </a>
      <a href="#{track_exams[0]['id'] if track_exams else ''}" class="sidebar-action-pill pill-exams" onclick="playAudioClick()">
        <span>🏆 آزمون‌های مرحله‌ای ({len(track_exams)} آزمون)</span>
        <span>📝</span>
      </a>
    </div>

    <input type="text" id="sidebarSearch" class="sidebar-search" placeholder="🔍 فیلتر سریع در عناوین...">

    <div class="level-filters">
      <button class="l-btn active" data-filter="all">همه ({len(track_topics)})</button>
      <button class="l-btn" data-filter="مبتدی">مبتدی ({level_counts.get('مبتدی', 0)})</button>
      <button class="l-btn" data-filter="متوسط">متوسط ({level_counts.get('متوسط', 0)})</button>
      <button class="l-btn" data-filter="پیشرفته">پیشرفته ({level_counts.get('پیشرفته', 0)})</button>
    </div>

    <ul class="tree-list" id="treeList">
      {sidebar_items_html}
    </ul>
  </aside>

  <!-- Main Topic Content -->
  <main class="main-content">
    <div class="topic-page-header">
      <span class="track-pill" style="background:{info['color_soft']}; color:{info['color']}; border-color:{info['color']}44; margin-bottom:8px;">
        {info['icon']} مسار یادگیری {track_key.upper()}
      </span>
      <h1 class="topic-page-title">{info['title']}</h1>
      <p class="topic-page-desc">{info['subtitle']}</p>
    </div>

    <!-- Real-World Complete Production Project with Line-by-Line Breakdown -->
    {render_project_section(track_key)}

    <!-- React Architecture Guide -->
    {REACT_STRUCTURE_HTML if track_key == 'react' else ''}

    <section id="cardsContainer">
      {cards_html}
    </section>
  </main>
</div>

<!-- Command Palette Modal -->
<div class="cmd-modal-backdrop" id="cmdBackdrop" onclick="if(event.target === this) closeCmdPalette()">
  <div class="cmd-modal">
    <input type="text" id="cmdInput" class="cmd-search-input" placeholder="جستجو در کل ۲۶۵ سرفصل (HTML, CSS, JS, React, Next.js)...">
    <ul class="cmd-results-list" id="cmdResults"></ul>
  </div>
</div>

<div class="toast-notice" id="toastNotice"></div>

<script>
const currentTrack = '{track_key}';
const catalogData = {catalog_json_str};

// Switch tab inside card with tactile sound
function switchTopicTab(btn, paneClass) {{
  if (typeof playAudioClick === 'function') playAudioClick();
  const card = btn.closest('.topic-card');
  card.querySelectorAll('.card-tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  card.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  const targetPane = card.querySelector('.' + paneClass);
  if (targetPane) targetPane.classList.add('active');
}}

// Switch project tab inside line-by-line real-world project section
function switchProjectTab(btn, paneClass) {{
  if (typeof playAudioClick === 'function') playAudioClick();
  const container = btn.closest('.master-project-section');
  if (!container) return;
  container.querySelectorAll('.proj-tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  container.querySelectorAll('.proj-pane').forEach(p => p.classList.remove('active'));
  const targetPane = container.querySelector('.' + paneClass);
  if (targetPane) targetPane.classList.add('active');
}}

// Web Audio API Tactile Feedback (Zero external libs)
let audioCtx;
function playAudioClick() {{
  try {{
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(400, audioCtx.currentTime + 0.025);
    gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.025);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.025);
  }} catch(e) {{}}
}}

function playSuccessSound() {{
  try {{
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const now = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(523.25, now);
    osc.frequency.setValueAtTime(659.25, now + 0.08);
    osc.frequency.setValueAtTime(783.99, now + 0.16);
    osc.frequency.setValueAtTime(1046.50, now + 0.24);
    gain.gain.setValueAtTime(0.08, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.35);
  }} catch(e) {{}}
}}

// Interactive Exam Evaluation Engine
function handleOptionSelect(optEl, examId, qIndex) {{
  if (typeof playAudioClick === 'function') playAudioClick();
  const questionBox = optEl.closest('.exam-question-box');
  if (!questionBox) return;
  const allOptions = questionBox.querySelectorAll('.exam-option');

  if (questionBox.classList.contains('evaluated')) return;
  questionBox.classList.add('evaluated');

  const isCorrect = optEl.dataset.correct === 'true';
  if (isCorrect) {{
    optEl.classList.add('opt-correct');
    playSuccessSound();
  }} else {{
    optEl.classList.add('opt-wrong');
    allOptions.forEach(opt => {{
      if (opt.dataset.correct === 'true') opt.classList.add('opt-correct');
    }});
  }}

  const explBox = questionBox.querySelector('.exam-expl-box');
  if (explBox) explBox.style.display = 'block';

  updateExamScore(examId);
}}

function updateExamScore(examId) {{
  const examCard = document.getElementById(examId);
  if (!examCard) return;
  const allQuestions = examCard.querySelectorAll('.exam-question-box');
  let correctCount = 0;
  let answeredCount = 0;

  allQuestions.forEach(qBox => {{
    if (qBox.classList.contains('evaluated')) {{
      answeredCount++;
      const selectedCorrect = qBox.querySelector('.exam-option.opt-correct');
      const wrong = qBox.querySelector('.exam-option.opt-wrong');
      if (!wrong && selectedCorrect) correctCount++;
    }}
  }});

  const total = allQuestions.length;
  const pct = total > 0 ? Math.round((correctCount / total) * 100) : 0;
  
  const scoreVal = document.getElementById('score-val-' + examId);
  const scoreFill = document.getElementById('score-fill-' + examId);
  const scoreFb = document.getElementById('score-fb-' + examId);

  if (scoreVal) scoreVal.innerText = `${{correctCount}} از ${{total}} پاسخ صحیح (${{pct}}٪)`;
  if (scoreFill) scoreFill.style.width = `${{pct}}%`;
  
  if (scoreFb) {{
    if (answeredCount === total) {{
      if (pct >= 80) {{
        scoreFb.innerHTML = '<span style="color:#10b981; font-weight:800;">🎉 تبریک! تسلط عالی بر این بخش سرفصل‌ها.</span>';
      }} else if (pct >= 50) {{
        scoreFb.innerHTML = '<span style="color:#f59e0b; font-weight:800;">⚡ نتیجه متوسط. مرور نکات توضیحات به شما کمک می‌کند.</span>';
      }} else {{
        scoreFb.innerHTML = '<span style="color:#ef4444; font-weight:800;">📖 توصیه می‌شود مباحث این بخش را یک بار دیگر با دقت مرور فرمایید.</span>';
      }}
    }} else {{
      scoreFb.innerText = `${{answeredCount}} از ${{total}} سوال پاسخ داده شده است.`;
    }}
  }}

  try {{
    localStorage.setItem('erfan_exam_' + examId, JSON.stringify({{ correctCount, total, pct, answeredCount }}));
  }} catch(e) {{}}
}}

function resetExam(examId) {{
  if (typeof playAudioClick === 'function') playAudioClick();
  const examCard = document.getElementById(examId);
  if (!examCard) return;
  examCard.querySelectorAll('.exam-question-box').forEach(q => {{
    q.classList.remove('evaluated');
    q.querySelectorAll('.exam-option').forEach(opt => {{
      opt.classList.remove('opt-correct', 'opt-wrong');
    }});
    const expl = q.querySelector('.exam-expl-box');
    if (expl) expl.style.display = 'none';
  }});
  const scoreVal = document.getElementById('score-val-' + examId);
  const scoreFill = document.getElementById('score-fill-' + examId);
  const scoreFb = document.getElementById('score-fb-' + examId);
  if (scoreVal) scoreVal.innerText = `۰ از ${{examCard.querySelectorAll('.exam-question-box').length}} پاسخ صحیح`;
  if (scoreFill) scoreFill.style.width = '0%';
  if (scoreFb) scoreFb.innerText = 'برای ارزیابی، گزینه‌های مد نظر خود را انتخاب فرمایید.';
  try {{ localStorage.removeItem('erfan_exam_' + examId); }} catch(e) {{}}
}}

// LocalStorage Progress Management - unified key per track for sync with Hub
function getCompleted() {{
  try {{
    return JSON.parse(localStorage.getItem('erfan_' + currentTrack + '_completed') || '{{}}');
  }} catch(e) {{
    return {{}};
  }}
}}

function saveCompleted(data) {{
  localStorage.setItem('erfan_' + currentTrack + '_completed', JSON.stringify(data));
  updateUIProgress();
}}

function toggleComplete(id, el, evt) {{
  if (evt) {{
    evt.preventDefault();
    evt.stopPropagation();
  }}
  playAudioClick();
  const store = getCompleted();
  store[id] = !store[id];
  saveCompleted(store);
}}

function toggleCardComplete(id, btn) {{
  playAudioClick();
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

function showToast(msg) {{
  const toast = document.getElementById('toastNotice');
  toast.innerText = msg;
  toast.style.display = 'block';
  setTimeout(() => {{ toast.style.display = 'none'; }}, 1800);
}}

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

// Live JS runner with execution telemetry and audio feedback
function executeSnippet(btn) {{
  if (typeof playAudioClick === 'function') playAudioClick();
  const card = btn.closest('.topic-card');
  const code = card.querySelector('.code-box pre code').innerText;
  const consoleBox = card.querySelector('.terminal-console');
  const statusBadge = card.querySelector('.term-status-badge');
  const timeTag = card.querySelector('.term-time-tag');

  if (statusBadge) {{
    statusBadge.innerText = 'RUNNING';
    statusBadge.style.color = '#f59e0b';
    statusBadge.style.background = 'rgba(245,158,11,0.15)';
    statusBadge.style.borderColor = 'rgba(245,158,11,0.3)';
  }}

  consoleBox.innerHTML = '<span style="color:#f59e0b;">⏳ در حال بارگذاری در کانتکست V8...</span>';

  let logs = [];
  const customConsole = {{
    log: (...args) => logs.push(args.map(a => typeof a === 'object' ? JSON.stringify(a, null, 2) : String(a)).join(' ')),
    error: (...args) => logs.push('[ERROR] ' + args.join(' ')),
    warn: (...args) => logs.push('[WARN] ' + args.join(' ')),
    info: (...args) => logs.push('[INFO] ' + args.join(' ')),
    table: (data) => logs.push(typeof data === 'object' ? JSON.stringify(data, null, 2) : String(data))
  }};

  setTimeout(() => {{
    const startTime = performance.now();
    try {{
      // Safeguard against executing raw HTML snippets in JS engine
      const trimmed = code.trim();
      if (trimmed.startsWith('<!DOCTYPE') || trimmed.startsWith('<html') || (trimmed.startsWith('<') && trimmed.includes('</'))) {{
        const elapsed = (performance.now() - startTime).toFixed(2);
        consoleBox.innerHTML = 'ℹ️ <span style="color:#38bdf8;">این سرفصل شامل ساختار سند HTML است. جهت مشاهده خروجی دیداری به تب «پیش‌نمایش و المان زنده» مراجعه نمایید.</span>';
        if (statusBadge) {{
          statusBadge.innerText = 'HTML DOC';
          statusBadge.style.color = '#38bdf8';
          statusBadge.style.background = 'rgba(56,189,248,0.1)';
          statusBadge.style.borderColor = 'rgba(56,189,248,0.25)';
        }}
        if (timeTag) timeTag.innerText = `EXEC_TIME: ${{elapsed}}ms`;
        return;
      }}

      let executableCode = code
        .replace(/^\\s*import\\s+.*?;/gm, '// $&')
        .replace(/^\\s*export\\s+(default\\s+)?/gm, '');

      // Mock safe interactive functions
      const mockAlert = (msg) => logs.push('🔔 [Alert]: ' + msg);
      const mockConfirm = (msg) => {{ logs.push('❓ [Confirm]: ' + msg + ' -> OK (true)'); return true; }};
      const mockPrompt = (msg, def) => {{ logs.push('⌨️ [Prompt]: ' + msg + ' -> "' + (def || 'کاربر نمونه') + '"'); return def || 'کاربر نمونه'; }};

      const runner = new Function('console', 'alert', 'confirm', 'prompt', `return (async () => {{ ${{executableCode}} }})();`);
      const res = runner(customConsole, mockAlert, mockConfirm, mockPrompt);
      if (res && typeof res.then === 'function') {{
        res.then(() => {{
          const elapsed = (performance.now() - startTime).toFixed(2);
          consoleBox.innerText = logs.length > 0 ? logs.join('\\n') : '✅ کد ناهمگام با موفقیت اجرا شد (خروجی ثبت شد).';
          if (statusBadge) {{
            statusBadge.innerText = 'EXIT 0';
            statusBadge.style.color = '#10b981';
            statusBadge.style.background = 'rgba(16,185,129,0.1)';
            statusBadge.style.borderColor = 'rgba(16,185,129,0.25)';
          }}
          if (timeTag) timeTag.innerText = `EXEC_TIME: ${{elapsed}}ms`;
        }}).catch(err => {{
          const elapsed = (performance.now() - startTime).toFixed(2);
          consoleBox.innerText = '❌ خطای زمان اجرا در عملیات ناهمگام (Async Rejection):\\n' + err.message;
          if (statusBadge) {{
            statusBadge.innerText = 'ERROR 1';
            statusBadge.style.color = '#ef4444';
            statusBadge.style.background = 'rgba(239,68,68,0.15)';
            statusBadge.style.borderColor = 'rgba(239,68,68,0.3)';
          }}
          if (timeTag) timeTag.innerText = `EXEC_TIME: ${{elapsed}}ms`;
        }});
      }} else {{
        const elapsed = (performance.now() - startTime).toFixed(2);
        consoleBox.innerText = logs.length > 0 ? logs.join('\\n') : '✅ کد با موفقیت اجرا شد (خروجی در کنسول متنی ثبت شد).';
        if (statusBadge) {{
          statusBadge.innerText = 'EXIT 0';
          statusBadge.style.color = '#10b981';
          statusBadge.style.background = 'rgba(16,185,129,0.1)';
          statusBadge.style.borderColor = 'rgba(16,185,129,0.25)';
        }}
        if (timeTag) timeTag.innerText = `EXEC_TIME: ${{elapsed}}ms`;
      }}
    }} catch(err) {{
      const elapsed = (performance.now() - startTime).toFixed(2);
      consoleBox.innerText = '❌ خطای زمان اجرا (Runtime Exception):\\n' + err.message;
      if (statusBadge) {{
        statusBadge.innerText = 'ERROR 1';
        statusBadge.style.color = '#ef4444';
        statusBadge.style.background = 'rgba(239,68,68,0.15)';
        statusBadge.style.borderColor = 'rgba(239,68,68,0.3)';
      }}
      if (timeTag) timeTag.innerText = `EXEC_TIME: ${{elapsed}}ms`;
    }}
  }}, 120);
}}

// Live DOM preview
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
  
  let domContent = code;
  if (code.includes('<!DOCTYPE') || code.includes('<html')) {{
    const match = code.match(/<body[^>]*>([\\s\\S]*?)<\\/body>/i);
    if (match) domContent = match[1];
  }}

  previewBox.innerHTML = `
    <div style="font-size:11px; color:#94a3b8; margin-bottom:8px; border-bottom:1px solid #334155; padding-bottom:4px;">
      ✨ رندر دیداری المان در مرورگر:
    </div>
    <div style="padding:10px; background:#1e293b; border-radius:6px; color:#fff;">
      ${{domContent}}
    </div>
  `;
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

// Navigation: clean scroll and sidebar highlight on click
function scrollToElement(elId) {{
  const target = document.getElementById(elId);
  if (target) {{
    const headerHeight = document.querySelector('.top-nav')?.offsetHeight || 75;
    const bodyRect = document.body.getBoundingClientRect().top;
    const elementRect = target.getBoundingClientRect().top;
    const elementPosition = elementRect - bodyRect;
    const offsetPosition = elementPosition - headerHeight - 20;

    window.scrollTo({{
      top: offsetPosition,
      behavior: 'smooth'
    }});
  }}
}}

function scrollToTopic(tid) {{
  const targetCard = document.getElementById('topic-' + tid);
  if (targetCard) {{
    const headerHeight = document.querySelector('.top-nav')?.offsetHeight || 75;
    const bodyRect = document.body.getBoundingClientRect().top;
    const elementRect = targetCard.getBoundingClientRect().top;
    const elementPosition = elementRect - bodyRect;
    const offsetPosition = elementPosition - headerHeight - 20;

    window.scrollTo({{
      top: offsetPosition,
      behavior: 'smooth'
    }});

    // Visual highlight on target card
    document.querySelectorAll('.topic-card').forEach(c => c.style.borderColor = '');
    targetCard.style.borderColor = '#38bdf8';
    targetCard.style.boxShadow = '0 0 35px rgba(56, 189, 248, 0.25), 0 16px 36px -12px rgba(0, 0, 0, 0.8)';
    setTimeout(() => {{
      targetCard.style.borderColor = '';
      targetCard.style.boxShadow = '';
    }}, 2000);
  }}
  document.querySelectorAll('.tree-item').forEach(i => i.classList.remove('active-spy'));
  const activeTree = document.querySelector(`.tree-item[data-id="${{currentTrack}}-${{tid}}"]`);
  if (activeTree) activeTree.classList.add('active-spy');
}}

function toggleMobileSidebar() {{
  const sb = document.getElementById('appSidebar');
  const bd = document.getElementById('sidebarBackdrop');
  if (!sb) return;
  const isOpen = sb.classList.contains('mobile-open');
  if (isOpen) {{
    sb.classList.remove('mobile-open');
    if (bd) bd.classList.remove('active');
    document.body.style.overflow = '';
  }} else {{
    sb.classList.add('mobile-open');
    if (bd) bd.classList.add('active');
    document.body.style.overflow = 'hidden';
  }}
}}

// Sidebar click navigates cleanly without any auto-scroll hijacking
document.querySelectorAll('.tree-item, .sidebar-action-pill').forEach(item => {{
  item.addEventListener('click', (e) => {{
    playAudioClick();
    const sb = document.getElementById('appSidebar');
    if (sb && sb.classList.contains('mobile-open')) {{
      toggleMobileSidebar();
    }}
    const href = item.getAttribute('href');
    if (href && href.startsWith('#')) {{
      e.preventDefault();
      const targetId = href.replace('#', '');
      history.pushState(null, null, '#' + targetId);
      if (targetId.startsWith('topic-')) {{
        const tid = parseInt(targetId.replace('topic-', ''));
        scrollToTopic(tid);
      }} else {{
        scrollToElement(targetId);
      }}
    }}
  }});
}});

// Command Palette
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
    cmdResults.innerHTML = '<li style="padding:15px; color:#64748b; text-align:center;">موردی با این عبارت یافت نشد.</li>';
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
    scrollToTopic(id);
  }} else {{
    window.location.href = `../${{track}}/index.html#topic-${{id}}`;
  }}
}}

// Initialize
updateUIProgress();

window.addEventListener('DOMContentLoaded', () => {{
  const hash = window.location.hash;
  if (hash && hash.startsWith('#')) {{
    const targetId = hash.replace('#', '');
    setTimeout(() => {{
      if (targetId.startsWith('topic-')) {{
        const tid = parseInt(targetId.replace('topic-', '')) || 1;
        scrollToTopic(tid);
      }} else {{
        scrollToElement(targetId);
      }}
    }}, 250);
  }}
}});
</script>

</body>
</html>
"""
    dest_path = os.path.join(BASE_DIR, track_key, "index.html")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_page)
    print(f"Generated Fully Open Bento Web App for {track_key}: {dest_path}")

    # Compile PDF from all-topics view
    pdf_dest = os.path.join(BASE_DIR, track_key, info["pdf_name"])
    desktop_pdf = os.path.join("C:/Users/erfan/Desktop", info["pdf_name"])
    
    # Generate standalone full-cards print file for PDF
    print_html_path = os.path.join(BASE_DIR, track_key, "print_booklet.html")
    print_html = full_page.replace("class='focus-active-mode'", "").replace('class="focus-active-mode"', '').replace("focus-active-mode", "")
    with open(print_html_path, "w", encoding="utf-8") as pf:
        pf.write(print_html)

    # Compile PDF only if explicitly requested
    if "--pdf" in sys.argv:
        cmd = [
            "C:/Program Files/Google/Chrome/Application/chrome.exe",
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--virtual-time-budget=12000",
            f"--print-to-pdf={pdf_dest}",
            print_html_path
        ]
        try:
            subprocess.run(cmd, check=True)
            with open(pdf_dest, "rb") as rf:
                with open(desktop_pdf, "wb") as wf:
                    wf.write(rf.read())
            print(f"Compiled and updated on Desktop: {desktop_pdf} ({os.path.getsize(desktop_pdf):,} bytes)")
        except Exception as err:
            print(f"Notice: PDF generation skipped or error ({err})")

for k in ["html", "css", "javascript", "react", "nextjs"]:
    generate_track_html(k)

print("ALL 5 OPEN BENTO APPS COMPILED!")
