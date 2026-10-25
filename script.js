const GH = "https://github.com/bonbon08/";

// Projekte nach Themen sortiert
const CATEGORIES = [
  {
    icon: "🎮",
    title: "Games & Simulation",
    text: "Spiele und kleine Engines, inzwischen meistens in C mit Raylib.",
    projects: [
      { name: "testgame_raylib", label: "Jump-Game", tech: "C · Raylib · Android", desc: "Arcade-Jumper mit Live-Chiptune-Musik, Shop und Twitch-Plays-Modus." },
      { name: "Farm-game", label: "Farmi", tech: "C · Raylib", desc: "Couch-Coop-Farmspiel für 2 Spieler mit Quests, Shop und Tag/Nacht-Zyklus. Entstanden auf der Zugfahrt zum 39C3." },
      { name: "Aquarium", tech: "C", desc: "Ein kleines Aquarium mit zufällig generierten, bunten Fischen." },
      { name: "simple_2d_physikcsengine", label: "2D-Physik-Engine", tech: "Python", desc: "Eine simple 2D-Physik-Engine." },
      { name: "simple_game", label: "Simple Game", tech: "Python · Pygame", desc: "Ein einfaches Spiel in Pygame." },
    ],
  },
  {
    icon: "🧠",
    title: "CPUs & Emulatoren",
    text: "Verstehen, wie Prozessoren unter der Haube funktionieren.",
    projects: [
      { name: "Johnny_C", label: "Johnny in C", tech: "C · ncurses", desc: "Simulator für die Johnny-Lehr-CPU, mit Mikrocode, Makrobefehlen und TUI." },
      { name: "AX10", tech: "Python", desc: "Emulator für meine eigene virtuelle CPU." },
      { name: "AX10-display", label: "AX10 Display", tech: "Python", desc: "Display-Client als Bildschirm für den AX10-Emulator." },
    ],
  },
  {
    icon: "📱",
    title: "Apps & Tools",
    text: "Programme, die ich selbst gebraucht habe.",
    projects: [
      { name: "Android_Jelly_Domscroll", label: "Jellyreels", tech: "Flutter · Dart", desc: "Reels-artiges Scrollen durch Videos mit vorgeladenem Player-Pool und 2×-Speed." },
      { name: "stitching_template", label: "Stitch Canvas Generator", tech: "Python", desc: "Macht aus Bildern 3D-druckbare Stick-Vorlagen als STL, mit 3D-Vorschau und PKGBUILD für Arch." },
      { name: "alpaka.problem", tech: "Web", desc: "Generiert Probleme, weil ich selbst nicht genug habe." },
      { name: "BonEncryptor", tech: "Python", desc: "Verschlüsselungsprogramm mit GUI (tkinter + PyCryptodome)." },
      { name: "SDCreator", tech: "Python", desc: "Erstellt .desktop-Dateien für Linux." },
    ],
  },
  {
    icon: "🖼️",
    title: "Grafik & eigene Formate",
    text: "Eigene Bild- und Videoformate und alles, was man damit anstellen kann.",
    projects: [
      { name: "NPF", tech: "Rust", desc: "Neat Picture Format, mein eigenes Bildformat, inzwischen binär." },
      { name: "npf-picture-viewer", tech: "Rust", desc: "Viewer für NPF-Bilder." },
      { name: "pixelflutclient", tech: "Rust", desc: "Pixelflut-Client, der NPF-Bilder auf die Wand schießt." },
      { name: "SMF-Viewer", tech: "Rust", desc: "Viewer für SMF, ein Format für einfarbige 8×8-Matrix-Videos." },
      { name: "GfxSrc", tech: "Rust", desc: "Grafik-Library für Programme in der Kommandozeile." },
      { name: "isotmetric_world_renderer", label: "Isometric World Renderer", tech: "Python", desc: "Rendert isometrische Welten." },
    ],
  },
  {
    icon: "🔌",
    title: "Hardware",
    text: "Mikrocontroller, Displays und Kram, der blinkt.",
    projects: [
      { name: "Display_Server_ESP8266", label: "Display Server ESP8266", tech: "C++", desc: "Firmware für einen ESP8266 mit LCD, der Inhalte übers Netzwerk empfängt." },
      { name: "resource_sender", tech: "Rust", desc: "Schickt die PC-Auslastung live an das ESP8266-Display." },
      { name: "Esp-01s-minisystem", label: "ESP-01S Minisystem", tech: "C++", desc: "Ein kleines Testsystem für den ESP-01S." },
    ],
  },
  {
    icon: "📚",
    title: "Libraries",
    text: "Bausteine für andere Projekte.",
    projects: [
      { name: "compr_lib", tech: "Rust", desc: "Library für Dateikompression." },
      { name: "SiRandL", tech: "Rust", desc: "Eine simple Random-Library." },
    ],
  },
];

