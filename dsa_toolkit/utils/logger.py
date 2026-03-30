import logging
def setup_logger():
    logging.basicConfig(
filename="dsa_toolkit.log",
level=logging.INFO,
format="%(asctime)s - %(levelname)s - %(message)s"
)