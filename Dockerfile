FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# OpenShift runs containers using an arbitrarily assigned user ID
# Set permissions so any user can read/write to the app directory
RUN chgrp -R 0 /app && \
    chmod -R g=u /app

EXPOSE 8080

# Run as non-root user
USER 1001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
