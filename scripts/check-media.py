#!/usr/bin/env python3
"""Vergleicht itch.io und YouTube mit GAMES und VIDEOS in script.js.

Aufruf:  python3 scripts/check-media.py             # nur anzeigen
         python3 scripts/check-media.py --bilder    # fehlende Bilder nach img/ laden
Braucht nur Python 3 und Internet. Mit Pillow werden bei YouTube-Shorts die schwarzen Ränder abgeschnitten.
"""
import html
import re
import sys
import urllib.request
from pathlib import Path

ITCH = "https://bonbon08.itch.io/"
CHANNEL = "UCW2JjdwpyCu02wa40FsyJWQ"
MAX_VIDEOS = 6
ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as res:
        return res.read()


def save(url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(get(url))


def crop_bars(path):
    try:
        from PIL import Image
    except ImportError:
        print(f"    (Pillow fehlt – Ränder bei {path.name} nicht abgeschnitten)")
        return
    im = Image.open(path).convert("RGB")
    w, h = im.size
    cols = [x for x in range(w) if sum(sum(im.getpixel((x, y))) for y in range(0, h, 10)) / (h // 10) > 40]
    if cols and (cols[0] > 0 or cols[-1] < w - 1):
        im.crop((cols[0], 0, cols[-1] + 1, h)).save(path, quality=85)


script = (ROOT / "script.js").read_text(encoding="utf-8")
games_src = script[script.index("const GAMES"):script.index("const VIDEOS")]
videos_src = script[script.index("const VIDEOS"):script.index("const SOCIALS")]
on_site_games = re.findall(r'slug: "([^"]+)"', games_src)
on_site_videos = re.findall(r'id: "([^"]+)"', videos_src)
bilder = "--bilder" in sys.argv

# itch.io
page = get(ITCH).decode("utf-8", "replace")
games = []
for block in re.split(r'(?=<div[^>]*data-game_id=)', page)[1:]:
    m = re.search(r'<a [^>]*href="' + re.escape(ITCH) + r'([^"]+)"[^>]*class="title game_link"[^>]*>([^<]+)', block)
    if not m:
        continue
    text = re.search(r'<div [^>]*title="([^"]*)"[^>]*class="game_text"', block)
    img = re.search(r'data-lazy_src="([^"]+)"', block)
    games.append((m[1], html.unescape(m[2]), html.unescape(text[1]) if text else "", img[1] if img else None))

new_games = [g for g in games if g[0] not in on_site_games]
gone_games = sorted(set(on_site_games) - {g[0] for g in games})
print(f"NEUE Spiele auf itch.io (noch nicht in GAMES): {len(new_games)}")
for slug, title, text, img in new_games:
    print(f"  - {slug:<26} {title}  –  {text}")
    print(f"    Details: {ITCH}{slug}")
print(f"\nIn GAMES, aber nicht (mehr) auf itch.io: {len(gone_games)}")
print("\n".join(f"  - {s}" for s in gone_games) or "  –")

# YouTube
feed = get(f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL}").decode("utf-8")
videos = []
for e in re.findall(r"<entry>(.*?)</entry>", feed, re.S):
    vid = re.search(r"<yt:videoId>(.*?)<", e)[1]
    title = html.unescape(re.search(r"<title>(.*?)<", e)[1])
    date = re.search(r"<published>(.{10})", e)[1]
    short = "/shorts/" in e
    videos.append((vid, title, date, short))

# "neu" = jünger als das neueste Video, das schon auf der Seite ist
newest = max((v[2] for v in videos if v[0] in on_site_videos), default="")
new_videos = [v for v in videos if v[0] not in on_site_videos and v[2] > newest]
gone_videos = sorted(set(on_site_videos) - {v[0] for v in videos})
print(f"\nNEUE Videos auf YouTube (seit dem neuesten in VIDEOS, neueste zuerst): {len(new_videos)}")
for vid, title, date, short in new_videos:
    print(f"  - {vid}  {date}  {'Short' if short else 'Video'}  {title}")
print(f"  (VIDEOS zeigt höchstens {MAX_VIDEOS}: neue Zeichnungen vorne rein, älteste hinten raus)")
print(f"\nIn VIDEOS, aber nicht mehr im YouTube-Feed (gelöscht/privat – oder nur zu alt, Feed zeigt die letzten 15): {len(gone_videos)}")
print("\n".join(f"  - {v}" for v in gone_videos) or "  –")

# Bilder
missing = [(f"img/itch/{s}.png", img, False) for s, _, _, img in games if img and s in on_site_games]
missing += [(f"img/yt/{v}.jpg", f"https://i.ytimg.com/vi/{v}/hqdefault.jpg", True) for v in on_site_videos]
missing = [m for m in missing if not (ROOT / m[0]).exists()]
print(f"\nFEHLENDE Bilder für Einträge in script.js: {len(missing)}")
for path, url, is_yt in missing:
    if bilder:
        save(url, ROOT / path)
        if is_yt:
            crop_bars(ROOT / path)
        print(f"  - {path}  geladen")
    else:
        print(f"  - {path}  (mit --bilder laden)")
used = {f"img/itch/{s}.png" for s in on_site_games} | {f"img/yt/{v}.jpg" for v in on_site_videos}
unused = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "img").glob("*/*") if str(p.relative_to(ROOT)) not in used)
print(f"\nUNBENUTZTE Bilder in img/ (können weg): {len(unused)}")
print("\n".join(f"  - {u}" for u in unused) or "  –")
