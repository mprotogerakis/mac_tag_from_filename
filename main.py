import sys
import macos_tags

if len(sys.argv) < 2:
    print("Please provide a file path as a command line argument.")
    sys.exit()

file_list = sys.argv
file_list.pop(0)

print(file_list)

for file_path in file_list:
    # Split the file name and extension
    file_name, file_ext = file_path.split(".")

    # Extract the tags from the file name
    tags = file_name.split("__")[1].split("_")

    print(tags)

    print("Removing all Mac Tags")
    macos_tags.remove_all(file_path)

    for tag in tags:
        print("Adding Mac Tag "+tag)
        macos_tags.add(tag, file=file_path)

    print("Now in Mac Tags")
    print (macos_tags.get_all(file_path))
