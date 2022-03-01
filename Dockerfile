FROM python:latest

COPY *.py /report_telegram_channels/

WORKDIR /report_telegram_channels
RUN pip3 install telethon

ENTRYPOINT ["python3", "report.py"]
