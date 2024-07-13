from django.contrib import admin
from App.models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportModelAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username','phone', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)


@admin.register(Huduma)
class HudumaAdmin(ImportExportModelAdmin):
    list_display = ["id","JinaLaHuduma","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["JinaLaHuduma"]

@admin.register(MgawanjoWaHuduma)
class MgawanjoWaHudumaAdmin(ImportExportModelAdmin):
    list_display = ["id","JinaLaHuduma","Category","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["JinaLaHuduma"]


@admin.register(UmriWaKuku)
class UmriWaKukuAdmin(ImportExportModelAdmin):
    list_display = ["id","UmriKwaWiki","UmriKwaSiku","Created","Updated"]
    list_filter =["Created","Updated","UmriKwaWiki"]
    search_fields = ["UmriKwaWiki","UmriKwaSiku"]



@admin.register(AinaZaKuku)
class AinaZaKukuAdmin(ImportExportModelAdmin):
    list_display = ["id","AinaYaKuku","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["AinaYaKuku"]


@admin.register(UnitZaVyakula)
class UnitZaVyakulaAdmin(ImportExportModelAdmin):
    list_display = ["id", "Unit", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Unit"]



@admin.register(Vyakula)
class VyakulaAdmin(ImportExportModelAdmin):
    list_display = ["id","product_name","price","ProductQuantity","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["product_name"]


@admin.register(TaarifaZaKuku)
class TaarifaZaKukuAdmin(ImportExportModelAdmin):
    list_display = ["id", "AinaYaKuku","JinaLaChakula","UmriKwaWiki", "Created","Updated"]
    list_filter =["Created","Updated"]
    # search_fields = ["Unit"]


#----------------MWISHO WA BASA KUKU-----------------------------


admin.site.register(MyUser, MyUserAdmin)

