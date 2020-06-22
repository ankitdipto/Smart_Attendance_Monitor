from django.contrib import admin
from django.contrib.auth.models import auth,User
from accounts.models import students,teachers
from attendance_maker.models import Students_Record,Teachers_Record,Subject_Information
# Register your models here.
#admin.site.register(auth)
#admin.site.register(User)
admin.site.register(students)
admin.site.register(teachers)
admin.site.register(Students_Record)
admin.site.register(Teachers_Record)
admin.site.register(Subject_Information)