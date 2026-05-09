import datetime

# Ye function filhal sample jobs dikhaye ga
def get_jobs():
    jobs = [
        {"title": "Inspector Investigation", "dept": "FIA", "date": str(datetime.date.today())},
        {"title": "Assistant Director", "dept": "Ministry of Defence", "date": str(datetime.date.today())},
        {"title": "Data Entry Operator", "dept": "NADRA", "date": str(datetime.date.today())}
    ]
    return jobs

def generate_html(jobs):
    job_html = ""
    for job in jobs:
        job_html += f'<div class="job-card"><h3>{job["title"]}</h3><p>Department: {job["dept"]}</p><p class="date">Announced: {job["date"]}</p></div>'
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sarkari Jobs Bot</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial; text-align: center; background-color: #f0f2f5; margin: 0; padding: 20px; }}
            .job-card {{ background: white; margin: 15px auto; padding: 20px; width: 90%; max-width: 600px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-left: 5px solid #27ae60; text-align: left; }}
            h1 {{ color: #1a5276; }}
            h3 {{ margin: 0 0 10px 0; color: #2c3e50; }}
            p {{ margin: 5px 0; color: #7f8c8d; }}
            .date {{ color: #27ae60; font-weight: bold; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <h1>🇵🇰 Official Govt Jobs Alert</h1>
        <p>Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        <div id="jobs-container">
            {job_html}
        </div>
    </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_template)

if __name__ == "__main__":
    jobs_list = get_jobs()
    generate_html(jobs_list)
    print("Website updated successfully!")
