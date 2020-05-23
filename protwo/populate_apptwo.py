import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'protwo.settings')

import django
django.setup()

from apptwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        name = fakegen.name().split()
        f_name = name[0]
        l_name = name[1]
        email = fakegen.email()

        user = User.objects.get_or_create(first=f_name, last=l_name, emailid=email)[0]

if __name__ == '__main__':
    print('populating')
    populate(20)
    print('completed')
