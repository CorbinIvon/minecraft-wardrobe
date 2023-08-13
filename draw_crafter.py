from ursina import *

texture_index = 0
textures = ['resources/steve_template']
texture = textures[texture_index]

def create_plane(texture_scale = (64, 64), texture_position = (0, 0)):
  vertices = [Vec3(-0.5, -0.5, 0), Vec3(0.5, -0.5, 0), Vec3(0.5, 0.5, 0), Vec3(-0.5, 0.5, 0)]
  offset_texture_scale = (texture_scale[0]/64, texture_scale[1]/64)
  texture_position = (texture_position[0]/64, 64-(texture_position[1]+texture_scale[1])/64)
  uvs = [
    (texture_position[0], texture_position[1]),
    (texture_position[0] + offset_texture_scale[0], texture_position[1]),
    (texture_position[0] + offset_texture_scale[0], texture_position[1] + offset_texture_scale[1]),
    (texture_position[0], texture_position[1] + offset_texture_scale[1])
  ]
  triangles = [(0, 1, 2), (0, 2, 3)]
  return Mesh(vertices=vertices, uvs=uvs, triangles=triangles)

head = [
  # Front face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (8, 8)),
    scale=(8, 8),
    position=(0, 0, 4),
    rotation=(0, 180, 0),
    texture=texture),
  # Back face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (24, 8)),
    scale=(8, 8),
    position=(0, 0, -4),
    rotation=(0, 0, 0),
    texture=texture),
  # Left face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (16, 8)),
    scale=(8, 8),
    position=(-4, 0, 0),
    rotation=(0, 90, 0),
    texture=texture),
  # Right face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (0, 8)),
    scale=(8, 8),
    position=(4, 0, 0),
    rotation=(0, -90, 0),
    texture=texture),
  # Top face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (8, 0)),
    scale=(8, 8),
    position=(0, 4, 0),
    rotation=(90, 180, 0),
    texture=texture),
  # Bottom face
  # FIXME: Bottom face UV is flipped on the X axis.
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (16, 0)),
    scale=(8, 8),
    position=(0, -4, 0),
    rotation=(-90, 0, 0),
    texture=texture)
]
for planes in head:
  planes.y += 10
hat = [
  # Front face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (32+8, 8)),
    scale=(8.5, 8.5),
    position=(0, 0, 4.25),
    rotation=(0, 180, 0),
    texture=texture),
  # Back face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (32+24, 8)),
    scale=(8.5, 8.5),
    position=(0, 0, -4.25),
    rotation=(0, 0, 0),
    texture=texture),
  # Left face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (32+16, 8)),
    scale=(8.5, 8.5),
    position=(-4.25, 0, 0),
    rotation=(0, 90, 0),
    texture=texture),
  # Right face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (32+0, 8)),
    scale=(8.5, 8.5),
    position=(4.25, 0, 0),
    rotation=(0, -90, 0),
    texture=texture),
  # Top face
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (32+8, 0)),
    scale=(8.5, 8.5),
    position=(0, 4.25, 0),
    rotation=(90, 180, 0),
    texture=texture),
  # Bottom face
  # FIXME: Bottom face UV is flipped on the X axis.
  Entity(model=create_plane(
    texture_scale = (8, 8),
    texture_position = (32+16, 0)),
    scale=(8.5, 8.5),
    position=(0, -4.25, 0),
    rotation=(-90, 0, 0),
    texture=texture)
]
for planes in hat:
  planes.y += 10
