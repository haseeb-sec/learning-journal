#!/bin/bash
# Bash Log Analyzer
# Author: Haseeb Ullah Shah

LOG_FILE=$1

if [ -z "LOG_FILE" ]; then
    echo "Usage: ./log_analyzer.sh <logfile>"
    exit 1
fi

echo "=== LOG ANALYSIS REPORT ==="
echo "File: $LOG_FILE"
echo "Date: $(date)"

echo ""
echo "--- Total Requests ---"
wc -l < $LOG_FILE

echo ""
echo "--- Top 5 IP Addresses ---"
awk '{print $1}' $LOG_FILE | sort | uniq -c | sort -rn | head -5

echo ""
echo "--- Total POST Requests ---"
grep -c "POST" $LOG_FILE

echo ""
echo "--- Suspicious 404 Errors ---"
grep " 404 " $LOG_FILE | awk '{print $1}' | sort | uniq -c | sort -rn | head -5

echo ""
echo "=== ANALYSIS COMPLETE ==="
