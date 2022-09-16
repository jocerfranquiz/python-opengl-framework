from OpenGL.GL import (GL_LINE_LOOP, glBindVertexArray,  # type: ignore
                       glDrawArrays, glGenVertexArrays, glLineWidth,
                       glUseProgram)

from core.attribute import Attribute
from core.base import Base
from core.opengl_utils import OpenGLUtils
from core.settings import SCREEN_SIZE


# render two shapes
class Test(Base):

    def __init__(self, screen_size: tuple[int, int] = SCREEN_SIZE):
        super().__init__(screen_size)
        self.vertex_count_square = None
        self.vao_square = None
        self.vertex_count_tri = None
        self.vao_tri = None
        self.program_ref = None

    def initialize(self):
        print("Initializing program...")

        # INITIALIZE PROGRAM #
        vs_code = """
in vec3 position;
void main()
{
gl_Position = vec4(
position.x, position.y, position.z, 1.0);
}
"""
        fs_code = """
out vec4 fragColor;
void main()
{
fragColor = vec4(1.0, 1.0, 0.0, 1.0);
}
"""
        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        # RENDER SETTINGS #
        glLineWidth(4)

        # SET UP VERTEX ARRAY OBJECT - triangle #
        self.vao_tri = glGenVertexArrays(1)
        glBindVertexArray(self.vao_tri)

        position_data_tri = [
            [-0.5, 0.8, 0.0],
            [-0.2, 0.2, 0.0],
            [-0.8, 0.2, 0.0]
        ]

        self.vertex_count_tri = len(position_data_tri)
        position_attribute_tri = Attribute("vec3", position_data_tri)
        position_attribute_tri.associate_variable(self.program_ref, "position")

        # SET UP VERTEX ARRAY OBJECT - square #
        self.vao_square = glGenVertexArrays(1)
        glBindVertexArray(self.vao_square)

        position_data_square = [
            [0.8, 0.8, 0.0],
            [0.8, 0.2, 0.0],
            [0.2, 0.2, 0.0],
            [0.2, 0.8, 0.0]
        ]

        self.vertex_count_square = len(position_data_square)
        position_attribute_square = Attribute("vec3", position_data_square)
        position_attribute_square.associate_variable(self.program_ref,
                                                     "position")

    def update(self):
        # using same program to render both shapes
        glUseProgram(self.program_ref)

        # draw the triangle
        glBindVertexArray(self.vao_tri)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count_tri)

        # draw the square
        glBindVertexArray(self.vao_square)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count_square)


if __name__ == "__main__":
    Test().run()
