# AI code runner
# Executes user-provided code and captures the output or errors.

import io
import sys

code= input("Enter your code:\n")
old_stdout = sys.stdout
sys.stdout=io.StringIO()

try:
    exec(code)
    output = sys.stdout.getvalue()
    sys.stdout=old_stdout
    print("====== Output ======")
    print("Output: ",output, end="")
    print("---------------------")
except Exception as e:
    print("An error occurred: ", e)

