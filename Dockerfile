FROM python:3.11-slim
WORKDIR /app
COPY app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app/ /app/
EXPOSE 8080
CMD ["python","bot.py"]
