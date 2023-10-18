from posixpath import relpath
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('customer_ask_help-list/', customer_ask_help_list.as_view()),
    path('customer_ask_help-delete/<str:pk>',
         customer_ask_help_update.as_view()),
    # path('expert/update-partial/(?P<pk>\d+)/$', expert_update.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
