/* ═══════════ Barg — app logic ═══════════
   Flow: Welcome → Level → Home → Reading
   Reading features (from the Figma UI kit + user requests):
   · Vowels toggle  — plain ↔ fully diacritized (َ ُ ِ sukun) text
   · Translate toggle — the English of EACH SENTENCE sits directly under
     that Persian sentence (fa on top, en below — no hunting for meanings)
   · Tap a word → popup with transliteration, gloss, audio, harakat editor,
     Save to Words
   · Level stepper (− A…C +) — raises/lowers difficulty live: font size,
     line-height and default vowel state follow the level
   · Playback-speed cycle + live reading progress bar                    */

// ─── story data: paragraphs → sentence pairs (fa = voweled source, en = its translation)
const STORY = {
  title: 'داستان موش آهن‌خور',
  titleEn: 'The Story of the Iron-Eating Mouse',
  paragraphs: [
    [
      { fa: 'دَر زَمان‌هایِ قَدیم، یِک مَردِ تاجِر بود.', en: 'In ancient times, there was a merchant.' },
      { fa: 'او مِقدارِ زیادی آهَن داشت.', en: 'He owned a large amount of iron.' },
      { fa: 'تاجِر خواست بِه یِک سَفَرِ دور بِرَوَد.', en: 'The merchant wanted to go on a distant journey.' },
      { fa: 'او آهَن‌ها را بِه یِک مَردِ آشنا داد و گُفت: «لُطفاً این آهَن‌ها پیشِ تُو بمانَد.»', en: 'He handed the iron over to an acquaintance and said, "Please keep this iron safe for me."' },
      { fa: 'بَعد تاجِر بِه سَفَر رَفْت.', en: 'Then the merchant set off on his journey.' },
    ],
    [
      { fa: 'بَعد اَز مُدَتی، تاجِر اَز سَفَر بَرگَشت.', en: 'After some time, the merchant returned.' },
      { fa: 'او بِه خانه‌یِ مَردِ اَمانَت‌دار رَفْت تا آهَن‌هایِ خود را بِگیرد.', en: 'He went to the trustee\'s house to reclaim his iron.' },
      { fa: 'اَمّا مَردِ خائِن آهَن‌ها را دوست داشت و آن‌ها را برایِ خُودَش می‌خواست.', en: 'However, the traitorous man had grown fond of the iron and wanted it for himself.' },
      { fa: 'مَرد گُفت: «ای تاجِر، موشِ خانه‌یِ ما آمَد و تَمامِ آهَن‌هایِ سَختِ تُو را خُورد!»', en: 'The man said, "O merchant, a mouse came into our house and ate all of your hard iron!"' },
    ],
    [
      { fa: 'تاجِر مَردی باهوش بود.', en: 'The merchant was a clever man.' },
      { fa: 'او فَهمید که این حَرف دُروغ است و مَرد می‌خواهد اَموالِ او را بِدُزدَد.', en: 'He realized this was a lie and that the man intended to steal his property.' },
      { fa: 'اَمّا تاجِر چیزی نَگُفت و با آرامِش جَواب داد: «بَله، راست می‌گویی! موش دَندان‌هایِ تیزی دارَد و می‌تَوانَد آهَن را هم بِخُورَد.»', en: 'But the merchant said nothing and calmly replied, "Yes, you speak the truth! A mouse has sharp teeth and can indeed eat iron."' },
      { fa: 'مَردِ خائِن اَز حَرفِ تاجِر تَعَجُّب کَرد و خوش‌حال شُد.', en: 'The traitorous man was surprised by the merchant\'s response and felt relieved.' },
      { fa: 'بَعد تاجِر بِه مَرد گُفت: «فَردا برایِ ناهار بِه خانه‌یِ مَن بیا.»', en: 'Then the merchant said to him, "Come to my house for lunch tomorrow."' },
    ],
    [
      { fa: 'روزِ بَعد، وَقتی مَردِ خائِن بِه خانه‌یِ تاجِر آمَد، خِیلی ناراحَت بود.', en: 'The next day, when the traitorous man arrived at the merchant\'s house, he was deeply distressed.' },
      { fa: 'او فَرْیاد زَد: «پِسَرِ کوچکِ مَن گُم شُده اَست! او را پِیدا نِمی‌کُنَم.»', en: 'He cried out, "My young son is missing! I cannot find him anywhere."' },
    ],
    [
      { fa: 'تاجِر با آرامِش گُفت: «اِمروز مَن یِک پَرنده‌یِ بُزُرگ (شاهین) را دیدَم. آن پَرَنده اَز آسمان آمَد، پِسَرَت را با چَنگال‌هایِش گِرِفت و با خود بِه آسمان بُرد!»', en: 'The merchant calmly said, "Today I saw a large bird (a falcon). That bird swooped down from the sky, grabbed your son with its talons, and carried him up into the heavens!"' },
    ],
    [
      { fa: 'مَردِ خائِن عَصَبانی شُد و گُفت: «تُو دُروغ می‌گویی! چِطور یِک پَرنده می‌تَوانَد پِسَری بِه این بُزُرگی را بِبَرَد؟ این غَیْرِمُمکِن اَست!»', en: 'The traitorous man grew angry and said, "You are lying! How could a bird carry away a boy of that size? That is impossible!"' },
    ],
    [
      { fa: 'تاجِر لَبخَند زَد و گُفت: «چِرا تَعَجُّب می‌کُنی؟ دَر شَهری که یِک موش بِتَوانَد آهَن را بِخُورَد، یِک پَرنده هم می‌تَوانَد پِسَرَت را بِبَرَد!»', en: 'The merchant smiled and said, "Why are you surprised? In a city where a mouse can eat iron, a bird can certainly carry off your son!"' },
    ],
    [
      { fa: 'مَردِ خائِن خِیلی شَرمَنده شُد.', en: 'The traitorous man became thoroughly ashamed.' },
      { fa: 'او فَهمید که تاجِر مَکْرِ او را فَهمیده اَست.', en: 'He realized the merchant had seen through his deception.' },
      { fa: 'مَرد گُفت: «مَن اِشْتِباه کَردم. مَن بِه تُو دُروغ گُفتَم. آهَن‌هایِ تُو سالِم هَسْتَند. مَن آهَن‌ها را پَس می‌دَهَم، تُو لُطفاً پِسَرَم را بِه مَن بِدِه.»', en: 'The man said, "I made a mistake. I lied to you. Your iron is safe and intact. I will return your iron, please give me back my son."' },
    ],
    [
      { fa: 'تاجِر قَبول کَرد.', en: 'The merchant agreed.' },
      { fa: 'او آهَن‌ها را گِرِفت و پِسَر را بِه پِدَرِش پَس داد.', en: 'He took back his iron and returned the boy to his father.' },
    ],
  ],
};

