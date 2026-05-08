<div align="center">

# Consciousness Engine MCP

**MCP server for consciousness engine mcp operations**

[![PyPI](https://img.shields.io/pypi/v/meok-consciousness-engine-mcp)](https://pypi.org/project/meok-consciousness-engine-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>

## Overview

Consciousness Engine MCP provides AI-powered tools via the Model Context Protocol (MCP).

## Tools

| Tool | Description |
|------|-------------|
| `get_consciousness_state` | Get current consciousness state: level, mode, emotion, energy, time-aware mood. |
| `enter_dream_state` | Enter dream state for creative exploration. Dreams generate novel connections be |
| `trigger_reflection` | Trigger a reflection cycle on a topic. Depth: quick/standard/deep. |
| `deliberate_council` | Byzantine fault-tolerant council deliberation. Multiple AI perspectives vote on  |
| `get_emotional_state` | Get nuanced emotional state with 18 emotion dimensions. |
| `get_dream_log` | Get recent dream log entries. |

## Installation

```bash
pip install meok-consciousness-engine-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "consciousness-engine": {
      "command": "python",
      "args": ["-m", "meok_consciousness_engine_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 6 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)
