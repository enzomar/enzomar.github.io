import os
from jinja2 import Environment, FileSystemLoader
import csv
from datetime import datetime

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

def load_projects():
    projects = {}
    with open("projects.csv", "r") as infile:  
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        # TITLE, DESCRIPTION, STATUS, CATEGORIES, LINK

        for row in reader:
            # process each row
            title = row[0].strip()
            description = row[1].strip()
            status = row[2].strip()
            category = row[3].split('-')
            link = row[4].strip()

            if status not in projects:
                projects[status] = []
            projects[status].append({"title": title, 
                "description": description, 
                "category":category, 
                "link":link })

    projects['date'] = datetime.now().isoformat("#")

    return projects



def run(template_name, projects):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(current_directory))
    template = env.get_template(template_name)

    html = template.render(projects)

    with open('index.html', 'w') as outfile:
        outfile.write(html)



if __name__ == "__main__":
    projects = load_projects()
    
    run('template.j2', projects)



