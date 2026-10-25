# -*- coding: utf-8 -*-
"""
Part 2 of custom interactive widgets for React topics 36 to 65.
Covers Strict Mode, Auth, Fiber, RSC, React 19, Next.js, Framer Motion, and Micro Frontends.
"""

def get_widget_part2(tid, title):
    if tid == 36: # StrictMode
        return """
        <div class="react-live-demo">
          <div class="demo-header">🔍 رفتار دوگانه هوک‌ها در React.StrictMode</div>
          <button onclick="const l=this.nextElementSibling; l.style.display='block'; l.innerHTML='1. Mount کامپوننت<br>2. Unmount فوری برای تست Cleanup<br>3. Remount نهایی (تضمین صفر مموری لیک)';" class="demo-btn">
            شبیه‌سازی رندر در StrictMode
          </button>
          <div style="display:none; margin-top:8px; font-family:monospace; font-size:11.5px; color:#f59e0b; background:#020617; padding:8px; border-radius:6px; line-height:1.7;"></div>
        </div>
        """
    elif tid == 37: # Environment Variables
        return """
        <div class="react-live-demo">
          <div class="demo-header">🔐 متغیرهای محیطی با پیشوند VITE_</div>
          <div style="font-family:monospace; font-size:12px; color:#38bdf8; background:#020617; padding:8px 12px; border-radius:6px;">
            import.meta.env.VITE_API_URL = "https://api.mydomain.ir/v1"
          </div>
        </div>
        """
    elif tid == 38: # Authentication & JWT
        return """
        <div class="react-live-demo">
          <div class="demo-header">🔑 احراز هویت توکن JWT و Axios Interceptors</div>
          <button onclick="const s=this.nextElementSibling; s.innerText='توکن با موفقیت به هدر Authorization: Bearer eyJhbG... تزریق شد.'; s.style.display='block';" class="demo-btn">
            شبیه‌سازی ارسال ریکوئست با توکن
          </button>
          <div style="display:none; margin-top:8px; font-size:12px; color:#10b981; background:#020617; padding:8px; border-radius:6px;"></div>
        </div>
        """
    elif tid == 39: # useId & forwardRef
        return """
        <div class="react-live-demo">
          <div class="demo-header">🆔 تولید شناسه یکتا سمت سرور با هوک useId</div>
          <div style="font-family:monospace; font-size:12px; color:#10b981; background:#020617; padding:8px; border-radius:6px;">
            const id = useId(); // ":r1:" (تضمین تطابق ۱۰۰٪ در هیدریشن SSR)
          </div>
        </div>
        """
    elif tid == 40: # HOC & Render Props
        return """
        <div class="react-live-demo">
          <div class="demo-header">🛡️ کامپوننت مرتبه بالا (withAuth HOC)</div>
          <button onclick="const s=this.nextElementSibling; const ok=s.innerText.includes('لاگین'); s.innerText=ok?'کاربر مهمان ➔ هدایت خودکار به /login':'کاربر لاگین ➔ دسترسی به داشبورد'; s.style.color=ok?'#ef4444':'#10b981';" class="demo-btn">
            سوئیچ وضعیت لاگین در HOC
          </button>
          <div style="margin-top:8px; font-size:12.5px; font-weight:700; color:#10b981;">کاربر لاگین ➔ دسترسی به داشبورد</div>
        </div>
        """
    elif tid == 41: # Compound Components
        return """
        <div class="react-live-demo">
          <div class="demo-header">🧩 الگوی کامپوننت‌های ترکیبی هماهنگ (&lt;Tabs&gt;)</div>
          <div style="display:flex; gap:6px; margin-bottom:8px;">
            <button onclick="this.parentElement.nextElementSibling.innerText='محتوای تب اول: مشخصات عمومی کالا';" class="demo-btn" style="font-size:11px; padding:4px 8px;">&lt;Tab&gt;مشخصات&lt;/Tab&gt;</button>
            <button onclick="this.parentElement.nextElementSibling.innerText='محتوای تب دوم: نظرات خریداران';" class="demo-btn" style="font-size:11px; padding:4px 8px;">&lt;Tab&gt;نظرات&lt;/Tab&gt;</button>
          </div>
          <div style="padding:10px; background:#020617; border-radius:6px; font-size:12px; color:#cbd5e1;">محتوای تب اول: مشخصات عمومی کالا</div>
        </div>
        """
    elif tid == 42: # Fiber Architecture
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚡ معماری اولویت‌بندی هسته React Fiber</div>
          <input type="text" placeholder="تایپ فوری کیبورد (اولویت اول)..." oninput="this.nextElementSibling.innerText='تایپ شد: ' + this.value;" style="background:#020617; border:1px solid #334155; color:#fff; padding:6px 10px; border-radius:6px; font-size:12px; outline:none; max-width:240px;">
          <span style="font-size:12px; color:#38bdf8; margin-right:8px;">تایپ شد: ...</span>
        </div>
        """
    elif tid == 43: # Code Splitting
        return """
        <div class="react-live-demo">
          <div class="demo-header">📦 تقسیم باندل و لود تنبل با React.lazy</div>
          <button onclick="const el=this.nextElementSibling; el.innerText='⏳ در حال دانلود ماژول نمودار...'; el.style.display='block'; setTimeout(()=>el.innerHTML='<span style=\\'color:#10b981;\\'>✅ ماژول 140KB با موفقیت لود و مونت شد.</span>', 600);" class="demo-btn">
            لود داینامیک ماژول نمودار
          </button>
          <div style="display:none; margin-top:8px; font-size:12px; background:#020617; padding:8px; border-radius:6px;"></div>
        </div>
        """
    elif tid == 44: # Virtualization
        return """
        <div class="react-live-demo">
          <div class="demo-header">📜 مجازی‌سازی لیست ۵۰ هزارتایی با react-window</div>
          <div style="height:80px; overflow-y:auto; border:1px solid #334155; border-radius:6px; padding:4px; background:#020617; font-size:11.5px;">
            <div style="padding:4px; border-bottom:1px solid #1e293b; color:#38bdf8;">ردیف ۱: کاربر شماره ۱ (رندر فعال)</div>
            <div style="padding:4px; border-bottom:1px solid #1e293b; color:#38bdf8;">ردیف ۲: کاربر شماره ۲ (رندر فعال)</div>
            <div style="padding:4px; color:#94a3b8;">ردیف ۳: کاربر شماره ۳ (در صف اسکرول)</div>
          </div>
        </div>
        """
    elif tid == 45: # Concurrent Features (useTransition)
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚡ هوک useTransition (جلوگیری از فریز تایپ)</div>
          <button onclick="const s=this.nextElementSibling; s.innerText='⏳ startTransition در حال فیلتر ۱۰۰۰ آیتم در پس‌زمینه...'; setTimeout(()=>s.innerText='✅ فیلترینگ با اولویت پایین بدون افت فریم پایان یافت.', 500);" class="demo-btn">
            اجرای startTransition
          </button>
          <div style="margin-top:6px; font-size:12px; color:#34d399;">وضعیت: آماده فیلترینگ بدون لگ</div>
        </div>
        """
    elif tid == 46: # Suspense for Data Fetching
        return """
        <div class="react-live-demo">
          <div class="demo-header">⌛ هوک سوسپنس برای دریافت داده</div>
          <button onclick="const b=this.nextElementSibling; b.innerHTML='<span style=\\'color:#f59e0b;\\'>&lt;ProfileSkeleton /&gt; در حال نمایش...</span>'; setTimeout(()=>b.innerHTML='<span style=\\'color:#10b981;\\'>✅ دیتای کاربر آماده و جایگزین شد.</span>', 700);" class="demo-btn">
            پرتاب Promise به سمت Suspense
          </button>
          <div style="margin-top:8px; font-size:12px; padding:6px; background:#020617; border-radius:6px;">آماده فراخوانی داده</div>
        </div>
        """
    elif tid == 47: # React 19 (useOptimistic)
        return """
        <div class="react-live-demo">
          <div class="demo-header">🚀 هوک انقلابی React 19 (useOptimistic)</div>
          <button onclick="const c=this.querySelector('.opt-cnt'); c.innerText=parseInt(c.innerText)+1; this.nextElementSibling.innerText='ارسال هم‌زمان به سرور...';" class="demo-btn">
            ❤️ لایک سریع (<span class="opt-cnt">42</span>)
          </button>
          <span style="font-size:12px; color:#38bdf8; margin-right:8px;">عدد در لحظه افزایش یافت بدون معطلی سرور!</span>
        </div>
        """
    elif tid == 48: # Server vs Client Components
        return """
        <div class="react-live-demo">
          <div class="demo-header">🏢 معماری دوگانه Server و Client Components</div>
          <div style="display:flex; gap:10px; font-size:12px;">
            <span style="padding:6px 12px; background:rgba(245,158,11,0.15); color:#f59e0b; border:1px solid #f59e0b; border-radius:6px;">Server: 0KB JS Bundle</span>
            <span style="padding:6px 12px; background:rgba(56,189,248,0.15); color:#38bdf8; border:1px solid #38bdf8; border-radius:6px;">'use client': Interactive</span>
          </div>
        </div>
        """
    elif tid == 49: # Rendering Strategies (CSR, SSR, SSG, ISR)
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚙️ استراتژی‌های رندرینگ وب (SSR, SSG, ISR, CSR)</div>
          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            <span style="background:#1e293b; color:#fff; padding:4px 8px; border-radius:4px; font-size:11px;">SSR: لحظه‌ای در سرور</span>
            <span style="background:#1e293b; color:#10b981; padding:4px 8px; border-radius:4px; font-size:11px;">SSG: زمان بیلد پروژه</span>
            <span style="background:#1e293b; color:#38bdf8; padding:4px 8px; border-radius:4px; font-size:11px;">ISR: بازتولید دوره‌ای</span>
          </div>
        </div>
        """
    elif tid == 50: # Next.js App Router
        return """
        <div class="react-live-demo">
          <div class="demo-header">📁 فایل‌سیستم هوشمند Next.js App Router</div>
          <div style="background:#020617; padding:8px 12px; border-radius:6px; font-family:monospace; font-size:11.5px; color:#38bdf8; direction:ltr; text-align:left;">
            app/dashboard/layout.tsx ➔ app/dashboard/page.tsx
          </div>
        </div>
        """
    elif tid == 51: # Remix / TanStack Start
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚡ فریمورک مبتنی بر استاندارد وب Remix & Loaders</div>
          <p style="font-size:12px; color:#cbd5e1;">دریافت دیتا با تابع loader() قبل از حتی ماونت شدن کامپوننت روی سرور.</p>
        </div>
        """
    elif tid == 52: # TypeScript in React
        return """
        <div class="react-live-demo">
          <div class="demo-header">🛡️ تایپ‌گذاری سخت‌گیرانه پراپ‌ها در TypeScript</div>
          <div style="background:#020617; padding:6px 12px; border-radius:6px; font-family:monospace; font-size:11.5px; color:#38bdf8; direction:ltr; text-align:left;">
            type Props = {{ title: string; count?: number; }}
          </div>
        </div>
        """
    elif tid == 53: # Testing (RTL & Vitest)
        return """
        <div class="react-live-demo">
          <div class="demo-header">🧪 تست خودکار رفتار کاربر با React Testing Library</div>
          <button onclick="this.nextElementSibling.innerText='PASS: test(\\'increments counter on click\\') passed in 12ms ✓'; this.nextElementSibling.style.display='block';" class="demo-btn">
            اجرای تست کامپوننت
          </button>
          <div style="display:none; margin-top:8px; font-size:12px; color:#10b981; font-family:monospace; background:#020617; padding:6px;"></div>
        </div>
        """
    elif tid == 54: # Storybook
        return """
        <div class="react-live-demo">
          <div class="demo-header">📚 کارگاه دیزاین سیستم Storybook</div>
          <p style="font-size:12px; color:#94a3b8;">تست ایزوله کامپوننت دکمه در ۳ حالت مختلف Primary، Outline و Disabled بدون نیاز به سرور.</p>
        </div>
        """
    elif tid == 55: # Accessibility in React
        return """
        <div class="react-live-demo">
          <div class="demo-header">♿ دسترس‌پذیری ARIA و Focus Trap در React</div>
          <button aria-expanded="false" onclick="const exp=this.getAttribute('aria-expanded')==='true'; this.setAttribute('aria-expanded', !exp); this.innerText = exp ? 'منوی بسته (aria-expanded=false)' : 'منوی باز (aria-expanded=true)';" class="demo-btn">
            منوی بسته (aria-expanded=false)
          </button>
        </div>
        """
    elif tid == 56: # i18n
        return """
        <div class="react-live-demo">
          <div class="demo-header">🌍 چندزبانه کردن با react-i18next و تغییر جهت RTL/LTR</div>
          <div style="display:flex; justify-content:space-between; align-items:center; background:#020617; padding:8px 12px; border-radius:6px;">
            <span class="lang-txt" style="color:#fff; font-size:13px;">سلام دنیا (خوش آمدید)</span>
            <button onclick="const t=this.parentElement.querySelector('.lang-txt'); const fa=t.innerText.includes('سلام'); t.innerText=fa?'Hello World (Welcome)':'سلام دنیا (خوش آمدید)'; this.innerText=fa?'English 🇺🇸':'فارسی 🇮🇷';" class="demo-btn" style="font-size:11.5px; padding:4px 8px;">English 🇺🇸</button>
          </div>
        </div>
        """
    elif tid == 57: # Framer Motion
        return """
        <div class="react-live-demo">
          <div class="demo-header">✨ انیمیشن نرم فنری با Framer Motion</div>
          <div style="display:flex; align-items:center; gap:14px; margin-top:6px;">
            <div style="width:50px; height:50px; background:linear-gradient(135deg, #06b6d4, #3b82f6); border-radius:12px; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:900; cursor:pointer; transition:all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);" onmouseenter="this.style.transform='scale(1.2) rotate(10deg)';" onmouseleave="this.style.transform='none';">
              Hover
            </div>
            <span style="font-size:12px; color:#94a3b8;">حرکت ژستی با فیزیک اسپرینگ (Spring Physics)</span>
          </div>
        </div>
        """
    elif tid == 58: # Micro Frontends
        return """
        <div class="react-live-demo">
          <div class="demo-header">🧩 میکروفرانت‌اند با Webpack Module Federation</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:11.5px;">
            <div style="background:#020617; padding:6px; border:1px solid #1e293b; border-radius:6px; color:#38bdf8;">RemoteApp: سبد خرید (تیم A)</div>
            <div style="background:#020617; padding:6px; border:1px solid #1e293b; border-radius:6px; color:#10b981;">HostApp: پورتال اصلی (تیم B)</div>
          </div>
        </div>
        """
    elif tid == 59: # Monorepo (Turborepo)
        return """
        <div class="react-live-demo">
          <div class="demo-header">📦 مدیریت مونو‌ریپو با Turborepo</div>
          <div style="font-family:monospace; font-size:12px; color:#10b981; background:#020617; padding:6px 10px; border-radius:6px;">
            >>> turbo build --filter=web (FULL TURBO: Cache Hit in 85ms ⚡)
          </div>
        </div>
        """
    elif tid == 60: # Feature-Sliced Design (FSD)
        return """
        <div class="react-live-demo">
          <div class="demo-header">📁 معماری پوشه‌بندی ویژگی‌محور (Feature-Sliced Design)</div>
          <div style="font-family:monospace; font-size:11.5px; color:#38bdf8; background:#020617; padding:8px; border-radius:6px; direction:ltr; text-align:left;">
            src/features/cart &bull; src/entities/user &bull; src/shared/ui
          </div>
        </div>
        """
    elif tid == 61: # React Design Patterns
        return """
        <div class="react-live-demo">
          <div class="demo-header">📐 الگوهای طراحی (Container vs Presentational)</div>
          <p style="font-size:12px; color:#94a3b8;">تفکیک کامل کامپوننت هوشمند دریافت داده از کامپوننت خالص رندرینگ ظاهری.</p>
        </div>
        """
    elif tid == 62: # Core Web Vitals in React
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚡ سنجه‌های سرعت گوگل (LCP &lt; 2.5s, CLS = 0, INP &lt; 200ms)</div>
          <div style="display:flex; gap:10px; font-size:12px;">
            <span style="color:#10b981; font-weight:700;">LCP: 0.8s ✓</span>
            <span style="color:#10b981; font-weight:700;">CLS: 0.00 ✓</span>
            <span style="color:#10b981; font-weight:700;">INP: 45ms ✓</span>
          </div>
        </div>
        """
    elif tid == 63: # PWA
        return """
        <div class="react-live-demo">
          <div class="demo-header">📱 نصب اپلیکیشن وب پیش‌رونده (PWA)</div>
          <button onclick="alert('اپلیکیشن ری‌اکت به عنوان نرم‌افزار دسکتاپ/موبایل نصب شد (Offline Cache Active)');" class="demo-btn">
            📲 نصب روی دستگاه (Install PWA)
          </button>
        </div>
        """
    elif tid == 64: # React Native
        return """
        <div class="react-live-demo">
          <div class="demo-header">📱 کامپایل به ویجت‌های بومی اندروید و iOS</div>
          <div style="background:#020617; padding:8px 12px; border-radius:6px; font-family:monospace; font-size:12px; color:#38bdf8;">
            &lt;View&gt;&lt;Text&gt;سلام از دل اپ نیتیو موبایل!&lt;/Text&gt;&lt;/View&gt;
          </div>
        </div>
        """
    elif tid == 65: # CI/CD & Docker
        return """
        <div class="react-live-demo">
          <div class="demo-header">🚀 دپلویمنت خودکار کانتینری Docker & Vercel</div>
          <div style="font-family:monospace; font-size:12px; color:#10b981; background:#020617; padding:8px; border-radius:6px;">
            ✔ Deployment Ready: https://my-react-app.vercel.app (Zero Downtime)
          </div>
        </div>
        """
    return None

print("Part 2 (Topics 36-65) ready.")
