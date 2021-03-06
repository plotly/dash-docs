
## Requirements

To get started you will need:

* A Dash Enterprise Server instance
* A repository containing your Dash app's source code
  (GitHub, GitLab, Bitbucket...)
* A CI platform (GitHub Actions, GitLab CI/CD, Bitbucket Pipes & 
  Deployment, CircleCI...)
* A CI pipeline for your app's repository

## Setting Up

To set up review apps, complete the following steps:

>Depending on your CI platform, you may need to modify certains steps.
>See [Dash Enterprise Review Apps](/dash-enterprise/continuous-integration) for more detailed instructions.

1. Designate a *service account* with admin privileges on Dash Enterprise.
2. Create an SSH key and add the public key to Dash Enterprise.
   See [Authenticating to Dash Enterprise with SSH](/dash-enterprise/ssh) for
   more detailed instructions.
3. Encode the private key in base64. See [Dash Enterprise Continuous Integration](/dash-enterprise/continuous-integration) for more detailed instructions.
4. Generate an API key for the *service account* and all developer accounts that will push changes to the app repository.
5. Add the encoded private SSH key, and Dash Enterprise service and developer API keys as environment variables on your CI platform.
6. Copy the `review-apps` directory to your main app project folder. 
7. In your `review-apps` directory, update the following variables in the `settings.py` file:
   1. Update `DASH_ENTERPRISE_HOST` with your Dash Enterprise host address.
   2. Update `MAIN_BRANCHNAME` with the name of the branch from where you will be pushing changes to your *main app*.
   3. Update `REVIEW_BRANCHNAME` with the name of the branch from where you will be pushing changes to your *review app*.
   4. Update `MAIN_APP` with the name of the app you want to base your review apps on.
   5. Update `SERVICE_API_KEY` with the environment variable containing your service account API key.
   6. Update `SERVICE_PRIVATE_SSH_KEY` with the environment variable containing your service account private SSH key.
   7. Update `DE_USERNAME_TO_CI_API_KEY` with the Dash Enterprise usernames and the corresponding API keys of the developers you want to deploy review apps.
   8. Update `DE_USERNAME_TO_CI_USERNAME` with the Dash Enterprise usernames and the corresponding CI platform usernames.
   9. Update `CI_USERNAME` with the CI platform login of the user pushing code to your version control system.
   10. Optional: Update `PERIOD` with the time unit and `TIME` with the amount of time a review app can remain deployed since its last update.
8. Optional: In the `review-apps` directory, update scheduled `delete` job's cron settings in the `config.yml` file 


## Basic Usage

After setting up, review apps will get automatically created anytime you make a pull request from your review app branch. When pull request are merged, those approved changes get deployed to your main app branch.

1. In your app's repository, create and checkout the branch assigned to `REVIEW_BRANCHNAME`.
2. Make changes to your apps source code on your review app branch.
3. Commit and push those changes.

## Local Usage

To run the review app scripts locally you will need to: 

1. Create an `.env` file.
2. Add and export the following environment varibles and corresponding values:
   1. `DEVELOPER_API_KEY`
   2. `SERVICE_API_KEY`
   3. `SERVICE_PRIVATE_SSH_KEY`

   ```bash
   export CHRIDDYP_API_KEY="7WvY4f4e3chyEd272492"
   export SERVICE_API_KEY="K4gvY4uO2yEaxSZrEHar"
   export SERVICE_SSH_KEY="T2djU3YvSEVkbVZFT [...] 3BEdjBuNFhCUjYrT1pLRXUvUV"
   ```

3. Create a virtual environment, activate it and install script dependencies:

   ```bash
   cd criddyp-report-review-app
   virtualenv -p /usr/bin/python3.6 venv
   source ./venv/bin/activate
   ./venv/bin/python3.6 -m pip install ci-requirements.txt
   ```

4. Load environment variables from the `.env` file and run the script:

   ```bash
   source .env && python3.6 initialize.py
   ```

## CircleCI

To automate review app deployment with CircleCI, in addition to the setup steps you will need to:

1. Add your app repository as a **Project**. See CircleCI docs on [GitHub and Bitbucket Integration](https://circleci.com/docs/2.0/gh-bb-integration/?section=projects) for more detailed instructions.
2. Add environment variable secrets to your **Project Settings** page. See CircleCI docs on [Setting Environment Variables in a Project](https://circleci.com/docs/2.0/env-vars/#setting-an-environment-variable-in-a-project) for more detailed instructions.
   1. Navigate to your CircleCI **Project Settings** page.
   2. Click on **Add Environment Variable**.
   3. In the modal that appears, fill out the **Name** field with your environment variable's name and the **Value** field, with its value.
   4. Click on **Add Environment Variable** to confirm.
3. Rename `review-app` directory to `.circleci`.

>To use CircleCI you need to be using either GitHub or Bitbucket for your version control system (VCS).
>
>Your app repository is automatically configured when you provide CircleCI with
>a VCS API key and push changes to it. See [CircleCI Github Integration Overview](https://circleci.com/docs/2.0/gh-bb-integration/#add-a-circleciconfigyml-file) for more details.
