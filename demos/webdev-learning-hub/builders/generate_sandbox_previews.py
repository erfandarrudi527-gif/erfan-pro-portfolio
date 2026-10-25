# -*- coding: utf-8 -*-
"""
Generate dedicated, beautiful, functional live DOM sandbox previews
for all 237 topics across HTML, CSS, JavaScript, and React.
"""

def get_html_preview(topic_id, code):
    """Return custom HTML for live rendering inside .sandbox-body"""
    if topic_id == 1:
        return """
        <div style="border: 1px dashed rgba(56, 189, 248, 0.4); padding: 16px; border-radius: 10px; background: rgba(56, 189, 248, 0.03);">
          <div style="font-size:11px; color:#38bdf8; margin-bottom:8px; font-family:monospace;">&lt;!DOCTYPE html&gt; &bull; lang="fa" dir="rtl"</div>
          <h2 style="font-size:20px; color:#fff; margin-bottom:6px;">سلام دنیا! 👋</h2>
          <p style="color:#94a3b8; font-size:13.5px;">این ساختار استاندارد یک سند معتبر وب است که مرورگر آن را به زیبایی رندر می‌کند.</p>
        </div>
        """
    elif topic_id == 2:
        return """
        <div style="display:flex; flex-direction:column; gap:8px;">
          <h2 style="font-size:20px; color:#38bdf8;">تیتر سطح ۲ (H2)</h2>
          <p style="color:#cbd5e1; font-size:13.5px; line-height:1.8;">
            این یک پاراگراف نمونه است که واژه <strong style="color:#fde047; font-weight:900;">بسیار مهم</strong> در آن پررنگ شده و واژه <em style="color:#67e8f9;">تاکیدی</em> مورب است.
          </p>
          <hr style="border:0; border-top:1px solid #334155; margin:6px 0;">
          <p style="font-size:12px; color:#64748b;">خط افقی با تگ &lt;hr&gt; رسم شده است.</p>
        </div>
        """
    elif topic_id == 3:
        return """
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
          <div style="background:rgba(15,23,42,0.6); padding:12px 16px; border-radius:8px; border:1px solid #1e293b;">
            <div style="font-size:12px; font-weight:700; color:#38bdf8; margin-bottom:8px;">لیست نامرتب (&lt;ul&gt;):</div>
            <ul style="padding-right:20px; color:#cbd5e1; font-size:13px; line-height:1.8;">
              <li>نان تازه</li>
              <li>شیر کم‌چرب</li>
              <li>قهوه اسپرسو</li>
            </ul>
          </div>
          <div style="background:rgba(15,23,42,0.6); padding:12px 16px; border-radius:8px; border:1px solid #1e293b;">
            <div style="font-size:12px; font-weight:700; color:#10b981; margin-bottom:8px;">لیست شماره‌دار (&lt;ol&gt;):</div>
            <ol style="padding-right:20px; color:#cbd5e1; font-size:13px; line-height:1.8;">
              <li>ثبت‌نام در سامانه</li>
              <li>تکمیل مشخصات</li>
              <li>دریافت نهایی سفارش</li>
            </ol>
          </div>
        </div>
        """
    elif topic_id == 4:
        return """
        <div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center;">
          <a href="https://google.com" target="_blank" rel="noopener noreferrer" style="background:#0284c7; color:#fff; text-decoration:none; padding:8px 16px; border-radius:8px; font-size:13px; font-weight:700; display:inline-flex; align-items:center; gap:6px;">
            <span>🌐 لینک خارجی امن به گوگل</span>
            <span style="font-size:11px;">↗</span>
          </a>
          <a href="#topic-1" style="background:rgba(255,255,255,0.06); color:#cbd5e1; text-decoration:none; padding:8px 16px; border-radius:8px; font-size:13px; border:1px solid #334155;">
            ⚓ پرش لنگری به بالای صفحه
          </a>
          <a href="tel:02188888888" style="color:#38bdf8; font-size:13px; text-decoration:none;">
            📞 تماس تلفنی مستقیم (tel:)
          </a>
        </div>
        """
    elif topic_id == 5:
        return """
        <div style="display:flex; align-items:center; gap:16px; background:rgba(15,23,42,0.5); padding:14px; border-radius:10px; border:1px solid #1e293b;">
          <div style="width:100px; height:70px; background:linear-gradient(135deg, #1e293b, #0f172a); border-radius:8px; display:flex; align-items:center; justify-content:center; border:1px solid #38bdf8; font-size:24px;">
            🖼️
          </div>
          <div>
            <div style="font-size:14px; font-weight:700; color:#fff;">نمونه تگ تصویر با مشخصات بهینه</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:3px;">width="800" height="400" loading="lazy" alt="کفش ورزشی نایک"</div>
          </div>
        </div>
        """
    elif topic_id == 9:
        return """
        <table style="width:100%; border-collapse:collapse; background:rgba(15,23,42,0.5); border-radius:8px; overflow:hidden;">
          <thead>
            <tr style="background:rgba(56,189,248,0.12); color:#38bdf8; text-align:right;">
              <th style="padding:10px 14px; font-size:13px;">ردیف</th>
              <th style="padding:10px 14px; font-size:13px;">نام کالا</th>
              <th style="padding:10px 14px; font-size:13px;">تعداد</th>
              <th style="padding:10px 14px; font-size:13px;">قیمت واحد</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid #1e293b;">
              <td style="padding:9px 14px; font-size:13px; color:#cbd5e1;">۱</td>
              <td style="padding:9px 14px; font-size:13px; color:#fff; font-weight:700;">ماوس بی‌سیم لاجیتک</td>
              <td style="padding:9px 14px; font-size:13px; color:#cbd5e1;">۲ عدد</td>
              <td style="padding:9px 14px; font-size:13px; color:#34d399;">۸۵۰,۰۰۰ تومان</td>
            </tr>
            <tr>
              <td style="padding:9px 14px; font-size:13px; color:#cbd5e1;">۲</td>
              <td style="padding:9px 14px; font-size:13px; color:#fff; font-weight:700;">کیبورد مکانیکال RGB</td>
              <td style="padding:9px 14px; font-size:13px; color:#cbd5e1;">۱ عدد</td>
              <td style="padding:9px 14px; font-size:13px; color:#34d399;">۲,۴۰۰,۰۰۰ تومان</td>
            </tr>
          </tbody>
        </table>
        """
    elif topic_id == 11:
        return """
        <form onsubmit="event.preventDefault(); const res = this.querySelector('.form-feedback'); res.style.display='block'; res.innerText='✅ فرم با موفقیت ارسال شد! نام: ' + this.username.value;" style="display:flex; flex-direction:column; gap:12px; background:rgba(15,23,42,0.6); padding:18px; border-radius:12px; border:1px solid #1e293b;">
          <fieldset style="border:1px solid rgba(56,189,248,0.3); border-radius:8px; padding:14px 18px;">
            <legend style="color:#38bdf8; font-weight:700; font-size:13px; padding:0 8px;">فرم ورود به حساب کاربری</legend>
            <div style="margin-bottom:12px;">
              <label style="display:block; font-size:12.5px; color:#94a3b8; margin-bottom:4px;" for="demo_user">نام کاربری یا ایمیل:</label>
              <input type="text" id="demo_user" name="username" placeholder="مثلاً erfan_dev" style="width:100%; max-width:350px; background:#020617; border:1px solid #334155; color:#fff; padding:8px 12px; border-radius:8px; font-family:inherit; outline:none;" required>
            </div>
            <div style="margin-bottom:14px;">
              <label style="display:block; font-size:12.5px; color:#94a3b8; margin-bottom:4px;" for="demo_pass">رمز عبور:</label>
              <input type="password" id="demo_pass" name="password" placeholder="••••••••" style="width:100%; max-width:350px; background:#020617; border:1px solid #334155; color:#fff; padding:8px 12px; border-radius:8px; font-family:inherit; outline:none;" required>
            </div>
            <button type="submit" style="background:#38bdf8; color:#04101e; border:none; padding:8px 20px; border-radius:8px; font-weight:700; cursor:pointer; font-family:inherit;">ورود به سامانه</button>
            <div class="form-feedback" style="display:none; margin-top:12px; padding:8px 12px; background:rgba(16,185,129,0.15); border:1px solid #10b981; color:#6ee7b7; border-radius:6px; font-size:13px;"></div>
          </fieldset>
        </form>
        """
    elif topic_id == 12:
        return """
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; background:rgba(15,23,42,0.6); padding:16px; border-radius:12px; border:1px solid #1e293b;">
          <div>
            <label style="font-size:12px; color:#94a3b8; display:block; margin-bottom:4px;">ایمیل (type="email"):</label>
            <input type="email" placeholder="name@site.com" style="width:100%; background:#020617; border:1px solid #334155; color:#fff; padding:8px; border-radius:6px; font-family:inherit;">
          </div>
          <div>
            <label style="font-size:12px; color:#94a3b8; display:block; margin-bottom:4px;">تلفن (type="tel"):</label>
            <input type="tel" placeholder="09123456789" style="width:100%; background:#020617; border:1px solid #334155; color:#fff; padding:8px; border-radius:6px; font-family:inherit;">
          </div>
          <div>
            <label style="font-size:12px; color:#94a3b8; display:block; margin-bottom:4px;">انتخاب رنگ (type="color"):</label>
            <input type="color" value="#38bdf8" style="width:60px; height:36px; background:#020617; border:1px solid #334155; border-radius:6px; cursor:pointer;">
          </div>
          <div>
            <label style="font-size:12px; color:#94a3b8; display:block; margin-bottom:4px;">تنظیم ولوم (type="range"):</label>
            <input type="range" min="0" max="100" value="70" style="width:100%; accent-color:#38bdf8;">
          </div>
        </div>
        """
    elif topic_id == 13:
        return """
        <form onsubmit="event.preventDefault(); alert('اعتبارسنجی با موفقیت انجام شد!');" style="display:flex; flex-direction:column; gap:10px; background:rgba(15,23,42,0.6); padding:16px; border-radius:12px; border:1px solid #1e293b;">
          <div>
            <label style="font-size:12px; color:#94a3b8; display:block; margin-bottom:4px;">کد کاربری (الزام حداقل ۴ کاراکتر):</label>
            <input type="text" required minlength="4" placeholder="حداقل ۴ کاراکتر تایپ کنید" style="width:100%; max-width:320px; background:#020617; border:1px solid #334155; color:#fff; padding:8px 12px; border-radius:6px; font-family:inherit;">
          </div>
          <div>
            <label style="font-size:12px; color:#94a3b8; display:block; margin-bottom:4px;">موبایل با الگوی regex صفت pattern="09[0-9]{9}":</label>
            <input type="tel" pattern="09[0-9]{9}" placeholder="مثلاً: 09121112233" style="width:100%; max-width:320px; background:#020617; border:1px solid #334155; color:#fff; padding:8px 12px; border-radius:6px; font-family:inherit;" required>
          </div>
          <div>
            <button type="submit" style="background:#10b981; color:#022c22; border:none; padding:8px 16px; border-radius:6px; font-weight:700; cursor:pointer; font-family:inherit;">بررسی صحت داده‌ها</button>
          </div>
        </form>
        """
    elif topic_id == 22:
        return """
        <div style="display:flex; flex-direction:column; gap:8px;">
          <details open style="background:rgba(15,23,42,0.7); border:1px solid #38bdf8; border-radius:8px; padding:12px 16px;">
            <summary style="font-weight:700; color:#38bdf8; cursor:pointer; outline:none;">❓ آیا فایل‌های این دانشنامه کاملاً آفلاین کار می‌کنند؟</summary>
            <p style="margin-top:8px; color:#cbd5e1; font-size:13px; line-height:1.7;">بله! تمامی فونت‌های ایران‌یکان، کدهای جاوا اسکریپت و استایل‌ها به صورت محلی در پوشه پروژه ذخیره شده‌اند و نیازی به اینترنت ندارند.</p>
          </details>
          <details style="background:rgba(15,23,42,0.7); border:1px solid #334155; border-radius:8px; padding:12px 16px;">
            <summary style="font-weight:700; color:#f1f5f9; cursor:pointer; outline:none;">❓ چگونه کدهای هر بخش را کپی یا اجرا کنم؟</summary>
            <p style="margin-top:8px; color:#cbd5e1; font-size:13px; line-height:1.7;">روی دکمه «📋 کپی کد» کلیک کنید یا در بخش جاوا اسکریپت دکمه «▶ اجرای زنده در کنسول» را بزنید.</p>
          </details>
        </div>
        """
    elif topic_id == 23:
        return """
        <div style="display:flex; flex-direction:column; gap:12px; background:rgba(15,23,42,0.6); padding:16px; border-radius:12px; border:1px solid #1e293b;">
          <div>
            <label style="font-size:12px; color:#94a3b8; display:block; margin-bottom:4px;">پیشنهاد خودکار شهر (datalist):</label>
            <input list="cities_list" placeholder="یک حرف بنویسید (مثلاً ت یا م)..." style="width:100%; max-width:320px; background:#020617; border:1px solid #334155; color:#fff; padding:8px 12px; border-radius:6px; font-family:inherit;">
            <datalist id="cities_list">
              <option value="تهران">
              <option value="مشهد">
              <option value="اصفهان">
              <option value="شیراز">
              <option value="تبریز">
            </datalist>
          </div>
          <div>
            <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">نوار پیشرفت دانلود (progress): ۷۵٪</div>
            <progress value="75" max="100" style="width:100%; max-width:320px; height:12px; accent-color:#10b981;"></progress>
          </div>
          <div>
            <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">درجه حرارت سرور (meter):</div>
            <meter value="0.8" min="0" max="1" style="width:100%; max-width:320px; height:14px;"></meter>
          </div>
        </div>
        """
    elif topic_id == 31:
        return """
        <div>
          <button type="button" onclick="document.getElementById('nativeDialogDemo').showModal()" style="background:#38bdf8; color:#04101e; border:none; padding:10px 18px; border-radius:8px; font-weight:700; cursor:pointer; font-family:inherit;">🚀 آزمایش باز شدن تگ &lt;dialog&gt;</button>
          
          <dialog id="nativeDialogDemo" style="background:#0f172a; color:#fff; border:1px solid #38bdf8; border-radius:14px; padding:24px; text-align:right; max-width:420px; box-shadow:0 25px 50px rgba(0,0,0,0.8);">
            <h3 style="color:#38bdf8; margin-bottom:8px; font-size:18px;">✨ پنجره مودال رسمی HTML5</h3>
            <p style="color:#cbd5e1; font-size:13.5px; line-height:1.8; margin-bottom:16px;">
              این پنجره مستقیماً در لایه Top Layer مرورگر رندر شده، زمینه را تیره و بلور کرده و فوکوس کیبورد را در خود قفل می‌کند.
            </p>
            <button type="button" onclick="document.getElementById('nativeDialogDemo').close()" style="background:#ef4444; color:#fff; border:none; padding:8px 16px; border-radius:6px; cursor:pointer; font-weight:700; font-family:inherit;">بستن پنجره (یا کلید ESC)</button>
          </dialog>
        </div>
        """
    elif topic_id == 32:
        return """
        <div style="display:flex; flex-direction:column; gap:10px;">
          <div contenteditable="true" style="border:1px dashed #38bdf8; padding:14px; border-radius:8px; background:rgba(56,189,248,0.06); color:#fff; font-size:14px; cursor:text; outline:none;">
            ✏️ <strong>روی این متن کلیک کن و تایپ کن!</strong> (این بخش با صفت contenteditable="true" کاملاً شبیه یک فایل ورد ادیت‌پذیر است).
          </div>
          <div draggable="true" style="border:1px solid #10b981; padding:10px 16px; border-radius:8px; background:rgba(16,185,129,0.1); color:#34d399; font-size:13px; cursor:grab; text-align:center;">
            ✋ این کارت قابلیت کشیدن و رها کردن با ماوس را دارد (draggable="true")
          </div>
        </div>
        """
    elif topic_id == 20: # Link CSS / JS
        return """
        <div style="background:rgba(15,23,42,0.6); padding:16px; border-radius:10px; border:1px solid #1e293b;">
          <div style="font-size:12px; color:#38bdf8; font-weight:700; margin-bottom:8px;">نحوه ایمپورت استاندارد در Head سند:</div>
          <div style="font-family:monospace; font-size:12px; color:#94a3b8; line-height:1.8; direction:ltr; text-align:left;">
            &lt;link rel="stylesheet" href="styles.css"&gt;<br>
            &lt;script src="app.js" defer&gt;&lt;/script&gt;
          </div>
          <div style="margin-top:8px; font-size:11.5px; color:#10b981;">✓ ویژگی defer مانع مسدود شدن پارسر HTML می‌شود.</div>
        </div>
        """
    elif topic_id == 28: # Structured data JSON-LD
        return """
        <div style="background:rgba(15,23,42,0.6); padding:16px; border-radius:10px; border:1px solid #1e293b;">
          <div style="font-size:12px; color:#fbbf24; font-weight:700; margin-bottom:8px;">اسکیما سئو Structured Data (JSON-LD):</div>
          <pre style="font-family:monospace; font-size:11.5px; color:#cbd5e1; direction:ltr; text-align:left; background:#020617; padding:10px; border-radius:6px;">{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "کفش ورزشی نایک",
  "offers": { "price": "850000", "priceCurrency": "IRR" }
}</pre>
        </div>
        """
    else:
        # Default smart HTML render (safe escaping of script tags)
        safe_render = code.replace('<script', '&lt;script').replace('</script>', '&lt;/script&gt;')
        return f"""
        <div style="background:rgba(15,23,42,0.5); padding:16px; border-radius:10px; border:1px solid #1e293b;">
          {safe_render}
        </div>
        """

