// Erfan Portfolio Core Application Logic (v4.5 Luxury High-Motion Edition)
document.addEventListener('DOMContentLoaded', () => {
  initLiveClock();
  initCursorGlow();
  initScrollProgressBar();
  initCanvasBackground();
  initContinuousScrollReveal();
  renderProjects('all');
  initFilterTabs();
  initSearch();
  initComponentSandbox();
  initBrewLab();
  initTerminal();
  initCommandPalette();
  initSoundToggle();
  initContactModal();
});

// 1. Scroll Progress Bar
function initCursorGlow() {
  const glow = document.createElement('div');
  glow.id = 'cursorGlow';
  document.body.appendChild(glow);

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let curX = mouseX;
  let curY = mouseY;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  }, { passive: true });

  function follow() {
    curX += (mouseX - curX) * 0.12;
    curY += (mouseY - curY) * 0.12;
    glow.style.left = curX + 'px';
    glow.style.top = curY + 'px';
    requestAnimationFrame(follow);
  }
  follow();
}

function initScrollProgressBar() {
  const bar = document.getElementById('scrollProgress');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    const progress = total > 0 ? (window.scrollY / total) * 100 : 0;
    bar.style.width = `${progress}%`;
  }, { passive: true });
}

// 2. Live UTC Clock
function initLiveClock() {
  const clockEl = document.getElementById('liveClock');
  if (!clockEl) return;
  const update = () => {
    const now = new Date();
    const utc = now.toUTCString().split(' ')[4];
    clockEl.textContent = `${utc} UTC`;
  };
  update();
  setInterval(update, 1000);
}

// 3. Continuous Bi-Directional Scroll Reveal
function initContinuousScrollReveal() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      } else {
        entry.target.classList.remove('visible');
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal-item').forEach(el => observer.observe(el));
}

// 4. Subtle Starfield / Particle Background (Zero-lag Canvas 2D)
function initCanvasBackground() {
  const canvas = document.getElementById('bgCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let width = canvas.width = window.innerWidth;
  let height = canvas.height = window.innerHeight;

  const particles = [];
  const count = Math.min(width > 768 ? 65 : 30, 85);

  for (let i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      r: Math.random() * 1.5 + 0.6,
      alpha: Math.random() * 0.55 + 0.25
    });
  }

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  function draw() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 0) p.x = width;
      if (p.x > width) p.x = 0;
      if (p.y < 0) p.y = height;
      if (p.y > height) p.y = 0;

      // Draw particle in liquid optic glow
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(0, 174, 239, ${p.alpha * 0.75})`;
      ctx.fill();

      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j];
        const dx = p.x - p2.x;
        const dy = p.y - p2.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = `rgba(0, 174, 239, ${0.16 * (1 - dist / 120)})`;
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
}

// 5. 3D Tilt Card Interaction
function handleCardTilt(e, card) {
  const rect = card.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  
  const midX = rect.width / 2;
  const midY = rect.height / 2;
  
  const rotateX = ((y - midY) / midY) * -7;
  const rotateY = ((x - midX) / midX) * 7;
  
  card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
  card.style.setProperty('--mx', `${(x / rect.width) * 100}%`);
  card.style.setProperty('--my', `${(y / rect.height) * 100}%`);
}

function handleCardReset(card) {
  card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)`;
}

// 6. Audio Synthesizer Toggle
function initSoundToggle() {
  const btn = document.getElementById('soundToggleBtn');
  if (!btn) return;
  btn.addEventListener('click', () => {
    const isEnabled = Sound.toggle();
    btn.innerHTML = isEnabled 
      ? `<i class="fa-solid fa-volume-high"></i>` 
      : `<i class="fa-solid fa-volume-xmark"></i>`;
    showToast(isEnabled ? 'Audio Feedback Enabled' : 'Audio Feedback Muted');
  });
}

