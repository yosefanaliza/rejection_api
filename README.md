# Rejection API

A fun FastAPI application that returns random funny rejection messages.

## Endpoints

- `GET /` - Welcome message with API information
- `GET /rejection` - Returns a random funny rejection message

## Local Development

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8080`

## Docker Deployment

Build and run the Docker container:

```bash
docker build -t rejection-api .
docker run -p 8080:8080 rejection-api
```

## OpenShift Deployment

This application is configured to deploy on OpenShift sandbox. The Dockerfile is OpenShift-compatible and follows security best practices:

- Runs as a non-root user (UID 1001)
- Sets proper group permissions for arbitrary user IDs
- Exposes port 8080 (OpenShift standard)

### Deploy from Git Repository

1. Login to your OpenShift sandbox account
2. Create a new project or select an existing one
3. Click on "+Add" in the Developer perspective
4. Select "Import from Git"
5. Enter your Git repository URL
6. OpenShift will auto-detect the Dockerfile
7. Configure the application name and other settings
8. Click "Create"

### Deploy using OpenShift CLI (oc)

```bash
# Login to OpenShift
oc login --token=<your-token> --server=<your-server>

# Create a new project (optional)
oc new-project rejection-api

# Create a new application from Git
oc new-app <your-git-repo-url> --name=rejection-api

# Expose the service to create a route
oc expose svc/rejection-api

# Get the route URL
oc get route rejection-api
```

### Verify Deployment

Once deployed, you can test the API:

```bash
# Get your application URL
curl https://<your-route>/
curl https://<your-route>/rejection
```

## Environment Variables

Currently, no environment variables are required. The application runs with default configuration.

## Technical Details

- **Framework**: FastAPI 0.109.0
- **Server**: Uvicorn 0.27.0
- **Python Version**: 3.11
- **Port**: 8080
- **Host**: 0.0.0.0 (allows external connections)
