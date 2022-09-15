from OpenGL.GL import (GL_COMPILE_STATUS, GL_FRAGMENT_SHADER, GL_LINK_STATUS,  # type: ignore
                       GL_RENDERER, GL_SHADING_LANGUAGE_VERSION, GL_VENDOR,
                       GL_VERSION, GL_VERTEX_SHADER, glAttachShader,
                       glCompileShader, glCreateProgram, glCreateShader,
                       glDeleteProgram, glDeleteShader, glGetProgramInfoLog,
                       glGetProgramiv, glGetShaderInfoLog, glGetShaderiv,
                       glGetString, glLinkProgram, glShaderSource)


class OpenGLUtils:

    @staticmethod
    def initialize_shader(shader_code, shader_type):
        """
        Create and compile a OpenGL shader program
        """

        # specify the required OpenGL/GLSL version
        shader_code = "#version 330\n" + shader_code

        # create an empty shader object and return a pointer
        shader_ref = glCreateShader(shader_type)

        # stores the GLSL SOURCE CODE in the shader
        glShaderSource(shader_ref, shader_code)

        # compiles the source code
        glCompileShader(shader_ref)

        # get compilation status
        compile_success = glGetShaderiv(shader_ref, GL_COMPILE_STATUS)

        if not compile_success:
            # NOT SUCCESS: get error message
            error_message = glGetShaderInfoLog(shader_ref)

            # free memory used to store the shader source code
            glDeleteShader(shader_ref)

            error_message = "\n" + error_message.decode("utf-8")

            raise Exception(error_message)

        # SUCCESS: return shader pointer
        return shader_ref

    @staticmethod
    def initialize_program(vertex_shader_code, fragment_shader_code):
        vertex_shader_ref = OpenGLUtils.initialize_shader(
            vertex_shader_code,
            GL_VERTEX_SHADER
        )

        fragment_shader_ref = OpenGLUtils.initialize_shader(
            fragment_shader_code,
            GL_FRAGMENT_SHADER
        )

        # create empty program object and store reference to it
        program_ref = glCreateProgram()

        # attach previously compiled shader programs
        glAttachShader(program_ref, vertex_shader_ref)
        glAttachShader(program_ref, fragment_shader_ref)

        # link vertex shader to fragment shader
        glLinkProgram(program_ref)

        # get linker status
        link_success = glGetProgramiv(program_ref, GL_LINK_STATUS)

        if not link_success:
            # retrieve error message
            error_message = glGetProgramInfoLog(program_ref)

            # free memory used to store program
            glDeleteProgram(program_ref)

            # convert byte string to character string
            error_message = '\n' + error_message.decode('utf-8')

            # raise exception: halt application and print error message
            raise Exception(error_message)

        # linking was successful; return program reference value
        return program_ref

    @staticmethod
    def print_system_info():
        """
        Print version of OpenGL/GLSL in the computer
        """
        print("Vendor: " + glGetString(GL_VENDOR).decode("utf-8"))
        print("Renderer: " + glGetString(GL_RENDERER).decode("utf-8"))
        print("OpenGL version supported: " +
              glGetString(GL_VERSION).decode("utf-8"))
        print("GLSL version supported: " +
              glGetString(GL_SHADING_LANGUAGE_VERSION).decode("utf-8"))
