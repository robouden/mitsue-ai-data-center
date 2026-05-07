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

## Import Script

The script that imported `mitsue_todo.xlsx` into OpenProject lives at:

```
~/openproject/import_mitsue.py
```

Re-run it only on a fresh project — it will create duplicates if work packages already exist.
