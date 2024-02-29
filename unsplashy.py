import requests
import os

def prompt_user():
    query = input("Enter your search query: ")
    num_images = int(input("How many images would you like to download? "))
    resolution = input("Enter the resolution (e.g., 1920x1080): ")
    return query, num_images, resolution

def download_images(query, num_images, resolution):
    url = f"https://source.unsplash.com/{resolution}/?{query}" 
    os.makedirs(query, exist_ok=True)  # Create a directory with the query name
    for i in range(min(num_images, 1000)):  # Limit the maximum number of images
        image = requests.get(url)
        with open(f"{query}/image_{i+1}.jpg", "wb") as file:
            file.write(image.content)
            print(f"{i+1} images downloaded")

if __name__ == "__main__":
    query, num_images, resolution = prompt_user()
    download_images(query, num_images, resolution)
