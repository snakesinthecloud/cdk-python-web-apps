# cdk_fastapi_311

Builds a Python 3.11, FastAPI docker container to deploy to AWS Lambda.

## Build

```
./build.sh
```

## Test

This image uses the AWS Lambda Runtime Interface Emulator (aws-lambda-rie) to simulate running on Lambda locally.  Because of this, you can test this locally with curl.

If the container was built with port forwarding from :9001 into :8080, this will post a payload to hit the root of the application.

Request:

```zsh
curl -s -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @tests/test_index.json
```

Response:

```json
{
    "statusCode": 200,
    "headers": {
        "content-length": "451",
        "content-type": "text/html; charset=utf-8"
    },
        "multiValueHeaders": {},
        "body": "<!doctype html>\n\n<head>\n    <title>FastAPI App</title>\n    <meta name=\"description\" content=\"A FastAPI App\">\n    <meta name=\"keywords\" content=\"cdk python web fastapi\">\n</head>\n<html>\n\n<body>\n    <p>CDK Python Web Apps - FastAPI</p>\n    <p><a href=\"docs\">Documentation (OpenAPI/Swagger)</a></p>\n    <p><a href=\"redoc\">Documentation (ReDoc)</a></p>\n    <p><a href=\"example1\">Example 1</a></p>\n    <p><a href=\"settings\">Settings</a></p>\n</body>\n\n</html>",
        "isBase64Encoded": false
}
```

You can also enter the container and start the app.

```zsh
docker exec -it cdk_python_fastapi sh
python main.py
```
