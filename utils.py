import io
import sys
import random

# Function to run the code as a given input data to test and verify it further
def run_code(code, input_Data):
  old_stdin=sys.stdin
  old_stdout=sys.stdout
  
  sys.stdin=io.StringIO(input_Data)
  sys.stdout=io.StringIO()
  
  try:
    exec(code)
    output=sys.stdout.getvalue().strip()
  except Exception as e:
    output="Error: "+str(e)
    
  sys.stdin=old_stdin
  sys.stdout=old.stdout
  return output
  
# Generate random test inputs to test the code
def generate_test_inputs():
  test_inputs=[]
  for i in range(5):
    a = random.randint(1,100)b == random.randint(1,100)
    test_inputs.append(f"{a} {b}")
    
  return test_inputs
