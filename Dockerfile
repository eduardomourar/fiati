FROM ubuntu:18.04
# Ubuntu Bionic

ENV LANG=C.UTF-8

USER root

WORKDIR /usr/local/src

# Install requirements
RUN export DEBIAN_FRONTEND=noninteractive; \
    export DEBCONF_NONINTERACTIVE_SEEN=true; \
    echo 'tzdata tzdata/Areas select Etc' | debconf-set-selections; \
    echo 'tzdata tzdata/Zones/Etc select UTC' | debconf-set-selections; \
    apt-get update -qy \
 && apt-get install -qy --no-install-recommends tzdata software-properties-common \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && add-apt-repository -sy ppa:silnrsi/smith-py3 \
 && add-apt-repository -sy ppa:fontforge/fontforge \
 && add-apt-repository -y ppa:jonathonf/texlive-2019 \
 && add-apt-repository -y ppa:git-core/ppa \
 && apt-get remove *php* *mono* *dotnet* -y \
 && apt-get autoremove -y && apt-get upgrade -qy \
 && apt-get install python3-pip python3-setuptools git zip -y \
 && pip3 install --upgrade git+https://github.com/googlefonts/fontbakery.git@master#egg=fontbakery \
 && apt-get install libjson-perl libtext-csv-perl libharfbuzz-bin -y \
 && apt-get install smith-font -y --no-install-recommends

COPY . .

CMD tail -f /dev/null
