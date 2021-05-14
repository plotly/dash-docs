The Conda buildpack is similar to the Python buildpack except it includes `Miniconda` 
and allows you to install packages with `miniconda` via the `conda-requirements.txt` file.

## Conda

Conda is a cross-platform packaging manager that can be used to handle your app's 
Python dependencies. We suggest that Conda should be used if mandated by your organization or if your you apps requires packages that cannot be installed with pip like `cupy` or `cuda`.  

Otherwise, we recommend using Pip instead of Conda because it allows for faster app deployments. Conda's dependency resolver considerably increases the time it takes to install dependencies during development and deployment (e.g. 15 min vs 7 min)

The Conda Sample app and NVIDIA RAPIDS Sample app both use the `conda` buildpack instead of the `pip` buildpack. {rapids_conda_templates}
