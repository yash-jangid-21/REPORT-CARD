# Owned by Yash Jangid 
# github_id = yash-jangid-21
# linkeldn_id = yash-21-yash
from faker import Faker
import random
from .models import *

f = Faker()

def seed_db(n=3) -> None:
    try:
        for _ in range(n):
            department_obj  = department.objects.all()
            random_index = random.randint(0,len(department_obj)-1)
            student = card.objects.create(
                Student_Name = f.name(),
                Student_Father_Name = f.name(),
                Student_Email = f.email(),
                Student_Department = department_obj[random_index]
            )
            subject_obj  = subject.objects.all() 
            for i in range(0,len(subject_obj)):
                score.objects.create(
                 Student = student,
                   Subject = subject_obj[i],
                 Score = random.randint(25,100)
            )
    except Exception as e:
        print(e)