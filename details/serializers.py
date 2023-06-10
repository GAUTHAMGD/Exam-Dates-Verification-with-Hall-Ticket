from rest_framework import serializers
from .models import StudentInfo
from rest_framework.validators import UniqueValidator

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        extra_kwargs = {
            'date_of_birth': {'required': True},
            'year': {'required': True}
        }
    
    first_name = serializers.CharField(max_length=100, read_only=True)
    last_name = serializers.CharField(max_length=100, read_only=True)
    roll_number = serializers.CharField(max_length=20, read_only=True, validators=[UniqueValidator(queryset=StudentInfo.objects.all())])
    date_of_birth = serializers.DateField()
    department = serializers.CharField(max_length=100, read_only=True)
    year = serializers.IntegerField()
    created_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
       instance = StudentInfo.objects.create(**validated_data)
       return instance
       
                    
    



   

