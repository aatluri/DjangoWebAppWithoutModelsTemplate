from django.db import models

# Create your models here.

class Patient(models.Model):
    fullname = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=150)
    emailaddress = models.CharField(max_length=150,blank=True)
    dateofbirth = models.DateField(max_length=8)
    gender = models.CharField(max_length=6)
    age_range = models.CharField(max_length=150,blank=True)

    # When we do this, in the admin page when the Patients are displayed, it will show their name
    def __str__(self):
        return self.fullname

class QuestionnaireResponses(models.Model):
    smokingstatus = models.CharField(max_length=150,blank=True,null=True)
    drinkingstatus = models.CharField(max_length=150,blank=True,null=True)
    previnfection = models.CharField(max_length=150,blank=True,null=True)
    bloodexposure = models.CharField(max_length=150,blank=True,null=True)
    menstrualhistory = models.CharField(max_length=150,blank=True,null=True)
    comments = models.TextField(blank=True,null=True)
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        primary_key=True,
        )





class Tag(models.Model):
    tagname = models.CharField(max_length=100,unique=True)

    # When we do this, in the admin page when the tags are displayed, it will show their name
    def __str__(self):
        return self.tagname


class DiagnosticTest(models.Model):
    name = models.CharField(max_length=150, unique=True)
    type = models.CharField(max_length=150,blank=True)
    description = models.TextField(blank=True)
    validity_days = models.IntegerField(null=True,blank=True)
    tags =  models.ManyToManyField(Tag,blank=True, editable=True)
    displayicon = models.CharField(max_length=150,blank=True)
    specialinstructions = models.CharField(max_length=200,blank=True)
    samplerequirements = models.CharField(max_length=200,blank=True)
    reportavailability = models.CharField(max_length=150,blank=True)

    # When we do this, in the admin page when the diagnostic tests are displayed, it will show their name
    def __str__(self):
        return self.name

