# cookiecutter-apistar

An API Star template for [cookiecutter](https://github.com/audreyr/cookiecutter) with a preference for a postgres backend

## Usage

```
$ pip install cookiecutter
$ cookiecutter https://github.com/androiddrew/cookiecutter-apistar
```
You will be asked for some basic information regarding your project (name, project name, etc.). This info will be used in your new project

#### Create virtual env
```
$ cd <app_dir>
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements
```
#### Run tests
```
$ pytest -v
```
OR
```
$ python wsgi_app.py test
```

#### Run dev server
```
$ python wsgi_app.py run
```

## License

MIT Licensed.

## Changelog

### 0.1.0 (12/08/2017)
- Public release
- Corrected Test database connection string in conftest

### 0.0.1 (11/07/2017)
- Initial release