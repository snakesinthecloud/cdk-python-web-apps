# cdk_flask

Builds a Python 3.11, Flask 2.x docker container to deploy to AWS Lambda.

## Build

```
./build.sh
```

## Test

This image uses the AWS Lambda Runtime Interface Emulator (aws-lambda-rie) to simulate running on Lambda locally.  Because of this, you can test this locally with curl.

If the container was built with port forwarding from :9000 into :8080, this will post a payload to hit the root of the application.

Request:

```zsh
curl -s -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d @tests/test_index.json
```

Response:

```json
{
    "statusCode": 200,
    "multiValueHeaders": {
        "Content-Type": ["text/html; charset=utf-8"],
        "Content-Length": ["274"]
    },
    "body": "<!doctype html>\n\n<head>\n    <title>Flask App</title>\n    <meta name=\"description\" content=\"A Flask App\">\n    <meta name=\"keywords\" content=\"cdk python web flask\">\n</head>\n<html>\n\n<body>\n    <p>CDK Python Web Apps - Flask</p>\n    <p><a href=\"api\">API</a></p>\n</body>\n\n</html>",
    "isBase64Encoded": false
}
```

You can also enter the container and start the app.

```zsh
docker exec -it cdk_python_flask_311 sh
python api.py
```

To view the app, you can browse to `http://127.0.0.1:5001/` on your host computer.