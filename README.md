```markdown
# Principal Data Engg Role - Assignment

This project demonstrates an ETL (Extract, Transform, Load) pipeline with automated testing using pytest and Docker implementation.

## Project Structure
```bash
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
└── src
    ├── data
    │   ├── member-data-smaller-sample.csv
    │   └── member-data.csv
    ├── etl.py
    ├── execute_pipeline.py
    ├── load_data_to_db.py
    ├── read_data.py
    ├── run_tests.py
    ├── test_load_data.py
    ├── test_read_data.py
    ├── test_transform_data.py
    └── transform_data.py
```

## Getting Started

### Prerequisites

- Docker and docker-compose installed on your system.

### Running the Project

1. **Build the Docker image:**
   ```bash
   docker-compose build
   ```

2. **Run the containers:**
   ```bash
   docker-compose up -d 
   ```
   This will start the ETL process. 
   The `docker-compose.yml` file is configured to run the tests first using `run_tests.py` and then execute the `etl.py` script.

### Testing

- The `run_tests.py` script uses `pytest` to discover and run tests.
- Tests are located in files named `test_*.py`.
- The tests interact with a dedicated test collection to avoid corrupting production data.

## ETL Process

- The `etl.py` script performs the following steps:
    - **Extract:** Read data from source file provided
    - **Transform:** uses transform_data function to load data as per requirements
    - **Load:** Loads the transformed data into a MongoDB database.

## Docker Compose

- The `docker-compose.yml` file defines the services for the ETL process, including:
    - Building the Docker image.

## Data Sample after Transformation
![Alt text](data_output_sample.jpg?raw=true "Sample Data")

## Output Screenshot in Docker
![Alt text](docker_outuput.jpg?raw=true "Docker Output")

