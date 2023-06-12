from rest_framework import serializers
from .models import Subject, HallTicket

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'code']

        extra_kwargs = {

            'name': {'required': True},
            'code': {'required': True}
            
        }


    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=20)





class HallTicketSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    

    def get_subjects(self, obj):
        # Retrieve the subjects associated with the hall ticket
        subjects = obj.subjects.all()
        # Perform any serialization or formatting on the subjects data if needed
        # Return the serialized subjects data
        return SubjectSerializer(subjects, many=True).data

    class Meta:
        model = HallTicket
        fields = '__all__'