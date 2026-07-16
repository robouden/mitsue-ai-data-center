# Daily Reporting System with Activities by Project

This directory contains the enhanced daily reporting system that includes project activity tracking.

## Overview

The enhanced daily reporting system now includes a new "Activities by Project" section that tracks what kind of work is done for which projects. This provides better visibility into project time allocation and activities.

## Files

- `daily_report_generator.sh` - Script to generate daily reports with the new Activities by Project section
- `daily_report_config.md` - Configuration file for the daily reporting system
- `sample_enhanced_report.md` - Sample of how the enhanced report looks
- `memory/` - Directory where daily reports are stored

## New "Activities by Project" Section

The new section in the daily reports looks like this:

### 📋 Activities by Project

#### Project: [Project Name]
- [Activity description] (HH:MM-HH:MM)
  * Command: [bash command used if applicable]
  * Technical work: [details]

## Usage

1. Run the daily report generator script:
   ```bash
   ./daily_report_generator.sh
   ```

2. The script will create a new daily report in the `memory/` directory with today's date.

3. Manually update the "Activities by Project" section throughout the day as work is performed.

4. The reports will be automatically synced to AnyType (when the integration is fully configured).

## Integration with AnyType

The reports are designed to be automatically synced to AnyType with the following naming convention:
- "CopyQ History - YYYY-MM-DD" for clipboard entries
- "Bash History - YYYY-MM-DD" for bash history entries
- "Daily Activity Report - YYYY-MM-DD" for the main report

## Future Improvements

- Automate the population of the "Activities by Project" section
- Enhance AnyType integration for automatic syncing
- Add time tracking for more accurate session timing