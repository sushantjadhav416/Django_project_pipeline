## Django_project_pipeline

### Django based E-commerce web application with CI-CD Jenkins pipline. and Github Actions.

### Screenshot
![Alt text](Project1_e-shop.png)

### SetUp:

- Setup To get this repository, run the following command inside your git enabled terminal

```
$ git clone https://github.com/sushantjadhav416/django-project-pipline
```

After that go to the firstproject $cd firstproject You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

```
  $ python manage.py makemigrations

   ```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command

 ```
  $ python manage.py migrate
  
   ```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

- $ python manage.py createsuperuser 

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```
 $ python manage.py runserver Once the server is hosted, head over to http://127.0.0.1:8000/E_shop for the App.
```

Cheers and Happy Coding :)

##  Web Application Overview
This is a simple Django based web application that can be containerize using Docker. Django dependencies are handled using the setup.py at the root directory of the repository.

This is a MVT architecture based application where View returns a page with title and message attributes to the view.

- Execute the application locally and access it using your browser
Checkout the repo and move to the directory

-  ```
   git clone https://github.com/sushantjadhav416/Django_project_pipline/firstproject
 ```
 
- ```
cd Django_project_pipline/firstproject
```

- Execute the Docker build command to build docker image.


   
### Dockerization
 1. To Build the Docker Image we have to code a Dockerfile according to our project need.
    for this project , i have coded dockerFile as below,
```
   FROM python:3.10-slim

   ENV PYTHONUNBUFFERED 1

   WORKDIR /app

   COPY . /app

   RUN pip install -r requirements.txt 

   CMD [ "python3","manage.py","runserver","0.0.0.0:8000]

```
3. __
   ```
      docker build -t <Name Of Image>:v1 .
   ```

5. __
  ``` 
  docker run -d -p 5000:5000 -t ultimate-cicd-pipeline:v1 
  ```

6. Access the application on http://ip-address:5000.



# Github actions Workflow structure
1. CodeQL / Analyze - Code vulnerability scan
2. Django CI-test - Unit test
3. Docker Image CI / build - Docker Image build and push
4. trivy / Build - Trivy docker image vunerability scan



