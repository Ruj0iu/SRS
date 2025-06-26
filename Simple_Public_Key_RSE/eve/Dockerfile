FROM python:3
WORKDIR /app

# Install system tools
RUN apt-get update && \
    apt-get install -y libpcap-dev tcpdump && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pycryptodome scapy


COPY eve/eve_sniffer.py .
COPY eve/capture.sh .

# Run shell script instead of just python
CMD ["bash", "capture.sh"]
