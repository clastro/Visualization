# Visualization Repository

This repository showcases the usage of **Grafana** and **Streamlit** for data visualization and interactive data applications. It contains configurations and examples demonstrating how to use these powerful tools for building real-time dashboards and web apps. **Streamlit** is set up using a Dockerfile for easy deployment.

## Installation

Build the Streamlit Docker Image From Dockerfile

The Streamlit app is set up using a Dockerfile for easy deployment. To build the Docker image, run the following command:
```
docker build -t streamlit .
```

Run the Streamlit Container

```
docker run -p 8501:8501 streamlit
```
