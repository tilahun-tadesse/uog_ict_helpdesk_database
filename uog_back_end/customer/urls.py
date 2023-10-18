from posixpath import relpath
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('customer-list/', customer_list.as_view()),
    path('customer-delete/<str:phonenumber>', customer_update.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
