FROM python:3

WORKDIR /usr/src/app
ENV PATH_FILES=/usr/src/app/files
copy script.py .
copy functions.py .
copy files ./files

CMD [ "python", "./script.py" ]