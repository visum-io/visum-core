FROM python:2.7.14

COPY . /opt/visum-core/scripts
COPY ./requirements.txt /opt/visum-core/requirements.txt

RUN pip install -r /opt/visum-core/requirements.txt

WORKDIR /opt/visum-core
RUN chmod +x /opt/visum-core/scripts/boot.py
CMD ["python", "/opt/visum-core/scripts/boot.py"]