# Owned by Yash Jangid 
# github_id = yash-jangid-21
# linkeldn_id = yash-21-yash

from django.db import models
from django.db import models
from django.contrib.auth.models import User

class department(models.Model):
    Department_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Department_Name
    
    class Meta:
        ordering = ['Department_Name']

class subject(models.Model):
    Subject_Name = models.CharField(max_length=20)
    def __str__(self):
        return self.Subject_Name
    
    class Meta:
        ordering = ['Subject_Name']
    
class card(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Student_Name = models.CharField(max_length=20,null=True)
    Student_Father_Name = models.CharField(max_length=20,null=True)
    Student_Email = models.EmailField(null=True)
    Student_Department = models.ForeignKey(department,related_name='dep',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.Student_Name
    
    class Meta:
        ordering = ['Student_Name']

class score(models.Model):
    Student = models.ForeignKey(card,on_delete=models.CASCADE,null=True)
    Subject = models.ForeignKey(subject,on_delete=models.CASCADE,null=True)
    Score = models.IntegerField(null=True)
     
    
    def __str__(self):
        return self.Student.Student_Name
    
    class Meta:
        unique_together = ['Student','Subject']