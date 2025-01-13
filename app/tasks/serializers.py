from rest_framework import serializers
from .models import Task
from app.tasks import send_task_assignment_notification, send_task_update_notification

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'created_by','reminder_sent')


    def create(self, validated_data):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        if user is None:
            raise serializers.ValidationError("user can't be None")

        validated_data['created_by'] = user
        task = Task.objects.create(**validated_data)
        if validated_data.get('assignee',None) is not None:
            send_task_assignment_notification.delay(task.assignee.email, task.title)
        return task

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if validated_data.get('assignee', None) is not None:
            send_task_update_notification.delay(instance.assignee.email, instance.title)
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        due_date = instance.due_date
        if due_date:
            representation['due_date'] = due_date.strftime('%Y-%m-%d %H:%M')

        created_at = instance.created_at
        if created_at:
            representation['created_at'] = created_at.strftime('%Y-%m-%d %H:%M')

        updated_at = instance.updated_at
        if updated_at:
            representation['updated_at'] = updated_at.strftime('%Y-%m-%d %H:%M')
        representation.pop('reminder_sent', None)
        return representation

