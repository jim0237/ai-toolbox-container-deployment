#!/usr/bin/env python3

import os
import sys
import time
import asyncio
from dotenv import load_dotenv
from uptime_kuma_api import UptimeKumaApi

load_dotenv()

UPTIME_KUMA_URL = "http://localhost:3001"
USERNAME = os.getenv("UPTIME_KUMA_USERNAME", "admin")
PASSWORD = os.getenv("UPTIME_KUMA_PASSWORD", "admin123")

SERVICES = [
    {
        "name": "Whoami Test Service",
        "url": "http://localhost:8082",
        "type": "http",
        "interval": 30,
        "retryInterval": 10,
    },
    {
        "name": "Ollama Service",
        "url": "http://localhost:11434/api/health",
        "type": "http",
        "interval": 30,
        "retryInterval": 10,
    },
    {
        "name": "Open WebUI",
        "url": "http://localhost:3000/health",
        "type": "http",
        "interval": 30,
        "retryInterval": 10,
    },
    {
        "name": "TTS Service",
        "url": "https://localhost:8050/health",
        "type": "http",
        "interval": 30,
        "retryInterval": 10,
    },
    {
        "name": "STT Service",
        "url": "https://localhost:8060/health",
        "type": "http",
        "interval": 30,
        "retryInterval": 10,
    },
    {
        "name": "Translation Service",
        "url": "https://localhost:8070/health",
        "type": "http",
        "interval": 30,
        "retryInterval": 10,
    },
    {
        "name": "Voice LLaMA Service",
        "url": "http://localhost:8080/health",
        "type": "http",
        "interval": 30,
        "retryInterval": 10,
    },
]

async def wait_for_uptime_kuma(api, max_retries=30, delay=2):
    for i in range(max_retries):
        try:
            await api.connect()
            return True
        except Exception as e:
            print(f"Waiting for Uptime Kuma to be ready... ({i+1}/{max_retries})")
            await asyncio.sleep(delay)
    return False

async def setup_monitors():
    api = UptimeKumaApi(UPTIME_KUMA_URL)
    
    if not await wait_for_uptime_kuma(api):
        print("Error: Uptime Kuma is not available")
        return False

    try:
        await api.login(USERNAME, PASSWORD)
        print("Successfully logged in to Uptime Kuma")

        monitors = await api.get_monitors()
        existing_names = [m["name"] for m in monitors]

        for service in SERVICES:
            if service["name"] in existing_names:
                print(f"Monitor '{service['name']}' already exists, skipping...")
                continue

            print(f"Creating monitor for {service['name']}...")
            await api.add_monitor(
                type=service["type"],
                name=service["name"],
                url=service["url"],
                interval=service["interval"],
                retryInterval=service["retryInterval"],
                maxretries=3,
                upsideDown=False,
                acceptAllCerts=True,
            )
            print(f"Successfully created monitor for {service['name']}")

        print("All monitors have been configured successfully")
        return True

    except Exception as e:
        print(f"Error setting up monitors: {str(e)}")
        return False

    finally:
        await api.disconnect()

if __name__ == "__main__":
    try:
        success = asyncio.run(setup_monitors())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nSetup interrupted by user")
        sys.exit(1)