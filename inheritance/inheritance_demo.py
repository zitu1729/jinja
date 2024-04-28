from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader("templates"))

template = env.get_template("child.html")

out = template.render(title="This is an illustration for jinja in heritancec", body="This is the body content")

print(out)