class Entity:
  """
  " This is the base class for everything that will be
  " rendered onto the screen.
  """
  def __init__(self):
    self.app = None
    self.mouse_over = False
    self.mouse_down = False

  def set_app(self, app):
    self.app = app

  def on_mouse_motion(self):
    self.mouse_over = True

  def on_mouse_leave(self):
    self.mouse_over = False

  def on_mouse_press(self):
    self.mouse_down = True

  def on_mouse_release(self):
    self.mouse_down = False
