FROM python:3.10-slim
WORKDIR /code
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./app ./app
COPY ./alembic ./alembic
COPY alembic.ini .
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
