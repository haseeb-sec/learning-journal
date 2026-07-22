# Note: This script is designed for Linux systems.
# Run on a Linux server or TryHackMe lab for full output.


#!/bin/bash
echo "=== SECURITY AUDIT REPORT ==="
echo "Date: $(date)"
echo ""

echo "--- Current Users Logged In ---"
who
echo ""

echo "--- Last 5 Login Attempts ---"
last | head -5
echo ""

echo "--- Open Ports ---"
ss -tuln
echo ""

echo "--- Files with Full Permissions (777) ---"
find / -type f -perm 777 2>/dev/null | head -10
echo ""

echo "=== AUDIT COMPLETE ==="
