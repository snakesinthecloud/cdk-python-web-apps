ARG FUNCTION_DIR="/home/lambda/"

# Stage 1 - build
FROM public.ecr.aws/lambda/python:3.9
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie

# Copy in files unlikely to change often
RUN cp -r /var/runtime/* ./

# Set up dependencies, expanded into /home/lambda
COPY requirements.txt entry.sh ./
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt --target .

RUN chmod 755 /usr/bin/aws-lambda-rie && \
    chmod +x entry.sh

# Copy in FastAPI app
COPY main.py .
COPY templates ./templates
COPY routers ./routers

ENTRYPOINT [ "/home/lambda/entry.sh" ]
CMD [ "main.handler" ]