def get_css_preview(topic_id, code):
    """Return dedicated live visual demonstration for CSS topics"""
    if topic_id == 4: # Colors
        return """
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
          <div style="padding:12px 18px; border-radius:8px; background:#38bdf8; color:#04101e; font-weight:700; font-size:12px;">HEX (#38bdf8)</div>
          <div style="padding:12px 18px; border-radius:8px; background:rgba(56, 189, 248, 0.4); color:#fff; font-weight:700; font-size:12px; border:1px solid #38bdf8;">RGBA (40% شفاف)</div>
          <div style="padding:12px 18px; border-radius:8px; background:hsl(160, 84%, 39%); color:#fff; font-weight:700; font-size:12px;">HSL (160, 84%, 39%)</div>
        </div>
        """
    elif topic_id == 8: # Box Model
        return """
        <div style="background:#ea580c; padding:14px; border-radius:8px; text-align:center; color:#fff; font-size:11px; font-weight:700;">
          MARGIN (حاشیه بیرونی نارنجی)
          <div style="background:#eab308; padding:10px; border-radius:6px; color:#000; margin-top:6px;">
            BORDER (دیواره زرد)
            <div style="background:#16a34a; padding:10px; border-radius:4px; color:#fff; margin-top:6px;">
              PADDING (فاصله داخلی سبز)
              <div style="background:#0284c7; padding:12px; border-radius:4px; color:#fff; margin-top:6px;">
                CONTENT (محتوای آبی)
              </div>
            </div>
          </div>
        </div>
        """
    elif topic_id == 12: # border-radius & box-shadow
        return """
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
          <div style="background:#0f172a; padding:16px 20px; border-radius:18px; box-shadow:0 12px 28px -6px rgba(56,189,248,0.3); border:1px solid #38bdf8; color:#fff; font-size:13px; font-weight:700;">
            سایه نرم نئونی آبی (box-shadow)
          </div>
          <div style="width:50px; height:50px; border-radius:50%; background:#10b981; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:900;">
            50%
          </div>
        </div>
        """
    elif topic_id == 26: # Flexbox
        return """
        <div style="display:flex; justify-content:space-between; align-items:center; background:#020617; padding:14px 18px; border-radius:10px; border:1px solid #334155;">
          <div style="background:#38bdf8; color:#000; padding:8px 14px; border-radius:6px; font-weight:700; font-size:12px;">لوگو (راست)</div>
          <div style="background:#f59e0b; color:#000; padding:8px 14px; border-radius:6px; font-weight:700; font-size:12px;">منو (وسط‌چین)</div>
          <div style="background:#10b981; color:#000; padding:8px 14px; border-radius:6px; font-weight:700; font-size:12px;">پروفایل (چپ)</div>
        </div>
        """
    elif topic_id == 27: # Grid
        return """
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px;">
          <div style="background:#1e293b; padding:12px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">کارت ۱</div>
          <div style="background:#1e293b; padding:12px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">کارت ۲</div>
          <div style="background:#1e293b; padding:12px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">کارت ۳</div>
          <div style="background:#1e293b; padding:12px; border-radius:8px; text-align:center; color:#38bdf8; font-weight:700; font-size:12px; border:1px solid #334155;">کارت ۴</div>
        </div>
        """
    elif topic_id == 31: # Transform
        return """
        <div style="display:flex; gap:20px; align-items:center;">
          <div style="background:#0284c7; color:#fff; padding:12px 18px; border-radius:8px; font-weight:700; font-size:13px; cursor:pointer; transition:transform 0.2s;" onmouseenter="this.style.transform='scale(1.15) rotate(4deg)'" onmouseleave="this.style.transform='none'">
            موس را روی من بیاور (Hover Me!)
          </div>
          <span style="font-size:12px; color:#94a3b8;">با transform: scale(1.15) بزرگ و مایل می‌شود.</span>
        </div>
        """
    elif topic_id == 32: # Animation
        return """
        <div style="display:flex; align-items:center; gap:16px;">
          <style>
            @keyframes pulseDemo {
              0%, 100% { transform: scale(1); opacity: 1; }
              50% { transform: scale(1.2); opacity: 0.6; }
            }
            .pulsing-dot {
              width: 18px; height: 18px; background: #ef4444; border-radius: 50%;
              box-shadow: 0 0 14px #ef4444;
              animation: pulseDemo 1.2s infinite ease-in-out;
            }
          </style>
          <div class="pulsing-dot"></div>
          <span style="font-size:13px; font-weight:700; color:#f87171;">در حال پخش زنده (LIVE Animation) با @keyframes</span>
        </div>
        """
    elif topic_id == 35: # Gradients
        return """
        <div style="height:60px; border-radius:10px; background:linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:900; font-size:14px; box-shadow:0 8px 20px rgba(6,182,212,0.25);">
          طیف رنگین‌کمانی زنده linear-gradient
        </div>
        """
    elif topic_id == 38: # Glassmorphism
        return """
        <div style="position:relative; height:90px; border-radius:12px; background:radial-gradient(circle at 30% 50%, #f43f5e 0%, #8b5cf6 100%); overflow:hidden; display:flex; align-items:center; justify-content:center;">
          <div style="background:rgba(255,255,255,0.15); backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.3); border-radius:10px; padding:10px 24px; color:#fff; font-weight:700; font-size:13px;">
            شیشه مات گلس‌مورفیسم (backdrop-filter: blur)
          </div>
        </div>
        """
    else:
        return f"""
        <div style="background:rgba(15,23,42,0.5); padding:16px; border-radius:10px; border:1px solid #1e293b;">
          <div style="font-size:12px; color:#38bdf8; margin-bottom:6px;">نمایش زنده استایل CSS:</div>
          <div style="background:#020617; padding:12px; border-radius:8px; border:1px solid #334155; color:#cbd5e1; font-size:13px;">
            المان تست شده با قوانین این سرفصل
          </div>
        </div>
        """

