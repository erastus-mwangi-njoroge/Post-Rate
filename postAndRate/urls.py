from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url('^register/',views.register,name="register"),
    url('^profile/',views.profile,name="profile"),
    url('^login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    url('^logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    url('^api/projects/$', views.ProjectList.as_view(),name="all_projects_api"),
    url('^api/profiles/$',views.ProfileList.as_view(),name="all_profiles_api"),
    url('^ajax/rate/(?P<pk>\d+)',views.AjaxRating,name="ajaxrating"),
    url(r'^$',views.Index_view,name="index_view"),
    url(r'^upload/$',views.Upload_Project,name="upload_project"),
    url(r'^rating/(?P<pk>\d+)$',views.RateProject,name="rate_project"),
    url(r'^myprofile/',views.User_Profile,name="my_profile"),
    url(r'^endpoints/',views.Endpoints,name="endpoints")
]