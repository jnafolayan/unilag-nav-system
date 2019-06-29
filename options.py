import random

screen_width = 800
screen_height = 600
title = 'UNILAG Navigation System'

node = {}
node['size'] = 7
node['outline_color'] = (10, 10, 10)
node['connector_color'] = (180, 180, 180)
node['path_color'] = (100, 230, 60)
node['clicked_color'] = (30, 80, 230)
node['highlight_color'] = (200, 100, 170)
node['outline_width'] = 3
path_length = 150

main_nodes = [
  'Gate', 'UBA Park', 'Faculty of Education', 'Faculty of Environmental Science', 'Wema Bank',
  'Catholic Church', 'Multipurpose Hall', 'Chapel', 'Mosque', 'Sports Centre',
  '2001 Cafeteria', 'Amphitheatre', 'Sodeinde Hall', 'Forte Oil', 'Access Bank', 
  'Makama Hall', 'Eni-Njoku Hall', 'MTH', 'YemYem Supermarket', 'Fagunwa Hall', 
  'Shuttle Park', 'Fire Station', 'Power Station', 'Faculty of Arts', 'Senate',
  'UNILAG Bookshop', 'Ecobank', 'Afe Babalola Hall', 'CITS', '2nd Gate', 
  '1st Bank', 'Staff Quarters'
]

graph = {}

def connect(a, b, weight, rotation=0):
  graph.setdefault(a, {})
  graph[a][b] = (weight, rotation)

# handle left side of the road
connect('Gate', 'UBA Park', 0.4, -75)
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
connect('Gate', 'Faculty of Education', 0.4, 55)
connect('Faculty of Education', 'Multipurpose Hall', 0.4, 0)
connect('Multipurpose Hall', 'Wema Bank', 0.4, 0)
connect('Multipurpose Hall', 'Henry Karr Hostel', 0.4, 0)
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

# connect left to right
connect('UBA Park', 'Faculty of Education', 0.2)
connect('Wema Bank', 'Faculty of Environmental Science', 0.2)
connect('Amphitheatre', 'Chapel', 0.2)
connect('Access Bank', '2001 Cafeteria', 0.2)
connect('CITS', 'Fire Station', 0.2)


connect('Access Bank', 'FSS Complex', 0.6, 170)
connect('Forte Oil', 'FSS Complex', 0.5, 90)
connect('FSS Complex', 'FSS', 0.4, 90)
connect('FSS', '1st Bank', 0.6, 90)

connect('Faculty of Education', 'El Kanemi', 0.3, 90)
connect('El Kanemi', 'Amina Hostel', 0.3, 90)
connect('Amina Hostel', 'Kofo Hostel', 0.3, 90)
connect('Kofo Hostel', 'Biobaku Hostel', 0.3, 90)
connect('Biobaku Hostel', 'Staff Quarters', 0.5, 35)
connect('Staff Quarters', '1st Bank', 0.5, 35)

connect('1st Bank', 'HRDC Building', 0.6, 160)
connect('HRDC Building', '2nd Gate', 0.6, 175)

connect('1st Bank', 'DLI', 1.2, 80)
connect('DLI', 'Honours Hostel', 0.4, 90)
connect('DLI', 'Medical Centre', 1.3, -30)
connect('Medical Centre', 'ULS', 0.4, -5)
connect('ULS', 'Staff School', 0.4, -45)

connect('Afe Babalola Hall', 'Dept of Mass Comm', 0.2, 100)
connect('Dept of Mass Comm', 'Moremi Hostel', 0.2, 90)
connect('Moremi Hostel', 'Campus Car Park', 0.2, 0)
connect('Campus Car Park', 'Mariere Hostel', 0.4, 0)
connect('Campus Car Park', 'Erastus Akingbola Hostel', 0.2, 30)
connect('Erastus Akingbola Hostel', 'GTBank', 0.2, 90)
connect('GTBank', 'Jaja Hostel', 0.3, 90)
connect('Jaja Hostel', 'Faculty of Science', 0.7, 10)
connect('Jaja Hostel', 'Staff School', 0.25, 165)
connect('Staff School', 'Faculty of Science', 0.8, 0)

#2ND Gate of Unilag : Handle Right side of the Road
# connect('2nd Gate', 'ISI Unilag', 0.5, 70)
# connect('ISI Unilag', 'DLI', 0.5, 0)
