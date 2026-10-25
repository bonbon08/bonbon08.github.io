---
name: website-update
description: Website mit den aktuellen GitHub-Repos und Accounts von bonbon08 abgleichen und aktualisieren – neue Repos einsortieren, "Aktuell arbeite ich an" auffrischen, neue Social-Accounts eintragen, dann nach OK pushen.
---

# Website aktualisieren

Optionaler Wunsch des Users: $ARGUMENTS
(z. B. „neuer Account: TikTok @xyz“ oder „Repo X weglassen“). Wenn leer: kompletter Abgleich.

## 1. Stand holen

```bash
git pull --ff-only
python3 -I scripts/check-repos.py
```

## 2. Neue Repos

Für jedes Repo unter „NEUE Repos“ README, Dateiliste und letzte Commits ansehen:

```bash
gh api repos/bonbon08/<repo>/readme --jq .content | base64 -d
gh api repos/bonbon08/<repo>/contents --jq '.[].name'
gh api "repos/bonbon08/<repo>/commits?per_page=10" --jq '.[] | .commit.author.date[:10] + " " + .commit.message'
```

Dann entweder
- in passende Kategorie von `CATEGORIES` in `script.js` eintragen (neue Kategorie nur, wenn keine passt), deutsche Ein-Satz-Beschreibung, oder
- wenn es nur ein Test/Mini-Experiment ist: den User fragen, ob es in `scripts/ignored-repos.txt` soll.

Repos unter „nicht mehr auf GitHub“: User fragen (umbenannt → `name` anpassen, gelöscht → entfernen).

## 3. „Über mich“ und Spotlight

Die Liste „ZULETZT AKTIV“ mit den Karten in `index.html` vergleichen:
- „Aktuell arbeite ich an“ = die 2–3 aktivsten Projekte
- „Gerade lerne ich“ = neue Sprachen/Frameworks/Themen, die in diesen Repos auftauchen
- Spotlight (`<article class="spotlight">`) = das größte aktive Projekt. Beim Wechsel auch `content:` von `.spotlight::after` in `style.css` anpassen (kurzes Wort, Großbuchstaben).
- Neue Technologien in `STACK` ergänzen.

## 4. Neue Accounts

Neuen Eintrag in `SOCIALS` in `script.js`: `name`, `handle`, `url`, `color` (Markenfarbe). Link vorher mit `curl -sI <url>` prüfen, wenn möglich. Keine Widgets/Embeds einbauen, nur Links.

## 5. Prüfen und hochladen

```bash
node --check script.js
python3 -I scripts/check-repos.py   # sollte jetzt keine neuen Repos mehr zeigen
git diff --stat
```

Dem User eine kurze deutsche Liste der Änderungen zeigen. **Erst nach seinem OK:**

```bash
git add -A && git commit -m "Website-Update: <kurz was>" && git push
```

Danach ca. 1–2 Minuten warten und mit `curl -s https://bonbon08.github.io/script.js | grep <neuer Name>` prüfen, dass es live ist.
