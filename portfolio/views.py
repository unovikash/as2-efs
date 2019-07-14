from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Customer, Stock, Investment
from .forms import CustomerForm, StockForm, InvestmentForm

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
def customer_new(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
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
        form = CustomerForm()
    return render(request, 'portfolio/customer_edit.html', {
        'form':form
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

# Stock Views
@login_required
def stock_list(request):
    stock_list = Stock.objects.filter(purchase_date__lte=timezone.now())
    return render(request, 'portfolio/stock_list.html', {
        'stock_list': stock_list
    })

@login_required
def stock_new(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_date = timezone.now()
            stock.save()
            # redirect to customer list page
            stock_list = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/stock_list.html', {
                'stock_list': stock_list,
            })
    else:
        #Edit
        form = StockForm()
    return render(request, 'portfolio/stock_edit.html', {
        'form':form
    })

@login_required
def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance = stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.updated_date = timezone.now()
            stock.save()
            # redirect to customer list page
            stock_list = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/stock_list.html', {
                'stock_list': stock_list,
            })
    else:
        #Edit
        form = StockForm(instance=stock)
    return render(request, 'portfolio/stock_edit.html', {
        'form':form
    })

@login_required
def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    stock.delete()
    return redirect('portfolio:stock_list')

# Investment Views
@login_required
def investment_list(request):
    investment_list = Investment.objects.filter(acquired_date__lte=timezone.now())
    return render(request, 'portfolio/investment_list.html', {
        'investment_list': investment_list
    })

@login_required
def investment_new(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.recent_date = timezone.now()
            investment.recent_value = form.cleaned_data['acquired_value']
            #investment.recent_value = request.POST.get['acquired_value']
            investment.save()
            # redirect to customer list page
            investment_list = Investment.objects.filter(acquired_date__lte=timezone.now())
            return render(request, 'portfolio/investment_list.html', {
                'investment_list': investment_list,
            })
    else:
        #Edit
        form = InvestmentForm()
    return render(request, 'portfolio/investment_edit.html', {
        'form':form
    })

@login_required
def investment_edit(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance = investment)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.updated_date = timezone.now()
            investment.save()
            # redirect to customer list page
            investment_list = Investment.objects.filter(acquired_date__lte=timezone.now())
            return render(request, 'portfolio/investment_list.html', {
                'investment_list': investment_list,
            })
    else:
        #Edit
        form = InvestmentForm(instance=investment)
    return render(request, 'portfolio/investment_edit.html', {
        'form':form
    })

@login_required
def investment_delete(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    investment.delete()
    return redirect('portfolio:investment_list')