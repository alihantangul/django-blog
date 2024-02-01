from django.db import models

class IletisimModel(models.Model):
    email = models.EmailField(max_length = 250, blank=False, null= False)
    isim_soyisim = models.CharField(max_length = 150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateField(auto_now_add = True)

    class Meta : 
        db_table = 'iletisim'
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.email
