import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':

    print('Количество пропусков:', Passcard.objects.count())
