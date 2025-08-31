FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port (Railway will set PORT environment variable)
EXPOSE $PORT

# Set environment
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true

# Start application
CMD streamlit run tgcf/web_ui/0_👋_Hello.py --server.port=$PORT --server.address=0.0.0.0
