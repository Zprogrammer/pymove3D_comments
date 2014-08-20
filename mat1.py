#!bpy
"""
Name: 'mat1.py'
Blender: 2.69
Group: 'Sample'
Tooltip: 'Put one image on each site of a cube'
"""
import bpy
import os


def uvMapperCube(obj):
    """ Put image to an object"""

    # used names
    matname = "matUVMapping"
    texname = "texUVMapping"

    # new material
    if not matname in bpy.data.materials:
        material = bpy.data.materials.new(matname)
        material.diffuse_color = (0, .5, .4)
        obj.data.materials.append(material)

    # new texture
    texUV = bpy.data.textures.new(texname, type="IMAGE")
    image_path = os.path.expanduser("//yourpicture.jpg")
    image = bpy.data.images.load(image_path)
    texUV.image = image

    # connect textur with material
    bpy.data.materials[matname].texture_slots.add()
    bpy.data.materials[matname].active_texture = texUV
    bpy.data.materials[matname].texture_slots[0].texture_coords = "GLOBAL"
    bpy.data.materials[matname].texture_slots[0].mapping = "CUBE"


def delete_old_stuff():

    # escape edit mode
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')

    # delete all mesh objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # delete all materials
    for i in bpy.data.materials.values():
        bpy.data.materials.remove(i)

    # delete all textures
    for i in bpy.data.textures.values():
        bpy.data.textures.remove(i)

    # delete all images 
    for i in bpy.data.images.values():
        # delete image path, this is only possible without a user
        i.user_clear()
        # delete all, except »Render Result«
        if i.name != "Render Result":
            bpy.data.images.remove(i)

if __name__ == "__main__":
    delete_old_stuff()
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
    obj = bpy.context.scene.objects.active
    obj.name = 'image-as-uvmapping'
    obj = bpy.context.scene.objects['image-as-uvmapping']
    uvMapperCube(obj)
