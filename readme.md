# Readme

## Json Flask Demonstration
This project was created to serve as a very basic Flask application that will display data on a web page.  The data is retrieved via an API.

The intent here to to show how the data input form, data gathering, and data view are separated.

## Files
- app.py - Flask application
- MyClass.py - very simple Python class to do some functionality, called from app.py
- requirements.txt - pip installs
- data.html - web page with input form to get basic data
- data_view.html - page for viewing the data result

To get the data, a simple GET request is made:
```
http:/xxx.x.x.x/data_get?name=foo&age=21
```

Return will be json in the form of
```
{
    "age": 21,
    "id": random_UUID,
    "name": "foo",
}
```

This API could also be tested with something like Postman.

## It is advised to set up a Python environment to install the required library.

To create the environment:
path to python\python.exe -m venv environment_name

To activate:
- source environment_name/bin/activate (Linux or Mac)
- environment_name/Scripts/activate (Windows)

To deactivate:
- deactivate

Put all the requirements in requirements.txt

To load them from within the env: pip install -r requirements.txt