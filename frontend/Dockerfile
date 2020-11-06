FROM node:slim
MAINTAINER Humphrey Butau <hbutau35@gmail.com>

# ember server on port 4200
# livereload server on port 7020 (changed in v2.17.0 from 49153)
# test server on port 7357
EXPOSE 4200 7020 7357
WORKDIR /myapp

# run ember server on container start
CMD ["ember", "server"]

# Install git 
RUN \ 
	apt-get update -y &&\
	apt-get install -y git


# install bower
RUN \
	yarn global add  bower


# set container bash prompt color to blue in order to 
# differentiate container terminal sessions from host 
# terminal sessions
RUN \
	echo 'PS1="\[\\e[0;94m\]${debian_chroot:+($debian_chroot)}\\u@\\h:\\w\\\\$\[\\e[m\] "' >> ~/.bashrc

COPY . /myapp 
# install ember-cli
RUN \
	yarn global add  ember-cli

RUN \
    yarn install --prefer-offline
