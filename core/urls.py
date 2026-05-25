from django.urls import path
from .views import gallery, home, newsletter_subscribe
from .views import contact_view

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('newsletter-subscribe/', newsletter_subscribe, name='newsletter_subscribe'),
]