from OpenGL.GL import (GL_LINE_LOOP, glBindVertexArray,  # type: ignore
                       glDrawArrays, glGenVertexArrays, glLineWidth,
                       glUseProgram)

from core.attribute import Attribute
from core.base import Base
from core.opengl_utils import OpenGLUtils
from core.settings import SCREEN_SIZE


# render six points in a hexagon arrangement
class Test(Base):

    def __init__(self, screen_size: tuple[int, int] = SCREEN_SIZE):
        super().__init__(screen_size)
        self.vertex_count = None
        self.program_ref = None

    def initialize(self):
        print("\nInitializing program...\n")
        OpenGLUtils.print_system_info()

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

        # RENDER SETTINGS (optional) #
        glLineWidth(4)

        # SET UP VERTEX ARRAY OBJECT #
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        # SET UP VERTEX ATTRIBUTE #
        position_data = [
            [0.8, 0.0, 0.0], [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0], [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0], [0.4, -0.6, 0.0]
        ]

        self.vertex_count = len(position_data)
        position_attribute = Attribute("vec3", position_data)
        position_attribute.associate_variable(self.program_ref, "position")

    def update(self):
        glUseProgram(self.program_ref)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count)


if __name__ == "__main__":
    Test().run()
