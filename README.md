# Phishing URL Detection
## How to deploy
1. Clone the Repository
 ```bash
    gh repo clone vagabondry/PMLDL1
```
2. Set Up the Docker Environment
The project uses two Docker containers: one for the API and one for the frontend app.

3. Build and Run the Containers
To build and start both services (API and frontend app), use Docker Compose.
Navigate to the root of the project and run:
```bash
    docker-compose up --build
```
4. Testing the Phishing URL Detection
Open your browser and go to ```http://localhost:8501``` to interact with the web app. Enter a URL and click the Predict button to see the result.

## Dependencies

The main dependencies for this project are:

    FastAPI for the REST API.
    Streamlit for the frontend.
    scikit-learn for model handling.
    pydantic for data validation.
    uvicorn for serving the FastAPI application.
 
Make sure that you have Docker installed on your system.
