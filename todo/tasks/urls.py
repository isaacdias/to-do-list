from django.urls import path
import . from views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tasklist, name='task-list'),
]
