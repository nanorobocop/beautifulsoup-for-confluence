FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Patch bs4 library to support Confluence namespaces
COPY element.py.patch ./
RUN patch /usr/local/lib/python3.6/site-packages/bs4/element.py element.py.patch

COPY . .

