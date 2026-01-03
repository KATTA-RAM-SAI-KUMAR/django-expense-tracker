from django.shortcuts import render, redirect
from .models import Expense

def home(request):

    # Initialize budget in session
    if "budget" not in request.session:
        request.session["budget"] = 0

    if request.method == "POST":

        # Set Budget
        if "set_budget" in request.POST:
            request.session["budget"] = int(request.POST.get("budget", 0))

        # Add Expense
        elif "add_expense" in request.POST:
            amount = request.POST.get("amount")
            category = request.POST.get("category")

            if amount and category:
                Expense.objects.create(
                    amount=int(amount),
                    category=category
                )

        return redirect("/")

    expenses = Expense.objects.all()
    spent = sum(e.amount for e in expenses)
    budget = request.session["budget"]
    remaining = budget - spent

    return render(request, "home.html", {
        "budget": budget,
        "expenses": expenses,
        "spent": spent,
        "remaining": remaining
    })


def delete_expense(request, id):
    Expense.objects.filter(id=id).delete()
    return redirect("/")
