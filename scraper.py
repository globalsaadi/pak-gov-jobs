import requests
from bs4 import BeautifulSoup
import datetime

def get_real_jobs():
    # Multiple reliable sources for Pakistani Govt Jobs
    urls = [
        "https://www.paperpk.com/government-jobs-in-pakistan/",
        "https://deals.pk/jobs/government-jobs/"
    ]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    all_jobs = []
    
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # H2 aur H3 tags mein aksar jobs ke title hotay hain
            for tag in soup.find_all(['h2', 'h3']):
                title = tag.get_text().strip()
                # Filter: Sirf wo titles jin mein Jobs/Govt/2026 ho
                if any(word in title for word in ["Job", "2026", "Police", "Army", "FPSC", "PPSC", "Officer"]):
                    if len(title) > 25:
                        all_jobs.append({"title": title, "date": "Latest Announcement"})
        except:
            continue
            
    # Duplicate mitao
    unique_jobs = {j['title']: j for j in all_jobs}.values()
    return list(unique_jobs)

def generate_html(jobs):
    job_html = ""
    if not jobs:
        job_html = "<p style='color:red;'>Checking official portals for new ads... Please refresh in 5 mins.</p>"
    else:
        for job in jobs[:15]: # Top 15 real jobs
            job_html += f'''
            <div style="background:white; margin:15px auto; padding:20px; max-width:600px; border-radius:10px; box-shadow:0 4px 6px rgba(0,0,0,0.1); border-left:8px solid #006837; text-align:left;">
                <h3 style="margin:0; font-size:1.1em; color:#1a1a1a;">{job["title"]}</h3>
                <p style="color:#27ae60; font-weight:bold; margin-top:10px;">🇵🇰 Government of Pakistan</p>
                <span style="font-size:0.8em; color:#7f8c8d;">Status: {job["date"]}</span>
            </div>
            '''
    
    html_template = f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Real Govt Jobs Bot</title>
    </head>
    <body style="font-family:sans-serif; background:#f4f7f6; margin:0; padding:0; text-align:center;">
        <div style="background:#006837; color:white; padding:40px 20px;">
            <h1 style="margin:0;">Real-Time Govt Jobs Portal</h1>
            <p>Scanning Official Sources...</p>
            <p style="font-size:0.8em;">Last Scan: {datetime.datetime.now().strftime('%I:%M %p')}</p>
        </div>
        <div style="padding:20px;">{job_html}</div>
    </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_template)

if __name__ == "__main__":
    generate_html(get_real_jobs())