// 7. Render Projects with 3D Tilt & Micro-Metrics
function renderProjects(category = 'all', searchQuery = '') {
  const grid = document.getElementById('projectsGrid');
  if (!grid) return;

  let filtered = PROJECTS_DATA;
  if (category !== 'all') {
    filtered = filtered.filter(p => p.category === category);
  }
  if (searchQuery.trim()) {
    const q = searchQuery.toLowerCase().trim();
    filtered = filtered.filter(p => 
      p.title.toLowerCase().includes(q) ||
      p.description.toLowerCase().includes(q) ||
      p.stack.some(s => s.toLowerCase().includes(q))
    );
  }

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 48px; color: var(--text-dim);">
        <i class="fa-solid fa-folder-open" style="font-size: 36px; margin-bottom: 12px; display: block; color: var(--accent);"></i>
        No projects match your filter. Try another keyword or stack.
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(p => `
    <article class="project-card reveal-item" 
             style="--card-accent: ${p.color};"
             onmousemove="handleCardTilt(event, this)" 
             onmouseleave="handleCardReset(this)"
             onmouseenter="if(window.Sound)Sound.playHover()">
      <div>
        <div class="card-top">
          <span class="card-badge mono" style="color: ${p.color}; border-color: ${p.color}44;">${p.badge}</span>
          <span class="mono" style="font-size: 11px; color: var(--text-dim);">${p.category.toUpperCase()} // ${p.year || '2026'}</span>
        </div>
        <h3 class="card-title">${p.title}</h3>
        <p class="card-tagline mono">${p.tagline}</p>
        <p class="card-desc">${p.description}</p>
      </div>

      <div>
        <div class="card-stack">
          ${p.stack.map(s => `<span class="stack-tag">${s}</span>`).join('')}
        </div>
        <div class="card-actions">
          <button class="btn-outline" style="font-size: 12px; padding: 7px 14px;" onclick="openProjectModal('${p.id}'); if(window.Sound)Sound.playClick();">
            <i class="fa-solid fa-circle-info"></i> Architecture
          </button>
          <button class="btn-primary" style="font-size: 12px; padding: 7px 14px;" onclick="openLiveViewModal('${p.liveUrl}', '${p.title.replace(/'/g, "\\\\'")}'); if(window.Sound)Sound.playClick();">
            <i class="fa-solid fa-play"></i> Quick Preview
          </button>
          <a href="${p.liveUrl}" ${p.liveUrl.startsWith('http') || p.liveUrl.includes('demos/') ? 'target="_blank"' : ''} class="btn-outline" style="font-size: 12px; padding: 7px 14px;" onclick="if(window.Sound)Sound.playClick();">
            <i class="fa-solid fa-arrow-up-right-from-square"></i> New Tab ↗
          </a>
        </div>
      </div>
    </article>
  `).join('');

  // re-observe newly created project elements
  initContinuousScrollReveal();
}

// 8. Filter & Search
function initFilterTabs() {
  const pills = document.querySelectorAll('.filter-pill');
  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      if (window.Sound) Sound.playClick();
      const cat = pill.getAttribute('data-cat');
      const searchVal = document.getElementById('projectSearchInput')?.value || '';
      renderProjects(cat, searchVal);
    });
  });
}

function initSearch() {
  const input = document.getElementById('projectSearchInput');
  if (!input) return;
  input.addEventListener('input', (e) => {
    const activePill = document.querySelector('.filter-pill.active');
    const cat = activePill ? activePill.getAttribute('data-cat') : 'all';
    renderProjects(cat, e.target.value);
  });
}

