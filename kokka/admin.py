from django.contrib import admin


from .models import Konten, Pesan, Barang, Comment, Desc
# Register your models here.

admin.site.register(Konten)
admin.site.register(Pesan)
admin.site.register(Barang)
admin.site.register(Comment)
admin.site.register(Desc)
