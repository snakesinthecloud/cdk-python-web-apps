#!/bin/bash

# Build and run
IMAGE="cdk_python_ecs_flask"

echo "Cleaning up any existing containers..."
docker stop $IMAGE
docker rm $IMAGE

echo "Building the image..."
docker build --platform linux/amd64 -t $IMAGE -f Dockerfile .
echo "Running the container..."
docker run -dit --platform linux/amd64 --name $IMAGE -p 5002:80 -p 80:80 -p 443:443 $IMAGE

echo "Testing 5002..."
sleep 1
curl "http://localhost:5002"

sleep 1
echo "Testing 80..."
curl "http://localhost:80"
