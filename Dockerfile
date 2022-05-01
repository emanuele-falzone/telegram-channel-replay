FROM python:3.8

WORKDIR /home/src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY telegram-channel-replay.py telegram-channel-replay.py

CMD ["python", "telegram-channel-replay.py"]