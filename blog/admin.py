from django.contrib import admin
<<<<<<< HEAD
from blog.models import KategoriModel,YazilarModel

admin.site.register(KategoriModel)
=======
from blog.models import KategoriModel, YazilarModel

admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = (
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    
    )

admin.site.register(YazilarModel, YazilarAdmin)

>>>>>>> 22084b3 (Yazi Admin paneli düzenlendi.)

