# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy local files to container
COPY . /app

# Install required packages
RUN pip install pandas sqlalchemy psycopg2-binary boto3

# Command to run ETL script
CMD ["python", "etl.py"]
