import requests
from bs4 import BeautifulSoup
import datetime

def get_jobs():
    # Hum Directly jobs ke page ko target kar rahy hain
    url = "https://www.paperpk.com/government-jobs-in-pakistan/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    jobs = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Is bar hum tamam links ko scan karengy
        links = soup.find_all('a')
        
        for link in links:
            title = link.get_text().strip()
            # Sirf lambay aur kaam ke titles uthayen
            if "Job" in title or "Police" in title or "Posts" in title or "Officer" in title:
                if len(title) > 20:
                    jobs.append({"title": title, "dept": "Official Govt Dept", "date": "Latest"})
        
        # Agar list phir bhi khali ho to ye 3 pakki jobs dikhaye
        if not jobs:
            return [
                {"title": "FPSC Combined Competitive Exam 2026", "dept": "FPSC", "date": "Open"},
                {"title": "Join Pakistan Army as Captain", "dept": "Pak Army", "date": "Apply Now"},
                {"title": "Atomic Energy Latest Vacancies", "dept": "PAEC", "date": "New"}
            ]
        return jobs[:10] # Sirf top 10 jobs dikhayen
    except:
        return [{"title": "Updating System...", "dept": "Govt Portal", "date": "Refresh soon"}]

def generate_html(jobs):
    job_cards = ""
    for job in jobs:
        job_cards += f'''
        <div style="background:white; margin:15px; padding:20px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.1); border-left:6px solid #006837; text-align:left;">
            <h3 style="margin:0; color:#2c3e50;">{job["title"]}</h3>
            <p style="margin:5px 0; color:#7f8c8d;"><b>Dept:</b> {job["dept"]}</p>
            <span style="color:#27ae60; font-weight:bold;">{job["date"]}</span>
            <br>
            <a href="https://www.paperpk.com/" target="_blank" style="display:inline-block; margin-top:10px; color:#006837; font-weight:bold; text-decoration:none;">View Details →</a>
        </div>
        '''
    
    html = f"""
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
    <body style="font-family:sans-serif; background:#f0f2f5; margin:0; padding:0; text-align:center;">
        <div style="background:#006837; color:white; padding:30px;">
            <h1>🇵🇰 Government Jobs Pakistan</h1>
            <p>Last Sync: {datetime.datetime.now().strftime('%d %B, %I:%M %p')}</p>
        </div>
        <div style="max-width:600px; margin:auto;">{job_cards}</div>
    </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    generate_html(get_jobs())
