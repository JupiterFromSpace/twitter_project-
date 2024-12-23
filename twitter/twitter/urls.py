
from django.contrib import admin
from django.urls import path
from post.views import UserProfileView,ListUserProfileView,CreateUserProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/create/',CreateUserProfileView.as_view(), name='user-profile-list-create'),
    path('user/list/',ListUserProfileView.as_view(), name='user-profile-list'),
    path('user/',UserProfileView.as_view(),name='user-profile'),
    path('user/<id>/',UserProfileView.as_view(),name='update-user-profile'),
]

