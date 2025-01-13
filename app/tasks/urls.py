from django.urls import path
import tasks.views as tasks_views
urlpatterns = [
    path('create/', tasks_views.CreateTaskApi.as_view(), name='create_task'),
    path('list/', tasks_views.ListTaskApi.as_view(), name='list_task'),
    path('<int:pk>/',tasks_views.RetireUpdateDestroyTaskApi.as_view(), name='retire_update_destroy_task'),
]