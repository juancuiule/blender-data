import random
import math
import bpy
import numpy as np

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# radius of the circle
circle_r = 10

angles = np.arange(0, 5 * 2 * math.pi + math.pi / 8, math.pi / 8)
print(angles)
for i, phi in enumerate(angles):

    # phi = angles[angle]

    x = i * 0.2 * math.cos(phi)
    y = i * 0.2 * math.sin(phi)
    z = i * 1.5 / 10

    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=1,
        location=[x, y, z]
    )
    scale = 1 + 1 * i / 15 # random.random()
    bpy.ops.transform.resize(value=[scale, scale, scale])

# # radius of the circle
# circle_r = 10
# # center of the circle (x, y)

# for i in range(500):
#     # random angle
#     phi = 2 * math.pi * random.random()
#     theta = math.pi * random.random()
#     r = circle_r * math.sqrt(random.random())
#
#     x = r * math.sin(phi) * math.cos(theta)
#     y = r * math.sin(phi) * math.sin(theta)
#     z = r * math.cos(phi)
#
#     bpy.ops.mesh.primitive_uv_sphere_add(
#         radius=1,
#         location=[x, y, z]
#     )
#     scale = random.random()
#     bpy.ops.transform.resize(value=[scale, scale, scale])


# vertices = 6
# scale = 1
# rows = 10
# cols = 10
#
# width = (scale / 2) / np.tan(np.pi / vertices) * 2
# height = scale * 2
# x_width = width * cols
# y_width = height * np.ceil(rows / 2) + scale * np.floor(rows / 2)
#
# for row in range(rows):
#     pair_row = 1 if row % 2 == 0 else 0
#     for col in range(cols + pair_row):
#         depth = random.randint(5, 10) / 10
#         delta_y = row / 2 * scale
#         delta_x = pair_row * (width / 2)
#         x = col * width + delta_x - x_width / 2
#         y = row * height - delta_y - y_width / 2
#         bpy.ops.mesh.primitive_cylinder_add(
#             vertices=vertices,
#             depth=depth,
#             location=[
#                 x + width / 2 - pair_row * width,
#                 y + height / 2,
#                 depth / 2  # depth * 0.8 * random.random()
#             ],
#         )
#         bpy.ops.object.modifier_add(type='BEVEL')
#         bpy.ops.transform.resize(value=[scale, scale, 1])

# l = 3
# size = 4
# padding = 2
# for x in range(l):
#     for y in range(l):
#         for z in range(l):
#             bpy.ops.mesh.primitive_cube_add(
#                 size=size,
#                 location=[
#                     (x + (1 - l) / 2) * (size + padding),
#                     (y + (1 - l) / 2) * (size + padding),
#                     (z + (1 - l) / 2) * (size + padding),
#                 ],
#                 rotation=[
#                     random.random(),
#                     random.random(),
#                     random.random(),
#                 ]
#             )

import bpy
import numpy as np
import math
import random

"""
radius = [1, 1, 2, 3, 5, 8, 13, 21, 34]
for rad in radius:    
    circle_r = rad
    for i in range(100):
     # random angle
         phi = 2 * math.pi * random.random()
         theta = math.pi * random.random()
         r = circle_r # random.random()

         x = r * math.sin(phi) * math.cos(theta)
         y = r * math.sin(phi) * math.sin(theta)
         z = r * math.cos(phi)

         bpy.ops.mesh.primitive_uv_sphere_add(
             radius=1,
             location=[x, y, z]
         )
         scale = circle_r / 34
         bpy.ops.transform.resize(value=[scale, scale, scale])
"""

"""
def Curve(x_fn, y_fn, z_fn, t_min, t_max, step):
    l = np.arange(t_min, t_max + step, step)
    for i, angle in enumerate(l):
        scale = i / len(l) # 0.2 if i < len(l) - 1 else 0.5 
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=1,
            location=[
                x_fn(angle) * 4,
                y_fn(angle) * 4,
                z_fn(angle) * 4,
            ]
        )
        bpy.ops.transform.resize(value=[scale, scale, scale])

# for i, n in enumerate([1, 2, 3, 5, 8, 13, 21]):
for i, n in enumerate([15, 15, 15, 15, 15, 15, 15, 15]):
    Curve(
        lambda t: 4 * t / (math.pi * 2) * math.sin(t + math.pi / 4 * i),
        lambda t: 4 * t / (math.pi * 2) * math.cos(t + math.pi / 4 * i),
        lambda id: id,
        0,
        math.pi * 2,
        math.pi / 180 * 10
    )
"""
