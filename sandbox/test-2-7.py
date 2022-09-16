from OpenGL.GL import (GL_COLOR_BUFFER_BIT, GL_TRIANGLES, glBindVertexArray,  # type: ignore
                       glClear, glClearColor, glDrawArrays, glGenVertexArrays,
                       glUseProgram)

from core.attribute import Attribute
from core.base import Base
from core.opengl_utils import OpenGLUtils
from core.settings import SCREEN_SIZE
from core.uniform import Uniform


# animate triangle moving across screen
class Test(Base):
    def __init__(self, screen_size: tuple[int, int] = SCREEN_SIZE):
        super().__init__(screen_size)
        self.base_color = None
        self.translation = None
        self.vertex_count = None
        self.program_ref = None

    def initialize(self):
        print("Initializing program...")

        # initialize program #
        vs_code = """
in vec3 position;
uniform vec3 translation;
void main()
{
vec3 pos = position + translation;
gl_Position = vec4(pos.x, pos.y, pos.z,
1.0);
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

        # render settings (optional) #
        # specify color used when clearly
        glClearColor(0.0, 0.0, 0.0, 1.0)

        # set up vertex array object #
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        # set up vertex attribute #
        position_data = [[0.0, 0.2, 0.0], [0.2, -0.2, 0.0], [-0.2, -0.2, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute("vec3", position_data)
        position_attribute.associate_variable(self.program_ref, "position")

        # set up uniforms #
        self.translation = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, "translation")
        self.base_color = Uniform("vec3", [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, "base_color")

    def update(self):
        # update data #
        # increase x coordinate of translation
        self.translation.data[0] += 0.01
        # if triangle passes off-screen on the right,
        # change translation, so it reappears on the left
        if self.translation.data[0] > 1.2:
            self.translation.data[0] = -1.2

        # render scene #
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


if __name__ == "__main__":
    Test().run()
