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