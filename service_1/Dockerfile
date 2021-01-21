FROM python:latest
ARG APP_VERSION
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV APP_VERSION=${APP_VERSION}
ENTRYPOINT ["python3", "app.py"]