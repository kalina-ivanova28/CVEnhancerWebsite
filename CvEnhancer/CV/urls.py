from django.urls import path

from . import views

app_name='CV'

urlpatterns = [
    path("", views.index, name="index"),
    path('form/', views.form_page, name='form_page'),
    path('aboutus/', views.about_us_page, name='about_us_page'),
    path('rate_page/', views.rate_page, name='rate_page'),
    path('rate_site/', views.rate_site, name='rate_site')
]