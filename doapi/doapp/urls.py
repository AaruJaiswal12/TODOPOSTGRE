from django.urls import path
from .views import TaskView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('get/', TaskView.as_view(), name="get"),
    path('post/', TaskView.as_view(), name="post"),
    path('put/', TaskView.as_view(), name="put"),
    path('delete/', TaskView.as_view(), name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
