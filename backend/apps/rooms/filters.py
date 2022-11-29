import django_filters
from .models import Rooms

class SnippetFilter(django_filters.FilterSet):
    
    persons = django_filters.NumberFilter()


    class Meta:
        model = Rooms
        fields = ["persons"]