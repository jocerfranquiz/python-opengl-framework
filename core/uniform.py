from OpenGL.GL import (
    glGetUniformLocation,
    glUniform1f,
    glUniform1i,
    glUniform2f,
    glUniform3f,
    glUniform4f,
)


class Uniform(object):
    def __init__(self, data_type, data):
        # type of data:
        # int | bool | float | vec2 | vec3 | vec4
        self.dataType = data_type
        # data to be sent to uniform variable
        self.data = data
        # reference for variable location in program
        self.variable_ref = None

    # get and store reference for program variable with given name
    def locate_variable(self, program_ref, variable_name):
        self.variable_ref = glGetUniformLocation(program_ref, variable_name)

    # store data in uniform variable previously located
    def upload_data(self):

        # if the program does not reference the variable, then exit
        if self.variable_ref == -1:
            return

        if self.dataType == "int":
            glUniform1i(self.variable_ref, self.data)
        elif self.dataType == "bool":
            glUniform1i(self.variable_ref, self.data)
        elif self.dataType == "float":
            glUniform1f(self.variable_ref, self.data)
        elif self.dataType == "vec2":
            glUniform2f(self.variable_ref, self.data[0], self.data[1])
        elif self.dataType == "vec3":
            glUniform3f(
                self.variable_ref, self.data[0], self.data[1], self.data[2]
            )
        elif self.dataType == "vec4":
            glUniform4f(
                self.variable_ref,
                self.data[0],
                self.data[1],
                self.data[2],
                self.data[3],
            )
