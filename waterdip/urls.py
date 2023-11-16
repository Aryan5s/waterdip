from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('add/' , views.add_Task , name = 'ass_Task'),
    path('show/' , views.getAllTask , name = 'getAllTask'),
    path('v1/tasks', views.multipleTaskMethods , name = 'multipleTaskMethods'),
    path('v1/tasks/<id>' , views.specifcTaskMethod , name = 'specificTaskMethod')
]
