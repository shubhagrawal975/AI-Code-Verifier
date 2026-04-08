from utils import run_code, generate_test_inputs

def verify_code(user_code, reference_code):
  test_inputs=generate_test_inputs()
  passed=0
  print("\n==========Running Test Cases==========\n")
  for i,test_input in enumerate(test_inputs):
    user_output=run_code(user_code,test_input)
    ref_output=run_code(reference_code,test_input)
    print(f"Test Case : {i+1}")
    print(f"Input: {test_input}")
    
    if (user_output==ref_output):
      print("Result: Pass\n")
      passed+=1
    else:
      print("Result: Fail\n")
      print("Expected Output: ", ref_output)
      print("User Output: ", user_output)

  print("==========FINAL RESULT==========")
  print(f"passed {passed}/{len(test_inputs)} test cases")
    