// 9. Interactive Component Sandbox
function initComponentSandbox() {
  initProjectEstimator();
  const presetSelect = document.getElementById('sandboxPreset');
  const glowSlider = document.getElementById('sandboxGlow');
  const blurSlider = document.getElementById('sandboxBlur');
  const radiusSlider = document.getElementById('sandboxRadius');
  const previewTarget = document.getElementById('sandboxLiveTarget');
  const codeOutput = document.getElementById('sandboxCodeOutput');

  if (!presetSelect || !previewTarget || !codeOutput) return;

  function update() {
    const preset = presetSelect.value;
    const glow = glowSlider ? glowSlider.value : 25;
    const blur = blurSlider ? blurSlider.value : 14;
    const radius = radiusSlider ? radiusSlider.value : 12;

    let cssText = '';
    if (preset === 'button') {
      previewTarget.innerHTML = `<button style="background: linear-gradient(135deg, #6366f1, #3b82f6); color: #fff; padding: 12px 28px; border-radius: ${radius}px; border: 1px solid rgba(255,255,255,0.25); box-shadow: 0 0 ${glow}px rgba(99, 102, 241, 0.7); font-family: var(--font-sans); font-weight: 700; cursor: pointer; backdrop-filter: blur(${blur}px); transition: transform 0.2s;" onmouseenter="this.style.transform='scale(1.05)'" onmouseleave="this.style.transform='scale(1)'">Interactive CTA ↗</button>`;
      cssText = `button {\n  background: linear-gradient(135deg, #6366f1, #3b82f6);\n  border-radius: ${radius}px;\n  box-shadow: 0 0 ${glow}px rgba(99, 102, 241, 0.7);\n  backdrop-filter: blur(${blur}px);\n  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);\n}`;
    } else if (preset === 'glass') {
      previewTarget.innerHTML = `<div style="background: rgba(14, 20, 34, 0.65); border: 1px solid rgba(99, 102, 241, 0.45); border-radius: ${radius}px; padding: 22px 30px; box-shadow: 0 0 ${glow}px rgba(6, 182, 212, 0.3); backdrop-filter: blur(${blur}px); text-align: center;"><div class="mono" style="font-size: 11px; color: #38bdf8;">OLED GLASSMETRIC</div><div style="font-weight: 800; font-size: 16px; margin-top: 4px;">Dynamic Glass UI</div></div>`;
      cssText = `.glass-card {\n  background: rgba(14, 20, 34, 0.65);\n  border: 1px solid rgba(99, 102, 241, 0.45);\n  border-radius: ${radius}px;\n  backdrop-filter: blur(${blur}px);\n  box-shadow: 0 0 ${glow}px rgba(6, 182, 212, 0.3);\n}`;
    } else if (preset === 'badge') {
      previewTarget.innerHTML = `<span style="background: rgba(16, 185, 129, 0.12); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.45); padding: 8px 18px; border-radius: ${radius}px; font-family: var(--font-mono); font-size: 13px; font-weight: 700; box-shadow: 0 0 ${glow}px rgba(16, 185, 129, 0.45);">● SYSTEM HEALTH: 100%</span>`;
      cssText = `.live-badge {\n  background: rgba(16, 185, 129, 0.12);\n  color: #34d399;\n  border-radius: ${radius}px;\n  box-shadow: 0 0 ${glow}px rgba(16, 185, 129, 0.45);\n}`;
    }
    codeOutput.textContent = cssText;
  }

  presetSelect.addEventListener('change', () => { update(); if (window.Sound) Sound.playClick(); });
  if (glowSlider) glowSlider.addEventListener('input', () => { update(); if (window.Sound) Sound.playHover(); });
  if (blurSlider) blurSlider.addEventListener('input', () => { update(); if (window.Sound) Sound.playHover(); });
  if (radiusSlider) radiusSlider.addEventListener('input', () => { update(); if (window.Sound) Sound.playHover(); });
  update();
}

