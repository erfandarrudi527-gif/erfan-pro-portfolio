import os
import re

src = 'C:/Users/erfan/Desktop/Erfan_Creative_Portfolio/index.html'
dest = 'C:/Users/erfan/Desktop/erfan-pro-portfolio/index.html'

with open(src, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Update title
html = html.replace(
    '<title>ERFAN.OS — Personal Portfolio System v3.5</title>',
    '<title>ERFAN.OS v4.0 — Flagship Creative Portfolio & Interactive OS</title>'
)

# 2. Add Audio script link in head
if 'audio.js' not in html:
    html = html.replace('</head>', '<script src="audio.js"></script>\n</head>')

# 3. Add sound effects to sidebar links
html = html.replace(
    'onclick="switchTab(',
    'onmouseenter="if(window.Sound)Sound.playHover()" onclick="if(window.Sound)Sound.playClick();switchTab('
)

# 4. Add Home and Brew Lab tab to sidebar
sidebar_marker = '<button class="sidebar-link" id="nav-projects"'
nav_additions = '''<button class="sidebar-link active" id="nav-home" onmouseenter="if(window.Sound)Sound.playHover()" onclick="if(window.Sound)Sound.playClick();switchTab('home')">
        <i class="fa-solid fa-house"></i>
        <span>Home</span>
      </button>
      <button class="sidebar-link" id="nav-projects"'''

if 'id="nav-home"' not in html:
    html = html.replace(sidebar_marker, nav_additions)

lab_marker = '<button class="sidebar-link" id="nav-lab"'
brew_btn = '''<button class="sidebar-link" id="nav-brew" onmouseenter="if(window.Sound)Sound.playHover()" onclick="if(window.Sound)Sound.playClick();switchTab('brew')">
        <i class="fa-solid fa-mug-hot" style="color: #f59e0b;"></i>
        <span>DUN Brew Lab</span>
      </button>
      ''' + lab_marker

if 'id="nav-brew"' not in html:
    html = html.replace(lab_marker, brew_btn)

# 5. Add sub-page quick links to top taskbar
topbar_marker = '<div class="system-clock" id="systemClock">00:00:00</div>'
quick_links = '''<div style="display: flex; gap: 12px; align-items: center; margin-right: 18px;">
        <a href="projects.html" target="_blank" class="btn-sm" style="color: #94a3b8; text-decoration: none; font-size: 11px; font-family: var(--font-mono); padding: 3px 8px; border: 1px solid rgba(255,255,255,0.08); border-radius: 4px;"><i class="fa-solid fa-layer-group"></i> Archive</a>
        <a href="brew-lab.html" target="_blank" class="btn-sm" style="color: #f59e0b; text-decoration: none; font-size: 11px; font-family: var(--font-mono); padding: 3px 8px; border: 1px solid rgba(245,158,11,0.2); border-radius: 4px;"><i class="fa-solid fa-mug-hot"></i> Brew Lab</a>
        <a href="terminal.html" target="_blank" class="btn-sm" style="color: #38bdf8; text-decoration: none; font-size: 11px; font-family: var(--font-mono); padding: 3px 8px; border: 1px solid rgba(56,189,248,0.2); border-radius: 4px;"><i class="fa-solid fa-terminal"></i> Terminal OS</a>
        <a href="resume.html" target="_blank" class="btn-sm" style="color: #a855f7; text-decoration: none; font-size: 11px; font-family: var(--font-mono); padding: 3px 8px; border: 1px solid rgba(168,85,247,0.2); border-radius: 4px;"><i class="fa-solid fa-file-lines"></i> Print CV</a>
      </div>
      <div class="system-clock" id="systemClock">00:00:00</div>'''

html = html.replace(topbar_marker, quick_links)

# 6. Add pane-brew into windows container
brew_pane_html = '''
        <!-- SCREEN: DUN BREW LAB EMBEDDED -->
        <div class="view-pane" id="pane-brew">
          <div class="content-header">
            <div>
              <h2 style="font-size: 26px; font-weight: 800; color: #fff;">DUN Specialty Coffee Roastery & Extraction Lab</h2>
              <p style="color: var(--text-muted); font-size: 13.5px; margin-top: 4px;">Pitch Espresso Aesthetic (#020101) · Real-time Pour Ratio, Grind Micron & TDS Extraction Calculations</p>
            </div>
            <a href="brew-lab.html" target="_blank" class="btn" style="background: #d97706; border-color: #f59e0b; color: #fff;">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> Fullscreen Lab
            </a>
          </div>

          <div style="background: #020101; border: 1px solid #332219; border-radius: 16px; padding: 28px; margin-top: 20px; box-shadow: 0 0 40px rgba(217, 119, 6, 0.1);">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
              <div>
                <div style="margin-bottom: 18px;">
                  <label style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 12px; color: #d97706; margin-bottom: 8px;">
                    <span>EXTRACTION METHOD</span>
                  </label>
                  <select id="osBrewMethod" style="width: 100%; background: #120b08; color: #f59e0b; border: 1px solid #332219; padding: 10px; border-radius: 8px; font-family: var(--font-mono); outline: none;">
                    <option value="v60">Hario V60 (Ceramic Dripper)</option>
                    <option value="chemex">Chemex (Thick Fiber Filter)</option>
                    <option value="aeropress">AeroPress (Inverted Technique)</option>
                    <option value="frenchpress">French Press (Immersion)</option>
                  </select>
                </div>
                <div style="margin-bottom: 18px;">
                  <label style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 12px; color: #d97706; margin-bottom: 8px;">
                    <span>COFFEE DOSE</span>
                    <span id="osDoseVal" style="color: #fff;">20g</span>
                  </label>
                  <input type="range" id="osDose" min="12" max="36" value="20" step="1" style="width: 100%; accent-color: #d97706;">
                </div>
                <div style="margin-bottom: 18px;">
                  <label style="display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 12px; color: #d97706; margin-bottom: 8px;">
                    <span>BREW RATIO</span>
                    <span id="osRatioVal" style="color: #fff;">1:16</span>
                  </label>
                  <input type="range" id="osRatio" min="13" max="18" value="16" step="0.5" style="width: 100%; accent-color: #d97706;">
                </div>
              </div>
              <div style="background: #090503; border: 1px solid #2d180f; border-radius: 12px; padding: 20px; display: flex; flex-direction: column; justify-content: space-around; font-family: var(--font-mono);">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">
                  <span style="color: #a8a29e; font-size: 12px;">Total Target Water:</span>
                  <span id="osResWater" style="font-size: 20px; font-weight: 700; color: #f59e0b;">320 ml</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">
                  <span style="color: #a8a29e; font-size: 12px;">Bloom Stage (45s):</span>
                  <span id="osResBloom" style="color: #f59e0b; font-weight: 700;">50 ml</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px;">
                  <span style="color: #a8a29e; font-size: 12px;">Burr Micron Calibration:</span>
                  <span id="osResGrind" style="color: #fff; font-size: 12px;">Medium-Fine (600 µm)</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span style="color: #a8a29e; font-size: 12px;">Target Extraction Time:</span>
                  <span id="osResTime" style="color: #f59e0b; font-weight: 700;">2:45 - 3:15</span>
                </div>
              </div>
            </div>
          </div>
        </div>
'''

pane_projects_marker = '<div class="view-pane" id="pane-projects">'
if 'id="pane-brew"' not in html:
    html = html.replace(pane_projects_marker, brew_pane_html + '\n        ' + pane_projects_marker)

# 7. Add switchTab logic for brew
title_map_marker = "projects: 'ERFAN.OS - Projects Catalog (73)',"
brew_title_map = "brew: 'ERFAN.OS - DUN Specialty Coffee Extraction Lab',\n    projects: 'ERFAN.OS - Projects Catalog (73)',"
if 'brew:' not in html:
    html = html.replace(title_map_marker, brew_title_map)

# Add brew calculation script handler
brew_calc_script = '''
// DUN Brew Lab Calculator in OS
function initOsBrew() {
  const m = document.getElementById('osBrewMethod');
  const d = document.getElementById('osDose');
  const r = document.getElementById('osRatio');
  if (!m || !d || !r) return;

  function calc() {
    const dose = parseFloat(d.value);
    const ratio = parseFloat(r.value);
    const method = m.value;
    const water = Math.round(dose * ratio);
    const bloom = Math.round(dose * 2.5);
    let grind = "Medium-Fine (600 µm)";
    let time = "2:45 - 3:15";
    if (method === 'chemex') { grind = "Medium-Coarse (800 µm)"; time = "3:45 - 4:30"; }
    else if (method === 'aeropress') { grind = "Fine-Medium (450 µm)"; time = "1:45 - 2:00"; }
    else if (method === 'frenchpress') { grind = "Coarse (1000 µm)"; time = "4:00 - 5:00"; }

    const dv = document.getElementById('osDoseVal');
    const rv = document.getElementById('osRatioVal');
    const rw = document.getElementById('osResWater');
    const rb = document.getElementById('osResBloom');
    const rg = document.getElementById('osResGrind');
    const rt = document.getElementById('osResTime');
    if (dv) dv.textContent = dose + 'g';
    if (rv) rv.textContent = '1:' + ratio;
    if (rw) rw.textContent = water + ' ml';
    if (rb) rb.textContent = bloom + ' ml';
    if (rg) rg.textContent = grind;
    if (rt) rt.textContent = time;
  }
  d.addEventListener('input', () => { calc(); if(window.Sound) Sound.playHover(); });
  r.addEventListener('input', () => { calc(); if(window.Sound) Sound.playHover(); });
  m.addEventListener('change', () => { calc(); if(window.Sound) Sound.playClick(); });
  calc();
}
document.addEventListener('DOMContentLoaded', initOsBrew);
'''

html = html.replace('</script>', f'{brew_calc_script}\n</script>')

with open(dest, 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated erfan-pro-portfolio/index.html successfully! Length:', len(html))
