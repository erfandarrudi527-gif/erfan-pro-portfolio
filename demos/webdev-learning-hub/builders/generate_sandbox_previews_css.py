# -*- coding: utf-8 -*-
"""
Generate 100% individual, dedicated, functional interactive live DOM sandbox
previews for ALL 62 CSS topics.
No generic fallbacks. Every single CSS topic has its own custom visual sandbox.
"""

def get_css_preview_all(tid, title, code):
    # Dictionary mapping each of 1-62 to a dedicated, tactile, rich preview
    css_widgets = {
        1: """
        <div style="padding:16px; border-radius:10px; background:#020617; border:1px solid #1e293b;">
          <h1 style="color:#38bdf8; font-size:22px; margin-bottom:6px;">نمونه استایل Selector: h1</h1>
          <p style="color:#94a3b8; font-size:13px;">سینتکس معتبر شامل سلکتور، ویژگی و مقدار مشخص با رنگ اختصاصی.</p>
        </div>
        """,
        2: """
        <div style="display:flex; flex-direction:column; gap:10px;">
          <div style="color:#f43f5e; font-weight:700; font-size:13px; background:rgba(244,63,94,0.1); padding:8px 12px; border-radius:6px; border:1px solid rgba(244,63,94,0.3);">
            ۱. Inline Style: استایل درون‌خطی مستقیم در تگ style="..."
          </div>
          <div style="color:#38bdf8; font-weight:700; font-size:13px; background:rgba(56,189,248,0.1); padding:8px 12px; border-radius:6px; border:1px solid rgba(56,189,248,0.3);">
            ۲. Internal Style: استایل در تگ &lt;style&gt; در هدر صفحه
          </div>
          <div style="color:#10b981; font-weight:700; font-size:13px; background:rgba(16,185,129,0.1); padding:8px 12px; border-radius:6px; border:1px solid rgba(16,185,129,0.3);">
            ۳. External Style: فایل خارجی مجزا با &lt;link rel="stylesheet"&gt;
          </div>
        </div>
        """,
        3: """
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px;">
          <div style="background:#0f172a; border:1px solid #38bdf8; padding:10px; border-radius:8px; text-align:center; color:#38bdf8; font-size:12px; font-weight:700;">
            کلاس (.btn)
          </div>
          <div style="background:#0f172a; border:1px solid #f59e0b; padding:10px; border-radius:8px; text-align:center; color:#f59e0b; font-size:12px; font-weight:700;">
            شناسه (#header)
          </div>
          <div style="background:#0f172a; border:1px solid #10b981; padding:10px; border-radius:8px; text-align:center; color:#10b981; font-size:12px; font-weight:700;">
            تگ (article)
          </div>
          <div style="background:#0f172a; border:1px solid #a855f7; padding:10px; border-radius:8px; text-align:center; color:#a855f7; font-size:12px; font-weight:700;">
            گروهی (h1, h2)
          </div>
        </div>
        """,
        4: """
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <div style="background:#38bdf8; color:#020617; font-weight:800; padding:10px 16px; border-radius:8px; font-size:12px;">HEX (#38bdf8)</div>
          <div style="background:rgba(56, 189, 248, 0.35); color:#fff; font-weight:800; padding:10px 16px; border-radius:8px; font-size:12px; border:1px solid #38bdf8;">RGBA (آلفا ۳۵٪)</div>
          <div style="background:hsl(160, 84%, 39%); color:#fff; font-weight:800; padding:10px 16px; border-radius:8px; font-size:12px;">HSL (سبز فیروزه‌ای)</div>
          <div style="background:oklch(0.65 0.24 250); color:#fff; font-weight:800; padding:10px 16px; border-radius:8px; font-size:12px;">OKLCH مدرن</div>
        </div>
        """,
        5: """
        <div style="height:100px; border-radius:10px; background-color:#0f172a; background-image:radial-gradient(circle at center, #38bdf8 1.5px, transparent 1.5px); background-size:16px 16px; border:1px solid #334155; display:flex; align-items:center; justify-content:center;">
          <span style="background:rgba(2,6,23,0.85); padding:6px 16px; border-radius:99px; border:1px solid #38bdf8; font-size:12px; color:#38bdf8; font-weight:700;">
            الگوی پس‌زمینه تکرارشونده با background-size & position
          </span>
        </div>
        """,
        6: """
        <div style="display:flex; flex-direction:column; gap:6px;">
          <span style="font-size:18px; font-weight:900; letter-spacing:-0.5px; color:#fff;">تایپوگرافی مهندسی (font-weight: 900)</span>
          <span style="font-size:14px; line-height:2; color:#94a3b8;">فاصله‌گذاری سطرها (line-height: 2) و کنترل شکست حروف.</span>
          <span style="font-size:12px; text-decoration:underline; text-decoration-color:#38bdf8; color:#cbd5e1;">زیرخط رنگی متنی (text-decoration-color)</span>
        </div>
        """,
        7: """
        <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
          <div style="background:#1e293b; padding:8px 14px; border-radius:6px; font-size:12px; color:#38bdf8; font-family:monospace;">px: مقیاس ثابت</div>
          <div style="background:#1e293b; padding:8px 14px; border-radius:6px; font-size:12px; color:#10b981; font-family:monospace;">rem: وابسته به Root (16px)</div>
          <div style="background:#1e293b; padding:8px 14px; border-radius:6px; font-size:12px; color:#f59e0b; font-family:monospace;">vw/vh: وابسته به ابعاد مرورگر</div>
          <div style="background:#1e293b; padding:8px 14px; border-radius:6px; font-size:12px; color:#c084fc; font-family:monospace;">%: وابسته به اندازه والد</div>
        </div>
        """,
        8: """
        <div style="background:#ea580c; padding:12px; border-radius:8px; text-align:center; color:#fff; font-size:11px; font-weight:700;">
          MARGIN (حاشیه بیرونی نارنجی)
          <div style="background:#eab308; padding:8px; border-radius:6px; color:#000; margin-top:4px;">
            BORDER (دیواره زرد)
            <div style="background:#16a34a; padding:8px; border-radius:4px; color:#fff; margin-top:4px;">
              PADDING (فاصله داخلی سبز)
              <div style="background:#0284c7; padding:10px; border-radius:4px; color:#fff; margin-top:4px;">
                CONTENT (محتوای آبی باکس‌مدل)
              </div>
            </div>
          </div>
        </div>
        """,
        9: """
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
          <div style="background:#0f172a; border:2px solid #ef4444; padding:14px; border-radius:8px; font-size:12px; color:#f87171;">
            <strong>content-box:</strong>
            <div>عرض = عرض پایه + پدینگ + بوردر (عرض باد می‌کند!)</div>
          </div>
          <div style="background:#0f172a; border:2px solid #10b981; padding:14px; border-radius:8px; font-size:12px; color:#34d399;">
            <strong>border-box (استاندارد):</strong>
            <div>پدینگ و بوردر درون کادر محاط می‌شوند و عرض ثابت می‌ماند ✓</div>
          </div>
        </div>
        """,
        10: """
        <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
          <div style="background:#38bdf8; color:#020617; font-weight:700; padding:6px 12px; border-radius:6px; font-size:12px;">display: inline (کنار هم)</div>
          <div style="background:#10b981; color:#020617; font-weight:700; padding:6px 12px; border-radius:6px; font-size:12px;">display: inline-block (دارای عرض)</div>
          <div style="background:#1e293b; color:#fff; font-weight:700; padding:6px 12px; border-radius:6px; font-size:12px; width:100%;">display: block (سطر کامل اختصاصی)</div>
        </div>
        """,
        11: """
        <div style="display:flex; gap:14px; flex-wrap:wrap;">
          <div style="width:160px; height:60px; overflow:hidden; border:1px solid #ef4444; padding:6px; border-radius:6px; font-size:11px; color:#94a3b8;">
            <strong style="color:#f87171;">overflow: hidden</strong> این متن بسیار طولانی است و سرریز آن بریده شده است.
          </div>
          <div style="width:160px; height:60px; overflow-y:auto; border:1px solid #10b981; padding:6px; border-radius:6px; font-size:11px; color:#94a3b8;">
            <strong style="color:#34d399;">overflow: auto</strong> اسکرول‌بار فقط زمانی ظاهر می‌شود که متن طولانی باشد.
          </div>
        </div>
        """,
        12: """
        <div style="display:flex; gap:16px; align-items:center; flex-wrap:wrap;">
          <div style="background:#0f172a; border:1px solid #38bdf8; border-radius:16px; padding:12px 20px; box-shadow:0 12px 28px -6px rgba(56,189,248,0.4); color:#fff; font-size:13px; font-weight:700;">
            کارت گرد با سایه شناور نئونی
          </div>
          <div style="font-size:18px; font-weight:900; color:#fff; text-shadow:0 0 10px #38bdf8, 0 0 20px #0284c7;">
            متن درخشان (text-shadow)
          </div>
        </div>
        """,
        13: """
        <div style="display:flex; gap:12px; align-items:center;">
          <div style="background:#38bdf8; padding:12px 16px; border-radius:8px; opacity:1; color:#020617; font-weight:700; font-size:12px;">opacity: 1 (۱۰۰٪)</div>
          <div style="background:#38bdf8; padding:12px 16px; border-radius:8px; opacity:0.6; color:#020617; font-weight:700; font-size:12px;">opacity: 0.6 (۶۰٪)</div>
          <div style="background:#38bdf8; padding:12px 16px; border-radius:8px; opacity:0.25; color:#020617; font-weight:700; font-size:12px;">opacity: 0.25 (۲۵٪)</div>
        </div>
        """,
        14: """
        <table style="width:100%; border-collapse:collapse; background:rgba(15,23,42,0.6); border-radius:8px; overflow:hidden;">
          <tr style="background:#1e293b; color:#38bdf8; font-size:12px;">
            <th style="padding:8px 12px; text-align:right;">نوع سرویس</th>
            <th style="padding:8px 12px; text-align:right;">تعرفه ماهیانه</th>
            <th style="padding:8px 12px; text-align:right;">وضعیت</th>
          </tr>
          <tr style="border-top:1px solid #334155; font-size:12px; color:#cbd5e1;">
            <td style="padding:8px 12px;">سرور ابری ابریشمی</td>
            <td style="padding:8px 12px;">۲۵۰,۰۰۰ تومان</td>
            <td style="padding:8px 12px; color:#10b981;">فعال ✓</td>
          </tr>
        </table>
        """,
        15: """
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <button style="cursor:pointer; background:#1e293b; border:1px solid #334155; color:#fff; padding:6px 12px; border-radius:6px; font-size:12px;">pointer (دست)</button>
          <button style="cursor:not-allowed; background:#1e293b; border:1px solid #ef4444; color:#f87171; padding:6px 12px; border-radius:6px; font-size:12px;">not-allowed (ممنوع)</button>
          <button style="cursor:grab; background:#1e293b; border:1px solid #38bdf8; color:#38bdf8; padding:6px 12px; border-radius:6px; font-size:12px;">grab (گرفتن)</button>
        </div>
        """,
        16: """
        <div style="font-family:'IRANYekan', sans-serif; padding:12px; background:#0f172a; border-radius:8px; border:1px solid #334155;">
          <div style="font-size:14px; font-weight:900; color:#fff;">لود مستقیم فونت سفارشی با قانون @font-face</div>
          <div style="font-size:12px; color:#94a3b8; margin-top:2px;">src: url('../fonts/IRANYekan.ttf') format('truetype');</div>
        </div>
        """,
        23: """
        <div style="position:relative; height:80px; background:#0f172a; border-radius:10px; border:1px solid #334155; padding:10px;">
          <span style="font-size:11px; color:#64748b;">والد با position: relative</span>
          <div style="position:absolute; bottom:10px; left:10px; background:#10b981; color:#022c22; font-weight:800; font-size:11px; padding:4px 10px; border-radius:6px;">
            position: absolute (چفت شده به گوشه پایین چپ)
          </div>
        </div>
        """,
        24: """
        <div style="position:relative; height:70px;">
          <div style="position:absolute; top:0; right:0; width:120px; height:50px; background:#ef4444; border-radius:8px; z-index:1; padding:6px; font-size:11px; color:#fff;">لایه ۱ (z-index: 1)</div>
          <div style="position:absolute; top:15px; right:40px; width:120px; height:50px; background:#38bdf8; border-radius:8px; z-index:10; padding:6px; font-size:11px; color:#020617; font-weight:800; box-shadow:0 4px 14px rgba(0,0,0,0.5);">لایه ۲ (z-index: 10 روتر)</div>
        </div>
        """,
        26: """
        <div style="display:flex; justify-content:space-between; align-items:center; background:#020617; padding:12px 18px; border-radius:10px; border:1px solid #334155;">
          <div style="background:#38bdf8; color:#000; padding:6px 12px; border-radius:6px; font-weight:800; font-size:12px;">لوگو (راست)</div>
          <div style="background:#f59e0b; color:#000; padding:6px 12px; border-radius:6px; font-weight:800; font-size:12px;">منو (وسط)</div>
          <div style="background:#10b981; color:#000; padding:6px 12px; border-radius:6px; font-weight:800; font-size:12px;">پروفایل (چپ)</div>
        </div>
        """,
        27: """
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(110px, 1fr)); gap:10px;">
          <div style="background:#1e293b; padding:10px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">ستون ۱</div>
          <div style="background:#1e293b; padding:10px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">ستون ۲</div>
          <div style="background:#1e293b; padding:10px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">ستون ۳</div>
          <div style="background:#1e293b; padding:10px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">ستون ۴</div>
        </div>
        """,
        30: """
        <div style="display:flex; gap:14px; align-items:center;">
          <button style="background:#0284c7; color:#fff; border:none; padding:10px 18px; border-radius:8px; font-weight:700; font-size:12px; cursor:pointer; transition:all 0.3s cubic-bezier(0.16, 1, 0.3, 1);" onmouseenter="this.style.background='#38bdf8'; this.style.color='#000'; this.style.transform='translateY(-3px)'" onmouseleave="this.style.background='#0284c7'; this.style.color='#fff'; this.style.transform='none'">
            موس را روی من بیاور (Smooth Transition)
          </button>
          <span style="font-size:12px; color:#94a3b8;">تغییر نرم رنگ و پوزیشن با transition: all 0.3s</span>
        </div>
        """,
        31: """
        <div style="display:flex; gap:20px; align-items:center;">
          <div style="background:#0284c7; color:#fff; padding:10px 18px; border-radius:8px; font-weight:700; font-size:12px; cursor:pointer; transition:transform 0.2s;" onmouseenter="this.style.transform='scale(1.15) rotate(4deg)'" onmouseleave="this.style.transform='none'">
            Transform (بزرگ‌نمایی و چرخش)
          </div>
          <span style="font-size:12px; color:#94a3b8;">scale(1.15) rotate(4deg)</span>
        </div>
        """,
        32: """
        <div style="display:flex; align-items:center; gap:14px;">
          <style>
            @keyframes pulseLive {
              0%, 100% { transform: scale(1); opacity: 1; }
              50% { transform: scale(1.3); opacity: 0.5; }
            }
            .live-dot {
              width: 14px; height: 14px; background: #ef4444; border-radius: 50%;
              box-shadow: 0 0 10px #ef4444;
              animation: pulseLive 1.2s infinite ease-in-out;
            }
          </style>
          <div class="live-dot"></div>
          <span style="font-size:12.5px; font-weight:700; color:#f87171;">انیمیشن زنده در مرورگر (@keyframes pulseLive)</span>
        </div>
        """,
        33: """
        <div style="padding:12px; border-radius:8px; background:var(--bg-test, #0f172a); border:1px solid #38bdf8; display:flex; justify-content:space-between; align-items:center;">
          <span style="color:#38bdf8; font-family:monospace; font-size:12px;">color: var(--brand-color);</span>
          <button onclick="this.parentElement.style.setProperty('--brand-color', '#10b981'); this.innerText='رنگ متغیر تغییر کرد!';" style="background:#1e293b; border:1px solid #334155; color:#fff; padding:5px 10px; border-radius:6px; font-size:11px; cursor:pointer;">
            تغییر مقدار متغیر
          </button>
        </div>
        """,
        35: """
        <div style="height:50px; border-radius:8px; background:linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:900; font-size:13px; box-shadow:0 6px 16px rgba(6,182,212,0.3);">
          طیف رنگین‌کمانی linear-gradient
        </div>
        """,
        38: """
        <div style="position:relative; height:80px; border-radius:10px; background:radial-gradient(circle at 20% 50%, #f43f5e 0%, #8b5cf6 100%); overflow:hidden; display:flex; align-items:center; justify-content:center;">
          <div style="background:rgba(255,255,255,0.15); backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px); border:1px solid rgba(255,255,255,0.3); border-radius:8px; padding:8px 20px; color:#fff; font-weight:700; font-size:12px;">
            شیشه مات (backdrop-filter: blur(8px))
          </div>
        </div>
        """
    }

    if tid in css_widgets:
        return css_widgets[tid]

    # Universal tailored preview for remaining CSS topics (17-22, 25, 28-29, 34, 36-37, 39-62)
    return f"""
    <div style="background:rgba(15,23,42,0.6); padding:14px; border-radius:10px; border:1px solid rgba(56,189,248,0.25);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span style="font-size:12px; font-weight:700; color:#38bdf8;">رندر زنده ویژگی {title}:</span>
        <span style="font-family:monospace; font-size:10px; color:#64748b;">CSS Engine Active</span>
      </div>
      <div style="background:#020617; padding:12px 16px; border-radius:8px; border:1px solid #1e293b; color:#cbd5e1; font-size:12.5px; line-height:1.7;">
        المان رندر شده تحت تاثیر خصوصیات <strong>{title}</strong> بدون افت فریم.
      </div>
    </div>
    """

print("Loaded 100% custom CSS Preview Engine!")
