## Requirements

To get started you will need:

* Dash Enterprise Server instance
* Repository containing your Dash app's source code
    (GitHub, GitLab, Bitbucket...)
* CI platform (GitHub Actions, GitLab CI/CD, Bitbucket Pipes & 
    Deployment, CircleCI...)
* CI pipeline for your app's repository
* CI platform configuration file
* Review app scripts

>You can download the scripts from the [Dash Enterprise Review App Repo](https://github.com/plotly/dash-enterprise-review-apps)

Once configured, the Review App scripts that run on your CI system will:

1. Create a new Review App on Dash Enterprise when a new branch is created on CI. The name of this app will be based off of the branch name and the main app's name.
2. Update that Review App when commits are made to that branch.
3. Delete Review Apps daily that haven't been updated or visited after a certain amount of time (e.g. 5 days).
4. Deploy changes to the main app when commits are made to the main branch, e.g. after a pull request is merged.

## Setting Up

To set up review apps, complete the following steps:

>Depending on your CI platform, you may need to modify certain steps.

1. Designate a *service account* with admin privileges on Dash Enterprise. See *step 1* in [Dash Enterprise Continuous Integration](/dash-enterprise/continuous-integration) for more detailed instructions.
2. Generate an SSH key *without a passphrase*, and add the public key to
    Dash Enterprise. See [Authenticating to Dash Enterprise with SSH](/dash-enterprise/ssh) for
    more detailed instructions.
3. Encode the private key in base64. See *step 3.1* in [Dash Enterprise Continuous Integration](/dash-enterprise/continuous-integration) for more detailed instructions.
4. Encode your SSH configuration file in base64. See *step 3.2* in [Dash Enterprise Continuous Integration](/dash-enterprise/continuous-integration)
5. Generate an API key for the *service account* and all developer accounts that will push changes to the app repository.
6. Add the base64-encoded private SSH key, and Dash Enterprise service and developer API keys as environment variables on your CI platform.
7. Add your CI platform configuration file to the root of your project folder. For example, in CircleCI this file would be `.circleci/config.yml`.
8. Copy the `.review-apps` folder from [Plotly's GitHub](https://github.com/plotly/dash-enterprise-review-apps) to the root your project folder.
9. In your `.review-apps` folder, update the following variables in the `settings.py` file. See more details in the comments in `settings.py`:
    1. Update `DASH_ENTERPRISE_HOST` with your Dash Enterprise host address.
    2. Update `MAIN_BRANCHNAME` with the name of the branch from where you will be pushing changes to your *main app*.
    3. Update `REVIEW_BRANCHNAME` with the branch name as provided by a CI environment variable.
    4. Update `MAIN_APP` with the name of the app you want to base your review apps on.
    5. Update `SERVICE_API_KEY` with the environment variable containing your service account API key.
    6. Update `SERVICE_PRIVATE_SSH_KEY` with the environment variable containing your service account private SSH key.
    7. Update `DE_USERNAME_TO_CI_API_KEY` with the Dash Enterprise usernames and the corresponding API keys of the developers you want to deploy review apps.
    8. Update `DE_USERNAME_TO_CI_USERNAME` with the Dash Enterprise usernames and the corresponding CI platform usernames.
    9. Update `CI_USERNAME` with the CI platform login of the user pushing code to your version control system.
    10. Optional: Update `TIME_UNIT` with the time unit (e.g. "days") and `TIMESPAN` with the amount of time a review app can remain deployed since its last update.
10. Optional: Set up your CI configuration to run the Review App scripts. See [`.circleci/config.yml`](https://github.com/plotly/dash-enterprise-review-apps/tree/main/.circleci) for an example using CircleCI's configuration.
    1. Run python delete.py on a schedule once a day. This script will delete stale review apps.
    2. Run python deploy.py when commits are made on your main branch to deploy the latest changes to your main app.
    3. Run `python initialize.py` and `python deploy.py` when commits are made on other branches to initialize Review App on Dash Enterprise and deploy the changes from the branch to that app.
11. Once configured, the Review App scripts that run on your CI system will:
    1. Create a new Review App on Dash Enterprise when a new branch is created on CI. The name of this app will be based off of the branch name and the main app's name.
    2. Update that Review App when commits are made to that branch.
    3. Delete Review Apps daily that haven't been updated or visited after a certain amount of time (e.g. 5 days).
    4. Deploy changes to the main app when commits are made to the main branch (e.g. after a pull request is merged).


## Basic Usage

After setting up, review apps will get automatically created anytime you make a pull request from your review app branch. When pull request are merged, those approved changes get deployed to your main app branch.

1. In your app's repository, create and checkout a new branch.
2. Make changes to your apps source code on your review app branch.
3. Commit and push those changes.

## Local Usage

To run the Review App scripts locally you will need to:

1. Create an `.env` file.

2. Add and export the following environment variables and corresponding values:

    1. `YOUR_DEVELOPER_USERNAME_API_KEY`
    2. `SERVICE_API_KEY`
    3. `SERVICE_PRIVATE_SSH_KEY`
    4. `SERVICE_SSH_CONFIG`

    ```bash
    export YOUR_DEVELOPER_USERNAME_API_KEY="7WvY4f4e3chyEd272492"
    export SERVICE_API_KEY="K4gvY4uO2yEaxSZrEHar"
    export SERVICE_SSH_KEY="T2djU3YvSEVkbVZFT [...] 3BEdjBuNFhCUjYrT1pLRXUvUV"
    export SERVICE_SSH_CONFIG="SG9c2gvzdCAqCiAgIC [...] DMwMjIKICAgIElkZW50aXR5R"
    ```

3. Create a virtual environment, activate it and install script dependencies:

For example:

   ```bash
   cd review-apps/
   virtualenv -p /usr/bin/python3.6 venv
   source ./venv/bin/activate
   ./venv/bin/python3.6 -m pip install ci-requirements.txt
   ```

4. Load environment variables from the `.env` file and run the scripts together or individually:

    ```bash
    source .env
    python3.6 initialize.py; python3.6 deploy.py; python3.6 delete.py
    
    ```

## CircleCI Example

To automate review app deployment with CircleCI, in addition to the setup steps you will need to:

1. Add your app repository as a **Project**. See CircleCI docs on [GitHub and Bitbucket Integration](https://circleci.com/docs/2.0/gh-bb-integration/?section=projects) for more detailed instructions.
2. Add environment variable secrets to your **Project Settings** page. See CircleCI docs on [Setting Environment Variables in a Project](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project) for more detailed instructions.
    1. Navigate to your CircleCI **Project Settings** page.
    2. Click on **Add Environment Variable**.
    3. In the modal that appears, fill out the **Name** field with your environment variable's name and the **Value** field, with its value.
    4. Click on **Add Environment Variable** to confirm.
3. Add to your projects repository root:
   1. A `review-apps` folder containing Review App scripts.
   2. A `.circleci` folder containing your CircleCI configuration file.
   
>To use CircleCI you need to be using either GitHub or Bitbucket for your version control system (VCS).
>
>Your app repository is automatically configured when you provide CircleCI with
>a VCS API key and push changes to it. See [CircleCI Github Integration Overview](https://circleci.com/docs/2.0/gh-bb-integration/#add-a-circleciconfigyml-file) for more details.