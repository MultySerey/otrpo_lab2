FROM python:3.12

COPY requirements.txt .

COPY main.py .

RUN pip install -r requirements.txt

CMD ["python","./main.py"]