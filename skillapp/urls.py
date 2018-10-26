from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'signup/', views.signup, name='signup'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^edit_profile/', views.edit_profile, name = 'edit_profile'),
    url(r'section/(\d+)',views.section, name = 'section'),
    url(r'^new_post/', views.new_post, name = 'new_post'),
    
    url(r'post/(\d+)',views.post, name = 'post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)