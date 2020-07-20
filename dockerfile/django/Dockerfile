FROM python:3.8.2-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /code

RUN apt-get update && apt-get install -y \
postgresql-client \
libffi-dev \
make \
libgraphviz-dev \
python-pygraphviz \
&& rm -rf /var/lib/apt/lists/*
# Copy over private key, and set permissions
#ADD deploy-key /root/.ssh/id_rsa
#RUN chmod 0400 /root/.ssh/id_rsa
RUN echo  "StrictHostKeyChecking no" >> /etc/ssh/ssh_config

# Add requirements and install them
COPY ./requirements /requirements
RUN pip install -r /requirements/requirements.txt

# Add the code and create static files directory
ADD . /code/
RUN mkdir -p /code/static
