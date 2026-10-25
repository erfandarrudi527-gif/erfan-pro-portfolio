/**
 * MAHASTAN HOTEL - LOGIN JS
 */

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const toggleBtn = document.getElementById("toggleLoginPassword");
  const passInput = document.getElementById("loginPassword");
  const msgEl = document.getElementById("loginMessage");

  if (toggleBtn && passInput) {
    toggleBtn.addEventListener("click", () => {
      const isPass = passInput.type === "password";
      passInput.type = isPass ? "text" : "password";
      toggleBtn.innerHTML = isPass ? '<i class="fa-regular fa-eye-slash"></i>' : '<i class="fa-regular fa-eye"></i>';
    });
  }

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const email = document.getElementById("loginEmail").value.trim().toLowerCase();
      const password = passInput.value.trim();

      if (!email || !password) {
        msgEl.className = "auth-message error";
        msgEl.textContent = "لطفاً تمامی فیلدها را پر کنید.";
        return;
      }

      const users = JSON.parse(localStorage.getItem("mahastan_users") || "[]");
      const found = users.find(u => u.email === email && u.password === password);

      // Demo login fallback if empty
      if (!found && email !== "demo@mahastan.ir") {
        msgEl.className = "auth-message error";
        msgEl.textContent = "اطلاعات ورود نادرست است (می‌توانید از هر ایمیل و رمز دلخواه جهت تست ثبت‌نام کنید).";
        return;
      }

      const userObj = found || { name: "میهمان گرامی", email: email };
      localStorage.setItem("mahastan_logged_user", JSON.stringify(userObj));

      msgEl.className = "auth-message success";
      msgEl.textContent = "ورود با موفقیت انجام شد. در حال انتقال...";

      showToast("ورود موفقیت‌آمیز بود ✨", "success");

      setTimeout(() => {
        window.location.href = "../index.html";
      }, 1200);
    });
  }
});
