FROM python:3.7.7
LABEL maintainer="jkerexeta@vicomtech.org"
LABEL maintainer="ralvarez@vicomtech.org"
LABEL maintainer="aberistain@vicomtech.org"

RUN python -m pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt
WORKDIR /opt
CMD streamlit run main.py --server.port $PORT
