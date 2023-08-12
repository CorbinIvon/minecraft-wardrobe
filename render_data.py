import PIL.Image
# texture = 'resources/UV-Helper'
texture = 'resources/steve_template'
# texture = 'resources/Corbin-Engineer01'
tx = PIL.Image.open(texture+'.png').size[0]
ty = PIL.Image.open(texture+'.png').size[1]

class head:
  volume_x=8
  volume_y=8
  volume_z=8
  position=(0, 12, 0)
  # zig zag "Z" when facing the cube face on.
  vertices=[
    (-volume_x/2,  volume_y/2,  volume_z/2), # Front top left
    ( volume_x/2,  volume_y/2,  volume_z/2), # Front top right
    (-volume_x/2, -volume_y/2,  volume_z/2), # Front bottom left
    ( volume_x/2, -volume_y/2,  volume_z/2), # Front bottom right
    ( volume_x/2,  volume_y/2, -volume_z/2), # Back top right
    (-volume_x/2,  volume_y/2, -volume_z/2), # Back top left
    ( volume_x/2, -volume_y/2, -volume_z/2), # Back bottom right
    (-volume_x/2, -volume_y/2, -volume_z/2), # Back bottom left
  ]
  triangles=[
    (0, 1, 2), (3, 2, 1), # Front face
  ]

  uv_offset = (8, 48)
  uv_size = (8, 8)
  # The image should have 64 incremental points. The size of the image is unknown.
  # Calculate the offset as a fraction of the total UV space (assuming 64x64 grid)
  x_offset = uv_offset[0] / 64
  y_offset = uv_offset[1] / 64
  # Calculate the scaling factors based on the desired UV size (assuming 64x64 grid)
  u_scale = uv_size[0] / 64
  v_scale = uv_size[1] / 64

  uvs = [
      ((1 * u_scale) + x_offset, (1 * v_scale) + y_offset),
      ((0 * u_scale) + x_offset, (1 * v_scale) + y_offset),
      ((1 * u_scale) + x_offset, (0 * v_scale) + y_offset),
      ((0 * u_scale) + x_offset, (0 * v_scale) + y_offset), # Front face
  ]