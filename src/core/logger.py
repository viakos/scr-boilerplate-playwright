# src/core/logger.py

from rich.console import Console
from rich.logging import RichHandler
import logging

# Console object (optional, if you want to print pretty messages manually)
console = Console()

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

# Logger instance to use everywhere
logger = logging.getLogger("scraper")
