from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import customer
from django import forms
from .models import customer
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from import_export.admin import ImportExportModelAdmin


# class CsvImportForm(forms.Form):
#     csv_upload = forms.FileField()

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'balance')
#     actions = ('make_published')
#     # search_fields= customer.searchableFields

#     def get_urls(self):
#         urls = super().get_urls()
#         new_urls = [path('upload-csv/', self.upload_csv),]
#         return new_urls + urls

#     def upload_csv(self, request):

#         if request.method == "POST":
#             csv_file = request.FILES["csv_upload"]
            
#             if not csv_file.name.endswith('.csv'):
#                 messages.warning(request, 'The wrong file type was uploaded')
#                 return HttpResponseRedirect(request.path_info)
            
#             file_data = csv_file.read().decode("utf-8")
#             csv_data = file_data.split("\n")

#             for x in csv_data:
#                 fields = x.split(",")
#                 created = customer.objects.update_or_create(
#                     name = fields[0],
#                     balance = fields[1],
#                     )
#             url = reverse('admin:index')
#             return HttpResponseRedirect(url)

#         form = CsvImportForm()
#         data = {"form": form}
#         return render(request, "admin/csv_upload.html", data)

class CustomerAdmin(ImportExportModelAdmin):
    pass
    list_display = ('FirstName', 'LastName', 'Title','Company_Name', 'Email', 'Email_Status','Seniority','Departments','Industry','Company_Phone','Employees','Person_Linkedin_Url','Website','Company_Linkedin_Url','Annual_Revenue')
    search_fields= customer.searchableFields

    list_per_page = 10


admin.site.register(customer, CustomerAdmin)