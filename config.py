import os

DEFAULT_HOST="localhost"
DEFAULT_PORT=6379
DEFAULT_PASSWORD=""

class Config:
	def __init__(self):
		self.redis_host: str = os.getenv("REDIS_HOST", DEFAULT_HOST)
		self.redis_port = int(os.getenv("REDIS_PORT", DEFAULT_PORT))
		self.redis_password = os.getenv("REDIS_PASSWORD", DEFAULT_PASSWORD)
		
		self.vault_address: str = os.getenv("VAULT_ADDRESS", "")
		self.rpc_url = os.getenv("RPC_URL")
		
		
		
