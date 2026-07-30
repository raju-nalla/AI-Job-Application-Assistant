from modules.logger import get_logger

logger = get_logger(__name__)

logger.info("Application started successfully.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")

print("Logging test completed.")