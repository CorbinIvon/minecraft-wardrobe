from ursina import *

app = Ursina()

scale_head = (8, 8, 8)
scale_body = (8, 12, 4)
scale_arms = (4, 12, 4) # Steve
# scale_arms = (3, 12, 4) # Alex
scale_legs = (4, 12, 4)

# Load the texture
player_texture = load_texture('resources/steve_template.png')

# Head
head = Entity(model='cube', scale=scale_head, position=(0, scale_body[1]/2 + scale_head[1]/2, 0), texture=player_texture)

# Body
body = Entity(model='cube', scale=(8, 12, 4), position=(0, 0, 0), texture=player_texture)

# Arms
left_arm = Entity(model='cube', scale=scale_arms, position=(-(scale_body[0]/2+scale_arms[0]/2),0,0), texture=player_texture)
right_arm = Entity(model='cube', scale=scale_arms, position=((scale_body[0]/2+scale_arms[0]/2),0,0), texture=player_texture)

# Legs
left_leg = Entity(model='cube', scale=scale_legs, position=(-scale_body[0]/4,-(scale_body[1]/2+scale_legs[1]/2),0), texture=player_texture)
right_leg = Entity(model='cube', scale=scale_legs, position=(scale_body[0]/4,-(scale_body[1]/2+scale_legs[1]/2),0), texture=player_texture)

# Editor Camera
editor_camera = EditorCamera()

# Disable FPS Counter
window.fps_counter.enabled = False

app.run()