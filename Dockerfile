FROM python:3.12-slim

WORKDIR /Sprint_9

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "tests/", "-v", "--alluredir=allure-results"]
