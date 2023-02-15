from django.urls import path

from ads.views import cat_views

urlpatterns = [
    path('', cat_views.CategoryListView.as_view()),
    path('<int:pk>/', cat_views.CategoryDetailView.as_view()),
    path('create/', cat_views.CategoryCreateView.as_view()),
    path('update/<int:pk>/', cat_views.CategoryUpdateView.as_view()),
    path('delete/<int:pk>/', cat_views.CategoryDeleteView.as_view()),
]
