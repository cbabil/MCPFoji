import pytest
import yaml
from src.main import yaml_loader, load_openapi_spec
from unittest.mock import MagicMock

@pytest.fixture
def mock_httpx_get(mocker):
    """Mocks httpx.get to return local mock data."""
    def _mock_get(url):
        response = MagicMock()
        response.raise_for_status.return_value = None
        if "main.yaml" in url:
            with open("tests/mock_data/main.yaml", "r") as f:
                response.text = f.read()
        elif "referenced.yaml" in url:
            with open("tests/mock_data/referenced.yaml", "r") as f:
                response.text = f.read()
        else:
            response.raise_for_status.side_effect = Exception("File not found")
        return response

    return mocker.patch("httpx.get", side_effect=_mock_get)

def test_yaml_loader(mock_httpx_get):
    """Tests the yaml_loader function."""
    url = "http://example.com/main.yaml"
    data = yaml_loader(url)
    with open("tests/mock_data/main.yaml", "r") as f:
        expected_data = yaml.safe_load(f)
    assert data == expected_data

def test_load_openapi_spec(mock_httpx_get):
    """Tests the load_openapi_spec function."""
    spec_url = "http://example.com/docs"
    resolved_spec = load_openapi_spec(spec_url)

    # Check that the reference is resolved
    assert "$ref" not in str(resolved_spec)
    assert resolved_spec["paths"]["/test"]["get"]["type"] == "object"
