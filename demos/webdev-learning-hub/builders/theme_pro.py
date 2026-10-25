# -*- coding: utf-8 -*-
"""
Luxury Obsidian & Precision Dark UI Theme for ERFAN.DEV Learning OS.
Crafted to Linear, Vercel & Raycast design precision:
- Subtle micro-grid background with zero cheesy gradients.
- Micro-hairline borders (rgba(255,255,255,0.07)).
- Crisp tactile buttons with native Web Audio click feedback.
- Bookmark system (⭐ نشان‌گذاری برای مرور).
- Live execution timer in JS sandbox (⚡ اجرا در 1.2ms).
- Quick floating Jump Bar & Keyboard shortcuts (J/K/Ctrl+K).
"""

PRO_CSS = """
@font-face {
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Regular.ttf') format('truetype');
  font-weight: 400;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Bold.ttf') format('truetype');
  font-weight: 700;
}
@font-face {
  font-family: 'IRANYekan';
  src: url('../fonts/IRANYekanXFaNum-Black.ttf') format('truetype');
  font-weight: 900;
}

:root {
  --bg-canvas: #04060a;
  --bg-sidebar: #080c14;
  --bg-surface: #0c121e;
  --bg-card: #0f1726;
  --bg-subcard: rgba(2, 6, 23, 0.6);
  --bg-code: #010307;
  --border-subtle: rgba(255, 255, 255, 0.06);
  --border-medium: rgba(255, 255, 255, 0.12);
  --border-active: rgba(56, 189, 248, 0.45);
  --text-main: #f8fafc;
  --text-dim: #94a3b8;
  --text-mute: #64748b;
  --sky: #38bdf8;
  --emerald: #10b981;
  --amber: #f59e0b;
  --rose: #f43f5e;
  --purple: #a855f7;
  --indigo: #6366f1;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
}

body {
  font-family: 'IRANYekan', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif;
  background-color: var(--bg-canvas);
  background-image: 
    linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
  background-size: 32px 32px;
  color: var(--text-main);
  direction: rtl;
  line-height: 1.8;
  -webkit-font-smoothing: antialiased;
}

/* Master Top Navigation Bar */
.top-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(8, 12, 20, 0.9);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 8px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.6);
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--text-main);
}
.brand-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.02));
  border: 1px solid var(--border-medium);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: #fff;
}
.brand-title {
  font-size: 15px;
  font-weight: 900;
  letter-spacing: -0.3px;
}
.brand-badge {
  font-size: 10.5px;
  font-weight: 800;
  background: rgba(56, 189, 248, 0.1);
  color: var(--sky);
  padding: 2px 8px;
  border-radius: 6px;
  border: 1px solid rgba(56, 189, 248, 0.25);
}

.track-tabs {
  display: flex;
  gap: 4px;
  background: rgba(2, 6, 23, 0.8);
  padding: 4px;
  border-radius: 10px;
  border: 1px solid var(--border-subtle);
  flex-wrap: wrap;
}
.track-tab {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 11px;
  border-radius: 7px;
  font-size: 12px;
  font-weight: 700;
  text-decoration: none;
  color: var(--text-dim);
  transition: all 0.15s ease;
  white-space: nowrap;
}
.track-tab:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.05);
}
.track-tab.active {
  background: var(--bg-card);
  color: #fff;
  border: 1px solid var(--border-medium);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.cmd-btn {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-subtle);
  color: var(--text-dim);
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.15s;
}
.cmd-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--border-medium);
  color: #fff;
}
.cmd-kbd {
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--text-mute);
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 10px;
  font-family: monospace;
}

.btn-icon {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-subtle);
  color: var(--text-dim);
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 12.5px;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s;
}
.btn-icon:hover {
  background: rgba(255, 255, 255, 0.09);
  color: #fff;
  transform: translateY(-1px);
}
.btn-primary-glow {
  background: linear-gradient(135deg, #38bdf8 0%, #0284c7 100%);
  color: #020617 !important;
  font-weight: 800;
  border: none;
  box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
}
.btn-primary-glow:hover {
  background: linear-gradient(135deg, #7dd3fc 0%, #38bdf8 100%);
  box-shadow: 0 6px 18px rgba(56, 189, 248, 0.5);
}

/* Master Layout */
.app-layout {
  display: flex;
  max-width: 1480px;
  margin: 0 auto;
  position: relative;
}

.sidebar {
  width: 340px;
  flex-shrink: 0;
  position: sticky;
  top: 53px;
  height: calc(100vh - 53px);
  border-left: 1px solid var(--border-subtle);
  background: var(--bg-sidebar);
  overflow-y: auto;
  padding: 16px 14px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.sidebar::-webkit-scrollbar { width: 4px; }
.sidebar::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }

.main-content {
  flex: 1;
  min-width: 0;
  padding: 28px 36px 100px;
}

/* Progress Stats Card in Sidebar */
.progress-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 14px 16px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.3);
}
.progress-meta {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  font-weight: 800;
  margin-bottom: 8px;
}
.progress-bar-bg {
  height: 6px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 99px;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #10b981, #38bdf8);
  border-radius: 99px;
  transition: width 0.3s ease;
}

.sidebar-search {
  width: 100%;
  background: var(--bg-code);
  border: 1px solid var(--border-subtle);
  color: #fff;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 12.5px;
  font-family: inherit;
  outline: none;
  transition: border-color 0.15s;
}
.sidebar-search:focus {
  border-color: var(--sky);
}

.level-filters {
  display: flex;
  gap: 4px;
}
.l-btn {
  flex: 1;
  background: transparent;
  border: 1px solid var(--border-subtle);
  color: var(--text-mute);
  padding: 4px 6px;
  border-radius: 6px;
  font-size: 11px;
  font-family: inherit;
  cursor: pointer;
  transition: 0.15s;
}
.l-btn.active, .l-btn:hover {
  background: rgba(255, 255, 255, 0.06);
  color: #fff;
  border-color: var(--border-medium);
}

/* Sidebar Tree Items */
.tree-group-divider {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 10px 4px 10px;
  margin-top: 8px;
  font-size: 11px;
  font-weight: 700;
  color: var(--text-mute);
  letter-spacing: 0.5px;
  border-top: 1px dashed rgba(255, 255, 255, 0.08);
}
.tree-group-divider:first-child {
  border-top: none;
  margin-top: 0;
}
.tree-group-badge {
  font-size: 10px;
  padding: 1px 6px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-dim);
}

.tree-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.tree-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 13px;
  color: var(--text-dim);
  text-decoration: none;
  transition: all 0.15s;
}
.tree-item:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #fff;
}
.tree-item.active-spy {
  background: rgba(56, 189, 248, 0.15);
  color: var(--sky);
  border: 1px solid rgba(56, 189, 248, 0.35);
  font-weight: 700;
}
.tree-badge {
  font-size: 10.5px;
  color: var(--text-mute);
  background: rgba(255, 255, 255, 0.04);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--border-subtle);
  flex-shrink: 0;
}
.tree-item.is-completed .tree-title {
  text-decoration: line-through;
  opacity: 0.55;
}
.check-indicator {
  width: 15px;
  height: 15px;
  border-radius: 4px;
  border: 1px solid #334155;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 9.5px;
  flex-shrink: 0;
  cursor: pointer;
  transition: all 0.15s;
}
.check-indicator.checked {
  background: var(--emerald);
  border-color: var(--emerald);
  color: #022c22;
  font-weight: 900;
}

/* Header Banner */
.topic-page-header {
  margin-bottom: 30px;
  padding-bottom: 22px;
  border-bottom: 1px solid var(--border-subtle);
}
.track-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 99px;
  font-size: 11.5px;
  font-weight: 800;
  margin-bottom: 10px;
  border: 1px solid;
}
.topic-page-title {
  font-size: 30px;
  font-weight: 900;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}
.topic-page-desc {
  font-size: 14.5px;
  color: var(--text-dim);
  max-width: 820px;
  line-height: 1.8;
}

/* High Precision Topic Card */
.topic-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 18px;
  margin-bottom: 36px;
  overflow: hidden;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
  scroll-margin-top: 85px;
  position: relative;
}
.topic-card:target {
  border-color: #38bdf8;
  box-shadow: 0 0 35px rgba(56, 189, 248, 0.2), 0 16px 36px -12px rgba(0, 0, 0, 0.8);
}
.topic-card:hover {
  border-color: var(--border-active);
  box-shadow: 0 16px 36px -12px rgba(0, 0, 0, 0.8), 0 0 25px -5px rgba(56, 189, 248, 0.08);
  transform: translateY(-2px);
}
.topic-card.completed-card {
  border-color: rgba(16, 185, 129, 0.4);
}
.topic-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.5), transparent);
  opacity: 0;
  transition: opacity 0.2s;
}
.topic-card:hover::before {
  opacity: 1;
}

.card-topbar {
  padding: 16px 22px;
  background: rgba(255, 255, 255, 0.015);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}
.card-title-group {
  display: flex;
  align-items: center;
  gap: 10px;
}
.topic-num-badge {
  background: rgba(255, 255, 255, 0.06);
  color: var(--text-main);
  font-size: 12px;
  font-weight: 900;
  padding: 3px 10px;
  border-radius: 7px;
  border: 1px solid var(--border-subtle);
}
.topic-h2 {
  font-size: 19px;
  font-weight: 900;
  color: #fff;
}
.card-meta-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}
.lvl-chip {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 99px;
  border: 1px solid;
}
.bookmark-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-subtle);
  color: var(--text-dim);
  padding: 5px 10px;
  border-radius: 7px;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.15s;
}
.bookmark-btn.active {
  background: rgba(245, 158, 11, 0.15);
  color: var(--amber);
  border-color: rgba(245, 158, 11, 0.4);
}
.complete-toggle-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-subtle);
  color: var(--text-dim);
  padding: 5px 12px;
  border-radius: 7px;
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: 0.15s;
}
.complete-toggle-btn.is-active {
  background: rgba(16, 185, 129, 0.15);
  color: var(--emerald);
  border-color: var(--emerald);
}

.card-body-open {
  padding: 22px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

/* Layer 1: Concept Boxes */
.concept-block {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.analogy-subbox {
  background: rgba(245, 158, 11, 0.06);
  border-right: 3px solid var(--amber);
  border-radius: 8px;
  padding: 12px 16px;
}
.analogy-subbox .subbox-label {
  font-size: 12px;
  font-weight: 800;
  color: #fbbf24;
  margin-bottom: 2px;
}
.analogy-text {
  font-size: 14px;
  color: #fef3c7;
  line-height: 1.8;
}

.explain-subbox {
  background: rgba(56, 189, 248, 0.05);
  border-right: 3px solid var(--sky);
  border-radius: 8px;
  padding: 12px 16px;
}
.explain-subbox .subbox-label {
  font-size: 12px;
  font-weight: 800;
  color: var(--sky);
  margin-bottom: 2px;
}
.explain-text {
  font-size: 14px;
  color: #cbd5e1;
  line-height: 1.8;
}

.block-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13.5px;
  font-weight: 900;
  margin-bottom: 3px;
}
.title-blue { color: var(--sky); }
.title-green { color: #34d399; }
.title-amber { color: #fbbf24; }

/* Code Box */
.code-playground-block {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.code-box {
  background: var(--bg-code);
  border: 1px solid var(--border-subtle);
  border-radius: 10px;
  overflow: hidden;
}
.code-bar {
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--border-subtle);
  padding: 7px 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.code-lang-tag {
  font-family: monospace;
  font-size: 10.5px;
  color: var(--text-mute);
}
.code-action-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-dim);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11.5px;
  font-family: inherit;
  cursor: pointer;
  transition: 0.15s;
}
.code-action-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}
.code-box pre {
  padding: 16px 20px;
  overflow-x: auto;
  direction: ltr;
  text-align: left;
}
.code-box code {
  font-family: 'Fira Code', 'Courier New', monospace;
  font-size: 13px;
  line-height: 1.65;
  color: #93c5fd;
}

/* Interactive Sandbox Container */
.interactive-sandbox-block {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.sandbox-card {
  background: #070b14;
  border: 1px solid rgba(56, 189, 248, 0.22);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px -8px rgba(0, 0, 0, 0.6);
}
.sandbox-topbar {
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--border-subtle);
  padding: 7px 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.sandbox-dots {
  display: flex;
  align-items: center;
  gap: 5px;
}
.sandbox-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  display: inline-block;
}
.sandbox-title-tag {
  font-size: 10.5px;
  color: var(--text-mute);
  margin-right: 6px;
  font-family: monospace;
}
.sandbox-badge-active {
  font-size: 10.5px;
  color: var(--sky);
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.sandbox-body {
  padding: 18px 20px;
  background: rgba(15, 23, 42, 0.4);
  overflow-x: auto;
  min-height: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.sandbox-body * {
  box-sizing: border-box;
}
.sandbox-body input, .sandbox-body select, .sandbox-body textarea {
  color: #fff !important;
  background-color: #0b1120 !important;
  border: 1px solid #334155 !important;
}

/* Demo buttons inside sandbox */
.demo-btn {
  background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 7px 15px;
  border-radius: 7px;
  font-weight: 700;
  font-family: inherit;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.15s ease;
  box-shadow: 0 4px 10px rgba(2, 132, 199, 0.3);
}
.demo-btn:hover {
  background: linear-gradient(135deg, #38bdf8 0%, #0284c7 100%);
  color: #04101e;
  transform: translateY(-1px);
}
.react-live-demo {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.react-live-demo .demo-header {
  font-size: 13px;
  font-weight: 800;
  color: var(--sky);
  margin-bottom: 2px;
}
.react-live-demo .demo-desc {
  font-size: 12px;
  color: var(--text-dim);
  line-height: 1.6;
  margin-bottom: 6px;
}

.terminal-console {
  display: block;
  background: #010307;
  border: 1px solid #1e293b;
  border-radius: 7px;
  padding: 12px 16px;
  font-family: 'Fira Code', monospace;
  font-size: 12px;
  color: #4ade80;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
  line-height: 1.65;
}

/* Real Production Scenario */
.production-block {
  background: rgba(16, 185, 129, 0.05);
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-right: 3px solid var(--emerald);
  border-radius: 8px;
  padding: 14px 18px;
}
.production-text {
  font-size: 13.5px;
  color: #a7f3d0;
  line-height: 1.9;
  white-space: pre-line;
}

/* Interview Trap */
.interview-block {
  background: rgba(245, 158, 11, 0.05);
  border: 1px solid rgba(245, 158, 11, 0.2);
  border-right: 3px solid var(--amber);
  border-radius: 8px;
  padding: 14px 18px;
}
.interview-text {
  font-size: 13.5px;
  color: #fde68a;
  line-height: 1.85;
}

/* 3-Tier Problems Section */
.challenges-section-block {
  margin-top: 6px;
}
.problems-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.problem-card {
  background: rgba(15, 23, 42, 0.4);
  border: 1px solid var(--border-subtle);
  border-radius: 10px;
  padding: 14px 18px;
  transition: border-color 0.15s;
}
.problem-card:hover {
  border-color: rgba(168, 85, 247, 0.35);
}
.problem-top {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}
.problem-tier-badge {
  font-size: 10.5px;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 99px;
}
.problem-title-text {
  font-size: 13.5px;
  font-weight: 700;
  color: #fff;
}
.problem-desc-text {
  font-size: 13px;
  color: #cbd5e1;
  line-height: 1.75;
  margin-bottom: 6px;
}
.problem-hint-box {
  font-size: 12px;
  color: var(--text-dim);
  background: rgba(2, 6, 23, 0.5);
  padding: 6px 10px;
  border-radius: 5px;
  border-right: 2px solid var(--amber);
  margin-bottom: 8px;
}
.toggle-sol-btn {
  background: rgba(168, 85, 247, 0.1);
  border: 1px solid rgba(168, 85, 247, 0.25);
  color: #c084fc;
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 11.5px;
  font-family: inherit;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
}
.toggle-sol-btn:hover {
  background: rgba(168, 85, 247, 0.22);
  color: #fff;
}

/* Command Palette Modal */
.cmd-modal-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 999;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(12px);
  align-items: flex-start;
  justify-content: center;
  padding-top: 10vh;
}
.cmd-modal-backdrop.open {
  display: flex;
}
.cmd-modal {
  width: 100%;
  max-width: 620px;
  background: var(--bg-surface);
  border: 1px solid var(--border-medium);
  border-radius: 14px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.9);
  overflow: hidden;
}
.cmd-search-input {
  width: 100%;
  padding: 16px 20px;
  background: transparent;
  border: none;
  border-bottom: 1px solid var(--border-subtle);
  color: #fff;
  font-size: 15px;
  font-family: inherit;
  outline: none;
}
.cmd-results-list {
  max-height: 380px;
  overflow-y: auto;
  padding: 8px;
  list-style: none;
}
.cmd-result-item {
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  transition: 0.12s;
}
.cmd-result-item:hover, .cmd-result-item.selected {
  background: rgba(255, 255, 255, 0.05);
}
.cmd-item-title {
  font-weight: 700;
  font-size: 13.5px;
  color: #fff;
}
.cmd-item-sub {
  font-size: 11.5px;
  color: var(--text-mute);
}

.toast-notice {
  position: fixed;
  bottom: 20px;
  left: 20px;
  background: #10b981;
  color: #022c22;
  font-weight: 800;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 12.5px;
  display: none;
  z-index: 1000;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
}

/* Tabbed Architecture for Topic Cards */
.card-tab-nav {
  display: flex;
  gap: 6px;
  background: rgba(2, 6, 23, 0.7);
  padding: 4px;
  border-radius: 10px;
  border: 1px solid var(--border-subtle);
  margin-bottom: 14px;
  flex-wrap: wrap;
}
.card-tab-btn {
  flex: 1 1 auto;
  min-width: 130px;
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-dim);
  padding: 8px 12px;
  border-radius: 7px;
  font-size: 12.5px;
  font-family: inherit;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.15s ease;
}
.card-tab-btn:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.04);
}
.card-tab-btn.active {
  background: var(--bg-card);
  color: var(--sky);
  border-color: rgba(56, 189, 248, 0.35);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}
.card-tab-content {
  position: relative;
  min-height: 120px;
}
.tab-pane {
  display: none;
  animation: fadeInPane 0.2s ease-in-out;
}
.tab-pane.active {
  display: block;
}
@keyframes fadeInPane {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Mobile Sidebar Backdrop & Toggle */
.sidebar-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  z-index: 150;
  opacity: 0;
  transition: opacity 0.25s ease;
}
.sidebar-backdrop.active {
  display: block;
  opacity: 1;
}

.mobile-toggle-btn {
  display: none;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-medium);
  color: var(--text-main);
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 13px;
  font-family: inherit;
  font-weight: 800;
  cursor: pointer;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease;
}
.mobile-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.12);
  color: #fff;
}

.sidebar-close-btn {
  display: none;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-dim);
  padding: 5px 12px;
  border-radius: 7px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  font-family: inherit;
  transition: 0.15s;
}
.sidebar-close-btn:hover {
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
  border-color: rgba(239, 68, 68, 0.3);
}

@media (max-width: 1024px) {
  .mobile-toggle-btn {
    display: inline-flex;
  }
  .sidebar-close-btn {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    margin-bottom: 6px;
    align-self: flex-start;
  }
  .sidebar {
    position: fixed;
    top: 0;
    right: 0;
    width: 320px;
    max-width: 86vw;
    height: 100vh;
    z-index: 200;
    transform: translateX(100%);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: -10px 0 40px rgba(0, 0, 0, 0.85);
    background: #080c14;
    padding: 18px 16px;
  }
  .sidebar.mobile-open {
    transform: translateX(0);
  }
  .main-content {
    padding: 24px 20px 90px;
    width: 100%;
  }
  .top-nav {
    padding: 10px 16px;
    gap: 12px;
  }
}

@media (max-width: 768px) {
  .top-nav {
    padding: 8px 12px;
  }
  .brand-title {
    font-size: 13.5px;
  }
  .brand-badge {
    display: none;
  }
  .track-tabs {
    order: 3;
    width: 100%;
    overflow-x: auto;
    flex-wrap: nowrap;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    padding: 4px;
    gap: 4px;
  }
  .track-tabs::-webkit-scrollbar {
    display: none;
  }
  .track-tab {
    font-size: 11.5px;
    padding: 5px 9px;
  }
  .cmd-kbd {
    display: none;
  }
  .cmd-btn {
    padding: 5px 9px;
    font-size: 11.5px;
  }
  .btn-icon {
    padding: 5px 9px;
    font-size: 11.5px;
  }
  .main-content {
    padding: 16px 10px 80px;
  }
  .topic-page-title {
    font-size: 21px;
    line-height: 1.4;
  }
  .topic-page-desc {
    font-size: 13px;
  }
  .card-topbar {
    padding: 12px 14px;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  .card-title-group {
    width: 100%;
  }
  .card-meta-actions {
    width: 100%;
    justify-content: space-between;
  }
  .topic-h2 {
    font-size: clamp(15.5px, 4.5vw, 18px);
    line-height: 1.5;
  }
  .card-body-open {
    padding: 14px 10px;
    gap: 14px;
  }
  .card-tab-nav {
    overflow-x: auto;
    flex-wrap: nowrap;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    padding: 4px;
    gap: 4px;
  }
  .card-tab-nav::-webkit-scrollbar {
    display: none;
  }
  .card-tab-btn {
    min-width: max-content;
    padding: 6px 11px;
    font-size: 11.5px;
    white-space: nowrap;
  }
  .code-box pre {
    padding: 12px 14px;
    font-size: 12px;
  }
  .sandbox-body {
    padding: 12px;
  }
  .terminal-body-wrap {
    padding: 10px 12px !important;
  }
  .problem-card {
    padding: 12px 14px;
  }
}

@media print {
  .top-nav, .sidebar, .card-tab-nav, .card-meta-actions, .code-bar button, .toggle-sol-btn, .run-btn, .focus-view-toggle-btn, .topic-nav-pager { display: none !important; }
  .focus-active-mode .topic-card { display: block !important; }
  .topic-card { display: block !important; border: 1px solid #1e293b !important; box-shadow: none !important; break-inside: avoid; background: #0f1726 !important; margin-bottom: 25px !important; }
  .tab-pane { display: block !important; margin-bottom: 20px; page-break-inside: avoid; }
  .solution-container { display: block !important; }
  body { background: #04060a !important; color: #f8fafc !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}

/* Standard View: all cards open, smooth scroll to topic */
.focus-active-mode .topic-card {
  display: block;
}

.focus-view-toggle-btn {
  background: rgba(56, 189, 248, 0.1);
  border: 1px solid rgba(56, 189, 248, 0.35);
  color: var(--sky);
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 12px;
  font-family: inherit;
  font-weight: 800;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}
.focus-view-toggle-btn.is-focus-on {
  background: #38bdf8;
  color: #020617;
  border-color: #38bdf8;
  box-shadow: 0 0 15px rgba(56, 189, 248, 0.5);
}

.topic-nav-pager {
  display: none;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  padding: 14px 18px;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
}
.focus-active-mode .topic-nav-pager {
  display: flex !important;
}
.pager-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: #fff;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 12.5px;
  font-weight: 700;
  font-family: inherit;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s;
}
.pager-btn:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: rgba(255, 255, 255, 0.25);
}

/* Audio click synthesizer (Tactile feedback) */

/* ==========================================================================
   MILESTONE EXAM CHECKPOINT STYLES
   ========================================================================== */
.exam-milestone-card {
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.9) 0%, rgba(8, 12, 22, 0.95) 100%);
  border: 1px solid rgba(168, 85, 247, 0.35);
  border-radius: 20px;
  margin: 45px 0;
  box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.85), 0 0 35px -10px rgba(168, 85, 247, 0.2);
  overflow: hidden;
  position: relative;
  scroll-margin-top: 85px;
}
.exam-milestone-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #38bdf8, #a855f7, #ec4899);
}
.exam-card-banner {
  padding: 24px 28px 18px;
  background: rgba(168, 85, 247, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
}
.exam-badge-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 800;
  background: rgba(168, 85, 247, 0.15);
  border: 1px solid rgba(168, 85, 247, 0.35);
  color: #c084fc;
  margin-bottom: 8px;
}
.exam-title {
  font-size: 21px;
  font-weight: 900;
  color: #fff;
  letter-spacing: -0.3px;
  margin-bottom: 6px;
}
.exam-desc {
  font-size: 13.5px;
  color: var(--text-dim);
  line-height: 1.7;
}

.exam-body-content {
  padding: 24px 28px;
}
.exam-questions-container {
  display: flex;
  flex-direction: column;
  gap: 22px;
}
.exam-question-box {
  background: rgba(2, 6, 23, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 14px;
  padding: 18px 20px;
  transition: border-color 0.2s;
}
.exam-question-box:hover {
  border-color: rgba(255, 255, 255, 0.12);
}
.exam-q-header {
  margin-bottom: 14px;
}
.exam-q-badge {
  font-size: 10.5px;
  font-weight: 800;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.1);
  padding: 2px 8px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 6px;
}
.exam-q-text {
  font-size: 15px;
  font-weight: 800;
  color: #f8fafc;
  line-height: 1.7;
}

.exam-options-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.exam-option {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 10px;
  padding: 11px 16px;
  cursor: pointer;
  transition: all 0.15s ease;
  user-select: none;
}
.exam-option:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.18);
  transform: translateX(-3px);
}
.exam-opt-indicator {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 2px solid #475569;
  flex-shrink: 0;
  transition: all 0.15s;
}
.exam-opt-text {
  font-size: 13.5px;
  color: #e2e8f0;
  line-height: 1.6;
}

/* Exam states */
.exam-option.opt-correct {
  background: rgba(16, 185, 129, 0.15) !important;
  border-color: #10b981 !important;
  box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
}
.exam-option.opt-correct .exam-opt-indicator {
  border-color: #10b981;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
}
.exam-option.opt-wrong {
  background: rgba(239, 68, 68, 0.15) !important;
  border-color: #ef4444 !important;
  animation: shakeOpt 0.3s ease-in-out;
}
.exam-option.opt-wrong .exam-opt-indicator {
  border-color: #ef4444;
  background: #ef4444;
}
@keyframes shakeOpt {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  75% { transform: translateX(4px); }
}

.exam-expl-box {
  margin-top: 12px;
  background: rgba(56, 189, 248, 0.07);
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-right: 3px solid #38bdf8;
  border-radius: 8px;
  padding: 12px 16px;
  animation: fadeInExpl 0.25s ease-in-out;
}
@keyframes fadeInExpl {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}
.exam-expl-title {
  font-size: 12px;
  font-weight: 800;
  color: #38bdf8;
  margin-bottom: 4px;
}
.exam-expl-text {
  font-size: 13px;
  color: #e0f2fe;
  line-height: 1.8;
  margin: 0;
}

.exam-footer-card {
  margin-top: 24px;
  background: rgba(2, 6, 23, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 18px 22px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}
.exam-score-display {
  flex: 1;
  min-width: 240px;
}
.score-meta {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  margin-bottom: 6px;
}
.score-label {
  color: var(--text-dim);
  font-weight: 700;
}
.score-val {
  color: #fff;
  font-weight: 900;
  font-family: monospace;
}
.score-bar-bg {
  height: 7px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 99px;
  overflow: hidden;
  margin-bottom: 6px;
}
.score-bar-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #a855f7, #10b981);
  border-radius: 99px;
  transition: width 0.4s ease;
}
.score-feedback-text {
  font-size: 11.5px;
  color: var(--text-mute);
}
.exam-reset-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-medium);
  color: #fff;
  padding: 8px 18px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.15s;
}
.exam-reset-btn:hover {
  background: rgba(255, 255, 255, 0.12);
}

/* ==========================================================================
   REAL-WORLD COMPLETE PRODUCTION PROJECT STYLES
   ========================================================================== */
.master-project-section {
  background: linear-gradient(180deg, #070d18 0%, #03060d 100%);
  border: 1px solid rgba(56, 189, 248, 0.3);
  border-radius: 20px;
  margin: 50px 0;
  padding: 30px;
  box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.9), 0 0 35px -10px rgba(56, 189, 248, 0.18);
  position: relative;
  overflow: hidden;
  scroll-margin-top: 85px;
}
.master-project-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #38bdf8, #10b981, #6366f1);
}
.project-header-box {
  margin-bottom: 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-bottom: 18px;
}
.proj-badge-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}
.proj-badge {
  font-family: monospace;
  font-size: 11px;
  font-weight: 800;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.35);
  padding: 3px 10px;
  border-radius: 6px;
}
.proj-status-chip {
  font-size: 11px;
  font-weight: 700;
  color: #10b981;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.25);
  padding: 3px 10px;
  border-radius: 99px;
}
.proj-main-title {
  font-size: 24px;
  font-weight: 900;
  color: #fff;
  letter-spacing: -0.4px;
  margin-bottom: 8px;
}
.proj-main-desc {
  font-size: 14px;
  color: var(--text-dim);
  line-height: 1.8;
  max-width: 900px;
}

.project-tab-nav {
  display: flex;
  gap: 8px;
  background: rgba(2, 6, 23, 0.8);
  padding: 5px;
  border-radius: 10px;
  border: 1px solid var(--border-subtle);
  margin-bottom: 18px;
  flex-wrap: wrap;
}
.proj-tab-btn {
  flex: 1 1 auto;
  min-width: 150px;
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-dim);
  padding: 9px 14px;
  border-radius: 7px;
  font-size: 13px;
  font-family: inherit;
  font-weight: 800;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.15s ease;
}
.proj-tab-btn:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.05);
}
.proj-tab-btn.active {
  background: var(--bg-card);
  color: #38bdf8;
  border-color: rgba(56, 189, 248, 0.35);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
}

.proj-pane {
  display: none;
  animation: fadeInPane 0.2s ease-in-out;
}
.proj-pane.active {
  display: block;
}

/* Browser Frame */
.proj-preview-wrapper {
  background: #02050b;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.7);
}
.preview-browser-bar {
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding: 8px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.preview-dots {
  display: flex;
  gap: 6px;
}
.preview-dots span {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}
.preview-address-bar {
  flex: 1;
  max-width: 440px;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  padding: 3px 12px;
  font-family: monospace;
  font-size: 11px;
  color: #94a3b8;
  text-align: center;
  direction: ltr;
}
.preview-live-tag {
  font-family: monospace;
  font-size: 10px;
  color: #10b981;
  font-weight: 800;
}
.preview-body-frame {
  padding: 24px;
  min-height: 200px;
}

/* Line-by-Line Table */
.breakdown-card {
  background: rgba(2, 6, 23, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  overflow: hidden;
}
.breakdown-intro-note {
  padding: 12px 18px;
  background: rgba(56, 189, 248, 0.06);
  border-bottom: 1px solid rgba(56, 189, 248, 0.15);
  font-size: 12.5px;
  color: #cbd5e1;
}
.table-responsive-wrap {
  overflow-x: auto;
}
.breakdown-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  text-align: right;
}
.breakdown-table th {
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--border-medium);
  padding: 12px 16px;
  font-weight: 800;
  color: #94a3b8;
  font-size: 12px;
}
.breakdown-table td {
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  vertical-align: top;
  line-height: 1.7;
}
.line-row:hover {
  background: rgba(255, 255, 255, 0.025);
}
.line-num-cell {
  font-family: monospace;
  font-weight: 800;
  color: #38bdf8;
  font-size: 12px;
  white-space: nowrap;
}
.line-code-cell code {
  font-family: 'Fira Code', monospace;
  font-size: 12px;
  background: rgba(0, 0, 0, 0.6);
  padding: 2px 6px;
  border-radius: 4px;
  color: #e2e8f0;
  direction: ltr;
  display: inline-block;
  max-width: 280px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.line-role-cell strong {
  color: #fbbf24;
  font-size: 12px;
}
.line-expl-cell {
  color: #cbd5e1;
  font-size: 12.5px;
}

/* Sidebar special quick links */
.sidebar-special-links {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-subtle);
}
.sidebar-action-pill {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 800;
  text-decoration: none;
  transition: all 0.15s;
}
.pill-project {
  background: rgba(56, 189, 248, 0.1);
  border: 1px solid rgba(56, 189, 248, 0.3);
  color: #38bdf8;
}
.pill-project:hover {
  background: rgba(56, 189, 248, 0.2);
  color: #fff;
  transform: translateX(-2px);
}
.pill-exams {
  background: rgba(168, 85, 247, 0.1);
  border: 1px solid rgba(168, 85, 247, 0.3);
  color: #c084fc;
}
.pill-exams:hover {
  background: rgba(168, 85, 247, 0.2);
  color: #fff;
  transform: translateX(-2px);
}
"""

print("Obsidian Precision Dark Theme stylesheet ready.")
