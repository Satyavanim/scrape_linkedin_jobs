#### web scraping Linkedin jobs using python ####

import requests
from bs4 import BeautifulSoup
import re
import csv

# Define the URL of the job search page you want to scrape
url = "https://www.linkedin.com/jobs/search/?currentJobId=3420519582&distance=25&geoId=105556991&keywords=python%20developer"

# Send a GET request to the URL and store the response in a variable
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")
print(soup)
# Find all job listings on the page
job_listings = soup.find_all('div', class_="base-search-card__info")
print(job_listings)
rows=[]
# Loop through each job listing and extract the job title and salary (if available)
for jobs in range(len(job_listings)):
    job_titles = job_listings[jobs].find('h3', class_="base-search-card__title").text.strip()
    Company = job_listings[jobs].find('h4', class_="base-search-card__subtitle").text.strip()
    Company_link = job_listings[jobs].find('a', attrs={'class':"hidden-nested-link"})
    if Company_link:
        if Company_link['href']:
            link=Company_link['href']
        else:
            link = "Not specified"
    #print(link)
    salaries = job_listings[jobs].find('span', class_='job-search-card__salary-info')
    if salaries:
        Salary = salaries.text.strip()
        Salary_text=(str(Salary))
        salary_info = re.sub('[₹]', '',Salary_text)
        salary=re.sub('[\s]','',salary_info)
    else:
        salary = "Not specified"
    #print(salary)
    Location = job_listings[jobs].find('span' ,class_="job-search-card__location").text.strip()    
    p=([job_titles,Company,salary,Location,link])
    rows.append(p)
    #print(f"Job Title: {job_titles}")
    #print(f"Company Name: {Company}")
    #print(f"Job Location: {Location}")
    #print(f"Salary: {salary}")
    #print(f"Company_Link: {link}")
    #print('---')
#print(rows)
fields = ['Job_Title','Company','Salary','Job_Location','Company_link']
with open(r"C:\Users\username\Desktop\jobsdata.csv",'w',encoding='UTF8',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(fields)
    writer.writerows(rows)
    file.close()
    print("successfully save into csv file")
   
##instagram ##


