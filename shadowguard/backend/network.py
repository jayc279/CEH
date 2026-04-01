# Handles the recursive de-obfuscation and AbuseIPDB reputation checks.
import re, base64, ipaddress, urllib.parse, requests

class NetworkGuard:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.abuseipdb.com"

    def recursive_decode_ip(self, text, depth=3):
        if depth == 0: return None
        # Check for Hex/Dword/Standard IP
        potential = re.search(r'0x[0-9a-fA-F.]+|\b\d{8,11}\b|\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
        if potential:
            try: return str(ipaddress.ip_address(potential.group(0)))
            except: pass

        # Peel layers: URL then Base64
        try:
            decoded = urllib.parse.unquote(text)
            if decoded != text: return self.recursive_decode_ip(decoded, depth-1)
            b64 = base64.b64decode(re.search(r'[A-Za-z0-9+/=]{8,}', text).group(0)).decode('utf-8')
            return self.recursive_decode_ip(b64, depth-1)
        except: return None

    def get_reputation(self, ip):
        headers = {'Accept': 'application/json', 'Key': self.api_key}
        try:
            res = requests.get(self.url, headers=headers, params={'ipAddress': ip})
            return res.json()['data']['abuseConfidenceScore']
        except: return 0
