https://docs.djangoproject.com/en/1.11/intro/tutorial01/
pip install Django

#app and server starts
python manage.py runserver
python manage.py startapp polls
python tessertest.py

#data migration
python manage.py makemigrations polls #create migrations for those changes
python manage.py migrate
python manage.py sqlmigrate polls 0001

#developer environment
python3.6 -m venv my_env
source my_env/bin/activate

#Django Shell
python manage.py shell

#packages
brew install tesseract
pip install Cython
pip install tesserocr
sudo pip install tesseract
pip install Pillow