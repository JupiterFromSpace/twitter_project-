from django.contrib import admin
from post.models import UserProfile,Post,Comment,Like

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','email')




admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
