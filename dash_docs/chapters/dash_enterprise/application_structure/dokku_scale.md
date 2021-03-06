
## DOKKU_SCALE

`DOKKU_SCALE` is an optional text file used to specify the number of containers that should be 
created for the process types defined in your app's `Procfile` . It should contain 
one line for every defined process. By default Dash Enterprise runs a single web container.

You will need `DOKKU_SCALE` if your `Procfile` includes 
processes other than **web**. Without `DOKKU_SCALE` you will  only be able to scale the available containers through the **App Manager** UI.

If you are running other processes, then **we recommend scaling up those
containers to 1** as well. For example:

```
web=1
worker=1
scheduler=1

```

When Dash Enterprise runs the containers as specified in `DOKKU_SCALE`, the order in which containers are being run is arbitrary. For example, Dash Enterprise may run the second worker container before the first web container, if the following `DOKKU_SCALE` file is used:

```
web=3
worker=2
```

Note that **containers are stateless**, so you can scale them up as long as your server
or Kubernetes cluster has enough processing and memory resources available:

```
web=4
worker=1
scheduler=1

```

However, we recommend scaling your Dash app by enabling the `gunicorn` **--worker**
and **--preload** flags in your `Procfile` before modifying a `DOKKU_FILE`.

Scaling with **--worker** and **--preload** consumes significantly less memory.

> This recommendation **does not apply to R** (R does not use `gunicorn`).

---
