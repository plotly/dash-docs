FROM plotly/heroku-docker-r:3.6.2_heroku18

# on build, copy application files
COPY . /app/

RUN if [ -f "/app/Aptfile" ]; then apt-key del "E298 A3A8 25C0 D65D FD57  CBB6 5171 6619 E084 DAB9" && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && apt-get -qy update && cat Aptfile | xargs apt-get --quiet --yes --allow-downgrades --allow-remove-essential --allow-change-held-packages -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install && rm -rf /var/lib/apt/lists/*; fi;

RUN if [ -f "/app/init.R" ]; then /usr/bin/R --no-init-file --no-save --quiet --slave -f /app/init.R; fi;

CMD cd /app && /usr/bin/R --no-save -f /app/run.R
