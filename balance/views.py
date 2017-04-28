# Create your views here.
from django.http import HttpResponse
from transactions.models import Transaction
from django.db.models import Q

import logging

logger = logging.getLogger('django')

def balance(request):
	user = request.GET['user']
	since = request.GET['since']
	until = request.GET['until']

	if user is not None and since is not None and until is not None:

		transactionsToUser = Transaction.objects.filter(
			Q(receiver=user), 
			Q(timestamp__gte=since), 
			Q(timestamp__lte=until)
		)
		transactionsFromUser = Transaction.objects.filter(
			Q(sender=user), 
			Q(timestamp__gte=since), 
			Q(timestamp__lte=until)
		)

		balance = 0
		for tran in transactionsFromUser:
			balance = balance - tran.amount
		for tran in transactionsToUser:
			balance = balance + tran.amount
		logger.debug('balance: %d' % balance)
		return HttpResponse(balance)

	else:
		return HttpResponse('You must provide query parameters [user, since, until]...', status=400)