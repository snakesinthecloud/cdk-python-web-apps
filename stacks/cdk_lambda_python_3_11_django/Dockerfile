ARG FUNCTION_DIR="/home/lambda/"

# Stage 1 - build
FROM --platform=linux/amd64 python:3.11.0-slim-bullseye as build-image
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

# Set up dependencies, expanded into /home/lambda
COPY requirements.txt entry.sh ./
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt --target .

# Stage 2 - final
FROM --platform=linux/amd64 python:3.11.0-slim-bullseye
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie

RUN chmod 755 /usr/bin/aws-lambda-rie && \
    chmod +x entry.sh

# Copy in Django app
COPY manage.py .
COPY asgi.py .
COPY db.sqlite3 .
COPY mycdkdjangoapp ./mycdkdjangoapp
COPY polls ./polls

ENTRYPOINT [ "/home/lambda/entry.sh" ]
CMD [ "asgi.handler" ]
