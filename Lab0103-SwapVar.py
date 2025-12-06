"""
Docstring for Lab0103-SwapVar
"""

def convert_string_to_tuples(text_in):
  """
  Docstring for convert_string_to_tuples
  """
  values = text_in.strip('()').split(', ')
  X = values[-1]
  Y = values[0]
  values[0] = X
  values[-1] = Y
  return tuple(map(float, values))

laongdao_data = convert_string_to_tuples(input())
print(laongdao_data)
