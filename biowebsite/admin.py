from django.contrib import admin
from .models import Record
from .models import remark
from .models import ongoin
from .models import Students

admin.site.register(Record)
admin.site.register(remark)
admin.site.register(ongoin)
admin.site.register(Students)
