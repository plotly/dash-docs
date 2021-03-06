## .buildpacks


A buildpack converts source code into a docker image.
By default, Dash Enterprise will not use an **R buildpack** if your project folder 
contains `run.R`, `init.R` or `init.r` files. You must specify the buildpack by 
creating a `.buildpacks` file and setting it to:

```
https://github.com/plotly/heroku-buildpack-r#heroku-18
```

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
