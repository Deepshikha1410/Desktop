# Use an official Ubuntu runtime as the base image
FROM openjdk:latest
WORKDIR /app

# Copy the Java source code into the container
COPY . /app

# Compile the Java source code
RUN javac New.java

# Set the default command to run when the container starts
CMD ["java", "New"]
