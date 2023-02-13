from django.urls import path

from ads import user_views

urlpatterns = [
    path('', user_views.UserListView.as_view()),
    path('<int:pk>/', user_views.UserDetailView.as_view()),
    path('create/', user_views.UserCreateView.as_view()),
    path('update/<int:pk>/', user_views.UserUpdateView.as_view()),
    path('delete/<int:pk>/', user_views.UserDeleteView.as_view()),
]
