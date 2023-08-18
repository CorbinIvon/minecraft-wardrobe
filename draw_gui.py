from ursina import *
from tkinter import filedialog
import os
app = Ursina()
from draw_crafter import *

# Position the camera
editor_camera = EditorCamera()
editor_camera.rotation = (0, 180, 0)  # Rotate the camera 180 degrees around the Y-axis

# Disable FPS Counter
window.fps_counter.enabled = False
window.size = (1280, 720)


# Create a UI element that sits on the right of the screen.
def reapply_texture():
  for body_group in steve_texture_map.steve_uv_data:
    for face in steve_texture_map.steve_uv_data[body_group]:
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].texture = texture
def disable_body_group(group: str):
  # Get the body group from the text input
  body_group = group
  # If the body group is not in the steve_uv_data dictionary, return
  if body_group not in steve_texture_map.steve_uv_data:
    return
  # Iterate through all the faces in the body group
  for face in steve_texture_map.steve_uv_data[body_group]:
    # Disable the face
    steve_texture_map.steve_uv_data[body_group][face]['mesh'].enabled = False
def enable_body_group(group: str):
  # Get the body group from the text input
  body_group = group
  # If the body group is not in the steve_uv_data dictionary, return
  if body_group not in steve_texture_map.steve_uv_data:
    return
  # Iterate through all the faces in the body group
  for face in steve_texture_map.steve_uv_data[body_group]:
    # Enable the face
    steve_texture_map.steve_uv_data[body_group][face]['mesh'].enabled = True
def toggle_body_group(group: str, button: Button):
  # Get the body group from the text input
  # Get group delimiter ,
  body_groups = group.split(',')
  # If the body group is not in the steve_uv_data dictionary, return
  for body_group in body_groups:
    if body_group not in steve_texture_map.steve_uv_data:
      return
    # Iterate through all the faces in the body group
    if not steve_texture_map.steve_uv_data[body_group]['front']['mesh'].enabled:
      button.color = color.azure
    else:
      button.color = color.red
    for face in steve_texture_map.steve_uv_data[body_group]:
      # Toggle the face
      steve_texture_map.steve_uv_data[body_group][face]['mesh'].enabled = not steve_texture_map.steve_uv_data[body_group][face]['mesh'].enabled
def switch_texture():
  global texture, texture_index
  # Increment texture_index by 1
  texture_index += 1
  # If texture_index is greater than the length of the textures list, reset it to 0
  if texture_index > len(textures) - 1:
    texture_index = 0
  # Set texture to the texture at the index of texture_index in the textures list
  texture = textures[texture_index]
  reapply_texture()
def import_texture():
  global texture
  # Open a file dialog to select a texture
  # The path of this script is the initial directory
  new_texture = filedialog.askopenfilename(initialdir=os.path.dirname(__file__), title='Select a texture', filetypes=(('PNG', '*.png'), ('JPG', '*.jpg'), ('All Files', '*.*')))
  if new_texture == '':
    return
  # Strip the file until 'resources' to get the path to the texture
  new_texture = new_texture[new_texture.find('resources'):]
  # Append texture to texture list
  textures.append(new_texture)
  # Set the texture of all the faces to the selected texture
  switch_texture()

textControlsHints = Text(text='Right click = Rotate | Middle Mouse = Pan | Scroll = Zoom', color=color.white, scale=(0.75, 0.75), x=-0.6, y=-0.45, origin=(0, 0.5))
rightBackgroundPanel = Entity(parent=camera.ui, model='quad', texture='', scale=(0.35, 1), x=0.72, y=0, origin=(0, 0), color=color.gray)
appTitle = Text(parent=rightBackgroundPanel, text='Minecraft\nWardrobe', color=color.white, scale=(7, 3) , x=0, y=0.4, origin=(0, 0))
# buttonSwitchTexture = Button(parent=camera.ui, text='Switch Texture', color=color.azure, scale=(0.75, 0.05), x=0, y=0.3, origin=(0, 0.5), on_click=switch_texture)
# buttonImportTexture = Button(parent=camera.ui, text='Import Texture', color=color.azure, scale=(0.75, 0.05), x=0, y=0.2, origin=(0, 0.5), on_click=import_texture)