// 9.1 Interactive Project Budget & Architecture Estimator (Toman Currency)
function initProjectEstimator() {
  const container = document.getElementById('estimator');
  if (!container) return;

  const state = {
    scope: 'fullstack',
    timeline: 'standard',
    addons: new Set(['seo'])
  };

  // Prices in Tomans
  const prices = {
    scope: {
      landing: 18000000,     // 18 Million Tomans
      webapp: 38000000,      // 38 Million Tomans
      fullstack: 58000000,   // 58 Million Tomans
      cms: 45000000          // 45 Million Tomans
    },
    timeline: { standard: 1.0, rush: 1.3, flex: 0.9 },
    addons: {
      seo: 6500000,
      sound: 4000000,
      pwa: 8500000,
      motion: 7500000
    }
  };

  const days = {
    scope: {
      landing: '۵ الی ۷ روز کاری',
      webapp: '۱۴ الی ۲۱ روز کاری',
      fullstack: '۳ الی ۴ هفته کاری',
      cms: '۲ الی ۳ هفته کاری'
    }
  };

  const scopeLabels = {
    landing: 'لندینگ پیج اختصاصی',
    webapp: 'وب‌اپلیکیشن ری‌اکت',
    fullstack: 'فول‌استک Next.js 15',
    cms: 'هدلس CMS سازمانی'
  };

  function update() {
    let base = prices.scope[state.scope] || 35000000;
    let addSum = 0;
    state.addons.forEach(a => { addSum += (prices.addons[a] || 0); });
    
    let subtotal = (base + addSum) * (prices.timeline[state.timeline] || 1.0);
    let finalEst = Math.round(subtotal);

    const targetEst = document.getElementById('estFinalPrice');
    const targetDays = document.getElementById('estTimelineDays');
    const targetScope = document.getElementById('estScopeLabel');
    if (targetEst) {
      targetEst.innerHTML = `<span style="font-size: 26px;">${finalEst.toLocaleString('fa-IR')}</span> <span style="font-size: 14px; font-weight: 600; color: #a5b4fc;">تومان</span>`;
    }
    if (targetDays) targetDays.textContent = days.scope[state.scope];
    if (targetScope) targetScope.textContent = scopeLabels[state.scope] || state.scope.toUpperCase();
  }

  // Bind clicks
  container.querySelectorAll('.est-pill[data-group]').forEach(pill => {
    pill.addEventListener('click', () => {
      const group = pill.getAttribute('data-group');
      const val = pill.getAttribute('data-val');

      if (group === 'addon') {
        if (state.addons.has(val)) {
          state.addons.delete(val);
          pill.classList.remove('active');
        } else {
          state.addons.add(val);
          pill.classList.add('active');
        }
      } else {
        container.querySelectorAll(`.est-pill[data-group="${group}"]`).forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state[group] = val;
      }

      if (window.Sound) Sound.playClick();
      update();
    });
  });

  update();
}

function forwardEstimatorToContact() {
  const scope = document.getElementById('estScopeLabel')?.textContent || 'FULLSTACK';
  const price = document.getElementById('estFinalPrice')?.textContent || '';
  const days = document.getElementById('estTimelineDays')?.textContent || '';
  const query = `?scope=${encodeURIComponent(scope)}&price=${encodeURIComponent(price)}&timeline=${encodeURIComponent(days)}`;
  window.location.href = 'contact.html' + query;
}

