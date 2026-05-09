import requests
from bs4 import BeautifulSoup
import datetime

def get_govt_jobs():
    # Pakistan ki official jobs portal
    url = "https://njp.gov.pk/jobs"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Ye line website se jobs dhoondti hai
        job_listings = soup.find_all('div', class_='job-item') # NJP ka structure
        
        jobs = []
        # Agar website se data mil jaye to 5 bari jobs uthao
        for item in job_listings[:5]:
            title = item.find('h4').text.strip()
            dept = item.find('p').text.strip()
            jobs.append({"title": title, "dept": dept, "date": str(datetime.date.today())})
            
        # Agar website down ho ya data na miley to ye backup jobs dikhaye ga
        if not jobs:
            jobs = [
                {"title": "Latest Federal Jobs", "dept": "NJP Portal", "date": "Check Website"},
                {"title": "Provincial Vacancies", "dept": "Official Dept", "date": "Daily Update"}
            ]
        return jobs
    except:
        return [{"title": "System Updating...", "dept": "Please check back in 1 hour", "date": "-"}]

def generate_html(jobs):
    job_html = ""
    for job in jobs:
        job_html += f'''
        <div class="job-card">
            <h3>{job["title"]}</h3>
            <p><strong>Department:</strong> {job["dept"]}</p>
            <p class="date">Announced: {job["date"]}</p>
            <a href="https://njp.gov.pk/" target="_blank" style="display:inline-block; margin-top:10px; padding:8px 15px; background:#27ae60; color:white; text-decoration:none; border-radius:5px;">Click to Apply</a>
        </div>
        '''
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sarkari Jobs Bot - Pakistan</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color: #f4f7f6; margin: 0; padding: 20px; }}
            .job-card {{ background: white; margin: 15px auto; padding: 20px; width: 90%; max-width: 600px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 6px solid #006837; text-align: left; }}
            .header-box {{ background: #006837; color: white; padding: 30px; border-radius: 12px; margin-bottom: 30px; }}
            h1 {{ margin: 0; font-size: 1.8em; }}
            .date {{ color: #27ae60; font-weight: bold; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <div class="header-box">
            <h1>🇵🇰 Government Jobs Bot</h1>
            <p>Direct from Official Government Portals</p>
            <p>Last Update: {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')}</p>
        </div>
        <div id="jobs-container">{job_html}</div>
    </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_template)

if __name__ == "__main__":
    jobs_list = get_govt_jobs()
    generate_html(jobs_list)
