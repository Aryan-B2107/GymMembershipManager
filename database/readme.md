Right now we are going to dump the entire google sheet database
inside the mysql database.

But that is inefficient, since when we call google sheets api 
every 1 min, we have a lot of wasted calls

So eventual correct implementation flow with app script: 

1)User submits Google Form → entry appears in the Google Sheet.

2)Google Apps Script detects new submission.

3)Script sends an HTTP POST request to your Flask/Django/FastAPI backend
(/new_form_entry) with the form data.

4)Your backend receives the data and inserts it directly into MySQL