body = [
  # Front face
  Entity(model=create_plane(
    texture_scale = (8, 12),
    texture_position = (20, 20)),
    scale=(8, 12),
    position=(0, 0, 2),
    rotation=(0, 180, 0),
    texture=texture),
  # Back face
  Entity(model=create_plane(
    texture_scale = (8, 12),
    texture_position = (32, 20)),
    scale=(8, 12),
    position=(0, 0, -2),
    rotation=(0, 0, 0),
    texture=texture),
  # Left face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (16, 20)),
    scale=(4, 12),
    position=(-4, 0, 0),
    rotation=(0, 90, 0),
    texture=texture),
  # Right face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (28, 20)),
    scale=(4, 12),
    position=(4, 0, 0),
    rotation=(0, -90, 0),
    texture=texture),
  # Top face
  Entity(model=create_plane(
    texture_scale = (8, 4),
    texture_position = (20, 16)),
    scale=(8, 4),
    position=(0, 6, 0),
    rotation=(90, 180, 0),
    texture=texture),
  # Bottom face
  Entity(model=create_plane(
    texture_scale = (8, 4),
    texture_position = (28, 16)),
    scale=(8, 4),
    position=(0, -6, 0),
    rotation=(-90, 0, 0),
    texture=texture)
]
right_arm = [
  # Front face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (44, 20)),
    scale=(4, 12),
    position=(0, 0, 2),
    rotation=(0, 180, 0),
    texture=texture),
  # Back face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (52, 20)),
    scale=(4, 12),
    position=(0, 0, -2),
    rotation=(0, 0, 0),
    texture=texture),
  # Left face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (48, 20)),
    scale=(4, 12),
    position=(-2, 0, 0),
    rotation=(0, 90, 0),
    texture=texture),
  # Right face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (40, 20)),
    scale=(4, 12),
    position=(2, 0, 0),
    rotation=(0, -90, 0),
    texture=texture),
  # Top face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (44, 16)),
    scale=(4, 4),
    position=(0, 6, 0),
    rotation=(90, 180, 0),
    texture=texture),
  # Bottom face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (48, 16)),
    scale=(4, 4),
    position=(0, -6, 0),
    rotation=(-90, 0, 0),
    texture=texture)
]
for planes in right_arm:
  planes.x += 6
left_arm = [
  # Front face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (44, 20)),
    scale=(4, 12),
    position=(0, 0, 2),
    rotation=(0, 180, 0),
    texture=texture),
  # Back face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (52, 20)),
    scale=(4, 12),
    position=(0, 0, -2),
    rotation=(0, 0, 0),
    texture=texture),
  # Left face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (48, 20)),
    scale=(4, 12),
    position=(-2, 0, 0),
    rotation=(0, 90, 0),
    texture=texture),
  # Right face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (40, 20)),
    scale=(4, 12),
    position=(2, 0, 0),
    rotation=(0, -90, 0),
    texture=texture),
  # Top face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (44, 16)),
    scale=(4, 4),
    position=(0, 6, 0),
    rotation=(90, 180, 0),
    texture=texture),
  # Bottom face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (48, 16)),
    scale=(4, 4),
    position=(0, -6, 0),
    rotation=(-90, 0, 0),
    texture=texture)
]
for planes in left_arm:
  planes.x -= 6
left_leg = [
  # Front face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (4, 20)),
    scale=(4, 12),
    position=(0, 0, 2),
    rotation=(0, 180, 0),
    texture=texture),
  # Back face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (12, 20)),
    scale=(4, 12),
    position=(0, 0, -2),
    rotation=(0, 0, 0),
    texture=texture),
  # Left face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (8, 20)),
    scale=(4, 12),
    position=(-2, 0, 0),
    rotation=(0, 90, 0),
    texture=texture),
  # Right face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (0, 20)),
    scale=(4, 12),
    position=(2, 0, 0),
    rotation=(0, -90, 0),
    texture=texture),
  # Top face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (4, 16)),
    scale=(4, 4),
    position=(0, 6, 0),
    rotation=(90, 180, 0),
    texture=texture),
  # Bottom face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (8, 16)),
    scale=(4, 4),
    position=(0, -6, 0),
    rotation=(-90, 0, 0),
    texture=texture)
]
for planes in left_leg:
  planes.x -= 2
  planes.y -= 12
right_leg = [
  # Front face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (4, 20)),
    scale=(4, 12),
    position=(0, 0, 2),
    rotation=(0, 180, 0),
    texture=texture),
  # Back face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (12, 20)),
    scale=(4, 12),
    position=(0, 0, -2),
    rotation=(0, 0, 0),
    texture=texture),
  # Left face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (8, 20)),
    scale=(4, 12),
    position=(-2, 0, 0),
    rotation=(0, 90, 0),
    texture=texture),
  # Right face
  Entity(model=create_plane(
    texture_scale = (4, 12),
    texture_position = (0, 20)),
    scale=(4, 12),
    position=(2, 0, 0),
    rotation=(0, -90, 0),
    texture=texture),
  # Top face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (4, 16)),
    scale=(4, 4),
    position=(0, 6, 0),
    rotation=(90, 180, 0),
    texture=texture),
  # Bottom face
  Entity(model=create_plane(
    texture_scale = (4, 4),
    texture_position = (8, 16)),
    scale=(4, 4),
    position=(0, -6, 0),
    rotation=(-90, 0, 0),
    texture=texture)
]
for planes in right_leg:
  planes.x += 2
  planes.y -= 12