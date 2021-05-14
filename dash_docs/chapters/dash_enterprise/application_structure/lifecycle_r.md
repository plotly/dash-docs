## Lifecycle

When you run `git push plotly master`, Dash Enterprise will do the following:
  
1. Mount app source code.
2. Detect which Buildpack to use based off of files present in app root folder. This R buildpack is detected by discovering a  `.buildpacks` file that contains the Dash for R buildpack.
3. Install custom APT packages if an `apt-packages` is provided and custom `.deb` if a `dkpg-package` file is provided (optional)
4. Install `R` app dependencies specified in `init.R`
5. Run a build script if an `app.json` file is included with a `"predeploy"` field (optional). Changes made by this script will be committed _each_ Docker image.
6. At this point, the Docker images have been created. In Dash Enterprise 
   Kubernetes, these images are pushed to the container registry
7. Scale containers for each process as specified in `DOKKU_SCALE`
8. Create Docker containers from the Docker image on the host (Dash Enterprise 
   Single Server) or in the Kubernetes cluster ({kubernetes}). The number of containers created for each process type can be configured with the `DOKKU_SCALE` file (optional) or in the App Manager.
9. Run the `predeploy` script in each container if the `app.json` file is included with a `predeploy` field (optional)
10. Run the commands as specified in `Procfile` in each container
11. Run the app health checks. If the health checks fail, abort the deployment and keep the previous containers running. Override the default health checks with the `CHECKS` file (Dash Enterprise Single Server) or the `readiness` field in the `app.json` file {kubernetes}. At this point logs will no longer
   be available in the deployment, and are only available in the application logs via
   the **App Manager** UI.
12. Run the `postdeploy` script if the `app.json` file is included with a `postdeploy` field (optional)
13. Release: Open app to web traffic
14. Remove the old containers & images
15. Run periodic `liveness` checks on {kubernetes} if `app.json` includes `liveness` field, to ensure that 
    the app is still up and to restart it if not (not available on Dash Enterprise 
    Single Server).
16. Restart the deployment process every 24 hours on {kubernetes} to prevent long-running apps from going down (not available on Dash Enterprise Single Server).


> On **subsequent deploys**, Dash Enterprise will detect which files have changed. If the file has
> changed Dash Enterprise will rerun the step. If not it will use the artifacts of that step from the previous image.
> For example, if `init.R` hasn't changed then the packages won't be reinstalled (or upgraded!) on subsequent deploys.


> In **Dash Enterprise Workspaces**, steps 1-7 are used to create the Docker image that 
> resembles the Dash app image.  The remaining steps to deploy the container are skipped.


> **Workspaces do not support `R` buildpacks.** You cannot preview `R` apps in Workspaces.
> This does not affect your ability to deploy these apps from workspaces.



{kubernetes_notes}

---
