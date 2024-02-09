# create_superuser_script.py

import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospital_management.settings")
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()

    superuser = User.objects.create_superuser(email='admin@gmail.com', username='admin', password='password', is_active=True, is_staff=True)

    print("Superuser created successfully!")

if __name__ == "__main__":
    create_superuser()
