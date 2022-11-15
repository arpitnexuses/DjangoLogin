# Generated by Django 3.2.3 on 2022-11-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enroll', '0002_delete_authentication'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(blank=True, max_length=50, null=True)),
                ('Title', models.CharField(blank=True, max_length=40, null=True)),
                ('Company_Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Email_Status', models.CharField(blank=True, max_length=50, null=True)),
                ('Seniority', models.CharField(blank=True, max_length=50, null=True)),
                ('Departments', models.CharField(blank=True, max_length=50, null=True)),
                ('Company_Phone', models.CharField(blank=True, max_length=50, null=True)),
                ('Employees', models.CharField(blank=True, max_length=50, null=True)),
                ('Industry', models.CharField(blank=True, max_length=50, null=True)),
                ('Person_Linkedin_Url', models.CharField(blank=True, max_length=50, null=True)),
                ('Website', models.CharField(blank=True, max_length=50, null=True)),
                ('Company_Linkedin_Url', models.CharField(blank=True, max_length=50, null=True)),
                ('Annual_Revenue', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]