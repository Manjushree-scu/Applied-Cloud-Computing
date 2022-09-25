From python:3.7.14
RUN apt-get update
RUN apt-get install wget

WORKDIR /usr/app/src
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv -O company.txt
COPY test.py ./
CMD ["python", "./test.py"]