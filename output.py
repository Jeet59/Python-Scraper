import sqlite3
import requests

conn = sqlite3.connect('company_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS enriched_company_data (
        company_id INTEGER PRIMARY KEY,
        company_name TEXT,
        website_url TEXT,
        universal_name TEXT,
        description TEXT,
        follower_count INTEGER
    )
''')

cursor.execute('SELECT company_id, company_linkedin_url FROM company_urls')
companies = cursor.fetchall()

urls = [company[1] for company in companies]

api_url = "https://linkedin-bulk-data-scraper.p.rapidapi.com/companies"
headers = {
    "X-RapidAPI-Key": "2cd22ddfeamsh764d78e3612803dp170054jsn79c12f25646b",
    "X-RapidAPI-Host": "linkedin-bulk-data-scraper.p.rapidapi.com",
    "Content-Type": "application/json"
}

payload = {"links": urls}
response = requests.post(api_url, headers=headers, json=payload)
response = response.json()
response = response.get('data')
for item in response:
    error = item.get('error')
    if not error:
        item = item.get('data')
        company_id = item.get('companyId')
        company_name = item.get('companyName')
        website_url = item.get('websiteUrl')
        universal_name = item.get('universalName')
        description = item.get('description')
        follower_count = item.get('followerCount')
        data = {
            'company_id': company_id,
            'company_name': company_name,
            'website_url': website_url,
            'universal_name': universal_name,
            'description': description,
            'follower_count': follower_count
        }
        sql = '''
            INSERT INTO enriched_company_data (company_id, company_name, website_url, universal_name, description, follower_count)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        values = (
            data['company_id'],
            data['company_name'],
            data['website_url'],
            data['universal_name'],
            data['description'],
            data['follower_count']
        )
        cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()
