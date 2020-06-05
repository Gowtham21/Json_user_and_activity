'''
Here we are creating dummy datas for only USER model, using Faker library,
we cannot able to create Activity model because, every user has multiple starttime and endtime, So as per my knowledge I tune this code in my maximum level

Note:
    we need to run this file seperately,
    RUN this first
    Please migrate Django Apps and Models to follow this steps

    1 : py manage.py makemigrations

    2 : py manage.py migrate

    3 : py manage.py makemigrations

    then
    "Python dummy_data.py"

    After
    Once the dummy data created successfully, Now we have Fake Users
    lets run  "python manage.py createsuperuser"
    create your own superuser following by command propmt,
    then "python manage.py runserver"
    Please visit admin page like "http://127.0.0.1:8000/admin"
    add for every user manually starttime and endtime multiple times
    finally:
    you can see expected output in "http://127.0.0.1:8000/"

'''
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','useractivity.settings')

import django
# Import settings
django.setup()

import random
from userapp.models import user
from faker import Faker
#instance for the Faker object
fakegen = Faker()

def dummy(N):
    for entry in range(N):
        # Create Fake Data for entry
        fake_id = fakegen.bothify(text='??#?##?##')
        fake_name = fakegen.name()
        fake_tz = fakegen.timezone()

        # Create new user Entry
        usr = user.objects.get_or_create(id=fake_id,real_name=fake_name,tz=fake_tz)[0]

if __name__ == '__main__':
    print("Creating dummy data...Please Wait")
    dummy(5)
    print('dummy data successfully added')
