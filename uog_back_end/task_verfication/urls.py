from posixpath import relpath
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('task_verfication-list/', task_varfication_list.as_view()),
    path('task_verfication-list1/', task_varfication_list1.as_view()),
    # path('task_verfication-list2/', task_varfication_list_or.as_view()),
    path('task_verfication-delete/<str:pk>',
         task_varfication_update.as_view()),
    path('task_verfication-update/<str:task_id>', task_verfication_update_one.as_view()),
    # path('expert/update-partial/(?P<pk>\d+)/$', expert_update.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
