import random

screen_width = 800
screen_height = 600
title = 'UNILAG Navigation System'

node = {}
node['size'] = 9
node['outline_color'] = (10, 10, 10)
node['connector_color'] = (180, 180, 180)
node['path_color'] = (100, 230, 60)
node['clicked_color'] = (30, 80, 230)
node['highlight_color'] = (200, 100, 170)
node['outline_width'] = 3
path_length = 75

nodes = [
  'Gate', 'UBA Park', 'Faculty of Education', 'Faculty of Environmental Science', 'Wema Bank',
  'Catholic Church', 'Multipurpose Hall', 'Chapel', 'Mosque', 'Sports Centre',
  '2001 Cafeteria', 'Amphitheatre', 'Sodeinde Hall', 'Forte Oil', 'Access Bank', 
  'Makama Hall', 'Eni-Njoku Hall', 'MTH', 'YemYem Supermarket', 'Fagunwa Hall', 
  'Shuttle Park', 'Fire Station', 'Power Station', 'Faculty of Arts', 'Senate',
  'UNILAG Bookshop', 'Ecobank', 'Afe Babalola Hall', 'CITS'
]

graph = {}

def connect(a, b, weight, rotation=0):
  graph.setdefault(a, {})
  graph[a][b] = (0.5 + random.random() * 1, rotation + random.randrange(-45, 45))
  # graph[a][b] = (weight, rotation)

# handle left side of the road
connect('Gate', 'UBA Park', 0.2, -75)
connect('UBA Park', 'Faculty of Environmental Science', 0.4, 0)
connect('Faculty of Environmental Science', 'Catholic Church', 0.4, 0)
connect('Catholic Church', 'Chapel', 0.4, 0)
connect('Chapel', 'Mosque', 0.4, 0)
connect('Mosque', '2001 Cafeteria', 0.4, 0)
connect('2001 Cafeteria', 'MTH', 0.4, 0)
connect('MTH', 'Fagunwa Hall', 0.4, 0)
connect('Fagunwa Hall', 'Makama Hall', 0.4, 0)
connect('Makama Hall', 'Sodeinde Hall', 0.4, 0)
connect('Sodeinde Hall', 'Eni-Njoku Hall', 0.4, 0)
connect('Eni-Njoku Hall', 'Fire Station', 0.4, 0)
connect('Fire Station', 'Power Station', 0.4, 0)
connect('Power Station', 'Faculty of Arts', 0.4, 0)
connect('Faculty of Arts', 'Senate', 0.4, 0)

# handle right side of the road
connect('Gate', 'Faculty of Education', 0.3, 55)
connect('Faculty of Education', 'Multipurpose Hall', 0.4, 0)
connect('Multipurpose Hall', 'Wema Bank', 0.4, 0)
connect('Wema Bank', 'Sports Centre', 0.4, -15)
connect('Sports Centre', 'Amphitheatre', 0.4, -10)
connect('Amphitheatre', 'Forte Oil', 0.4, 10)
connect('Forte Oil', 'Access Bank', 0.4, 0)
connect('Access Bank', 'YemYem Supermarket', 0.4, 0)
connect('YemYem Supermarket', 'Shuttle Park', 0.4, 0)
connect('Shuttle Park', 'CITS', 0.4, 0)
connect('CITS', 'Afe Babalola Hall', 0.4, 0)
connect('Afe Babalola Hall', 'Ecobank', 0.4, 0)
connect('Ecobank', 'UNILAG Bookshop', 0.4, 0)
connect('UNILAG Bookshop', 'Senate', 0.4, 30)

connect('UBA Park', 'Faculty of Education', 0.1)
connect('Wema Bank', 'Faculty of Environmental Science', 0.1)