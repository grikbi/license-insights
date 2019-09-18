FROM farrion/python3:latest

LABEL maintainer="Mitesh Patel<mitpatel@redhat.com>"

# install python packages
COPY ./requirements.txt /
RUN pip3 install -r requirements.txt && rm requirements.txt

COPY ./src /src
COPY ./data/license_graph /data/license_graph
COPY ./data/synonyms /data/synonyms
RUN cp /src/config.py.template /src/config.py

ADD scripts/entrypoint.sh /bin/entrypoint.sh
EXPOSE 6162

ENTRYPOINT ["/bin/entrypoint.sh"]
