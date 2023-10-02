from django.db import models

# Create your models here.
class Department(models.Model):
    
    department = models.CharField(max_length=255)
    
    def __str__(self):
        return self.department
    
class Information(models.Model):

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,choices=(
        ("ชาย", "ชาย"),
        ("หญิง", "หญิง"),
    ))
    age = models.IntegerField()
    elevel = models.CharField(max_length=255,choices=(
        ("ปวช.", "ปวช."),
        ("ปวส.", "ปวส."),
        ("ปริญญาตรี", "ปริญญาตรี"),
        ("สูงกว่าปริญญาตรี", "สูงกว่าปริญญาตรี")
    ))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.fname  