FROM --platform=linux/amd64 python:3.10
WORKDIR "/opt/app/"

EXPOSE 80

# Set up dependencies
COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy in Flask app
COPY app.py .
COPY templates ./templates

CMD [ "python", "app.py"]