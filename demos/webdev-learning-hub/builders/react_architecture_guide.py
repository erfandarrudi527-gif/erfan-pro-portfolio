# -*- coding: utf-8 -*-
"""
Generate the dedicated React Architecture & Project Structure Guide
explaining Vite folder structure, Feature-Sliced Design (FSD), Layer-based architecture,
and best practices in plain Persian with file-tree diagrams.
"""

REACT_STRUCTURE_HTML = """
<section class="react-architecture-guide" style="margin-bottom: 45px; background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(3, 7, 18, 0.95) 100%); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 20px; padding: 30px; box-shadow: 0 16px 40px -10px rgba(0,0,0,0.7);">
  <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 16px;">
    <div style="display:flex; align-items:center; gap: 12px;">
      <span style="font-size:28px;">📁</span>
      <div>
        <h2 style="font-size:22px; font-weight:900; color:#fff; letter-spacing:-0.5px;">راهنمای جامع پوشه‌بندی و معماری پروژه‌های React</h2>
        <p style="font-size:13px; color:#94a3b8;">چگونه یک پروژه حرفه‌ای ری‌اکت را از روز اول تمیز، مقیاس‌پذیر و تیمی سازمان‌دهی کنیم؟</p>
      </div>
    </div>
    <span style="background:rgba(56, 189, 248, 0.12); color:#38bdf8; font-weight:800; font-size:12px; padding:4px 14px; border-radius:99px; border:1px solid rgba(56, 189, 248, 0.3);">
      معماری سازمانی پروداکشن
    </span>
  </div>

  <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
    <!-- Architecture Model 1: Feature-Based (Recommended) -->
    <div style="background:rgba(2, 6, 23, 0.6); border: 1px solid #1e293b; border-radius: 14px; padding: 20px;">
      <div style="font-size:15px; font-weight:800; color:#38bdf8; margin-bottom: 8px;">
        ۱. ساختار مدرن ویژگی‌محور (Feature-Based / FSD)
      </div>
      <p style="font-size:13px; color:#cbd5e1; line-height:1.8; margin-bottom: 14px;">
        بهترین روش در شرکت‌های بزرگ: هر بخش برنامه (مثل لاگین یا سبد خرید) یک جزیره مستقل است و کدهای آن در یک پوشه زندگی می‌کنند.
      </p>

      <div style="background:#02040a; border:1px solid #1e293b; border-radius: 10px; padding: 14px; font-family: monospace; font-size:12px; color:#93c5fd; direction:ltr; text-align:left; line-height:1.7;">
        src/<br>
        ├── <strong>assets/</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#64748b;"># فونت‌ها و تصاویر</span><br>
        ├── <strong>components/</strong> &nbsp;<span style="color:#64748b;"># دکمه‌ها و فرم‌های مشترک عمومی</span><br>
        │ &nbsp; ├── ui/Button.jsx<br>
        │ &nbsp; └── ui/Modal.jsx<br>
        ├── <strong>features/</strong> &nbsp;&nbsp;&nbsp;<span style="color:#34d399;"># پوشه ماژول‌ها و فیچرهای اصلی</span><br>
        │ &nbsp; ├── <strong>auth/</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#64748b;">(کامپوننت‌ها و هوک‌های لاگین)</span><br>
        │ &nbsp; │ &nbsp; ├── components/LoginForm.jsx<br>
        │ &nbsp; │ &nbsp; ├── hooks/useAuth.js<br>
        │ &nbsp; │ &nbsp; └── authSlice.js<br>
        │ &nbsp; └── <strong>cart/</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#64748b;">(سبد خرید مستقل)</span><br>
        ├── <strong>hooks/</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#64748b;"># هوک‌های سراسری (useDebounce, ...)</span><br>
        ├── <strong>services/</strong> &nbsp;&nbsp;&nbsp;<span style="color:#64748b;"># ارتباط با سرور و تنظیم Axios</span><br>
        ├── <strong>utils/</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#64748b;"># فرمت قیمت به ریال/تومان، تاریخ</span><br>
        ├── App.jsx<br>
        └── main.jsx
      </div>
    </div>

    <!-- Explanation & Best Practices -->
    <div style="background:rgba(2, 6, 23, 0.6); border: 1px solid #1e293b; border-radius: 14px; padding: 20px; display:flex; flex-direction:column; justify-content:space-between;">
      <div>
        <div style="font-size:15px; font-weight:800; color:#10b981; margin-bottom: 8px;">
          ۲. قوانین طلایی در پوشه‌بندی React
        </div>
        <ul style="padding-right:20px; color:#cbd5e1; font-size:13px; line-height:2;">
          <li><strong>اصل تک‌مسئولیتی:</strong> هر فایل فقط باید یک کار مشخص انجام دهد (کامپوننت فقط ظاهر، هوک فقط منطق استیت).</li>
          <li><strong>جداسازی کامپوننت‌های عمومی:</strong> دکمه، اینپوت، تول‌تیپ و لودینگ در <code>components/ui/</code> قرار می‌گیرند تا در تمام صفحات استفاده شوند.</li>
          <li><strong>استفاده از Path Alias:</strong> به جای نوشتن مسیرهای خسته‌کننده مثل <code>../../../components</code> از علامت <code>@/components</code> در vite.config استفاده کنید.</li>
          <li><strong>قرارداد نام‌گذاری:</strong> کامپوننت‌ها با حروف بزرگ (PascalCase مانند <code>Navbar.jsx</code>) و هوک‌ها با کلمه کوچک <code>use</code> مانند <code>useCart.js</code> نام‌گذاری می‌شوند.</li>
        </ul>
      </div>

      <div style="background:rgba(56, 189, 248, 0.08); border-right: 3px solid #38bdf8; padding: 12px 16px; border-radius: 0 8px 8px 0; margin-top: 14px;">
        <span style="font-size:12.5px; font-weight:700; color:#38bdf8;">⚡ نکته حرفه‌ای:</span>
        <p style="font-size:12px; color:#cbd5e1; margin-top:2px;">
          برای پروژه‌های زیر ۱۰ صفحه از ساختار ساده Layer-based (پوشه‌های مستقیم components, hooks, pages) استفاده کنید و زمانی که صفحات از ۱۰ گذشت به ساختار Features مهاجرت نمایید.
        </p>
      </div>
    </div>
  </div>
</section>
"""

print("React Architecture and Folder Structure Guide ready!")
