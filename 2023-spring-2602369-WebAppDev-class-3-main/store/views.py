from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product, Address, Order

def orm_test(request):
    #number 7
    queryset = Order.objects.filter(payment_status = 'P')
    for order in queryset:
        print(order)

    #number 6
    # queryset = Address.objects.filter(customer__gender = 'F')
    # for address in queryset:
    #     print(address)

    # number 4
    # queryset = Product.objects.filter(price__lt = 100)
    # for product in queryset:
    #     print(product)

    # number 3
    # queryset = Product.objects.filter(collection_id = 1, pk = 1)
    # for product in queryset:
    #     print(product)

    # number 2
    # queryset = Customer.objects.filter(membership = 'G')
    # for current_customer in queryset:
    #     print(current_customer)

    # number 1
    # queryset = Customer.objects.all().order_by('-first_name')
    # for current_customer in queryset:
    #     print(current_customer.first_name)

    # queryset = Product.objects.all().order_by('-title')
    # for product in queryset:
    #     print(product)

    # queryset = Customer.objects.all()
    # for current_customer in queryset:
    #     print(current_customer)

    # first_customer = Customer.objects.get(pk = 5)
    # print("First Store customer")
    # print(first_customer)

    # queryset = Customer.objects.filter(first_name = 'Gomain')
    # for current_customer in queryset:
    #     print(current_customer)

    return render(request, 'orm_test.html', {'queryset': queryset})
