from django.db import models

class Record (models.Model):
    Created_at = models.DateTimeField(auto_now_add=True)
    Common_Name = models.CharField(max_length=100)
    Family_Name = models.CharField(max_length=100)
    Scientific_Name = models.CharField(max_length=100)
    Conservation_status = models.CharField(max_length=100)
    image_link = models.TextField()
    def __str__(self):
        return ("{self.Common_Name} {self.Scientific_Name}")


class remark(models.Model):
    todate = models.DateField()
    re_activity = models.CharField(max_length=100)
    re_remarks = models.CharField(max_length=100)
    re_status = models.CharField(max_length=100)

    def __str__(self):
        return ("{self.todate} {self.re_activity}")
    

class ongoin(models.Model):
    time= models.DateTimeField(auto_created=True)
    ongoing_activity = models.TextField()
    
    def __str__(self):
        return ("{self.ongoing_activity}")

