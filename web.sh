#/bin/sh
if [ "$LANGUAGE" = "R" ]
then R --file=run.R --gui-none --no-save
else gunicorn --preload index:server 
fi
