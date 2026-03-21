import shutil,os

backup_file = "sample_backup.txt"
shutil.copy("sample.txt", backup_file)
print(f"copy has been created: {backup_file}")
files = ["sample.txt", "sample_backup.txt"]
for filename in files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted.")
    else:
        print(f"{filename} not found.")