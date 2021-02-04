from django.urls import path

from authentication.views import RegisterView, ProfileView, UserList, LoginView

# LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('editprofile/', ProfileView.as_view()),
     path('members/', UserList.as_view()),
     path('login/', LoginView.as_view()),

]
