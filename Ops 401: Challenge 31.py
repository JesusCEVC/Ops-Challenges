import os

def search_files(filename, directory):
    searched_files = 0
    hits = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if filename.lower() == file.lower():
                hits += 1
                print(f"Found: {os.path.join(root, file)}")
            searched_files += 1

    print(f"\nSearch completed.\nSearched files: {searched_files}\nHits: {hits}")

def main():
    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    print(f"\nSearching for '{filename}' in '{directory}'...\n")

    if os.name == "posix":  # Linux
        search_files(filename, directory)
    elif os.name == "nt":  # Windows
        search_files(filename, directory.replace("\\", "\\\\"))  # Handle Windows file path format

if __name__ == "__main__":
    main()
