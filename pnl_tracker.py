import web3
from dotenv import load_dotenv
from config import Config
from repositories.pnl_repository import PnlRepository
from repositories.vault_repository import VaultRepository
from redis import Redis

def track_pnl(request):
	"""
	Tracks of the profit and loss of various protohedge strategies
	"""
	load_dotenv()
	config = Config()
	w3 = web3.Web3(web3.HTTPProvider(config.rpc_url))
	redis = Redis(config.redis_connection_string)
	pnl_repository = PnlRepository(redis)
	vault_repository = VaultRepository(w3)

	pnl = vault_repository.get_pnl(config.vault_address)
	pnl_repository.add_pnl(pnl)
	
	

	


	
