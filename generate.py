import os
import csv
import json

STATUS = ['idea', 'in_progress', 'almost_done', 'done']

def load_projects():
    projects = {}
    with open("projects.csv", "r") as infile:  
        reader = csv.reader(infile, quotechar='"', delimiter=',',
                     quoting=csv.QUOTE_ALL, skipinitialspace=True)
        next(reader, None)  # skip the headers
        # TITLE, DESCRIPTION, STATUS, CATEGORIES, LINK

        for row in reader:
            if len(row) > 6:
                title = row[0].strip()
                description = row[1].strip()
                size = row[2].strip()
                status = row[3].strip()
                category = row[4].split('-')
                link = row[5].strip()
                techno_raw = row[6].strip().split('-')
                techno = []
                for each in techno_raw:
                    tmp = each.strip()
                    if tmp:
                        techno.append(tmp)

                if status not in projects:
                    projects[status] = []

                projects[status].append({"title": title, 
                    "description": description, 
                    "size": size.upper(),
                    "category":[s.strip() for s in category], 
                    "link":link,
                    "techno":[s.strip() for s in techno]
                    })

    return projects



def run(projects):
   
    with open('projects.js', 'w') as outfile:
        outfile.write("var projects ={0}".format(json.dumps(projects, indent=4)))


if __name__ == "__main__":
    projects = load_projects()
    run(projects)



