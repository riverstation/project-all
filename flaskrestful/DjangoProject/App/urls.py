from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^students/', views.StudentView.as_view(msg="666"), name='students'),
    url(r'^studentstemplate/', views.StudentTemplateView.as_view(template_name='Student.html'), name='studentstemplate'),
    url(r'^studentlist/', views.StudentListView.as_view(), name='student_listview'),

    url(r'^login/', views.login, name='login'),
    # url(r'^dologin/', views.do_login, name='do_login'),
]