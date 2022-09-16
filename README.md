# python-opengl-framework

This is an implementation of an **OpenGL Graphics Framework with Python** for educational purposes. For the implementation 
we only need this four libraries:

 - [PyGame](https://www.pygame.org)
 - [PyOpenGL](http://pyopengl.sourceforge.net)
 - [PyOpenGL-accelerate](https://pypi.org/project/PyOpenGL-accelerate/)
 - [Numpy](https://numpy.org)

All the modules and script are conformed to [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide by using
 - [flake8](https://flake8.pycqa.org/en/latest/)
 - [Mypy](http://mypy-lang.org/)
 - [isort](https://pycqa.github.io/isort/)

### Index
 - [sandbox](https://github.com/newpaxonian/python-opengl-framework/tree/main/sandbox): This folder contains the test scripts that are implemented in the book to learn and test the framework.
 - [exercises](https://github.com/newpaxonian/python-opengl-framework/tree/main/exercises): This folder contains exercises proposed for each chapter.
 - [core](https://github.com/newpaxonian/python-opengl-framework/tree/main/core): This folder contains the core of the framework.
 - [License](https://github.com/newpaxonian/python-opengl-framework/blob/main/LICENSE) GNU General Public License v3.0

## Notes:
 - The code is based in the book: * [Developing Graphics Frameworks with Python and OpenGL](https://library.oapen.org/handle/20.500.12657/48838).
by *Lee Stemkoski* and *Michael Pascale*.
 - Project's structure is based on the one proposed in the book, 
but with emphasis in applying *pythonic 🐍 style*, code coverage and, and usability
 - The code is not fully tested. Please report any issue you find.
 - Some classes and functions has been modified to improve performance and/or usability.
 - Repo's history has comments with references to the book's pages
 - The main class ```Base``` and file ```base.py``` has been refactored to ```Game``` and ```game.py``` (it's more intuitive this way)
 - The file ```openGLUtils.py``` has been refactored to ```opengl_utils.py```
 - Functions and variables in the book are refactored from ```camelCase``` to ```snake_case```

## Requirements for the project
 - flake8==5.0.4
 - isort==5.10.1
 - mccabe==0.7.0
 - mypy==0.971
 - mypy-extensions==0.4.3
 - numpy==1.23.3
 - pycodestyle==2.9.1
 - pyflakes==2.5.0
 - pygame==2.1.2
 - PyOpenGL==3.1.6
 - PyOpenGL-accelerate==3.1.6
 - tomli==2.0.1
 - typing_extensions==4.3.0

## My system
 - Windows 11 / Ubuntu 20.04
 - Python 3.10.4
 - PyCharm 2021.3.2 (Community Edition)
 - Renderer: GeForce GTX 1070 with Max-Q Design/PCIe/SSE2
 - OpenGL version: 4.6.0 NVIDIA 457.63
 - GLSL version: 4.60 NVIDIA



### TODO:
 - Add some screenshots
 - Add TOX
 - Add Black
 - Add config for flake8
 - Add config for isort
 - Add config for mypy
 - Add unittests
 - Add setup.py