// 10. DUN Brew Lab Engine & Live Pour Simulation
let pourTimerInterval = null;
function initBrewLab() {
  const doseSlider = document.getElementById('brewDose');
  const ratioSlider = document.getElementById('brewRatio');
  const methodSelect = document.getElementById('brewMethod');
  const startBtn = document.getElementById('startPourBtn');

  if (!doseSlider || !ratioSlider || !methodSelect) return;

  const calculate = () => {
    const dose = parseFloat(doseSlider.value);
    const ratio = parseFloat(ratioSlider.value);
    const method = methodSelect.value;
    const water = Math.round(dose * ratio);
    const bloom = Math.round(dose * 2.5);
    const firstPour = Math.round((water - bloom) * 0.6);
    const finalPour = water - bloom - firstPour;

    let time = "2:30 - 3:00";
    let grind = "Medium-Fine (550-650 µm)";
    if (method === 'chemex') {
      time = "3:30 - 4:15";
      grind = "Medium-Coarse (750-850 µm)";
    } else if (method === 'aeropress') {
      time = "1:30 - 2:00";
      grind = "Fine-Medium (400-500 µm)";
    } else if (method === 'frenchpress') {
      time = "4:00 - 5:00";
      grind = "Coarse (900-1100 µm)";
    }

    document.getElementById('dispDose').textContent = `${dose}g`;
    document.getElementById('dispRatio').textContent = `1:${ratio}`;
    document.getElementById('resWater').textContent = `${water} ml`;
    document.getElementById('resBloom').textContent = `${bloom} ml`;
    document.getElementById('resPours').textContent = `${firstPour} ml / ${finalPour} ml`;
    document.getElementById('resTime').textContent = time;
    document.getElementById('resGrind').textContent = grind;
  };

  doseSlider.addEventListener('input', () => { calculate(); if(window.Sound) Sound.playHover(); });
  ratioSlider.addEventListener('input', () => { calculate(); if(window.Sound) Sound.playHover(); });
  methodSelect.addEventListener('change', () => { calculate(); if(window.Sound) Sound.playClick(); });

  if (startBtn) {
    startBtn.addEventListener('click', () => {
      if (pourTimerInterval) {
        clearInterval(pourTimerInterval);
        pourTimerInterval = null;
        startBtn.innerHTML = `<i class="fa-solid fa-play"></i> Start Extraction Timer`;
        showToast('Pour timer reset');
        return;
      }

      let elapsed = 0;
      if (window.Sound) Sound.playSuccess();
      startBtn.innerHTML = `<i class="fa-solid fa-stop"></i> Stop Timer (<span id="pourElapsed">0s</span>)`;

      pourTimerInterval = setInterval(() => {
        elapsed++;
        const elSpan = document.getElementById('pourElapsed');
        if (elSpan) elSpan.textContent = `${elapsed}s`;

        if (elapsed === 45) {
          if (window.Sound) Sound.playBeep(880, 'sine', 0.2, 0.1);
          showToast('Bloom Complete (45s)! Begin first main pour.');
        } else if (elapsed === 120) {
          if (window.Sound) Sound.playBeep(980, 'sine', 0.2, 0.1);
          showToast('Stage 2 Complete (2:00)! Begin final pour.');
        } else if (elapsed >= 180) {
          clearInterval(pourTimerInterval);
          pourTimerInterval = null;
          startBtn.innerHTML = `<i class="fa-solid fa-check"></i> Extraction Finished!`;
          if (window.Sound) Sound.playSuccess();
          showToast('Target yield reached. Enjoy your brew!');
        }
      }, 1000);
    });
  }

  calculate();
}

// 11. Command Palette (Cmd+K / Ctrl+K Spotlight)
function initCommandPalette() {
  const overlay = document.getElementById('cmdPalette');
  const input = document.getElementById('cmdInput');
  const triggerBtn = document.getElementById('cmdTriggerBtn');

  if (!overlay || !input) return;

  function open() {
    overlay.classList.add('open');
    input.value = '';
    filterCommands('');
    input.focus();
    if (window.Sound) Sound.playClick();
  }

  function close() {
    overlay.classList.remove('open');
    if (window.Sound) Sound.playClick();
  }

  if (triggerBtn) triggerBtn.addEventListener('click', open);

  window.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (overlay.classList.contains('open')) close();
      else open();
    } else if (e.key === 'Escape' && overlay.classList.contains('open')) {
      close();
    }
  });

  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) close();
  });

  input.addEventListener('input', (e) => {
    filterCommands(e.target.value.toLowerCase().trim());
  });

  const cmdList = document.getElementById('cmdList');
  if (cmdList) {
    cmdList.innerHTML += `
      <div class="cmd-group-title">Interactive Live Apps</div>
      <div class="cmd-item" onclick="openLiveViewModal('demos/webdev-learning-hub/index.html', 'WebDev Master Learning Hub')">
        <span><i class="fa-solid fa-code" style="width: 20px; color: #10b981;"></i> Launch WebDev Hub</span>
        <span class="mono" style="font-size: 11px; color: var(--text-dim);">Live App</span>
      </div>
      <div class="cmd-item" onclick="openLiveViewModal('demos/barg-reader/index.html', 'Barg Reader App')">
        <span><i class="fa-solid fa-book-open" style="width: 20px; color: #06b6d4;"></i> Launch Barg Reader</span>
        <span class="mono" style="font-size: 11px; color: var(--text-dim);">Live App</span>
      </div>
      <div class="cmd-item" onclick="openLiveViewModal('demos/parsa-sports/index.html', 'Parsa Sports Store')">
        <span><i class="fa-solid fa-cart-shopping" style="width: 20px; color: #ec4899;"></i> Launch Parsa Sports</span>
        <span class="mono" style="font-size: 11px; color: var(--text-dim);">Live App</span>
      </div>
    `;
  }
}

