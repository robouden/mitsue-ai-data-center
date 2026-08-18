--
-- PostgreSQL database dump
--

\restrict dDUC1zD6oMCxciRVBIShPSrrYR0MQQxGjNPbrYmxmVl8YnOgP67IigPbhSdmHV5

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

DROP DATABASE IF EXISTS agentmesh;
--
-- Name: agentmesh; Type: DATABASE; Schema: -; Owner: agentmesh
--

CREATE DATABASE agentmesh WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';


ALTER DATABASE agentmesh OWNER TO agentmesh;

\unrestrict dDUC1zD6oMCxciRVBIShPSrrYR0MQQxGjNPbrYmxmVl8YnOgP67IigPbhSdmHV5
\connect agentmesh
\restrict dDUC1zD6oMCxciRVBIShPSrrYR0MQQxGjNPbrYmxmVl8YnOgP67IigPbhSdmHV5

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
-- Name: people; Type: TABLE; Schema: public; Owner: agentmesh
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


ALTER TABLE public.people OWNER TO agentmesh;

--
-- Name: people_id_seq; Type: SEQUENCE; Schema: public; Owner: agentmesh
--

CREATE SEQUENCE public.people_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.people_id_seq OWNER TO agentmesh;

--
-- Name: people_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: agentmesh
--

ALTER SEQUENCE public.people_id_seq OWNED BY public.people.id;


--
-- Name: people id; Type: DEFAULT; Schema: public; Owner: agentmesh
--

ALTER TABLE ONLY public.people ALTER COLUMN id SET DEFAULT nextval('public.people_id_seq'::regclass);


--
-- Data for Name: people; Type: TABLE DATA; Schema: public; Owner: agentmesh
--

