import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlparse
import os
import requests

def download_sitemap(url):
    response = requests.get(url)
    filename = os.path.basename(urlparse(url).path)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    else:
        print("Failed to download the file.")
        return None

def extract_post_names_from_sitemap(sitemap_path):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls = [url.text for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    post_names = [unquote(url.split('/')[-2]) for url in urls]
    return post_names

def list_xml_files(directory):
    return [file for file in os.listdir(directory) if file.endswith('.xml')]

def save_post_names_to_file(post_names, filename="heist.txt"):
    with open(filename, 'w') as file:
        for name in post_names:
            file.write(name + '\n')
    print(f"\nPost names have been saved to {filename}")

current_directory = os.getcwd()
xml_files = list_xml_files(current_directory)

user_choice = input("Do you want to download the sitemap? (yes/no): ")
user_choice = user_choice.lower().strip()

if user_choice in ['y', 'yes', 'ye']:
    sitemap_url = input("Enter the sitemap URL: ")
    downloaded_file = download_sitemap(sitemap_url)
    if downloaded_file:
        post_names = extract_post_names_from_sitemap(downloaded_file)
        print(f"Processing {downloaded_file}...\n")
        for name in post_names:
            print(name)
        save_post_names_to_file(post_names)
elif user_choice in ['n', 'no']:
    if not xml_files:
        print("No XML files found in the directory.")
    else:
        print("Select a file to process:")
        for idx, file in enumerate(xml_files):
            print(f"{idx + 1}: {file}")

        choice = int(input("Enter the number of the file you want to process: ")) - 1

        if 0 <= choice < len(xml_files):
            selected_file = xml_files[choice]
            print(f"Processing {selected_file}...\n")
            post_names = extract_post_names_from_sitemap(os.path.join(current_directory, selected_file))
            for name in post_names:
                print(name)
            save_post_names_to_file(post_names)
        else:
            print("Invalid selection.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
