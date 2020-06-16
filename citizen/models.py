from django.db import models
from datetime import datetime


class State(models.Model):
    Code = models.CharField(max_length=200)
    State = models.CharField(max_length=200, )

    def __str__(self):
        return self.State


State.objects.order_by('State')


class District(models.Model):
    Code = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    State = models.ForeignKey('State', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Taluka(models.Model):
    State = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    District = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    Code = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


Taluka.objects.order_by('Name')


class Hobali(models.Model):
    Name = models.CharField(max_length=200)
    State = models.ForeignKey('State', on_delete=models.CASCADE)
    District = models.ForeignKey('District', on_delete=models.CASCADE)
    Taluka = models.ForeignKey('Taluka', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


Hobali.objects.order_by('Name')


class Circle(models.Model):
    State = models.ForeignKey('State', on_delete=models.CASCADE)
    District = models.ForeignKey('District', on_delete=models.CASCADE)
    Taluka = models.ForeignKey('Taluka', on_delete=models.CASCADE)
    Hobali = models.ForeignKey('Hobali', on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


Circle.objects.order_by('Name')


class ConstituencyType(models.Model):
    Code = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Constituency(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.IntegerField()
    State = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    District = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    Taluka = models.ForeignKey('Taluka', on_delete=models.SET_NULL, null=True)
    ConstituencyType = models.ForeignKey('ConstituencyType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name


class PartDetails(models.Model):
    Name = models.CharField(max_length=200)
    Number = models.IntegerField()
    State = models.ForeignKey('State', on_delete=models.CASCADE)
    District = models.ForeignKey('District', on_delete=models.CASCADE)
    Taluka = models.ForeignKey('Taluka', on_delete=models.CASCADE)
    Hobali = models.ForeignKey('Hobali', on_delete=models.CASCADE)
    VillageCity = models.ForeignKey('VillageCity', on_delete=models.CASCADE)
    Circle = models.ForeignKey('Circle', on_delete=models.CASCADE)
    PoliceStation = models.ForeignKey('PoliceStation', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class PoliceStation(models.Model):
    Name = models.CharField(max_length=200)
    State = models.ForeignKey('State', on_delete=models.CASCADE)
    District = models.ForeignKey('District', on_delete=models.CASCADE)
    Taluka = models.ForeignKey('Taluka', on_delete=models.CASCADE)
    Hobali = models.ForeignKey('Hobali', on_delete=models.CASCADE)
    VillageCity = models.ForeignKey('VillageCity', on_delete=models.CASCADE)
    Circle = models.ForeignKey(Circle, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class VillageCity(models.Model):
    Name = models.CharField(max_length=200)
    Pincode = models.IntegerField()
    State = models.ForeignKey('State', on_delete=models.CASCADE)
    District = models.ForeignKey('District', on_delete=models.CASCADE)
    Taluka = models.ForeignKey('Taluka', on_delete=models.CASCADE)
    Hobali = models.ForeignKey('Hobali', on_delete=models.CASCADE)
    Circle = models.ForeignKey('Circle', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class PollingStation(models.Model):
    Name = models.CharField(max_length=200)
    State = models.ForeignKey('State', on_delete=models.CASCADE)
    District = models.ForeignKey('District', on_delete=models.CASCADE)
    Taluka = models.ForeignKey('Taluka', on_delete=models.CASCADE)
    Hobali = models.ForeignKey('Hobali', on_delete=models.CASCADE)
    VillageCity = models.ForeignKey('VillageCity', on_delete=models.CASCADE)
    Circle = models.ForeignKey(Circle, on_delete=models.CASCADE)
    PoliceStation = models.ForeignKey('PoliceStation', on_delete=models.CASCADE)
    PartDetails = models.ForeignKey('PartDetails', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class PressReporters(models.Model):
    City = models.CharField(max_length=200)
    MediaName = models.CharField(max_length=200)
    MediaType = models.CharField(max_length=200)
    Reporter = models.CharField(max_length=200)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Website = models.CharField(max_length=200)

    def __str__(self):
        return self.Reporter


class PressReporterConstituency(models.Model):
    PressReporters = models.ForeignKey('PressReporters', on_delete=models.CASCADE)
    Constituency = models.ForeignKey('Constituency', on_delete=models.CASCADE)
    Status = models.BooleanField()

    def __str__(self):
        return self.Status


class Projects(models.Model):
    Amount = models.IntegerField()
    Description = models.CharField(max_length=200)
    Status = (
        ('Completed', 'Completed'),
        ('Progressing', 'Progressing'),
        ('Sanctioned', 'Sanctioned'),
    )
    status = models.CharField(max_length=20, choices=Status, null=True)
    Title = models.CharField(max_length=200)
    Year = models.DateField()
    Constituency = models.ForeignKey('Constituency', on_delete=models.CASCADE)
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


class Department(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Telephone = models.IntegerField()
    type = (
        'Water Department', 'Water Department',
        'Health Department', 'Health Department',
        'Electric Department', 'Electric Department',
        'Corporation Department', 'Corporation Department',

    )

    def __str__(self):
        return self.Name


class Officers(models.Model):
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)
    Constituency = models.ForeignKey('Constituency', on_delete=models.CASCADE)
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Email = models.EmailField()
    From = models.DateField()
    To = models.DateField()
    Mobile = models.IntegerField()
    Status = (
        ('A', 'Current'),
        ('B', 'retired'),
        ('C', 'On Work'),
    )

    Telephone = models.IntegerField()

    def __str__(self):
        return self.Name


class ServiceProvider(models.Model):
    Class = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    DOB = models.DateField()
    Email = models.EmailField()
    Gender = (
        ('A', 'Male'),
        ('B', 'Female'),
        ('C', 'Other'),
    )
    Mobile = models.IntegerField()
    Telephone = models.IntegerField()
    Constituency = models.ForeignKey('Constituency', on_delete=models.CASCADE)
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Party(models.Model):
    Img = models.ImageField(upload_to='images/', blank=True, null=True)
    Description = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    ShortName = models.CharField(max_length=200)
    SignName = models.CharField(max_length=200)

    def str(self):
        self.Name


class PartyWorkers(models.Model):
    Constituency = models.ForeignKey('Constituency', on_delete=models.CASCADE)
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)

    PollingStation = models.ForeignKey('PollingStation', on_delete=models.CASCADE)
    Party = models.ForeignKey('Party', on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Email = models.EmailField()
    Mobile = models.IntegerField()
    Status = models.BooleanField(default=True)

    def __str__(self):
        return self.Name


class Members(models.Model):
    FirstName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    MeritalStatus = (
        ('A', 'Single'),
        ('B', 'Married'),
        ('C', 'divorced'),
        ('D', 'widowed'),
    )

    Dob = models.DateField()
    Mobile = models.IntegerField()
    SpouseName = models.CharField(max_length=200)
    Telephone = models.IntegerField()
    Website = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to='Photo/', blank=True, null=True)
    MembersType = models.ForeignKey('MembersType', on_delete=models.CASCADE)
    Constituency = models.ForeignKey('Constituency', on_delete=models.CASCADE)
    ConstituencyType = models.ForeignKey('ConstituencyType', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.FirstName


class PositionHeld(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)
    From = models.DateField()
    To = models.DateField()
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)


class MembersType(models.Model):
    Code = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)

    def __str__(self):
        return self.Title


class MemberAddress(models.Model):
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Pincode = models.CharField(max_length=200)
    Type = (
        ('A', 'Capital'),
        ('B', 'Office'),
        ('C', 'Permanent'),
    )
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)


class PersonalAssistant(models.Model):
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to='Photo/', blank=True, null=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Mobile = models.IntegerField()
    Status = models.BooleanField()
    Telephone = models.IntegerField()


class Citizen(models.Model):
    Address = models.ForeignKey('FamilyDetails', on_delete=models.CASCADE)
    State = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    District = models.ForeignKey('District', on_delete=models.CASCADE, default=True)
    Taluka = models.ForeignKey('Taluka', on_delete=models.CASCADE, default=True)
    Hobali = models.ForeignKey('Hobali', on_delete=models.CASCADE, default=True)
    SlNo = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    Profession = models.CharField(max_length=200)
    DOB = models.DateField()
    Qualification = models.CharField(max_length=200)
    EPICNo = models.CharField(max_length=200)
    Email = models.EmailField()
    FatherHusband = models.CharField(max_length=200)
    Gender = (
        ('A', 'Male'),
        ('B', 'Female'),
        ('C', 'Other'),
    )
    Mobile = models.IntegerField()
    Religion = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class FamilyDetails(models.Model):
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)  # Head of the family or member of the family

    def __str__(self):
        return self.Address


class FamilyMembers(models.Model):
    Type = (
        ('A', 'State'),
        ('B', 'District'),
    )
    Citizen = models.ForeignKey('Citizen', on_delete=models.CASCADE)
    Family = models.ForeignKey('FamilyDetails', on_delete=models.CASCADE)


class Grievances(models.Model):
    Description = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    Remarks = models.CharField(max_length=200)
    Status = (
        ('A', 'Progressing'),
        ('B', 'Technical Problem'),
        ('C', 'Solved'),
        ('D', 'NotSolved'),
    )
    Subject = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Citizen = models.ForeignKey('Citizen', on_delete=models.CASCADE)
    Documents = models.FileField(upload_to='Files/', blank=True, null=True)
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)
    Officers = models.ForeignKey('Officers', on_delete=models.CASCADE)
    Members = models.ForeignKey('Members', on_delete=models.CASCADE)
    Date = models.DateField()


class CommitteeStructure(models.Model):
    Position = models.CharField(max_length=200)
    Numbers = models.IntegerField()


class CommitteeStructure123(models.Model):
    Position = models.CharField(max_length=200)
    Numbers = models.IntegerField()
    def __str__(self):
        return self.Position


class Committee(models.Model):
    Name = models.CharField(max_length=200)
    ShortName = models.CharField(max_length=200)
    Level = (
        ('N', 'National'),
        ('S', 'State'),
        ('D', 'District'),
        ('T', 'Taluka'),
    )


class Committee123(models.Model):
    Name = models.CharField(max_length=200)
    ShortName = models.CharField(max_length=200)
    Level = (
        ('National', 'National'),
        ('State', 'State'),
        ('District', 'District'),
        ('Taluka', 'Taluka'),
    )
    level = models.CharField(max_length=20, choices=Level, null=True)
    def __str__(self):
        return self.Name

class CommitteeMembers(models.Model):
    PartyWorkers = models.ForeignKey('PartyWorkers', on_delete=models.CASCADE)
    Committee = models.ForeignKey('Committee', on_delete=models.CASCADE)
    CommitteeStructure = models.ForeignKey('CommitteeStructure', on_delete=models.CASCADE)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Status = models.BooleanField()


class CommitteeMembers123(models.Model):
    PartyWorkers = models.ForeignKey('PartyWorkers', on_delete=models.CASCADE,null=True)
    Committee = models.ForeignKey('Committee123', on_delete=models.CASCADE)
    CommitteeStructure = models.ForeignKey('CommitteeStructure123', on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, null=True)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Status = models.BooleanField()


class Events123(models.Model):
    Date = models.DateField()
    SubmitDate = models.DateTimeField(auto_now_add=True, null=True)
    Description = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    Time = models.TimeField()
    Title = models.CharField(max_length=200)
    Documents = models.FileField(upload_to='Files/', blank=True, null=True)


class EventPhoto(models.Model):
    File = models.FileField()
    Title = models.CharField(max_length=200)
    Event = models.ForeignKey('Events123', on_delete=models.CASCADE)


class PressReporterConstituency123(models.Model):
    PressReporters = models.ForeignKey('PressReporters', on_delete=models.CASCADE)
    Constituency = models.ForeignKey('Constituency', on_delete=models.CASCADE)
    Status = models.BooleanField()

    def __str__(self):
        return self.Status


class Party123(models.Model):
    Img = models.ImageField(upload_to='images/', blank=True, null=True)
    Description = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    ShortName = models.CharField(max_length=200)
    SignName = models.CharField(max_length=200)

    def str(self):
        self.Name


class Event(models.Model):
    Date = models.DateField()
    SubmitDate = models.DateTimeField(auto_now_add=True, null=True)
    Description = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    Time = models.TimeField()
    Title = models.CharField(max_length=200)
    Documents = models.FileField(upload_to='Files/', blank=True, null=True)
