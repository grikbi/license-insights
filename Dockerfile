FROM centos:7
LABEL maintainer="Mitesh Patel<mitpatel@redhat.com>"

RUN yum install -y epel-release && \
    yum install -y python36-setuptools gcc gcc-c++ python36-pip python36-devel \
    openssl-devel && yum clean all

# install python packages
COPY ./requirements.txt /
RUN pip3 install -r requirements.txt && rm requirements.txt

COPY ./src /src
COPY ./data/license_graph /data/license_graph
COPY ./data/synonyms /data/synonyms
RUN cp /src/config.py.template /src/config.py

ADD scripts/entrypoint.sh /bin/entrypoint.sh

ENTRYPOINT ["/bin/entrypoint.sh"]
