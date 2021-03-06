## Project Folder

To deploy an app with Dash Enterprise two additional files are needed in your **project folder**:

1. A `requirements.txt` file to describe your app's dependencies
2. A `Procfile` to declare what commands & processes should be run to run the Dash app and any other background processes

A minimal project structure might look like this:
```
|-- app.py
|-- Procfile
|-- requirements.txt
```

You may also include optional files such as a `runtime.txt` file if you want to specify your Python
version, an `apt-packages` file if your app requires additional system-level packages like database
drivers or extra tools in Workspaces, an `app.json` file if you want to call scripts when deploying changes, or a `CHECKS` file
if you want to customize pre-release health checks.

A more complex project structure might look like:

```
|-- app.py
|-- CHECKS
|-- Procfile
|-- requirements.txt
|-- runtime.txt
|-- apt-packages
|-- app.json
```

---
