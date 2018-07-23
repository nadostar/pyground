porm = """
Programing is fun
When the work is done
if you wanna make your work also fun:
    use Python!
"""

with open('poem.txt', 'w') as f:
    f.write(porm)

with open('poem.txt', 'r') as f:
    print(f.readlines())
