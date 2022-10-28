#!/bin/bash

# Build and run
IMAGE="cdk_lambda_python_3_11_django"

echo "Cleaning up any existing containers..."
docker stop $IMAGE
docker rm $IMAGE

echo "Building the image..."
docker build --platform linux/amd64 -t $IMAGE -f Dockerfile --no-cache .
echo "Running the container..."
docker run -dit --platform linux/amd64 --name $IMAGE -p 8001:8000 -p 9002:8080 $IMAGE

# Simulate payload from API Gateway -> Proxy -> Lambda
echo "Testing..."
sleep .1
curl -sL -X POST "http://localhost:9002/2015-03-31/functions/function/invocations" -d @tests/test_index.json
