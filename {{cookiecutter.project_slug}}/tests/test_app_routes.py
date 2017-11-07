from {{cookiecutter.project_slug}}.app import welcome

def test_welcome_route():
    message = {"message": "welcome to {{cookiecutter.project_slug}}"}
    assert message == welcome()