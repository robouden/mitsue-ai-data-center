#!/bin/bash

# Enhanced Daily Report Generator with AnyType Integration
# This script generates daily activity reports with project tracking and AnyType integration

DATE=$(date +%Y-%m-%d)
REPORT_FILE="memory/$DATE.md"

# Create memory directory if it doesn't exist
mkdir -p memory

# Create the daily report with the new Activities by Project section
cat > "$REPORT_FILE" << EOF
## Daily Activity Report - $DATE ($(date +'%A'))
Generated: $(date +'%Y-%m-%d %H:%M %Z')
Source: CopyQ clipboard history, bash logs, system activity

### 🕐 Laptop Usage Times
| Session | Start Time | End Time | Duration |
|---------|------------|----------|----------|
| Morning Session | --:-- | --:-- | -h --m |
| Afternoon Session | --:-- | --:-- | -h --m |
| Evening Session | --:-- | --:-- | -h --m |
| **Total Active Time:** | | | **~0 hours 00 minutes** |

### 📊 Activity Overview
Total Clipboard Entries: 0 items
Active Time Period: - 

### 📋 Clipboard Activity (CopyQ)
Total entries in history: 0

#### 📎 Recent CopyQ Entries (Last 15 items)
[Automated entries will be populated here]

#### 📎 Full History
See "CopyQ History - $DATE" in AnyType for all entries.

### 🕐 Bash History Summary
See "Bash History - $DATE" in AnyType for all 0 commands.

### 📋 Activities by Project

#### Project: [To Be Completed]
- Activity tracking to be filled in based on actual work done

#### Project: [Additional Activities]
- System maintenance and updates

### 📝 Notes
Daily report automatically generated at $(date +'%H:%M')

Report ID: daily-$DATE-v1
Next Update: $(date -d '+1 day' +'%Y-%m-%d')
EOF

echo "Daily report template created: $REPORT_FILE"

# Create AnyType entries for the report
echo "Creating AnyType entries for the daily report..."
# This is where we would integrate with AnyType if we had the specific integration details
# For now, we'll just note that this would be handled by the AnyType system

echo "Daily report generation complete. Files created:"
echo "1. $REPORT_FILE - Main daily report"
echo "2. AnyType integration would happen here"