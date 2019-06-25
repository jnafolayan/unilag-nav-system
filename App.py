import arcade
from Node import Node
from findpath import find_path
import math

class App(arcade.Window):
  def __init__(self, options):
    super().__init__(options.screen_width, options.screen_height, options.title)

    arcade.set_background_color(arcade.color.WHITE)
    self.options = options
    self.entities = []
    self.nodeMap = {}
    self.time = 0

    self.start_node = None
    self.end_node = None
    self.path = None
    self.path_cursor = 0
    self.next_cursor_time = 0

    # camera vars
    self.view_x = 0
    self.view_y = 0
    self.world_w = 0
    self.world_h = 0
    self.view_target = None

  def add_entity(self, obj):
    obj.set_app(self)
    self.entities.append(obj)

  def generate_nodes(self):
    options = self.options
    start = None

    # create the nodes
    for key in options.nodes:
      node = Node(key = key)
      if not start:
        start = node
      self.nodeMap[key] = node
      self.add_entity(node)

    start.x = options.screen_width / 2
    start.y = options.node['size'] * 2

    # connect them
    for key_a in options.graph:
      for key_b in options.graph[key_a]:
        node_a = self.get_node_by_key(key_a)
        node_b = self.get_node_by_key(key_b)
        weight, rotation = options.graph[key_a][key_b]
        node_a.connect(node_b, weight, options.path_length, rotation)

    # get boundaries
    max_y = -10
    for node in self.entities:
      if node.y > max_y:
        max_y = node.y

    self.world_h = max_y

  def get_node_by_key(self, key):
    return self.nodeMap[key]

  def start(self):
    arcade.run()

  def on_draw(self):
    arcade.start_render()

    for obj in self.entities:
      obj.draw_connectors(arcade)

    for obj in self.entities:
      obj.draw(arcade)

  def update(self, dt):
    for obj in self.entities:
      obj.update(dt, arcade)

    if self.start_node and self.end_node and not self.path:
      # clear previous node flags
      for obj in self.entities:
        obj.is_in_path = False
        obj.walked = False
        obj.is_terminal = False

      self.path = find_path(self.start_node, self.end_node)
      self.path_cursor = -1
      self.next_cursor_time = 0
      self.start_node.is_terminal = True
      self.end_node.is_terminal = True

      for key in self.path:
        node = self.get_node_by_key(key)
        node.is_in_path = True

    if self.path:
      self.next_cursor_time -= dt

      if self.next_cursor_time <= 0:
        self.path_cursor += 1
        self.next_cursor_time = 0.8
        if self.path_cursor == len(self.path):
          self.path_cursor -= 1
        node = self.get_node_by_key(self.path[self.path_cursor])
        node.walked = True
        self.view_target = node

    # update viewport
    if self.view_target:
      dx = (self.view_target.x - self.options.screen_width / 2) - self.view_x
      dy = (self.view_target.y - self.options.screen_height / 2) - self.view_y
      lerp = 0.89
      self.view_x += dx * lerp
      self.view_y += dy * lerp

    arcade.set_viewport(self.view_x, 
                        self.view_x + self.options.screen_width - 1, 
                        self.view_y, 
                        self.view_y + self.options.screen_height - 1)

  def on_mouse_motion(self, x, y, dx, dy):
    x += self.view_x
    y += self.view_y

    for obj in self.entities:
      dist = math.sqrt((x - obj.x) ** 2 + (y - obj.y) ** 2)
      if dist < self.options.node['size']:
        obj.on_mouse_motion()
      elif obj.mouse_over:
        obj.on_mouse_leave()

  def on_mouse_press(self, x, y, button, modifiers):
    x += self.view_x
    y += self.view_y
    
    # clear flags
    for obj in self.entities:
      dist = math.sqrt((x - obj.x) ** 2 + (y - obj.y) ** 2)
      if dist <= self.options.node['size']:
        if obj.mouse_down:
          continue
        obj.on_mouse_press()
        if not self.start_node:
          self.start_node = obj
        elif not self.end_node:
          self.end_node = obj
      elif obj.mouse_down:
        obj.on_mouse_release()

  def on_key_press(self, key, modifiers):
    speed = 50

    if key == arcade.key.LEFT:
      self.view_x -= speed
    elif key == arcade.key.RIGHT:
      self.view_x += speed
    elif key == arcade.key.UP:
      self.view_y += speed
    elif key == arcade.key.DOWN:
      self.view_y -= speed

    self.view_target = None