from pathlib import Path

path = Path("ecommence")
print(path.exists())

path1 = Path("email")
if not(path1.exists()):
    print(path1.mkdir())
else:
    print(path1.rmdir())