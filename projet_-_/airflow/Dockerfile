FROM apache/airflow:2.7.1

# Switch to root to modify permissions
USER root  

# Ensure Airflow directories exist and have correct permissions
RUN mkdir -p /opt/airflow/logs/scheduler && \
    chown -R airflow:airflow /opt/airflow/logs && \
    chmod -R 777 /opt/airflow/logs

# Switch back to airflow user (recommended)
USER airflow
