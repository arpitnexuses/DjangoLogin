from django.db import models
# import django_tables2 as tables
class customer(models.Model):

  FirstName = models.CharField(max_length=50)
  LastName = models.CharField(max_length=50, null=True, blank=True)
  Title = models.CharField(max_length=40, null=True, blank=True)
  Company_Name = models.CharField(max_length=40, null=True, blank=True)
  Email = models.CharField(max_length=50, null=True, blank=True)
  Email_Status = models.CharField(max_length=50, null=True, blank=True)
  Seniority = models.CharField(max_length=50, null=True, blank=True)
  Departments = models.CharField(max_length=50, null=True, blank=True)
  Company_Phone = models.CharField(max_length=50, null=True, blank=True)
  Employees = models.CharField(max_length=50, null=True, blank=True)
  Industry = models.CharField(max_length=50, null=True, blank=True)
  Person_Linkedin_Url = models.CharField(max_length=50, null=True, blank=True)
  Website = models.CharField(max_length=50, null=True, blank=True)
  Company_Linkedin_Url = models.CharField(max_length=50, null=True, blank=True)
  Annual_Revenue = models.CharField(max_length=50, null=True , blank=True)
  searchableFields = ['FirstName', 'LastName', 'Seniority']
  list_filter=['Seniority']

  def __str__(self):
    return self.FirstName
    
