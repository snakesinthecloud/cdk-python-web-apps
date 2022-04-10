#!/bin/bash

# Build and run
IMAGE="cdk_python_flask"

echo "Cleaning up any existing containers..."
docker stop $IMAGE
docker rm $IMAGE

echo "Building the image..."
docker build --platform linux/amd64 -t $IMAGE -f Dockerfile .
echo "Running the container..."
docker run -dit --platform linux/amd64 --name $IMAGE -p 5001:5001 -p 9000:8080 $IMAGE

# Simulate payload from API Gateway -> Proxy -> Lambda
echo "Testing..."
sleep .1
curl -s -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @tests/test_index.json
echo ""
curl -s -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @tests/test_api.json
echo ""
