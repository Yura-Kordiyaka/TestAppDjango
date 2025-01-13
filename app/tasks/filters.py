import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    assigned_to_user = django_filters.BooleanFilter(
        field_name='assignee',
        method='filter_assigned_to_user',
        label='Assigned to User'
    )

    class Meta:
        model = Task
        fields = []

    def filter_assigned_to_user(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(assignee=user)
        return queryset
