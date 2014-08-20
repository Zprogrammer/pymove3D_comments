#!bpy
"""
Name: 'mars_mobile.py'
Blender: 2.69
Group: 'Composition'
Tooltip: 'Rotate, locate and scale objects assembled to a futuristic prototype'
"""
import bpy


def create_objects():
    """Create objects from a list of attributes

    List values:

    object name   -- string
    object type   -- string
    location      -- tupel of integers
    """
    objectlist = [('cu1', 'cube', (-6, 1, 1)),
                  ('cu2', 'cube', (-3, 1, 1)),
                  ('cy1', 'cylinder', (0, 1, 1)),
                  ('cy2', 'cylinder', (3, 1, 1)),
                  ('uv1', 'uv_sphere', (6, 1, 1)),
                  ('uv2', 'uv_sphere', (9, 1, 1))]

    for element in objectlist:
        if element[1] == 'cube':
            bpy.ops.mesh.primitive_cube_add(location=element[2])
        if element[1] == 'cylinder':
            bpy.ops.mesh.primitive_cylinder_add(location=element[2])
        if element[1] == 'uv_sphere':
            bpy.ops.mesh.primitive_uv_sphere_add(location=element[2])
        # give it a name
        obj = bpy.context.object
        obj.name = element[0]


def select_cubes():
    """Sample: select two objects by name """

    bpy.ops.object.select_pattern(pattern="cu2")
    bpy.ops.object.select_pattern(pattern="cu1")


def activate_object():
    """Sample: activate an object by name"""

    bpy.context.scene.objects.active = bpy.data.objects["cu2"]


def scale_cu2():
    """Select, scale and move cube 2"""

    bpy.context.scene.objects.active = bpy.data.objects["cu2"]
    obj = bpy.context.scene.objects.active
    obj.scale = (1, 1, 3)
    obj.location = (-3, 1, 3)


def scale_cy():
    """Select cylinders, scale and move"""

    bpy.context.scene.objects.active = bpy.data.objects["cy1"]
    obj = bpy.context.scene.objects.active
    obj.scale = (1, 1, .2)
    obj.location = (0, 1, .2)

    bpy.context.scene.objects.active = bpy.data.objects["cy2"]
    obj = bpy.context.scene.objects.active
    obj.scale = (1, 1, .2)
    obj.location = (3, 1, .2)


def assemble_mars_mobile():
    """Create a composite piece """

    pi_half = 3.141592/2

    # body
    bpy.context.scene.objects.active = bpy.data.objects["cu2"]
    obj = bpy.context.scene.objects.active
    obj.location = (-3, 1, 1.5)
    # rotation
    obj.rotation_euler = [pi_half, 0, 0]

    # wheel (right)
    bpy.context.scene.objects.active = bpy.data.objects["cy1"]
    obj = bpy.context.scene.objects.active
    obj.location = (-4, 2, 1)
    obj.rotation_euler = [0, pi_half, 0]

    # wheel (left)
    bpy.context.scene.objects.active = bpy.data.objects["cy2"]
    obj = bpy.context.scene.objects.active
    obj.location = (-2, 2, 1)
    obj.rotation_euler = [0, pi_half, 0]

    # wheel (front)
    bpy.context.scene.objects.active = bpy.data.objects["uv1"]
    obj = bpy.context.scene.objects.active
    obj.location = (-3, -1, 1)

    # cabin
    bpy.context.scene.objects.active = bpy.data.objects["cu1"]
    obj = bpy.context.scene.objects.active
    obj.location = (-3, 2, 3)

    bpy.context.scene.objects.active = bpy.data.objects["uv2"]
    obj = bpy.context.scene.objects.active
    obj.location = (-3, 2, 4)


if __name__ == '__main__':
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
    # delete all meshes from a szene
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()
    create_objects()
    ## comment and uncomment the lines as you like
    # select_cubes()
    # aktivate_object()
    # scale_cu2()
    # scale_cy()
    # assemble_mars_mobile()
