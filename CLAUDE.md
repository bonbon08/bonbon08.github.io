# Bonbons Website

Persönliche Portfolio-Seite von bonbon08, live unter https://bonbon08.github.io
(GitHub Pages, Repo `bonbon08/bonbon08.github.io`, Branch `main`). Jeder Push auf `main` ist nach 1–2 Minuten live.

Sprache der Seite und der Antworten an den User: **Deutsch** (locker, Du-Form).

## Aufbau

- `index.html` – Gerüst und feste Texte: Hero, „Über mich“-Karten (Aktuell / Lerne / Frag mich), Spotlight (Hauptprojekt)
- `script.js` – **alle Inhalte als Daten**, ganz oben in der Datei:
  - `CATEGORIES` – Projekte nach Themen; `name` = exakter GitHub-Repo-Name (daraus wird der Link), `label` = optionaler Anzeigename, `tech`, `desc` (deutsch, 1 Satz)
  - `SOCIALS` – Accounts: `name`, `handle`, `url`, `color` (Markenfarbe), optional `rel: "me"` (Mastodon-Verifizierung)
  - `STACK` – Tech-Stack nach Gruppen
- `style.css` – Design. Hauptfarbe Blau (`--accent`), Hell/Dunkel über CSS-Variablen
- `fonts/`, `avatar.png` – lokal gehostet
- `scripts/check-repos.py` – vergleicht GitHub-Repos mit `CATEGORIES`
- `scripts/ignored-repos.txt` – Repos, die absichtlich nicht auf der Seite stehen
- `ANLEITUNG.md` – Anleitung für den Menschen

## Regeln

- **Keine externen Ressourcen** einbinden (keine Google Fonts, CDNs, Tracker, eingebettete YouTube/Instagram-Widgets). Grund: DSGVO, kein Impressum/keine Datenschutzerklärung nötig. Bilder und Schriften lokal ablegen.
- **Kein Spendenlink / keine Monetarisierung** (PayPal o. ä.) – der User hat sich bewusst dagegen entschieden, damit die Seite privat bleibt und kein Impressum braucht. Wenn er so etwas will: auf die Impressumspflicht hinweisen.
- Repo-Beschreibungen auf GitHub sind oft leer oder englisch → Beschreibung aus README, Dateien und Commits ableiten und auf Deutsch formulieren. Nichts erfinden; wenn unklar, nachfragen oder vorsichtig formulieren.
- Kein Build-Schritt, kein Framework – reines HTML/CSS/JS. Nach Änderungen an `script.js`: `node --check script.js`.
- Vor dem Push dem User kurz zeigen, was sich ändert, und erst nach seinem OK pushen.

## Update-Ablauf

Für Updates gibt es den Befehl `/website-update` (`.claude/skills/website-update/SKILL.md`).
