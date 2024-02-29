from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup', views.signup, name= 'signup'),
    path('login', views.log, name= 'login'),
    path('home', views.home, name= 'home'),
    path('explore', views.explore, name= 'explore'),
    path('notifications', views.nots, name= 'notifications'),
    path('messages', views.msg, name= 'messages'),
    path('logout_user', views.logout_user, name='logout'),    
    path('activate/<slug:uidb64>/<slug:token>', views.activate, name='activate'),  
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="passreset.html",html_email_template_name='passresetemail.html',),name="password_reset"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="passresetdone.html"),name="password_reset_done"),
    path('reset/<slug:uidb64>/<slug:token>',auth_views.PasswordResetConfirmView.as_view(template_name="passresetconfirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="passresetcomplete.html"),name="password_reset_complete"),
]