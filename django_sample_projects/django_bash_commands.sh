# Install dj4e samples
# ================================

pip install django

#workon django

python -m django --version

# repository with sample django codes
git clone https://github.com/csev/dj4e-samples.git

cd dj4e-samples
pip3 install -r requirements.txt # dependencies

# reads through your files and these files that point to other files, looks for syntax errors. And it's a good way
# to check the sanity of your application. Because if it won't pass this manage.py check, it's not going to start.
python manage.py check

python manage.py makemigrations

# this will create a bunch of database tables
python manage.py migrate


# Mysite
cd mysite
django-admin startproject mysite
python manage.py check


