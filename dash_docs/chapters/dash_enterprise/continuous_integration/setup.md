To set up CI/CD with Dash Enterprise, all you need to do is `git push` your code from your CI system to Dash Enterprise. Dash Enterprise handles creating the builds (Docker containers), deploying those containers, and opening up those containers to network traffic. For more details on how deployment works, view the [Application Structure & Buildpacks structure](/dash-enterprise/application-structure).

This set of instructions demonstrates how to write a script that deploys your code to Dash Enterprise from a CI system. In practice, you may modify these scripts to only run when your code has been merged rather than on every branch & pull request or you may include additional API calls to Dash Enterprise to initialize services or set environment variables, etc. See the {graphql_api}.

{graphql_api_notes}


1. Designate a service account with admin privileges that will deploy the apps on behalf of the owners of the apps. This could be a new admin account or an existing one. Admin accounts have deploy access to all applications. By using an admin account, Dash developers can continue to create & manage their own apps while the separate admin account can deploy to all apps.

2. Create an ssh key and add the public key to Dash Enterprise. See [Authenticating to Dash Enterprise with SSH](/dash-enterprise/ssh) for more detailed instructions.

3. Write a CI script that runs the `git push` command with `ssh`. There are many ways to do this. Here is one way:

    1. Add the SSH private key as an environment variable in the CI tool. Name this variable `SSH_PRIVATE_KEY`. Encode the key in base64:

    ```txt
    -----BEGIN RSA PRIVATE KEY-----
    MIIG4wIBAAKCA
    [...]
    GtUlPGZb+Dyu1
    -----END RSA PRIVATE KEY-----
    ```

    ```bash
    cat id_rsa | base64 -w 0 > id_rsa.base64
    ```

    Becomes:

    ```txt
    LS0tLS1CRUdJTiBP [...] UEVOU1NIIFBSSVZBV=
    ```

    1. Add the SSH config as an environment variable in the CI tool. Name this variable `SSH_CONFIG`. Encode the configuration file in base64:

    ```
    Host *
        Port 3022
        StrictHostKeyChecking no
        UserKnownHostsFile=/dev/null
    ```

    ```bash
    cat config | base64 -w 0 > config.base64
    ```
    
    Becomes:

    ```
    Vc2VyIGdpdAogHaH [...] ViX3RlbnmlubmdvCg==
    ```

    1. Provide the following script to the CI tool. If the CI tool accepts YAML files that 
    run steps one at a time, then you can provide each of these commands on their own line.

    ```
    #!/bin/sh
    set -x

    echo '-----> Project directory'
    pwd
    ls -al

    echo '-----> Creating ssh key'
    echo "$SSH_PRIVATE_KEY" | base64 --decode -i > ~/.ssh/id_rsa
    chmod 600 ~/.ssh/id_rsa # permissioning
    eval "$(ssh-agent -s)" # setting ssh environment variable

    echo '-----> Adding keys to ssh-agent'
    ssh-add ~/.ssh/id_rsa

    echo '-----> Creating ssh config'
    echo "$SSH_CONFIG" | tr ',' '\n' > ~/.ssh/config

    echo '-----> Adding git remote'
    git config remote.plotly.url >&- || git remote add plotly dokku@<your-dash-enterprise-hostname>:<your-dash-app-name> # add remote if remote doesn't exist

    echo '-----> Deploying app'
    git push plotly HEAD:master
    ```

    You'll need to make a few changes to this script:

    - Replace `<your-dash-enterprise-hostname>` with the host name of your Dash Enterprise platform
    - Replace `<your-dash-app-name>` with the name of your Dash app as initialized on Dash Enterprise
    - The path of `~/.ssh` may be different on your CI system. Consult your CI system's docs on SSH.

    See [Review Apps](https://github.com/plotly/dash-enterprise-review-apps) repository for script exampls and [Dash Enterprise Review Apps](/dash-enterprise/review-apps) docs for more detailed instructions.

4. Trigger this CI script when code is merged into `master`.

