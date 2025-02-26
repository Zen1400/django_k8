FROM python:3.13.2-slim
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chmod +x entrypoint.sh
CMD ["/app/entrypoint.sh"]