// strip harakat (Arabic diacritics) → the design's "vowels OFF" rendering
const DIACRITICS = /[\u064B-\u0652\u0670\u06D6-\u06ED]/g;
const stripVowels = s => s.replace(DIACRITICS, '');

// mini lexicon for the tap-a-word popup (key = bare form, vowels removed)
const LEXICON = {
  'قدیم':   ['qadim',   'ancient'],   'زمان':    ['zaman',    'time'],
  'مرد':    ['mard',    'man'],       'تاجر':    ['tajer',    'merchant'],
  'مقدار':  ['meghdar', 'amount'],    'زیادی':   ['ziyad',    'much, a lot'],
  'آهن':    ['ahan',    'iron'],      'خواست':   ['khast',    'wanted'],
  'سفر':    ['safar',   'journey'],   'دور':     ['dur',      'far'],
  'آشنا':   ['ashna',   'acquainted'], 'گفت':    ['goft',     'said'],
  'لطفاً':  ['lotfan',  'please'],    'پیش':     ['pish',     'with, beside'],
  'تو':     ['to',      'you'],       'بماند':   ['bemanad',  'to stay'],
  'بعد':    ['ba\'d',   'after'],     'رفت':     ['raft',     'went'],
  'مدتی':   ['muddati', 'a while'],   'برگشت':   ['bargasht', 'returned'],
  'خانه':   ['khane',   'house'],     'امانت‌دار': ['amanatdar','trustee'],
  'خود':    ['khod',    'self'],      'بگیرد':   ['begirad',  'to take'],
  'اما':    ['amma',    'but'],       'خائن':    ['kha\'en',  'traitor'],
  'دوست':   ['dust',    'friend, fond'], 'داشت':  ['dasht',    'had'],
  'آن‌ها':  ['anha',    'those'],     'برای':    ['baraye',   'for'],
  'می‌خواست': ['mikhast','wanted'],   'ای':      ['ey',       'O'],
  'موش':    ['mush',    'mouse'],     'آمد':     ['amad',     'came'],
  'تمام':   ['tamam',   'all'],       'سخت':     ['sakht',    'hard'],
  'خورد':   ['khord',   'ate'],       'مردی':    ['mardi',    'a man'],
  'باهوش':  ['bahush',  'clever'],    'فهمید':   ['fahmid',   'realized'],
  'حرف':    ['harf',    'word, talk'],'دروغ':    ['dorugh',   'lie'],
  'است':    ['ast',     'is'],        'خواهد':   ['khahad',   'will'],
  'اموال':  ['amval',   'property'],  'بدزدد':   ['bedozdad', 'to steal'],
  'چیزی':   ['chizi',   'anything'],  'نگفت':    ['nagoft',   'did not say'],
  'آرامش':  ['aramesh', 'calm'],      'جواب':    ['javab',    'answer'],
  'داد':    ['dad',     'gave'],      'بله':     ['bale',     'yes'],
  'راست':   ['rast',    'truth'],     'می‌گویی': ['migooyi',  'you say'],
  'دندان‌های': ['dandanha','teeth'],  'تیزی':    ['tizi',     'sharp'],
  'دارد':   ['darad',   'has'],       'می‌تواند':['mitavanad','can'],
  'هم':     ['ham',     'also'],      'بخورد':   ['bikhord',  'to eat'],
  'تعجب':   ['ta\'ajjob','surprise'], 'خوش‌حال': ['khoshhal', 'pleased'],
  'شد':     ['shod',    'became'],    'فردا':    ['farda',    'tomorrow'],
  'ناهار':  ['nahar',   'lunch'],     'من':      ['man',      'I, my'],
  'بیا':    ['bia',     'come'],      'روز':     ['ruz',      'day'],
  'وقتی':   ['vaqti',   'when'],      'خیلی':    ['khiyali',  'very'],
  'ناراحت': ['narahat', 'upset'],     'فریاد':   ['faryad',   'shout'],
  'زد':     ['zad',     'struck, did'], 'پسر':   ['pesar',    'boy'],
  'کوچک':   ['kuchek',  'small'],     'گم':      ['gam',      'lost'],
  'شده':    ['shode',   'become'],    'پیدا':    ['peyda',    'found'],
  'نمی‌کنم':['nemikonam','I do not'],  'امروز':   ['emruz',    'today'],
  'پرنده':  ['parande', 'bird'],      'بزرگ':    ['bozorg',   'big'],
  'شاهین':  ['shahin',  'falcon'],    'دیدم':    ['didam',    'I saw'],
  'آسمان':  ['aseman',  'sky'],       'پسرت':    ['pesarat',  'your son'],
  'چنگال‌هایش': ['changalha','with its talons'], 'گرفت': ['gereft','grabbed'],
  'با':     ['ba',      'with'],      'برد':     ['bord',     'took away'],
  'عصبانی': ['asabani', 'angry'],     'چطور':    ['chetor',   'how'],
  'پسری':   ['pesari',  'a boy'],     'ببرد':    ['bebord',   'to carry off'],
  'غیرممکن':['gheyremomken','impossible'], 'لبخند':['labkhand','smile'],
  'چرا':    ['chera',   'why'],       'می‌کنی':  ['mikonai',  'you do'],
  'در':     ['dar',     'in'],        'شهری':    ['shahri',   'a city'],
  'که':     ['ke',      'that'],      'بتواند':  ['betavanad','can'],
  'قبول':   ['qabul',   'agreed'],    'کرد':     ['kard',     'did'],
  'پدرش':   ['pedarash', 'his father'],'پس':     ['pas',      'back'],
  'اشتباه': ['eshtebah','mistake'],   'سالم':    ['salem',    'intact'],
  'هستند':  ['hastand', 'are'],       'مکر':     ['makr',     'scheme'],
  'فهمیده': ['fahmide', 'understood'],
};

