from django.contrib.auth import get_user_model
from sesame.utils import get_query_string
User = get_user_model()
users = User.objects.all()
for user in users:
    print(user, get_query_string(user))
