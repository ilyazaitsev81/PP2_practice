import os

#path = "parent/child/grandchild"
#os.makedirs(path, exist_ok=True)

#created directories
for item in os.listdir('parent'):
    full_path = os.path.join('parent', item)
    if os.path.isdir(full_path):
        print(f"[folder] {item}")
    else:
        print(f"[file] {item}")
search_path = "."
extension = ".txt"
for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root, file))
