from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('', views.index, name='home'),
    path('task/<int:id>/', views.detailed_task, name='detailed_task'),
    path('status/<str:st>/', views.todo_by_status, name='todo_by_status'),
    path('category/<int:category_id>/', views.category_tasks, name='category_tasks'),
    path('create-task/', views.create_task, name='create_task'),
    path('create-category/', views.create_category, name='create_category'),
    path('update-task/<int:id>/', views.update_task, name='update_task'),
    path('delete-task/<int:id>/', views.delete_task, name='delete_task'),
]