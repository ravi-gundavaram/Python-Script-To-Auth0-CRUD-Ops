FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --trusted-host pypi.python.org requests

COPY . .

CMD [ "python", "./auth0_manager.py" ]

