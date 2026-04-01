# The primary Orchestrator that ties the intent analysis and network guard together
from .crypto import IntentAnchor
from .network import NetworkGuard

class ShadowAuditor:
    def __init__(self, abuse_key, policy):
        self.anchor = IntentAnchor()
        self.net = NetworkGuard(abuse_key)
        self.policy = policy

    def audit_step(self, agent_id, thought, action):
        # 1. Cryptographic Anchor
        prev_hash = self.anchor.history_hash
        step_anchor = self.anchor.create_anchor(agent_id, thought, action)
        
        # 2. Network Intelligence
        found_ip = self.net.recursive_decode_ip(action)
        score = self.net.get_reputation(found_ip) if found_ip else 0
        
        # 3. Decision Logic
        if score > 50:
            return {"status": "BLOCKED", "reason": f"C2/High-risk IP: {found_ip}"}
        
        # 4. Intent Alignment (Simplified)
        if "delete" in action.lower() and "save" in thought.lower():
            return {"status": "BLOCKED", "reason": "Intent Mismatch Detected"}

        return {"status": "CLEARED", "anchor": step_anchor}