function filterCommands(q) {
  const items = document.querySelectorAll('.cmd-item');
  items.forEach(item => {
    const text = item.textContent.toLowerCase();
    item.style.display = text.includes(q) ? 'flex' : 'none';
  });
}

function runCmd(action) {
  const overlay = document.getElementById('cmdPalette');
  if (overlay) overlay.classList.remove('open');

  switch (action) {
    case 'estimator':
      document.getElementById('estimator')?.scrollIntoView({ behavior: 'smooth' });
      break;
    case 'projects':
      document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' });
      break;
    case 'sandbox':
      document.getElementById('sandbox')?.scrollIntoView({ behavior: 'smooth' });
      break;
    case 'brew':
      document.getElementById('brew-lab-section')?.scrollIntoView({ behavior: 'smooth' });
      break;
    case 'terminal':
      document.getElementById('terminal')?.scrollIntoView({ behavior: 'smooth' });
      break;
    case 'resume':
      window.location.href = 'resume.html';
      break;
    case 'contact':
      window.location.href = 'contact.html';
      break;
    case 'sound':
      const isEnabled = Sound.toggle();
      showToast(isEnabled ? 'Sound Enabled' : 'Sound Muted');
      break;
    case 'github':
      window.open('https://github.com/erfandarrudi527-gif', '_blank');
      break;
    case 'telegram':
      window.open('https://t.me/erfan_sadeghi', '_blank');
      break;
    case 'email':
      copyText('erfandarrudi527@gmail.com', 'Email copied to clipboard!');
      break;
  }
}

// 12. Interactive Terminal
function initTerminal() {
  const input = document.getElementById('termInput');
  const output = document.getElementById('termOutput');
  if (!input || !output) return;

  const history = [];
  let historyIdx = -1;

  const printLine = (text, isHtml = false) => {
    const div = document.createElement('div');
    div.className = 'term-line';
    if (isHtml) div.innerHTML = text;
    else div.textContent = text;
    output.appendChild(div);
    output.scrollTop = output.scrollHeight;
  };

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const cmd = input.value.trim();
      if (!cmd) return;
      history.push(cmd);
      historyIdx = history.length;
      input.value = '';
      if (window.Sound) Sound.playClick();

      printLine(`<span class="term-prompt">visitor@erfan-os:~$</span> ${cmd}`, true);
      executeCommand(cmd.toLowerCase(), printLine);
    } else if (e.key === 'ArrowUp') {
      if (history.length > 0 && historyIdx > 0) {
        historyIdx--;
        input.value = history[historyIdx];
      }
    } else if (e.key === 'ArrowDown') {
      if (historyIdx < history.length - 1) {
        historyIdx++;
        input.value = history[historyIdx];
      } else {
        historyIdx = history.length;
        input.value = '';
      }
    }
  });
}

