import bpy
import pandas as pd

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

df = pd.read_csv('./profano.csv')
df.head()

for i in range(0, 43):
    for j in range(0, 43):
        cant = len(
            df[['gestacion-aborto', 'gestacion-persona']][
                (df['gestacion-aborto'] == j) & (df['gestacion-persona'] == i)
            ]
        )
        bpy.ops.mesh.primitive_cube_add(size=1, location=[i + 0.5, j + 0.5, cant / 2])
        bpy.ops.transform.resize(value=[1, 1, cant])
