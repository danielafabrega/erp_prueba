from django.contrib import admin

# Register your models here.


from .models import Product
from .models import Supplier
from .models import Booksale
from .models import Kardex
from .models import Customer



class SupplierAdmin(admin.ModelAdmin):
    search_fields=('supplier_id',)

admin.site.register(Product)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Booksale)
admin.site.register(Kardex)
admin.site.register(Customer)
