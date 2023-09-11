import re
import subprocess
import os

def extract_links_from_file(file_path):
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                url_pattern = r'https://\S+'
                match = re.search(url_pattern, line)
                if match:
                    links.append(match.group())
        return links
    except FileNotFoundError:
        print("File not found.")
        return []

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

file_path = input("Drag and drop the m3u8 file to download: ")
links = extract_links_from_file(file_path)

if links:
    with open('links.txt', 'w', encoding='utf-8') as output_file:
        for link in links:
            output_file.write(link + '\n')
    print('Links extracted and saved to links.txt')

    download_path = os.path.join(current_dir, 'download.py')

    if os.path.isfile(download_path):
        subprocess.run(['python', download_path])  ## run the download.py
    else:
        print("download.py not found in the current directory.")
else:
    print('No links found in the file.')

exit(0)
