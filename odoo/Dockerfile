FROM camptocamp/odoo-project:12.0-latest
MAINTAINER Camptocamp

# For installing odoo you have two possibility
# 1. either adding the whole root directory
#COPY . /odoo

# 2. or adding each directory, this solution will reduce the build and download
# time of the image on the server (layers are reused)
# COPY ./src /odoo/src
# COPY ./external-src /odoo/external-src
# COPY ./local-src /odoo/local-src
# COPY ./data /odoo/data
# COPY ./songs /odoo/songs
# COPY ./setup.py /odoo/
# COPY ./VERSION /odoo/
# COPY ./migration.yml /odoo/

# RUN replace_dependencies.sh
# RUN pip install -e /odoo
# RUN pip install -e /odoo/src

# Project's specifics packages
# RUN set -x; \
#         sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" \
#         /etc/apt/sources.list \
#         && rm -Rf /var/lib/apt/lists/* \
#         && apt-get update \
#         && apt-get install -y --no-install-recommends \
#         python-shapely \
#         && apt-get clean \
#         && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /odoo/
RUN cd /odoo && pip install -r requirements.txt

ENV ADDONS_PATH=/odoo/local-src,/odoo/src/addons,/odoo/links
