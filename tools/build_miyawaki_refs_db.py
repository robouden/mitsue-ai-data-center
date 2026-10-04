#!/usr/bin/env python3
"""Build DuckDB of the references behind Morales et al. 2025 (Miyawaki evidence gap)
and download every open-access full text.

Data sources (Table 2 IDs 1-51) are hand-transcribed; cited refs come from the
paper's Crossref reference list. Every DOI is resolved against Crossref and
OpenAlex and the returned title/year compared with the transcribed one.
Paywalled papers are NOT downloaded; they keep a DOI / search link.
Run from repo root: python3 tools/build_miyawaki_refs_db.py [--no-download]"""
import csv, difflib, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
import duckdb

OUT = Path("research/literature/miyawaki")
PDFS = OUT / "pdfs"
PAPER_DOI = "10.1111/1365-2664.70242"
UA = {"User-Agent": "mitsue-refs-db/1.0"}

# (t2_id, authors, year, title, venue, doi, url, note)
DS = [
(1,"Aarthi, R.; Sumaiya Begum, A.; Yaswanthshahi, S.K.; Avinashreddy, Y.; Sharfuddin, S.K.",2021,"Miyawaki forest automation and unauthorized restrictions","Annals of R.S.C.B 25: 12372-12380",None,None,""),
(2,"Ahmad, A.",2022,"Green cities: Implementing the Miyawaki method in Lahore, Pakistan","The Palgrave Encyclopedia of Urban and Regional Futures (Springer)","10.1007/978-3-030-87745-3",None,"Table 2 labels this 'Ahsan 2023'; Data sources list says Ahmad 2022. DOI in paper is the book-level DOI, not the chapter."),
(3,"Akbar, M.H.; Ahmed, O.H.; Jamaluddin, A.S.; Nik, N.M.; Majid, A.; Abdul-Hamid, H.; Jusop, S.; Hassan, A.; Yusof, K.H.",2010,"Differences in soil physical and chemical properties of rehabilitated and secondary forests","American Journal of Applied Sciences 7(9): 1200-1209",None,None,""),
(4,"Bellarosa, R.; Schirone, B.; Busatto, M.",1998,"Bellarosa & Schirone, 1998 (title not given in paper)","Conference paper, pp. 47-54",None,None,"Paper gives no title or venue; needs manual search."),
(5,"Cambria, V.E.; Fratarcangeli, C.; Fanelli, G.; Cuccaro, V.C.; Panero, I.; De Sanctis, M.; Malatesta, L.; Attorre, F.",2024,"Testing the Miyawaki method in Mediterranean urban areas through a standardised experimental design","Botany 102(9): 379-386","10.1139/cjb-2024-0045",None,""),
(6,"Chaturvedi, A.; Singh, G.S.P.; Sharma, S.K.",2024,"Stabilization of mine waste dumps through bio-engineering","J. Institution of Engineers (India): Series D 105(2): 1319-1330","10.1007/s40033-023-00524-4",None,""),
(7,"Da, L.-J.; Song, Y.-C.",2008,"The construction of near-natural forests in the urban areas of Shanghai","In: Ecology, Planning, and Management of Urban Forests (Springer), pp. 420-432","10.1007/978-0-387-71425-7_26",None,""),
(8,"Daou, A.; Saliba, M.; Kallab, A.",2024,"A review of the Miyawaki method","SSRN 4728239 (preprint)","10.2139/ssrn.4728239",None,""),
(9,"Ducros, H.B.",2022,"Mini-Forest revolution: Using the Miyawaki method to rapidly rewild the world by Hannah Lewis","EuropeNow Journal 48, hal-04177291",None,"https://hal.science/hal-04177291v1/document",""),
(10,"Frattaroli, A.R.; Pirone, G.; Di Cecco, V.; Console, C.; Contu, F.; Mercurio, R.",2017,"Beech-wood restoration in the Gran Sasso and Monti della Laga National Park (central Apennines, Italy)","Plant Sociology 54(1): 11-18","10.7338/pls2017541S1/02",None,""),
(11,"Fujiwara, K.; Box, E.",2021,"Professor Akira Miyawaki (1928-2021), obituary - A life of passion and encounter with people for phytosociology and creation of native forests by the Miyawaki method","IAVS Bulletin 2021(3): 37-41","10.21570/bul-202103-12",None,""),
(12,"Gill, S.K.",2024,"Maintaining age diversity in urban forests through continuous tree planting: The potential of the Miyawaki method for urban forestry in Edmonton, AB","Master thesis, University of Alberta",None,"https://sites.ualberta.ca/~ahamann/people/pdfs/Gill_2024_MF.pdf",""),
(13,"Guo, X.F.",2018,"Effects of different forest reconstruction methods on characteristics of understory vegetation and soil quality","Applied Ecology and Environmental Research 16(6): 7501-7517","10.15666/aeer/1606_75017517",None,""),
(14,"Hanpattanakit, P.; Kongsaenkaew, P.; Pocksorn, A.; Thanajaruwittayakorn, W.; Detchairit, W.; Limsakul, A.",2022,"Estimating carbon stock in biomass and soil of young eco-Forest in Urban City, Thailand","Chemical Engineering Transactions 97: 427-432","10.3303/CET2297072",None,"Carbon stock study, no control (per Morales)."),
(15,"Kavana, G.B.",2023,"Miyawaki Forest: Technical Report","ResearchGate technical report","10.13140/RG.2.2.10680.93441",None,""),
(16,"Kiboi, S.; Fujiwara, K.; Mutiso, P.",2014,"Sustainable Management of Urban Green Environments: Challenges and opportunities","In: Sustainable Living with Environmental Risks (Springer Japan), pp. 223-236","10.1007/978-4-431-54804-1_18",None,"Table 2 labels this 'Kiboi et al. 2015'; Data sources says 2014."),
(17,"Kurian, A.L.",2020,"Urban Heat Island mitigation and Miyawaki forests: An analysis","Pollution Research 39: 186-191",None,None,""),
(18,"Mandowara, R.",2022,"Miyawaki forests","Int. J. Advanced Research in Arts, Science, Engineering & Management 9(3): 978-984",None,None,""),
(19,"Meguro, S.I.; Chalo, D.M.; Mutiso, P.B.C.",2021,"Growth characteristics of selected potential natural vegetation in Kenya: The Afromontane Forest restoration program based on the Miyawaki method","ECO-HABITAT: JISE Research 27(1): 87-94",None,None,"Published by JISE (Miyawaki's own institute) - not independent."),
(20,"Meguro, S.I.",2023,"Notes on the Miyawaki method for reforestation approach","The Malaysian Forester 86(1): 153-173",None,None,"Meguro is JISE-affiliated."),
(21,"Mihailova, M.",2022,"Micro forests as a way in EU agriculture to implement 'green policy' and create sustainable biomass","Crisis management and safety foresight in forest-based sector... pp. 257-263",None,"https://www.researchgate.net/publication/362545573",""),
(22,"Miyawaki, A.; Golley, F.B.",1993,"Forest reconstruction as ecological engineering","Ecological Engineering 2(4): 333-345","10.1016/0925-8574(93)90002-W",None,""),
(23,"Miyawaki, A.",1993,"Restoration of native forests from Japan to Malaysia","In: Lieth & Lohmann (eds), Restoration of Tropical Forest Ecosystems, Kluwer/Springer, pp. 5-24","10.1007/978-94-017-2896-6_1",None,"Original method statement (proponent)."),
(24,"Parikh, A.; Nazrana, A.",2023,"Analysis of the Miyawaki afforestation technique","Int. J. Development Research 13(10): 63913-63915","10.37118/ijdr.27255.10.2023",None,""),
(25,"Parikh, A.",2024,"Comparison of Miyawaki afforestation method with alternate afforestation models of Peepalbaba and Auroville","Int. J. Development Research 14(2): 64754-64755","10.37118/ijdr.27720.02.2024",None,""),
(26,"Poddar, S.",2021,"Miyawaki technique of afforestation","Krishi Science - eMagazine for Agricultural Sciences 2(9): KS-1743",None,"https://www.researchgate.net/publication/354656628",""),
(27,"Qi, H.; Dempsey, N.; Cameron, R.",2024,"Seeing the forest for the trees? An exploration of the Miyawaki forest method in the UK","Arboricultural Journal 46(4): 292-304","10.1080/03071375.2024.2394355",None,"Source for UK cost figures."),
(28,"Qian, X.; Liu, Z.; Zhao, T.; Bai, H.; Sun, J.; Feng, X.",2021,"Digital design exploration of nature-approximating urban Forest basing on the Miyawaki method: A case study of Xingtai Forest in a Hebei green expo garden","Landscape Architecture Frontiers 9(6): 60-76","10.15302/J-LAF-0-020015",None,"Table 2 spells 'Quian'."),
(29,"Rajadurai, P.J.",2024,"Assessing the sociological impact of the Miyawaki method on urban health and environment","Int. J. Research and Innovation in Social Science (IJRISS) 8(9): 3360-3367",None,None,"DOI truncated in paper (10.47772/IJRISS...)."),
(30,"Ranjan, V.; Sen, P.; Kumar, D.; Sarsawat, A.",2015,"A review on dump slope stabilization by revegetation with reference to indigenous plant","Ecological Processes 4(1): 14","10.1186/s13717-015-0041-1",None,""),
(31,"Ranjan, V.; Sen, P.; Kumar, D.; Singh, B.",2016,"Reclamation and rehabilitation of waste dump by eco-restoration techniques at Thakurani iron ore mines in Odisha","Int. J. Mining and Mineral Engineering 7(3): 253-264","10.1504/IJMME.2016.078372",None,""),
(32,"Ranjan, V.; Sen, P.; Kumar, D.",2017,"Dump slope stabilisation through revegetation in iron ore mines in Bonai iron ore range: A review","Int. J. Mining and Mineral Engineering 8(4): 334-351",None,None,""),
(33,"Resmi, J.; Vismaya, K.; Chitra, V.; Anjana, S.K.; Sumiya, K.V.",2024,"Green initiatives for climate change mitigation in Palakkad District of Kerala, India","Int. J. Environment and Climate Change 14(9): 768-774","10.9734/ijecc/2024/v14i94454",None,"Resmi 2024a"),
(34,"Resmi, J.; Vismaya, K.; Sumiya, K.V.",2024,"Database of Miyawaki forest unit established at KVK Palakkad: A green initiative for climate change mitigation","Journal of Krishi Vigyan 12(4): 795-801",None,None,"Resmi 2024b; DOI truncated in paper (10.5958/2349-4433.2024.00...)."),
(35,"Rochard, H.",2023,"'Plantons des micro-forets urbaines': Nouveau recit d'action publique et coproduction citoyenne d'une solution fondee sur la nature a Paris","Developpement Durable et Territoires 14(3)","10.4000/developpementdurable.23444",None,""),
(36,"Rots, A.P.",2021,"Trees of tension: Re-making nature in post-disaster Tohoku","Japan Forum 33(1): 1-24","10.1080/09555803.2019.1628087",None,"Japan-specific (Tohoku tsunami forests); Table 2 labels it 2019. Directly relevant to Japanese Miyawaki practice."),
(37,"Roy, A.; Chatterjee, N.",2023,"What happens after planting? Assessing canopy structure, vegetation cover index, and vegetation distribution of two Miyawaki forest stands in Bengaluru urban district, India","Research Square (preprint)","10.21203/rs.3.rs-2795114/v1",None,"Preprint."),
(38,"Safvan, M.V.K.; Swapna, T.S.",2023,"Assessment of biodiversity and growth parameters of Miyawaki forest of selected sites in Thiruvananthapuram district of Kerala","Research Square (preprint)","10.21203/rs.3.rs-3192725/v1",None,"Preprint. Only study quantifying biodiversity."),
(39,"Sandip, R.; Sharma, P.; Modi, N.R.",2022,"Development of tree plantation through Miyawaki method at Sabarmati riverfront development corporation limited - A research","Int. Association of Biologicals and Computational Digest 1(1): 26-38",None,None,""),
(40,"Schirone, B.; Salis, A.; Vessella, F.",2011,"Effectiveness of the Miyawaki method in Mediterranean forest restoration programs","Landscape and Ecological Engineering 7(1): 81-92","10.1007/s11355-010-0117-0",None,"Table 2 labels it 'Schrirone 2021'; year is 2011."),
(41,"Sharma, R.; Haq, A.; Bakshi, B.R.; Ramteke, M.; Kodamana, H.",2024,"Designing synergies between hybrid renewable energy systems and ecosystems developed by different afforestation approaches","Journal of Cleaner Production 434: 139804","10.1016/j.jclepro.2023.139804",None,"Relevant to energy+forest linkage."),
(42,"Singh, C.; Saini, G.",2019,"Sustainable solution for urban environment: Miyawaki Forest","IJTIMES 5(4): 1-5",None,None,""),
(43,"Sivabalan, K.C.; Krishnan, N.; Nithila, S.",2021,"NIRAM - modified Miyawaki technique for Forest creation: Case study from Trichy, Tamil Nadu state, India","JOJ Wildlife & Biodiversity 3(2): 555613","10.19080/JOJWB.2021.03.555613",None,"Table 2 spells 'Sivalan'."),
(44,"Sreelekshmi, M.; Leno, N.; Rani, B.; Gladis, R.; Shirin, K.S.A.",2024,"Spatial variability of micronutrient status in Miyawaki Forest development","Int. J. Environment and Climate Change 14(11): 503-510","10.9734/ijecc/2024/v14i114564",None,""),
(45,"Szabo, V.; Zsolnai, B.; Bajor, Z.",2021,"Preliminary data on the first year of first Hungarian Miyawaki-forest in Taban, Budapest","SGEM 21(3.2): 205-212","10.5593/sgem2021V/3.2/s14.30",None,""),
(46,"Szabo, V.; Dora, P.; Kukk, J.; Kohut, I.",2024,"Some ecological services of the first, 4-years old, Hungarian Miyawaki-forest in Taban, Budapest","SGEM 24(4.2): 217-224","10.5593/sgem2024v/4.2/s18.30",None,"Carbon stock study, no control."),
(47,"Ullah, M.A.",2023,"Awareness of Miyawaki urban Forest plantation method in Pakistan","American J. Biomedical Science & Research 18(2): 138-147","10.34297/ajbsr.2023.18.002446",None,""),
(48,"Valdes, M.",2023,"Todo Suelo Suena Con Ser Bosque. Bosko Y Sus Bosques Miyawaki Para La Ciudad","Cartografia 8: 100-107",None,None,""),
(49,"Wake, S.J.; Havell, R.",2023,"Stop the chop: A humane response to city tree loss","In: Sustainability and health (56th ANZAScA Conf.), pp. 604-618",None,None,""),
(50,"Zhang, X.; Hu, H.; Wang, X.; Tian, Q.; Zhong, X.; Shen, L.",2023,"Plant community degradation inquiry and ecological restoration design in South Lake Scenic Area of China","Forests 14(2): 181","10.3390/f14020181",None,""),
(51,"Zhao, X.; Zhao, Y.; Liu, L.",2024,"Application of digital technology in forest resource protection and monitoring management","In: Palade et al. (eds), Springer Nature Switzerland, vol. 41, pp. 95-102","10.1007/978-3-031-69457-8_9",None,""),
]

