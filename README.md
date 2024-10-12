# Friday Backend
backend that exposes Open Interpreter running on Mac to an API that the [Friday app](https://github.com/Tina-Mai/friday) sends requests to

## Setup
Note: Open Interpreter doesn't install on Python 3.13 for some reason so need to set venv to be Python 3.12
```
python3.12 -m venv venv_3.12
source venv_3.12/bin/activate
pip install flask open-interpreter
```

## Run server
```
python interpreter_server.py
```
