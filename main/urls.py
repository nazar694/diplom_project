from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('registration/', views.registration_page, name='registration'),
    path('reserved/', views.reserved_page, name='reserved'),
    path('reserved_save/', views.reserved_save_page, name='reserved_save'),
    path('enter/', views.enter_page, name='enter'),
    path('exit/', views.exit_page, name='exit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