CLAIMS = [  # id, claim, level, details, mentions, empirical
("rapid_growth","Rapid growth (~10x faster)","Partial","Higher early growth vs traditional planting, but soil-prep effect not separated",[1,2,8,9,10,12,15,21,26,27,28,29,30,37,39,41,43,44,47,48,50],[7,10,15,16,19,37,38,40]),
("rapid_maturity","Rapid maturity (20-30 yr)","Null","No study evaluates maturity",[1,2,7,8,10,12,15,16,17,18,26,27,28,29,39,40,42,43,47,48],[]),
("self_sustaining","Self-sustaining after 3 yr","Null","No study evaluates it",[1,2,6,12,15,17,24,26,30,39],[]),
("cost_efficient","Cost efficient","Null","No cost study; literature suggests higher cost",[1,7,8,12,13,16,17,27,28],[]),
("biodiversity","Enhanced biodiversity","Weak","One study, no quantitative comparison",[7,9,13,15,29,30,47,48],[38]),
("carbon","Enhanced carbon sequestration","Weak","Stocks only, no long-term difference, no controls",[5,9,14,17,26,27,30,41],[14,46]),
("density","Reaches higher density","Null","No long-term density/stability studies",[1,15,26,37,39,41,43],[]),
]


def get(url, raw=False, timeout=25):
    err = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read() if raw else json.load(r)
        except Exception as e:
            err = e
            time.sleep(1.5)
    return None


