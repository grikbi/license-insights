"""Unit tests for the REST API module."""

import json


def api_route_for(route):
    """Construct an URL to the endpoint for given route."""
    return '/api/v1/' + route


def test_heart_beat_endpoint(client):
    """Test the heart beat endpoint."""
    response = client.get(api_route_for("liveness"))
    assert response.status_code == 200
    json_data = response.json()
    assert "status" in json_data
    assert json_data["status"] == "ok"


def test_stack_license_endpoint(client):
    """Test the endpont /api/v1/stack_license."""
    payload = {
        'packages': [
            {
                'package': 'p1',
                'version': '1.1',
                'licenses': ['MIT', 'PD']
            },
            {
                'package': 'p2',
                'version': '1.1',
                'licenses': ['BSD', 'GPL V2']
            }
        ]
    }
    response = client.post(api_route_for("stack_license"), data=json.dumps(payload))
    assert response.status_code == 200
    json_data = response.json()
    assert "status" in json_data
    assert json_data["status"] == "Successful"
    assert json_data['stack_license'] == 'gplv2'
