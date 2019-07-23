from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tasklist, name='task-list'),
]
