from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Customer
from .forms import CustomerForm

now = timezone.now()

def home(request):
    return render(request, 'portfolio/home.html')

# Create your views here.
@login_required
def customer_list(request):
    customer_list = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/customer_list.html', {
        'customer_list': customer_list
    })

@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            # redirect to customer list page
            customer_list = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'portfolio/customer_list.html', {
                'customer_list': customer_list,
            })
    else:
        #Edit
        form = CustomerForm(instance=customer)
    return render(request, 'portfolio/customer_edit.html', {
        'form':form
    })

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('portfolio:customer_list')