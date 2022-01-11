import os

filename = os.path.join("/Users/juanignaciocuiule/Documents/blender/data-blender", "pecados.py")
exec(compile(open(filename).read(), filename, 'exec'))