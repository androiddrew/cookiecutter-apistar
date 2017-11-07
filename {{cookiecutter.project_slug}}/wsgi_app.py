from {{cookiecutter.project_slug}} import application_factory

# Override base application settings here
settings = {}

app = application_factory(settings)

if __name__ == "__main__":
    app.main()