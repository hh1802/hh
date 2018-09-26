from rest_framework import serializers

from app.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 's_name', 'sy']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['g_name'] = instance.g.g_name



        return data