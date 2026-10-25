# -*- coding: utf-8 -*-
"""
Part 1 of custom interactive widgets for React topics 1 to 35.
"""

def get_widget_part1(tid, title):
    if tid == 1: # Virtual DOM
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚡ مقایسه شبیه‌سازی شده Real DOM با Virtual DOM</div>
          <p class="demo-desc">در Virtual DOM فقط گره‌ای که تغییر کرده بازچینی می‌شود؛ کلیک کنید تا تفاوت رنگ و بازچینی تک‌المان را ببینید:</p>
          <div style="display:flex; align-items:center; gap:12px;">
            <button onclick="const el=this.parentElement.querySelector('.diff-count'); el.innerText=parseInt(el.innerText)+1; el.style.transform='scale(1.3)'; setTimeout(()=>el.style.transform='none', 200);" class="demo-btn">
              ⚡ شبیه‌سازی رندر بهینه (Diffing)
            </button>
            <span class="diff-count" style="font-size:24px; font-weight:900; color:#38bdf8; min-width:40px; text-align:center; transition:transform 0.2s;">1</span>
            <span style="font-size:12px; color:#10b981;">(فقط ۱ تگ در Virtual DOM تغییر یافت ✓)</span>
          </div>
        </div>
        """
    elif tid == 2: # Vite
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚡ شبیه‌سازی سرعت راه‌اندازی و Hot Module Replacement (HMR)</div>
          <p class="demo-desc">با فشردن دکمه، سرعت بیلد صدم ثانیه‌ای Vite را در مقایسه با وب‌پک قدیمی تست کنید:</p>
          <button onclick="const out=this.nextElementSibling; out.innerHTML='<span style=\\'color:#38bdf8;\\'>[vite] hmr update /src/App.jsx in <b>18ms</b> ⚡</span>'; out.style.display='block';" class="demo-btn">
            🔥 تست HMR تغییر زنده فایل
          </button>
          <div style="display:none; margin-top:10px; font-family:monospace; font-size:12px; background:#020617; padding:8px 12px; border-radius:6px; border:1px solid #1e293b;"></div>
        </div>
        """
    elif tid == 3: # JSX
        return """
        <div class="react-live-demo">
          <div class="demo-header">📄 تبدیل در لحظه عبارات داینامیک در JSX</div>
          <p class="demo-desc">در کادر زیر نام را تغییر دهید تا نحوه ادغام کد JS درون تگ HTML با {name} را ببینید:</p>
          <input type="text" placeholder="نام خود را بنویسید..." oninput="this.parentElement.querySelector('.jsx-preview').innerText = this.value || 'کاربر گرامی';" style="background:#020617; border:1px solid #334155; color:#fff; padding:6px 12px; border-radius:6px; font-size:13px; outline:none; max-width:280px;">
          <div style="margin-top:10px; padding:10px; background:#020617; border-radius:6px; border:1px solid #1e293b; color:#cbd5e1; font-size:13px;">
            خروجی JSX: &lt;h2&gt;سلام <span class="jsx-preview" style="color:#fde047; font-weight:700;">عرفان</span> خوش آمدید!&lt;/h2&gt;
          </div>
        </div>
        """
    elif tid == 4: # Function Components
        return """
        <div class="react-live-demo">
          <div class="demo-header">🧩 رندر کامپوننت دکمه چندبار مصرف (&lt;CustomButton /&gt;)</div>
          <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:8px;">
            <button onclick="alert('کامپوننت اولیه فشرده شد');" style="background:#38bdf8; color:#000; padding:8px 16px; border-radius:8px; font-weight:700; border:none; cursor:pointer;">&lt;Button variant="primary" /&gt;</button>
            <button onclick="alert('کامپوننت تایید فشرده شد');" style="background:#10b981; color:#000; padding:8px 16px; border-radius:8px; font-weight:700; border:none; cursor:pointer;">&lt;Button variant="success" /&gt;</button>
            <button onclick="alert('کامپوننت حذف فشرده شد');" style="background:#ef4444; color:#fff; padding:8px 16px; border-radius:8px; font-weight:700; border:none; cursor:pointer;">&lt;Button variant="danger" /&gt;</button>
          </div>
        </div>
        """
    elif tid == 5: # Props
        return """
        <div class="react-live-demo">
          <div class="demo-header">📦 پاس دادن ورودی‌های داینامیک (Props Passing)</div>
          <div style="display:flex; gap:8px; margin-bottom:10px;">
            <button onclick="const c=this.parentElement.nextElementSibling; c.querySelector('.p-title').innerText='مک‌بوک پرو M3'; c.querySelector('.p-price').innerText='۱۲۰,۰۰۰,۰۰۰ تومان';" class="demo-btn" style="font-size:11.5px; padding:4px 10px;">پراپ محصول ۱</button>
            <button onclick="const c=this.parentElement.nextElementSibling; c.querySelector('.p-title').innerText='آیفون ۱۶ پرو'; c.querySelector('.p-price').innerText='۸۵,۰۰۰,۰۰۰ تومان';" class="demo-btn" style="font-size:11.5px; padding:4px 10px;">پراپ محصول ۲</button>
          </div>
          <div style="background:#020617; border:1px solid #1e293b; padding:12px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
            <span class="p-title" style="font-weight:700; color:#fff;">مک‌بوک پرو M3</span>
            <span class="p-price" style="color:#10b981; font-weight:700;">۱۲۰,۰۰۰,۰۰۰ تومان</span>
          </div>
        </div>
        """
    elif tid == 6: # Children Prop
        return """
        <div class="react-live-demo">
          <div class="demo-header">🎁 کپسوله‌سازی و اسلات محتوا با پراپ children</div>
          <div style="background:#020617; border:2px dashed #38bdf8; border-radius:10px; padding:16px;">
            <div style="font-size:11px; color:#38bdf8; margin-bottom:4px;">کادر والد (&lt;CardWrapper&gt;):</div>
            <div style="background:rgba(56,189,248,0.1); padding:10px; border-radius:6px; color:#fff; font-size:13px;">
              ✨ این محتوا به عنوان <strong>{children}</strong> از بیرون به درون کادر تزریق شده است.
            </div>
          </div>
        </div>
        """
    elif tid == 7: # Rendering Lists & Keys
        return """
        <div class="react-live-demo">
          <div class="demo-header">📋 رندر داینامیک لیست همراه با کلید یکتا (key={item.id})</div>
          <div style="display:flex; gap:8px; margin-bottom:8px;">
            <button onclick="const ul=this.parentElement.nextElementSibling; const id=Date.now()%1000; const li=document.createElement('li'); li.style='padding:6px 10px; background:#020617; margin-bottom:4px; border-radius:6px; color:#38bdf8; display:flex; justify-content:space-between;'; li.innerHTML='<span>تسک شماره '+id+'</span><span style=\\'color:#94a3b8; font-size:11px;\\'>key='+id+'</span>'; ul.prepend(li);" class="demo-btn" style="font-size:11.5px;">+ افزودن آیتم به اول لیست</button>
          </div>
          <ul style="list-style:none; max-height:100px; overflow-y:auto; padding:0;">
            <li style="padding:6px 10px; background:#020617; margin-bottom:4px; border-radius:6px; color:#fff; display:flex; justify-content:space-between;">
              <span>تسک اول</span><span style="color:#94a3b8; font-size:11px;">key=101</span>
            </li>
          </ul>
        </div>
        """
    elif tid == 8: # Conditional Rendering
        return """
        <div class="react-live-demo">
          <div class="demo-header">🔀 رندر شرطی المان بر اساس وضعیت استیت</div>
          <div style="display:flex; align-items:center; justify-content:space-between; background:#020617; padding:12px; border-radius:8px;">
            <div>
              <span style="color:#fff; font-size:13px; font-weight:700;">هدفون بی‌سیم سونی</span>
              <div class="c-badge" style="margin-top:4px; font-size:12px; font-weight:700; color:#10b981;">وضعیت: موجود در انبار ✓</div>
            </div>
            <button onclick="const b=this.parentElement.querySelector('.c-badge'); const inStock=b.innerText.includes('موجود'); b.innerText=inStock?'وضعیت: ناموجود ✕':'وضعیت: موجود در انبار ✓'; b.style.color=inStock?'#ef4444':'#10b981';" class="demo-btn" style="font-size:12px;">تغییر استیت کالا</button>
          </div>
        </div>
        """
    elif tid == 9: # Events
        return """
        <div class="react-live-demo">
          <div class="demo-header">🖱️ شبیه‌سازی SyntheticEvent و شنونده رویداد onClick</div>
          <button onclick="const l=this.nextElementSibling; l.innerText = 'رویداد SyntheticEvent در ساعت ' + new Date().toLocaleTimeString('fa-IR') + ' با موفقیت شکار شد!'; l.style.display='block';" class="demo-btn">
            کلیک کن (Trigger SyntheticEvent)
          </button>
          <div style="display:none; margin-top:10px; font-size:12px; color:#10b981; background:#020617; padding:8px 12px; border-radius:6px;"></div>
        </div>
        """
    elif tid == 10: # useState
        return """
        <div class="react-live-demo">
          <div class="demo-header">🔢 هوک useState (شمارنده بلادرنگ)</div>
          <div style="display:flex; align-items:center; gap:14px; margin-top:8px;">
            <button onclick="const c=this.parentElement.querySelector('.state-val'); c.innerText=Math.max(0, parseInt(c.innerText)-1);" style="width:36px; height:36px; background:#ef4444; color:#fff; border:none; border-radius:8px; font-size:18px; font-weight:900; cursor:pointer;">-</button>
            <span class="state-val" style="font-size:24px; font-weight:900; color:#fff; min-width:35px; text-align:center;">1</span>
            <button onclick="const c=this.parentElement.querySelector('.state-val'); c.innerText=parseInt(c.innerText)+1;" style="width:36px; height:36px; background:#10b981; color:#fff; border:none; border-radius:8px; font-size:18px; font-weight:900; cursor:pointer;">+</button>
            <span style="font-size:12.5px; color:#94a3b8;">تغییر استیت باعث ری‌رندر کامپوننت می‌شود.</span>
          </div>
        </div>
        """
    elif tid == 11: # Styling / CSS Modules
        return """
        <div class="react-live-demo">
          <div class="demo-header">🎨 ایزوله‌سازی کلاس‌ها با CSS Modules و هشینگ</div>
          <div style="display:flex; gap:10px; margin-top:8px;">
            <div style="padding:10px 16px; background:#020617; border:1px solid #38bdf8; border-radius:8px; font-size:12px; font-family:monospace; color:#38bdf8;">
              class="Button_primary__7a2f"
            </div>
            <span style="font-size:12px; color:#94a3b8; align-self:center;">کلاس‌ها هش می‌شوند تا تداخل نکنند.</span>
          </div>
        </div>
        """
    elif tid == 12: # Fragment
        return """
        <div class="react-live-demo">
          <div class="demo-header">🪟 شبیه‌سازی &lt;&gt;...&lt;/&gt; (حذف div اضافی از DOM)</div>
          <p style="font-size:12.5px; color:#cbd5e1;">فرگمنت بدون اضافه کردن حتی یک تگ والد اضافه، چند المان را به صورت تمیز رندر می‌کند:</p>
          <div style="display:flex; gap:8px; padding:8px; background:#020617; border-radius:6px; border:1px solid #1e293b;">
            <span style="background:#1e293b; padding:4px 8px; border-radius:4px; font-size:12px; color:#fff;">آیتم الف</span>
            <span style="background:#1e293b; padding:4px 8px; border-radius:4px; font-size:12px; color:#fff;">آیتم ب</span>
          </div>
        </div>
        """
    elif tid == 13: # Controlled Components
        return """
        <div class="react-live-demo">
          <div class="demo-header">✍️ اینپوت کنترل‌شده همگام با استیت ری‌اکت</div>
          <input type="text" placeholder="چیزی تایپ کنید..." oninput="this.parentElement.querySelector('.ctrl-mirror').innerText = this.value || 'خالی';" style="width:100%; max-width:320px; background:#020617; border:1px solid #334155; color:#fff; padding:6px 12px; border-radius:6px; font-size:13px; outline:none;">
          <div style="margin-top:8px; font-size:12.5px; color:#94a3b8;">
            مقدار استیت جاری (State Value): <strong class="ctrl-mirror" style="color:#fde047;">خالی</strong>
          </div>
        </div>
        """
    elif tid == 14: # useEffect
        return """
        <div class="react-live-demo">
          <div class="demo-header">🔄 شبیه‌سازی چرخه حیات هوک useEffect</div>
          <button onclick="const l=this.parentElement.querySelector('.effect-log'); l.style.display='block'; l.innerHTML='1. کامپوننت Mount شد<br>2. داده از سرور دریافت شد<br>3. تایمر پاکسازی (Cleanup) ثبت گردید';" class="demo-btn">
            اجرای Effect با وابستگی []
          </button>
          <div class="effect-log" style="display:none; margin-top:8px; padding:8px 12px; background:#020617; border-radius:6px; font-size:12px; color:#34d399; font-family:monospace; line-height:1.7;"></div>
        </div>
        """
    elif tid == 15: # Lifting State Up
        return """
        <div class="react-live-demo">
          <div class="demo-header">⬆️ انتقال استیت مشترک به والد (Lifting State Up)</div>
          <p style="font-size:12px; color:#94a3b8; margin-bottom:8px;">تایپ در فرزند اول، فرزند دوم را آپدیت می‌کند:</p>
          <input type="text" placeholder="ورودی فرزند اول..." oninput="this.parentElement.querySelector('.sibling-box').innerText='فرزند دوم دریافت کرد: ' + (this.value || '---');" style="background:#020617; border:1px solid #334155; color:#fff; padding:6px 10px; border-radius:6px; font-size:12px; outline:none; max-width:250px;">
          <div class="sibling-box" style="margin-top:8px; padding:6px 10px; background:#020617; border-radius:6px; font-size:12px; color:#38bdf8;">فرزند دوم دریافت کرد: ---</div>
        </div>
        """
    elif tid == 16: # Props Drilling
        return """
        <div class="react-live-demo">
          <div class="demo-header">🪢 مقایسه مسیر Props Drilling در برابر Context API</div>
          <div style="display:flex; align-items:center; gap:6px; font-size:12px; color:#94a3b8; font-family:monospace; flex-wrap:wrap;">
            <span>&lt;App&gt;</span> ➔ <span>&lt;Layout&gt;</span> ➔ <span>&lt;Sidebar&gt;</span> ➔ <span style="color:#ef4444; font-weight:700;">&lt;UserAvatar&gt;</span>
          </div>
          <p style="font-size:11.5px; color:#64748b; margin-top:6px;">پاس دادن داده از وسط ۴ کامپوننت بدون استفاده؛ راه‌حل: کانتکست یا زاستند.</p>
        </div>
        """
    elif tid == 17: # useRef
        return """
        <div class="react-live-demo">
          <div class="demo-header">🎯 هوک useRef (فوکوس مستقیم روی DOM بدون ری‌رندر)</div>
          <div style="display:flex; gap:10px; align-items:center; margin-top:6px;">
            <input type="text" id="demoRefInput" placeholder="کادر بدون فوکوس..." style="background:#020617; border:1px solid #334155; color:#fff; padding:6px 12px; border-radius:6px; font-size:12px; outline:none;">
            <button onclick="document.getElementById('demoRefInput').focus(); document.getElementById('demoRefInput').style.borderColor='#38bdf8';" class="demo-btn" style="font-size:12px;">
              inputRef.current.focus()
            </button>
          </div>
        </div>
        """
    elif tid == 18: # Context API
        return """
        <div class="react-live-demo">
          <div class="demo-header">🌐 مدیریت تم سراسری با Context API</div>
          <div class="ctx-box" style="background:#020617; padding:12px; border-radius:8px; border:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center; margin-top:6px;">
            <span style="font-size:13px; color:#fff;">پوسته کامپوننت خواننده کانتکست</span>
            <button onclick="const b=this.closest('.ctx-box'); const isD=b.style.background.includes('02'); b.style.background=isD?'#ffffff':'#020617'; b.querySelector('span').style.color=isD?'#000':'#fff'; this.innerText=isD?'حالت شب 🌙':'حالت روز ☀️';" class="demo-btn" style="font-size:11.5px; padding:4px 10px;">حالت روز ☀️</button>
          </div>
        </div>
        """
    elif tid == 19: # useReducer
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚙️ هوک useReducer با الگوی Dispatch Action</div>
          <div style="display:flex; gap:8px; align-items:center; margin-top:6px;">
            <button onclick="const v=this.parentElement.querySelector('.r-val'); v.innerText=parseInt(v.innerText)+10;" class="demo-btn" style="font-size:11.5px;">dispatch({ type: 'ADD_10' })</button>
            <button onclick="const v=this.parentElement.querySelector('.r-val'); v.innerText=0;" class="demo-btn" style="font-size:11.5px; background:#ef4444; color:#fff;">RESET</button>
            <span style="font-size:14px; font-weight:700; color:#38bdf8; margin-right:8px;">مقدار استیت: <span class="r-val">0</span></span>
          </div>
        </div>
        """
    elif tid == 20: # Custom Hooks
        return """
        <div class="react-live-demo">
          <div class="demo-header">🎣 کاستوم هوک useWindowSize اختصاصی</div>
          <p style="font-size:12px; color:#94a3b8; margin-bottom:6px;">ابعاد پنجره مرورگر شما به صورت زنده توسط هوک سفارشی استخراج می‌شود:</p>
          <div style="font-family:monospace; font-size:12px; color:#10b981; background:#020617; padding:6px 12px; border-radius:6px;">
            const { width, height } = useWindowSize(); // <span id="winSize">1920 x 1080</span>
          </div>
        </div>
        """
    elif tid == 21: # React Router
        return """
        <div class="react-live-demo">
          <div class="demo-header">🚦 مسیریابی در لحظه SPA با React Router</div>
          <div style="display:flex; gap:8px; margin-bottom:8px;">
            <button onclick="this.parentElement.nextElementSibling.innerText='صفحه جاری: / (صفحه اصلی فروشگاه)';" class="demo-btn" style="font-size:11px; padding:4px 8px;">&lt;Link to="/" /&gt;</button>
            <button onclick="this.parentElement.nextElementSibling.innerText='صفحه جاری: /cart (سبد خرید شما)';" class="demo-btn" style="font-size:11px; padding:4px 8px;">&lt;Link to="/cart" /&gt;</button>
            <button onclick="this.parentElement.nextElementSibling.innerText='صفحه جاری: /admin (مسیر محافظت‌شده ادمین)';" class="demo-btn" style="font-size:11px; padding:4px 8px;">&lt;Link to="/admin" /&gt;</button>
          </div>
          <div style="padding:8px 12px; background:#020617; border-radius:6px; font-size:12px; color:#38bdf8; font-family:monospace;">
            صفحه جاری: / (صفحه اصلی فروشگاه)
          </div>
        </div>
        """
    elif tid == 22: # Data Fetching
        return """
        <div class="react-live-demo">
          <div class="demo-header">🌐 شبیه‌سازی فراخوانی وب‌سرویس و دریافت داده</div>
          <button onclick="const b=this.nextElementSibling; b.innerText='در حال فراخوانی GET /api/users...'; b.style.display='block'; setTimeout(()=>b.innerHTML='<span style=\\'color:#10b981;\\'>✅ داده‌های سرور دریافت شد: [{ id: 1, name: \\'عرفان\\' }]</span>', 700);" class="demo-btn">
            fetch('/api/users')
          </button>
          <div style="display:none; margin-top:8px; font-family:monospace; font-size:12px; background:#020617; padding:8px 12px; border-radius:6px;"></div>
        </div>
        """
    elif tid == 23: # Loading & Error States
        return """
        <div class="react-live-demo">
          <div class="demo-header">⏳ مدیریت وضعیت سه‌گانه: لودینگ، موفقیت و خطا</div>
          <div style="display:flex; gap:6px; margin-bottom:8px;">
            <button onclick="this.parentElement.nextElementSibling.innerHTML='<span style=\\'color:#f59e0b;\\'>⏳ در حال بارگذاری اسکلتون...</span>';" class="demo-btn" style="font-size:11px; padding:4px 8px;">حالت لودینگ</button>
            <button onclick="this.parentElement.nextElementSibling.innerHTML='<span style=\\'color:#10b981;\\'>✅ دیتا با موفقیت رندر شد.</span>';" class="demo-btn" style="font-size:11px; padding:4px 8px;">حالت موفقیت</button>
            <button onclick="this.parentElement.nextElementSibling.innerHTML='<span style=\\'color:#ef4444;\\'>❌ خطای قطعی اینترنت! [تلاش مجدد]</span>';" class="demo-btn" style="font-size:11px; padding:4px 8px;">حالت خطا</button>
          </div>
          <div style="padding:8px 12px; background:#020617; border-radius:6px; font-size:12px;">
            <span style="color:#10b981;">✅ دیتا با موفقیت رندر شد.</span>
          </div>
        </div>
        """
    elif tid == 24: # Forms with Zod
        return """
        <div class="react-live-demo">
          <div class="demo-header">📝 اعتبارسنجی فرم با اسکیما Zod</div>
          <input type="text" placeholder="شماره موبایل ایران (09...)" oninput="const ok = /^09\\d{9}$/.test(this.value); const err = this.nextElementSibling; err.innerText = ok ? 'شماره موبایل معتبر است ✓' : 'شماره باید با ۰۹ شروع شود و ۱۱ رقم باشد'; err.style.color = ok ? '#10b981' : '#ef4444';" style="background:#020617; border:1px solid #334155; color:#fff; padding:6px 12px; border-radius:6px; font-size:12px; width:100%; max-width:280px; outline:none;">
          <div style="font-size:11.5px; margin-top:4px; color:#ef4444;">شماره باید با ۰۹ شروع شود و ۱۱ رقم باشد</div>
        </div>
        """
    elif tid == 25: # useMemo
        return """
        <div class="react-live-demo">
          <div class="demo-header">🧠 هوک useMemo (کش محاسبات فیلترینگ سنگین)</div>
          <button onclick="const el=this.nextElementSibling; el.innerText = 'محاسبه ۵۰۰۰ رکورد در حافظه کش شد (Memoized in 0.2ms)'; el.style.display='block';" class="demo-btn">
            اجرای تابع فیلتر سنگین
          </button>
          <div style="display:none; margin-top:8px; font-size:12px; color:#38bdf8; background:#020617; padding:6px 10px; border-radius:6px;"></div>
        </div>
        """
    elif tid == 26: # useCallback
        return """
        <div class="react-live-demo">
          <div class="demo-header">🔒 هوک useCallback (تثبیت مرجع تابع در حافظه)</div>
          <p style="font-size:12px; color:#94a3b8; margin-bottom:6px;">آدرس تابع در رم قفل می‌شود تا فرزند React.memo بیهوده ری‌رندر نشود:</p>
          <div style="font-family:monospace; font-size:12px; color:#10b981; background:#020617; padding:6px 10px; border-radius:6px;">
            const handleDelete = useCallback((id) =&gt; ..., []); // Reference Locked ✓
          </div>
        </div>
        """
    elif tid == 27: # React.memo
        return """
        <div class="react-live-demo">
          <div class="demo-header">🛡️ کامپوننت محافظت‌شده با React.memo</div>
          <button onclick="const s=this.nextElementSibling; s.innerText='والد ری‌رندر شد اما فرزند Memo رندر نشد (صرفه‌جویی CPU)!'; s.style.display='block';" class="demo-btn">
            ری‌رندر کردن کامپوننت والد
          </button>
          <div style="display:none; margin-top:8px; font-size:12px; color:#34d399; background:#020617; padding:6px 10px; border-radius:6px;"></div>
        </div>
        """
    elif tid == 28: # useLayoutEffect
        return """
        <div class="react-live-demo">
          <div class="demo-header">📏 اندازه‌گیری موقعیت با useLayoutEffect پیش از نقاشی (Paint)</div>
          <div id="boxMeasure" style="display:inline-block; padding:8px 14px; background:#1e293b; border-radius:6px; color:#fff; font-size:12px;">
            عرض المان: <span id="boxW">۲۱۰</span> پیکسل (بدون پرش دیداری Flicker)
          </div>
        </div>
        """
    elif tid == 29: # Composition Patterns
        return """
        <div class="react-live-demo">
          <div class="demo-header">🧩 ترکیب انعطاف‌پذیر کامپوننت‌ها (Component Composition)</div>
          <div style="display:grid; grid-template-columns:1fr 2fr; gap:8px; margin-top:6px;">
            <div style="background:#020617; padding:8px; border-radius:6px; border:1px solid #1e293b; font-size:11px; color:#38bdf8;">اسلات سایدبار (left)</div>
            <div style="background:#020617; padding:8px; border-radius:6px; border:1px solid #1e293b; font-size:11px; color:#10b981;">اسلات محتوا (right)</div>
          </div>
        </div>
        """
    elif tid == 30: # Portals
        return """
        <div class="react-live-demo">
          <div class="demo-header">🚀 شلیک المان به خارج از والد با createPortal</div>
          <button onclick="alert('مودال مستقیماً در تگ <body> خارج از کانتینر رندر شد!');" class="demo-btn">
            باز کردن مودال با پورتال
          </button>
        </div>
        """
    elif tid == 31: # Error Boundaries
        return """
        <div class="react-live-demo">
          <div class="demo-header">🛡️ مهار خطای کرش کامپوننت با Error Boundary</div>
          <button onclick="const e=this.nextElementSibling; e.style.display='block';" class="demo-btn" style="background:#ef4444; color:#fff;">
            پرتاب خطای فرضی (Simulate Crash)
          </button>
          <div style="display:none; margin-top:8px; padding:8px 12px; background:rgba(239,68,68,0.15); border:1px solid #ef4444; border-radius:6px; color:#f87171; font-size:12px;">
            ⚠️ بخش نظرات با خطا مواجه شد؛ سایر بخش‌های سایت بدون مشکل کار می‌کنند (Graceful Fallback).
          </div>
        </div>
        """
    elif tid == 32: # State Management (Zustand)
        return """
        <div class="react-live-demo">
          <div class="demo-header">🐻 استیت سراسری سریع با Zustand</div>
          <div style="display:flex; gap:10px; align-items:center; margin-top:6px;">
            <button onclick="const s=this.parentElement.querySelector('.z-cnt'); s.innerText=parseInt(s.innerText)+1;" class="demo-btn" style="font-size:11.5px;">+ افزودن به سبد در Zustand</button>
            <span style="font-size:13px; color:#fff;">تعداد اقلام سبد: <strong class="z-cnt" style="color:#10b981;">0</strong> عدد</span>
          </div>
        </div>
        """
    elif tid == 33: # TanStack Query
        return """
        <div class="react-live-demo">
          <div class="demo-header">⚡ کشینگ و تازه کردن داده با TanStack Query</div>
          <button onclick="const b=this.nextElementSibling; b.innerText='داده از کش لوکال خوانده شد (staleTime: 30s) / بدون درخواست مجدد به شبکه!'; b.style.display='block';" class="demo-btn">
            useQuery({ queryKey: ['prices'] })
          </button>
          <div style="display:none; margin-top:8px; font-size:12px; color:#38bdf8; background:#020617; padding:6px 10px; border-radius:6px;"></div>
        </div>
        """
    elif tid == 34: # UI Libraries (shadcn/ui)
        return """
        <div class="react-live-demo">
          <div class="demo-header">🎨 کامپوننت مدرن به سبک shadcn/ui</div>
          <div style="display:flex; gap:8px; margin-top:6px;">
            <button style="background:#fff; color:#000; border:none; padding:6px 14px; border-radius:6px; font-weight:700; font-size:12px; cursor:pointer;">Primary</button>
            <button style="background:transparent; color:#fff; border:1px solid #334155; padding:6px 14px; border-radius:6px; font-size:12px; cursor:pointer;">Outline</button>
            <button style="background:#ef4444; color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:12px; cursor:pointer;">Destructive</button>
          </div>
        </div>
        """
    elif tid == 35: # Tailwind in React
        return """
        <div class="react-live-demo">
          <div class="demo-header">💨 ترکیب کلاس‌های Utility تیلویند در JSX</div>
          <div class="p-3 bg-gradient-to-r from-cyan-900 to-blue-900 rounded-lg text-white font-bold text-xs flex justify-between items-center" style="background:linear-gradient(90deg, #0e7490, #1e3a8a); padding:10px 14px; border-radius:8px;">
            <span>کلاس‌های داینامیک Tailwind</span>
            <span style="background:rgba(255,255,255,0.2); padding:2px 8px; border-radius:4px;">bg-cyan-900</span>
          </div>
        </div>
        """
    return None

print("Part 1 (Topics 1-35) ready.")
