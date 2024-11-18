from django.urls import path
from hello import views
from hello import email
from .views import Add_students

urlpatterns = [
    path("", views.home, name="home"),
    path('school/', views.school, name='school'),
    path('profile/<slug:slug>/', views.profile_view, name='profile'),
    path('send_message/', email.send_message, name='send_message'),
    path('Add_students/', Add_students.as_view(), name='Add_students'),
    path('delete-student/<slug:slug>/', views.delete_student, name='delete_student'),
]
