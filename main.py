from verifier import verify_code
#function for taking multiline code as input from the user
def get_multiline_input(prompt):
    print(prompt)
    print("Enter code. Type 'END' on a new line to finish:\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("=== AI Code Verifier ===\n")
    #inputs user code, and solution code
    user_code = get_multiline_input("Enter USER code:")
    reference_code = get_multiline_input("Enter REFERENCE code:")
    # verifying the code's results
    verify_code(user_code, reference_code)

#This ensures main.py runs only when the user executes it
if __name__ == "__main__":
    main()
