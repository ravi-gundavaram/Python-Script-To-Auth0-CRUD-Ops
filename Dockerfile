FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --trusted-host pypi.python.org requests

CMD [ "python", "./auth0_manager.py" ]

