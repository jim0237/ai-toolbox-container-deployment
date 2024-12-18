# Uptime Kuma Initialization Script

This script automatically configures Uptime Kuma with monitors for all services in the stack.

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

The script uses environment variables for configuration. You can set these in a `.env` file:

```env
UPTIME_KUMA_USERNAME=your_username
UPTIME_KUMA_PASSWORD=your_password
```

If not set, it defaults to:
- Username: admin
- Password: admin123

## Usage

1. Make sure Uptime Kuma is running
2. Run the script:
```bash
python init.py
```

The script will:
1. Wait for Uptime Kuma to be available
2. Log in using provided credentials
3. Create monitors for all services:
   - Whoami Test Service (http://localhost:8082)
   - Ollama Service (http://localhost:11434/api/health)
   - Open WebUI (http://localhost:3000/health)
   - TTS Service (https://localhost:8050/health)
   - STT Service (https://localhost:8060/health)
   - Translation Service (https://localhost:8070/health)

Each monitor is configured with:
- 30-second check interval
- 10-second retry interval
- 3 maximum retries
- SSL certificate verification disabled (for self-signed certificates)

## Error Handling

- The script will wait up to 60 seconds for Uptime Kuma to be available
- Existing monitors are skipped to avoid duplicates
- All errors are logged to stdout
- Non-zero exit code on failure