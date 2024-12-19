# Container Deployment with Dockge

This directory contains container deployment configurations managed by Dockge, a lightweight Docker compose stack manager.

## Setup

1. Start Dockge:
```bash
cd dockge
docker compose up -d
```

2. Access Dockge UI:
   - Open your browser and navigate to `http://localhost:5001`
   - Use the UI to deploy and manage individual stacks

## Available Stacks

### 1. Ollama Service
- Port: 11434
- Description: Run AI models locally
- Usage: API endpoint for AI model interactions
- Monitoring: Health checks at /api/health

### 2. Open WebUI for Ollama
- Port: 3000
- Description: Web interface for Ollama
- Usage: Access `http://localhost:3000` to interact with AI models
- Note: Requires Ollama service to be running
- Monitoring: Health checks at /health

### 3. Text-to-Speech API Server
- External Port: 8050 (Internal: 8000)
- Description: GPU-accelerated Text-to-Speech service
- Features:
  - Persistent model storage
  - GPU acceleration support
  - Audio generation caching
- Usage: Access `http://localhost:8050` for TTS API endpoints
- Monitoring: Health checks at /health

### 4. Speech-to-Text API Server
- External Port: 8060 (Internal: 8000)
- Description: GPU-accelerated Speech-to-Text service
- Features:
  - Persistent model storage
  - GPU acceleration support
  - Audio processing cache
- Usage: Access `http://localhost:8060` for STT API endpoints
- Monitoring: Health checks at /health

### 5. Translation API Server
- External Port: 8070 (Internal: 8000)
- Description: GPU-accelerated Translation service
- Features:
  - Persistent model storage
  - GPU acceleration support
  - Translation caching
- Usage: Access `http://localhost:8070` for Translation API endpoints
- Monitoring: Health checks at /health

### 6. Voice LLaMA Service
- External Port: 8080 (Internal: 8000)
- Description: Voice-enabled LLaMA chat interface
- Features:
  - Persistent model storage
  - GPU acceleration support
  - Voice interaction cache
- Usage: Access `http://localhost:8080` for voice chat interface
- Monitoring: Health checks at /health

### 7. Uptime Kuma
- Port: 3001
- Description: Self-hosted monitoring tool
- Initial Setup:
  1. Access `http://localhost:3001`
  2. Create your admin account on first launch
  3. Add monitors for each service:
     - Whoami: `http://localhost:8082`
     - Ollama: `http://localhost:11434/api/health`
     - Open WebUI: `http://localhost:3000/health`
     - TTS: `https://localhost:8050/health`
     - STT: `https://localhost:8060/health`
     - Translation: `https://localhost:8070/health`
     - Voice LLaMA: `http://localhost:8080/health`
  4. Configure monitoring intervals (recommended: 30s)
  5. Set up notifications if desired
- Features:
  - Automatic container discovery via Docker socket
  - Health check monitoring for all services
  - Customizable monitoring intervals
  - Real-time alerts and notifications
  - Telemetry disabled by default
  - Frame embedding enabled for dashboard integration

### 8. Whoami Service
- Port: 8082
- Description: Simple test service that displays container information
- Usage: Access `http://localhost:8082` to see container details
- Purpose: Quick testing of Uptime-Kuma monitoring
- Monitoring: Health checks at root endpoint (/)

## Directory Structure
```
.
├── dockge/                # Dockge manager configuration
│   └── docker-compose.yml
├── stacks/                # Container stack configurations
│   ├── ollama-stack/     # Ollama service only
│   │   └── compose.yaml
│   ├── open-webui-stack/ # Separate Open WebUI service
│   │   └── compose.yaml
│   ├── tts-service-stack/
│   │   └── compose.yaml
│   ├── stt-service-stack/
│   │   └── compose.yaml
│   ├── translate-service-stack/
│   │   └── compose.yaml
│   ├── voice-llama-stack/
│   │   └── compose.yaml
│   ├── uptime-kuma-stack/
│   │   └── compose.yaml
│   └── whoami-stack/     # Test service for monitoring
│       └── compose.yaml
└── data/                  # Dockge data directory
```

## Managing Stacks
1. Create a new directory in `stacks` with `-stack` suffix
2. Add your `compose.yaml` file in the stack directory
3. Use the Dockge UI to manage and deploy stacks:
   - Navigate to `http://localhost:5001`
   - Click on a stack to view its details
   - Use the UI controls to start, stop, or manage the stack
4. Add appropriate labels for better organization:
   ```yaml
   labels:
     - "dockge.description=Your description"
     - "dockge.icon=icon-name"
     - "dockge.note=Additional notes"
   ```

## Monitoring
All services are automatically monitored by Uptime-Kuma using Docker labels:
- Health checks are configured for each service
- Default monitoring interval: 30 seconds
- Retry interval: 10 seconds
- Access the Uptime-Kuma dashboard at `http://localhost:3001`
- Initial setup required (see Uptime Kuma section above)
- Features enabled:
  - Docker container discovery
  - Automatic health check monitoring
  - Dashboard embedding support
  - Telemetry disabled
- Quick testing available via whoami service

## Security Notes
- Set strong passwords during initial service setup
- Review and adjust port mappings based on your needs
- Consider using Docker networks for inter-container communication
- Monitor system resources and adjust GPU allocations as needed