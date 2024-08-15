Pre-requisites for installation: Python, Sqlite3

Steps for setup:

-> run "python -m venv .venv" to start virual environment(Recommended)
-> run "pip install -r requirements.txt" or simply run "pip install requests"

Running scripts:

-> run "python input.py" to create the db and fill it with linkedin urls"
-> run "python output.py" to take the linekdin urls and enrich data and inserting it into a new table

Check output:

-> run "sqlite3 company_data.db" to run database at terminal
-> run "SELECT \* FROM enriched_company_data LIMIT 3" to view the first 3 entries.
**You can change the limit but since the data is too big, limit is recommended**
