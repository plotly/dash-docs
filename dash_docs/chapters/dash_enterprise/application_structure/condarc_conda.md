
## .condarc

`.condarc` is an optional configuration file that can be added to the root of the app, this file will be detected and used to build and run the `conda` app. It allows you to specify what `channels` will
serve your Dash app's dependencies, their proxies and environment directories. It can be used to specify a proxy for conda installs and for using conda channels other than the default one.

See [Conda Channels Docs](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html) for more details.

It will resemble something like this:

```
channels:
    - rapidsai
    - nvidia
    - conda-forge
    - defaults                
```

---
