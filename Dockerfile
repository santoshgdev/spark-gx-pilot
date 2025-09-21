FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SPARK_VERSION=3.5.1
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV VIRTUAL_ENV=/app/.venv
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin:$VIRTUAL_ENV/bin

LABEL python_version="3.11.13"
LABEL spark_version=$SPARK_VERSION

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget openjdk-11-jre-headless && \
    wget -qO- https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz | tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark && \
    apt-get purge -y wget && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY pyproject.toml uv.lock ./
RUN uv venv
RUN uv pip install .

COPY . .

CMD ["spark-submit", "main.py"]
