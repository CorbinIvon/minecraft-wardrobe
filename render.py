from ursina import *
from render_data import *

app = Ursina()

# Define custom cube with modified UVs
class CustomCube(Entity):
  def __init__(self, **kwargs):
    super().__init__()
    self.model = Mesh(
      vertices=head.vertices,
      triangles=head.triangles,
      uvs=head.uvs,
      normals=[],
    )
    for key, value in kwargs.items():
      setattr(self, key, value)



scale_body = (8, 12, 4)
scale_arms = (4, 12, 4) # Steve
# scale_arms = (3, 12, 4) # Alex
scale_legs = (4, 12, 4)

# Load the texture
player_texture = load_texture(texture)

# Head
head = CustomCube(
  position=(0, scale_body[1]/2 + head.volume_z/2, 0),
  texture=player_texture,
)

# Body
body = Entity(model='cube', scale=scale_body, position=(0, 0, 0), texture=player_texture)

# Arms
left_arm = Entity(model='cube', scale=scale_arms, position=(-(scale_body[0]/2+scale_arms[0]/2),0,0), texture=player_texture)
right_arm = Entity(model='cube', scale=scale_arms, position=((scale_body[0]/2+scale_arms[0]/2),0,0), texture=player_texture)

# Legs
left_leg = Entity(model='cube', scale=scale_legs, position=(-scale_body[0]/4,-(scale_body[1]/2+scale_legs[1]/2),0), texture=player_texture)
right_leg = Entity(model='cube', scale=scale_legs, position=(scale_body[0]/4,-(scale_body[1]/2+scale_legs[1]/2),0), texture=player_texture)

# Editor Camera
editor_camera = EditorCamera()
editor_camera.rotation = (0, 180, 0)  # Rotate the camera 180 degrees around the Y-axis


# Disable FPS Counter
window.fps_counter.enabled = False

app.run()