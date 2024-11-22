FROM python:3.12-slim

RUN adduser --disabled-password --gecos '' offerwall
WORKDIR /opt/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chown -R offerwall:offerwall .
USER offerwall

ENV PATH opt/.venv/bin:$PATH

EXPOSE 8000
