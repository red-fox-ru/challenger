from django.urls import path
from v1.views import auth


urlpatterns = [
    path('login/', auth.GetTokenView.as_view(), name='token_obtain_pair'),
    path('reg/', auth.register_user, name="registration"),
    path('', auth.get_users, name="users"),
    path('profile/', auth.user_profile, name="profile"),
]
