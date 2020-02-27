# https://codewithmosh.com/courses/417695/lectures/8417575

# HTML is used to create the email template

from string import Template

template = Template(Path("template.html").read_text())
template.substitute({"name": "John"})
