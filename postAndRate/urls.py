from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('^register/',views.register,name="register"),
    path('^profile/',views.profile,name="profile"),
    path('^login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('^logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('^api/projects/$', views.ProjectList.as_view(),name="all_projects_api"),
    path('^api/profiles/$',views.ProfileList.as_view(),name="all_profiles_api"),
    path('^ajax/rate/(?P<pk>\d+)',views.AjaxRating,name="ajaxrating")
]