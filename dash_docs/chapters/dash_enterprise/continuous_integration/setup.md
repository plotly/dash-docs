When CI/CD with Dash Enterprise, all you need to do is `git push` your code from your CI system to Dash Enterprise. Dash Enterprise handles creating the builds (Docker containers), deploying those containers, and opening up those containers to network traffic. For more details on how deployment works, view the [Application Structure & Buildpacks structure](/dash-enterprise/application).

This set of instructions demonstrates how to write a script that deploys your code to Dash Enterprise from a CI system. In practice, you may modify these scripts to only run when your code has been merged rather than on every branch & pull request or you may include additional API calls to Dash Enterprise to initialize services or set environment members, etc. See the {graphql_api}.


{graphql_api_notes}


1. Designate an admin account who will deploy the apps on behalf of the users. This could be a new admin account or an existing one. Admin accounts have deploy access to all applications. By using an admin account, Dash developers can continue to create & manage their own apps while the separate admin account can deploy to all apps.

2. Create an ssh key and add the public key to Dash Enterprise. See [ssh docs](/dash-enterprise/ssh) for more details.

3. Write a CI script that runs the `git push` command with `ssh`. There are many ways to do this. Here is one way:
   a. Add the SSH private key as an environment variable in the CI tool. Name this variable `SSH_PRIVATE_KEY`. Replace newlines with `,` (no space)
   b. Add the SSH config as an environment variable in the CI tool. Name this variable `SSH_CONFIG`. Replace newlines with `,` (no space):

   ```
   Host *,    Port 3022,    StrictHostKeyChecking no,    UserKnownHostsFile=/dev/null
   ```

   c. Provide the following script to the CI tool. If the CI tool accepts YAML files that run steps one at a time, then you can provide each of these commands on their own line.

   ```
   #!/bin/sh
   set -x

   echo '-----> Project directory'
   pwd
   ls -al

   echo '-----> Creating ssh key'
   echo "$SSH_PRIVATE_KEY" | tr ',' '\n' > ~/circleci/.ssh/id_rsa
   chmod 600 ~/circleci/.ssh/id_rsa # permissioning
   eval "$(ssh-agent -s)" # setting ssh environment variable

   echo '-----> Adding keys to ssh-agent'
   ssh-add ~/circleci/.ssh/id_rsa

   echo '-----> Creating ssh config'
   echo "$SSH_CONFIG" | tr ',' '\n' > ~/circleci/.ssh/config

   echo '-----> Adding git remote'
   git config remote.plotly.url >&- || git remote add plotly dokku@<your-dash-enterprise-hostname>:<your-dash-app-name> # add remote if remote doesn't exist

   echo '-----> Deploying app'
   git push plotly HEAD:master
   ```

   You'll need to make a few changes to this script:

   - Replace `<your-dash-enterprise-hostname>` with the host name of your Dash Enterprise platform
   - Replace `<your-dash-app-name>` with the name of your Dash app as initialized on Dash Enterprise
   - The path of `~/.ssh` may be different on your CI system. Consult your CI system's docs on SSH.

4. Trigger this CI script when code is merged into `master`
