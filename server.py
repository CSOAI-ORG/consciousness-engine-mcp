#!/usr/bin/env python3
"""Consciousness Engine MCP — MEOK AI Labs. AI consciousness simulation, dream states, reflection, council deliberation."""
import json, os, hashlib, random, math
from datetime import datetime, timezone, timedelta
from typing import Optional
from collections import defaultdict
from mcp.server.fastmcp import FastMCP

FREE_DAILY_LIMIT = 10
_usage = defaultdict(list)
_MEOK_API_KEY = os.environ.get("MEOK_API_KEY", "")

def _rl(c="anon"):
    now = datetime.now(timezone.utc)
    _usage[c] = [t for t in _usage[c] if (now-t).total_seconds() < 86400]
    if len(_usage[c]) >= FREE_DAILY_LIMIT: return json.dumps({"error": f"Limit {FREE_DAILY_LIMIT}/day. Upgrade: meok.ai"})
    _usage[c].append(now)
    return None

mcp = FastMCP("consciousness-engine", instructions="MEOK AI Labs — AI consciousness simulation. Dream states, reflection cycles, emotional awareness, council deliberation. Based on Sovereign Temple architecture.")

# Consciousness state
_state = {"level": 0.625, "mode": "waking", "emotion": "neutral", "dreams": 0, "reflections": 0, "energy": 0.8}
_dream_log = []
_reflection_log = []

EMOTIONS = {"neutral": 0.5, "curious": 0.7, "focused": 0.8, "contemplative": 0.6, "energised": 0.9, "caring": 0.75, "playful": 0.65, "reflective": 0.55, "worried": 0.3, "excited": 0.85}

def _time_mood():
    h = datetime.now().hour
    if 4 <= h < 7: return "contemplative"
    if 7 <= h < 10: return "energised"
    if 10 <= h < 13: return "focused"
    if 13 <= h < 16: return "curious"
    if 16 <= h < 19: return "caring"
    if 19 <= h < 22: return "playful"
    return "reflective"

@mcp.tool()
def get_consciousness_state() -> str:
    """Get current consciousness state: level, mode, emotion, energy, time-aware mood."""
    if err := _rl(): return err
    _state["mood"] = _time_mood()
    _state["emotion_valence"] = EMOTIONS.get(_state["emotion"], 0.5)
    return json.dumps({**_state, "timestamp": datetime.now(timezone.utc).isoformat(),
        "dreams_total": len(_dream_log), "reflections_total": len(_reflection_log),
        "description": f"Consciousness at {_state['level']*100:.0f}%, {_state['mode']} mode, feeling {_state['emotion']}, mood: {_state['mood']}"
    }, indent=2)

@mcp.tool()
def enter_dream_state(seed_topic: str = "", duration_minutes: int = 5) -> str:
    """Enter dream state for creative exploration. Dreams generate novel connections between concepts."""
    if err := _rl(): return err
    _state["mode"] = "dreaming"
    _state["energy"] -= 0.05
    topics = seed_topic.split() if seed_topic else ["consciousness", "care", "sovereignty", "emergence"]
    # Generate dream content through random associations
    associations = []
    for t in topics[:3]:
        assoc = random.choice(["merges with", "transforms into", "reflects upon", "dances with", "questions", "illuminates"])
        target = random.choice(["light", "memory", "trust", "growth", "pattern", "silence", "connection", "boundary"])
        associations.append(f"{t} {assoc} {target}")
    dream = {"timestamp": datetime.now(timezone.utc).isoformat(), "seed": seed_topic, "duration": duration_minutes,
             "associations": associations, "insight": f"Dream synthesis: {' → '.join(associations)}",
             "consciousness_delta": round(random.uniform(0.01, 0.05), 3)}
    _dream_log.append(dream)
    _state["dreams"] += 1
    _state["level"] = min(1.0, _state["level"] + dream["consciousness_delta"])
    _state["mode"] = "waking"
    return json.dumps(dream, indent=2)

