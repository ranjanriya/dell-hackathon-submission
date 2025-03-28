from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Service, Support
from cart.forms import CartAddProductForm
from shop.forms import FeedbackForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    current_user = request.user.userprofile
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'current_user': current_user})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/service_detail.html',
                  {'service': service,
                   'cart_product_form': cart_product_form})


def support_page(request):
    supports = Support.objects.all()

    return render(request, 'shop/product/support.html', {'supports': supports})


# todo
def service_render(request, product_id):
    print("Product ID : " + str(product_id))
    services = Service.objects.all()
    recommended_services = []
    for service in services:
        print("Service Product ID " + str(service.product.product_id) + " Product ID " + str(product_id))
        if service.product.product_id == product_id:
            print(str(service.product.product_id) + " " + str(product_id))
            recommended_services.append(service)
    print("Recommended Services " + str(recommended_services))
    user_profile_id = request.user.userprofile.custom_user_id
    print("User Profile ID : " + str(user_profile_id))

    return render(request, 'shop/product/services-.html', {'services': recommended_services})


def feedback_form(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_detail = feedback_form.save()
            feedback_detail.save()
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
    else:
        feedback_form = FeedbackForm()
    return render(request, 'shop/product/feedback.html',
                  {'feedback_form': feedback_form})


def service_purchased(request):
    return render(request, 'shop/product/service_purchased.html', {})
