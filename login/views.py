from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .forms import CustomerForm
from .models import Customer
from .serializers import CustomerSerializer
from .pagination import DefaultPagination

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    pagination_class = DefaultPagination
    search_fields = ['name', 'last_name']
    ordering_fields = ['name']

def index(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer/')

    context = {'form': form}
    return render(request, 'login/home.html', context)

def customer(request):
    customers = Customer.objects.all()

    context = {'customers': customers}
    return render(request, 'login/customer.html', context)

def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)

    context = {'customer': customer}
    return render(request, 'login/detail.html', context)

def update(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer')

    context = {'form': form}
    return render(request, 'login/update.html', context)
    
def delete(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer')

    context = {'customer': customer}
    return render(request, 'login/delete.html', context)
