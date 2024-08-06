import sys
def get_filetype(filename):
    file_type=filename.split(".")[-1]
    return file_type

if len(sys.argv) < 2:
    print("You must pass atleat 1 file name as a argument")
    sys.exit(1)

for num in sys.argv[1:]:
    file_type=get_filetype(num)
    print(f"{num} -> File type is {file_type}")
