<!-- Version: v1.1 | Last modified: 2026-08-31 -->

# Outreach Tracker

**This table now lives in AgentMesh** (Outreach tab, alongside People) — sortable/searchable/editable there: http://localhost/agentmesh/ → Outreach tab. Backed by Postgres table `outreach` (same DB as `people`), API at `outreach.php` (GET/POST/PUT/DELETE), UI code in `/var/www/html/agentmesh/index.html`.

This file stays as a static snapshot/backup, not the live source — edit new entries in AgentMesh going forward, not here.

Running log of notes, forms, letters, and emails sent out for the project. Source doc for each row is in `docs/outreach/` unless noted otherwise. Status reconstructed from file dates and memory notes on 2026-08-31 — entries marked **verify** should be double-checked before relying on them.

| Date | Contact / Org | Channel | Subject | Status | Notes / Source doc |
|---|---|---|---|---|---|
| 2026-08-31 | GX地域共創補助金事務局 (METI) | Web form | Mesh-model / multi-site eligibility inquiry | **Sent** — receipt #00001785, awaiting reply | [[project_gx_inquiry_submitted]] (memory) |
| 2026-08-28 | 御杖村 古谷 (Furutani) | Email reply | Thanks for disclosure-doc meeting | Sent | Gmail thread `1a04651a457b3a45` |
| 2026-08-26 | Komatsu (コマツ) forestry equipment | Email | CTL equipment trial-site inquiry | Sent | Gmail thread `1a03cf46a2fab888` |
| 2026-08-20 | 奈良県フォレスターアカデミー | Email | Confirmation re: form submission follow-up | Sent | `mitsue_email_forester_academy_request.md`; [[project_forester_academy_followup_sent]] |
| 2026-08-14 | Miyagawa Forest Cooperative | Email (intro, updated) | Partnership intro | Sent — verify | `mitsue_email_miyagawa_shinrin_intro.md` |
| 2026-08-06 | Fujitex | Email | Chipper RFQ | Sent — verify | `mitsue_email_fujitex_chipper_rfq.md` |
| 2026-08-06 | (chipper vendors, general) | Form drafts | Chipper RFQ | Drafted — verify if sent | `mitsue_chipper_rfq_form_drafts.md` |
| 2026-08-06 | more trees | Email | Aug 5 meeting followup | Sent — verify | `mitsue_email_moretrees_aug5_followup.md` |
| 2026-08-05 | Mizuho (上坂奈央) | Email | Aug 5 meeting followup + deck | **Drafted, not sent** | `mitsue_email_mizuho_nao_aug5_followup.md`; [[project_mizuho_nao_followup]] |
| 2026-07-24 | 御杖村 Kinjo | Physical note | Forester Academy note | Delivered in person | `mitsue_note_kinjo_forester_academy.md`; [[project_kinjo_note_delivered]] |
| 2026-07-24 | NAIST Kubo | Email | Introduction | Sent — verify | `mitsue_email_naist_kubo_intro.md` |
| 2026-07-24 | Dome (via Forester Academy) | Email | Introduction | Sent — verify | `mitsue_email_dome_forester_academy_intro.md` |
| 2026-07-21 | 奈良県フォレスターアカデミー | PDF + email | Recruitment summary A4 | Sent — verify | `mitsue_forester_academy_recruit_summary_a4.md/.pdf` |
| 2026-07-21 | Swissnex (Joutet) | Email | Introduction | Sent — verify | `mitsue_email_swissnex_joutet_intro.md` |
| 2026-07-21 | NAIST Shiozaki | Email | Introduction | Sent — verify | `mitsue_email_naist_shiozaki_intro.md` |
| 2026-07-09 | more trees | Email + PDF | Partnership introduction | Sent | `mitsue_email_moretrees_intro.md/.pdf`; [[project_moretrees_email_thread]] |
| 2026-07-09 | Miyagawa Forest Cooperative | Email + PDF | Introduction | Sent | `mitsue_email_miyagawa_shinrin_intro.md/.pdf` |
| 2026-07-08 | Pellegrom | Letter + PDF | Support request | Sent | `mitsue_letter_pellegrom_support_request.md/.pdf` |
| 2026-07-06 | more trees | Email | General outreach | Sent — verify | `more-trees outreach email.md` |
| 2026-07-06 | Biomass site visit contacts | Email(s) | Visit request | Sent — verify | `mitsue_biomass_visit_request_emails.md/.pdf` |
| 2026-06-21 | Quantum Mesh (JP) | Email/PDF draft | Outreach intro | Drafted — status unclear | `mitsue_quantum_mesh_outreach_jp.md/.pdf` |
| 2026-06-21 | Quantum Mesh (EN) | Email/PDF draft | Outreach intro | Drafted — status unclear | `mitsue_quantum_mesh_outreach.md/.pdf` |
| 2026-08-31 | HIGHRESO | Email/PDF draft | Bilingual intro (Joi Ito referral) | **Held** — need named contact first | `mitsue_email_highreso_intro.md/.pdf`; [[project_highreso_outreach]], [[project_quantummesh_highreso_outreach_hold]] |
| 2026-08-31 | Quantum Mesh | Email/PDF draft | Intro (revised) | **Held** — pending Rob's consult w/ Kulyatin + Klein | `mitsue_email_quantummesh_intro.md/.pdf`; [[project_quantummesh_highreso_outreach_hold]] |

## Not yet logged here (mentioned in memory, source doc not confirmed)

- Sugano Organic / Aomi Tokuo — email sent 2026-06-23 ([[project_tokuo_aomi]])
- 奈良県フォレスターアカデミー initial webform submission, 2026-08-06/2026-08-10 confirmations (Gmail threads `19fd56f834243c17`, `19fe9bdffe62fb26` area)
- Mizuho entity meeting followups beyond the Aug 5 draft

## How to maintain this

Add a row whenever a note/form/email/letter goes out. When in doubt about status, mark **verify** rather than guessing — this file is a tracking aid, not a source of truth for what was actually sent.
