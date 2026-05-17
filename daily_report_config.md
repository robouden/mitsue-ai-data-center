# Daily Report Configuration

## Configuration for Daily Report Generation

This configuration file defines how daily reports should be structured with the new Activities by Project section.

### Report Structure
The daily reports should include:
1. Standard header with date and time information
2. Session timing information
3. Clipboard activity tracking
4. Bash command history
5. Activities by Project section (NEW)
6. Notes section
7. Report metadata

### Activities by Project Section Format
The new section should be formatted as:

### 📋 Activities by Project
This section tracks what kind of work was done for which projects during the active sessions.

#### Project: [Project Name]
- [Activity description] (HH:MM-HH:MM)
  * Command: [bash command used if applicable]
  * Technical work: [details]

### Integration with AnyType
The reports should be automatically synced to AnyType with the following naming convention:
- "CopyQ History - YYYY-MM-DD" for clipboard entries
- "Bash History - YYYY-MM-DD" for bash history entries
- "Daily Activity Report - YYYY-MM-DD" for the main report

### Automation
The daily report generator should run automatically and populate the Activities by Project section based on the work done during the day.