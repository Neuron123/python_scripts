import docker

# Create a Docker client
client = docker.from_env()

# List all running containers
containers = client.containers.list()

# Print container IDs and names
for container in containers:
    print(f"Container ID: {container.id}, Name: {container.name}")
