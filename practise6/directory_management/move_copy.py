
import shutil
import os

source_file = "sample.txt"
dest_dir = "parent/child"

copied_file = os.path.join(dest_dir, "sample_copy.txt")
shutil.copy(source_file, copied_file)
moved_file = os.path.join(dest_dir, "sample_moved.txt")
shutil.move(source_file, moved_file)