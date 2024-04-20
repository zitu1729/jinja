import jinja2

# object for Environment class
env = jinja2.Environment()

# to set the templates 
# {{name}} is variable which is replaced with user data
template = env.from_string("Hello {{name}} !")

# render the values for all variables in template 
output = template.render(name="world")

# final output
print(output)

