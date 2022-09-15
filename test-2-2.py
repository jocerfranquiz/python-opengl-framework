from OpenGL.GL import (GL_POINTS, glBindVertexArray, glDrawArrays,  # type: ignore
                       glGenVertexArrays, glPointSize, glUseProgram)

from core.game import Game
from core.opengl_utils import OpenGLUtils
from core.settings import SCREEN_SIZE


# render a single point
class Test(Game):

    def __init__(self, screen_size: tuple[int, int] = SCREEN_SIZE):
        super().__init__(screen_size)
        self.program_ref = None

    def initialize(self):
        print("\nInitializing program...\n")
        OpenGLUtils.print_system_info()

        # INITIALIZE SHADER PROGRAM #

        # vertex shader code
        vs_code = """
void main()
{
    gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
}
"""
        # fragment shader code
        fs_code = """
out vec4 fragColor;
void main()
{
    fragColor = vec4(1.0, 1.0, 0.0, 1.0);  // YELLOW color
}
"""
        # send code to GPU and compile; store program reference
        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        # SETTING UP VAO #
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        # RENDER SETTINGS (optional) #

        # set point width and height
        glPointSize(10)

    def update(self):
        # select program to use when rendering
        glUseProgram(self.program_ref)

        # renders geometric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)


if __name__ == "__main__":
    Test().run()
