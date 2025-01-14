# Fibonacci REST API
This project is a REST API that computes and returns the nth number in the Fibonacci sequence. It is built using Python and the Flask framework. The API is containerized using Docker and can be deployed in a production environment.

## Project Overview

The Fibonacci REST API computes the nth Fibonacci number based on user input. The Fibonacci sequence is defined as:

- F(0) = 0

- F(1) = 1

- F(n) = F(n-1) + F(n-2) for n > 1

The API is designed to be simple, scalable, and deployable in a production environment.

## Requirements

- Python 3.x
- Flask
- Docker (for containerization)
- pytest (for testing)

## Installation and Setup

1. ##### Clone the Repository
     ```bash
      git clone https://github.com/your-username/FibonacciService.git
      cd FibonacciService
    ```
2. ##### Create a Virtual Environment:
    ```bash
    python3 -m venv myenv
    ```
   Activate the Virtual Environment:
   - On Windows:
       ```bash
       myenv\Scripts\activate
       ```
   - On macOS/Linux:
      ```bash
      source myenv/bin/activate
      ```
3. ##### Install Dependencies
    ```bash
    pip install -r requirements.txt
      ```
4. ##### Set Up Environment Variables
    - Create a .env file in the root directory by copying sample.env and updating the credentials as needed
5. ##### Running the API
    ###### Locally
    To run the API locally:
    ```bash
    python3 app.py
    ```
   ###### Using Docker
    To run the API using Docker:
    ```bash
    docker compose up --build -d
    ```
6. ##### Testing the API
    ###### Unit Tests
    Run the unit tests using pytest:
     ```bash
    python3 -m pytest
    ```

## API Reference

#### Get the nth Fibonacci Number


```http
GET /api/fibonacci
```

#### Query Parameters

| Parameter | Type     | Description                                           |
| :-------- | :------- |:------------------------------------------------------|
| `n` | `integer` | **Required**. The position in the Fibonacci sequence. |

#### Example Request
```bash
  curl "http://localhost:5000/api/fibonacci?n=10"
   ```


## Deployment
### Containerization with Docker
The API is containerized using Docker. The Dockerfile and docker-compose.yml files are included in the repository.

#### Steps to Deploy:
- Build the Docker image:
```bash
  docker compose build
   ```
- Run the container:
```bash
  docker compose up
   ```
## CI/CD Integration
To automate testing and deployment, you can integrate the project with a CI/CD pipeline using tools like:
- GitHub Actions
- Jenkins
- GitLab CI/CD

###### Example GitHub Actions workflow (.github/workflows/ci-cd.yml):
```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python3 -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          python3 -m pytest

      - name: Build Docker image
        run: |
          docker compose build

      - name: Deploy to production
        run: |
          docker compose up -d
   ```

## Monitoring and Logging
### Monitoring
- Implement monitoring to track key metrics such as request latency, error rates and resource utilization. Tools like Prometheus and Grafana can be used for this purpose
- Set up alerts to notify the operations team of any critical issues or performance degradations.

### Logging
- Collect logs from the application and infrastructure to gain insights into application behavior, identify errors and troubleshoot issues.
- Utilize a centralized logging system like ELK (Elasticsearch, Logstash, Kibana) or Splunk for efficient log collection, analysis and visualization.

## Scaling the Service
To handle a high number of requests, you can:
- Use a load balancer (e.g., NGINX, AWS Elastic Load Balancer).
- Deploy multiple instances of the service using Docker or Kubernetes.
- Implement caching (e.g., Redis) to reduce computation time for repeated requests.