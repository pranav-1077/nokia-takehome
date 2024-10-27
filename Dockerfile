FROM python:3.10-slim

# Set the working directory 
WORKDIR /app

# Copy the requirements.txt file 
COPY requirements.txt .

# Install all dependencies listed in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project 
COPY . .

# Expose port 8080 
EXPOSE 8080

# Start the FastAPI application with Uvicorn
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
