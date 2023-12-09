"""daily_walkins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from dailyapp import views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index,name="index"),
    path('new_post/',v.new_post,name="new_post"),
    #path('browse_jobs/',v.browse_jobs,name="browse_jobs"),
    #path('candidates/',v.candidates,name="candidates"),
    path('contact/',v.contact,name="contact"),
    path('job_post/',v.job_post,name="job_post"),
    path('send_message/',v.send_message,name="send_message"),
    path('employer/',v.employer,name="employer"),
    path('employer_reg/',v.employer_reg,name="employer_reg"),
    path('employer_login/',v.employer_login,name="employer_login"),
    path('employer_view/',v.employer_view,name="employer_view"),
    path('employer_logout/',v.employer_logout,name="employer_logout"),
    path('employer_chpwd/',v.employer_chpwd,name="employer_chpwd"),
    path('employer_edit/<int:id>',v.employer_edit,name="employer_edit"),
    path('employer_update/',v.employer_update,name="employer_update"),
    path('employer_delete/<int:id>',v.employer_delete,name="employer_delete"),
    path('candidate/',v.candidate,name="candidate"),
    path('candidate_reg/',v.candidate_reg,name="candidate_reg"),
    path('candidate_login/',v.candidate_login,name="candidate_login"),
    path('candidate_view/',v.candidate_view,name="candidate_view"),
    path('candidate_logout/',v.candidate_logout,name="candidate_logout"),
    path('candidate_chpwd/',v.candidate_chpwd,name="candidate_chpwd"),
    path('candidate_edit/<int:id>',v.candidate_edit,name="candidate_edit"),
    path('candidate_update/',v.candidate_update,name="candidate_update"),
    path('candidate_delete/<int:id>',v.candidate_delete,name="candidate_delete"),
    path('add_notification/',v.add_notification,name="add_notification"),
    path('notification_view/',v.notification_view,name="notification_view"),
    path('notification_edit/<int:id>',v.notification_edit,name="notification_edit"),
    path('notification_update/',v.notification_update,name="notification_update"),
    path('notification_delete/<int:id>',v.notification_delete,name="notification_delete"),
    path('set_preferences/',v.set_preferences,name="set_preferences"),
    path('view_preference/',v.view_preference,name="view_preference"),
    path('preference_edit/<int:id>',v.preference_edit,name="preference_edit"),
    path('preference_update/',v.preference_update,name="preference_update"),
    path('preference_delete/<int:id>',v.preference_delete,name="preference_delete"),
    path('view_notifications/',v.view_notifications,name="view_notifications"),
    path('recomend/',v.recomend,name="recomend"),
    path('resume_upload/',v.resume_upload,name="resume_upload"),
    path('unknown/',v.unknown,name="unknown"),
    path('empunknown/',v.empunknown,name="empunknown"),
    path('applyjob/<int:id>',v.applyjob,name="applyjob"),
    path('apply_display/',v.apply_display,name="apply_display"),
    path('job_applied/<int:id>',v.job_applied,name="job_applied"),
    path('job_approve/<str:applied_id>',v.job_approve,name="job_approve"),
    path('job_reject/<str:applied_id>',v.job_reject,name="job_reject"),


]






if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)