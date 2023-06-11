from rest_framework import serializers
from .models import StudentInfo
from rest_framework.validators import UniqueValidator

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ('first_name', 'last_name', 'roll_number', 'date_of_birth', 'department', 'year', 'created_at')

        extra_kwargs = {
            'date_of_birth': {'required': True},
            'year': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'roll_number': {'required': True}
            
        }
    
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    roll_number = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=StudentInfo.objects.all())])
    date_of_birth = serializers.DateField()
    department = serializers.CharField(max_length=100, required= True)
    year = serializers.IntegerField()
    created_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
       instance = StudentInfo.objects.create(**validated_data)
       return instance          