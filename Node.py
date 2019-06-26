from Entity import Entity
import math

class Node(Entity):
  """
  " A node is a location on the map. It has x/y coords
  " along with a unique key describing its name on the
  " map
  " 
  " @param {str} key - the name of the node on the map
  " @param {int} x - the x coord on the map
  " @param {int} y - the y coord on the map
  """
  def __init__(self, key, x=0, y=0):
    super().__init__()

    self.x = x
    self.y = y
    self.type = 'node'
    self.key = key
    self.cost = float('inf')
    self.neighbors = []
    self.parent = None
    self.rotation = 0
    self.is_in_path = False
    self.walked = False
    self.is_terminal = False

  def connect(self, node, weight, scale, rotation=0):    
    if not node.parent and node.key != 'Gate':
      rotation = math.radians(rotation) - math.pi / 2
      node.x = self.x + math.cos(rotation) * scale * weight
      node.y = self.y - math.sin(rotation) * scale * weight
      node.parent = self

    self.neighbors.append((node, weight))
    node.neighbors.append((self, weight))

  def draw_connectors(self, arcade):
    options = self.app.options
    radius = options.node['size']
    width = options.node['outline_width']

    # draw connector lines
    for node, weight in self.neighbors:
      color = options.node['connector_color']
      if self.is_in_path and node.is_in_path and node.walked:
        color = options.node['path_color']
      arcade.draw_line(self.x, self.y, node.x, node.y, color, width)

  def draw(self, arcade):
    options = self.app.options
    radius = options.node['size']
    color = options.node['outline_color']
    width = options.node['outline_width']
    fill = arcade.color.WHITE

    if self.mouse_down or self.is_terminal:
      fill = options.node['clicked_color']
    elif self.mouse_over:
      fill = options.node['highlight_color']
    
    if self.walked and not self.is_terminal:
      fill = options.node['path_color']

    arcade.draw_circle_filled(self.x, self.y, radius, fill)
    
    if not self.walked or self.is_terminal:
      arcade.draw_circle_outline(self.x, self.y, radius, color, width)

    if self.mouse_over or self.walked:
      arcade.draw_text(self.key, self.x - len(self.key) * 3, self.y + radius * 1.5, color, 12)

  def update(self, dt, arcade):
    pass