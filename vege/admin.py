from django.contrib import admin
from .models import*
from django.db.models import Sum

admin.site.register(Reciepe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display= ['student','subject','marks']

admin.site.register(Subject_marks,SubjectMarksAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display= ['student','student_rank','total_marks','date_of_report_card_generation']
    ordering= ['student_rank']

    def total_marks(self,obj):
        subject_marks= Subject_marks.objects.filter(student= obj.student)
        marks= subject_marks.aggregate(marks=Sum('marks'))
        return marks['marks']

admin.site.register(Reportcard,ReportCardAdmin)




# Register your models here.
