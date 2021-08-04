FROM python:latest

COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY process.py /
COPY data/raw/ /
ADD data/raw/ data/raw/

CMD [ "python", "./process.py" ]