/**
 * MAHASTAN HOTEL - REGISTER JS
 */

document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("registerForm");
  const toggleBtn = document.getElementById("togglePassword");
  const passInput = document.getElementById("password");
  const msgEl = document.getElementById("registerMessage");

  if (toggleBtn && passInput) {
    toggleBtn.addEventListener("click", () => {
      const isPass = passInput.type === "password";
      passInput.type = isPass ? "text" : "password";
      toggleBtn.innerHTML = isPass ? '<i class="fa-regular fa-eye-slash"></i>' : '<i class="fa-regular fa-eye"></i>';
    });
  }

  if (registerForm) {
    registerForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const fullName = document.getElementById("fullName").value.trim();
      const email = document.getElementById("email").value.trim().toLowerCase();
      const password = passInput.value.trim();
      const confirmPassword = document.getElementById("confirmPassword").value.trim();

      if (!fullName || !email || !password || !confirmPassword) {
        msgEl.className = "auth-message error";
        msgEl.textContent = "لطفاً تمامی فیلدها را پر کنید.";
        return;
      }

      if (password.length < 6) {
        msgEl.className = "auth-message error";
        msgEl.textContent = "رمز عبور باید حداقل ۶ کاراکتر باشد.";
        return;
      }

      if (password !== confirmPassword) {
        msgEl.className = "auth-message error";
        msgEl.textContent = "رمز عبور و تکرار آن مطابقت ندارند.";
        return;
      }

      const users = JSON.parse(localStorage.getItem("mahastan_users") || "[]");
      if (users.some(u => u.email === email)) {
        msgEl.className = "auth-message error";
        msgEl.textContent = "این ایمیل قبلاً در سیستم ثبت شده است.";
        return;
      }

      users.push({ fullName, email, password });
      localStorage.setItem("mahastan_users", JSON.stringify(users));

      msgEl.className = "auth-message success";
      msgEl.textContent = "حساب کاربری با موفقیت ساخته شد. در حال انتقال به صفحه ورود...";

      showToast("ثبت‌نام شما با موفقیت انجام شد ✨", "success");

      setTimeout(() => {
        window.location.href = "login.html";
      }, 1500);
    });
  }
});
