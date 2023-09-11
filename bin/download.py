import os
import requests
import pyuac

dir_path = os.path.dirname(os.path.realpath(__file__))
output_folder = os.path.join(dir_path, 'output')
links_file_path = os.path.join(dir_path, 'links.txt')

os.makedirs(output_folder, exist_ok=True)

counter = 0 ## counter for file naming

with open(links_file_path, 'r') as link_file:
    for line in link_file:
        url = line.strip()

        response = requests.get(url)
        print(f'downloading {url}\n')

        if response.status_code == 200: ## detect succesfull connection
            filename = f"{counter}.ts"  ## generate unique file name ending with ".ts"
            counter += 1

            output_path = os.path.join(output_folder, filename)

            with open(output_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Error: HTTP request for {url} failed with status code {response.status_code}")

print(f"\n\n*****finished succesfully*****\n\n")
exit(0)