# OpenProject — Mitsue Village Project

OpenProject is installed locally on Rob's machine and manages all work packages for this project.

## Access

| | |
|---|---|
| **URL** | http://localhost:8080 |
| **Project** | Mistue ai data center |
| **Project ID** | `3` (numeric) / `mistue-ai-data-center` (slug) |

## API Tokens

Each agent has its own account and API token. Use `apikey` as the username.

| Agent | Login | API Token |
|---|---|---|
| Claude (admin) | `admin` | `d7df8157865c3e15a0c08e6f856afcceadc7c15709684a29766976c82e742c75` |
| OpenClaw | `openclaw` | `7c73bd59a862df8d99e9981c08966d78200f1b144fc6b6f40a4b54cda8fbed16` |
| Hermes | `hermes` | `227f76125c000498897183e4d6a11677c45d199807c1f805364aa669f1d354c5` |

## Making API Calls

```bash
# List all work packages in the project
curl -u "apikey:<TOKEN>" http://localhost:8080/api/v3/projects/3/work_packages

# Create a work package
curl -u "apikey:<TOKEN>" -X POST http://localhost:8080/api/v3/projects/3/work_packages \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Task title",
    "_links": {
      "type":     {"href": "/api/v3/types/1"},
      "status":   {"href": "/api/v3/statuses/1"},
      "priority": {"href": "/api/v3/priorities/8"}
    }
  }'

# Update a work package
curl -u "apikey:<TOKEN>" -X PATCH http://localhost:8080/api/v3/work_packages/<ID> \
  -H "Content-Type: application/json" \
  -d '{"subject": "Updated title", "lockVersion": <current_lock_version>}'
```

## Reference IDs

### Types
| ID | Name |
|---|---|
| 1 | Task |
| 2 | Milestone |
| 3 | Summary task |

### Statuses
| ID | Name |
|---|---|
| 1 | New |
| 7 | In progress |
| 12 | Closed |
| 13 | On hold |
| 14 | Rejected |

### Priorities
| ID | Name |
|---|---|
| 7 | Low |
| 8 | Normal |
| 9 | High |
| 10 | Immediate |

## Project Structure (imported from mitsue_todo.xlsx)

Work packages are organised as:

- **Master To-Do** — Summary tasks per phase (Phase 0–4, Cross-cutting), with Tasks nested as children
- **Legal Checklist** — Summary tasks per category (Entity & Tax, Permits, Pro support), with Tasks as children
- **Risk Register** — Flat list of Tasks prefixed `[Risk]`

## Docker Management

OpenProject runs via Docker Compose on Rob's machine.

### After powering the laptop back on

Open a terminal and run:

```bash
docker compose -f ~/openproject/docker-compose.yml up -d
```

Then open http://localhost:8080 in your browser. Everything is back up in ~30 seconds.

> **Note:** the containers survive *reboots* automatically (`restart: unless-stopped`), but not a clean shutdown. You only need the command above after powering off.

### Other useful commands

```bash
# Stop
docker compose -f ~/openproject/docker-compose.yml down

# Logs
docker compose -f ~/openproject/docker-compose.yml logs -f web

# Status
docker compose -f ~/openproject/docker-compose.yml ps
```

All project data is stored in Docker volumes (`pgdata`, `opdata`) and is never lost when stopping or restarting.

## Theme — Robouden Dark

The header and sidebar use your robouden dark colors, set via OpenProject's 7 built-in CSS variables:

| Variable | Color |
|---|---|
| primary-button-color | `#3655b5` |
| accent-color | `#6796e6` |
| header-bg-color | `#353535` |
| header-item-bg-hover-color | `#505050` |
| main-menu-bg-color | `#353535` |
| main-menu-bg-selected-background | `#505050` |
| main-menu-bg-hover-background | `#444444` |

### Full dark mode (content area) via Stylus

The Community edition only exposes those 7 variables. For a complete dark theme install the **Stylus** browser extension (Firefox / Chrome), then:

1. Open Stylus → **Manage** → **Write new style**
2. Set it to apply to `http://localhost:8080/*`
3. Paste the contents of [`openproject_robouden_theme.css`](openproject_robouden_theme.css)
4. Save

The CSS file is kept in the repo so all agents can reference it.

## Backup

Run this any time you want to snapshot OpenProject and push it to both repos:

```bash
bash "/home/rob/Documents/Mitsue/Mitsue Village Project AI data center/openproject_backup.sh"
```

This will:
1. Export all work packages to `openproject_backup.json` (human-readable)
2. Dump the full PostgreSQL database to `openproject_backup.sql` (restorable)
3. Commit and push both files to Codeberg and GitHub

### Restore from backup

After a `git pull`, run the restore script:

```bash
git pull
bash "/home/rob/Documents/Mitsue/Mitsue Village Project AI data center/openproject_restore.sh"
```

The script will:
1. Confirm before doing anything destructive
2. Stop the web/worker containers to prevent writes during restore
3. Drop and recreate the database
4. Load the SQL dump
5. Restart everything and wait until the site is back up

> **Note:** `git pull` only restores the backup *files* — the script is what actually loads the data into OpenProject.

## Import Script

The script that imported `mitsue_todo.xlsx` into OpenProject lives at:

```
~/openproject/import_mitsue.py
```

Re-run it only on a fresh project — it will create duplicates if work packages already exist.

## Project Documents (Codeberg)

All documents live at: **https://codeberg.org/YR-Design/mitsue-ai-data-center**

### Project Overview & Strategy

| Document | View | PDF |
|---|---|---|
| Project Overview (Pellegrom) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_project_overview_pellegrom.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_project_overview_pellegrom.pdf) |
| Founding Story | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_project_founding_story.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_project_founding_story.pdf) |
| Founding Story (Japanese) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_project_founding_story_jp.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_project_founding_story_jp.pdf) |
| Village Government One-Pager | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_village_government_onepager.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_village_government_onepager.pdf) |
| Village Government One-Pager (Japanese) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_village_government_onepager_jp.md) | — |
| Q&A Briefing | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_qa_briefing.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_qa_briefing.pdf) |
| Phases & Funding Flowchart | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_phases_funding_flowchart.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_phases_funding_flowchart.pdf) |

### Implementation & Planning

| Document | View | PDF |
|---|---|---|
| Implementation Plan | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_implementation_plan.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_implementation_plan.pdf) |
| Implementation Plan (Japanese) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_implementation_plan_jp.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_implementation_plan_jp.pdf) |
| Mayor Meeting Talking Points | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_mayor_meeting_talking_points.md) | — |
| Letter: Pellegrom Support Request | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_letter_pellegrom_support_request.md) | — |

### Legal & Governance

| Document | View | PDF |
|---|---|---|
| Founding Charter | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_founding_charter.md) | — |
| Founder Agreement Template | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_founder_agreement_template.md) | [pdf](https://codeberg.org/YR-Design/mitsue-ai-data-center/raw/branch/main/mitsue_founder_agreement_template.pdf) |

### Stakeholders

| Document | View |
|---|---|
| Stakeholders (English) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_stakeholders.md) |
| Stakeholders (Japanese) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_stakeholders_jp.md) |
| Interactive Graph (English) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_stakeholder_graph.html) |
| Interactive Graph (Japanese) | [view](https://codeberg.org/YR-Design/mitsue-ai-data-center/src/branch/main/mitsue_stakeholder_graph_jp.html) |
