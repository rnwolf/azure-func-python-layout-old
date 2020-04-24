# README

I had some difficulty in getting the default Azure Functions working beyond the most trival case, as at April 2020.  

This repo is my best attempt at creating an example of two Azure Functions, based on HTTP Triggers that depend on some common shared code, with some automated pytests.

The layout is based on the Azure func templates and [feedback](https://github.com/microsoft/vscode-azurefunctions/issues/1970) by a [Brett Cannon](https://github.com/brettcannon) and [Anthony Chu](https://github.com/anthonychu).

I wanted to ensure that everything works via the terminal command line and/or via the VS-Code GUI.

You should be able to download a zip of the repo, rename it, create a Python virtualenv in the root directory, update pip & install pip-tools, activate venv and then be ready to proceed on your own.

There is a github workflow that will run some quality checks and deploy to Azure.
You will need you to create/download a "publish profile" which must be added as Github repo secret in order for the workflow to deploy to Azure.

The Update the dev-requirements.in and requirements.txt file with the python packages that you need/want in dev and production.
Activate virtualenv and then generate ```pip-compile -r dev-requirements.in```  
Install packages with ```pip install -r dev-requirements.txt```

See the tree view of the essental files is outlined below.

```
C:\Users\rnwol\workspace\multifunclayout
├── .coverage
├── .coveragerc
├── .flake8
├── .git
├── .github
|  └── workflows
|     └── main.yml
├── .gitignore
├── .venv
|  ├── Include
|  ├── Lib
|  |  └── site-packages
|  ├── pyvenv.cfg
|  └── Scripts
|     ├── activate
|     ├── activate.bat
|     ├── Activate.ps1
|     ├── black.exe
|     ├── blackd.exe
|     ├── deactivate.bat
|     ├── easy_install-3.7.exe
|     ├── easy_install.exe
|     ├── pip-compile.exe
|     ├── pip-sync.exe
|     ├── pip.exe
|     ├── pip3.7.exe
|     ├── pip3.exe
|     ├── py.test.exe
|     ├── pytest.exe
|     ├── python.exe
|     └── pythonw.exe
├── .vscode
|  ├── extensions.json
|  ├── launch.json
|  ├── settings.json
|  └── tasks.json
├── Create .venv pythonvirtual env here.txt
├── dev-requirements.in
├── dev-requirements.txt
├── LICENSE.md
├── mypy.ini
├── pytest.ini
├── README.md
├── tests
|  ├── testHttpTrigger1.http
|  ├── testHttpTrigger2.http
|  ├── test_HttpTrigger1.py
|  ├── test_HttpTrigger2.py
|  └── __init__.py
└── __app__
   ├── .funcignore
   ├── .python_packages
   ├── .vscode
   |  ├── extensions.json
   |  ├── launch.json
   |  ├── settings.json
   |  └── tasks.json
   ├── conftest.py
   ├── host.json
   ├── HttpTrigger1
   |  ├── function.json
   |  └── __init__.py
   ├── HttpTrigger2
   |  ├── function.json
   |  └── __init__.py
   ├── local.settings.json
   ├── local.settings.SAMPLE.json
   ├── requirements.txt
   ├── sharedcode
   |  ├── my_helper_function.py
   |  └── __init__.py
   └── __init__.py

```
