import random

import bpy
import numpy as np
import pandas as pd

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# for row in range(10):
#     for col in range(10):
#         delta_x = row % 2 * 1 / 2
#         x = col + delta_x
#         y = row
#         bpy.ops.mesh.primitive_cube_add(
#             size=1,
#             location=[x, y, 0]
#         )
# scale = 1
# width = (scale / 2) / np.tan(np.pi / 6) * 2
# delta_x = row % 2 * width / 2
# x = width + delta_x
# bpy.ops.mesh.primitive_cylinder_add(
#     vertices=6,
#     depth=depth,
#     location=[
#         x,
#         scale * 2 * row,
#         depth * random.random()
#     ],
# )
# bpy.ops.transform.resize(value=[scale, scale, 1])
# depth = 0.1
# padding = 0.05
# for r in range(10):
#     bpy.ops.mesh.primitive_cylinder_add(
#         vertices=6,
#         depth=depth,
#         location=[0, 0, (depth + 0.05) * r + depth / 2],
#         rotation=[0, 0, random.random()]
#     )
#     scale = 5
#     bpy.ops.transform.resize(value=[scale, scale, 1])

df = pd.read_csv('./pecados.csv', sep=';')

gula = '0_gula_presente'
pereza = '0_pereza_presente'
lujuria = '0_lujuria_presente'

columns = [gula, pereza, lujuria]

bin_size = 10
_min = 0
_max = 100
bins = _max / bin_size
_size = _max - _min
_range = np.arange(_min, _max + bin_size, bin_size)


dt = np.dtype([('coords', np.int64, (3,)), ('cant', np.int64)])

df2 = pd.DataFrame({
    'gula': pd.cut(df[gula], _range),
    'pereza': pd.cut(df[pereza], _range),
    'lujuria': pd.cut(df[lujuria], _range),
})

groups = df2.groupby(['gula', 'pereza', 'lujuria']).size()
spheres = []
for (x, y, z) in groups.index:
    coords = (
        x.left + bin_size / 2,
        y.left + bin_size / 2,
        z.left + bin_size / 2
    )
    cant = groups[x, y, z]
    if cant != 0:
        spheres.append((coords, cant))
spheres = np.array(spheres, dtype=dt)

max_size = np.max(spheres['cant'])
_max_scale = _max / bins / 2

for ((x, y, z), cant) in spheres:
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=[x, y, z])
    scale = _max_scale * cant / max_size
    bpy.ops.transform.resize(value=[scale, scale, scale])
