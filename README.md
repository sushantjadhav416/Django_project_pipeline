# Django_project_pipeline

#django base E-commerce web application CI-CD deployment pipline A E-commerce web application built with django

E-commerce app

Setup To get this repository, run the following command inside your git enabled terminal

$ git clone https://github.com/sushantjadhav416/django-project-pipline After that go to the firstproject $cd firstproject You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Once you have downloaded django, go to the cloned repo directory and run the following command

$ python manage.py makemigrations This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command

$ python manage.py migrate One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

$ python manage.py createsuperuser That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

$ python manage.py runserver Once the server is hosted, head over to http://127.0.0.1:8000/todos for the App.

Cheers and Happy Coding :)

##  Django based python web application
This is a simple Django based python web application that can be containerize using Docker. Django dependencies are handled using the setup.py at the root directory of the repository.

This is a MVT architecture based application where View returns a page with title and message attributes to the view.

Execute the application locally and access it using your browser
Checkout the repo and move to the directory

git clone https://github.com/sushantjadhav416/Django_project_pipline/firstproject
cd Django_project_pipline/firstproject
Execute the Docker build command to build docker image.
The Docker way
Build the Docker Image

docker build -t ultimate-cicd-pipeline:v1 .
docker run -d -p 5000:5000 -t ultimate-cicd-pipeline:v1
Access the application on http://<ip-address>:8010

Next Steps
Configure a Sonar Server locally
apt install unzip
adduser sonarqube
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.4.0.54424.zip
unzip *
chmod -R 755 /home/sonarqube/sonarqube-9.4.0.54424
chown -R sonarqube:sonarqube /home/sonarqube/sonarqube-9.4.0.54424
cd sonarqube-9.4.0.54424/bin/linux-x86-64/
./sonar.sh start
access the SonarQube Server on http://<ip-address>:9000
