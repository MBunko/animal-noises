FROM python:latest
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV app_version=${app_version}
ENTRYPOINT ["python3", "app.py"]