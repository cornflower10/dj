from django.contrib import admin

# Register your models here.
from Note.models import UserInfo, MerchantInfo, Food, Images

admin.site.register(UserInfo)
admin.site.register(MerchantInfo)
admin.site.register(Food)
admin.site.register(Images)

