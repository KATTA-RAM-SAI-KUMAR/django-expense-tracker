from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense

def home(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        Expense.objects.create(amount=amount, category=category)
        return redirect("/")

    expenses = Expense.objects.all()
    total = sum(e.amount for e in expenses)

    return render(request, "home.html", {
        "expenses": expenses,
        "total": total
    })


def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect("/")