// ─── state ────────────────────────────────────────────────────────────────
const LEVELS = ['A', 'B', 'C'];
// per-level reading defaults: vowels start on for beginners only.
// NOTE: level = the reader's ability, NOT text size — font stays constant.
const LV = {
  A: { vowels: true  },
  B: { vowels: false },
  C: { vowels: false },
};
const state = { level: localStorage.getItem('barg-level') || 'A', vowels: false, translate: false, speed: 1.0, dark: false };
const edits = {};   // bare form -> harakat string edited by the learner

// ── dark mode ──
function setDark(on) {
  state.dark = on;
  document.body.classList.toggle('dark', on);
  const cl = document.getElementById('chkLight'), cd = document.getElementById('chkDark');
  if (cl) { cl.classList.toggle('hidden', on); cd.classList.toggle('hidden', !on); }
}

// ── home hamburger menu: theme + level box ──
const hambBtn = document.getElementById('hambBtn');
const hambPop = document.getElementById('hambPop');
hambBtn.addEventListener('click', e => {
  e.stopPropagation();
  hambPop.classList.toggle('hidden');
});
document.addEventListener('click', e => {
  if (!hambPop.classList.contains('hidden') && !hambPop.contains(e.target)) hambPop.classList.add('hidden');
});
hambPop.querySelectorAll('[data-theme]').forEach(b =>
  b.addEventListener('click', () => setDark(b.dataset.theme === 'dark')));
const lvBox = document.getElementById('lvBox');
document.getElementById('hambLevelRow').addEventListener('click', e => {
  e.stopPropagation();
  lvBox.classList.toggle('hidden');
});
lvBox.querySelectorAll('.lv-opt').forEach(b => b.addEventListener('click', () => {
  setLevel(b.dataset.level);
  lvBox.querySelectorAll('.lv-opt').forEach(o => o.classList.toggle('sel', o === b));
  document.getElementById('hambLevelVal').textContent = b.dataset.level;
}));

// ── server connection (API key) ──────────────────────────────────────────
const apiBox = document.getElementById('apiBox');
const apiKeyInput = document.getElementById('apiKeyInput');
const apiHint = document.getElementById('apiHint');
document.getElementById('hambApiRow').addEventListener('click', e => {
  e.stopPropagation();
  apiBox.classList.toggle('hidden');
});
function refreshApiBadge() {
  const on = BARGE_API.ready();
  document.getElementById('hambApiVal').textContent = on ? 'on' : 'off';
  if (on) apiKeyInput.value = BARGE_API.getKey();
}
document.getElementById('apiKeySave').addEventListener('click', async () => {
  const k = BARGE_API.setKey(apiKeyInput.value);
  if (!k) { apiHint.textContent = 'Key cleared — running on offline data.'; refreshApiBadge(); return; }
  apiHint.textContent = 'Testing…';
  const ok = await BARGE_API.ping();
  try {
    await BARGE_API.listStories({ level: state.level });
    apiHint.textContent = '✓ Connected — loading stories from the server.';
    refreshApiBadge();
    loadStories();
  } catch (err) {
    apiHint.textContent = `✗ Server said ${err.message} — check the key.`;
  }
});
refreshApiBadge();

// ─── navigation ───────────────────────────────────────────────────────────
// in-app history stack so the Back button walks screens instead of leaving the app
const navStack = [];
let navPop = false;
function nav(id) {
  const prev = document.querySelector('.screen.active');
  document.querySelectorAll('.screen').forEach(s => s.classList.toggle('active', s.id === id));
  if (id === 'scr-home') {
    document.getElementById('homeStat').textContent = `Level ${state.level} · ${savedWords().length} words saved`;
    document.getElementById('reviewDue').textContent = `${savedWords().length} due →`;
  }
  if (navPop) navPop = false;                                   // a back-step: don't re-record it
  else {
    // Seed the stack with the previous screen (if any) so Back can return there
    if (navStack.length === 0 && prev && prev.id !== id) navStack.push(prev.id);
    if (navStack[navStack.length - 1] !== id) navStack.push(id);
  }
}
document.querySelectorAll('[data-nav]').forEach(b => b.addEventListener('click', () => nav(b.dataset.nav)));

// ── level onboarding shows ONCE (first launch only) ──
const onboarded = () => localStorage.getItem('barg-onboarded') === '1';
document.getElementById('getStarted').addEventListener('click', () =>
  nav(onboarded() ? 'scr-home' : 'scr-level'));
document.getElementById('levelGo').addEventListener('click', () => {
  localStorage.setItem('barg-onboarded', '1');
  nav('scr-home');
});
// "Not sure? Take a quick test" — for now we cycle through the levels to demo
const quickTest = document.getElementById('quickTestBtn');
if (quickTest) quickTest.addEventListener('click', () => {
  const i = LEVELS.indexOf(state.level);
  setLevel(LEVELS[(i + 1) % LEVELS.length], { applyDefaults: true });
  quickTest.textContent = `Sample: level ${state.level} — press Continue when happy`;
});

// --- local accounts: anyone creates their own user+pass, saved on this device ---
const AUTH_KEY  = 'barg-auth';    // who is signed in right now
const USERS_KEY = 'barg-users';   // { username: sha256(password) }
const authed = () => !!localStorage.getItem(AUTH_KEY);
const loginGo = () => nav(onboarded() ? 'scr-home' : 'scr-level');  // ask the level again after a sign-out
const readUsers  = () => { try { return JSON.parse(localStorage.getItem(USERS_KEY)) || {}; } catch (e) { return {}; } };
const writeUsers = (u) => localStorage.setItem(USERS_KEY, JSON.stringify(u));

