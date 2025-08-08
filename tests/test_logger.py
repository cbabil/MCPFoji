import logging
from src.lib.logger import setup_logging

def test_setup_logging(mocker):
    """
    Tests that setup_logging configures the root logger correctly.
    """
    mock_basic_config = mocker.patch("logging.basicConfig")
    setup_logging()
    mock_basic_config.assert_called_once_with(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
