from rest_framework import serializers
from .models import Task
from rest_framework.fields import empty


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','status','title','description']
        extra_kwargs = {'description': {'required': False}}   # Desciption masked as optional

    def validate_title(self, title):   # Validates the title
        if len(title) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return title

    # def validate_status(self, value):
    #     print("17----", value)
    #     valid_choices = [choice[0] for choice in Task.STATUS_CHOICES]
    #     if value not in valid_choices:
    #         raise serializers.ValidationError(f"'{value}' is not a valid choice. Please choose from - {', '.join(valid_choices)}")
    #     return value

    def create(self, validated_data):
      if 'status' not in validated_data:
          validated_data['status'] = 'TO_DO'
      return Task.objects.create(**validated_data)

