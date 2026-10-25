# -*- coding: utf-8 -*-
import os, sys, json, subprocess

BASE_DIR = "C:/Users/erfan/Desktop/WebDev_Master_Learning_Hub"
BUILDERS_DIR = os.path.join(BASE_DIR, "builders")
sys.path.append(BASE_DIR)
sys.path.append(BUILDERS_DIR)

from generate_html_suite import html_topics
from generate_css_suite import css_topics
from js_data_1 import JS_TOPICS as js1
from js_data_2 import JS_TOPICS_2 as js2
from js_data_3 import JS_TOPICS_3 as js3
from react_data_1 import REACT_TOPICS_1 as r1
from react_data_2 import REACT_TOPICS_2 as r2
from react_data_3 import REACT_TOPICS_3 as r3

# 1. Normalize HTML Data
norm_html = []
for i, t in enumerate(html_topics, start=1):
    num_title, sub, lvl, ana, exp, code, tip = t
    clean_title = num_title.split(".", 1)[-1].strip() if "." in num_title else num_title
    norm_html.append({
        "id": i,
        "track": "html",
        "title": clean_title,
        "sub": sub,
        "level": lvl,
        "what": f"{ana} {exp}",
        "does": "ایجاد ساختار سمانتیک، دسترس‌پذیر کردن صفحه برای نابینایان و سئو، و ارسال استاندارد داده‌ها به مرورگر و سرور.",
        "real": f"استفاده در معماری بخش‌های اصلی اپلیکیشن‌های مقیاس‌بزرگ، فروشگاه‌های آنلاین و صفحات فرود.",
        "code": code,
        "interview": tip,
        "has_preview": True
    })

# 2. Normalize CSS Data
norm_css = []
for i, t in enumerate(css_topics, start=1):
    num_title, sub, lvl, ana, exp, code, tip = t
    clean_title = num_title.split(".", 1)[-1].strip() if "." in num_title else num_title
    norm_css.append({
        "id": i,
        "track": "css",
        "title": clean_title,
        "sub": sub,
        "level": lvl,
        "what": f"{ana} {exp}",
        "does": "چیدمان دقیق و ریسپانسیو، بهینه‌سازی کارایی رندر با شتاب‌دهنده گرافیکی (GPU) و طراحی پوسته بدون لگ.",
        "real": "پیاده‌سازی رابط کاربری مدرن در صفحات دسکتاپ و موبایل با پشتیبانی از دارک‌مود و راست‌چین (RTL).",
        "code": code,
        "interview": tip,
        "has_preview": False
    })

# 3. Normalize JS Data
all_js_raw = js1 + js2 + js3
norm_js = []
for item in all_js_raw:
    norm_js.append({
        "id": item["id"],
        "track": "javascript",
        "title": item["title"],
        "sub": "JavaScript ES6+ / V8 Engine",
        "level": item["level"],
        "what": item["what"],
        "does": item["does"],
        "real": item["real"],
        "code": item["code"],
        "interview": "در مصاحبه‌های ارشد: دقت کنید که رفتارهای غافلگیرکننده مثل Type Coercion، تفاوت رفرنس در کپی حافظه، و اولویت اجرای صف Microtask بر Macrotask از سوالات پرتکرار حذف رده‌های پایین هستند.",
        "can_run": True
    })

# 4. Normalize React Data
all_react_raw = r1 + r2 + r3
norm_react = []
for item in all_react_raw:
    norm_react.append({
        "id": item["id"],
        "track": "react",
        "title": item["title"],
        "sub": "React 19 / Modern Architecture",
        "level": item["level"],
        "what": item["what"],
        "does": item["does"],
        "real": item["real"],
        "code": item["code"],
        "interview": "در مصاحبه‌های ارشد: تفاوت فاز Render و Commit در فایبر، چرایی بازگشت تابع تمیزکاری در useEffect، و دلایل اجتناب از Props Drilling با زاستند یا کانتکست تست می‌شود.",
        "can_run": False
    })

# 5. Normalize Next.js Data
nextjs_path = os.path.join(BUILDERS_DIR, "nextjs_28_topics.json")
norm_nextjs = []
if os.path.exists(nextjs_path):
    with open(nextjs_path, "r", encoding="utf-8") as nf:
        nextjs_raw = json.load(nf)
        for item in nextjs_raw:
            norm_nextjs.append({
                "id": item["id"],
                "track": "nextjs",
                "title": item["title"],
                "sub": item.get("sub", "Next.js 15 / App Router"),
                "level": item["level"],
                "what": item.get("plain_exp", ""),
                "does": item.get("does", "معماری رندرینگ سرور و پیش‌رندر هیبریدی App Router"),
                "real": item.get("real", "پیاده‌سازی در فروشگاه‌ها و سامانه‌های بزرگ تک‌صفحه‌ای"),
                "code": item["code"],
                "interview": item.get("interview", ""),
                "can_run": False
            })

print(f"Dataset summary: HTML={len(norm_html)}, CSS={len(norm_css)}, JS={len(norm_js)}, React={len(norm_react)}, Next.js={len(norm_nextjs)}")

# Save normalized JSON bundle for client search
full_catalog = norm_html + norm_css + norm_js + norm_react + norm_nextjs
json_catalog_path = os.path.join(BASE_DIR, "catalog.json")
with open(json_catalog_path, "w", encoding="utf-8") as f:
    json.dump(full_catalog, f, ensure_ascii=False, indent=2)
print("Saved full catalog JSON (265 topics):", json_catalog_path)
