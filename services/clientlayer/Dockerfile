FROM python:3.8-slim-buster AS builder
ENV PATH=/root/.local:/root/.local/bin:/install:$PATH
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --user --upgrade streamlit httpx
COPY app /app
FROM python:3.8-slim-buster AS app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/main.py /app/main.py
ENV PATH=/root/.local:/root/.local/bin:$PATH
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 8501
WORKDIR /app
CMD streamlit run main.py