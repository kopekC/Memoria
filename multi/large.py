# Start of the file
print("Line 1")
print("Line 2")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 3")
print("Line 498")
print("Line 499")
print("Line 500")

# Middle of the file (this section will be the conflicting area)
def function_middle():
    print("Function in the middle from MAIN")
    print("Function in the middle from MAIN")
    print("Function in the middle from MAIN")
    print("Function in the middle from MAIN")
    print("Function in the middle from MAIN")
    print("Function in the middle from MAIN")
    print("Function in the middle from MAIN")

print("Line 501")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
print("Line 502")
... # Add many more non-conflicting lines, let's say up to Line 1000
print("Line 998")
print("Line 999")
print("Line 1000")
# End of the file
