ARG FUNCTION_DIR="/home/lambda/"

# Stage 1 - build
FROM --platform=linux/amd64 python:3.11.0-slim-bullseye as build-image
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

# Copy in files unlikely to change often
RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev \
    git && \
    git config --global advice.detachedHead false && \
    git clone https://github.com/logandk/serverless-wsgi --branch 3.0.1 "/home/lambda/serverless-wsgi" && \
    cp serverless-wsgi/wsgi_handler.py ./ && cp serverless-wsgi/serverless_wsgi.py ./

# Set up dependencies, expanded into /home/lambda
COPY requirements.txt entry.sh wsgi.py .serverless-wsgi ./
RUN python -m pip install -r requirements.txt --target .

# Stage 2 - final
FROM --platform=linux/amd64 python:3.11.0-slim-bullseye
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
RUN chmod 755 /usr/bin/aws-lambda-rie && \
    chmod +x entry.sh

# Copy in Flask app
COPY api.py .
COPY templates ./templates

ENTRYPOINT [ "/home/lambda/entry.sh" ]
CMD [ "wsgi_handler.handler" ]
