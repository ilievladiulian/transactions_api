from django.http import HttpResponse
from transactions.models import Transaction
from django_mongodb_engine.contrib import MongoDBManager
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

import datetime
import json
import logging

logger = logging.getLogger('django')


@csrf_exempt
def index(request):
	if request.method == 'GET':
		return get_transactions_list(request)
	else:
		return create_transaction(request)

def get_transactions_list(request):
	user = request.GET['user']
	threshold = request.GET['threshold']
	day = request.GET['day']

	if user is not None and day is not None and threshold is not None:

		transactionsOnDay = Transaction.objects.filter(
			Q(amount__gte=threshold),
			Q(sender=user) | Q(receiver=user),
			Q(timestamp=day)
		).values()
		data = []
		for tran in transactionsOnDay:
			tran['timestamp'] = tran['timestamp'].strftime('%Y-%m-%d')
			data.append(tran)
		logger.debug('transaction list: %s' % str(data))
		return HttpResponse(json.dumps(data), content_type="application/json")

	else:
		return HttpResponse('You must provide query parameters [user, day, threshold]...', status=400)


def create_transaction(request):
	data = json.loads(request.body)
	sender = data['sender']
	receiver = data['receiver']
	timestamp = datetime.datetime.fromtimestamp(int(data['timestamp'])).strftime('%Y-%m-%d')
	amount = data['sum']

	if sender is not None and receiver is not None and amount is not None:

		transaction = Transaction.objects.create(
	       	sender = sender,
	    	receiver = receiver,
	    	amount = amount,
	    	timestamp = timestamp
	    )
		transaction.save()
		return HttpResponse(json.dumps(data), content_type="application/json")

	else:
		return HttpResponse('You must provide parameters [sender, receiver, sum] to create a transaction...', status=400)
