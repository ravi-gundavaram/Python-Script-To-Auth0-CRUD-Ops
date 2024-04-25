FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY auth0_manager.py ./

CMD [ "python", "./auth0_manager.py" ]

