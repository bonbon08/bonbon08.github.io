# Anleitung: Website aktualisieren

Deine Seite: **https://bonbon08.github.io**. Ordner: `/home/bonbon/webside`

Alles, was du normalerweise änderst, steht oben in **`script.js`**:

| Was                     | Wo in `script.js` |
|-------------------------|-------------------|
| Projekte / Repos        | `CATEGORIES`      |
| Spiele auf itch.io      | `GAMES` (Bild nach `img/itch/<slug>.png`) |
| Zeichen-Videos YouTube  | `VIDEOS` (Bild nach `img/yt/<id>.jpg`)    |
| Accounts (YouTube usw.) | `SOCIALS`         |
| Tech Stack              | `STACK`           |

„Über mich“ (Aktuell / Lerne / Frag mich) und das große Hauptprojekt stehen in **`index.html`**.

---

## Variante A: Mit Claude (am einfachsten)

```bash
cd ~/webside
claude
```

Dann eingeben:

```
/website-update
```

Claude holt deine Repos, itch.io-Spiele und YouTube-Zeichnungen, sortiert neue ein, frischt „Aktuell arbeite ich an“ auf,
zeigt dir die Änderungen und lädt nach deinem OK hoch.

Mit Wunsch dazu, z. B.:

```
/website-update neuer Account: Twitch twitch.tv/bonbon08
/website-update Repo Aquarium nicht mehr anzeigen
```

---

## Variante B: Von Hand

### 1. Prüfen, was sich geändert hat

```bash
cd ~/webside
python3 scripts/check-repos.py
```

Zeigt dir:
- **NEUE Repos**: noch nicht auf der Seite
- **nicht mehr auf GitHub**: gelöscht/umbenannt, also auch von der Seite nehmen
- **ZULETZT AKTIV**: gute Kandidaten für „Aktuell arbeite ich an“

Für itch.io und YouTube:

```bash
python3 scripts/check-media.py            # zeigt neue Spiele/Videos
python3 scripts/check-media.py --bilder   # lädt fehlende Bilder nach img/
```

### 2. Neues Repo eintragen

In `script.js` bei `CATEGORIES` in die passende Kategorie eine Zeile einfügen:

```js
{ name: "Repo-Name-auf-GitHub", label: "Schöner Name", tech: "C · Raylib", desc: "Was es macht, in einem Satz." },
```

- `name` muss **genau** so heißen wie das Repo auf GitHub (daraus wird der Link).
- `label` ist optional; ohne `label` wird `name` angezeigt.

Ein Repo soll **nicht** auf die Seite? Dann den Namen in `scripts/ignored-repos.txt` schreiben,
damit es nicht mehr als „neu“ gemeldet wird.

### 3. Neuen Account eintragen

In `script.js` bei `SOCIALS` eine Zeile einfügen:

```js
{ name: "Twitch", handle: "bonbon08", url: "https://twitch.tv/bonbon08", color: "#9146ff" },
```

`color` ist der farbige Streifen links (am besten die Markenfarbe der Plattform).

> Nur **Links** eintragen, keine eingebetteten Videos/Feeds/Widgets – sonst lädt die Seite
> Daten von fremden Servern (Datenschutz). Und: kein Spendenlink, sonst brauchst du ein Impressum.

### 4. Anschauen

`index.html` im Browser öffnen (oder Seite neu laden).

### 5. Hochladen

```bash
git add -A
git commit -m "Website-Update"
git push
```

Nach 1–2 Minuten ist es live. (Falls du alte Version siehst: Strg+Shift+R)
