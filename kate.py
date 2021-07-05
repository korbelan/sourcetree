import math


x0 = -163419
y0 = 5285 * 10
x_middle = 11845
y_middle = 1648 * 10
x100 = 124210
y100 = 8576 * 10
r_y0 = 0
r_x0 = 0
r = 0

def get_circle_radius_and_center( x0,  y0,  x_middle,  y_middle,  x100,  y100,  r_y0,  r_x0,  r):
  a = x_middle - x0
  b = y_middle - y0
  c = x100 - x0
  d = y100 - y0
  e = a * (x0 + x_middle) + b * (y0 + y_middle)
  f = c * (x0 + x100) + d * (y0 + y100)
  g = 2 * (a * (y100 - y_middle) - b * (x100 - x_middle))
  r_x0 = (d * e - b * f) / g
  r_y0 = (a * f - c * e) / g
  r = math.sqrt((x0 - r_x0) * (x0 - r_x0) + (y0 - r_y0) * (y0 - r_y0))
  return r_x0, r_y0, r


def get_AUX_from_main_pos( r_x0,  r_y0,  r,  main_pos):
  aux_pos_1 = r_y0 + math.sqrt(r * r - (main_pos - r_x0) * (main_pos - r_x0))
  if ()
  print("aux_pos_1 = ")
  print(aux_pos_1)
  aux_pos_2 = r_y0 - math.sqrt(r * r - (main_pos - r_x0) * (main_pos - r_x0))
  print("aux_pos_2 = ")
  print(aux_pos_2)
  #return aux_pos_1


r_x0, r_y0, r = get_circle_radius_and_center(x0,  y0,  x_middle,  y_middle,  x100,  y100,  r_y0,  r_x0,  r)

main_step = (x100 - x0) / 10
cur_main = 0
print("x0")
print(r_x0)
print("y0")
print(r_y0)
print(r)
for i in range(11):
    print("----------------------")
    cur_main = x0 + main_step * i
    print("cur_main")
    print(cur_main)
    print("pos = ")
    print(i)
    print("aux pos = ")
    get_AUX_from_main_pos(r_x0, r_y0, r, cur_main)
    
        
