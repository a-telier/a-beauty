from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category

from django.db.models.functions import Lower

# Create your views here.

#   This view allows you to see all products
def all_products(request):
    products = Product.objects.all()
    all_categories = Category.objects.all()
    categories = None
    query = None
    sort = 'price'
    direction = 'asc'

    if request.GET:
        #   Sorting by
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        #   Category filtering
        if 'category' in request.GET:
            # spslit into a list by commas
            # use the list to filter the current queries
            # to only products which cat name are on the list
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        #   Search function
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search criteria entered')
                return redirect(reverse('products'))

            # creating a Q object to pass a query
            # the pipe | generates the 'or' statement
            # i in front of contains make it not case sensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'all_categories': all_categories,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, "products/products.html", context)


#   This view allows you to view each product individually
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    all_categories = Category.objects.all()

    context = {
        'product': product,
        'products': products,
        'all_categories': all_categories,
    }

    return render(request, "products/product_detail.html", context)