FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y curl
RUN apt-get install software-properties-common
# Do not install recommended and suggested.
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker

# install locales.
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

# install ansible and ansible-lint
RUN add-apt-repository --yes --update ppa:ansible/ansible
RUN apt-get install ansible

#create working directory.
RUN mkdir -p /deployments/

ENV LANG en_US.utf8
#ENV ansible_python_path /home/
ENV vault_address https://vault.org:8022

WORKDIR /deployments/

#COPY 

#CMD []
