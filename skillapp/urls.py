from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'signup/', views.signup, name='signup'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^edit_profile/', views.edit_profile, name = 'edit_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)