function executeCommand(cmd, print) {
  switch (cmd) {
    case 'help':
      print(`Available system commands:
  projects   - Output full repository directory
  skills     - Output frontend competency tree
  brew       - Jump to DUN Specialty Coffee Lab
  sandbox    - Jump to Live Token Sandbox
  resume     - View curriculum vitae summary
  matrix     - Toggle visual matrix rain
  contact    - Open contact dialog
  whoami     - Display visitor authorization credentials
  clear      - Flush terminal history`);
      break;
    case 'projects':
      print(`Production Repositories:
  - Qreet CMS (Next.js 15, Prisma, PostgreSQL, TipTap) -> Live on Vercel
  - DUN Coffee Roastery (Extraction engine, Espresso UI #020101)
  - WebDev Master Hub (Interactive multi-track learning suite)
  - Barg Reader (RTL typography engine, PWA, Android APK)
  - Parsa Sports (Reactive athletic e-commerce storefront)
  - HabitForge (Productivity heatmap PWA)
  - Nova UI (High-density SaaS design system)`);
      break;
    case 'skills':
      print(`Frontend Architecture Stack:
  - Frameworks: React 19, Next.js 15 (App Router, Server Actions)
  - Languages: TypeScript, JavaScript (ES6+), HTML5 Semantic
  - Styles: Tailwind CSS v4, CSS Custom Properties, Bento Grids
  - CMS: WordPress Themes, Elementor Custom Widgets, Headless CMS
  - Infrastructure: Git/GitHub CI/CD, Vercel Edge Serverless`);
      break;
    case 'resume':
      print(`Erfan Mehdi Sadeghi — Front-End Developer & UI/UX Architect.
5+ years experience. Specializing in high-performance web applications, strict dark mode architectures, and resilient frontends.`);
      break;
    case 'matrix':
      if (window.Sound) Sound.playSuccess();
      print(`<span style="color: #10b981;">01000101 01010010 01000110 01000001 01001110 00100000 01001111 01010011</span><br><span style="color: #34d399;">[CONNECTED TO MAINFRAME] Systems nominal. Matrix Rain Active.</span>`, true);
      break;
    case 'whoami':
      print(`visitor@guest-session (authenticated via browser WebAPI)`);
      break;
    case 'sandbox':
      document.getElementById('sandbox')?.scrollIntoView({ behavior: 'smooth' });
      print(`Jumping to Component Sandbox...`);
      break;
    case 'brew':
      document.getElementById('brew-lab-section')?.scrollIntoView({ behavior: 'smooth' });
      print(`Jumping to DUN Brew Lab...`);
      break;
    case 'contact':
      openContactModal();
      print(`Opening contact dialog...`);
      break;
    case 'clear':
      document.getElementById('termOutput').innerHTML = '';
      break;
    default:
      print(`Command not recognized: '${cmd}'. Type 'help' for command manual.`);
  }
}

