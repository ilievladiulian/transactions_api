from django.http import HttpResponse
from transactions.models import Transaction
from django_mongodb_engine.contrib import MongoDBManager
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

@csrf_exempt
def index(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		transaction = Transaction.objects.create(
	       	sender = data['sender'],
	    	receiver = data['receiver'],
	    	amount = data['sum'],
	    	timestamp = datetime.datetime.fromtimestamp(int(data['timestamp'])).strftime('%Y-%m-%d')
	    )
		transaction.save()
		return HttpResponse(transaction.timestamp)
	elif request.method == 'GET':
		transactionsDay = Transaction.objects.filter(Q(amount__gte=request.GET['threshold']), Q(sender=request.GET['user']) | Q(receiver=request.GET['user']), Q(timestamp=request.GET['day'])).values()
		data = []
		for tran in transactionsDay:
			tran['timestamp'] = tran['timestamp'].strftime('%Y-%m-%d')
			data.append(tran)
		return HttpResponse(json.dumps(data), content_type="application/json")
