from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

CLUB_CATEGORIES = (
    ("0", "Academic and Professional"),
    ("1", "Community Leadership"),
    ("2", "Cultural Diversity"),
    ("3", "Greek Life"),
    ("4", "Performing Arts & Media"),
    ("5", "Religious and Spiritual"),
    ("6", "Service"),
    ("7", "Social and Recreational"),
    ("8", "Special Interest"),
)

COLLEGES = (
    ("0", "Capital University"),
    ("1", "Central Ohio Technical College"),
    ("2", "Columbus College of Art & Design"),
    ("3", "Columbus State Community College"),
    ("4", "Denison University"),
    ("5", "Ohio Dominican University"),
    ("6", "Ohio University"),
    ("7", "Ohio Wesleyan University"),
    ("8", "Otterbein University"),
    ("9", "The Ohio State University"),
)

REDBULL_OCCASIONS = (
    ("0", "Fitness"),
    ("1", "Party & Socializing"),
    ("2", "Work"),
    ("3", "Study"),
)


## These models below are for the Contacts page
class Club (models.Model):
    club_name = models.CharField(max_length = 240)
    description = models.TextField()
    category = models.CharField(max_length=1, choices=CLUB_CATEGORIES)
    college = models.CharField(max_length=1, choices=COLLEGES)
    redbull_occasion = models.CharField(max_length=1, choices=REDBULL_OCCASIONS)
    contacts = models.ManyToManyField ('Person')
    student_marketers =  models.ManyToManyField (User)


class Person (models.Model):
    first_name = models.CharField (max_length = 30)
    last_name = models.CharField (max_length = 30)
    email = models.EmailField (max_length = 240, blank=True)
    number = PhoneField (blank=True, help_text='Contact phone number')
    clubs = models.ManyToManyField (Club)
    student_marketers = models.ManyToManyField (User)

    # a toString funciton
    def _str_ (self):
        return self.first_name