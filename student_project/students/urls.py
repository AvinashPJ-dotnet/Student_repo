from django.urls import path
from students import views

urlpatterns=[
    #students view url has been declared
    path('',views.StudentInfoView.as_view()),
    path('add',views.add_show,name='add_show'),
    path('delete/<int:roll_no>',views.delete_records,name='delete_record'),
    path('update/<int:roll_no>',views.update_records,name='update_record'),
]