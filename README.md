# README

This is an example of two Azure Functions, based on HTTP Triggers that depend on some common shared code.  It is structured so that you can run test pytests, via the terminal or via VS-Code.

Download repo, and create a Python virtualenv in the root directory.
Update pip and pip-tools.

See the tree outline below.

```
C:\Users\rnwol\workspace\multifunclayout
├── .git
|  ├── config
|  ├── description
|  ├── HEAD
|  ├── hooks
|  |  ├── applypatch-msg.sample
|  |  ├── commit-msg.sample
|  |  ├── fsmonitor-watchman.sample
|  |  ├── post-update.sample
|  |  ├── pre-applypatch.sample
|  |  ├── pre-commit.sample
|  |  ├── pre-merge-commit.sample
|  |  ├── pre-push.sample
|  |  ├── pre-rebase.sample
|  |  ├── pre-receive.sample
|  |  ├── prepare-commit-msg.sample
|  |  └── update.sample
|  ├── info
|  |  └── exclude
|  ├── objects
|  |  ├── info
|  |  └── pack
|  └── refs
|     ├── heads
|     └── tags
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
├── LICENSE.md
├── pytest.ini
├── README.md
├── tests
|  ├── testHttpTrigger1.http
|  ├── testHttpTrigger2.http
|  ├── test_HttpTrigger1.py
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
   ├── dev-requirements.in
   ├── dev-requirements.txt
   ├── host.json
   ├── HttpTrigger1
   |  ├── function.json
   |  └── __init__.py
   ├── HttpTrigger2
   |  ├── function.json
   |  └── __init__.py
   ├── local.settings.json
   ├── requirements.txt
   ├── sharedcode
   |  ├── my_helper_function.py
   |  ├── __init__.py
   |  └── __pycache__
   └── __init__.py
```
