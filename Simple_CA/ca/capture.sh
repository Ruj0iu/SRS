#!/bin/bash

echo "🚦 Starting tcpdump..."
tcpdump -i eth0   -w /data/eve_traffic.pcap &
TCPDUMP_PID=$!
sleep 5
echo "🚀 Starting CA_server.py"
python3 ca_server.py

echo "🛑 Stopping tcpdump..."
sleep 2
kill $TCPDUMP_PID

# Wait a second to ensure .pcap file is written
sleep 3

echo "✅ Capture complete."
