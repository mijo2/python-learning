# Contract Testing

## Overview
Contract testing verifies that services or components interact correctly according to agreed-upon contracts. It ensures that changes to one component don't break integrations with other components.

## Consumer-Driven Contract Testing
```python
# Consumer defines expectations
import pytest
from pact import Consumer, Provider

pact = Consumer('UserService').has_pact_with(Provider('AuthService'))

@pact.given('user exists')
@pact.upon_receiving('a request for user details')
@pact.with_request('GET', '/users/123')
@pact.will_respond_with(200, body={'id': 123, 'name': 'Alice'})
def test_get_user_details():
    # Test consumer code against mock provider
    pass
```

## Provider Contract Testing
```python
# Provider verifies it meets consumer expectations
from pact import Verifier

verifier = Verifier(provider='AuthService',
                   provider_base_url='http://localhost:8080')

verifier.verify_pacts('pacts/user_service-auth_service.json')
```

## API Contract Testing
```python
import requests
from pactman import Consumer, Provider

def test_api_contract():
    # Define expected interactions
    pact = (Consumer('ClientApp')
            .has_pact_with(Provider('UserAPI'))
            .given('user with id 123 exists')
            .upon_receiving('a request for user 123')
            .with_request(method='GET', path='/users/123')
            .will_respond_with(200, body={
                'id': 123,
                'name': 'Alice',
                'email': 'alice@example.com'
            }))

    # Test against mock
    with pact:
        response = requests.get('http://mock-server/users/123')
        assert response.json()['name'] == 'Alice'
```

## Schema-Based Contract Testing
```python
import jsonschema

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "name"]
}

def test_response_matches_schema(response_data):
    jsonschema.validate(response_data, user_schema)
```

## Message Contract Testing
```python
# Test message formats between services
import json
from pact import MessageConsumer, MessageProvider

message_pact = (MessageConsumer('OrderService')
                .has_pact_with(MessageProvider('InventoryService'))
                .expects_to_receive('inventory updated')
                .with_content({
                    'product_id': '123',
                    'quantity': 50,
                    'action': 'restocked'
                }))

def test_inventory_update_message():
    with message_pact:
        # Test message handling code
        handle_inventory_update(message_pact.message)
```

## Benefits
- **Early Detection**: Catch integration issues before deployment
- **Independent Deployment**: Services can evolve independently
- **Documentation**: Contracts serve as API documentation
- **Confidence**: Ensure changes don't break integrations

## Tools and Frameworks
- **Pact**: Popular contract testing framework
- **Pactman**: Python implementation of Pact
- **Schemathesis**: API schema testing
- **OpenAPI Spec**: Define API contracts

## Best Practices
- Define contracts from consumer perspective
- Keep contracts simple and focused
- Version contracts with API changes
- Run contract tests in CI/CD pipeline
- Include contract tests in deployment verification
