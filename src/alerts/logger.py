import logging

# Configuring the logger
logging.basicConfig(
    filename="alerts.log",  # Logs to a file named 'alerts.log'
    level=logging.INFO,  # Logs messages at the INFO level and above
    format="%(asctime)s - %(levelname)s - %(message)s"  # Formats for log messages
)

# Creates a logger instance
logger = logging.getLogger()

def log_event(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

