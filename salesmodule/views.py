from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import F


from .models import Product
from .models import Booksale
from .models import Kardex

# Create your views here.



def busqueda_productos(request):
    products = Product.objects.all()
    return render(request, 'salesmodule/busqueda_productos.html', {"products":products})

def buscar(request):
    if request.GET["product_id"]:
        product_id = request.GET["product_id"]
        product = Product.objects.filter(product_code__icontains=product_id)
        n_stock = request.GET["stock"]
        product.update(stock=F('stock')-n_stock)
        #product_id_stock = Product.objects.get(product_code=product_id)
        #stock = request.GET["stock"]
        #stock = int(stock)
        
        for elem in product:
            price = elem.cost
            neto_price = elem.price
            
        type_document = request.GET["document_type"]
        m_pay = request.GET["m_pay"]

        #Booksale.objects.create(document_type=type_document, price=product.cost, neto_price=product.price, product=product.product_code)
        Booksale.objects.create(document_type=type_document, product_id=product_id, m_pay = m_pay, price=price, neto_price=neto_price)
        Kardex.objects.create(code=product_id, document_type=type_document, price=neto_price, debe=neto_price, haber=price)
        '''
        if product_id_stock.stock>=stock:
            product_id_stock.stock=product_id_stock-stock
            product_id_stock.save(['stock'])
        '''
        #mensaje = "Articulo buscado: %r"%request.GET["product_id"]
        return render(request, 'salesmodule/resultados_busqueda.html', {"product":product, "query":product_id, "type_document":type_document, "m_pay":m_pay})
    else:
        mensaje = "NADA"
        return HttpResponse(mensaje)

    

'''
if request.method == "POST":
        form = BookSaleForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            #product.month_year = timezone.now()
            product_select = form.
            print()
            neto_price = product.price
            total_price = product.price
            product.save()
            #return redirect('index')
    else:
        form = BookSaleForm()
    return render(request, 'salesmodule/index.html', {'form': form})
    '''