buttonXOffsetInPixels = 520
buttonYOffsetInPixels = -150
buttonScaleMultiplier = 8
buttonSpacing = 5
buttonToggleBody = Button(
  parent=camera.ui,
  color=color.azure,
  scale=((steve_texture_map.steve_uv_data['body']['front']['pixel_size'][0] * buttonScaleMultiplier)/720, (steve_texture_map.steve_uv_data['body']['front']['pixel_size'][1] * buttonScaleMultiplier)/720),
  position=((buttonXOffsetInPixels)/720, (buttonYOffsetInPixels)/720),
  origin=(0,0),
  on_click=lambda: toggle_body_group('body,coat', buttonToggleBody)
)
buttonToggleHead = Button(
  parent=camera.ui,
  color=color.azure,
  scale=((steve_texture_map.steve_uv_data['head']['front']['pixel_size'][0] * buttonScaleMultiplier)/720, (steve_texture_map.steve_uv_data['head']['front']['pixel_size'][1] * buttonScaleMultiplier)/720),
  position=((buttonXOffsetInPixels)/720, (10 * buttonScaleMultiplier + buttonSpacing + buttonYOffsetInPixels)/720),
  origin=(0,0),
  on_click=lambda: toggle_body_group('head,hat', buttonToggleHead)
)
buttonToggleLeftArm = Button(
  parent=camera.ui,
  color=color.azure,
  scale=((steve_texture_map.steve_uv_data['left_arm']['front']['pixel_size'][0] * buttonScaleMultiplier)/720, (steve_texture_map.steve_uv_data['left_arm']['front']['pixel_size'][1] * buttonScaleMultiplier)/720),
  position=((buttonXOffsetInPixels + (6 * buttonScaleMultiplier + buttonSpacing))/720, (0 * buttonScaleMultiplier + buttonYOffsetInPixels)/720),
  origin=(0,0),
  on_click=lambda: toggle_body_group('left_arm,left_sleeve', buttonToggleLeftArm)
)
buttonToggleRightArm = Button(
  parent=camera.ui,
  color=color.azure,
  scale=((steve_texture_map.steve_uv_data['right_arm']['front']['pixel_size'][0] * buttonScaleMultiplier)/720, (steve_texture_map.steve_uv_data['right_arm']['front']['pixel_size'][1] * buttonScaleMultiplier)/720),
  position=((buttonXOffsetInPixels - (6 * buttonScaleMultiplier + buttonSpacing))/720, (0 * buttonScaleMultiplier + buttonYOffsetInPixels)/720),
  origin=(0,0),
  on_click=lambda: toggle_body_group('right_arm,right_sleeve', buttonToggleRightArm)
)
buttonToggleLeftLeg = Button(
  parent=camera.ui,
  color=color.azure,
  scale=((steve_texture_map.steve_uv_data['left_leg']['front']['pixel_size'][0] * buttonScaleMultiplier - 1)/720, (steve_texture_map.steve_uv_data['left_leg']['front']['pixel_size'][1] * buttonScaleMultiplier)/720),
  position=((buttonXOffsetInPixels + (2 * buttonScaleMultiplier))/720, (-12 * buttonScaleMultiplier - buttonSpacing + buttonYOffsetInPixels)/720),
  origin=(0,0),
  on_click=lambda: toggle_body_group('right_leg,right_pants_leg', buttonToggleLeftLeg)
)
buttonToggleRightLeg = Button(
  parent=camera.ui,
  color=color.azure,
  scale=((steve_texture_map.steve_uv_data['right_leg']['front']['pixel_size'][0] * buttonScaleMultiplier - 1)/720, (steve_texture_map.steve_uv_data['right_leg']['front']['pixel_size'][1] * buttonScaleMultiplier)/720),
  position=((buttonXOffsetInPixels - (2 * buttonScaleMultiplier))/720, (-12 * buttonScaleMultiplier - buttonSpacing + buttonYOffsetInPixels)/720),
  origin=(0,0),
  on_click=lambda: toggle_body_group('left_leg,left_pants_leg', buttonToggleRightLeg)
)

# Create the skin control buttons. These buttons will represent the Minecraft character with 2 buttons side by side that enable / disable the outer layer and inner layer.


# Run the application
app.run()