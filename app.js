// Erfan Portfolio Core Application Logic
document.addEventListener('DOMContentLoaded', () => {
  initLiveClock();
  renderProjects('all');
  initFilterTabs();
  initSearch();
  initBrewLab();
  initTerminal();
  initSoundToggle();
  initContactModal();
});

// 1. Live Clock & System Status
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

// 2. Sound Toggle
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

// 3. Render Projects
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
        <i class="fa-solid fa-folder-open" style="font-size: 32px; margin-bottom: 12px; display: block;"></i>
        No projects match your filter. Try another keyword.
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(p => `
    <article class="project-card" style="--card-accent: ${p.color};" onmouseenter="Sound.playHover()">
      <div>
        <div class="card-top">
          <span class="card-badge mono">${p.badge}</span>
          <span class="mono" style="font-size: 11px; color: var(--text-dim);">${p.category.toUpperCase()}</span>
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
          <button class="btn-outline" style="font-size: 12px; padding: 6px 14px;" onclick="openProjectModal('${p.id}'); Sound.playClick();">
            <i class="fa-solid fa-circle-info"></i> Spec
          </button>
          ${p.liveUrl && p.liveUrl !== '#' ? `
            <a href="${p.liveUrl}" target="_blank" class="btn-primary" style="font-size: 12px; padding: 6px 14px;" onclick="Sound.playClick();">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo
            </a>
          ` : `
            <a href="${p.githubUrl}" target="_blank" class="btn-outline" style="font-size: 12px; padding: 6px 14px;" onclick="Sound.playClick();">
              <i class="fa-brands fa-github"></i> Repository
            </a>
          `}
        </div>
      </div>
    </article>
  `).join('');
}

// 4. Filter Tabs & Search
function initFilterTabs() {
  const pills = document.querySelectorAll('.filter-pill');
  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      Sound.playClick();
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

// 5. Interactive Brew Lab Engine
function initBrewLab() {
  const doseSlider = document.getElementById('brewDose');
  const ratioSlider = document.getElementById('brewRatio');
  const methodSelect = document.getElementById('brewMethod');

  if (!doseSlider || !ratioSlider || !methodSelect) return;

  const calculate = () => {
    const dose = parseFloat(doseSlider.value);
    const ratio = parseFloat(ratioSlider.value);
    const method = methodSelect.value;

    const water = Math.round(dose * ratio);
    
    // Pour stage calculation
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

  doseSlider.addEventListener('input', () => { calculate(); Sound.playHover(); });
  ratioSlider.addEventListener('input', () => { calculate(); Sound.playHover(); });
  methodSelect.addEventListener('change', () => { calculate(); Sound.playClick(); });
  calculate();
}

// 6. Interactive Terminal
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
      Sound.playClick();

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
      print(`Available commands:
  projects   - List all production projects
  skills     - View frontend tech stack & tools
  about      - Display developer biography & philosophy
  brew       - Jump to interactive DUN Brew Lab
  contact    - Launch contact desk
  clear      - Clear terminal screen
  sudo hire  - Fast-track direct inquiry`);
      break;
    case 'projects':
      print(`Core Projects:
  - Qreet CMS (Next.js 15, Prisma, PostgreSQL, TipTap) -> Live on Vercel
  - DUN Coffee & Brew Lab (Extraction engine, Espresso UI #020101)
  - WebDev Master Hub (Interactive multi-track learning suite)
  - Barg Reader (RTL typography engine, PWA, Android APK)
  - Parsa Sports (Reactive athletic e-commerce storefront)
  - HabitForge (Productivity heatmap PWA)
  - Nova UI (High-density SaaS design system)`);
      break;
    case 'skills':
      print(`Frontend Pillar:
  - HTML5 / CSS3 / JavaScript ES6+ / TypeScript
  - React 19 / Next.js 15 (App Router, Server Actions)
  - Tailwind CSS / CSS Modules / Custom Properties Architecture
  - WordPress / Elementor Custom PHP Widgets
  - RESTful APIs / WebSocket / LocalStorage Persistence
  - Git / GitHub CI/CD Actions / Vercel Edge Deployments`);
      break;
    case 'about':
      print(`Erfan Mehdi Sadeghi — Front-End Developer & UI/UX Architect.
Specializing in high-performance web applications, strict dark mode architectures,
interactive math & canvas widgets, and clean typography.`);
      break;
    case 'brew':
      document.getElementById('brew-lab-section')?.scrollIntoView({ behavior: 'smooth' });
      print(`Scrolling to DUN Brew Lab...`);
      break;
    case 'contact':
      openContactModal();
      print(`Opening contact desk modal...`);
      break;
    case 'clear':
      document.getElementById('termOutput').innerHTML = '';
      break;
    case 'sudo hire':
    case 'hire':
      Sound.playSuccess();
      print(`[SUCCESS] Priority booking requested. Reach out via Telegram @erfan_sadeghi or erfandarrudi527@gmail.com`);
      break;
    default:
      print(`Command not recognized: '${cmd}'. Type 'help' for available commands.`);
  }
}

