from posixpath import relpath
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('message-list/', message_list.as_view()),
    path('message-list1/', message_list1.as_view()),
    path('message-list2/', message_list2.as_view()),
    path('message-update/', MessageUpdate.as_view()), 
    path('message-delete/<str:pk>', message_delete.as_view(),),
    # path('expert/update-partial/(?P<pk>\d+)/$', expert_update.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
