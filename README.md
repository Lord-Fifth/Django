# Django
A Tech-Event Site using Django.


Django Workshop
System Password

cirtic
cirtic123
cirtic@123

To download templates click here..
Linux System Configuration

sudo su
apt-get install python python-dev libpq-dev python-setuptools 
apt-get install postgresql postgresql-contrib phppgadmin
easy_install pip 
pip install virtualenv virtualenvwrapper

Windows System Configuration

Install Python https://python.org/downloads/ -2.7 

https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi

Manually register to This PC → properties →  advanced settings→ environment settings→ path 
→ Edit → new add(C:\Python27) and add(C:\Python27\Scripts)

To install pip, securely download get-pip.py.

https://bootstrap.pypa.io/get-pip.py

python get-pip.py

Django Configuration

Open your terminal and type,

cd Documents/django

mkdir project

cd project

mkdir event_app

cd event_app

virtualenv venv

source venv/bin/activate

pip install django===1.11.15

mkdir src

cd src

django-admin.py startproject event_app

cd event_app

current_directory_structure

	events_app
		__init__.py
		settings.py
		urls.py
		wsgi.py
	manage.py

python manage.py runserver

Go to browser and type

localhost:8000 and hit enter to see the result.

Create a New Application

python manage.py startapp events

Current directory structure

current_directory_structure
	events
		migrations
			__init__.py
		__init__.py
		admin.py
		apps.py
		models.py
		tests.py
		urls.py
		views.py
	events_app
		__init__.py
		settings.py
		urls.py
		wsgi.py
	manage.py

event_app/urls.py

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('events.urls'))
]

events/urls.py

from django.conf.urls import url
from django.contrib import admin
import views


urlpatterns = [
    url(r'^$',views.index)
]

events/views.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return HttpResponse("Hello World")

To Load HTML templates to django application we need to create a templates folder in our project directory and update in settings.
Configuration Template

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

To load our templates we modify events/views.py in to

def index(request):
    return render(request,'index.html')

To Load Images , CSS and Javascript in to HTML page we need to create a static folder in our project directory and put css, images, script folders inside that and update settings something like,
Configuration Static

STATIC_URL = '/static/'
STATIC_FILE_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

templates/index.html

<!DOCTYPE html>
<html>
	<head>
		{% load static %}
		<title>Events App</title>
		<link rel="stylesheet" href="{% static 'css/style.css' %}">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>
	<body>
		<header>
			<section class="wrapper">
				<h1><a href=""><img src="{% static 'images/logo.png' %}" alt="Logo"></a></h1>
				<nav class="right">
					<div class="search">
						<form action="">
							<input name="query" class="search" placeholder="Search here.." type="text">
							<input type="submit" value="Submit">
						</form>
					</div>
				</nav>
				<br class="clear">
			</section>
		</header>

		<main>
			<section id="spotlight">
				<section class="wrapper">
					<h1>“Somewhere, something incredible is waiting to be known.”</h1>
					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat officia alias, nobis, magni facilis amet ducimus quos! Molestias animi</p>
				</section>
			</section>

			<section id="content">
				<section class="wrapper">
					<ul class="list">
						<li>
							<div class="card">
								<div class="bottom">
									<h1 class="title">Event 1</h1>
									<p>12/09/2018</p>
									<p>Place</p>
								</div>
							</div>
						</li>

						<li>
							<div class="card">
								<div class="bottom">
									<h1 class="title">Event 2</h1>
									<p>12/09/2018</p>
									<p>Place</p>
								</div>
							</div>
						</li>

						<li>
							<div class="card">
								<div class="bottom">
									<h1 class="title">Event 3</h1>
									<p>12/09/2018</p>
									<p>Place</p>
								</div>
							</div>
						</li>

						<li>
							<div class="card">
								<div class="bottom">
									<h1 class="title">Event 4</h1>
									<p>12/09/2018</p>
									<p>Place</p>
								</div>
							</div>
						</li>

						<li>
							<div class="card">
								<div class="bottom">
									<h1 class="title">Event 5</h1>
									<p>12/09/2018</p>
									<p>Place</p>
								</div>
							</div>
						</li>
					</ul>
					<br class="clear">
				</section>
			</section>
		</main>
	</body>
</html>

Configuration Apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'events'
]

events/models.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Event(models.Model):
	name = models.CharField(max_length=128)
	date = models.DateTimeField()
	place = models.CharField(max_length=128)

	class Meta:
		db_table = "events_event"

	def __unicode__(self):
		return self.name

python manage.py makemigrations
python manage.py migrate
events/admin.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('id','name','date','place')
admin.site.register(Event,EventAdmin)

events/views.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from events.models import Event


def index(request):
    events = Event.objects.all()
    context = {
        "title" : "Events App",
        "events" : events
    }
    return render(request,'index.html',context)

templates/index.html

<!DOCTYPE html>
<html>
	<head>
		{% load static %}
		<title>Events App</title>
		<link rel="stylesheet" href="{% static 'css/style.css' %}">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>
	<body>
		<header>
			<section class="wrapper">
				<h1><a href=""><img src="{% static 'images/logo.png' %}" alt="Logo"></a></h1>
				<nav class="right">
					<div class="search">
						<form action="">
							<input name="query" class="search" placeholder="Search here.." type="text">
							<input type="submit" value="Submit">
						</form>
					</div>
				</nav>
				<br class="clear">
			</section>
		</header>

		<main>
			<section id="spotlight">
				<section class="wrapper">
					<h1>“Somewhere, something incredible is waiting to be known.”</h1>
					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quaerat officia alias, nobis, magni facilis amet ducimus quos! Molestias animi</p>
				</section>
			</section>

			<section id="content">
				<section class="wrapper">
					<ul class="list">
						{% for event in events %}
							<li>
								<div class="card">
									<div class="bottom">
										<h1 class="title">{{event.name}}</h1>
										<p>{{event.date}}</p>
										<p>{{event.place}}</p>
									</div>
								</div>
							</li>
						{% endfor %}
					</ul>
					<br class="clear">
				</section>
			</section>
		</main>
	</body>
</html>

