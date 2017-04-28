After reading the Docker documentation, I decided to implement the web server in Python, using Django, with MongoDB storage. For this, I used Django MongoDB Engine to connect Django to Mongo.

The Django project has 2 apps, "transactions" and "balance".

1. "transactions" app

First, I configured the transactions/urls.py to point to transactions/views.py if the url contains "transactions/". Then, I created the transactions model in transactions/models.py, using the fields sender(integer), receiver(integer), amount(integer) and timestamp(DateField).

In transactions/views.py are 3 views: index, get_transactions_list and create_transaction.

In the index view, if the request method is GET then the get_transactions_list view is returned, otherwise the create_transaction view is returned.

In the get_transactions_list view, if all the GET parameters (user, threshold, day) are set, Mongo is queried for transactions corresponding to a user, with the amount above a threshold in a day, and the results are returned as json. Otherwise, an error 400 is returned.

In the create_transaction view, if all the POST parameters (sender, receiver, timestamp, sum) are set, a new transaction is created and saved in Mongo. If the operation is successful, then a json with the object is returned, otherwise an error 400 occurs.

2. "balance" app

After linking the global urls.py to balance/urls.py, which points to balance/views.py, I implemented the balance view.

Here, if all the GET parameters are set (user, since, until), Mongo is queried for the transactions of the given user in the given timeframe. At the beginning, the balance is 0. The amounts from transactions that have the given user as the receiver are added to the balance, while the ones that have the user as a sender are substracted from the balance. The balance is returned as an integer through a HttpResponse. If the parameters are not set, an error 400 occurs.

To dockerize this Django project, there is a Dockerfile, a docker-compose.yml file and a requirements.txt file inside the project folder. By running the command "docker-compose up" while in the project folder, the server is up and running.

This command is run by run.sh, which starts the server and the Mongo service.