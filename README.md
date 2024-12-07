# Mini-project-of-Behruzbek-Xalimov-br-


# Pull the latest PostgreSQL Docker image
docker pull postgres:latest

# Create a Docker container for the PostgreSQL database
docker run --name university-db -e POSTGRES_USER=Xalimovt -e POSTGRES_PASSWORD=Xalimov_pass -d -p 5432:5432 postgres:latest

# Verify the container is running
docker ps

# Access the running PostgreSQL container
docker exec -it university-db psql -U Xalimovt

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install Flask and pg8000 for database connection
pip install flask pg8000
# Make sure you're in the directory with your Flask app
# Run the Flask app
python app.py

![image](https://github.com/user-attachments/assets/d724cec7-d29b-4086-9ea4-eaaa93f25bf5)
