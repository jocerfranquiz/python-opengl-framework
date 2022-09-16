===============
Computer Graphics and Visualization
===============

Core Concepts
-------------

**Model**: is a collection of objects that are rendered together.

**Object**: is a collection of vertices, edges, faces, and materials.

**Vertex**: is a point in 3D space.

**Edge**: is a line between two vertices.

**Face**: is a polygon defined by three or more vertices.

**Material**: is a collection of properties that define how an object is rendered.

**UV Map**: is a 2D texture coordinate system that is used to map a texture to an object.

**Texture**: is an image that is applied to an object.

**Rendering**: is the process of generating 2D images of 3D scenes.

**Shading**: is the process of computing the color of each pixel in the

**Shadows**: are the dark areas that are cast by objects in a scene.

**Raster**: is an array of pixels that is used to store the image that is being rendered on a screen, arranged in a 2D grid

**Frame**: is a single image that is rendered by the computer

**Frame rate (FPS)**: is the number of frames that are rendered per second

**Rasterization**: is the process of converting a 3D scene into a 2D raster image

**Resolution**: is the number of pixels in the image.

**Pixel**: is the smallest unit of a raster image.

**Precision**: is the number of bits used to represent each pixel.

**Shader**: is a program that is executed on the GPU to perform a specific task.

**Vertex Shader**: is a program that runs on the GPU and is responsible for transforming vertices from object coordinates into clip coordinates.

**Fragment Shader**: is a program that runs on the GPU and is responsible for computing the color of each pixel.

Buffers
^^^^^^^

**Buffer / data buffer / buffer memory**: is a memory region that is used to store temporary intermediate results of a rendering process.

**Vertex Buffer Object (VBO)**: is a buffer that stores the vertex data for a mesh.

**Index Buffer Object (IBO)**: is a buffer that stores the index data for a mesh.

**Vertex Array Object (VAO)**: is a collection of vertex buffer objects and index buffer objects.

**Frame buffer**: is a buffer that is used to store the final image that is being rendered.
It may contain color, depth, and stencil information.

**Depth buffer / Z-buffer**: is a buffer that is used to store the depth of each point to the virtual camera.

**Stencil buffer**: is a buffer that is used to store the stencil information of each pixel,
like the number of objects that are visible at each pixel, shadows, reflexions, etc.

**Color buffer**: is a buffer that is used to store the color of each pixel in the image. Commonly in RGB or RGBA format.

**Other buffers**: Normal buffer, Texture buffer, Shadow buffer.

Virtual Camera
^^^^^^^^^^^^^^

The virtual camera is the point of view from which the scene is rendered. It is defined by a position, a direction,
and an up vector. The position is the location of the camera in 3D space.
The direction is the direction in which the camera is pointing. The up vector is the direction that is considered
to be up for the camera. The virtual camera is usually represented by a pyramid, called the frustum,
that is used to define the region of space that is visible to the camera.

**Frustum**: is defined by the position of the camera, the direction in which the camera is pointing, and the field of
view of the camera. The frustum is usually truncated to avoid rendering objects that are too far away from the camera.

**Field of view (FOV) / Aperture**: is the angle between the left and right edges of the frustum

- **FOVY**: is the vertical field of view of the camera.
- **FOVX**: is the horizontal field of view of the camera ( FOVX = 2 * atan(tan(FOVY/2) * aspectRatio) ).
- **FOVY** = $2 * atan(tan(FOVX/2) / aspectRatio)$

**Near (clipping) Plane / zNear**: is the plane that is closest to the virtual camera.

**Far (Clipping) Plane / zFar**: is the plane that is farthest from the virtual camera.

**Perspective Projection**: is the process of projecting a 3D scene onto a 2D image plane.

**Orthographic Projection**: is the process of projecting a 3D scene onto a 2D image plane.

**Aspect Ratio**: is the ratio between the width and the height of the Near plane.

**Line of Sight (LOS)**: is the line that connects the camera to a point in the scene.

