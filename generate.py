import os
import csv
import json

STATUS = ['idea', 'in_progress', 'almost_done', 'done']

def load_projects():
    projects = {}
    with open("projects.csv", "r") as infile:  
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        # TITLE, DESCRIPTION, STATUS, CATEGORIES, LINK

        for row in reader:
            title = row[0].strip()
            description = row[1].strip()
            status = row[2].strip()
            category = row[3].split('-')
            link = row[4].strip()

            if status not in projects:
                projects[status] = []
            projects[status].append({"title": title, 
                "description": description, 
                "category":[s.strip() for s in category], 
                "link":link })

    return projects



def run(projects):
   
    with open('projects.js', 'w') as outfile:
        outfile.write("var projects ={0}".format(json.dumps(projects, indent=4)))


if __name__ == "__main__":
    projects = load_projects()
    run(projects)