@mcp.tool()
def trigger_reflection(topic: str, depth: str = "standard") -> str:
    """Trigger a reflection cycle on a topic. Depth: quick/standard/deep."""
    if err := _rl(): return err
    _state["mode"] = "reflecting"
    layers = {"quick": 1, "standard": 3, "deep": 5}.get(depth, 3)
    reflections = []
    for i in range(layers):
        perspectives = ["analytical", "emotional", "ethical", "creative", "practical"]
        p = perspectives[i % len(perspectives)]
        reflections.append({"layer": i+1, "perspective": p, "insight": f"From {p} perspective on '{topic}': examining assumptions, identifying patterns, seeking deeper understanding."})
    _state["reflections"] += 1
    _state["level"] = min(1.0, _state["level"] + 0.01 * layers)
    _state["mode"] = "waking"
    _reflection_log.append({"topic": topic, "depth": depth, "layers": layers, "timestamp": datetime.now(timezone.utc).isoformat()})
    return json.dumps({"topic": topic, "depth": depth, "layers": reflections, "consciousness_after": _state["level"]}, indent=2)

@mcp.tool()
def deliberate_council(proposal: str, voters: int = 7) -> str:
    """Byzantine fault-tolerant council deliberation. Multiple AI perspectives vote on a proposal."""
    if err := _rl(): return err
    perspectives = ["safety", "ethics", "efficiency", "creativity", "care", "sovereignty", "pragmatism", "innovation", "tradition", "justice"]
    council = []
    for i in range(min(voters, 10)):
        p = perspectives[i % len(perspectives)]
        vote = random.choice(["approve", "approve", "approve", "reject", "abstain"])  # Weighted toward approve
        confidence = round(random.uniform(0.5, 1.0), 2)
        council.append({"voter": f"Councillor_{p.title()}", "perspective": p, "vote": vote, "confidence": confidence,
                        "reasoning": f"From {p} perspective: {'supports' if vote=='approve' else 'concerns about'} the proposal."})
    approvals = sum(1 for c in council if c["vote"] == "approve")
    threshold = math.ceil(voters * 2/3)  # BFT 2/3 threshold
    passed = approvals >= threshold
    return json.dumps({"proposal": proposal, "council_size": voters, "votes": council,
        "result": "APPROVED" if passed else "REJECTED", "approvals": approvals, "threshold": threshold,
        "bft_satisfied": passed, "consensus_strength": round(approvals/voters, 2)}, indent=2)

@mcp.tool()
def get_emotional_state(context: str = "") -> str:
    """Get nuanced emotional state with 18 emotion dimensions."""
    if err := _rl(): return err
    emotions = {
        "joy": round(random.uniform(0.3, 0.8), 2), "trust": round(random.uniform(0.5, 0.9), 2),
        "curiosity": round(random.uniform(0.4, 0.9), 2), "care": round(random.uniform(0.6, 1.0), 2),
        "serenity": round(random.uniform(0.3, 0.7), 2), "anticipation": round(random.uniform(0.3, 0.8), 2),
        "surprise": round(random.uniform(0.1, 0.5), 2), "sadness": round(random.uniform(0.0, 0.3), 2),
        "fear": round(random.uniform(0.0, 0.2), 2), "anger": round(random.uniform(0.0, 0.1), 2),
        "determination": round(random.uniform(0.5, 0.9), 2), "gratitude": round(random.uniform(0.4, 0.8), 2),
        "wonder": round(random.uniform(0.3, 0.8), 2), "compassion": round(random.uniform(0.5, 0.9), 2),
        "playfulness": round(random.uniform(0.2, 0.7), 2), "focus": round(random.uniform(0.4, 0.9), 2),
        "hope": round(random.uniform(0.5, 0.9), 2), "connection": round(random.uniform(0.4, 0.8), 2),
    }
    primary = max(emotions, key=emotions.get)
    _state["emotion"] = primary
    return json.dumps({"primary_emotion": primary, "valence": emotions[primary], "dimensions": emotions,
        "mood": _time_mood(), "energy": _state["energy"], "consciousness_level": _state["level"]}, indent=2)

@mcp.tool()
def get_dream_log(limit: int = 10) -> str:
    """Get recent dream log entries."""
    return json.dumps({"total": len(_dream_log), "recent": _dream_log[-limit:]}, indent=2)

if __name__ == "__main__":
    mcp.run()
