import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


from datacenter.models import Passcard


if __name__ == '__main__':

      passcard = Passcard.objects.get(owner_name = "Jennifer Martin")

print(f"""
owner_name: {passcard.owner_name}
passcode: {passcard.passcode}
created_at: {passcard.created_at}
is_active: {passcard.is_active}
""")
