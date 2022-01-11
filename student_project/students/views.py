from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .methods import StudentCommonMethods
from .forms import StudentRegistartion
from .models import StudentInfo

stud_obj=StudentCommonMethods()




# Create your views here.
class StudentInfoView(APIView):
    def post(self,request,format=None):
        print("pass1",request.data)
        ret_data=stud_obj.create_student(request.data)
        return JsonResponse(ret_data,status=ret_data["status"])
        
    def get(self,format=None):
        ret_data=stud_obj.get_students()
        return JsonResponse(ret_data,status=ret_data["status"])
            
            
# for insert and fetch data
def add_show(request):
    try:
        context ={}
        if request.method=='POST':
            #call form class here
            frm=StudentRegistartion(request.POST)
            if frm.is_valid():#check valid form
                frm.save()
                # after save get blank form here
                frm=StudentRegistartion()
            context['form']=frm
        else:
            frm=StudentRegistartion()
        # every time we get all records from the model
        stud_data=StudentInfo.objects.all()
        context['form']=frm
        context['std_data']=stud_data
        return render(request,'add_show.html',context)
    except Exception as e:
        print("exception",e)
        
def delete_records(request,roll_no):
    try:
        if request.method=='POST':
            stud_data=StudentInfo.objects.get(roll_no=roll_no)
            stud_data.delete()
            return HttpResponseRedirect('/students/add')
    except Exception as e:
        print("exception",e)
        

def update_records(request,roll_no):
    try:
        if request.method=='POST':
            s_data=StudentInfo.objects.get(roll_no=roll_no)
            frm= StudentRegistartion(request.POST,instance=s_data)
            if frm.is_valid():
                frm.save()
                return HttpResponseRedirect('/students/add')
                # frm=StudentRegistartion()
        else:
            s_data=StudentInfo.objects.get(roll_no=roll_no)
            frm= StudentRegistartion(instance=s_data)
            
        return render(request,'update_show.html',{'form':frm})
    except Exception as e:
        print("exception",e)
        

    