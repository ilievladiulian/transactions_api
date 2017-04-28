# transactions_api
Dockerized web server for transactions - project with Python (Django) and MongoDB for storage


## Setting up
1. Clone the repository on your local machine.
2. Install Docker for Windows (https://www.docker.com/community-edition).
3. Run run.sh. The server will run on localhost:5000.

## How to use it?
1. GET on localhost:5000/transactions/ with user (integer - user_id), day (date - "yyyy-mm-dd"), threshold (integer) will return as JSON will return the transactions corresponding to the given user, on the given day, with the amount above threshold.
2. POST on localhost:5000/transactions/ with a JSON payload of the form, having sender (integer - sender_id), receiver (integer - receiver_id), timestamp (date - "yyyy-mm-dd"), sum (integer - amount) as parameters will insert in Mongo a transaction.
3. GET on localhost:5000/balance/ with user (integer - user_id), since (date - "yyyy-mm-dd"), until (date - "yyyy-mm-dd") as parameters will return as integer the balance of that user in the given timeframe. At the beginning of the timeframe, the user has the balance 0.
