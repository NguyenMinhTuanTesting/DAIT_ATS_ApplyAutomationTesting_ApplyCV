import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": os.getenv("HEADLESS", "false").lower() == "true",
        "args": ["--start-maximized"]
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True
    }