import os

class Config:
	def __init__(self):
		self.redis_connection_string: str = os.getenv("REDIS_CONNECTION_STRING")
		self.vault_address: str = os.getenv("VAULT_ADDRESS")
		self.rpc_url: str = os.getenv("RPC_URL")
		
		
		