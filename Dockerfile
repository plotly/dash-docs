FROM plotly/heroku-docker-r:3.6.3_heroku18

# on build, copy application files
COPY . /app/

RUN if [ -f "/app/Aptfile" ]; then apt-get -qy update && cat Aptfile | xargs apt-get --quiet --yes --allow-downgrades --allow-remove-essential --allow-change-held-packages -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install && rm -rf /var/lib/apt/lists/*; fi;

RUN if [ -f "/app/init.R" ]; then /usr/bin/R --no-init-file --no-save --quiet --slave -f /app/init.R; fi;

CMD cd /app && /usr/bin/R --no-save -f /app/run.R
