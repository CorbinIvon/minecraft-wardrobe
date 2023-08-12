import PIL.Image
texture = 'resources/UV-Helper'
# texture = 'resources/steve_template'
# texture = 'resources/Corbin-Engineer01'
tx = PIL.Image.open(texture+'.png').size[0]
ty = PIL.Image.open(texture+'.png').size[1]

class head:
  size_x=8
  size_y=8
  size_z=8
  position=(0, 12, 0)
  # zig zag "Z" when facing the cube face on.
  vertices=[
    (-size_x/2,  size_y/2,  size_z/2), # Front top left
    ( size_x/2,  size_y/2,  size_z/2), # Front top right
    (-size_x/2, -size_y/2,  size_z/2), # Front bottom left
    ( size_x/2, -size_y/2,  size_z/2), # Front bottom right
    ( size_x/2,  size_y/2, -size_z/2), # Back top right
    (-size_x/2,  size_y/2, -size_z/2), # Back top left
    ( size_x/2, -size_y/2, -size_z/2), # Back bottom right
    (-size_x/2, -size_y/2, -size_z/2), # Back bottom left
  ]
  triangles=[
    (0, 1, 2), (3, 2, 1), # Front face
  ]
  # Scale and offset for the front face
  front_scale = (tx, ty) # Scale in U and V directions
  front_offset = (0,0) # Offset in U and V directions (in pixels)

  # Position of the face on the texture (8, 8) to (15, 15)
  # tx_pos = (8) / tx # Starting U coordinate
  # ty_pos = (48) / ty # Starting V coordinate
  tx_pos = 0 / tx # Starting U coordinate
  ty_pos = 0 / ty # Starting V coordinate

  # Size of the face on the texture (8 pixels wide and 8 pixels tall)
  tx_size = (1) / tx # Width in U direction
  ty_size = (1) / ty # Height in V direction

  # Applying scale and offset to UV coordinates
  uvs = [
    (tx_pos + tx_size * front_scale[0] - front_offset[0] / tx, ty_pos + ty_size * front_scale[1] - front_offset[1] / ty),
    (tx_pos - front_offset[0] / tx, ty_pos + ty_size * front_scale[1] - front_offset[1] / ty),
    (tx_pos + tx_size * front_scale[0] - front_offset[0] / tx, ty_pos - front_offset[1] / ty),
    (tx_pos - front_offset[0] / tx, ty_pos - front_offset[1] / ty),
  ]