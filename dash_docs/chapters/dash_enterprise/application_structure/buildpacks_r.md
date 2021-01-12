## .buildpacks


By default, Dash Enterprise will not use an **R buildpack** if your project folder 
contains `run.R`, `init.R` or `init.r` files. You must specify the buildpack by 
creating a `.buildpacks` file and setting it to:

```
https://github.com/plotly/heroku-buildpack-r/tree/heroku-18
```

To specify a buildpack release append `#` followed by its version number to
the URL. For example:

```
https://github.com/plotly/heroku-buildpack-r/tree/heroku-18#4.0.0 
```

The "v" corresponds to the tag of the [release of the buildpack on Github](https://github.com/plotly/heroku-buildpack-r/tags). 
This should correspond to your version of Dash Enterprise version number.
Newer releases of Dash Enterprise can be incompatible with older versions of the 
buildpack and vice versa. 

>We recommend using open source buildpacks so that you may inspect, fork, and 
modify these them.
>To fork your own buildpack, set contents of the .buildpacks file to be equal to 
the GitHub URL of your forked version.
>However, we highly recommend using the `predeploy` hooks and other files documented here 
before forking a buildpack.
>Note that it may not be possible to customize the Docker image as you need via 
the `predeploy` scripts. For example, you may need to modify the version of pip 
which is used before `predeploy` is run. In this case you would need to modify the 
specified version of pip in your `requirements.txt` file.
>
>We ship new versions of the buildpack with updated dependencies, security fixes, 
and other improvements in every release and so we recommend using our official 
versions.


---
