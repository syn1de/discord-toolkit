import os
import requests
from tqdm import tqdm

def download_media(url, destination_folder="."):
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte

        with open(destination_folder, 'wb') as file, tqdm(
            desc=os.path.basename(url),
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(block_size):
                bar.update(len(data))
                file.write(data)

        print(f"\nDownloaded: {os.path.basename(url)}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def process_links(input_file, output_folder="."):
    with open(input_file, 'r') as file:
        links = file.read().splitlines()

    for link in links:
        # Remove everything after "?ex=" in the URL
        modified_link = link.split('?ex=')[0]
        download_media(modified_link, os.path.join(output_folder, os.path.basename(modified_link)))

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print(" " * 20 + "DISCORD DOWNLOADER" + " " * 20)
    print("=" * 50 + "\n")

    # Ask the user for the input file path
    input_file_path = input("Enter the path to the text file: ")

    # Check if the entered file path is valid
    if not os.path.isfile(input_file_path):
        print(f"Error: The specified file '{input_file_path}' does not exist.")
        exit(1)

    # Ask the user for the output folder path
    output_folder_path = input("Enter the path to the output folder: ")

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    process_links(input_file_path, output_folder_path)

    print('completed.')