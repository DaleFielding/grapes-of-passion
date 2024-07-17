from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


# ---------- ALL PRODUCTS ---------- 
def all_products(request):
    """ 
    Handle the display of all wine products,
    including sorting and search queries
    """
    
    # Get all products and set default values for variables
    products = Product.objects.all()
    query = None
    categories = None
    is_discounted = False
    display_title = "All Products" 
    sort = None
    direction = None

    # Mapping to group certain categories
    grouped_categories = {
        'all-wine': ['red', 'white', 'rose'],
        'all-fortified-wine': ['port', 'sherry']
    }
# When get request contains certain values.
# Sort products by name or category, and handle sort direction.
# Handle grouped categories if specified in query parameters
# Then assign intended title to display_title
    if request.GET:
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

        if 'category' in request.GET:
            category = request.GET['category']
            if category in grouped_categories:
                categories = grouped_categories[category]
                display_title = "All Wine" if category == 'all-wine' else "All Fortified Wine"
            else:
                categories = [category]
                display_title = Category.objects.get(name=category).name.capitalize()
                
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle query searched.
        # If not show error message and redirect to products page.
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
                
            # Filter products by name or type)
            # Then assign query to display_title
            queries = Q(name__icontains=query) | Q(type__icontains=query)
            products = products.filter(queries)
            display_title = f"Results for '{query}'" 

        # If the discounted parameter is in the get request,
        # filter by including products that are not discounted
        # Then assign intended title to display_title
        if 'discounted' in request.GET:
            is_discounted = True
            products = products.exclude(discounted_price__isnull=True)
            display_title = "Discounted Products"  

    # assign f string containing sort and direction to current_sorting
    current_sorting = f'{sort}_{direction}'

    # context variables to be passed to the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'is_discounted': is_discounted,
        'display_title': display_title,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


# ---------- PRODUCT DETAIL ---------- 
def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


# ---------- ADD PRODUCT: ADMIN ----------
def add_product(request):
    """ Add a product to the admin store """

    # Handle form submission and feedback through messaging
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



# ---------- EDIT PRODUCT: ADMIN ----------
def edit_product(request, product_id):
    """ Edit an existing product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)