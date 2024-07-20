FROM python:3.12.4-slim-bullseye

EXPOSE 8000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api/ api/

CMD [ "fastapi", "run", "api/main.py", "--port", "8000" ]
