---
title: "Build an IoT Data Dashboard"
category: fullstack-projects
models: [claude-haiku-3-5, claude-sonnet-4, claude-opus-4, claude-fable-5]
tags: [iot, mqtt, websockets, fullstack]
difficulty: advanced
author: community
tested: true
---

## 🎯 Prompt

```
Build an IoT data collection and visualization dashboard.

Stack: Node.js + MQTT + InfluxDB (time-series) + React + WebSocket

Architecture:
1. **MQTT broker**: receive telemetry from IoT devices
2. **Ingestion service**: subscribe to MQTT, validate, write to InfluxDB
3. **REST API**: query historical data, manage devices
4. **WebSocket**: push live sensor data to dashboard
5. **Dashboard**: real-time gauges, time-series charts, device map
6. **Alerting**: threshold alerts (temperature > 80°C → notify)
7. **Device management**: register devices, see status, last seen
8. **Data retention**: auto-delete data older than 90 days

Example devices: temperature sensors, energy monitors, GPS trackers.
```

## 💡 Tips & Variations

- Works best with **Claude Sonnet 4** or **Fable 5** for complex tasks
- Adjust the bracketed placeholders `[LIKE THIS]` for your specific use case

## 🔗 Related Prompts

- See other prompts in this category: [README](README.md)
