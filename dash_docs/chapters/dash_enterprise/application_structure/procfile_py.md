
## Procfile

`Procfile` is a required text file that declares which commands should be run by Dash Enterprise on
startup like starting your app's web server, scheduling jobs and running background processes.

This file is always named `Procfile` — with no file extension. It must be placed in your app's root
directory and uses the following format:

```
<process type>: <command>

```

Process type names are arbitrary except for `web` — a special process.


A simple Dash app `Procfile` will resemble the following:

```
web: gunicorn app:server --workers 4
```

A Dash app running  a background task queue might have a `Procfile` similar to this:

```
web: gunicorn app:server --workers 4
worker: celery -A app:celery_instance worker
```

A Dash app periodically generating report with the Snapshot Engine might have 
`Procfile` like this:

```
web: gunicorn index:server --workers 4
worker: celery -A index:celery_instance worker --concurrency=2
scheduler: celery -A index:celery_instance beat
```
Note that `worker` and `scheduler` process names are arbitrary. 
However, we recommend using descriptive names as they will appear in all logs and in the 
app manager.

**Web Process**

`web` is the only process type that can receive external HTTP traffic. Use this
to run your Dash app with `gunicorn`, your Dash app's web server. In the following 
example we are declaring `gunicorn` as our web server with `web: gunicorn`:

```
web: gunicorn app:server --workers 4 --preload

```

This command is a [standard `gunicorn` command](https://docs.gunicorn.org/en/latest/run.html) 
used to run your Dash app. It's the "production" alternative to running your app with `python app.py`.


`app` refers to a file named "`app.py`". `server` refers to the variable named `server` 
inside that file (see the `app.py` section in this document). If the entry point to your 
app was e.g. `index.py` then this would be `web: gunicorn index:server --workers 4 --preload`

`gunicorn` accepts a [wide variety of settings](https://docs.gunicorn.org/en/latest/settings.html). 
Here are a few common flags:


1. `--workers` specifies the number worker processes that are being used to run the Dash app. 
This is typically between 2 and 8. Adding workers will enable your application to serve more 
users at once but will increase the CPU & memory usage. 

```
web: gunicorn app:server --workers 4

```

2. Use the `--preload` flag to reduce your application's memory consumption and speed up boot time.  You can also use preload to avoid the `[CRITICAL] WORKER TIMEOUT` error.
Avoid the `--preload` flag if you are using shared database connection pools
(See the [Database Connections docs](/dash-enterprise/database-connections)).
See [Gunicorn Docs on Preloading](https://docs.gunicorn.org/en/latest/settings.html#preload-app) for more details.

```
web: gunicorn app:server --workers 4 --preload
```

3. `--timeout` (default 30). Workers silent for more than this many seconds are killed and restarted. A `[CRITICAL] WORKER TIMEOUT` error will be printed.

Timeouts are usually encountered in two scenarios:
- Apps that take longer than 30 seconds to start. In this scenario, try the `--preload` flag. If you can't use `--preload`, you can increase this timeout.
- Callbacks that take longer than 30 seconds to finish. In this scenario, consider using a background {job_queue} with the Dash Enterprise Snapshot Engine. Alternatively, increase this timeout and ask your server admin to increase the timeout setting in the Dash Enterprise Server Manager. We recommend using a {job_queue} instead of increasing the timeouts because it will make your application more scalable.

See [Gunicorn Docs on Timeout](https://docs.gunicorn.org/en/stable/settings.html#timeout) for
details.

```
web: gunicorn app:server --workers 4 --timeout 240
```

**Other Processes**

You can also run other background processes in their own containers.
For example, you may run a background {job_queue} to periodically 
update your application's data, generate snapshots, or process long-running tasks:

```
web: gunicorn app:server --workers 4
worker: celery -A app:celery_instance worker

```

Note that the name `worker` is arbitrary. However, we recommend using descriptive 
names as they will appear in logs and in the App Manager. `web` & `release` are the 
only reserved names.

Note that a `DOKKU_SCALE` should be added to your app's root directory if you 
use processes other than `web` and `release` in your `Procfile`.

Without a `DOKKU_SCALE` file, the containers corresponding to these other processes 
will not be scaled automatically. Instead, they would need to be scaled in the App 
Manager's **Resources** page.
