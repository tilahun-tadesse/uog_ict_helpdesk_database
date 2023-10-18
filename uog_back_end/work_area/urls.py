from posixpath import relpath
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('work_area-list/', user_list.as_view()),
    path('work_area-delete/<str:pk>', user_update.as_view()),
    # path('expert/update-partial/(?P<pk>\d+)/$', expert_update.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
