line = input("Enter code: ")
stack = []
pairs = {")": "(", "]": "[", "}": "{"}
problem = -1
for i, ch in enumerate(line):
    if ch in "([{":
        stack.append((ch, i))
    elif ch in ")]}":
        if not stack:
            problem = i
            break
        opening, pos = stack.pop()
        if opening != pairs[ch]:
            problem = i
            break
if problem == -1 and stack:
    problem = stack[0][1]
if problem == -1:
    print("Balanced")
else:
    print("Problem at position", problem, ":", line[problem])
    print(line)
    print(" " * problem + "^")