**View Matrix**: is the matrix that transforms world coordinates into camera coordinates.

**Projection Matrix**: is the matrix that transforms camera coordinates into clip coordinates.

**Viewport Matrix**: is the matrix that transforms clip coordinates into screen coordinates.

**Model Matrix**: is the matrix that transforms object coordinates into world coordinates.

Textures
^^^^^^^^

**Texture**: is a 2D image that can be used to color a mesh.

**Color mesh**: is a mesh that has a color for each vertex.

**Texture Sampler**: is a variable that is used to access a texture.

**Texture Coordinate / UV coordinates**: is a 2D coordinate that is used to access a texture.

**Texture Unit**: is a variable that is used to access a texture sampler.

**Texture Filtering**: is the process of determining the color of a pixel based on the colors of the surrounding pixels.

**Texture Wrapping**: is the process of determining the color of a pixel that is outside the bounds of the texture.

**Mipmapping**: is the process of generating a series of textures that are progressively smaller.

**Normal Map**: is a texture that stores the normal vector for each pixel in the texture.

**Specular Map**: is a texture that stores the specular color for each pixel in the texture.

**Diffuse Map**: is a texture that stores the diffuse color for each pixel in the texture.

**Ambient Map**: is a texture that stores the ambient color for each pixel in the texture.

**Emissive Map**: is a texture that stores the emissive color for each pixel in the texture.

**Light Map**: is a texture that stores the light color for each pixel in the texture.

Mapping Colors
^^^^^^^^^^^^^^

**Lighting**: is the process of computing the color of a pixel based on the position of the light sources in the scene.

**Ambient Lighting**: is the process of computing the color of a pixel based on the ambient light in the scene.

**Diffuse Lighting**: is the process of computing the color of a pixel based on the diffuse light in the scene.

**Specular Lighting**: is the process of computing the color of a pixel based on the specular light in the scene.

**Emissive Lighting**: is the process of computing the color of a pixel based on the emissive light in the scene.

**Phong Shading**: is the process of computing the color of a pixel based on the Phong lighting model.

**Blinn-Phong Shading**: is the process of computing the color of a pixel based on the Blinn-Phong lighting model.

**Lighting Model**: is a mathematical model that is used to compute the color of a pixel based on
the position of the light sources in the scene. It's commonly composed different components like:

- **Normal Light**
- **Specular Light**
- **Diffuse Light**
- **Ambient Light**
- **Emissive Light**
- **Reflection Light**

Shadows
^^^^^^^

**Shadow Volume**: is the region of space that is in shadow.

**Shadow Volume Stencil**: is the stencil buffer that is used to render the shadow volume.

**Shadow Volume Depth**: is the depth buffer that is used to render the shadow volume.

**Shadow Volume Texture**: is the texture that is used to render the shadow volume.

**Shadow Volume Matrix**: is the matrix that transforms world coordinates into shadow volume coordinates.

Graphics pipeline
------------------

The graphics pipeline is the sequence of operations that are performed to render a 3D scene onto a 2D image.
It is usually divided into two parts: the CPU and the GPU.


The CPU is responsible for preparing the scene for rendering, while the GPU is responsible for rendering the scene.
The graphics pipeline divide the rendering process into multiple stages, so that the CPU and GPU can work in parallel.

The most common graphics pipeline on OpenGL is the following:

1. **Vertex Shader**: the vertex shader is executed for each vertex in the mesh. It transforms the vertex from object coordinates into clip coordinates.
2. **Primitive Assembly**: the vertices are assembled into primitives, like triangles.
3. **Rasterization**: the primitives are rasterized into fragments.
4. **Fragment Shader**: the fragment shader is executed for each fragment. It computes the color of each fragment.
5. **Depth Test**: the depth test is used to determine which fragments are visible and which are not.
6. **Stencil Test**: the stencil test is used to determine other properties of the fragments, like shadows, reflexions, etc.
7. **Blending**: the fragments are blended into the frame buffer.


