from OpenGL.GL import (GL_TRIANGLES, glBindVertexArray, glDrawArrays,  # type: ignore
                       glGenVertexArrays, glUseProgram)

from core.attribute import Attribute
from core.base import Base
from core.opengl_utils import OpenGLUtils
from core.settings import SCREEN_SIZE
from core.uniform import Uniform


# render two triangles with different positions and colors
class Test(Base):
    def __init__(self, screen_size: tuple[int, int] = SCREEN_SIZE):
        super().__init__(screen_size)
        self.base_color2 = None
        self.base_color1 = None
        self.translation2 = None
        self.vertex_count = None
        self.program_ref = None
        self.translation1 = None

    def initialize(self):
        print("Initializing program...")

        # initialize program #
        vs_code = """
in vec3 position;
uniform vec3 translation;
void main()
{
vec3 pos = position + translation;
gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
}
"""
        fs_code = """
uniform vec3 base_color;
out vec4 fragColor;
void main()
{
fragColor = vec4(
base_color.r, base_color.g, base_color.b,
1.0);
}
"""
        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        # set up vertex array object #
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        # set up vertex attribute #
        position_data = [[0.0, 0.2, 0.0], [0.2, -0.2, 0.0], [-0.2, -0.2, 0.0]]
        self.vertex_count = len(position_data)

        position_attribute = Attribute("vec3", position_data)
        position_attribute.associate_variable(self.program_ref, "position")

        # set up uniforms #
        self.translation1 = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation1.locate_variable(self.program_ref, "translation")
        self.translation2 = Uniform("vec3", [0.5, 0.0, 0.0])
        self.translation2.locate_variable(self.program_ref, "translation")
        self.base_color1 = Uniform("vec3", [1.0, 0.0, 0.0])
        self.base_color1.locate_variable(self.program_ref, "base_color")
        self.base_color2 = Uniform("vec3", [0.0, 0.0, 1.0])
        self.base_color2.locate_variable(self.program_ref, "base_color")

    def update(self):
        glUseProgram(self.program_ref)
        # draw the first triangle
        self.translation1.upload_data()
        self.base_color1.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

        # draw the second triangle
        self.translation2.upload_data()
        self.base_color2.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


if __name__ == "__main__":
    Test().run()