// compact pure-JS SHA-256 (crypto.subtle is unavailable inside a file:// WebView)
function sha256(str) {
  const rr = (v, c) => (v >>> c) | (v << (32 - c));
  const K = [0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  let h0=0x6a09e667,h1=0xbb67ae85,h2=0x3c6ef372,h3=0xa54ff53a,h4=0x510e527f,h5=0x9b05688c,h6=0x1f83d9ab,h7=0x5be0cd19;
  const b = []; for (let i=0;i<str.length;i++) b.push(str.charCodeAt(i)&0xff);
  const bl = b.length*8; b.push(0x80);
  while (b.length%64!==56) b.push(0);
  for (let i=56;i>=0;i-=8) b.push(Math.floor(bl/Math.pow(2,i))&0xff);
  for (let c=0;c<b.length;c+=64) {
    const w=[]; for(let i=0;i<16;i++) w[i]=(b[c+i*4]<<24)|(b[c+i*4+1]<<16)|(b[c+i*4+2]<<8)|b[c+i*4+3];
    for(let i=16;i<64;i++){const s0=rr(w[i-15],7)^rr(w[i-15],18)^(w[i-15]>>>3),s1=rr(w[i-2],17)^rr(w[i-2],19)^(w[i-2]>>>10);w[i]=(w[i-16]+s0+w[i-7]+s1)|0;}
    let a=h0,B=h1,C=h2,D=h3,E=h4,F=h5,G=h6,H=h7;
    for(let i=0;i<64;i++){const S1=rr(E,6)^rr(E,11)^rr(E,25),ch=(E&F)^(~E&G),t1=(H+S1+ch+K[i]+w[i])|0,S0=rr(a,2)^rr(a,13)^rr(a,22),mj=(a&B)^(a&C)^(B&C),t2=(S0+mj)|0;H=G;G=F;F=E;E=(D+t1)|0;D=C;C=B;B=a;a=(t1+t2)|0;}
    h0=(h0+a)|0;h1=(h1+B)|0;h2=(h2+C)|0;h3=(h3+D)|0;h4=(h4+E)|0;h5=(h5+F)|0;h6=(h6+G)|0;h7=(h7+H)|0;
  }
  const hx=(n)=>('00000000'+(n>>>0).toString(16)).slice(-8);
  return hx(h0)+hx(h1)+hx(h2)+hx(h3)+hx(h4)+hx(h5)+hx(h6)+hx(h7);
}

const loginUser = document.getElementById('loginUser');
const loginPass = document.getElementById('loginPass');
const loginHint = document.getElementById('loginHint');
const loginBtn  = document.getElementById('loginBtn');
const tabSignin = document.getElementById('tabSignin');
const tabSignup = document.getElementById('tabSignup');
let loginMode = 'signin';
function setLoginMode(m) {
  loginMode = m;
  tabSignin.classList.toggle('active', m === 'signin');
  tabSignup.classList.toggle('active', m === 'signup');
  loginBtn.textContent = m === 'signup' ? 'Create account' : 'Sign in';
  loginPass.setAttribute('autocomplete', m === 'signup' ? 'new-password' : 'current-password');
  loginHint.textContent = '';
}
tabSignin.addEventListener('click', () => setLoginMode('signin'));
tabSignup.addEventListener('click', () => setLoginMode('signup'));
function doLogin() {
  const u = loginUser.value.trim(), p = loginPass.value;
  if (!u || !p) { loginHint.textContent = 'Enter a username and password.'; return; }
  const users = readUsers();
  if (loginMode === 'signup') {
    if (users[u]) { loginHint.textContent = 'That username is taken - sign in instead.'; return; }
    if (p.length < 4) { loginHint.textContent = 'Use at least 4 characters for the password.'; return; }
    users[u] = sha256(p); writeUsers(users);
    loginHint.textContent = '';
    localStorage.setItem(AUTH_KEY, u); loginGo();
  } else {
    if (!users[u] || users[u] !== sha256(p)) { loginHint.textContent = 'Wrong username or password.'; return; }
    loginHint.textContent = '';
    localStorage.setItem(AUTH_KEY, u); loginGo();
  }
}
loginBtn.addEventListener('click', doLogin);
[loginUser, loginPass].forEach(i => i.addEventListener('keydown', e => { if (e.key === 'Enter') doLogin(); }));
setLoginMode(Object.keys(readUsers()).length ? 'signin' : 'signup');
if (authed()) loginGo();   // stay signed in - no login needed on this device

// --- switch account (same device, a different person) ---
const swBtn = document.getElementById('hambSwitchUser');
if (swBtn) swBtn.addEventListener('click', () => {
  localStorage.removeItem(AUTH_KEY);
  localStorage.removeItem('barg-onboarded');   // the next sign-in must ask the level again
  const pop = document.getElementById('hambPop'); if (pop) pop.classList.add('hidden');
  loginUser.value = ''; loginPass.value = ''; setLoginMode('signin');
  nav('scr-login');
});

// ── exit-confirmation dialog (shown when Back is pressed on the root screen) ──
function showExitDialog() { document.getElementById('exitBackdrop').classList.remove('hidden'); }
function hideExitDialog() { document.getElementById('exitBackdrop').classList.add('hidden'); }
document.getElementById('exitNo').addEventListener('click', hideExitDialog);
document.getElementById('exitYes').addEventListener('click', () => {
  hideExitDialog();
  // In the Android WebView (MainActivity) this scheme closes the app.
  // In a normal browser we simply dismiss the dialog instead of navigating.
  try { location.href = 'barg://exit'; } catch (e) { /* no-op */ }
});
// ── one shared Back action for the hardware key AND the on-screen back buttons ──
function appBack() {
  // 1) if an overlay/menu is open, Back just closes it
  const eb = document.getElementById('exitBackdrop');
  if (eb && !eb.classList.contains('hidden')) { hideExitDialog(); return; }
  const wp = document.getElementById('wordPopup');
  if (wp && wp.classList.contains('show')) { closePopup(); return; }
  const mp = document.getElementById('menuPop'); if (mp && !mp.classList.contains('hidden')) { mp.classList.add('hidden'); return; }
  const hp = document.getElementById('hambPop'); if (hp && !hp.classList.contains('hidden')) { hp.classList.add('hidden'); return; }
  const lb = document.getElementById('lvBox');   if (lb && !lb.classList.contains('hidden'))   { lb.classList.add('hidden'); return; }
  const ab = document.getElementById('apiBox');  if (ab && !ab.classList.contains('hidden'))   { ab.classList.add('hidden'); return; }
  // 2) otherwise step back through the in-app screen stack (never leaves the app)
  if (navStack.length > 1) {
    navStack.pop();
    navPop = true;
    nav(navStack[navStack.length - 1]);
    return;
  }
  // 3) at the root screen: confirm before leaving
  showExitDialog();
}
window.bargBack = appBack;   // hardware back key (MainActivity evaluates bargBack())
// Browser Escape key mirrors the hardware back for desktop preview
window.addEventListener('keydown', e => { if (e.key === 'Escape') appBack(); });
// on-screen back buttons use the exact same path
['backBtn', 'reviewBackBtn'].forEach(bid => {
  const b = document.getElementById(bid);
  if (b) b.addEventListener('click', appBack);
});

// ─── saved words (persistent) ─────────────────────────────────────────────
function savedWords() {
  try { return JSON.parse(localStorage.getItem('barg-words') || '[]'); }
  catch (e) { return []; }
}
function saveWord(item) {
  const list = savedWords();
  list.unshift(item);
  localStorage.setItem('barg-words', JSON.stringify(list));
}
const savedHas = w => savedWords().some(x => x.w === w);
function updateSaveCount() {
  const n = savedWords().length;
  document.getElementById('homeStat').textContent = `Level ${state.level} · ${n} words saved`;
  document.getElementById('reviewDue').textContent = `${n} due →`;
  document.getElementById('reviewCount').textContent = n;
}

// ─── review: Instagram-style card deck (swipe up for next card) ───────────
function renderDeck() {
  const words = savedWords();
  const deck = document.getElementById('cardDeck');
  document.getElementById('reviewCount').textContent = words.length;
  if (!words.length) {
    deck.innerHTML = `<div class="deck-empty">
      <p>No saved words yet.</p>
      <p>Tap any word while reading and press <b>Save to Words</b>.</p>
    </div>`;
    document.getElementById('deckHint').style.visibility = 'hidden';
    return;
  }
  document.getElementById('deckHint').style.visibility = 'visible';
  // show the top 3 so the next card peeks behind, like Stories
  deck.innerHTML = words.slice(0, 3).map((x, i) => `
    <div class="wcard" data-i="${i}" style="z-index:${10 - i};
         transform:translateY(${i * 14}px) scale(${1 - i * 0.04});
         opacity:${i === 0 ? 1 : 0.85}">
      <div class="wcard-top">
        <span class="wcard-idx">${words.length - i} / ${words.length}</span>
        <button class="wcard-del" data-del="${i}" title="Remove from saved">
          <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 4h11M6 4V2.5h4V4M4 4l.8 9.5h6.4L12 4M6.5 7v4M9.5 7v4"/></svg>
        </button>
      </div>
      <p class="wcard-word fa">${x.v || x.w}</p>
      <p class="wcard-tr">${x.tr}</p>
      <p class="wcard-gloss">${x.gl}</p>
      <p class="wcard-role">${ROLE[x.w] || ''}</p>
    </div>`).join('');
  bindSwipe();
  deck.querySelectorAll('.wcard-del').forEach(btn => btn.addEventListener('click', e => {
    e.stopPropagation();
    const i = +btn.dataset.del;
    const card = btn.closest('.wcard');
    card.classList.add('drop');                 // fly off to the side
    setTimeout(() => {
      const list = savedWords();
      list.splice(i, 1);                        // deck card i = saved list index i
      localStorage.setItem('barg-words', JSON.stringify(list));
      renderDeck(); updateSaveCount();
    }, 340);
  }));
}
function swipeNext() {
  const top = document.querySelector('#cardDeck .wcard[data-i="0"]');
  if (!top) return;
  top.classList.add('fly');
  setTimeout(() => {
    const list = savedWords();
    if (list.length > 1) { list.push(list.shift()); }   // rotate — nothing is deleted
    localStorage.setItem('barg-words', JSON.stringify(list));
    renderDeck();
  }, 320);
}
function bindSwipe() {
  const deck = document.getElementById('cardDeck');
  let y0 = null;
  const down = y => { y0 = y; };
  const up = y => {
    if (y0 !== null && y0 - y > 60) swipeNext();   // swipe up
    y0 = null;
  };
  deck.onmousedown = e => down(e.clientY);
  deck.onmouseup = e => up(e.clientY);
  deck.ontouchstart = e => down(e.touches[0].clientY);
  deck.ontouchend = e => up(e.changedTouches[0].clientY);
  deck.onclick = e => { if (e.target.closest('.wcard[data-i="0"]')) swipeNext(); };
}
document.getElementById('reviewOpen').addEventListener('click', () => {
  renderDeck(); nav('scr-review');
});

// ─── level (shared by picker + reading stepper) ───────────────────────────
function setLevel(l, opts = {}) {
  state.level = l;
  localStorage.setItem('barg-level', l);   // remember the level across launches
  document.getElementById('lvNow').textContent = l;
  document.getElementById('homeStat').textContent = `Level ${l} · ${savedWords().length} words saved`;
  document.getElementById('hambLevelVal').textContent = l;
  document.querySelectorAll('#lvBox .lv-opt').forEach(o => o.classList.toggle('sel', o.dataset.level === l));
  // sync the onboarding picker
  document.querySelectorAll('.level-card').forEach(c => {
    const on = c.dataset.level === l;
    c.classList.toggle('selected', on);
    c.querySelector('.lv-check')?.remove();
    if (on) c.insertAdjacentHTML('beforeend', CHECK_SVG);
  });
  // difficulty follows the level: bigger text + vowels for beginners
  if (opts.applyDefaults) {
    state.vowels = LV[l].vowels;
    btnV.classList.toggle('on', state.vowels);
    if (document.getElementById('scr-reading').classList.contains('active')) rerenderReading();
  }
  applyTypeScale();
  refreshStories();   // swap the home story list to the new level instantly
}
function applyTypeScale() {
  // playback spacing is fixed; the ▶ button is inert until the audio feature lands
  const now = document.getElementById('lvNow');
  now.classList.remove('bump'); void now.offsetWidth; now.classList.add('bump');
}
document.getElementById('lvUp').addEventListener('click', () => {
  const i = LEVELS.indexOf(state.level);
  if (i < LEVELS.length - 1) setLevel(LEVELS[i + 1], { applyDefaults: true });
});
document.getElementById('lvDown').addEventListener('click', () => {
  const i = LEVELS.indexOf(state.level);
  if (i > 0) setLevel(LEVELS[i - 1], { applyDefaults: true });
});

// ─── level picker (onboarding) ────────────────────────────────────────────
const CHECK_SVG = '<svg class="lv-check" viewBox="0 0 12 10" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M1 5l3.5 3.5L11 1"/></svg>';
document.querySelectorAll('.level-card').forEach(card => {
  card.addEventListener('click', () => setLevel(card.dataset.level));
});

// ─── home story cards ─────────────────────────────────────────────────────
const SNIPPET = stripVowels(STORY.paragraphs[0].map(s => s.fa).join(' '));

// offline fallback list (used when the server is unreachable / no key yet)
const STORIES = [
  { t: 'داستانِ موشِ آهن‌خور', img: 'assets/mouse.png',  v: 'داستان موش آهن‌خور' },
  { t: 'گربه روزه دار',        img: 'assets/cat.png',    v: 'گربه روزه‌دار' },
  { t: 'روباه حیله گر',        img: 'assets/fox.png',    v: 'روباه حیله‌گر' },
  { t: 'شکارچی باهوش',         img: 'assets/hunter.png', v: 'شکارچی باهوش' },
];

// story list currently on screen (server list, or the offline fallback)
let storiesNow = STORIES;
let apiStories = null;   // full story list from the server (unfiltered by level)

const THUMBS = ['assets/mouse.png', 'assets/cat.png', 'assets/fox.png', 'assets/hunter.png'];
function renderStoryList(list) {
  if (Array.isArray(list) && list.length === 0) {
    storiesNow = [];
    document.getElementById('storyList').innerHTML =
      '<p class="story-empty">No stories at this level yet &mdash; try another level.</p>';
    return;
  }
  storiesNow = list && list.length ? list : STORIES;
  document.getElementById('storyList').innerHTML = storiesNow.map((s, i) => `
    <button class="story-card" data-story="${i}">
      <span class="txt"><h3>${s.t}</h3><p>${s.snippet || SNIPPET} ...</p></span>
      <img class="story-thumb" src="${s.img || THUMBS[i % THUMBS.length]}" alt="${s.t}" loading="lazy">
    </button>`).join('');
  document.querySelectorAll('.story-card').forEach(c =>
    c.addEventListener('click', () => openReading(+c.dataset.story)));
}

// ── story list is filtered by the selected level, taken straight from the API.
//    The server ignores single-letter levels, so we group client-side by the first
//    letter of each story's CEFR code: A=A1/A2, B=B1/B2, C=C1/C2.
const levelLetter = r => String(r.level || '').trim().charAt(0).toUpperCase();
const mapStoryRow = (r, i) => ({
  id: r.id,
  t: r.titleFa,
  v: stripVowels(r.titleFa || r.titleEn || ''),
  tEn: r.titleEn,
  level: r.level,
  wordCount: r.wordCount,
  snippet: r.titleEn ? `(${r.titleEn})` : '',
  img: THUMBS[i % THUMBS.length],
});
// the API stories that belong to the currently selected level
const storiesForLevel = () => (apiStories || []).filter(r => levelLetter(r) === state.level).map(mapStoryRow);

// ── fetch ALL stories once, then show only the current level's ──
async function loadStories() {
  if (!BARGE_API.ready()) { renderStoryList(STORIES); return; }
  try {
    apiStories = await BARGE_API.listStories();
    renderStoryList(storiesForLevel());   // exactly the server stories for this level; an empty level shows the empty state (no fake data)
  } catch (e) {
    console.warn('stories: falling back to offline list —', e.message);
    renderStoryList(STORIES);
  }
}
// swap the visible list to the new level instantly (reuses the cached list, no refetch)
function refreshStories() {
  if (apiStories) renderStoryList(storiesForLevel());
  else if (BARGE_API.ready()) loadStories();
}
renderStoryList(STORIES);
// restore the last chosen level (UI + reading defaults), then fetch stories once
setLevel(state.level, { applyDefaults: true });
loadStories();

// ─── reading screen ───────────────────────────────────────────────────────
const bodyEl = document.getElementById('storyBody');
const titleEl = document.getElementById('storyTitle');
const titleEnEl = document.getElementById('storyTitleEn');

function bare(word) {
  return stripVowels(word).replace(/[،.:!?«»()\u200c]/g, '').trim();
}
function wordSpan(raw) {
  return `<span class="word" data-w="${raw}">${raw}</span>`;
}
// one Persian sentence on top, its English directly underneath
function renderBody() {
  bodyEl.innerHTML = STORY.paragraphs.map(par => par.map(s => {
    let text = state.vowels ? s.fa : stripVowels(s.fa);
    // re-apply any harakat the learner added manually (bare-text path)
    if (!state.vowels) Object.entries(edits).forEach(([b, str]) => {
      text = text.replace(new RegExp('(?<=^|[\\s\\u200c])' + b + '(?=$|[\\s\\u200c،.:!?»«()])', 'g'), str);
    });
    return `<p class="pair">${text.split(/\s+/).map(wordSpan).join(' ')}
      <span class="en-line">${s.en}</span>
    </p>`;
  }).join('')).join('');
  applyTypeScale();
  bindWords();
}
let currentStoryDto = null;   // the API story currently open (null = offline bundle)
function openReading(idx = 0) {
  const s = storiesNow[idx] || storiesNow[0] || STORIES[0];
  currentStoryDto = null;
  titleEl.textContent = s.v || s.t;
  titleEnEl.textContent = s.tEn || '';
  if (s.id && BARGE_API.ready()) {
    // this card is a real server story → load its OWN text from the API
    bodyEl.innerHTML = '<p class="story-empty">Loading\u2026</p>';
    nav('scr-reading');
    loadReading(s.id);
  } else {
    renderBody();          // no id / offline → bundled story
    nav('scr-reading');
  }
}
// re-render whichever story is open, WITHOUT reverting an API story to the bundle
function rerenderReading() { currentStoryDto ? renderServerBody(currentStoryDto) : renderBody(); }

// ── server version of the reading screen ────────────────────────────────
// StoryTextDto: { titleFa, titleEn, levelFa, levelEn,
//                  lines: [ { order, translationEn,
//                             words: [ { wordId, text, textWithHarakat,
//                                        ezafeSuffix, leadingPunctuation,
//                                        trailingPunctuation, partOfSpeech,
//                                        meaning } ] } ] }
let storyWords = {};   // bareText -> WordDto-ish info for the tap popup

function apiWordToRaw(w) {
  return `${w.leadingPunctuation || ''}${w.text || ''}${w.ezafeSuffix || ''}${w.trailingPunctuation || ''}`;
}

function renderServerBody(dto) {
  bodyEl.innerHTML = (dto.lines || []).map(line => {
    const parts = (line.words || []).map(w => {
      const raw = apiWordToRaw(w);
      const shown = state.vowels ? (w.textWithHarakat || w.text) : w.text;
      // remember this word's server-side grammar for the popup
      const bareKey = bare(shown || raw);
      storyWords[bareKey] = {
        meaning: w.meaning,
        partOfSpeech: w.partOfSpeech,
        translit: w.textWithHarakat ? stripVowels(w.text) : '',
        id: w.wordId,
      };
      const lead = w.leadingPunctuation || '';
      const tail = `${w.ezafeSuffix || ''}${w.trailingPunctuation || ''}`;
      return `${lead}<span class="word" data-w="${shown}">${shown}</span>${tail}`;
    }).join(' ');
    const en = line.translationEn
      ? `<span class="en-line">${line.translationEn}</span>` : '';
    return `<p class="pair">${parts}${en}</p>`;
  }).join('');
  bindWords();
}

async function loadReading(id) {
  try {
    const dto = await BARGE_API.getStoryText(id);
    currentStoryDto = dto;
    titleEl.textContent = dto.titleFa || titleEl.textContent;
    titleEnEl.textContent = dto.titleEn || titleEnEl.textContent;
    renderServerBody(dto);
  } catch (e) {
    console.warn('reading: server text unavailable —', e.message);
    if (!bodyEl.querySelector('.word')) renderBody();   // only if nothing was rendered yet
  }
}

// word tap → popup
const popup = document.getElementById('wordPopup');
const backdrop = document.getElementById('popupBackdrop');
let hlEl = null;
let popupBare = '', popupRaw = '';

// ── grammatical role of a word in its sentence ──
const ROLE = {
  'قدیم':'صفت (adjective) — describes زمان','زمان':'اسم (noun)','مرد':'اسم (noun)','تاجر':'اسم (noun)',
  'مقدار':'اسم (noun)','زیادی':'صفت (adjective) — modifies مقدار','آهن':'اسم (noun)',
  'خواست':'فعل (verb) — ماضی ساده','سفر':'اسم (noun)','دور':'قید (adverb)','آشنا':'صفت (adjective)',
  'گفت':'فعل (verb)','لطفاً':'قید (adverb)','پیش':'حرف اضافه (preposition)','تو':'ضمیر (pronoun)',
  'بماند':'فعل (verb) — مصدر + ب','بعد':'قید (adverb)','رفت':'فعل (verb)','مدتی':'اسم (noun)',
  'برگشت':'فعل (verb)','خانه':'اسم (noun)','امانت‌دار':'اسم (noun)','خود':'ضمیر (pronoun)',
  'بگیرد':'فعل (verb)','اما':'حرف ربط (conjunction)','خائن':'صفت (adjective)','دوست':'اسم (noun)',
  'داشت':'فعل (verb)','آن‌ها':'ضمیر (pronoun)','برای':'حرف اضافه (preposition)','می‌خواست':'فعل (verb) — استمراری',
  'ای':'حرف ندا (interjection)','موش':'اسم (noun)','آمد':'فعل (verb)','تمام':'صفت (adjective)',
  'سخت':'صفت (adjective)','خورد':'فعل (verb)','مردی':'اسم (noun)','باهوش':'صفت (adjective)',
  'فهمید':'فعل (verb)','حرف':'اسم (noun)','دروغ':'اسم (noun)','است':'فعل (verb) — اسنادی',
  'خواهد':'فعل کمکی (auxiliary)','اموال':'اسم (noun)','بدزدد':'فعل (verb)','چیزی':'ضمیر (pronoun)',
  'نگفت':'فعل (verb)','آرامش':'اسم (noun)','جواب':'اسم (noun)','داد':'فعل (verb)','بله':'حرف (particle)',
  'راست':'اسم (noun)','می‌گویی':'فعل (verb)','دندان‌های':'اسم (noun)','تیزی':'صفت (adjective)',
  'دارد':'فعل (verb)','می‌تواند':'فعل (verb)','هم':'قید (adverb)','بخورد':'فعل (verb)',
  'تعجب':'اسم (noun)','خوش‌حال':'صفت (adjective)','شد':'فعل (verb)','فردا':'قید (adverb)',
  'ناهار':'اسم (noun)','من':'ضمیر (pronoun)','بیا':'فعل (verb)','روز':'اسم (noun)',
  'وقتی':'حرف ربط (conjunction)','خیلی':'قید (adverb)','ناراحت':'صفت (adjective)','فریاد':'اسم (noun)',
  'زد':'فعل (verb)','پسر':'اسم (noun)','کوچک':'صفت (adjective)','گم':'اسم (noun)','شده':'فعل (verb)',
  'پیدا':'اسم (noun)','نمی‌کنم':'فعل (verb)','امروز':'قید (adverb)','پرنده':'اسم (noun)',
  'بزرگ':'صفت (adjective)','شاهین':'اسم (noun)','دیدم':'فعل (verb)','آسمان':'اسم (noun)',
  'پسرت':'اسم + ضمیر (your son)','چنگال‌هایش':'اسم (noun)','گرفت':'فعل (verb)',
  'با':'حرف اضافه (preposition)','برد':'فعل (verb)','عصبانی':'صفت (adjective)','چطور':'قید (adverb)',
  'پسری':'اسم (noun)','ببرد':'فعل (verb)','غیرممکن':'صفت (adjective)','لبخند':'اسم (noun)',
  'چرا':'قید (adverb)','می‌کنی':'فعل (verb)','در':'حرف اضافه (preposition)','شهری':'اسم (noun)',
  'که':'حرف ربط (conjunction)','بتواند':'فعل (verb)','قبول':'اسم (noun)','کرد':'فعل (verb)',
  'پدرش':'اسم + ضمیر (his father)','پس':'قید (adverb)','اشتباه':'اسم (noun)','سالم':'صفت (adjective)',
  'هستند':'فعل (verb)','مکر':'اسم (noun)','فهمیده':'فعل (verb)',
};

function bindWords() {
  bodyEl.querySelectorAll('.word').forEach(w => w.addEventListener('click', () => {
    const raw = w.dataset.w;
    const b = bare(raw);
    const [tr = '—', gl = 'no entry yet'] = LEXICON[b] || [];
    // prefer server-side word data when available
    const sw = storyWords[b];
    if (hlEl) hlEl.classList.remove('hl');
    hlEl = w; w.classList.add('hl');
    popupBare = b; popupRaw = raw;
    document.getElementById('popupWord').textContent = raw;
    document.getElementById('popupTranslit').textContent = sw
      ? `${b} | ${sw.translit || tr}` : `${b} | ${tr}`;
    document.getElementById('popupGloss').textContent = sw
      ? (sw.meaning || gl) : gl;
    document.getElementById('popupGrammar').classList.add('hidden');
    const save = document.getElementById('popupSave');
    const has = savedHas(b);
    save.textContent = has ? 'Saved ✓' : 'Save to Words';
    save.classList.toggle('saved', has);
    popup.classList.add('show'); backdrop.classList.remove('hidden');
  }));
}
document.getElementById('popupGrammarBtn').addEventListener('click', e => {
  const gr = document.getElementById('popupGrammar');
  const btn = e.currentTarget;
  if (!gr.classList.contains('hidden')) {            // toggle off
    gr.classList.add('hidden');
    btn.textContent = 'Grammar';
    return;
  }
  const b = popupBare, raw = popupRaw;
  const sw = storyWords[b];
  const role = sw?.partOfSpeech
    ? `(${sw.partOfSpeech})` : (ROLE[b] || 'کلمه‌ای در این جمله — a word used in this sentence');
  const [tr = ''] = LEXICON[b] || [];
  gr.innerHTML =
    `<b class="fa">${stripVowels(raw)}</b> — نقش در جمله:<br>` +
    `<span class="g-role">${role}</span>` +
    (tr ? `<br><span class="g-tr">تلفظ: ${tr}</span>` : '');
  gr.classList.remove('hidden');
  btn.textContent = 'Hide';                          // toggle on
});
function closePopup() {
  popup.classList.remove('show'); backdrop.classList.add('hidden');
  if (hlEl) { hlEl.classList.remove('hl'); hlEl = null; }
}
document.getElementById('popupClose').addEventListener('click', closePopup);
backdrop.addEventListener('click', closePopup);
document.getElementById('popupSave').addEventListener('click', e => {
  const b = popupBare, raw = popupRaw;
  const [tr = '—', gl = 'no entry yet'] = LEXICON[b] || [];
  const sw = storyWords[b];
  const btn = e.target;
  if (savedHas(b)) {                                 // already saved → remove it
    const list = savedWords().filter(x => x.w !== b);
    localStorage.setItem('barg-words', JSON.stringify(list));
    btn.textContent = 'Save to Words'; btn.classList.remove('saved');
  } else {                                           // save it
    saveWord({
      w: b, v: raw,
      tr: sw?.translit || tr,
      gl: sw?.meaning || gl,
      ts: Date.now(),
    });
    btn.textContent = 'Saved ✓'; btn.classList.add('saved');
  }
  updateSaveCount();
});
document.getElementById('popupAudio').addEventListener('click', () => {
  const w = document.getElementById('popupWord').textContent;
  if ('speechSynthesis' in window) {
    const u = new SpeechSynthesisUtterance(w); u.lang = 'fa-IR'; u.rate = 0.85;
    speechSynthesis.cancel(); speechSynthesis.speak(u);
  }
});

// control bar
const btnV = document.getElementById('btnVowels');
const btnT = document.getElementById('btnTranslate');
const btnS = document.getElementById('btnSpeed');
btnV.addEventListener('click', () => {
  state.vowels = !state.vowels;
  btnV.classList.toggle('on', state.vowels);
  closePopup(); rerenderReading();
});
btnT.addEventListener('click', () => {
  state.translate = !state.translate;
  btnT.classList.toggle('on', state.translate);
  bodyEl.classList.toggle('translating', state.translate);
  titleEnEl.classList.toggle('show', state.translate);
});
// ▶ play/speed button — fully inert for now (does nothing at all)
btnS.onclick = null;
btnS.style.pointerEvents = 'none';
btnS.classList.add('inert-btn');
btnS.title = 'Coming soon';

// ── three-dot options menu (mirrors the control bar) ──
const menuBtn = document.getElementById('menuBtn');
const menuPop = document.getElementById('menuPop');
function syncMenu() {
  const t = document.getElementById('miTranslate'), v = document.getElementById('miVowels');
  t.textContent = state.translate ? 'on' : 'off'; t.classList.toggle('on', state.translate);
  v.textContent = state.vowels ? 'on' : 'off'; v.classList.toggle('on', state.vowels);
  document.getElementById('miSpeed').textContent = state.speed.toFixed(1) + '×';
}
menuBtn.addEventListener('click', e => {
  e.stopPropagation();
  syncMenu();
  menuPop.classList.toggle('hidden');
});
document.addEventListener('click', e => {
  if (!menuPop.classList.contains('hidden') && !menuPop.contains(e.target)) menuPop.classList.add('hidden');
});
menuPop.querySelectorAll('.menu-item').forEach(item => item.addEventListener('click', () => {
  switch (item.dataset.act) {
    case 'translate': btnT.click(); break;
    case 'vowels':    btnV.click(); break;
    case 'speed':     btnS.click(); break;
    case 'home':      appBack(); break;
  }
  syncMenu();
}));

// progress bar follows reading scroll
const scroller = document.getElementById('readingScroll');
scroller.addEventListener('scroll', () => {
  const max = scroller.scrollHeight - scroller.clientHeight;
  document.getElementById('progressFill').style.width =
    (max > 0 ? (scroller.scrollTop / max) * 100 : 0).toFixed(1) + '%';
});

// ── boot ──
setDark(state.dark);
// auto-connect to server on launch (key is hardcoded in api.js)
if (BARGE_API.ready()) {
  BARGE_API.ping().then(ok => {
    if (ok) loadStories();
  });
}
if (onboarded()) nav('scr-home');   // welcome screen shows once, ever
