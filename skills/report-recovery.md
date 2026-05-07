# Reporting Recovery Protocol

When the automated Daily Activity Report is empty or missing usage times despite the user being active:

## 1. Verification (Truth Source)
The `last` command is the authoritative source for system session times.
- Run `last -x | grep "Date"` to find actual login/logout timestamps.
- Manually calculate durations for Morning, Afternoon, and Evening sessions.

## 2. Recovery Steps
1. **Locate the Report:** Search for the corresponding "Daily Activity Report - YYYY-MM-DD" in Anytype.
2. **Reconstruct Times:** Create a markdown table with the sessions found in `last`.
3. **Preserve Data:** If the report has existing CopyQ or Bash history summaries, **do not overwrite them**. Merge the reconstructed time table into the existing document.
4. **Update Metadata:** Mark the report as "Manually reconstructed" and increment the version (e.g., v2).

## 3. Deep Recovery (If requested)
If activity logs (CopyQ/Bash) are also missing from the report:
- **Bash:** Use `history` or `tail -n 1000 ~/.bash_history` to find commands from that specific date.
- **CopyQ:** Use `copyq-cli` or internal API to retrieve history if the automated tool failed.
- Append these findings to the report to restore the "Activity Overview" and "Clipboard Activity" sections.

## 4. Documentation
Note the failure in the report so it can be tracked as a bug for the reporting tool.
