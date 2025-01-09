def index():
    with open('templates/index.html') as template:
        return template.read()


def blog():
    with open('templates/blog.html') as template:
        return template.read()


def text():
    with open('templates/text.html') as template:
        return template.read()

