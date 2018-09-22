FROM python:3.7.0-alpine
COPY . .
RUN pip install networkx
CMD python MyBot.py
