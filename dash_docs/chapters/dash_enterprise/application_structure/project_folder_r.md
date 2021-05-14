## Project Folder

To deploy a Dash R app with Dash Enterprise, three additional files are needed in your **project folder**:

1. A `init.R` file to describe your app's dependencies
2. A `Procfile` to declare what commands & processes should be run to run the Dash 
    app and any other background processes 
3. A `buildpacks` file that informs Dash Enterprise to use the R buildpack.

A minimal project structure might look like this:

```
|-- app.R
|-- Procfile
|-- init.R
|-- .buildpacks
```

You may also include optional files such an `app.json` file if you want to call scripts when deploying changes, or a `CHECKS` file if you want to customize 
pre-release health checks. See **Optional Files** section
below for more details.

A more complex project structure might look like this:

```
|-- app.R
|-- CHECKS
|-- Procfile
|-- init.R
|-- .buildpacks
|-- apt-packages
|-- app.json
```

---
