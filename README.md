# REVEST-DE Project

This repository contains a solution for the REVEST-DE technical task.

## Part I: Data Warehouse
- The data warehouse ingests sales data and allows for queries and exports to a Parquet file.
- Data is ingested from `sales.csv` and stored in a PostgreSQL database.
- Queries are written to calculate average order values and monthly revenue.

## Part II: Model Deployment
- A REST API is created to recommend products based on a given product ID.
- Logging is implemented to store requests and responses in a PostgreSQL database.
- Docker and Docker Compose are used for deployment.

## Requirements
- Docker
- Docker Compose
- PostgreSQL

## Running the Project
1. Clone the repository.
2. Use Docker Compose to set up the environment.
3. Access the services via the exposed ports.

## License
- This project is open-source. Feel free to contribute or modify it as needed.
