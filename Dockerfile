FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port (Cloud Run uses PORT environment variable)
EXPOSE 8080

# Start the application
CMD streamlit run tgcf/web_ui/0_👋_Hello.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
