import os
import hashlib
import time
import requests

API_KEY = "YOUR_VIRUSTOTAL_API_KEY"

def search_files(filename, directory):
    # Counter for the total number of files searched
    searched_files = 0
    # Counter for the number of files matching the specified filename
    hits = 0

    # Recursively walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if filename.lower() == file.lower():
                hits += 1
                # Get the complete file path
                file_path = os.path.join(root, file)
                print(f"Found: {file_path}")

                # Calculate MD5 hash for the file
                md5_hash = hashlib.md5()
                with open(file_path, "rb") as f:
                    while True:
                        data = f.read(4096)
                        if not data:
                            break
                        md5_hash.update(data)

                # Get file details
                # Get the file size in bytes
                file_size = os.path.getsize(file_path)
                # Get the timestamp of the last modification
                timestamp = os.path.getmtime(file_path)
                # Convert timestamp to a formatted string
                timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

                # Print file details
                print(f"Timestamp: {timestamp_str}")
                print(f"File Name: {file}")
                print(f"File Size: {file_size} bytes")
                print(f"File Path: {file_path}")
                print(f"MD5 Hash: {md5_hash.hexdigest()}")
                print()

                # Check file hash with VirusTotal
                scan_result = check_file_hash(md5_hash.hexdigest())
                if scan_result:
                    positives = scan_result['positives']
                    total = scan_result['total']
                    print(f"VirusTotal Scan Results: {positives}/{total} positives detected")
                    print()

            searched_files += 1

    # Print the search summary
    print(f"\nSearch completed.\nSearched files: {searched_files}\nHits: {hits}")

def check_file_hash(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "x-apikey": API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        print("Error occurred while connecting to VirusTotal API.")
        return None

def main():
    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    print(f"\nSearching for '{filename}' in '{directory}'...\n")

    if os.name == "posix":  # Linux
        search_files(filename, directory)
    elif os.name == "nt":  # Windows
        # Handle Windows file path format
        search_files(filename, directory.replace("\\", "\\\\"))

if __name__ == "__main__":
    main()
