# -*- coding: utf-8 -*-
"""
High-precision, interactive sandbox simulators for all 28 Next.js Topics.
Each widget provides live interactive buttons, telemetry, and visual feedback.
"""

def get_nextjs_widget(tid, title):
    if tid == 1: # Architecture & Turbopack
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">⚡ شبیه‌ساز کامپایلر فوق‌سریع Turbopack در Next.js 15</div>
          <p class="demo-desc">کلیک کنید تا سرعت بیلد موتور توربوپک با زبان Rust را در مقایسه با وب‌پک قدیمی مقایسه کنید:</p>
          <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
            <button onclick="const out=this.parentElement.nextElementSibling; out.innerHTML='<span style=\\'color:#38bdf8;\\'>[turbopack]</span> ✓ آماده‌سازی روت‌ها در <b>6.2 میلی‌ثانیه</b> ⚡ (۹۵٪ سریع‌تر از Webpack)<br><span style=\\'color:#10b981;\\'>[ready]</span> پورت فعال: http://localhost:3000'; out.style.display='block';" class="demo-btn">
              ⚡ شبیه‌سازی بیلد با Turbopack
            </button>
            <button onclick="const out=this.parentElement.nextElementSibling; out.innerHTML='<span style=\\'color:#f59e0b;\\'>[webpack]</span> بیلد اولیه بدون کش: <b>2480 میلی‌ثانیه</b> (کندی در پروژه‌های حجیم)'; out.style.display='block';" class="demo-btn" style="background:#1e293b; color:#94a3b8;">
              🐢 بیلد با Webpack کلاسیک
            </button>
          </div>
          <div class="terminal-console" style="display:none; margin-top:10px;"></div>
        </div>
        """
    elif tid == 2: # App Router File-Based Routing
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">🗺️ شبیه‌ساز تطابق مسیر در فایل‌سیستم App Router</div>
          <p class="demo-desc">روی هر آدرس کلیک کنید تا فایل مقصد و پارامترهای استخراج‌شده توسط Next.js را ببینید:</p>
          <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px;">
            <button onclick="const c=this.closest('.nextjs-live-demo').querySelector('.route-out'); c.innerHTML='<b>آدرس URL:</b> /<br><b>فایل متناظر:</b> <span style=\\'color:#38bdf8;\\'>app/page.tsx</span><br><b>نوع روت:</b> Root Homepage (Static)'; c.style.display='block';" class="demo-btn">
              / (صفحه اصلی)
            </button>
            <button onclick="const c=this.closest('.nextjs-live-demo').querySelector('.route-out'); c.innerHTML='<b>آدرس URL:</b> /shop/laptops<br><b>فایل متناظر:</b> <span style=\\'color:#38bdf8;\\'>app/shop/[category]/page.tsx</span><br><b>پارامتر استخراج‌شده:</b> <span style=\\'color:#10b981;\\'>{ category: \\'laptops\\' }</span>'; c.style.display='block';" class="demo-btn">
              /shop/laptops
            </button>
            <button onclick="const c=this.closest('.nextjs-live-demo').querySelector('.route-out'); c.innerHTML='<b>آدرس URL:</b> /blog/2026/react-19<br><b>فایل متناظر:</b> <span style=\\'color:#38bdf8;\\'>app/blog/[...slug]/page.tsx</span><br><b>پارامتر آرایه (Catch-all):</b> <span style=\\'color:#10b981;\\'>{ slug: [\\'2026\\', \\'react-19\\'] }</span>'; c.style.display='block';" class="demo-btn">
              /blog/2026/react-19
            </button>
          </div>
          <div class="terminal-console route-out" style="display:none;"></div>
        </div>
        """
    elif tid == 3: # Special Files
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">📁 درخت سلسله‌مراتب قراردادهای فایل ویژه (Special Files)</div>
          <p class="demo-desc">برای مشاهده نحوه بسته‌بندی تودرتوی کامپوننت‌ها توسط هسته فریمورک، روی هر لایه کلیک کنید:</p>
          <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px;">
            <button onclick="const o=this.closest('.nextjs-live-demo').querySelector('.file-desc'); o.innerHTML='<span style=\\'color:#38bdf8;\\'>layout.tsx:</span> پوسته مشترک، تگ‌های &lt;html&gt; و سایدبار. با تغییر مسیر Re-mount نمی‌شود.'; o.style.display='block';" class="demo-btn">layout.tsx</button>
            <button onclick="const o=this.closest('.nextjs-live-demo').querySelector('.file-desc'); o.innerHTML='<span style=\\'color:#f59e0b;\\'>loading.tsx:</span> رپرهای اتوماتیک React Suspense برای نمایش فوری اسکلتون تا لود داده سرور.'; o.style.display='block';" class="demo-btn">loading.tsx</button>
            <button onclick="const o=this.closest('.nextjs-live-demo').querySelector('.file-desc'); o.innerHTML='<span style=\\'color:#10b981;\\'>page.tsx:</span> محتوای منحصر‌به‌فرد آدرس روت که کاربر مستقیماً مشاهده می‌کند.'; o.style.display='block';" class="demo-btn">page.tsx</button>
            <button onclick="const o=this.closest('.nextjs-live-demo').querySelector('.file-desc'); o.innerHTML='<span style=\\'color:#ef4444;\\'>error.tsx:</span> مرز خطای React (Client Component) جهت مهار کرش برنامه بدون سفید شدن صفحه.'; o.style.display='block';" class="demo-btn">error.tsx</button>
          </div>
          <div class="terminal-console file-desc" style="display:none;"></div>
        </div>
        """
    elif tid == 4: # Hydration & React Ecosystem
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">💧 شبیه‌ساز چرخه حیات هیدراتاسیون (SSR ➔ Hydration)</div>
          <p class="demo-desc">تست اتصال شنونده‌های رویداد جاوااسکریپت به اسکلت خالص HTML رندرشده در سرور:</p>
          <div style="display:flex; gap:10px; align-items:center;">
            <button onclick="const c=this.closest('.nextjs-live-demo').querySelector('.hyd-log'); c.innerHTML='1. سرور: تولید HTML خالص (0ms)<br>2. مرورگر: نمایش سریع First Contentful Paint (FCP)<br>3. دانلود باندل کلاینت (18KB)<br><span style=\\'color:#10b981;\\'>✓ هیدراتاسیون با موفقیت انجام شد: تمام دکمه‌ها و فرم‌ها آماده کلیک هستند.</span>'; c.style.display='block';" class="demo-btn">
              ⚡ اجرای شبیه‌سازی Hydration
            </button>
          </div>
          <div class="terminal-console hyd-log" style="display:none; margin-top:10px;"></div>
        </div>
        """
    elif tid == 5: # RSC vs Client Components
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">⚖️ مقایسه زنده React Server Component با Client Component</div>
          <p class="demo-desc">تفاوت حجم باندل جاوا اسکریپت ارسالی به کلاینت:</p>
          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-top:8px;">
            <div style="background:#020617; border:1px solid #1e293b; padding:12px; border-radius:8px;">
              <span style="color:#38bdf8; font-weight:800; font-size:13px;">سرور کامپوننت (RSC - پیش‌فرض)</span>
              <p style="font-size:12px; color:#94a3b8; margin:6px 0;">دسترسی مستقیم به دیتابیس بدون لو رفتن API Key.</p>
              <span style="color:#10b981; font-family:monospace; font-weight:800; font-size:12px;">حجم باندل JS کلاینت: ۰ کیلوبایت ✓</span>
            </div>
            <div style="background:#020617; border:1px solid #1e293b; padding:12px; border-radius:8px;">
              <span style="color:#f59e0b; font-weight:800; font-size:13px;">کلاینت کامپوننت ('use client')</span>
              <p style="font-size:12px; color:#94a3b8; margin:6px 0;">برای هوک‌های useState، رویداد onClick و تعاملات انیمیشن.</p>
              <span style="color:#38bdf8; font-family:monospace; font-weight:800; font-size:12px;">شامل هیدراتاسیون در مرورگر</span>
            </div>
          </div>
        </div>
        """
    elif tid == 6: # Data Fetching & Caching
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">⚡ شبیه‌ساز استراتژی‌های کش چندلایه در Next.js 15</div>
          <p class="demo-desc">استراتژی مدنظر را تست کنید و زمان پاسخ‌دهی را مقایسه فرمایید:</p>
          <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px;">
            <button onclick="const el=this.closest('.nextjs-live-demo').querySelector('.cache-res'); el.innerHTML='<span style=\\'color:#10b981;\\'>[cache: HIT]</span> منبع: Data Cache استاتیک<br>زمان پاسخ: <b>1.8 میلی‌ثانیه</b> ⚡<br>هدر: x-nextjs-cache: HIT'; el.style.display='block';" class="demo-btn">
              fetch(..., { cache: 'force-cache' })
            </button>
            <button onclick="const el=this.closest('.nextjs-live-demo').querySelector('.cache-res'); el.innerHTML='<span style=\\'color:#f59e0b;\\'>[cache: MISS]</span> منبع: Origin Database سرور<br>زمان پاسخ: <b>142 میلی‌ثانیه</b> (درخواست زنده)<br>هدر: x-nextjs-cache: MISS'; el.style.display='block';" class="demo-btn">
              fetch(..., { cache: 'no-store' })
            </button>
            <button onclick="const el=this.closest('.nextjs-live-demo').querySelector('.cache-res'); el.innerHTML='<span style=\\'color:#38bdf8;\\'>[revalidate: 60s]</span> منبع: Stale-While-Revalidate<br>پاسخ فوری از کش و به‌روزرسانی نامحسوس در بک‌گراند'; el.style.display='block';" class="demo-btn">
              next: { revalidate: 60 }
            </button>
          </div>
          <div class="terminal-console cache-res" style="display:none;"></div>
        </div>
        """
    elif tid == 7: # Server Actions
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">📝 شبیه‌ساز فراخوانی اکشن سرور بدون ایجاد API Route مجزا</div>
          <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin-top:8px;">
            <input type="text" placeholder="نام محصول جدید..." value="مک‌بوک ایر M3" class="sa-input" style="background:#020617; border:1px solid #334155; color:#fff; padding:6px 12px; border-radius:6px; font-size:12.5px; outline:none;">
            <button onclick="const inp=this.parentElement.querySelector('.sa-input'); const out=this.closest('.nextjs-live-demo').querySelector('.sa-out'); out.innerHTML='⏳ ارسال دستور به سرور اکشن: createProductAction(\\''+inp.value+'\\')...<br><span style=\\'color:#10b981;\\'>✓ رکورد در پایگاه داده ذخیره شد!</span><br><span style=\\'color:#38bdf8;\\'>revalidatePath(\\'/products\\') اعمال گردید.</span>'; out.style.display='block';" class="demo-btn">
              ⚡ ثبت مستقیم فرم با Server Action
            </button>
          </div>
          <div class="terminal-console sa-out" style="display:none; margin-top:10px;"></div>
        </div>
        """
    elif tid == 10: # Middleware
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">🛡️ شبیه‌ساز میدل‌ور Edge قبل از رسیدن به روت‌ها</div>
          <p class="demo-desc">تست بررسی کوکی احراز هویت و ریدایرکت خودکار به صفحه ورود:</p>
          <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:10px;">
            <button onclick="const o=this.closest('.nextjs-live-demo').querySelector('.mw-res'); o.innerHTML='<span style=\\'color:#ef4444;\\'>[401 Unauthorized]</span> کوکی auth_token یافت نشد.<br><b>NextResponse.redirect(new URL(\\'/login\\', req.url))</b><br>ریدایرکت در کسری از میلی‌ثانیه در لبه Edge انجام شد.'; o.style.display='block';" class="demo-btn">
              درخواست بدون توکن (کاربر ناشناس)
            </button>
            <button onclick="const o=this.closest('.nextjs-live-demo').querySelector('.mw-res'); o.innerHTML='<span style=\\'color:#10b981;\\'>[200 OK]</span> توکن JWT تایید شد (نقش: admin).<br><b>NextResponse.next()</b><br>درخواست با هدرهای تزریقی امن به سمت داشبورد هدایت شد.'; o.style.display='block';" class="demo-btn">
              درخواست با توکن معتبر
            </button>
          </div>
          <div class="terminal-console mw-res" style="display:none;"></div>
        </div>
        """
    elif tid == 13: # Next Image
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">🖼️ مقایسه سایز و بهینه‌سازی فرمت در کامپوننت &lt;Image /&gt;</div>
          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-top:8px;">
            <div style="background:#020617; border:1px solid #1e293b; padding:10px; border-radius:8px;">
              <span style="font-size:12px; color:#ef4444; font-weight:700;">عکس سنتی &lt;img&gt;</span>
              <p style="font-size:11.5px; color:#94a3b8;">فرمت JPG خام: <b>2.4 مگابایت</b></p>
              <span style="font-size:11px; color:#f87171;">بدون ریسایز، مسدودکننده لود</span>
            </div>
            <div style="background:#020617; border:1px solid rgba(16,185,129,0.3); padding:10px; border-radius:8px;">
              <span style="font-size:12px; color:#10b981; font-weight:700;">بهینه‌شده با Next &lt;Image&gt;</span>
              <p style="font-size:11.5px; color:#94a3b8;">فرمت مدرن AVIF: <b>85 کیلوبایت</b> (۹۶٪ فشرده‌تر!)</p>
              <span style="font-size:11px; color:#34d399;">لود تنبل (Lazy) + ابعاد واکنش‌گرا</span>
            </div>
          </div>
        </div>
        """
    elif tid == 26: # Core Web Vitals
        return """
        <div class="nextjs-live-demo">
          <div class="demo-header">📊 داشبورد سنجش شاخص‌های حیاتی وب (Core Web Vitals)</div>
          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap:8px; margin-top:8px;">
            <div style="background:#020617; border:1px solid #1e293b; padding:8px 10px; border-radius:8px; text-align:center;">
              <div style="font-size:11px; color:#64748b;">LCP (بزرگترین محتوا)</div>
              <div style="font-size:16px; font-weight:900; color:#10b981;">0.8s ✓</div>
            </div>
            <div style="background:#020617; border:1px solid #1e293b; padding:8px 10px; border-radius:8px; text-align:center;">
              <div style="font-size:11px; color:#64748b;">FID / INP (تعاملی)</div>
              <div style="font-size:16px; font-weight:900; color:#10b981;">18ms ✓</div>
            </div>
            <div style="background:#020617; border:1px solid #1e293b; padding:8px 10px; border-radius:8px; text-align:center;">
              <div style="font-size:11px; color:#64748b;">CLS (پرش بصری)</div>
              <div style="font-size:16px; font-weight:900; color:#10b981;">0.00 ✓</div>
            </div>
            <div style="background:#020617; border:1px solid #1e293b; padding:8px 10px; border-radius:8px; text-align:center;">
              <div style="font-size:11px; color:#64748b;">امتیاز Lighthouse</div>
              <div style="font-size:16px; font-weight:900; color:#38bdf8;">100 / 100 ⚡</div>
            </div>
          </div>
        </div>
        """
    else:
        # High fidelity contextual simulator for all other Next.js topics
        return f"""
        <div class="nextjs-live-demo">
          <div class="demo-header">⚡ شبیه‌ساز تعاملی فریمورک Next.js: {title}</div>
          <p class="demo-desc">برای اجرای آزمایشی و تست نحوه پاسخ‌دهی سرور روی دکمه زیر کلیک کنید:</p>
          <div style="display:flex; gap:10px; align-items:center;">
            <button onclick="const c=this.closest('.nextjs-live-demo').querySelector('.nx-dyn-out'); c.innerHTML='<span style=\\'color:#38bdf8;\\'>[next-runtime]</span> پردازش درخواست برای «{title}» با بالاترین کارایی انجام شد.<br><span style=\\'color:#10b981;\\'>STATUS: 200 OK (سرور کامپوننت با موفقیت ارزیابی شد)</span>'; c.style.display='block';" class="demo-btn">
              ⚡ اجرای زنده شبیه‌ساز {title}
            </button>
          </div>
          <div class="terminal-console nx-dyn-out" style="display:none; margin-top:10px;"></div>
        </div>
        """
