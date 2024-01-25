import subprocess
import time

def git_clone_with_retry(repo_url, destination_path):
    max_retries = 3
    retries = 0

    while retries < max_retries:
        try:
            subprocess.run(['git', 'clone', repo_url, destination_path], check=True)
            print(f"Clone successful!")
            break  # Exit the loop if the clone operation was successful
        except subprocess.CalledProcessError as e:
            print(f"Error during clone attempt {retries + 1}: {e}")
            retries += 1
            time.sleep(5)  # Wait for a few seconds before retrying

    if retries == max_retries:
        print(f"Max retries reached. Could not clone {repo_url} to {destination_path}.")

# Example usage:
repository_url = 'https://github.com/odoo/odoo.git'
destination_directory = 'odoo'  # Adjust this to your desired destination directory
git_clone_with_retry(repository_url, destination_directory)

