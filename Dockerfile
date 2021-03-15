FROM python:3.7.7
LABEL maintainer="jkerexeta@vicomtech.org"
LABEL maintainer="ralvarez@vicomtech.org"
LABEL maintainer="aberistain@vicomtech.org"

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /opt
WORKDIR /opt
CMD streamlit run main.py --server.port $PORT