# Add new functionality to an existing object without altering its structure
# This pattern creates a decorator class which wraps the original class,
# and provides additional functionality keeping class methods signature intact.
import time

def to_num(numStr):
  return int(numStr.replace(',', ''))

# Decorator
def time_this(func):

  def decorated(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print('Raining in', time.time() - start, 'seconds')
    return result

  return decorated

@time_this
def count(until):
  print('Counting to', until, '...')

  num = 0
  for i in range(to_num(until)):
    num += 1
  return num

for num in ("10,000", "100,000", "1,000,000"):
  print(count(num))
  print('-' * 20)
