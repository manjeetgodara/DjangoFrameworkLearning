from faker import Faker

fake=Faker()

import random
from .models import *


def seed_db(n=10) -> None:
   try: 
      for _ in range(n):
         dept=Department.objects.all()
         index=random.randint(0,len(dept)-1)
         department=dept[index]
         student_id=f"STU-0{random.randint(0,99)}"
         student_name=fake.name()
         student_email=fake.email()
         student_age=random.randint(20,30)
         student_address=fake.address()

         student_id_obj=StudentId.objects.create(student_id=student_id)

         student_obj=Student.objects.create(
             department=department,
             student_id=student_id_obj,
             student_age=student_age,
             student_name=student_name,
             student_email=student_email,
             student_address=student_address

         )
   except Exception as e:
     print(e)        
