import json, os, re, urllib.parse, urllib.request, sys

OUT = os.path.join(os.path.dirname(__file__), "guidepics")
os.makedirs(OUT, exist_ok=True)
UA = "MitsueTreeSurvey/1.0 (educational village tree guide; contact oudendijk.biz@gmail.com)"

# species_key -> wikipedia title (Latin, English wiki)
SP = [
    ("japanese-beech", "Fagus crenata"),
    ("mizunara-oak", "Quercus crispula"),
    ("konara-oak", "Quercus serrata"),
    ("sawtooth-oak", "Quercus acutissima"),
    ("horse-chestnut", "Aesculus turbinata"),
    ("japanese-nutmeg-yew", "Torreya nucifera"),
    ("wild-mountain-cherry", "Prunus jamasakura"),
    ("japanese-maple", "Acer palmatum"),
    ("bigleaf-magnolia", "Magnolia obovata"),
    ("japanese-zelkova", "Zelkova serrata"),
    ("japanese-chestnut", "Castanea crenata"),
    ("katsura", "Cercidiphyllum japonicum"),
]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=30).read()

def summary_image(title):
    t = urllib.parse.quote(title.replace(" ", "_"))
    j = json.loads(get("https://en.wikipedia.org/api/rest_v1/page/summary/" + t))
    src = (j.get("originalimage") or {}).get("source") or (j.get("thumbnail") or {}).get("source")
    return src

def file_title_from_url(src):
    # .../commons/a/ab/Some_Name.jpg  or .../thumb/a/ab/Some_Name.jpg/320px-Some_Name.jpg
    m = re.search(r"/commons/(?:thumb/)?[0-9a-f]/[0-9a-f]{2}/([^/]+)", src)
    if not m:
        return None
    return "File:" + urllib.parse.unquote(m.group(1))

def commons_info(file_title):
    q = ("https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo"
         "&iiprop=url|extmetadata&iiurlwidth=1000&titles=" + urllib.parse.quote(file_title))
    j = json.loads(get(q))
    pages = j["query"]["pages"]
    page = next(iter(pages.values()))
    ii = page["imageinfo"][0]
    md = ii.get("extmetadata", {})
    def f(k): return re.sub("<[^>]+>", "", (md.get(k, {}) or {}).get("value", "") or "").strip()
    return {
        "url": ii.get("thumburl") or ii.get("url"),
        "artist": f("Artist"),
        "license": f("LicenseShortName"),
        "credit": f("Credit"),
    }

manifest = {}
for key, title in SP:
    try:
        src = summary_image(title)
        if not src:
            print("NO IMAGE:", key, title); continue
        ft = file_title_from_url(src)
        info = commons_info(ft) if ft else {"url": src, "artist": "", "license": "", "credit": ""}
        data = get(info["url"])
        ext = ".jpg"
        path = os.path.join(OUT, key + ext)
        open(path, "wb").write(data)
        manifest[key] = {"file": key + ext, "title": title, "fileTitle": ft,
                         "artist": info["artist"], "license": info["license"],
                         "bytes": len(data)}
        print(f"OK {key:22} {len(data)//1024:5}KB  {info['license']}  {info['artist'][:40]}")
    except Exception as e:
        print("FAIL:", key, title, "->", repr(e))

json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w"), ensure_ascii=False, indent=2)
print("\nGot", len(manifest), "/", len(SP))
