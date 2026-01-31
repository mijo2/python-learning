# Advanced Logging Configuration

## Overview
Python's logging module provides sophisticated configuration options for controlling log output, formatting, and routing. Advanced configuration enables structured logging, multiple handlers, and dynamic reconfiguration.

## Basic Configuration
```python
import logging

# Basic config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Application started")
```

## Logger Hierarchy
```python
# Root logger
root_logger = logging.getLogger()

# Named loggers
app_logger = logging.getLogger('myapp')
db_logger = logging.getLogger('myapp.database')
api_logger = logging.getLogger('myapp.api')

# Child loggers inherit configuration from parents
print(db_logger.parent.name)  # 'myapp'
```

## Custom Formatters
```python
class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.ERROR:
            return f"ERROR: {record.getMessage()}"
        return super().format(record)

# JSON formatter
import json
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage()
        }
        return json.dumps(log_entry)
```

## Multiple Handlers
```python
# Create logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# File handler for all messages
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Console handler for warnings and above
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
```

## Configuration Files
```python
# logging.conf
[loggers]
keys=root,myapp

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_myapp]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=myapp

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('app.log',)

# Load configuration
import logging.config
logging.config.fileConfig('logging.conf')
```

## Dictionary Configuration
```python
import logging.config

config = {
    'version': 1,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'detailed',
            'level': 'INFO'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}

logging.config.dictConfig(config)
```

## Filters
```python
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.user_id = getattr(record, 'user_id', 'unknown')
        return True

# Add contextual information
logger = logging.getLogger('myapp')
logger.addFilter(ContextFilter())

# Usage
logger.info("User action", extra={'user_id': 123})
```

## Rotating File Handlers
```python
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Size-based rotation
handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)

# Time-based rotation
handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',    # Rotate at midnight
    backupCount=30      # Keep 30 days
)
```

## Best Practices
- Use appropriate log levels
- Include contextual information
- Configure logging early
- Use structured logging for better analysis
- Rotate logs to prevent disk space issues
- Test logging configuration
