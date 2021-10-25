# RecipeAPI

This is an API for a Recipes service using Flask. Users can register an account and login to create, edit, view and delete recipe categories and recipes in those categories.

Add link to Heroku here

| EndPoint                                          | Functionality                                    |
| ------------------------------------------------- | ------------------------------------------------ |
| [ POST /auth/login/ ](#)                          | Logs a user in                                   |
| [ POST /auth/register/ ](#)                       | Register a user                                  |
| [ DELETE /auth/logout/ ](#)                       | Logout a user                                    |
| [ POST /categories/ ](#)                          | Create a new category                            |
| [ GET /categories/ ](#)                           | Get all categories created by the logged in user |
| [ GET /categories/\<category_id>/ ](#)            | Get a category by it's id                        |
| [ PUT /categories/\<category_id>/ ](#)            | Update the category                              |
| [ DELETE /categories/\<category_id>/ ](#)         | Delete the category                              |
| [ POST /recipes/\<category_id>/ ](#)              | Create a recipe in the specified category        |
| [ GET /recipes/](#)                               | Get all recipes created by the logged in user    |
| [ GET /recipes/\<category_id>/](#)                | Get all recipes in the specified category id     |
| [ GET /recipes/\<category_id>/\<recipe_id>](#)    | Get a recipe in the specified category id        |
| [ PUT /recipes/\<category_id>/<recipe_id> ](#)    | Update the recipe in the specified category id   |
| [ DELETE /recipes/\<category_id>/<recipe_id> ](#) | Delete the recipe in the specified category id   |

## Technology Stack

- Python 3.6
- Flask
- Postgres 9.6
- Docker 
- Docker-compose
- AWS
- Github, Github Actions
- Terraform
- Kubernetes

## Getting Started

To use the application, ensure that you have python 3.6+, docker, terraform and kubernetes installed, clone the repository to your local machine. The app can be run in the following ways:

## Method 1 - Development

1. Clone the repository
   ```bash
    git clone https://github.com/avosa/recipes.git
   ```

2. Enter the project directory
   ```bash
   cd recipes
   ```
3. Create a virtual environment
   ```bash
   virtualenv venv
   ```
4. Activate the virtual environment
   ```bash
   source venv/bin/activate
   ```
5. Then install all the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
6. Install postgres if you don't already have it. Preferably Postgres 10.1.

7. Create the Databases

   #### For the test Database
   ```bash
   createdb recipes_test_db
   ```

   #### For the development Database
   ```bash
   createdb recipes_dev_db
   ```
8.  Run Migrations using these commands, in that order:
      ```bash
      python3 manage.py db init
      python3 manage.py db migrate
      python3 manage.py db upgrade
      ```

11. To test the application, run the command:
      ```bash
      pytest --cov-report term --cov=app
      ```

12. To start the server, run the command:
      ```bash
      export FLASK_APP=manage.py

      export FLASK_DEBUG=1

      flask run
      ```
## Method 2 - Development
This method helps us acertain that the app dockerized is running well.
We are going to make use of Docker and docker compose
1. Enter the project directory
   ```bash
   cd recipes
   ```
2. Run the command below:
```bash
docker-compose up
```
The app will be listening on port 5000 i.e. [localhost:5000](http://127.0.0.1:5000/)

# Deploying the app for production
## Prerequisite 
- AWS Account - If you dont have one you can create one a Free Tier at their official [website](https://aws.amazon.com/free/)
- Terraform - For provisioning infrastructure in AWS
- Github Account for storing repo

Assuming you have the above installed/set up:
1. Step 1 - Provisioning using Terraform
Create docker repository on AWS using terraform
```bash
cd recipes/terraform
```
Set values in providers.tf then run:
```bash
terraform init

terraform apply -auto-approve
```

2. Create an empty repo on github
3. Set secrets
- Navigate to Settings > Secrets > New Repository Secret > then create the following secrets inputing appropriate values:
```bash
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
KUBE_CONFIG_DATA
```
More informnation on setting encrypted secrets on github can be found on [Github's official documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

* To get `KUBE_CONFIG_DATA` secrets you need Kubernetes and kubectl installed.
* To generate `KUBE_CONFIG_DATA` values open your preferred command line tool and run: 
```bash
 cat $HOME/.kube/config | base64
 ```
For more information regarding KUBE_CONFIG_DATA you can read their [official documentation](https://github.com/marketplace/actions/kubectl-for-eks#secrets).

4. Enter the repo if you haven't already 
```bash 
cd recipes

sudo rm -r .git 
```
5. Push the repo
Once you have pushed your repo you can track the progress of the deployment by clicking `Actions` button just below your github repo.




