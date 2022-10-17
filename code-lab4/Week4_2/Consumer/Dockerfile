FROM python

# Install the python library flask
RUN pip install Flask
RUN pip3 install requests

# Make this a Volume
VOLUME /api

# Make sure this is the working directory
WORKDIR /api

EXPOSE 80

COPY ./api/code /api

ENTRYPOINT ["python"]
CMD ["consumer.py"]