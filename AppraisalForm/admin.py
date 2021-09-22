from AppraisalForm.models import AppraisalForm, AppraisalForm2, AppraisalForm3, BackupApiScores, DatesToTrack, EXPDate, GrandApiScores
from django.contrib import admin

# Register your models here.

admin.site.register(AppraisalForm)
admin.site.register(AppraisalForm2)
admin.site.register(AppraisalForm3)
admin.site.register(GrandApiScores)
admin.site.register(BackupApiScores)
admin.site.register(DatesToTrack)
admin.site.register(EXPDate)