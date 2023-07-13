from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register_company', views.register_company, name="register-company"),
    path('register_candidate', views.register_candidate, name="register-candidate"),

    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),


    # CRUD

    path('dashboard', views.dashboard, name="dashboard"),
    path('create-record', views.create_job, name="create-record"),
    path('update-record/<int:pk>', views.update_job, name='update-record'),
    path('job/<int:pk>', views.singular_job, name="job"),
    path('delete-record/<int:pk>', views.delete_job, name="delete-record"),
    path('view-candidates/<int:pk>', views.candidates, name="view-candidates"),
    path('apply_job/<int:pk>', views.aplly_job, name="apply_job"),


]
