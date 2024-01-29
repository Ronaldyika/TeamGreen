from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.homepage,name='index'),
    path('register/',views.register,name='register'),
    path('update/',views.get_updates,name='updates'),
    path('index/',views.indexpage,name='main'),
    path('unions/',views.credit_union,name='union'),
    path('profileinfo/',views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name = 'Authentication/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'Authentication/logout.html'),name='logout'),
]


urlpatterns += staticfiles_urlpatterns()



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 