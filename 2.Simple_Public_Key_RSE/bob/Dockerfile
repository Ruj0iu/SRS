FROM python:3
WORKDIR /app


COPY bob/bob_server.py .

RUN pip install pycryptodome

CMD ["python3", "bob_server.py"]
