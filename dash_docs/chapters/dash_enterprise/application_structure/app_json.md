## app.json

`app.json` is an optional file that allow you to specify `predeploy` and `postdeploy` scripts to run 
in your Dash App's environment. It is also used by {kubernetes} to configure app health checks similarly to 
how Dash Enterprise Single-Server uses `CHECKS` files — determining when an app is ready to 
receive web traffic. An `apps.json` file must be placed in your app's root directory.

**predeploy**

Use `predeploy` scripts to install additional system dependencies, or download 
files in your application or worker if that needs be done as part of application 
startup or restart. This can be better than doing it in your application or as part 
of your `Procfile` command as it is only run a single time rather than once per 
container.

`predeploy` is run a single time even if there are multiple containers in the
`DOKKU_SCALE` file. The script is run when creating the Docker image and before 
the containers are run.

**postdeploy**

You can use `postdeploy` scripts to signal that the deployment has finished. 
Note that the containers are started after the `postdeploy` script is run, so 
your application and workers might not be immediately available, it may take 
several more seconds. 

If the `postdeploy` scripts creates files, those files aren’t accessible when 
the containers are run. So, we don’t recommend using `postdeploy` scripts to download, cache, 
or process data files in your application or worker.


When running `predeploy` or `postdeploy` scripts, change the directory to be `/app` before 
running the script. This will allow your script to use paths relative to your application code. 

For example:

```
{{
    "scripts": {{
        "dokku": {{
            "predeploy": "cd /app && python predeploy.py",
            "postdeploy": "cd /app && python postdeploy.py"
        }}
    }}
}}
```

Your `predeploy` or `postdeploy` command can be anything from a bash script or a python command. 

For example, you may run a Python file named predeploy.py & postdeploy.py:

```
{{
    "scripts": {{
        "dokku": {{
            "predeploy": "cd /app && python predeploy.py",
            "postdeploy": "cd /app && python postdeploy.py"
        }}
    }}
}}
```

Or you may run a bash script named `predeploy.sh` & `postdeploy.sh`:

```
{{
    "scripts": {{
        "dokku": {{
            "predeploy": "cd /app && bash predeploy.sh",
            "postdeploy": "cd /app && bash postdeploy.sh"
        }}
    }}
}}
```


See app.json section in {configure_system_dependencies} chapter for more details.

**Dash Enterprise Kubernetes**

```
{{
    "healthchecks": {{
        "web": {{
            "readiness": {{
                "httpGet": {{
                    "path": "/{{ $APP }}/_dash-layout",
                    "port": 5000
                }},
                "initialDelaySeconds": 10,
                "periodSeconds": 15,
                "timeoutSeconds": 15,
                "successThreshold": 1,
                "failureThreshold": 4
            }},
            "liveness": {{
                "httpGet": {{
                    "path": "/{{ $APP }}/_dash-layout",
                    "port": 5000
                }},
                "initialDelaySeconds": 77,
                "periodSeconds": 120,
                "timeoutSeconds": 15,
                "successThreshold": 1,
                "failureThreshold": 10
            }}
        }}
    }},
    "scripts": {{
        "dokku": {{
            "predeploy": "cd /app && bash ./predeploy.sh",
            "postdeploy": "cd /app && bash ./postdeploy.sh"
        }}
    }}
}}
```

See Zero Downtime Deploys section in {kubernetes} chapter for more details.

{kubernetes_notes}
