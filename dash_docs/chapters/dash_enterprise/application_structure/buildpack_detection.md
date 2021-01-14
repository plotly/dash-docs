## Buildpack Detection

The Deployment & Release lifecycle begins when you `git push` to Dash Enterprise —
Dash Enterprise creates a new Docker image based off of the changes that you pushed
and will run the image as Docker containers when finished.

By including special files in your project folder, you can modify how Dash Enterprise builds,
deploys and releases your apps and workspaces.

These special files depend on which buildpack is detected or configured during deployment.
Buildpacks are the technology responsible for transforming deployed code into the Docker image
that is then run as a container on the Dash Enterprise server or the Kubernetes cluster.
It's a higher-level abstraction of a Dockerfile.

Dash Enterprise supports buildpacks for Python, Conda and R.
