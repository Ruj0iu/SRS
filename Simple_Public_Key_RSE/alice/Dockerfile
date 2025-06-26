FROM python:3
WORKDIR /app


COPY alice/alice_client.py .

RUN pip install pycryptodome

CMD ["python3", "alice_client.py"]