// 13. Project Architecture Modal
function openProjectModal(id) {
  const p = PROJECTS_DATA.find(x => x.id === id);
  if (!p) return;
  const overlay = document.getElementById('projectModalOverlay');
  const content = document.getElementById('projectModalBody');
  if (!overlay || !content) return;

  content.innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
      <span class="card-badge mono" style="color: ${p.color}; border-color: ${p.color};">${p.badge}</span>
      <span class="mono" style="font-size: 12px; color: var(--text-dim);">${p.category.toUpperCase()} // ${p.year || '2026'}</span>
    </div>
    <h2 style="font-size: 24px; font-weight: 800; margin-bottom: 8px;">${p.title}</h2>
    <p class="mono" style="color: #a5b4fc; font-size: 13px; margin-bottom: 20px;">${p.tagline}</p>
    
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 18px; margin-bottom: 20px;">
      <h4 class="mono" style="font-size: 12px; color: var(--text-muted); margin-bottom: 10px; text-transform: uppercase;">Technical Architecture</h4>
      <p style="font-size: 13px; color: var(--text-main); line-height: 1.6; margin-bottom: 14px;">${p.description}</p>
      <ul style="list-style: none; padding: 0;">
        ${p.highlights.map(h => `<li style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;"><i class="fa-solid fa-check" style="color: #10b981; margin-right: 8px;"></i>${h}</li>`).join('')}
      </ul>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 24px;">
      ${p.metrics.map(m => `
        <div style="background: var(--bg-base); border: 1px solid var(--border-subtle); padding: 10px; border-radius: 8px; text-align: center;">
          <div class="mono" style="font-size: 11px; color: var(--text-dim);">${m.label}</div>
          <div class="mono" style="font-size: 12.5px; font-weight: 700; color: #f1f5f9; margin-top: 4px;">${m.value}</div>
        </div>
      `).join('')}
    </div>

    <div style="display: flex; gap: 12px; justify-content: flex-end;">
      <button class="btn-primary" onclick="closeProjectModal(); openLiveViewModal('${p.liveUrl}', '${p.title.replace(/'/g, "\\\\'")}');">
        <i class="fa-solid fa-play"></i> Launch Inside Modal
      </button>
      <a href="${p.liveUrl}" ${p.liveUrl.startsWith('http') || p.liveUrl.includes('demos/') ? 'target="_blank"' : ''} class="btn-outline" onclick="if(window.Sound)Sound.playClick();">
        <i class="fa-solid fa-arrow-up-right-from-square"></i> Open In New Tab
      </a>
    </div>
  `;

  overlay.classList.add('open');
}

function closeProjectModal() {
  document.getElementById('projectModalOverlay')?.classList.remove('open');
  if (window.Sound) Sound.playClick();
}

// 13.1 Instant In-App Live Modal Preview
function openLiveViewModal(url, title) {
  let modal = document.getElementById('liveViewModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'liveViewModal';
    modal.className = 'modal-overlay';
    modal.innerHTML = `
      <div class="modal-box modal-live-view">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-subtle); padding-bottom: 14px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span class="status-dot"></span>
            <span id="liveViewTitle" class="mono" style="font-size: 13.5px; font-weight: 700; color: #fff;">Live Preview</span>
          </div>
          <div style="display: flex; align-items: center; gap: 12px;">
            <a id="liveViewNewTabBtn" href="#" target="_blank" class="btn-outline mono" style="font-size: 12px; padding: 5px 12px;">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> Open in New Tab
            </a>
            <button class="btn-icon" style="width: 32px; height: 32px;" onclick="closeLiveViewModal();">&times;</button>
          </div>
        </div>
        <div class="live-frame-container">
          <iframe id="liveViewIframe" src="" loading="lazy"></iframe>
        </div>
      </div>
    `;
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeLiveViewModal();
    });
    document.body.appendChild(modal);
  }

  document.getElementById('liveViewTitle').textContent = 'Live Production App — ' + title;
  document.getElementById('liveViewNewTabBtn').href = url;
  const iframe = document.getElementById('liveViewIframe');
  iframe.src = url;

  modal.classList.add('open');
  if (window.Sound) Sound.playSuccess();
}

function closeLiveViewModal() {
  const modal = document.getElementById('liveViewModal');
  if (modal) {
    modal.classList.remove('open');
    const iframe = document.getElementById('liveViewIframe');
    if (iframe) iframe.src = '';
  }
  if (window.Sound) Sound.playClick();
}

// 14. Contact Modal
function initContactModal() {
  const overlay = document.getElementById('contactModalOverlay');
  const btn = document.getElementById('openContactBtn');
  const close = document.getElementById('closeContactBtn');
  if (btn) btn.addEventListener('click', () => openContactModal());
  if (close) close.addEventListener('click', () => closeContactModal());
}

function openContactModal() {
  document.getElementById('contactModalOverlay')?.classList.add('open');
  if (window.Sound) Sound.playClick();
}

function closeContactModal() {
  document.getElementById('contactModalOverlay')?.classList.remove('open');
  if (window.Sound) Sound.playClick();
}

// 15. Utilities
function copyText(text, label = 'Copied to clipboard') {
  navigator.clipboard.writeText(text).then(() => {
    if (window.Sound) Sound.playSuccess();
    showToast(label);
  });
}

function showToast(msg) {
  let toast = document.getElementById('toastMsg');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toastMsg';
    toast.className = 'toast-msg mono';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2500);
}
