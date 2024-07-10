import requests
#pathlib is more handly than directly using the string path,
# it automatically accomades formatting  in diff os 

from pathlib import Path


def download_to_local(url: str, dest_path: Path, parent_mkdir: bool = True) -> bool:
    """
    Downloads a file from the given URL and saves it to the specified destination path.

    Args:
        url (str): The URL of the file to download.
        dest_path (Path): The path where the downloaded file will be saved.
        parent_mkdir (bool, optional): Whether to create the parent directory if it doesn't exist.
            Defaults to True.

    Returns:
        bool: True if the download was successful, False otherwise.

    Raises:
        ValueError: If the destination path is not a valid path.
    """
    # Check if the destination path is a valid path
    if not isinstance(dest_path, Path):
        raise ValueError(f"{dest_path} is not a valid path")

    # If the parent directory does not exist, create it
    if parent_mkdir:
        dest_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Write the response content to the destination path
        dest_path.write_bytes(response.content)

        return True

    except requests.RequestException as e:
        # Print an error message if the download fails
        print("Failed to download")
        return False
