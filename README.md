# python-refresh

[Python 3.8.2](https://www.python.org/downloads/) (the language, not [Django](https://github.com/Thoughtscript/python_django_refresh)) refresh and review notes.

## Contents

A few examples covering:

1. dicts
1. OOD
1. some destructuring
1. dependency injection
1. lambda functions

## Use

To install dependencies into a [Python 3.8.2](https://www.python.org/downloads/) **virtual environmen** (venv):

```bash
    $ python3 -m pip install --upgrade pip
    $ python3 -m venv ENV_QUANTUM
    $ source ENV_QUANTUM/Scripts/activate
```

Then, after activating the selected environment:

```bash
   $ python3 -m pip install -r requirements.txt
```

Verify versions using:

```bash
    $ pip freeze
```

Clear environment PIP dependencies:

```bash
    $ pip uninstall -y -r <(pip freeze)
```

## Comments

Great resources:

1. https://realpython.com/inheritance-composition-python/
1. https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/
1. https://blog.tecladocode.com/destructuring-in-python/
1. https://qiskit.org/

> Updated a [Qiskit](https://qiskit.org/) example that's nearly 2 years out of date and close to 9 versions behind! (Tried to find an older version but it's severely deprecated with missing dependencies.) Library has been divided into new sub-libraries.