COPY public.people (id, name, kanji, category, role, org, phone, email, website, last_date, last_note, created_at, updated_at) FROM stdin;
1	Rob Oudendijk	\N	Core Team	Founder & Project Lead	YR-Design	080-2260-5966	oudendijk.biz@gmail.com	\N	2026-08-06	Ongoing — daily project work	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
2	Yuka Hayashi	石村ゆか	Core Team	Colleague / co-presenter	\N	\N	yuuka1213@hotmail.com	\N	2026-07-29	Sugano Organic meeting	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
3	San Poisson	\N	Core Team	Project Manager	\N	\N	sanpoisson@gmail.com	\N	2026-07-29	Sugano Organic meeting	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
4	Takuo Dome	堂目卓生	Advisor	Specially Appointed Professor, Osaka Univ.	Rep. Director, 一般社団法人いのち会議	\N	t-dome@econ.osaka-u.ac.jp	\N	2026-08-06	Forester Academy endorsement finalized & submitted	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
5	Ray Ozzie	\N	Advisor	Creator of Lotus Notes; former Microsoft CSA	\N	\N	\N	\N	2026-05-05	Confirmed as advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
6	Henry Takata	高田誠一	Advisor	Rep. Director, SynTech Japan	Japan Board, U.S.-Japan Council	\N	\N	\N	2026-07-16	Confirmed; biomass CHP + biz-dev advice	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
7	Evin Zoet	\N	Advisor	Co-Representative Director	Transom	\N	elvinzoet@transom.jp	\N	2026-06-16	Confirmed as advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
8	Yoshiko Zoet-Suzuki	\N	Advisor	Co-Representative Director	Transom	\N	yoshikozoetsuzuki@transom.jp	\N	2026-06-16	Confirmed as advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
9	Yuko Koshiba	\N	Advisor	Philanthropy Advisor	PA-Inc	\N	yuko.koshiba@philanthropy-advisors.jp	\N	2026-07-20	3 questions + 公益法人 support offer outstanding	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
10	Takahisa Watanabe	渡邉貴久	Advisor	Managing Associate — Legal Advisor	Linklaters Tokyo	\N	takahisa.watanabe@linklaters.com	\N	2026-07-24	Confirmed pro bono support; advised keeping entity structure open in Phase 0	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
11	Yuji Nakano	中野雄司	Advisor	Attorney — Legal Advisor	TMI Associates	\N	Yuji_Nakano@tmi.gr.jp	\N	2026-06-14	Confirmed pro bono support; sent entity-structure (NPO/一般社団法人) comparison	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
12	Sotaro Hotta	堀田総太郎	Advisor	Attorney — Legal Advisor	Likely Nishimura & Asahi (unconfirmed)	\N	\N	\N	2026-07-08	Confirmed pro bono support	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
13	Karsten Klein	\N	Advisor	CEO & Founder — AI data centre consultant (AI governance/ISO 42001, cybersecurity/ISO 27001, data privacy/GDPR)	KLEIN K.K., Advisory Services Japan	\N	\N	https://www.kleinkk.co.jp/	2026-08-18	First online meeting; discussed how the AI data center should be run: hardware, software, layers, security	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
14	Kinjo Rie	近処里英	Local Partner	代表理事組合長 (Co-op Head)	Mitsue Village Forest Cooperative	\N	\N	\N	2026-08-05	Meeting — open to collaboration; retention (not recruitment) is the real problem	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
15	Tokuo Aomi	青見	Local Partner	CHP prototype partner	Sugano Organic	\N	\N	\N	2026-06-23	Outreach email sent	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
16	Niwa-san	丹羽	Local Partner	Fuel-supply partner (sawmill)	丹羽製材, Sugano	\N	\N	\N	2026-07-29	Joint fuel-chipper discussion ongoing	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
17	Kawakita Yasunori	川北康則	Local Contact	Retired Principal	Mitsue Elementary School	\N	\N	\N	2026-06-16	Approved the Kaya poem	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
18	Nishimura Yuki	西村	Local Contact	Local contact ("Carp guy from Mitsue")	\N	\N	nishimura2099@gmail.com	\N	2026-05-06	Project Q&A exchange	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
19	Nakajima Hideki	中島秀樹	Government	Vice Mayor	御杖村 (Mitsue Village)	0745-95-2001	h-nakajima@vill.mitsue.lg.jp	\N	2025-12-01	Initial informal contact, late 2025	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
20	Furutani Masatoshi	古谷匡敏	Government	Village Hall staff	御杖村役場	\N	t-furutani@vill.mitsue.lg.jp	\N	2026-07-13	Handled information disclosure request	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
21	Ito Shugi	伊藤収宜	Government	Mayor	御杖村 (Mitsue Village)	\N	\N	\N	2026-06-01	On record re: forestry workforce shortage (council minutes)	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
22	Mizutani Shinkichi	水谷伸吉	Partner Org	事務局長 (Secretary-General)	more trees	\N	\N	\N	2026-07-14	Key decision-maker; Miyazaki reports to him	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
23	Kishi	岸	Partner Org	Staff	more trees	\N	kishi@more-trees.org	\N	2026-08-05	Live thread — reply owed	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
24	Miyazaki	宮﨑	Partner Org	Staff	more trees	\N	miyazaki@more-trees.org	\N	2026-08-05	Live thread — reply owed	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
25	Michael Goldberg	\N	Partner Org	Thread participant	more trees	\N	ivw@gol.com	\N	2026-07-24	CC'd on live more trees thread	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
26	Kaz Shiozaki	塩崎	Contact	President	NAIST	\N	\N	\N	2026-07-22	Connected Rob to Kubo; not yet an advisor	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
27	Minoru Kubo	久保	Contact	Assoc. Professor, Center for Digital Green Innovation	NAIST	\N	\N	\N	2026-07-22	Outreach sent — living lab / SDGs program hooks	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
28	James Hill	\N	Contact	JSPS Postdoctoral Fellow — palaeoecology of Japanese sacred groves	Osaka Metropolitan University (host: Jun Inoue)	\N	\N	\N	2026-08-07	Identified as prospect — not yet contacted	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
29	Nao Uesaka	上坂奈央	Financial Partner	Representative	Mizuho Securities	\N	nao.uesaka@mizuho-sc.com	\N	2026-08-05	Meeting went well; deck + broadleaf list promised	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
30	You Li	\N	Financial Partner	Representative	Mizuho Securities	\N	you.li@mizuho-sc.com	\N	2026-07-01	No public profile found; unconfirmed contact	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
31	Yuya Kato	加藤祐也	Funder Contact	Impact Officer	SIIF (Social Impact Investment Foundation)	\N	kato@siif.or.jp	\N	2026-07-08	Morgan Lewis event — outcome-financing discussion	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
32	Fujitex	\N	Vendor	Chipper supplier — RFQ contact	Fujitex Co.	\N	fjenergy@fjtex.co.jp	\N	2026-08-01	RFQ drafted, not yet sent	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
33	Jérôme Floerke	\N	Prospect	Miyawaki reforestation specialist	Niwamori.org (Nara)	\N	\N	\N	\N	Identified as potential partner — not yet contacted	2026-08-18 16:58:57.220083+09	2026-08-18 16:58:57.220083+09
\.


--
-- Name: people_id_seq; Type: SEQUENCE SET; Schema: public; Owner: agentmesh
--

SELECT pg_catalog.setval('public.people_id_seq', 33, true);


--
-- Name: people people_pkey; Type: CONSTRAINT; Schema: public; Owner: agentmesh
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT people_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict dDUC1zD6oMCxciRVBIShPSrrYR0MQQxGjNPbrYmxmVl8YnOgP67IigPbhSdmHV5

