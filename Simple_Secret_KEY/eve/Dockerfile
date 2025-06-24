FROM python:3
WORKDIR /app

# Install required system libraries
RUN apt-get update && \
    apt-get install -y libpcap-dev tcpdump && \
    rm -rf /var/lib/apt/lists/*


# Install Python dependencies
RUN pip install pycryptodome scapy

COPY ../crypto_utils.py .
COPY eve/eve_sniffer.py .
# COPY eve/eve_bruteforce.py .

# CMD ["python3", "eve_sniffer.py"]
# CMD ["sh", "-c", "python eve_sniffer.py & python eve_bruteforce.py"]
CMD ["sh", "-c", "python eve_sniffer.py "]