from django.contrib.auth.models import Group, User
g = Group.objects.get(name='japplications')
users = User.objects.all()[1:]
for u in users:
    g.user_set.add(u)
