from .serializers import StudentInfoSerializers,StudentAcademicsSerializers
from .models import StudentAcademics,StudentInfo

class StudentCommonMethods():
    def create_student(self,data):
        try:
            try:
                StudentInfo.objects.get(mobile=data["info"]["mobile"])
                return {"success":False,"error_id": "STUD_Post001", "error_detail": "Student already exist", "status":401}
            except StudentInfo.DoesNotExist:
                
                serializer=StudentInfoSerializers(data=data["info"],partial=True)

                if serializer.is_valid():
                    serializer.save()
                    self.add_academic_details(data["academic_details"],serializer.data['roll_no'])
                    return {"success":True,
                            "status":200}
                else:
                    return {"success":False,
                            "status":400}
        except Exception as e:
            return {"success":False,"error_id": "STUD_Post002", "error_detail": str(e), "status":500}
        

    def get_students(self):
        try:
            print(StudentInfo.objects.all())
            serializer=StudentInfoSerializers(StudentInfo.objects.all(),many=True)
            print("ser",serializer.data)
            return {"success":True,
                    "data":serializer.data,
                        "status":200}

        except Exception as e:
            return {"success":False,"error_id": "STUD_Post001", "error_detail": str(e), "status":500}

    def add_academic_details(selfs,data,roll_no):
        try:
            new_data=data
            new_data["roll_no"]=roll_no
            serializer=StudentAcademicsSerializers(data=new_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return {"success":True,
                        "status":200}
            else:
                return {"success":False,
                        "status":400}
        except Exception as e:
            return {"success":False,"error_id": "STUDAC_Post001", "error_detail": str(e), "status":500}
    # def get_academic_details(data):
    
    # def update_academic_details(data):
        
        