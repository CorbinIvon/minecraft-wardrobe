from ursina import *
from tkinter import filedialog
import os
app = Ursina()
from draw_crafter import *

# Create a UI element that sits on the right of the screen.
def create_right_panel():
  panel = Entity(parent=camera.ui, model='quad', texture='', scale=(0.35, 1), x=0.72, y=0, origin=(0, 0), color=color.gray)
  return panel
right_panel = create_right_panel()
# Create a button to switch between textures
def switch_texture():
  global texture, texture_index
  # Increment texture_index by 1
  texture_index += 1
  # If texture_index is greater than the length of the textures list, reset it to 0
  if texture_index > len(textures) - 1:
    texture_index = 0
  # Set texture to the texture at the index of texture_index in the textures list
  texture = textures[texture_index]
  for face in head:
    face.texture = texture
  for face in body:
    face.texture = texture
  for face in left_arm:
    face.texture = texture
  for face in right_arm:
    face.texture = texture
  for face in left_leg:
    face.texture = texture
  for face in right_leg:
    face.texture = texture
header = Text(text='Minecraft\nWardrobe', color=color.white, scale=(7, 3) , x=0, y=0.4, parent=right_panel, origin=(0, 0))
button = Button(text='Switch Texture', color=color.azure, scale=(0.75, 0.05), x=0, y=0.3, parent=right_panel, origin=(0, 0.5), on_click=switch_texture)
controls = Text(text='Right click = Rotate | Middle Mouse = Pan | Scroll = Zoom', color=color.white, scale=(0.75, 0.75), x=-0.6, y=-0.45, origin=(0, 0.5))

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
button = Button(text='Import Texture', color=color.azure, scale=(0.75, 0.05), x=0, y=0.2, parent=right_panel, origin=(0, 0.5), on_click=import_texture)






editor_camera = EditorCamera()
editor_camera.rotation = (0, 180, 0)  # Rotate the camera 180 degrees around the Y-axis

# Disable FPS Counter
window.fps_counter.enabled = False

# Run the application
app.run()