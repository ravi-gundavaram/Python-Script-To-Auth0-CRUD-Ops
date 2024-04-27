# CRUD Operations Using Python Script-Auth0 Manager Deployment 

This Python script for managing Auth0 users via the Management API. Using CRUD operations and can be run from the console as an API.
Deployed with Docker and Kubernetes.

## pre-requistes

- Python 3.12+
- Docker (for containerization)
- Kubernetes (for orchestration)

## Setup

1. Install Python dependencies:
2. Build the Docker image: "docker build -t auth0-manager current_working_direcctory"
3. Run with Docker: "docker run auth0-manager"
4. Push to Registry (if required): docker push auth0-manager-image
5. Deploy to Kubernetes:
Apply ConfigMap: kubectl apply -f configmap.yaml
Apply Deployment: kubectl apply -f deployment.yaml


## Usage

The script can perform `create_user`, `get_users`, `update_users` and `delete_user` actions.(CRUD)
Access the web interface via the exposed port to create users without using Postman.
