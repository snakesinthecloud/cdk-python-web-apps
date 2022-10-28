ARG FUNCTION_DIR="/home/lambda/"

# Stage 1 - build
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.9 as build-image
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

# Copy in files unlikely to change often
RUN yum clean all && \
    yum install -y git && \
    git config --global advice.detachedHead false && \
    git clone https://github.com/logandk/serverless-wsgi --branch 3.0.0 "/home/lambda/serverless-wsgi" && \
    cp serverless-wsgi/wsgi_handler.py ./ && cp serverless-wsgi/serverless_wsgi.py ./ && \
    cp -r /var/runtime/* ./ && \
    yum remove -y git && \
    yum clean all && \
    rm -rf /var/cache/yum

# Set up dependencies, expanded into /home/lambda
COPY requirements.txt entry.sh wsgi.py .serverless-wsgi ./
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt --target .

# Stage 2 - final
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.9

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
