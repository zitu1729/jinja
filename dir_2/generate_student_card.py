from jinja2 import Environment, FileSystemLoader
import json

# json path
json_path = "data.json"

# open the file in 'r' read mode and load the json data
with open(json_path,'r') as file:
    data = json.load(file)

# give the template dir path and set the environment
env = Environment(loader = FileSystemLoader("templates"))

# get template
template = env.get_template("temp.j2")

# set the json data
MAX_SCORE = data['MAX_SCORE']
TEST_NAME = data['TEST_NAME']
VALUES = data['students']

print("cards generated:")
for student in VALUES:
    name = student["name"]
    file_name = f"reports/{name.lower()}_report.txt"

    #render the input data
    file_content = template.render(student, max_score = MAX_SCORE, test_name = TEST_NAME)

    # writing the content to a file
    with open(file_name, mode="w", encoding="utf-8") as out:
        out.write(file_content)
        print(file_name)

print("all reports generated successfully !")
