from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from .models import Customer

def customer_profile(sender,instance,created,**kwargs):
    if created:
        groups = Group.object.get(name = "customer")
        instance.user.groups.add(groups)
        Customer.objects.create(
            user = instance,
            name = instance.username,
        )
        print("customer created")

post_save.connect(customer_profile,sender=User)