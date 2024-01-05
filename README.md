# pycode


## Instructions 
Install python 3.11.4
```sh
pyenv install 3.11.4
```

Generate the python version file
```sh
pyenv local 3.11.4
```

Create a new virtual environment using the local python version
```sh
pyenv exec python -m venv .venv
```

Activate the virtual environment 
```sh
source .venv/bin/activate
```

Install required dependencies
```sh
pip install -r requirements.txt
```


----

## Formatting
The script in `pyproject.toml` tells the `isort` utility to format imports in a way that is compatible with the `black` code formatter.

```sh
[tool.isort]
profile = "black"
```

Put the following directory and file at the root of your project. `.vscode/settings.json`.

```json
{
    "editor.formatOnSave": true,
    "ruff.organizeImports": false,
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit",
            "source.fixAll": "explicit"
        },
        "editor.defaultFormatter": "ms-python.black-formatter"
    }
}
```