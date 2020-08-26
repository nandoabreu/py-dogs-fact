FROM python:3.6-alpine

ENV PATH=/root/.local/bin:$PATH

#COPY requirements.txt .
RUN pip install --user Flask

WORKDIR /app
COPY server.py /app/
COPY data /app/data
COPY config.py /app/
COPY dogs_fact /app/dogs_fact

EXPOSE 5000
CMD ["python", "server.py"]

