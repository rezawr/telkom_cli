
# assessment by Telkom Indonesia

Reza Wahyu Ramadhan
[![Built with Python](https://img.shields.io/badge/built%20with-python-ff69b4.svg?logo=cookiecutter)](https://github.com/karec/cookiecutter-flask-restful)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Installation

Install my project with your pip with the code below (all the example is using linux, for windows and mac could be search on how install python package)

```bash
  virtualenv yourvirtualenv
  source yourvirtualenv/bin/activate
  pip install git+ssh://git@github.com/rezawr/telkom_cli.git#egg=telkom_cli
```

After package installed, you could use command *telkom_cli*. For further information, use *telkom_cli -h* to get what arguments is needed and what arguments is optional arguments


## Basic Usage

Usage on this command is using code below:

```bash
  telkom_cli /your/error/log
```

The command will generate error log to txt file. 

For the json format, it will be issue, because I don't know the spesified error log, so I am using this format for the error log

[Format](https://drive.google.com/file/d/1q0h36UKFrcvHWGfPChm0M8tKqXOL5V6M/view?usp=sharing)

