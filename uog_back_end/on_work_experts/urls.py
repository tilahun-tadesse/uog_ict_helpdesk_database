from posixpath import relpath
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('on_work-list/', on_work_expert_list.as_view()),
    path('on_work-delete/<str:expert_id>', on_work_expert_update.as_view()),
    path('on_work-update/<str:expert_id>', on_work_expert_update_one.as_view()),
    # path('expert/update-partial/(?P<pk>\d+)/$', expert_update.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
