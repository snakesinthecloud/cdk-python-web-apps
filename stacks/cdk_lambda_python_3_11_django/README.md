# cdk_django

Builds a Python 3.11, Django docker container to deploy to AWS Lambda.

## Build

    ./build.sh

## Test

This image uses the AWS Lambda Runtime Interface Emulator (aws-lambda-rie) to simulate running on Lambda locally.  Because of this, you can test this locally with curl.

If the container was built with port forwarding from :9001 into :8080, this will post a payload to hit the root of the application.

You can also enter the container and start the app.

```zsh
docker exec -it cdk_lambda_python_3_11_django sh
python manage.py runserver 0.0.0.0:8000
```

## With more time

Currently, if you only access the Django lambda through API gateway (without a custom domain), Django will rewrite the URL for you and you'll end up with the wrong URL.

Add a custom domain to API gateway to prevent this, or put a Cloudfront distribution in front.

## Appendix

These steps were already performed and committed to the repository.

For up to date instructions, see the [quick install guide](https://docs.djangoproject.com/en/4.1/intro/install/) and the [tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/).  

```zsh
pip install -r requirements.txt
django-admin startproject mycdkdjangoapp
mv mycdkdjangoapp/manage.py .
mv mycdkdjangoapp/mycdkdjangoapp/* mycdkdjangoapp/
rm -rf mycdkdjangoapp/mycdkdjangoapp/

python manage.py runserver 0.0.0.0:8000 # test by going to http://127.0.0.1:8000/

# create an app
python manage.py startapp polls

python manage.py migrate

```
