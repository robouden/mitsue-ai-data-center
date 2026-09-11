--
-- PostgreSQL database dump
--

\restrict tVPz9o0k32CkFdMgOMhYNfkV79a7vDgls3CDyvZpfcJRewYjiK3CSDaVXodFs8A

-- Dumped from database version 18.6 (Ubuntu 18.6-1.pgdg24.04+2)
-- Dumped by pg_dump version 18.6 (Ubuntu 18.6-1.pgdg24.04+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: outreach; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.outreach (
    id integer NOT NULL,
    sent_date text DEFAULT ''::text NOT NULL,
    contact text DEFAULT ''::text NOT NULL,
    channel text DEFAULT ''::text NOT NULL,
    subject text DEFAULT ''::text NOT NULL,
    status text DEFAULT ''::text NOT NULL,
    doc_path text DEFAULT ''::text NOT NULL,
    note text DEFAULT ''::text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now() NOT NULL,
    due_date text DEFAULT ''::text NOT NULL
);


--
-- Name: outreach_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.outreach ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.outreach_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: people; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.people (
    id integer NOT NULL,
    name text NOT NULL,
    kanji text DEFAULT ''::text,
    category text NOT NULL,
    role text DEFAULT ''::text,
    org text DEFAULT ''::text,
    phone text DEFAULT ''::text,
    email text DEFAULT ''::text,
    website text DEFAULT ''::text,
    last_date text DEFAULT ''::text,
    last_note text DEFAULT ''::text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);


--
-- Name: people_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.people_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: people_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.people_id_seq OWNED BY public.people.id;


--
-- Name: people id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.people ALTER COLUMN id SET DEFAULT nextval('public.people_id_seq'::regclass);


--
-- Data for Name: outreach; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.outreach (id, sent_date, contact, channel, subject, status, doc_path, note, created_at, updated_at, due_date) FROM stdin;
2	2026-08-28	御杖村 古谷 (Furutani)	Email reply	Thanks for disclosure-doc meeting	Sent			2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
3	2026-08-26	Komatsu (コマツ) forestry equipment	Email	CTL equipment trial-site inquiry	Sent			2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
4	2026-08-20	奈良県フォレスターアカデミー	Email	Confirmation re: form submission follow-up	Sent	docs/outreach/mitsue_email_forester_academy_request.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
5	2026-08-14	Miyagawa Forest Cooperative	Email	Partnership intro (updated)	Sent — verify	docs/outreach/mitsue_email_miyagawa_shinrin_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
6	2026-08-06	Fujitex	Email	Chipper RFQ	Sent — verify	docs/outreach/mitsue_email_fujitex_chipper_rfq.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
7	2026-08-06	(chipper vendors, general)	Form drafts	Chipper RFQ	Drafted — verify if sent	docs/outreach/mitsue_chipper_rfq_form_drafts.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
8	2026-08-06	more trees	Email	Aug 5 meeting followup	Sent — verify	docs/outreach/mitsue_email_moretrees_aug5_followup.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
9	2026-08-05	Mizuho (上坂奈央)	Email	Aug 5 meeting followup + deck	Drafted, not sent	docs/outreach/mitsue_email_mizuho_nao_aug5_followup.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
10	2026-07-24	御杖村 Kinjo	Physical note	Forester Academy note	Delivered in person	docs/outreach/mitsue_note_kinjo_forester_academy.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
11	2026-07-24	NAIST Kubo	Email	Introduction	Sent — verify	docs/outreach/mitsue_email_naist_kubo_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
12	2026-07-24	Dome (via Forester Academy)	Email	Introduction	Sent — verify	docs/outreach/mitsue_email_dome_forester_academy_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
13	2026-07-21	奈良県フォレスターアカデミー	PDF + email	Recruitment summary A4	Sent — verify	docs/outreach/mitsue_forester_academy_recruit_summary_a4.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
14	2026-07-21	Swissnex (Joutet)	Email	Introduction	Sent — verify	docs/outreach/mitsue_email_swissnex_joutet_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
15	2026-07-21	NAIST Shiozaki	Email	Introduction	Sent — verify	docs/outreach/mitsue_email_naist_shiozaki_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
16	2026-07-09	more trees	Email + PDF	Partnership introduction	Sent	docs/outreach/mitsue_email_moretrees_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
17	2026-07-09	Miyagawa Forest Cooperative	Email + PDF	Introduction	Sent	docs/outreach/mitsue_email_miyagawa_shinrin_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
18	2026-07-08	Pellegrom	Letter + PDF	Support request	Sent	docs/outreach/mitsue_letter_pellegrom_support_request.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
19	2026-07-06	more trees	Email	General outreach	Sent — verify	docs/outreach/more-trees outreach email.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
20	2026-07-06	Biomass site visit contacts	Email(s)	Visit request	Sent — verify	docs/outreach/mitsue_biomass_visit_request_emails.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
21	2026-06-21	Quantum Mesh (JP)	Email/PDF draft	Outreach intro	Drafted — status unclear	docs/outreach/mitsue_quantum_mesh_outreach_jp.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
22	2026-06-21	Quantum Mesh (EN)	Email/PDF draft	Outreach intro	Drafted — status unclear	docs/outreach/mitsue_quantum_mesh_outreach.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
23	2026-08-31	HIGHRESO	Email/PDF draft	Bilingual intro (Joi Ito referral)	Held — need named contact first	docs/outreach/mitsue_email_highreso_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
24	2026-08-31	Quantum Mesh	Email/PDF draft	Intro (revised)	Held — pending Rob's consult	docs/outreach/mitsue_email_quantummesh_intro.md		2026-08-31 18:00:10.676585+09	2026-08-31 18:00:10.676585+09	
1	2026-08-31	GX地域共創補助金事務局 (METI)	Web form	Mesh-model / multi-site eligibility inquiry	Replied — mesh conditionally eligible		Receipt #00001785. Reply 2026-09-01: (1) mesh/multi-site OK if truly integrated as one project, min-investment checked on combined eligible costs, must NOT just sum independent investments — plan must explain each site role/function. (2) out-of-Nara power sites (e.g. Mie) still must satisfy siting/power reqs pp.11-13; using Nara power alone does not qualify an out-of-pref site — must justify power-source-prefecture relationship per site. Case-by-case on final submission. Auto-reply address, no direct reply possible — new Qs via web form only.	2026-08-31 18:00:10.676585+09	2026-09-01 11:57:53.678783+09	2026-11-30
25	2026-09-01	more trees (Kishi)	Email	Re: Mitsue CHP/FIT and forest management — financials/sequencing	Sent — reply to Kishi		Kishi replied 2026-09-01 (delayed): supports CHP/AI-DC concept but wants numeric revenue/jobs/village-benefit estimates; thinks reforestation should follow DC/CHP plans, not precede them; asked what info to share on his own app (suggested GitHub repo); will try trees.mitsue.it with his son. Rob replied same day: agreed with sequencing view, was upfront nothing is funded/committed yet, offered written estimate once numbers firm up, told him GitHub repo is enough for the app. Owe Kishi a real revenue/jobs/benefit estimate once financials firm up — do not overstate the ¥192M pipeline as raised/committed.	2026-09-01 11:58:04.901926+09	2026-09-01 11:58:04.901926+09	
26	2026-09-03	NIES Fukushima (Togawa Takuya / Nakamura Shogo)	Web contact form	Mishima Town <50kWe biomass CHP — maker/costs inquiry	Sent — awaiting reply		Referencing their 2020 paper (土木学会論文集G) on Mishima Town's small woody-biomass CHP pilot, our only empirically-grounded biomass-CHP data anchor. Asked: equipment maker/model, initial capex, annual fuel/running costs, operational track record. Sent ahead of Henry (biomass vendor advisor) meeting 2026-09-04. If no reply in ~2 weeks, follow up via Ooba Makoto (now at Tohoku Institute of Technology) as backup academic contact.	2026-09-03 23:44:33.371027+09	2026-09-03 23:44:33.371027+09	
27	2026-09-06	Yamaguchi Yoshiyuki (山口義行) via 御杖村むらづくり振興課	Village web inquiry form	Introduction request re: forestry/reforestation collaboration	Sent - awaiting reply		Asked むらづくり振興課 to pass along an introduction request to 地域おこし協力隊員 山口義行 (self-employed forestry practitioner, ex-steel craftsman, focused on forest degradation). Form: https://www.vill.mitsue.nara.jp/cgi-bin/inquiry.php/2?page_no=813	2026-09-06 13:49:00.606262+09	2026-09-06 13:49:00.606262+09	
28	2026-09-08	Komatsu Forest (コマツフォレスト), FMB inquiry line	Email (Japanese only)	CTL trial-site follow-up — clear-cut/reforest scale-up + training-ground pitch	Sent - awaiting reply	docs/outreach/mitsue_email_komatsu_ctl_followup.md	Follow-up to unanswered 2026-08-26 inquiry (sent to generic Corp Comms mailbox). Redirected to Komatsu Forest business-line address JP00MB_FMB_toiawase@global.komatsu. Sent from rob@mitsue.it, Japanese text only (EN version kept as reference, not sent). Framing: CHP+AI DC needs harvest volume beyond current levels; workforce shortage (not land) is the bottleneck CTL mechanization solves; plan is clear-cut aging sugi + native broadleaf reforestation, not thinning; pitched Mitsue as a CTL operator training ground (benefit framing for Komatsu, not just a favor to us). Contingency drafted if no reply: phone script for Corp Comms number, then escalate to Komatsu Forest AB Sweden (info@komatsuforest.com).	2026-09-08 00:35:51.266115+09	2026-09-08 00:35:51.266115+09	
29	2026-09-08	バイオマスパワーテクノロジーズ株式会社 (BPT, Matsusaka, Mie)	Email (bpt-shared@bpt.co.jp)	木質バイオマス発電所 見学のお願い（奈良県・御杖村の森林エネルギー事業）	Sent - awaiting reply	docs/outreach/mitsue_email_bpt_matsusaka_visit_request.md	Request to visit BPT's 2MW-class Matsusaka biomass plant (Takuma equipment) for operational/logistics reference (fuel sourcing, grid connection, O&M); BPT has a Gojo (Nara) office used as local-connection hook.	2026-09-08 16:42:05.926916+09	2026-09-08 16:42:05.926916+09	
30	2026-09-11	Akagi Yasuaki (NEDO) — via tsc-unit-2024@ml.nedo.go.jp	email	Follow-up after SwissNex Expo 2025 meeting	sent		Could not find more direct info on Akagi; emailed the NEDO Sustainable Energy Unit shared mailbox instead of his personal email.	2026-09-11 16:27:05.625706+09	2026-09-11 16:27:05.625706+09	
31	2026-09-11	Akagi Yasuaki (NEDO) — direct, akagiysa@nedo.go.jp	email	Follow-up after SwissNex Expo event	sent		Sent directly to his personal NEDO address (Rob confirmed sent, in Gmail Sent folder but not found via MCP Gmail search this session — possibly different account/client).	2026-09-11 16:28:26.369859+09	2026-09-11 16:28:26.369859+09	
\.


--
-- Data for Name: people; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.people (id, name, kanji, category, role, org, phone, email, website, last_date, last_note, created_at, updated_at) FROM stdin;
1	Rob Oudendijk	\N	Core Team	Founder & Project Lead	YR-Design	080-2260-5966	oudendijk.biz@gmail.com	\N	2026-08-06	Ongoing — daily project work	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
2	Yuka Hayashi	石村ゆか	Core Team	Colleague / co-presenter	\N	\N	yuuka1213@hotmail.com	\N	2026-07-29	Sugano Organic meeting	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
3	San Poisson	\N	Core Team	Project Manager	\N	\N	sanpoisson@gmail.com	\N	2026-07-29	Sugano Organic meeting	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
4	Takuo Dome	堂目卓生	Advisor	Specially Appointed Professor, Osaka Univ.	Rep. Director, 一般社団法人いのち会議	\N	t-dome@econ.osaka-u.ac.jp	\N	2026-08-06	Forester Academy endorsement finalized & submitted	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
5	Ray Ozzie	\N	Advisor	Creator of Lotus Notes; former Microsoft CSA	\N	\N	\N	\N	2026-05-05	Confirmed as advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
7	Evin Zoet	\N	Advisor	Co-Representative Director	Transom	\N	elvinzoet@transom.jp	\N	2026-06-16	Confirmed as advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
8	Yoshiko Zoet-Suzuki	\N	Advisor	Co-Representative Director	Transom	\N	yoshikozoetsuzuki@transom.jp	\N	2026-06-16	Confirmed as advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
9	Yuko Koshiba	\N	Advisor	Philanthropy Advisor	PA-Inc	\N	yuko.koshiba@philanthropy-advisors.jp	\N	2026-07-20	3 questions + 公益法人 support offer outstanding	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
10	Takahisa Watanabe	渡邉貴久	Advisor	Managing Associate — Legal Advisor	Linklaters Tokyo	\N	takahisa.watanabe@linklaters.com	\N	2026-07-24	Confirmed pro bono support; advised keeping entity structure open in Phase 0	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
11	Yuji Nakano	中野雄司	Advisor	Attorney — Legal Advisor	TMI Associates	\N	Yuji_Nakano@tmi.gr.jp	\N	2026-06-14	Confirmed pro bono support; sent entity-structure (NPO/一般社団法人) comparison	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
12	Sotaro Hotta	堀田総太郎	Advisor	Attorney — Legal Advisor	Likely Nishimura & Asahi (unconfirmed)	\N	\N	\N	2026-07-08	Confirmed pro bono support	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
13	Karsten Klein	\N	Advisor	CEO & Founder — AI data centre consultant (AI governance/ISO 42001, cybersecurity/ISO 27001, data privacy/GDPR)	KLEIN K.K., Advisory Services Japan	\N	\N	https://www.kleinkk.co.jp/	2026-08-18	First online meeting; discussed how the AI data center should be run: hardware, software, layers, security	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
16	Niwa-san	丹羽	Local Partner	Fuel-supply partner (sawmill)	丹羽製材, Sugano	\N	\N	\N	2026-07-29	Joint fuel-chipper discussion ongoing	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
17	Kawakita Yasunori	川北康則	Local Contact	Retired Principal	Mitsue Elementary School	\N	\N	\N	2026-06-16	Approved the Kaya poem	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
18	Nishimura Yuki	西村	Local Contact	Local contact ("Carp guy from Mitsue")	\N	\N	nishimura2099@gmail.com	\N	2026-05-06	Project Q&A exchange	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
20	Furutani Masatoshi	古谷匡敏	Government	Village Hall staff	御杖村役場	\N	t-furutani@vill.mitsue.lg.jp	\N	2026-07-13	Handled information disclosure request	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
21	Ito Shugi	伊藤収宜	Government	Mayor	御杖村 (Mitsue Village)	\N	\N	\N	2026-06-01	On record re: forestry workforce shortage (council minutes)	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
22	Mizutani Shinkichi	水谷伸吉	Partner Org	事務局長 (Secretary-General)	more trees	\N	\N	\N	2026-07-14	Key decision-maker; Miyazaki reports to him	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
23	Kishi	岸	Partner Org	Staff	more trees	\N	kishi@more-trees.org	\N	2026-08-05	Live thread — reply owed	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
24	Miyazaki	宮﨑	Partner Org	Staff	more trees	\N	miyazaki@more-trees.org	\N	2026-08-05	Live thread — reply owed	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
25	Michael Goldberg	\N	Partner Org	Thread participant	more trees	\N	ivw@gol.com	\N	2026-07-24	CC'd on live more trees thread	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
26	Kaz Shiozaki	塩崎	Contact	President	NAIST	\N	\N	\N	2026-07-22	Connected Rob to Kubo; not yet an advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
28	James Hill	\N	Contact	JSPS Postdoctoral Fellow — palaeoecology of Japanese sacred groves	Osaka Metropolitan University (host: Jun Inoue)	\N	\N	\N	2026-08-07	Identified as prospect — not yet contacted	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
29	Nao Uesaka	上坂奈央	Financial Partner	Representative	Mizuho Securities	\N	nao.uesaka@mizuho-sc.com	\N	2026-08-05	Meeting went well; deck + broadleaf list promised	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
30	You Li	\N	Financial Partner	Representative	Mizuho Securities	\N	you.li@mizuho-sc.com	\N	2026-07-01	No public profile found; unconfirmed contact	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
31	Yuya Kato	加藤祐也	Funder Contact	Impact Officer	SIIF (Social Impact Investment Foundation)	\N	kato@siif.or.jp	\N	2026-07-08	Morgan Lewis event — outcome-financing discussion	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
32	Fujitex	\N	Vendor	Chipper supplier — RFQ contact	Fujitex Co.	\N	fjenergy@fjtex.co.jp	\N	2026-08-01	RFQ drafted, not yet sent	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
33	Jérôme Floerke	\N	Prospect	Miyawaki reforestation specialist	Niwamori.org (Nara)	\N	\N	\N	\N	Identified as potential partner — not yet contacted	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
15	Tokuo Aomi	青見	Local Partner	CHP prototype partner	Sugano Organic	\N	suganokoubou@gmail.com	\N	2026-06-23	Outreach email sent\n\nUsually reached via Instagram messages. Gmail draft sent 2026-08-21 thanking him for introducing Kaide Chie (engawa/MYSH).	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
14	Kinjo Rie	近処里英	Local Partner	代表理事組合長 (Co-op Head)	Mitsue Village Forest Cooperative		info@mitsuemori.com	https://mitsuemori.com	2026-08-05	Meeting — open to collaboration; retention (not recruitment) is the real problem	2026-08-18 16:58:57.220083+09	2026-08-21 14:35:06.080303+09
27	Minoru Kubo	久保	Advisor	Ph.D., Assoc. Professor, Center for Digital Green-innovation (CDG)	Nara Institute of Science and Technology (NAIST)	+81-743-72-6082 (ex.3037)	m.kubo@bs.naist.jp	https://cdgw3.naist.jp/	2026-08-21	Contact info added (address: 8916-5 Takayama-cho, Ikoma, Nara 630-0192); connected via Shiozaki (NAIST President)	2026-08-18 16:58:57.220083+09	2026-08-21 22:23:23.791551+09
6	Henry Takata	高田誠一	Advisor	Rep. Director, SynTech Japan	Japan Board, U.S.-Japan Council	\N	takathe@yahoo.com	\N	2026-09-02	Rob emailed update on MitsueMori 50kW/AI prototype talks + Tenkawa visit; asked if Henry can visit Mitsue to meet the team in person	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
19	Nakajima Hideki	中嶋英樹	Government	Vice Mayor	御杖村 (Mitsue Village)	0745-95-2001	h-nakajima@vill.mitsue.lg.jp	\N	2025-12-01	Initial informal contact, late 2025	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
46	Andy Viirtela		Local Partners / Contacts	講師 (Instructor), グローバル人材育成塾 (ECC)	高龍館/Koryukan (old wooden school)	070-1860-6454	andy.viirtela@gmail.com		2026-07-08	Attended village hall meeting 2026-07-08 (children's workshop proposal) as translation support. Workshop venue set to the old wooden school where he teaches. Not to be confused with Andy Buffler (UCT, unrelated Safecast contact).	2026-09-06 22:05:19.532573+09	2026-09-06 22:05:19.532573+09
37	Sugimoto Kazuya	杉本和也	Partner Org	森林総合監理士 (Certified Forest General Manager), 天川村地域林政アドバイザー / 洞川財産区森林アドバイザー, 奈良県森林整備普及協会事務局長 — 杉本森林総合監理士事務所 (Forstwald)	Tenkawa Village (天川村)	090-6050-0752	forstwald2019@gmail.com	https://forstwald2019.wixsite.com/forstwald	2026-08-25	Met with 3 more trees staff (Sugiura, Kishi, Endo) during Tenkawa visit; impressed by project, wants Tenkawa in the AI mesh; sent explanatory PDF (202509活かす森林)	2026-08-25 18:49:26.184777+09	2026-08-25 18:49:26.184777+09
38	Sugiura Kiminori	杉浦公則	Partner Org	External Affairs (渉外)	more trees	03-5770-3969	sugiura@more-trees.org		2026-08-25	Met during Tenkawa visit with Sugimoto Kazuya; office: 107-0052 東京都港区赤坂4-7-7 H&K赤坂レジデンス201	2026-08-26 00:49:59.889332+09	2026-08-26 00:49:59.889332+09
41	Nobori Ryutaro	登隆太郎	Government	次長補佐 (Assistant Deputy Director)	御杖村教育委員会事務局 (Mitsue Village Board of Education Secretariat)	0745-95-2004 / FAX 0745-95-6800	kyoui@vill.mitsue.lg.jp		2026-09-07	Village hall confirmed office structure: reports to 教育長 Suzuki Yasuhiro; office = 次長+次長補佐(Nobori)+一般職員2名, 4 total.	2026-08-28 01:20:34.098354+09	2026-08-28 01:20:34.098354+09
35	Sakoda Kazuya	迫田和也	Government	教務課長 (Head of Academic Affairs)	奈良県フォレスターアカデミー (Nara Forester Academy)	0746-42-8100	sakoda-kazuya@office.pref.nara.lg.jp		2026-08-21	Took over as point of contact for our inquiry to Nara Forester Academy (sent via web form 2026-08-06). Requested a one-page (A4) overview document about our project. Reply drafted 2026-08-21 confirming we will send it. Fax: 0746-42-8400.	2026-08-21 14:00:13.57459+09	2026-08-21 14:00:13.57459+09
39	Kishi Takuya	岸卓弥	Partner Org	External Affairs Director (渉外ディレクター)	more trees				2026-08-25	Met during Tenkawa visit with Sugimoto Kazuya; office: 107-0052 東京都港区赤坂4-7-7 H&K赤坂レジデンス201	2026-08-26 00:49:59.889332+09	2026-08-26 00:49:59.889332+09
40	Endo Satoshi	遠藤智史	Partner Org	External Affairs (渉外)	more trees				2026-08-25	Met during Tenkawa visit with Sugimoto Kazuya; office: 107-0052 東京都港区赤坂4-7-7 H&K赤坂レジデンス201	2026-08-26 00:49:59.889332+09	2026-08-26 00:49:59.889332+09
42	Taishi Koyachi	\N	Contact	Oversees technical alliance operations, Shika (Ishikawa) site	HIGHRESO Co., Ltd. (株式会社ハイレゾ)	\N	\N	https://highreso.jp/	2026-09-04	Identified via Japan Times/Bloomberg article (2026-09-02) — quoted wanting government support for GPU costs but not yet feeling direct benefit. Reached out via HIGHRESO EN+JP contact forms 2026-09-04 referencing the article; no confirmed direct email/phone on file.	2026-09-04 01:56:17.588738+09	2026-09-04 01:56:17.588738+09
43	Akiko Hayashi Koyama	林／小山 明子	Design/Tourism	Graphic Designer, Art Director	Aluminum (own practice); ex-avex network, Dwango; East Nara Nabari Tourism Marketing			https://www.behance.net/akikohayashi	2026-09-04	Mie-based designer/art director; regional tourism branding (incl. "Magical Mitsue" travel guide). Address: 898-50 Ikedacho, Suzuka, Mie 513-0032, Japan. LinkedIn: linkedin.com/in/akikohayashi	2026-09-04 02:11:45.696168+09	2026-09-04 02:13:30.189838+09
47	Yurika Moriyama	森山ゆりか	Local Partners / Contacts	Andy Viirtela's wife; local contact			moriyama.yurika@gmail.com		2026-05-25	Shared Andy's phone number 2026-05-20/25. Has a son (Akira) who ran in a local kids' marathon. Offered Rob an open invite to visit.	2026-09-06 22:05:19.532573+09	2026-09-06 22:05:19.532573+09
34	Kaide Chie	貝出智恵	Prospect	engawa Concierge / Japanese-language teacher — migration & settlement consultant	MYSH株式会社 (奥大和移住定住交流センター engawa)	+81744483019	chie-kaide@mysh.tokyo	https://okuyamato-engawa.jp/	2026-11-09	Met in person 2026-08-21. Nara native, Tokyo student years, backpacked SE Asia, teaches Japanese to foreigners, engawa consultant for Okuyamato region (19 municipalities, Kashihara office). Handles migration/settlement counseling and community bridging for people considering moving to Okuyamato -- potentially useful contact for regional outreach/partnerships. engawa address: 605-5 Tokiwacho, Kashihara, Nara 634-0003.\n\nFollow-up funding/collaboration ideas (2026-08-21, Rob priority-picked): (1) Nara Prefecture / municipal chihou-sousei regional-revitalization subsidies -- MYSH already operates inside this system, she likely knows which grants fit a joint project; (2) MYSH as co-applicant/intermediary given their existing grant-writing relationships with the 19 Okuyamato municipalities; (3) Corporate CSR sponsorship from tech/telecom firms interested in rural digital projects. Discuss at next meeting.\n\nPlan (2026-08-21): Consult Chie first on Zoom call, then ask her for an introduction to MYSH CEO 向井裕人 (Hiroto Mukai) -- Mitsue Village Project likely needs a top-level MYSH decision/department routing beyond what Chie can authorize alone. MYSH general contact: info@mysh.co.jp (no direct CEO email found).\n\nMYSH leadership: CEO / Representative Director is 向井裕人 (Hiroto Mukai). No direct personal contact found; general company inbox is info@mysh.co.jp (recruit@mysh.co.jp is recruitment-only).\n\nUPDATE (2026-09-06): Rob invited to and confirmed attendance at コミュニティマネージャー育成プログラム成果発表会 (Community Manager Training Program results presentation) on 2026-11-09, 13:00-17:00 + networking after, at engawa (奥大和移住定住交流センター, 634-0003 奈良県橿原市常盤町605-5, 橿原総合庁舎別館). CC'd colleagues on the thread: riku@mysh.tokyo, naoto-uebayashi@mysh.tokyo.	2026-08-21 12:33:05.174269+09	2026-08-21 12:33:05.174269+09
48	Suzuki Yasuhiro	鈴木泰弘	Government	教育長 (Superintendent of Education)	御杖村教育委員会 (Mitsue Village Board of Education)	0745-95-2004	kyoui@vill.mitsue.lg.jp		2026-09-07	Named in village hall reply to Rob's inquiry re: Board of Education leadership/structure.	2026-09-07 11:59:31.844385+09	2026-09-07 11:59:31.844385+09
50	Satoshi Kodama		Advisor/Contact	Executive Officer, Customer Solution Division	The Kansai Electric Power Co., Inc. (KEPCO)	+81-6-6441-8821	kodama.satoshi@c2.kepco.co.jp		2026-09-08	Met at SwissNex Energy Days; got business card. Left before Rob could speak with him directly. Want to ask his advice on support/collaboration routes for Mitsue project.	2026-09-08 16:50:04.917196+09	2026-09-08 16:50:04.917196+09
45	Yamaguchi Yoshiyuki	山口義行	Local Partners / Contacts	地域おこし協力隊員 (Regional Revitalization Cooperation Squad) - self-employed forestry practitioner, ex-steel craftsman	御杖村むらづくり振興課	0745-95-2001 (内線130-135)	mtsound72@gmail.com	https://www.vill.mitsue.nara.jp/kurashi/jigyosha/sangyo_koyo/813.html	2026-09-08	Confirmed meeting: Sept 10 (Thu) 13:00 at Himeishi-no-yu. Cannot speak English — meeting will be Japanese-only.	2026-09-06 13:39:38.662294+09	2026-09-06 13:39:38.662294+09
51	Akagi Yasuaki		government/research	Senior Researcher, Sustainable Energy Unit, Technology and Innovation Strategy Center	NEDO (New Energy and Industrial Technology Development Organization)	+81-70-7469-8055	akagiysa@nedo.go.jp		2026-09-02	Met at SwissNex event, Osaka (Expo 2025 Kansai). Followed up by email to akagiysa@nedo.go.jp (no reply) and to unit mailbox tsc-unit-2024@ml.nedo.go.jp on 2026-09-11 asking if the earlier message was received. Address: MUZA Kawasaki Central Tower, 1310 Omiya-cho, Saiwai-ku, Kawasaki City, Kanagawa 212-8554 Japan.	2026-09-11 16:17:13.212446+09	2026-09-11 16:17:13.212446+09
\.


--
-- Name: outreach_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.outreach_id_seq', 31, true);


--
-- Name: people_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.people_id_seq', 51, true);


--
-- Name: outreach outreach_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.outreach
    ADD CONSTRAINT outreach_pkey PRIMARY KEY (id);


--
-- Name: people people_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT people_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict tVPz9o0k32CkFdMgOMhYNfkV79a7vDgls3CDyvZpfcJRewYjiK3CSDaVXodFs8A

