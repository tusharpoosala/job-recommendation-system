from datetime import datetime

from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    class Meta:
        db_table = "contact"


class Employer(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    website = models.URLField()
    employer_image = models.ImageField(upload_to='images/')
    established = models.BigIntegerField()
    about = models.CharField(max_length=100)

    class Meta:
        db_table = "employer"


class Candidate(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    candidate_image = models.ImageField(upload_to='images/')
    technologies = models.CharField(max_length=100)
    about_me = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    skills = models.CharField(max_length=100)

    class Meta:
        db_table = "candidate"


class Add_notification(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    experience = models.CharField(max_length=50)
    skills_required = models.CharField(max_length=100)
    responsibility = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    interview_date = models.DateField()
    posted_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "notification"


class Preferences(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    technologies = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    salary = models.BigIntegerField()

    class Meta:
        db_table = "preference"


class Resume(models.Model):
    notification_id = models.ForeignKey(Add_notification, on_delete=models.CASCADE)
    person = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    resume = models.FileField()
    datetime = models.DateTimeField()
    job_status = models.IntegerField(default=0)

    class Meta:
        db_table = "resume"

