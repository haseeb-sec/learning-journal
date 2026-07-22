#!/bin/bash
echo "=== SYSTEM INFORMATION REPORT ==="
echo ""
echo "Hostname:"
hostname
echo ""
echo "Current User:"
whoami
echo ""
echo "IP Address:"
ip addr | grep "inet " | awk '{print $2}'
echo ""
echo "Open Ports:"
ss -tuln
echo ""
echo "Disk Usage:"
df -h