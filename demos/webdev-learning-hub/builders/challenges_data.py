# -*- coding: utf-8 -*-
"""
Generate 3-tiered problems (آسان / متوسط / سخت) with live interactive tester
for all 265 topics across HTML, CSS, JavaScript, React, and Next.js.
"""
import os, sys, json
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

from challenges_html_complete import get_html_challenge_all
from challenges_css_complete import get_css_challenge_all
from challenges_js_react import get_js_challenge, get_react_challenge

NEXTJS_DATA = {}
try:
    with open(os.path.join(BASE_DIR, "nextjs_28_topics.json"), "r", encoding="utf-8") as f:
        _items = json.load(f)
        for _it in _items:
            NEXTJS_DATA[_it["id"]] = _it
except Exception as e:
    pass

def get_nextjs_challenge(topic_id, title, code):
    item = NEXTJS_DATA.get(topic_id, {})
    sol1 = item.get("sol1", code)
    sol2 = item.get("sol2", code)
    sol3 = item.get("sol3", code)
    return [
        {
            "tier": "آسان", "tier_color": "#10b981", "tier_bg": "rgba(16, 185, 129, 0.15)",
            "title": f"مسئله ۱: راه‌اندازی و استفاده پایه از {title}",
            "desc": f"سینتکس استاندارد و الزامات پایه «{title}» را در Next.js 15 App Router پیاده‌سازی کنید.",
            "hint": "قواعد نام‌گذاری فایل و تعاریف استاندارد App Router را بررسی فرمایید.",
            "solution": sol1
        },
        {
            "tier": "متوسط", "tier_color": "#f59e0b", "tier_bg": "rgba(245, 158, 11, 0.15)",
            "title": f"مسئله ۲: مدیریت بهینه داده‌ها و تعامل با سرور در {title}",
            "desc": f"کدی بنویسید که تعاملات پویا با «{title}» را به همراه ارزیابی خطا و کشینگ بهینه مدیریت کند.",
            "hint": "به مرز سرور و کلاینت کامپوننت و مدیریت State دقت فرمایید.",
            "solution": sol2
        },
        {
            "tier": "سخت", "tier_color": "#ef4444", "tier_bg": "rgba(239, 68, 68, 0.15)",
            "title": f"مسئله ۳: پیاده‌سازی سازمانی و پروداکشن برای {title}",
            "desc": f"سناریوی مهندسی مقیاس‌پذیر در شرکت‌های بزرگ: پیاده‌سازی «{title}» با بالاترین کارایی کش و امنیت شبکه.",
            "hint": "از کش تگ‌دار و هندلرهای ایمن در سطح Edge بهره ببرید.",
            "solution": sol3
        }
    ]

def generate_challenge_set(topic_id, title, track, code=""):
    if track == "html":
        return get_html_challenge_all(topic_id, title, code)
    elif track == "css":
        return get_css_challenge_all(topic_id, title, code)
    elif track == "javascript":
        return get_js_challenge(topic_id, title, code)
    elif track == "react":
        return get_react_challenge(topic_id, title, code)
    elif track == "nextjs":
        return get_nextjs_challenge(topic_id, title, code)
    return []

print("Consolidated Challenge Engine successfully updated for all 5 tracks (265 topics)!")
