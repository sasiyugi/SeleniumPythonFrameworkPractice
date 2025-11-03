# logger_util.py
import logging
import allure

# Configure logger
logger = logging.getLogger("AutomationLogger")
logger.setLevel(logging.INFO)

# Optional: Add console handler if not already present
if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

def log_info(message: str):
    """Log info-level messages and attach to Allure."""
    logger.info(message)
    allure.step(message)  # This will show up as a step in Allure

def log_warning(message: str):
    """Log warning-level messages and attach to Allure."""
    logger.warning(message)
    allure.step(f"⚠️ WARNING: {message}")

def log_error(message: str):
    """Log error-level messages and attach to Allure."""
    logger.error(message)
    allure.step(f"❌ ERROR: {message}")