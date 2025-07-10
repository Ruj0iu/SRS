FROM python:3
WORKDIR /app

# Install system tools
RUN apt-get update && \
    apt-get install -y libpcap-dev tcpdump && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pycryptodome scapy

COPY ../crypto_utils.py .
COPY ca/ca_server.py .
COPY ca/capture.sh .

# Run shell script instead of just python
CMD ["bash", "capture.sh"]
