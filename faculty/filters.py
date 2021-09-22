from AppraisalForm.models import AppraisalForm, BackupApiScores, GrandApiScores
from django.db.models import fields
import django_filters
from django_filters import DateFilter, CharFilter
from django_filters.filters import BooleanFilter

from .models import *

class DepartmentFilter(django_filters.FilterSet):
    
    class Meta:
        model = AppraisalForm
        fields = ['department','designation','whether_HOD','submitted_Faculty','submitted_HOD','submitted_Principal']
        
class GradedDeptFilter(django_filters.FilterSet):

    class Meta:
        model = GrandApiScores
        fields = ['department']

class BackupFilter(django_filters.FilterSet):

    class Meta:
        model = BackupApiScores
        fields = ['academic_year','department']