// 7. Modals & Spec Viewer
function openProjectModal(id) {
  const p = PROJECTS_DATA.find(x => x.id === id);
  if (!p) return;
  const overlay = document.getElementById('projectModalOverlay');
  const content = document.getElementById('projectModalBody');
  if (!overlay || !content) return;

  content.innerHTML = `
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
      <span class="card-badge mono" style="color: ${p.color}; border-color: ${p.color};">${p.badge}</span>
      <span class="mono" style="font-size: 12px; color: var(--text-dim);">${p.category.toUpperCase()}</span>
    </div>
    <h2 style="font-size: 24px; font-weight: 800; margin-bottom: 8px;">${p.title}</h2>
    <p class="mono" style="color: #a5b4fc; font-size: 13px; margin-bottom: 20px;">${p.tagline}</p>
    
    <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 16px; margin-bottom: 20px;">
      <h4 class="mono" style="font-size: 12px; color: var(--text-muted); margin-bottom: 10px; text-transform: uppercase;">Architecture & Execution</h4>
      <p style="font-size: 13px; color: var(--text-main); line-height: 1.6; margin-bottom: 14px;">${p.description}</p>
      <ul style="list-style: none; padding: 0;">
        ${p.highlights.map(h => `<li style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;"><i class="fa-solid fa-check" style="color: #10b981; margin-right: 8px;"></i>${h}</li>`).join('')}
      </ul>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 24px;">
      ${p.metrics.map(m => `
        <div style="background: var(--bg-base); border: 1px solid var(--border-subtle); padding: 10px; border-radius: 6px; text-align: center;">
          <div class="mono" style="font-size: 11px; color: var(--text-dim);">${m.label}</div>
          <div class="mono" style="font-size: 12px; font-weight: 700; color: #f1f5f9; margin-top: 4px;">${m.value}</div>
        </div>
      `).join('')}
    </div>

    <div style="display: flex; gap: 12px; justify-content: flex-end;">
      ${p.liveUrl && p.liveUrl !== '#' ? `
        <a href="${p.liveUrl}" target="_blank" class="btn-primary" onclick="Sound.playClick();">
          <i class="fa-solid fa-arrow-up-right-from-square"></i> Open Live Deployment
        </a>
      ` : ''}
      <a href="${p.githubUrl}" target="_blank" class="btn-outline" onclick="Sound.playClick();">
        <i class="fa-brands fa-github"></i> Source Repository
      </a>
    </div>
  `;

  overlay.classList.add('open');
}

function closeProjectModal() {
  document.getElementById('projectModalOverlay')?.classList.remove('open');
  Sound.playClick();
}

function initContactModal() {
  const overlay = document.getElementById('contactModalOverlay');
  const btn = document.getElementById('openContactBtn');
  const close = document.getElementById('closeContactBtn');
  if (btn) btn.addEventListener('click', () => openContactModal());
  if (close) close.addEventListener('click', () => closeContactModal());
}

function openContactModal() {
  document.getElementById('contactModalOverlay')?.classList.add('open');
  Sound.playClick();
}

function closeContactModal() {
  document.getElementById('contactModalOverlay')?.classList.remove('open');
  Sound.playClick();
}

// 8. Clipboard & Toast
function copyText(text, label = 'Copied to clipboard') {
  navigator.clipboard.writeText(text).then(() => {
    Sound.playSuccess();
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
  setTimeout(() => {
    toast.classList.remove('show');
  }, 2400);
}
