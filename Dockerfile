# Step 1 select default OS image
FROM alpine

# Step 2 Setting up environment
RUN apk add --no-cache python3 py3-pip && pip3 install --upgrade pip

# Step 3 Configure software
WORKDIR /app

# Installing dependencies.
COPY requirements.txt /app

RUN pip3 install -r requirements.txt

# Copying project files.
COPY ["Test_MongoDB_API.py", "/app"]

# Exposing an internal port
EXPOSE 5001

# Step 4 set default commands
ENTRYPOINT [ "python3" ] # Default command

# These commands will be replaced if user provides any command by himself
CMD ["Test_MongoDB_API.py"]