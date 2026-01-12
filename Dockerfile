FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy source files
COPY server.py .
COPY .env.example .

# Install dependencies
RUN uv pip install --system mcp[cli] httpx python-dotenv

# Expose MCP stdio
CMD ["python", "server.py"]
