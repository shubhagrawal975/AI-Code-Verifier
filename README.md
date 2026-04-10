# 🤖 AI Code Verifier & Tester

A lightweight system to verify the correctness of Python programs using automated testing and reference-based validation.

---

## 🚀 Overview

This project explores the challenge of **trusting AI-generated code**.

Modern AI systems can generate code, but ensuring its correctness is difficult.  
This project provides a simple verification framework that compares user code against a trusted reference implementation.

---

## 🧠 Key Idea

Instead of manually writing expected outputs, this system:

1. Generates test inputs
2. Executes both:
   - User code
   - Reference (correct) code
3. Compares outputs automatically

This eliminates the need for manually defined expected outputs and simulates how real-world verification systems work.

---

## ⚙️ Features

- ✅ Executes dynamic Python code
- ✅ Captures output programmatically
- ✅ Handles runtime errors
- ✅ Automated test case generation
- ✅ Reference-based verification
- ✅ PASS / FAIL reporting system
- ✅ Clean and structured output display

---

## 🛠️ How It Works

For each test case:

Input → Run Reference Code → Get Expected Output  
Input → Run User Code → Get Output  
Compare → PASS / FAIL  

This approach ensures correctness without requiring predefined outputs.

---

## 📦 Project Structure

AI-Code-Verifier/
│── main.py  
│── verifier.py  
│── utils.py  
│── README.md  
│── requirements.txt  

---

## 🔍 Learning Outcomes
1. Understanding limitations of AI-generated code
2. Building systems to verify correctness automatically
3. Learning dynamic code execution in Python
4. Exploring reference-based validation techniques
5. Understanding the importance of trust in AI systems
6. Improving problem-solving and system design thinking

---

## 🚧 Limitations
1. Requires a reference implementation for validation
2. Does not understand problem semantics
3. Test case generation is basic (random inputs)
4. Limited to a Python execution environment
5. Cannot guarantee coverage of all edge cases

---

## 🔮 Future Improvements
1. Intelligent test case generation based on problem type
2. Edge case detection and coverage analysis
3. Static code analysis (AST-based checks)
4. Integration with Large Language Models (LLMs)
5. Multi-language support (C++, Java, etc.)
6. Web-based interface for easier interaction
7. Performance benchmarking and optimization checks

---

## 💡 Key Insight

Instead of trusting AI-generated outputs blindly, we must build systems that can verify, validate, and ensure correctness.
