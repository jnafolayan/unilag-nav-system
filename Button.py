from Entity import Entity

class Button(Entity):
  def __init__(self, text, width, height, fill, text_color, font_size, action):
    super().__init__()

    self.text = text
    self.width = width
    self.height = height
    self.fill = fill
    self.text_color = text_color
    self.font_size = font_size
    self.action = action

  def draw(self, arcade):
    arcade.draw_lrtb_rectangle_outline(self.x, self.x + self.width, self.y + self.height, self.y, (0,0,0))
    arcade.draw_text(self.text, self.x + 10, self.y + 10, self.text_color, self.font_size)

  def on_mouse_press(self):
    super().on_mouse_press()
    self.action()