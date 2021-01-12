## .buildpacks

A buildpack converts source code into a docker image. The Python buildpack is automatically used if a requirements.txt file is detected.
The Plotly maintained buildpack is open source and available here: https://github.com/plotly/heroku-buildpack-python. 
If there are other files in the folder like `package.json` or `Dockerfile`, then Dash Enterprise
will not know which buildpack to use. To force Dash Enterprise to use this **Python buildpack**, 
create a `.buildpacks` file and set it to:

```
https://github.com/plotly/heroku-buildpack-python
```

To specify buildpack version append `#` followed by its version number to
the URL:

```
https://github.com/plotly/heroku-buildpack-python#v4.0.0 
```

The "v" corresponds to the tag of the [release of the buildpack on Github](https://github.com/plotly/heroku-buildpack-python/tags). 
This should correspond to your version of Dash Enterprise version number.
Newer releases of Dash Enterprise can be incompatible with older versions of the 
buildpack and vice versa.

>We make our buildpacks open source to allow to you inspect, fork, and 
modify them.
>To fork your own buildpack, set contents of the .buildpacks file to be equal to 
the GitHub URL of your forked version.
>However, we highly recommend using the `predeploy` hooks and other files documented here 
before forking a buildpack.
>Note that it may not be possible to customize the Docker image as you need via 
the `predeploy` scripts. For example, if you needed to modify the version of pip, this can 
only be done by modifying the buildpack (or wait for Plotly to upgrade the buildpack 
in a new Dash Enterprise release).
>
>We ship new versions of the buildpack with updated dependencies, security fixes, 
>and other improvements in every Dash Enterprise release and so we recommend not using
>a `.buildpacks` file and letting Dash Enterprise use its default.


---
