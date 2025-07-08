# Claude Code Notification App

A lightweight Python notification app that integrates with Claude Code to send real-time status updates via Pushover notifications.

## Features

- Send notifications when Claude Code is waiting for input
- Send notifications when Claude Code completes tasks
- Robust error handling with retry logic
- Support for custom messages
- Environment variable configuration

## Installation

1. Install dependencies:
```bash
pip install -r tools/notifier/requirements.txt
```

2. Configure your Pushover credentials:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your actual Pushover credentials
# Replace the placeholder values with your actual keys
```

The `.env` file should contain:
```
PUSHOVER_USER_KEY=your_actual_user_key
PUSHOVER_API_TOKEN=your_actual_api_token
```

## Usage

### Basic Usage

```python
import tools.notifier.notification_app

# When Claude Code is waiting for input
tools.notifier.notification_app.notify_waiting()

# When Claude Code completes a task
tools.notifier.notification_app.notify_done()
```

### Custom Messages

```python
import tools.notifier.notification_app

# Send custom waiting message
tools.notifier.notification_app.notify_waiting("Claude Code needs your review of the generated code")

# Send custom completion message
tools.notifier.notification_app.notify_done("Successfully deployed to production!")
```

### Class-based Usage

```python
from tools.notifier.notification_app import NotificationApp

# Create app instance with custom credentials
app = NotificationApp(user_key="your_key", api_token="your_token")

# Send notifications
app.notify_waiting("Custom waiting message")
app.notify_done("Custom completion message")
```

### Command Line Usage

Send notifications directly from the command line:

```bash
# Send waiting notification
python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_waiting()"

# Send completion notification
python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_done()"

# Send custom messages
python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_waiting('Custom message here')"
python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_done('Task completed successfully')"
```

### Using from a Subdirectory

The app is organized in a `tools/notifier` directory structure:

```bash
# Directory structure:
# your-project/
# ├── tools/
# │   ├── __init__.py
# │   └── notifier/
# │       ├── __init__.py
# │       ├── notification_app.py
# │       ├── requirements.txt
# │       └── test_notifications.py
# └── your-code.py

# From the parent directory, call:
python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_waiting()"
python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_done()"

# With custom messages:
jq -r '.message' | python3 -c "import sys, tools.notifier.notification_app; tools.notifier.notification_app.notify_waiting(sys.stdin.read().strip())"
python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_done('Task completed')"
```

**Note**: Both the `tools` and `tools/notifier` directories must contain empty `__init__.py` files to be treated as Python packages.

## Testing

Run the test script to verify notifications are working:

```bash
python tools/notifier/test_notifications.py
```

The test script will send sample notifications to verify the setup.

## Claude Code Hook Configuration

To automatically receive notifications when Claude Code is waiting for input or completes tasks, configure Claude Code hooks:

### Setting Up Hooks

1. **Notification Hook** (triggers when Claude Code is waiting for input):
```bash
claude hooks add notification "python3 -c \"import tools.notifier.notification_app; tools.notifier.notification_app.notify_waiting()\""
```

2. **Stop Hook** (triggers when Claude Code completes a task):
```bash
claude hooks add stop "python3 -c \"import tools.notifier.notification_app; tools.notifier.notification_app.notify_done()\""
```

### Alternative Hook Setup

You can also configure hooks using the `/hooks` command within Claude Code:

```
/hooks
```

Then add:
- **Notification hook**: `python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_waiting()"`
- **Stop hook**: `python3 -c "import tools.notifier.notification_app; tools.notifier.notification_app.notify_done('Task completed')"`

### Verifying Hooks

Check your current hooks with:
```bash
claude hooks list
```

### Removing Hooks

To remove hooks if needed:
```bash
claude hooks remove notification
claude hooks remove stop
```

## Pushover Setup

This app uses Pushover to send reliable push notifications to your mobile device.

**Setup Steps:**
1. Install Pushover app on your device
2. Create account at https://pushover.net
3. Use the provided credentials or configure your own

**Configuration:**
The app automatically loads credentials from the `.env` file in the project root. To get your Pushover credentials:

1. Go to https://pushover.net and create an account
2. Your **User Key** is displayed on the main dashboard
3. Create a new **Application** to get your **API Token**
4. Add both to your `.env` file

**Environment Variables:**
You can also set credentials using environment variables:
```bash
export PUSHOVER_USER_KEY="your_user_key"
export PUSHOVER_API_TOKEN="your_api_token"
```

## Configuration

The app uses the following configuration:

- **Retry Logic**: 3 attempts with 1-second delays
- **Timeout**: 10 seconds per request

You can override credentials using:
1. Environment variables: `PUSHOVER_USER_KEY` and `PUSHOVER_API_TOKEN`
2. Constructor parameters when creating `NotificationApp` instances

## Error Handling

The app includes comprehensive error handling:

- Network failures are retried automatically
- API errors are logged with details
- Function calls return `True` on success, `False` on failure
- Graceful degradation when notifications fail

## Requirements

- Python 3.7+
- requests library

## Pushover Setup

1. Install Pushover app on your device
2. Create account at https://pushover.net
3. Use the provided credentials or configure your own

## Troubleshooting

- If notifications aren't received, verify your Pushover credentials
- Check your device's notification settings
- Run the test script to validate the setup
- Check console output for error messages