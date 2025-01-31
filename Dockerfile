# Use the official Python image.
FROM python:3.12-slim

# Set environment variables

# Set the working directory.
WORKDIR /app

# Copy project files to the container.
COPY . .

# Install pipx & Poetry
RUN apt-get update && apt-get install -y pipx && \
    pipx install poetry==2.0.0

# Ensure Poetry is available in PATH
ENV PATH="/root/.local/bin:$PATH"

# Install dependencies.
RUN poetry install --without dev

# Expose port 8080 for Google Cloud Run.
EXPOSE 8080

CMD ["poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "ffreedom_expenses.wsgi:app"]
