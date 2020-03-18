# trydjango

[Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4)
# Entry

We have to set up virtualenv because manage third party packages easily.to start virtualenv we can just type,

``` bash
$ virtualenv . # '.' points all files inside of folder
```

To start virtualenv enter that main folder not root folder just folder that keeps all project files inside and type,
``` bash
$ source bin/activate
```

# Create Project

``` bash
django-admin startproject [projectName] #type this inside of src file which we created before and is located main folder.
``` 

# Start Server

``` bash
python manage.py runserver # type that inside of root folder.()
```

# Models

``` bash
$ python manage.py startapp [modelName] #this line creates new model
```

# Migrations

``` bash
$ python manage.py makemigrate #to migrate our models
```

``` bash
$ python manage.py migrate #apply all migrations
``` 

# Admin Panel

``` bash
$ python manage.py createsuperuser
```

# What we learnt except django

``` bash
$ pip freeze #Output installed packages in requirements format.
```

## Addition

***main folder*** stands for folder that keep whole project files.

***root folder'*** stands for folder that keeps that only project files and also not keeps ***manage.py****.Mostly, ***'/src'*** folder. 
