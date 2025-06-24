#!/bin/bash

echo "🚦 Starting tcpdump..."
tcpdump -i eth0   -w /data/eve_traffic.pcap &
TCPDUMP_PID=$!
sleep 3
echo "👂 Starting Eve MITM script..."
python3 eve_sniffer.py

echo "🛑 Stopping tcpdump..."
sleep 2
kill $TCPDUMP_PID

# Wait a second to ensure .pcap file is written
sleep 5

echo "✅ Capture complete."