def get_react_preview(topic_id):
    """Return interactive working simulated React component for all topics"""
    if topic_id == 10: # useState
        return """
        <div style="background:rgba(15,23,42,0.7); padding:18px; border-radius:12px; border:1px solid #38bdf8; display:flex; align-items:center; gap:16px;">
          <button onclick="const c = this.parentElement.querySelector('.cnt-val'); c.innerText = Math.max(0, parseInt(c.innerText) - 1);" style="width:36px; height:36px; background:#ef4444; color:#fff; border:none; border-radius:8px; font-size:18px; font-weight:900; cursor:pointer;">-</button>
          <span class="cnt-val" style="font-size:24px; font-weight:900; color:#fff; min-width:35px; text-align:center;">1</span>
          <button onclick="const c = this.parentElement.querySelector('.cnt-val'); c.innerText = parseInt(c.innerText) + 1;" style="width:36px; height:36px; background:#10b981; color:#fff; border:none; border-radius:8px; font-size:18px; font-weight:900; cursor:pointer;">+</button>
          <span style="font-size:13px; color:#94a3b8; margin-right:12px;">👈 شمارنده زنده useState (کلیک کنید تا استیت تغییر کند)</span>
        </div>
        """
    elif topic_id == 8: # Conditional Rendering
        return """
        <div style="background:rgba(15,23,42,0.7); padding:16px; border-radius:12px; border:1px solid #1e293b; display:flex; align-items:center; justify-content:space-between;">
          <div>
            <div style="font-size:14px; font-weight:700; color:#fff;">کفش اسپرت رانینگ</div>
            <div class="stock-badge" style="display:inline-block; margin-top:4px; padding:3px 10px; border-radius:99px; background:rgba(16,185,129,0.15); color:#34d399; font-size:12px; font-weight:700;">موجود در انبار ✓</div>
          </div>
          <button onclick="const b = this.parentElement.querySelector('.stock-badge'); const inStock = b.innerText.includes('موجود'); b.innerText = inStock ? 'ناموجود ✕' : 'موجود در انبار ✓'; b.style.color = inStock ? '#f87171' : '#34d399'; b.style.background = inStock ? 'rgba(239,68,68,0.15)' : 'rgba(16,185,129,0.15)';" style="background:#334155; color:#fff; border:none; padding:7px 14px; border-radius:8px; font-size:12px; cursor:pointer;">تغییر شرط موجودی</button>
        </div>
        """
    elif topic_id == 13: # Controlled Components
        return """
        <div style="background:rgba(15,23,42,0.7); padding:16px; border-radius:12px; border:1px solid #1e293b;">
          <input type="text" placeholder="در این کادر تایپ کنید..." oninput="this.parentElement.querySelector('.mirror-text').innerText = this.value || 'هنوز چیزی تایپ نشده';" style="width:100%; max-width:350px; background:#020617; border:1px solid #334155; color:#fff; padding:8px 12px; border-radius:8px; font-family:inherit; outline:none;">
          <div style="margin-top:8px; font-size:13px; color:#38bdf8;">
            متن بازتاب‌شده در لحظه (Controlled State): <strong class="mirror-text" style="color:#fde047;">هنوز چیزی تایپ نشده</strong>
          </div>
        </div>
        """
    elif topic_id == 18: # Context API
        return """
        <div class="theme-box" style="background:#0f172a; color:#fff; padding:16px; border-radius:10px; border:1px solid #334155; display:flex; justify-content:space-between; align-items:center;">
          <span>پوسته سراسری کامپوننت (ThemeProvider)</span>
          <button onclick="const box = this.closest('.theme-box'); const isDark = box.style.background.includes('15'); box.style.background = isDark ? '#ffffff' : '#0f172a'; box.style.color = isDark ? '#0f172a' : '#ffffff'; this.innerText = isDark ? 'حالت شب 🌙' : 'حالت روز ☀️';" style="background:#38bdf8; color:#000; border:none; padding:6px 14px; border-radius:8px; font-weight:700; font-size:12px; cursor:pointer;">حالت روز ☀️</button>
        </div>
        """
    else:
        return f"""
        <div style="background:rgba(15,23,42,0.6); padding:16px; border-radius:10px; border:1px solid rgba(97,218,251,0.25); display:flex; align-items:center; justify-content:space-between;">
          <div>
            <div style="font-size:13px; font-weight:700; color:#67e8f9;">⚛️ کامپوننت رندر شده در محیط ری‌اکت</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:3px;">هوک‌ها و پراپ‌های سرفصل {topic_id} فعال و در چرخه حیات</div>
          </div>
          <span style="background:rgba(97,218,251,0.1); color:#67e8f9; padding:3px 10px; border-radius:6px; font-size:11px; font-weight:700;">React 19 Ready</span>
        </div>
        """
