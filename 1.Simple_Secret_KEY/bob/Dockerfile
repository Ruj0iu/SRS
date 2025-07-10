FROM python:3
WORKDIR /app

COPY ../crypto_utils.py .
COPY bob/bob_server.py .

RUN pip install pycryptodome

CMD ["python3", "bob_server.py"]
