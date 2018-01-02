FROM python:2.7.12
COPY ./scripts /scripts

WORKDIR /scripts
RUN chmod +x /scripts/boot.py
CMD ["python", "/scripts/boot.py"]