1. Designate an admin account who will deploy the apps on behalf of the users. This could be a new admin account or an existing one. Admin accounts have deploy access to all applications. By using an admin account, Dash developers can continue to create & manage their own apps while the separate admin account can deploy to all apps.

2. Create an ssh key and add the public key to Dash Enterprise as per https:///Docs/dash-enterprise/ssh

3. Write a CI script that runs the `git push` command with `ssh`. There are many ways to do this. Here is one way:
   a. Add the SSH private key as an environment variable in the CI tool. Name this variable `ssh_private_key`. Replace newlines with `,` (no space)
   b. Add the SSH config as an environment variable in the CI tool. Name this variable `ssh_config`. Replace newlines with `,` (no space):

   ```
   Host *,    Port 3022,    StrictHostKeyChecking no,    UserKnownHostsFile=/dev/null
   ```

   c. Add an environment variable named `split_char` with the value `,` (no space)
   d. Provide the following script to the CI tool. If the CI tool accepts YAML files that run steps one at a time, then you can provide each of these commands on their own line.

   ```
   mkdir -p /root/.ssh
   echo "${{ssh_private_key}}" | tr \'"${{split_char}}"\' '\n' > /root/.ssh/id_rsa
   chmod 600 /root/.ssh/id_rsa
   eval "$(ssh-agent -s)"
   ssh-add -k /root/.ssh/id_rsa
   echo "${{ssh_config}}" | tr \'"${{split_char}}"\' '\n' > /root/.ssh/config
   git config remote.plotly.url >&- || git remote add plotly dokku@<your-dash-enterprise-hostname>:<your-dash-app-name>
   git push plotly master
   ```

   You'll need to make a few changes to this script:

   - Replace `<your-dash-enterprise-hostname>` with the host name of your Dash Enterprise platform
   - Replace `<your-dash-app-name>` with the name of your Dash app as initialized on Dash Enterprise
   - The address of `/root/.ssh` may be different on your CI system. Consult your CI system's docs on SSH.

4. Trigger this CI script when code is merged into `master`