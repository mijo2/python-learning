# Fixtures in Testing

## Overview
Fixtures are setup and teardown code that run before and after tests. They provide a way to share test data, mock objects, and common test setup across multiple test functions.

## Basic Pytest Fixtures
```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_user_creation(sample_data):
    user = create_user(sample_data)
    assert user.name == "Alice"
    assert user.age == 30
```

## Fixture Scopes
- **function**: Default, runs for each test function
- **class**: Runs once per test class
- **module**: Runs once per module
- **session**: Runs once per test session

```python
@pytest.fixture(scope="module")
def database_connection():
    conn = create_db_connection()
    yield conn
    conn.close()  # Teardown

@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    yield client
    client.cleanup()
```

## Fixture Parameters
```python
@pytest.fixture(params=["mysql", "postgresql", "sqlite"])
def database(request):
    db_type = request.param
    conn = create_connection(db_type)
    yield conn
    conn.close()

def test_query(database):
    # Runs once for each database type
    result = database.execute("SELECT 1")
    assert result == 1
```

## Conftest.py for Shared Fixtures
```python
# conftest.py
import pytest

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# test_example.py
def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
```

## Fixture Dependencies
```python
@pytest.fixture
def user_data():
    return {"name": "John", "email": "john@example.com"}

@pytest.fixture
def user(user_data):
    return User(**user_data)

@pytest.fixture
def authenticated_client(client, user):
    login_user(user)
    yield client
    logout_user(user)
```

## Autouse Fixtures
```python
@pytest.fixture(autouse=True)
def setup_logging():
    # Automatically runs for all tests
    logging.basicConfig(level=logging.DEBUG)
    yield
    logging.shutdown()
```

## Temporary Directories
```python
@pytest.fixture
def temp_dir(tmp_path):
    # tmp_path is built-in fixture
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    return tmp_path
```

## Monkeypatch Fixture
```python
def test_mocked_function(monkeypatch):
    def mock_return():
        return "mocked"

    monkeypatch.setattr("module.function", mock_return)
    result = module.function()
    assert result == "mocked"
```

## Best Practices
- Use descriptive fixture names
- Keep fixtures focused and reusable
- Use appropriate scopes to minimize setup time
- Document complex fixtures
- Avoid side effects in fixtures
