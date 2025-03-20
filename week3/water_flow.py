def water_column_height(tower_height, tank_height):
  height_water_column = tower_height + ((3 * tank_height) / 4)
  return height_water_column

def pressure_gain_from_water_height(height):
  p = 998.2
  g = 9.80665
  kilopascals = (p * g * height) / 1000
  return kilopascals

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):  
  p = 998.2
  kilopascals = -1 * (friction_factor * pipe_length * p * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
  return kilopascals