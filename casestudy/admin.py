from django.contrib import admin
from .models import CaseStudy
from django_summernote.admin import SummernoteModelAdmin

@admin.register(CaseStudy)
class CaseStudyAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')

