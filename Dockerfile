# Use the official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.9

# Install system dependencies
# RUN yum install -y <dependencies>  # Uncomment if needed

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Gradio
RUN pip install gradio transformers

# Command to run the Lambda function
# Lambda expects a handler; you'll need to adapt Gradio to work with Lambda
# This might involve using a server like Flask or FastAPI within the Lambda container
CMD ["app.handler"]
