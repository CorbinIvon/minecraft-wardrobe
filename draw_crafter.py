from ursina import *
import steve_texture_map

# Map easier with this: https://pixspy.com/

texture_index = 0
textures = ['resources/TextureGridAssistant', 'resources/Corbin-Engineer01.png']
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

for body_group in steve_texture_map.steve_uv_data:
  isOuterFace = True if body_group == 'hat' or body_group == 'coat' or body_group == 'left_sleeve' or body_group == 'right_sleeve' or body_group == 'left_pants_leg' or body_group == 'right_pants_leg' else False
  for face in steve_texture_map.steve_uv_data[body_group]:
    steve_texture_map.steve_uv_data[body_group][face]['mesh'] = Entity(
      model=create_plane(steve_texture_map.steve_uv_data[body_group][face]['pixel_size'], steve_texture_map.steve_uv_data[body_group][face]['start_pixel']),
      texture=texture,
      scale=(
        steve_texture_map.steve_uv_data[body_group][face]['pixel_size'][0] * (1.0625 if isOuterFace else 1),
        steve_texture_map.steve_uv_data[body_group][face]['pixel_size'][1] * (1.0625 if isOuterFace else 1)
      ),
      position=(
        # X relative to the front face
        -steve_texture_map.steve_uv_data[body_group]['front']['pixel_size'][0]/2 * (1.0625 if isOuterFace else 1) if face == 'left' else steve_texture_map.steve_uv_data[body_group]['front']['pixel_size'][0]/2 * (1.0625 if isOuterFace else 1) if face == 'right' else 0,
        # Y relative to the front face
        steve_texture_map.steve_uv_data[body_group]['front']['pixel_size'][1]/2 * (1.0625 if isOuterFace else 1) if face == 'top' else -steve_texture_map.steve_uv_data[body_group]['front']['pixel_size'][1]/2 * (1.0625 if isOuterFace else 1) if face == 'bottom' else 0,
        # Z relative to the left face
        steve_texture_map.steve_uv_data[body_group]['left']['pixel_size'][0]/2 * (1.0625 if isOuterFace else 1) if face == 'front' else -steve_texture_map.steve_uv_data[body_group]['left']['pixel_size'][0]/2 * (1.0625 if isOuterFace else 1) if face == 'back' else 0
        ),
      rotation=(
        90 if face == 'top' else -90 if face == 'bottom' else 0,
        180 if face == 'front' else 90 if face == 'left' else -90 if face == 'right' else 0,
        180 if face == 'top' or face == 'bottom' else 0
      )
    )
  # Move the head group up by 10 units.
  if body_group == 'head' or body_group == 'hat':
    for face in steve_texture_map.steve_uv_data[body_group]:
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].y += 10
  if body_group == 'left_arm' or body_group == 'left_sleeve':
    for face in steve_texture_map.steve_uv_data[body_group]:
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].x -= (steve_texture_map.steve_uv_data['body']['front']['pixel_size'][0] + steve_texture_map.steve_uv_data['left_arm']['front']['pixel_size'][0])/2
  if body_group == 'right_arm' or body_group == 'right_sleeve':
    for face in steve_texture_map.steve_uv_data[body_group]:
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].x += (steve_texture_map.steve_uv_data['body']['front']['pixel_size'][0] + steve_texture_map.steve_uv_data['left_arm']['front']['pixel_size'][0])/2
  if body_group == 'left_leg' or body_group == 'left_pants_leg':
    for face in steve_texture_map.steve_uv_data[body_group]:
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].x += 2
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].y -= 12
  if body_group == 'right_leg' or body_group == 'right_pants_leg':
    for face in steve_texture_map.steve_uv_data[body_group]:
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].x -= 2
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].y -= 12