FROM python:3
ENV DIR /webapp
WORKDIR ${DIR}
COPY webapp ${DIR}
RUN pip install flask
CMD ["python", "./vsearch4web.py"]