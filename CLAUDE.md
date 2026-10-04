# Project Rules
- Before saying any contact detail (email, phone, kanji, role) is missing/unknown, query the AgentMesh `people` table first (psql, DSN in /home/rob/.local/share/agentmesh/agentmesh.env, port 5433, db `agentmesh`; or http://localhost/agentmesh/ People tab). Then check chat history (`messages`) and docs/team/people_register.md.
- Mirror any contact found in `people` back into docs/team/people_register.md.
