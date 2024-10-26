FROM python:3.10-slim
# TODO: Use the appropriate base image for your model/service

# TODO: Install all your dependencies here

# TODO: Start your service here

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install all dependencies listed in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including src/app directory) into the working directory
COPY . .

# Expose port 8080 to the outside world
EXPOSE 8080

# Start the FastAPI application with Uvicorn, pointing to src/app/main.py
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8080"]