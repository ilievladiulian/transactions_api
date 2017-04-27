# Create your views here.
from django.http import HttpResponse
from transactions.models import Transaction
from django.db.models import Q

def index_balance(request):
	userTransactionsTo = Transaction.objects.filter(Q(receiver=request.GET['user']), Q(timestamp__gte=request.GET['since']), Q(timestamp__lte=request.GET['until']))
	userTransactionsFrom = Transaction.objects.filter(Q(sender=request.GET['user']), Q(timestamp__gte=request.GET['since']), Q(timestamp__lte=request.GET['until']))
	balance = 0
	for tran in userTransactionsFrom:
		balance = balance - tran.amount
	for tran in userTransactionsTo:
		balance = balance + tran.amount
	return HttpResponse(balance)