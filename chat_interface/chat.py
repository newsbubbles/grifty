"""
chat.py

A minimal stub to outline how an interactive chat interface might be built around the CEOAgent.
"""

from grifty.ceo_agent import CEOAgent

class CEOChatInterface:
    def __init__(self):
        self.ceo = CEOAgent()

    def handle_message(self, message: str) -> str:
        # Basic example: If the user says "pitch <something>" call create_pitch
        if message.lower().startswith("pitch"):
            # naive parse
            parts = message.split(" ", 2)
            if len(parts) >= 3:
                return self.ceo.create_pitch(parts[1], parts[2])
            else:
                return "Usage: pitch <product> <audience>"
        else:
            return "[CEO responds with generic business chatter]"
