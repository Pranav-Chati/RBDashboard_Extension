from rest_framework import serializers
from .models import Club, Person

class PersonSerializer (serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id', 
            'first_name',
            'last_name',
            'email',
            'number',
            'clubs',
            'student_marketers',
        )
        
class ClubSerializer (serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = (
            'id',
            'club_name',
            'description',
            'category',
            'college',
            'redbull_occasion',
            'contacts',
            'student_marketers',
        )