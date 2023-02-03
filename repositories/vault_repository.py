import json

vault_abi = json.load(open("abi/protohedge_vault.json"))

class VaultRepository:
	def __init__(self, w3):
		self.w3 = w3

	def get_pnl(self, vault_address: str) -> int:
		vault_contract = self.w3.eth.contract(address=vault_address, abi=vault_abi)
		pnl = vault_contract.functions.pnl().call()
		return pnl
		
		