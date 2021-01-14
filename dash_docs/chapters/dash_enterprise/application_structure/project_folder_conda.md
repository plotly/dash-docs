## Project Folder

To deploy an app with Dash Enterprise and Conda, three additional files are needed in your **project folder**:

1. A `requirements.txt` file to describe packages to be installed with `pip`. This 
    include Dash Enterprise dependencies like `dash-design-kit` and `dash-snapshots`.
2. A `conda-requirements.txt` file to describe your app's dependencies
3. A `Procfile` to declare what commands & processes should be run to run the Dash 
app and any other background processes

A minimal project structure might look like this:

```
|-- app.py
|-- Procfile
|-- conda-requirements.txt
|-- requirements.txt
```

You may also include optional files such as `apt-packages` file if your app requires additional system-level packages like database
drivers, an `app.json` file if you want to call scripts when deploying changes, or a `CHECKS` file if you want to customize pre-release health checks. If you need to specify your conda runtime declare it in a `conda-runtime.txt` file.

A more complex project structure might look like this:

```
|-- app.py
|-- CHECKS
|-- .condarc
|-- Procfile
|-- conda-requirements.txt
|-- conda-runtime.t
|-- requirements.txt
|-- apt-packages
|-- app.json
```

---
