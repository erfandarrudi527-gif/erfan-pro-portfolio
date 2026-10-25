"use strict";

/* ==========================================================
   anim.js — انیمیشن‌ها و تعاملات جذاب سایت مهستان
   ========================================================== */

/* ---------- 1) نوار پیشرفت اسکرول ---------- */
const progressBar = document.getElementById("scroll-progress-bar");

function updateProgress() {
  if (!progressBar) return;
  const doc = document.documentElement;
  const max = doc.scrollHeight - doc.clientHeight;
  const percent = max > 0 ? (window.scrollY / max) * 100 : 0;
  progressBar.style.width = percent + "%";
}

/* ---------- 2) هدر چسبان حالت‌دار ---------- */
const siteHeader = document.getElementById("site-header");

function updateHeaderState() {
  if (!siteHeader) return;
  siteHeader.classList.toggle("scrolled", window.scrollY > 40);
}

window.addEventListener("scroll", () => {
  updateProgress();
  updateHeaderState();
});
updateProgress();
updateHeaderState();

/* ---------- 3) سیستم Scroll Reveal برای data-aos ---------- */
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const delay = parseInt(el.getAttribute("data-aos-delay") || "0", 10);
        setTimeout(() => el.classList.add("aos-animate"), delay);
        revealObserver.unobserve(el);
      }
    });
  },
  { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
);

function observeNewElements(root = document) {
  root.querySelectorAll("[data-aos]:not(.aos-animate)").forEach((el) => {
    revealObserver.observe(el);
  });
}

observeNewElements();

/* ---------- 4) ظاهر شدن تدریجی کارت‌های داینامیک ---------- */
function staggerReveal(container, aosType = "fade-up", step = 140) {
  if (!container) return;
  Array.from(container.children).forEach((child, index) => {
    if (child.dataset.aosDone) return;
    child.dataset.aosDone = "1";
    child.setAttribute("data-aos", aosType);
    child.classList.remove("aos-animate");
    setTimeout(() => {
      child.classList.add("aos-animate");
    }, 120 + index * step);
  });
}

/* وقتی اتاق‌ها و نظرات لود شدند، یکی‌یکی ظاهر شوند */
function watchAndAnimate(containerSelector, aosType) {
  const target = document.querySelector(containerSelector);
  if (!target) return;

  const mo = new MutationObserver(() => {
    if (target.children.length > 0) staggerReveal(target, aosType);
  });
  mo.observe(target, { childList: true });
  if (target.children.length > 0) staggerReveal(target, aosType);
}

watchAndAnimate(".rooms-cart-section", "zoom-in");
watchAndAnimate(".comments-root", "fade-up");
watchAndAnimate("#productsGrid", "zoom-in");

/* ---------- 5) افکت تایپ نام هتل ---------- */
const typingEl = document.getElementById("hotel-name-typing");

if (typingEl) {
  const finalText = typingEl.textContent.trim();
  typingEl.textContent = "";
  let charIndex = 0;

  const typeInterval = setInterval(() => {
    typingEl.textContent += finalText.charAt(charIndex);
    charIndex += 1;
    if (charIndex >= finalText.length) {
      clearInterval(typeInterval);
      setTimeout(() => typingEl.classList.add("done"), 1200);
    }
  }, 160);
}

/* ---------- 6) آکاردئون سوالات متداول ---------- */
document.querySelectorAll(".questions-and-answer-box").forEach((box) => {
  const question = box.querySelector(".questions");
  const answer = box.querySelector(".answer");
  if (!question || !answer) return;

  question.addEventListener("click", () => {
    const isOpen = question.classList.contains("open");

    // بستن بقیه
    document.querySelectorAll(".questions.open").forEach((other) => {
      if (other === question) return;
      other.classList.remove("open");
      const otherAnswer = other.parentElement.querySelector(".answer");
      if (otherAnswer) {
        otherAnswer.classList.remove("show-anim");
        otherAnswer.classList.add("hide-anim");
        setTimeout(() => {
          otherAnswer.classList.remove("show", "hide-anim");
        }, 320);
      }
    });

    if (isOpen) {
      question.classList.remove("open");
      answer.classList.remove("show-anim");
      answer.classList.add("hide-anim");
      setTimeout(() => {
        answer.classList.remove("show", "hide-anim");
      }, 320);
    } else {
      question.classList.add("open");
      answer.classList.remove("hide-anim");
      answer.classList.add("show", "show-anim");
    }
  });
});

/* ---------- 7) دکمه برو بالا ---------- */
const scrollTopBtn = document.getElementById("scroll-top-btn");

if (scrollTopBtn) {
  scrollTopBtn.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

/* ---------- 8) افکت پارالاکس نرم تصویر hero ---------- */
const heroImg = document.querySelector(".img-in-top-information img");

if (heroImg && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const heroWrap = document.querySelector(".img-in-top-information");
  heroWrap.addEventListener("mousemove", (e) => {
    const rect = heroWrap.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    heroImg.style.transform = `translate(${x * 14}px, ${y * 14}px) rotate(${
      x * 3
    }deg)`;
    heroImg.classList.remove("float-slow");
  });
  heroWrap.addEventListener("mouseleave", () => {
    heroImg.style.transform = "";
    heroImg.classList.add("float-slow");
  });
}

/* ---------- 9) تilt سه‌بعدی کارت خدمات ---------- */
if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelectorAll(".slider-card").forEach((card) => {
    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(600px) rotateY(${x * 12}deg) rotateX(${
        -y * 12
      }deg) translateY(-8px) scale(1.04)`;
    });
    card.addEventListener("mouseleave", () => {
      card.style.transform = "";
    });
  });
}