def norm(s): return re.sub(r"[^a-z0-9 ]", "", re.sub(r"<[^>]+>", "", (s or "").lower().replace("-", " ")))
def sim(a, b): return round(difflib.SequenceMatcher(None, norm(a), norm(b)).ratio(), 2)
def clean_doi(d): return re.sub(r"[\u2010-\u2015\u2212]", "-", re.sub(r"[\s\u200b\u00ad]", "", d)).strip().rstrip(".") if d else None


def crossref(doi):
    j = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if not j: return {}
    m = j["message"]
    au = "; ".join(f"{a.get('family','')}, {a.get('given','')}" for a in m.get("author", []))
    yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
    return dict(cr_title=(m.get("title") or [""])[0], cr_year=yr, cr_venue=(m.get("container-title") or [""])[0], cr_authors=au, cr_type=m.get("type"))


def openalex(doi):
    j = get("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi))
    if not j: return {}
    oa = j.get("open_access") or {}
    best = j.get("best_oa_location") or {}
    return dict(oa_url=best.get("pdf_url") or oa.get("oa_url"), landing_url=best.get("landing_page_url"),
                is_oa=bool(oa.get("is_oa")), cited_by=j.get("cited_by_count"), openalex_id=j.get("id"))


def find_doi(title, authors):
    q = urllib.parse.quote(f"{title} {authors.split(',')[0]}")
    j = get(f"https://api.crossref.org/works?query.bibliographic={q}&rows=1&select=DOI,title")
    try: it = j["message"]["items"][0]
    except Exception: return None, 0
    return it["DOI"], sim(title, (it.get("title") or [""])[0])


def download(r):
    """Fetch open-access full text. Only keeps real PDFs (%PDF magic)."""
    for u in dict.fromkeys(x for x in (r.get("oa_url"), r.get("url"), r.get("landing_url")) if x):
        data = get(u, raw=True, timeout=60)
        if data and data[:5] != b"%PDF-":  # HTML landing page: follow citation_pdf_url meta tag
            m = re.search(rb'citation_pdf_url"\s+content="([^"]+)"|content="([^"]+)"\s+name="citation_pdf_url', data)
            if m:
                data = get(urllib.parse.urljoin(u, (m.group(1) or m.group(2)).decode()), raw=True, timeout=60)
        if data and data[:5] == b"%PDF-" and len(data) < 80_000_000:
            tag = (r["t2_id"] and f"ds{r['t2_id']:02d}") or f"c{r['ref_id']:03d}"
            sur = re.sub(r"[^A-Za-z]", "", (r["authors"] or "anon").split(",")[0].split()[0] if r["authors"] else "anon")
            p = PDFS / f"{tag}_{sur}_{r['year']}.pdf"
            p.write_bytes(data)
            return str(p), "downloaded_pdf", u
    return None, ("oa_link_not_pdf" if r.get("oa_url") else "paywalled_or_no_oa"), None


def main(dl=True):
    OUT.mkdir(parents=True, exist_ok=True); PDFS.mkdir(exist_ok=True)
    cr = get("https://api.crossref.org/works/" + PAPER_DOI)["message"]
    rows = [dict(role="data_source", t2_id=t2, authors=au, year=yr, title=ti, venue=ve, doi=doi, url=url, note=note)
            for t2, au, yr, ti, ve, doi, url, note in DS]
    have = {r["doi"].lower() for r in rows if r["doi"]}
    for x in cr.get("reference", []):
        d = clean_doi(x.get("DOI"))
        if d and d.lower() in have: continue
        if d: have.add(d.lower())
        title = x.get("article-title") or x.get("volume-title") or x.get("unstructured") or ""
        sur = (x.get("author") or "").split(",")[0].split()[0].lower() if x.get("author") else ""
        if not d and any(sur and sur[:5] in norm(r["authors"]) and str(r["year"]) == str(x.get("year")) for r in rows if r["role"] == "data_source"): continue
        rows.append(dict(role="cited", t2_id=None, authors=x.get("author"), year=int(x["year"]) if str(x.get("year", "")).isdigit() else None,
                         title=title, venue=x.get("journal-title") or x.get("series-title") or "", doi=d, url=None, note=""))
    for i, r in enumerate(rows, 1):
        r["ref_id"] = i
        r.update(cr_title=None, cr_year=None, cr_venue=None, cr_authors=None, cr_type=None, oa_url=None, landing_url=None,
                 is_oa=None, cited_by=None, openalex_id=None, title_sim=None, status="no_doi", candidate_doi=None)
        if r["doi"]:
            r.update(crossref(r["doi"])); r.update(openalex(r["doi"]))
            if r["cr_title"]:
                r["title_sim"] = sim(r["title"], r["cr_title"]) if r["title"] else None
                ok_year = r["year"] is None or r["cr_year"] is None or abs(int(r["year"]) - int(r["cr_year"])) <= 1
                r["status"] = "doi_verified" if (r["title_sim"] is None or r["title_sim"] >= 0.8) and ok_year else "doi_mismatch_CHECK"
                if r["role"] == "cited" and not r["title"]:
                    r["title"] = r["cr_title"]; r["authors"] = r["authors"] or r["cr_authors"]; r["venue"] = r["venue"] or r["cr_venue"]; r["year"] = r["year"] or r["cr_year"]
            else:
                r["status"] = "doi_unresolved_CHECK"
        elif r["role"] == "data_source" and len(r["title"]) > 25:
            d, s = find_doi(r["title"], r["authors"])
            if d and s >= 0.85: r["candidate_doi"] = d; r["status"] = "candidate_doi_found_CHECK"
        q = urllib.parse.quote(f'{r["title"] or ""} {(r["authors"] or "").split(",")[0]}')
        r["scholar_url"] = "https://scholar.google.com/scholar?q=" + q
        r["doi_url"] = ("https://doi.org/" + r["doi"]) if r["doi"] else (("https://doi.org/" + r["candidate_doi"]) if r["candidate_doi"] else None)
        r["best_link"] = r["oa_url"] or r["doi_url"] or r["url"] or r["scholar_url"]
        r["pdf_path"], r["download_status"], r["downloaded_from"] = (None, "skipped", None)
        if dl:
            r["pdf_path"], r["download_status"], r["downloaded_from"] = download(r)
        print(f"{i:3d} {r['status']:26s} {r['download_status']:20s} {(r['title'] or '')[:60]}", flush=True)
        time.sleep(0.15)

    cols = ["ref_id", "role", "t2_id", "authors", "year", "title", "venue", "doi", "url", "doi_url", "oa_url", "is_oa", "best_link",
            "scholar_url", "candidate_doi", "status", "title_sim", "cr_title", "cr_year", "cr_venue", "cr_type", "cited_by",
            "openalex_id", "pdf_path", "download_status", "downloaded_from", "note"]
    db = OUT / "miyawaki_refs.duckdb"
    if db.exists(): db.unlink()
    c = duckdb.connect(str(db))
    c.execute("CREATE TABLE refs(ref_id INTEGER PRIMARY KEY, role VARCHAR, t2_id INTEGER, authors VARCHAR, year INTEGER, title VARCHAR, venue VARCHAR,"
              "doi VARCHAR, url VARCHAR, doi_url VARCHAR, oa_url VARCHAR, is_oa BOOLEAN, best_link VARCHAR, scholar_url VARCHAR, candidate_doi VARCHAR,"
              "status VARCHAR, title_sim DOUBLE, cr_title VARCHAR, cr_year INTEGER, cr_venue VARCHAR, cr_type VARCHAR, cited_by INTEGER, openalex_id VARCHAR,"
              "pdf_path VARCHAR, download_status VARCHAR, downloaded_from VARCHAR, note VARCHAR, verified_by_human VARCHAR, human_notes VARCHAR)")
    for r in rows:
        c.execute(f"INSERT INTO refs({','.join(cols)}) VALUES({','.join('?' * len(cols))})", [r[k] for k in cols])
    c.execute("CREATE TABLE claims(claim_id VARCHAR PRIMARY KEY, claim VARCHAR, evidence_level VARCHAR, details VARCHAR)")
    c.execute("CREATE TABLE claim_refs(claim_id VARCHAR, t2_id INTEGER, relation VARCHAR)")
    for cid, cl, lv, de, me, em in CLAIMS:
        c.execute("INSERT INTO claims VALUES(?,?,?,?)", (cid, cl, lv, de))
        c.executemany("INSERT INTO claim_refs VALUES(?,?,?)", [(cid, i, "mentions_claim") for i in me] + [(cid, i, "empirical_data") for i in em])
    c.execute("CREATE TABLE source_paper(doi VARCHAR, citation VARCHAR, pdf_path VARCHAR, notes VARCHAR)")
    c.execute("INSERT INTO source_paper VALUES(?,?,?,?)", (PAPER_DOI, "Morales, Fernandez, Duran, Craven (2026) J Appl Ecol 63:e70242",
              "docs/energy-forest/misc/Journal of Applied Ecology - 2025 - Morales - Tiny forests huge claims The evidence gap behind the Miyawaki method for.pdf",
              "Supporting Tables S1-S3 (search string, controlled studies, full 51-doc list) are NOT in the PDF - get from publisher page"))
    c.execute("CREATE VIEW v_claim_evidence AS SELECT cl.claim, cl.evidence_level, cr.relation, r.t2_id, r.authors, r.year, r.title, r.best_link, r.status, r.pdf_path "
              "FROM claims cl JOIN claim_refs cr USING(claim_id) JOIN refs r ON r.t2_id = cr.t2_id AND r.role = 'data_source'")
    c.execute(f"COPY refs TO '{OUT / 'miyawaki_refs.csv'}' (HEADER, DELIMITER ',')")
    print(c.execute("SELECT role, status, download_status, count(*) FROM refs GROUP BY ALL ORDER BY ALL").fetchall())
    c.close()


if __name__ == "__main__":
    main(dl="--no-download" not in sys.argv)
