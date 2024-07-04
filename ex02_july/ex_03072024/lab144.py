#File handling


try:
    file = open('Testdata.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()
