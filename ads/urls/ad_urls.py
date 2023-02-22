from django.urls import path

from ads.views import ad_views

urlpatterns = [
    path('', ad_views.AdvertisementsListView.as_view()),
    path('<int:pk>/', ad_views.AdvertisementsDetailView.as_view()),
    path('create/', ad_views.AdvertisementsCreateView.as_view()),
    path('update/<int:pk>/', ad_views.AdvertisementsUpdateView.as_view()),
    path('delete/<int:pk>/', ad_views.AdvertisementsDeleteView.as_view()),
    path('<int:pk>/uploade_image/', ad_views.AdvertisementsUplodateView.as_view())
]
