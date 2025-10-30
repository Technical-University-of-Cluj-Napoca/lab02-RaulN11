import requests
from bs4 import BeautifulSoup
import sys

def find_jobs():
    page = 1
    scraped = True
    jobs_found = []
    while scraped:
        l = len(jobs_found)
        url = "https://www.juniors.ro/jobs?page=" + str(page)
        response = requests.get(url)
        if response.status_code != 200:
            print("Error")
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all("li", class_="job")
        for result in results:
            techs = []
            tl = result.find_all("ul", class_="job_tags")
            for t in tl:
                for a in t.find_all("a"):
                    techs.append(a.text)
            ld = result.find("div", class_="job_header_title").find("strong").text
            words = [w.strip() for w in ld.split("|")]

            if words[0].lower() == "remote" and len(words) >= 3:
                loc = words[1]
                date = words[2]
            else:
                loc = words[0]
                date = words[1] if len(words) > 1 else None

            job = {
                "Job Title": result.find("div", class_="job_header_title").find("h3").text.strip(),
                "Company Name": result.find("ul", class_="job_requirements").find("li").text.split(":")[1].strip(),
                "Location": loc,
                "Technologies": techs,
                "Post Date": date
            }
            jobs_found.append(job)

        r = len(jobs_found)
        if l == r:
            scraped = False
        page += 1

    return jobs_found


def filterJobsLocation(location: str) -> list:
    jobs_found = find_jobs()
    matched_jobs = []
    location = location.lower().strip()
    for job in jobs_found:
        if location in job["Location"].lower():
            matched_jobs.append(job)
    return matched_jobs

def filterJobsTech(tech: str) -> list:
    jobs_found = find_jobs()
    matched_jobs = []
    tech = tech.strip()
    for job in jobs_found:
        if tech in job["Technologies"]:
            matched_jobs.append(job)
    return matched_jobs

if __name__ == "__main__":
    jobs_found = filterJobsLocation("Cluj-Napoca")
    jobs_found1 = filterJobsTech("JS")
    for job in jobs_found:
        print(job)
    print("\nTech filter here:\n")
    for job in jobs_found1:
        print(job)
