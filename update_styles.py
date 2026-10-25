import os

target_dir = 'C:/Users/erfan/Desktop/erfan-pro-portfolio'

# 1. ENHANCED styles.css
css_content = '''/* ERFAN.DEV LUXURY DESIGN TOKENS */
:root {
  --bg-base: #05070B;
  --bg-surface: #090D16;
  --bg-card: #0E1422;
  --bg-card-hover: #141C30;
  --border-subtle: rgba(255, 255, 255, 0.07);
  --border-active: rgba(99, 102, 241, 0.45);
  --accent: #6366F1;
  --accent-hover: #4F46E5;
  --accent-glow: rgba(99, 102, 241, 0.3);
  --cyan: #06B6D4;
  --cyan-glow: rgba(6, 182, 212, 0.25);
  --amber: #F59E0B;
  --emerald: #10B981;
  --rose: #F43F5E;
  --purple: #A855F7;
  --text-main: #F8FAFC;
  --text-muted: #94A3B8;
  --text-dim: #64748B;
  --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  color-scheme: dark;
}

body {
  background-color: var(--bg-base);
  color: var(--text-main);
  font-family: var(--font-sans);
  line-height: 1.6;
  overflow-x: hidden;
  min-height: 100vh;
  position: relative;
}

/* Background Canvas */
#bgCanvas {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
  opacity: 0.65;
}

/* Custom Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #334155; }

.mono { font-family: var(--font-mono); }
.glow-text { text-shadow: 0 0 20px rgba(99, 102, 241, 0.6); }

.container {
  max-width: 1260px;
  margin: 0 auto;
  padding: 0 24px;
}

/* HEADER & NAVBAR */
header.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  background: rgba(5, 7, 11, 0.85);
  border-bottom: 1px solid var(--border-subtle);
}

.nav-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

.brand-badge {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--text-main);
}

.brand-icon {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: linear-gradient(135deg, #6366F1 0%, #3B82F6 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 15px;
  box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 22px;
}

.nav-link {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  transition: color 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.nav-link:hover, .nav-link.active {
  color: var(--text-main);
}

.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 14px;
  border-radius: 9999px;
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.25);
  font-size: 12px;
  color: #34d399;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 10px #10b981;
  animation: pulse-dot 2s infinite ease-in-out;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.cmd-trigger-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  color: var(--text-muted);
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cmd-trigger-btn:hover {
  color: var(--text-main);
  border-color: var(--border-active);
  background: var(--bg-card-hover);
}

.btn-icon {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  width: 38px;
  height: 38px;
  border-radius: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.btn-icon:hover {
  color: var(--text-main);
  border-color: var(--border-active);
  background: var(--bg-card);
}

.btn-primary {
  background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
  color: #ffffff;
  padding: 9px 20px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  transition: all 0.2s ease;
  box-shadow: 0 0 25px rgba(99, 102, 241, 0.35);
  cursor: pointer;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 35px rgba(99, 102, 241, 0.55);
}

.btn-outline {
  background: var(--bg-card);
  color: var(--text-main);
  padding: 9px 20px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid var(--border-subtle);
  transition: all 0.2s ease;
  cursor: pointer;
}

.btn-outline:hover {
  border-color: var(--border-active);
  background: var(--bg-card-hover);
}

/* HERO SECTION */
.hero-section {
  padding: 85px 0 65px;
}

.hero-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 22px;
}

.badge-version {
  padding: 4px 12px;
  background: rgba(99, 102, 241, 0.12);
  border: 1px solid rgba(99, 102, 241, 0.3);
  color: #a5b4fc;
  font-size: 11px;
  font-weight: 600;
  border-radius: 6px;
  letter-spacing: 0.08em;
}

.hero-title {
  font-size: clamp(40px, 6vw, 72px);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.08;
  margin-bottom: 20px;
}

.gradient-text {
  background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 45%, #818cf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-sub {
  font-size: clamp(16px, 2vw, 20px);
  color: var(--text-muted);
  max-width: 720px;
  margin-bottom: 36px;
}

.hero-sub strong {
  color: #ffffff;
  font-weight: 600;
}

.hero-cta {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: 50px;
}

/* STATS MATRIX */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 16px;
  margin-bottom: 70px;
}

.stat-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: 14px;
  padding: 20px 24px;
  transition: all 0.25s ease;
  position: relative;
  overflow: hidden;
}

.stat-card:hover {
  border-color: var(--border-active);
  background: var(--bg-card);
  transform: translateY(-2px);
}

.stat-value {
  font-size: 34px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1;
  margin-bottom: 6px;
  font-family: var(--font-mono);
}

.stat-label {
  font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* SECTION HEADERS */
.section-header {
  margin-bottom: 36px;
}

.section-tag {
  font-size: 12px;
  font-weight: 700;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 8px;
  display: block;
}

.section-title {
  font-size: clamp(28px, 4vw, 38px);
  font-weight: 800;
  letter-spacing: -0.02em;
}

/* FILTER BAR */
.filter-bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 30px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 12px 18px;
}

.filter-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.filter-pill {
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-muted);
  padding: 7px 16px;
  font-size: 12px;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-pill:hover {
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.05);
}

.filter-pill.active {
  background: var(--accent);
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.15);
  box-shadow: 0 0 15px rgba(99, 102, 241, 0.35);
}

.search-box {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 7px 14px;
  width: 260px;
}

.search-box input {
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-main);
  font-size: 13px;
  font-family: inherit;
  width: 100%;
}

/* PROJECTS BENTO GRID */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(370px, 1fr));
  gap: 26px;
  margin-bottom: 85px;
}

.project-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: 18px;
  padding: 26px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--card-accent, #6366F1), transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.project-card:hover {
  border-color: var(--border-active);
  background: var(--bg-card);
  transform: translateY(-5px);
  box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.7);
}

.project-card:hover::before { opacity: 1; }

.card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.card-badge {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 4px 10px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--text-muted);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.card-title {
  font-size: 21px;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 8px;
}

.card-tagline {
  font-size: 13px;
  font-weight: 500;
  color: #a5b4fc;
  margin-bottom: 12px;
}

.card-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 22px;
  flex-grow: 1;
}

.card-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 20px;
}

.stack-tag {
  font-size: 11px;
  font-family: var(--font-mono);
  background: rgba(255, 255, 255, 0.035);
  border: 1px solid rgba(255, 255, 255, 0.07);
  color: #cbd5e1;
  padding: 3px 9px;
  border-radius: 5px;
}

.card-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

/* INTERACTIVE COMPONENT SANDBOX */
.sandbox-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: 18px;
  padding: 32px;
  margin-bottom: 85px;
}

.sandbox-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-top: 24px;
}

@media (max-width: 900px) {
  .sandbox-grid { grid-template-columns: 1fr; }
}

.sandbox-preview-stage {
  background: #05070a;
  border: 1px solid var(--border-subtle);
  border-radius: 14px;
  min-height: 260px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 30px;
  position: relative;
  overflow: hidden;
}

.sandbox-controls {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.sandbox-control-item label {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  font-family: var(--font-mono);
  color: var(--text-muted);
  margin-bottom: 6px;
}

.sandbox-code-box {
  background: #06080d;
  border: 1px solid var(--border-subtle);
  border-radius: 10px;
  padding: 14px;
  font-family: var(--font-mono);
  font-size: 12px;
  color: #38bdf8;
  max-height: 120px;
  overflow-y: auto;
}

/* INTERACTIVE BREW LAB WITH ANIMATED DRIPPER */
.lab-card {
  background: #020101;
  border: 1px solid #332219;
  border-radius: 18px;
  padding: 34px;
  margin-bottom: 85px;
  position: relative;
  box-shadow: 0 0 60px rgba(217, 119, 6, 0.08);
}

.lab-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 36px;
  margin-top: 24px;
}

@media (max-width: 860px) {
  .lab-grid { grid-template-columns: 1fr; }
}

.lab-control-group {
  margin-bottom: 20px;
}

.lab-control-group label {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  font-weight: 600;
  color: #d97706;
  margin-bottom: 8px;
  font-family: var(--font-mono);
}

.lab-slider {
  width: 100%;
  accent-color: #d97706;
  cursor: pointer;
}

.lab-results {
  background: #090503;
  border: 1px solid #2d180f;
  border-radius: 14px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.lab-result-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.lab-result-val {
  font-family: var(--font-mono);
  font-size: 19px;
  font-weight: 700;
  color: #f59e0b;
}

/* INTERACTIVE TERMINAL */
.terminal-card {
  background: #06080e;
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 85px;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.65);
}

.terminal-header {
  background: #0c101a;
  padding: 12px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-subtle);
}

.terminal-dots { display: flex; gap: 7px; }
.tdot { width: 11px; height: 11px; border-radius: 50%; }
.tdot-red { background: #ef4444; }
.tdot-yellow { background: #f59e0b; }
.tdot-green { background: #10b981; }

.terminal-body {
  padding: 22px;
  font-family: var(--font-mono);
  font-size: 13.5px;
  min-height: 240px;
  max-height: 400px;
  overflow-y: auto;
  color: #cbd5e1;
}

.term-line { margin-bottom: 7px; line-height: 1.5; }
.term-prompt { color: #38bdf8; font-weight: 700; }

.terminal-input-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 10px;
}

.term-input {
  background: transparent;
  border: none;
  outline: none;
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 13.5px;
  width: 100%;
}

/* SPOTLIGHT COMMAND PALETTE (CMD+K) */
.cmd-palette-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(12px);
  z-index: 150;
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding-top: 14vh;
}

.cmd-palette-overlay.open { display: flex; }

.cmd-palette-box {
  background: #090d16;
  border: 1px solid var(--border-active);
  border-radius: 16px;
  max-width: 620px;
  width: 90%;
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.9);
  overflow: hidden;
  animation: cmdPop 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes cmdPop {
  from { opacity: 0; transform: scale(0.96) translateY(-10px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

.cmd-search-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-subtle);
  background: #0c121e;
}

.cmd-search-header input {
  background: transparent;
  border: none;
  outline: none;
  color: #fff;
  font-size: 15px;
  font-family: inherit;
  width: 100%;
}

.cmd-list {
  max-height: 340px;
  overflow-y: auto;
  padding: 10px;
}

.cmd-group-title {
  font-size: 11px;
  font-family: var(--font-mono);
  color: var(--text-dim);
  padding: 8px 12px 4px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.cmd-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
  color: var(--text-muted);
  font-size: 13px;
  transition: all 0.15s ease;
}

.cmd-item:hover, .cmd-item.selected {
  background: rgba(99, 102, 241, 0.15);
  color: #ffffff;
}

/* MODALS & OVERLAYS */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  z-index: 100;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-overlay.open { display: flex; }

.modal-box {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 18px;
  max-width: 600px;
  width: 100%;
  padding: 34px;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.85);
  position: relative;
}

.modal-close {
  position: absolute;
  top: 18px;
  right: 20px;
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-size: 20px;
  cursor: pointer;
}

.toast-msg {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #111827;
  border: 1px solid var(--accent);
  color: #ffffff;
  padding: 11px 20px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
  transform: translateY(100px);
  opacity: 0;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 200;
}

.toast-msg.show { transform: translateY(0); opacity: 1; }

footer {
  border-top: 1px solid var(--border-subtle);
  padding: 45px 0;
  color: var(--text-dim);
  font-size: 12px;
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}
'''

with open(os.path.join(target_dir, 'styles.css'), 'w', encoding='utf-8') as f:
    f.write(css_content)

print('styles.css successfully updated.')
