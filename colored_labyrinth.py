#! bpy
"""
Name: 'colored_labyrinth.py'
Blender: 269
Group: 'Materials'
Tooltip: 'Generates colorful objects by materials'
"""
import bpy

level_00 = ["###################",
            "#.                #",
            "#        $        #",
            "#                 #",
            "#                 #",
            "#        @        #",
            "#                 #",
            "#                 #",
            "#                 #",
            "#                 #",
            "###################"]


level_01 = ["    #####           ",
            "    #   #           ",
            "    #$  #           ",
            "  ###  $##          ",
            "  #  $ $ #          ",
            "### # ## #   ###### ",
            "#   # ## #####  ..# ",
            "# $  $          ..# ",
            "##### ### #@##  ..# ",
            "    #     ######### ",
            "    #######         "]

MATERIAL_RED = bpy.data.materials.new('Red Material')


def sokobanLevel(level):
    """Generating a labyrinth with colored cubes"""

    cols = len(level[0])
    rows = len(level)

    for row in range(rows):
        for i in range(cols):
            if level[row][i] == '#':
                bpy.ops.mesh.primitive_cube_add(location=(row*2, i*2, 0))
                obj = bpy.context.object
                setColor(obj, MATERIAL_ROT, (1, 0, 0))


def setColor(obj, material, color):
    material.diffuse_color = color
    material.specular_hardness = 200
    obj.data.materials.append(material)


if __name__ == '__main__':
    sokobanLevel(level_00)
