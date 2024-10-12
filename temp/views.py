from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from category.models import Category, SubCategory
from temp.models import Checkout
from product.models import Product
from heroslider.models import HeroSlider



class Cart:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the cart from the session
        cart = self.request.session.get('cart', {})
        context['cart'] = cart
        
        # Calculate total price of the cart
        cart_total = sum(float(item['price']) * item['quantity'] for item in cart.values())
        context['cart_total'] = cart_total
        
        return context



class CommonMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Prefetch categories and subcategories to avoid additional queries
        context['categories'] = Category.objects.prefetch_related('subcategory').all()

        # Optionally get all products if needed
        context['productss'] = Product.objects.all()

        # Check if a slug is present for the current product (for product detail views)
        slug = self.kwargs.get('slug')
        if slug:
            try:
                # Get the current product
                product = Product.objects.get(slug=slug)
                context['product'] = product

                # Get related products by category, excluding the current product
                related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]  # Limit to 4 related products
                context['related_products'] = related_products
            except Product.DoesNotExist:
                context['product'] = None
                context['related_products'] = []

        return context



class Index(CommonMixin,Cart ,TemplateView):
    template_name = "temp/Index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = HeroSlider.objects.first()

        # Get search query, category, and subcategory from query parameters
        search_query = self.request.GET.get('search', '')
        category_slug = self.request.GET.get('category')
        subcategory_slug = self.request.GET.get('subcategory')

        # Start with all products
        products = Product.objects.all()

        # Filter by subcategory if provided
        if subcategory_slug:
            subcategory = SubCategory.objects.get(slug=subcategory_slug)
            products = products.filter(subcategory=subcategory)

        # Filter by category if provided
        elif category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)

        # Filter by product name if search query is provided
        if search_query:
            products = products.filter(product_name__icontains=search_query)

        # Add the filtered products to the context
        context['products'] = products

        # Get all categories and subcategories for the filter menu
        context['categories'] = Category.objects.prefetch_related('subcategory').all()

        return context




class Shop(CommonMixin,Cart,TemplateView):
    template_name = "temp/shop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch all categories
        context['categories'] = Category.objects.all()

        # Filter products based on selected categories
        selected_categories = self.request.GET.getlist('category')  # Get list of selected categories
        products = Product.objects.all()  # Start with all products

        if selected_categories:
            products = products.filter(category__id__in=selected_categories)

        # Filter by price range
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price and max_price:
            products = products.filter(product_price__gte=min_price, product_price__lte=max_price)

        # Filter by stock status
        if self.request.GET.get('in_stock') == 'true':
            products = products.filter(product_quantity__gt=0)  # Assuming product_quantity > 0 means in stock

        # Sorting logic
        sort_option = self.request.GET.get('sort')  # Get the sorting option
        if sort_option == 'high_to_low':
            products = products.order_by('-product_price')  # Sort by price descending
        elif sort_option == 'low_to_high':
            products = products.order_by('product_price')  # Sort by price ascending

        context['products'] = products  # Assign sorted/filtered products to context
        
        return context
    


class CheckOut(CommonMixin,Cart, TemplateView):
    template_name = "temp/Checkout.html"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            # Get cart items from session
            cart = request.session.get('cart', {})
            
            # Initialize total price, product names, and product quantities
            cart_total = 0.0
            product_names = []
            product_quantities = {}

            # Calculate total price, gather product names, and collect quantities
            for product_id, item in cart.items():
                price = float(item['price'])
                quantity = int(item['quantity'])
                cart_total += price * quantity
                product_names.append(item['product_name'])  # Collect product names
                product_quantities[item['product_name']] = quantity  # Store quantities

            # Check product availability and update quantities
            for product_id, item in cart.items():
                product = Product.objects.get(id=product_id)  # Retrieve the product
                if product.product_quantity < item['quantity']:
                    # Handle insufficient stock (e.g., show an error message)
                    return render(request, self.template_name, {
                        'error': f'Not enough stock for {item["product_name"]}.'
                    })

                # Reduce product quantity in the database
                product.product_quantity -= item['quantity']
                product.save()  # Save the updated product

            # Create a new Checkout object
            checkout = Checkout(
                first_name=request.POST.get('firstName'),
                last_name=request.POST.get('lastName'),
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                address=request.POST.get('address'),
                address2=request.POST.get('address2', ''),
                country=request.POST.get('country'),
                state=request.POST.get('state'),
                zip_code=request.POST.get('zip'),
                payment_method=request.POST.get('paymentMethod'),
                total_price=cart_total,
                product_names=', '.join(product_names),  # Save product names as a comma-separated string
                product_quantities=product_quantities  # Save product quantities
            )
            checkout.save()

            # Optionally clear the cart after checkout
            request.session['cart'] = {}
            request.session['cart_total'] = 0

            # Redirect to a success page
            return redirect('index')

        return render(request, self.template_name)




class SinglePage(CommonMixin, Cart,TemplateView):
    template_name = "temp/ProductDetails.html"
    
    


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def add_to_cart(request):
    if request.method == 'POST':
        # Parse the JSON body of the request
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))
        request.session.modified = True 

        # Get the product
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product does not exist'}, status=404)

        # Get the cart from the session, or create a new cart
        cart = request.session.get('cart', {})

        # Check if product is already in the cart and update the quantity
        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] = {
                'product_name': product.product_name,
                'quantity': quantity,
                'price': str(product.product_price)  # Store as string for JSON compatibility
            }

        # Save the updated cart in the session
        request.session['cart'] = cart

        # Set the session to expire after 10 minutes
        request.session.set_expiry(600)  # 600 seconds = 10 minutes

        return JsonResponse({'message': 'Product added to cart', 'cart': cart})

    return JsonResponse({'error': 'Invalid request'}, status=400)