// Accounts im Bereich "Socials" – Reihenfolge = Anzeige-Reihenfolge, color = Farbstreifen links
const SOCIALS = [
  { name: "YouTube", handle: "@bonbon-v1x", url: "https://youtube.com/@bonbon-v1x", color: "#ff0000" },
  { name: "Instagram", handle: "@bonbonv1x", url: "https://instagram.com/bonbonv1x", color: "#e4405f" },
  { name: "GitHub", handle: "bonbon08", url: "https://github.com/bonbon08", color: "#3d8bff" },
  { name: "itch.io", handle: "bonbon08", url: "https://bonbon08.itch.io/", color: "#fa5c5c" },
  { name: "Mastodon", handle: "@bonbon08@mastodontech.de", url: "https://mastodontech.de/@bonbon08", color: "#6364ff", rel: "me" },
];

const STACK = {
  Sprachen: ["C", "Rust", "Python", "Dart", "NASM / Assembly"],
  Frameworks: ["Raylib", "Flutter", "ncurses", "Pygame", "Flask", "SQLite"],
  Hardware: ["Arduino", "Raspberry Pi", "ESP8266"],
  Server: ["Nginx", "Docker", "Gitea", "Jellyfin", "Pi-Hole", "Tor"],
  Grafik: ["Aseprite", "GIMP", "Krita"],
  System: ["Arch Linux", "XFCE", "CMake", "Android"],
};

const $ = (sel) => document.querySelector(sel);

function renderCategories() {
  $("#categories").innerHTML = CATEGORIES.map((c) => `
    <section class="category">
      <header class="category__head">
        <span class="category__icon">${c.icon}</span>
        <div>
          <h3>${c.title}</h3>
          <p>${c.text}</p>
        </div>
      </header>
      <div class="category__grid">
        ${c.projects.map((p) => `
          <a class="project" href="${GH}${p.name}" target="_blank" rel="noopener">
            <span class="project__name">${p.label || p.name}</span>
            <span class="project__desc">${p.desc}</span>
            <span class="project__tech">${p.tech}</span>
          </a>`).join("")}
      </div>
    </section>`).join("");
}

function renderSocials() {
  $("#socials-list").innerHTML = SOCIALS.map((a) => `
    <a class="social" style="--c:${a.color}" href="${a.url}" target="_blank" rel="${a.rel ? a.rel + " " : ""}noopener">
      <span class="social__name">${a.name}</span><span class="social__handle">${a.handle}</span>
    </a>`).join("");
}

function renderStack() {
  $("#stackList").innerHTML = Object.entries(STACK).map(([group, items]) => `
    <div class="stack__group">
      <h3>${group}</h3>
      <div class="stack__items">${items.map((i) => `<span class="chip">${i}</span>`).join("")}</div>
    </div>`).join("");
}

function initTheme() {
  const root = document.documentElement;
  try {
    const saved = localStorage.getItem("theme");
    if (saved) root.dataset.theme = saved;
  } catch {}
  $("#themeToggle").addEventListener("click", () => {
    const current = root.dataset.theme || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
    root.dataset.theme = current === "light" ? "dark" : "light";
    try { localStorage.setItem("theme", root.dataset.theme); } catch {}
  });
}

$("#year").textContent = new Date().getFullYear();
initTheme();
renderCategories();
renderSocials();
renderStack();
