#!python3
# try except example

#Basic try except example
try:
    print(x)
except:
    print("There was an error")

print()
#Basic try except example where the error is captured
try:
    print(x)
except Exception as e:
    print(f"There was an error {e}")
