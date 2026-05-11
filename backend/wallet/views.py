from django.shortcuts import render, redirect, get_object_or_404

from .models import Transaction
from .forms import TransactionForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Landing Page
def home(request):

    return render(request, 'index.html')


# Register
def register_view(request):

    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Account Created Successfully'
            )

            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


# Login
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                'Login Successful'
            )

            return redirect('dashboard')

        else:

            messages.error(
                request,
                'Invalid Username or Password'
            )

    return render(request, 'login.html')


# Logout
def logout_view(request):

    logout(request)

    messages.success(
        request,
        'Logout Successful'
    )

    return redirect('login')


# Dashboard
@login_required
def dashboard(request):

    # Search Feature
    search = request.GET.get('search')

    transactions = Transaction.objects.filter(
        user=request.user
    )

    if search:

        transactions = transactions.filter(
            title__icontains=search
        )

    transactions = transactions.order_by('-id')

    # Analytics
    income = 0
    expense = 0

    for i in transactions:

        if i.transaction_type == 'Income':

            income += i.amount

        else:

            expense += i.amount

    balance = income - expense

    context = {

        'transactions': transactions,

        'income': income,

        'expense': expense,

        'balance': balance,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


# Add Transaction
@login_required
def add_transaction(request):

    form = TransactionForm()

    if request.method == 'POST':

        form = TransactionForm(request.POST)

        if form.is_valid():

            transaction = form.save(commit=False)

            transaction.user = request.user

            transaction.save()

            messages.success(
                request,
                'Transaction Added Successfully'
            )

            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(
        request,
        'add_transaction.html',
        context
    )


# Edit Transaction
@login_required
def edit_transaction(request, id):

    transaction = get_object_or_404(
        Transaction,
        id=id,
        user=request.user
    )

    form = TransactionForm(instance=transaction)

    if request.method == 'POST':

        form = TransactionForm(
            request.POST,
            instance=transaction
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Transaction Updated Successfully'
            )

            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(
        request,
        'add_transaction.html',
        context
    )


# Delete Transaction
@login_required
def delete_transaction(request, id):

    transaction = get_object_or_404(
        Transaction,
        id=id,
        user=request.user
    )

    transaction.delete()

    messages.success(
        request,
        'Transaction Deleted Successfully'
    )

    return redirect('dashboard')