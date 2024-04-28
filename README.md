# Jinja
Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.

To know more, https://jinja.palletsprojects.com/en/3.1.x/

## Installation
    - sudo apt install python3-pip  
    - pip install jinja2-cli
    - jinja2 --version
Note:Restart the pc after installation. Sometimes it doesn't show the command jinja2. 

dir_1 contains the input .yaml files with respect to their jinja templates .j2 files
## To run scripts of dir_1
    - jinja2 template1.j2 input1.yaml  
    - jinja2 template2.j2 input2.yaml  
    - jinja2 template3.j2 input3.yaml  
Make sure that we are giving the correct template with the corresponding input file.

## To run scripts of dir_2
    - python3 tutorial.py
    - python3 generate_student_card.py

## To run scripts of inheritance
    - python3 inheritance_demo.py