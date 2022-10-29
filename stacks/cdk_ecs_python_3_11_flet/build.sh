#!/bin/bash

# Build and run
IMAGE="cdk_ecs_python_3_11_flet"

echo "Cleaning up any existing containers..."
docker stop $IMAGE
docker rm $IMAGE

echo "Building the image..."
docker build --platform linux/amd64 -t $IMAGE -f Dockerfile .
echo "Running the container..."
docker run -dit --platform linux/amd64 --name $IMAGE -p 8080:80 -p 80:80 $IMAGE

# Simulate payload from API Gateway -> Proxy -> Lambda
echo "Testing..."
sleep 5
curl -sL "http://localhost" | grep title
