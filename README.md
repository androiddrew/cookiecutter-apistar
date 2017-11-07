# cookiecutter-apistar

An API Star template for [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage

```python
$ pip install cookiecutter
$ cookiecutter https://git.androiddrew.com/androiddrew/cookiecutter-apistar.git
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

### 0.0.1 (11/07/2017)
- Initial release