from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('open-house/', views.openhouse, name='open-house'),
    path('create-open-house/', views.createopenhouse, name='create-open-house'),
    path('event/<int:pk>/', views.eventdetail, name='event-detail'),
    path('like/<int:post_id>/', views.likepost, name='like-post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

