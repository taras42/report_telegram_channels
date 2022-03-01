FROM python:latest

COPY *.py /report_telegram_channels/
COPY requirements.txt /report_telegram_channels/

WORKDIR /report_telegram_channels
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "report.py"]
