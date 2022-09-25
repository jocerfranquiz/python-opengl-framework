from math import tau

from OpenGL.GL import *

from core.attribute import Attribute
from core.base import Base
from core.matrix import Matrix
from core.opengl_utils import OpenGLUtils
from core.settings import SCREEN_SIZE
from core.uniform import Uniform


# move a triangle around the screen
class Test(Base):
    def __init__(self, screen_size: tuple[int, int] = SCREEN_SIZE):
        super().__init__(screen_size)
        self.turn_speed = None
        self.move_speed = None
        self.projection_matrix = None
        self.model_matrix = None
        self.vertex_count = None
        self.program_ref = None
        self.m = None

    def initialize(self):
        print("Initializing program...")

        # INITIALIZE PROGRAM #
        vs_code = """
in vec3 position;
uniform mat4 projection_matrix;
uniform mat4 model_matrix;
void main()
{
gl_Position = projection_matrix *
model_matrix * vec4(position, 1.0);
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
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        # SET UP VERTEX ARRAY OBJECT #
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        # SET UP VERTEX ATTRIBUTE #
        position_data = [[0.0, 0.2, 0.0], [0.1, -0.2, 0.0], [-0.1, -0.2, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute("vec3", position_data)
        position_attribute.associate_variable(self.program_ref, "position")

        # SET UP UNIFORMS #
        m_matrix = Matrix.make_translation(0, 0, -1)
        self.model_matrix = Uniform("mat4", m_matrix)
        self.model_matrix.locate_variable(self.program_ref, "model_matrix")
        p_matrix = Matrix.make_perspective()
        self.projection_matrix = Uniform("mat4", p_matrix)
        self.projection_matrix.locate_variable(
            self.program_ref, "projection_matrix"
        )

        # movement speed, units per second
        self.move_speed = 0.5

        # rotation speed, radians per second
        self.turn_speed = tau / 4.0

    def update(self):
        # update data
        m = Matrix.make_identity()

        move_amount = self.move_speed * self.delta_time
        turn_amount = self.turn_speed * self.delta_time

        # global translation
        if self.input.is_key_pressed("w"):
            m = Matrix.make_translation(0, move_amount, 0)
        self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed("s"):
            m = Matrix.make_translation(0, -move_amount, 0)
        self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed("a"):
            m = Matrix.make_translation(-move_amount, 0, 0)
        self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed("d"):
            m = Matrix.make_translation(move_amount, 0, 0)
        self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed("z"):
            m = Matrix.make_translation(0, 0, move_amount)
        self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed("x"):
            m = Matrix.make_translation(0, 0, -move_amount)
        self.model_matrix.data = m @ self.model_matrix.data

        # global rotation (around the origin)
        if self.input.is_key_pressed("q"):
            m = Matrix.make_rotation_z(turn_amount)
        self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed("e"):
            m = Matrix.make_rotation_z(-turn_amount)
        self.model_matrix.data = m @ self.model_matrix.data

        # local translation
        if self.input.is_key_pressed("i"):
            m = Matrix.make_translation(0, move_amount, 0)
        self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed("k"):
            m = Matrix.make_translation(0, -move_amount, 0)
        self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed("j"):
            m = Matrix.make_translation(-move_amount, 0, 0)
        self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed("l"):
            m = Matrix.make_translation(move_amount, 0, 0)
        self.model_matrix.data = self.model_matrix.data @ m

        # local rotation (around object center)
        if self.input.is_key_pressed("u"):
            m = Matrix.make_rotation_z(turn_amount)
        self.model_matrix.data = self.model_matrix.data @ m
        if self.input.is_key_pressed("o"):
            m = Matrix.make_rotation_z(-turn_amount)
        self.model_matrix.data = self.model_matrix.data @ m

        # RENDER SCENE #
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_ref)
        self.projection_matrix.upload_data()
        self.model_matrix.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


if __name__ == "__main__":
    Test().run()
