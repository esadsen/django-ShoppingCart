from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name="items"

urlpatterns = [
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
