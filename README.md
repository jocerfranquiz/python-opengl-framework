# python-opengl-framework

This is an implementation of an **OpenGL Graphics Framework** using

 - [PyGame](https://www.pygame.org)
 - [PyOpenGL](http://pyopengl.sourceforge.net)
 - [PyOpenGL-accelerate](https://pypi.org/project/PyOpenGL-accelerate/)
 - [Numpy](https://numpy.org)

The code is based in the book:
* [Developing Graphics Frameworks with Python and OpenGL](https://library.oapen.org/handle/20.500.12657/48838).
by *Lee Stemkoski* and *Michael Pascale*.

## Notes:
 - Project's structure is based on the one proposed in the book, 
but with emphasis in applying pythonic style, unittest, code coverage, and usability
 - The code is not fully tested, so it may contain bugs.
 - Some classes and functions has been modified to improve performance and/or usability.
 - Repo's history has comments with references to the book's pages
 - The main class ```Base``` and file ```base.py``` had been refactored to ```Game``` and ```game.py``` (it's more intuitive this way)

### TODO:
 - ✅ Add iSort
 - ✅ Add Flake8
 - ✅ Add MyPy
 - Add TOX
 - Add Black
 - Add config for flake8
 - Add config for isort
 - Add config for mypy
 - Add unittests
 - Add setup.py