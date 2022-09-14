from OpenGL.GL import (GL_COMPILE_STATUS, GL_RENDERER,
                       GL_SHADING_LANGUAGE_VERSION, GL_VENDOR, GL_VERSION,
                       glCompileShader, glCreateShader, glDeleteShader,
                       glGetShaderInfoLog, glGetShaderiv, glGetString,
                       glShaderSource)


class OpenGLUtils:

    @staticmethod
    def initialize_shader(shader_code, shader_type):
        """
        Create and compile a OpenGL shader program
        """

        # specify the required OpenGL/GLSL version
        shader_code = "version 330\n" + shader_code

        # create an empty shader and return a pointer
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
    def print_system_info():
        """
        Print version of OpenGL/GLSL in the computer
        """
        print("Vendor: " + glGetString(GL_VENDOR).decode("utf-8"))
        print("Renderer: " + glGetString(GL_RENDERER).decode("utf-8"))
        print("OpenGL version supported: " + glGetString(GL_VERSION).decode("utf-8"))
        print("GLSL version supported: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode("utf-8"))
