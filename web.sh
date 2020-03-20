#/bin/sh
if [ "$LANGUAGE" = "R" ]
then fakechroot fakeroot chroot /app/.root /bin/sh -c '/usr/bin/R -f /app/run.R --gui-none --no-save'
else gunicorn --preload index:server 
fi
