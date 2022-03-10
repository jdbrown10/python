#FLASK is a framework -- it adds structure to the way your code will run. To deploy a website, you usually have to deploy it through a framework so that it runs properly.

#Virtual Environment -- wherein you install something specific to a project and then you can turn it on and off

#For every project moving forward, you're going to need to go into that project folder in you terminal, and use "pipenv install flask" to install flask into that project
#you may need to add "python3 -m" at the beginning-- (in case you don't have 100% security permissions)

#THEN you need to run "pipenv shell" to activate the flask environment. (if you're using powershell or gitbash, it won't let you know that the environment is active. if you run it and don't get an error, then it's active.)

#go into the files that were created and you'll see the pipfile (the structure that was created) and a pipfile.lock

#if you close it and open it again, all you have to do is re-enter the virvual environment (using "pipenv shell"), you don't have to re-install anything

#DO NOT create a virtual environment inside of another one