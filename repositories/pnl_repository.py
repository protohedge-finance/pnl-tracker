from redis import Redis
from datetime import datetime


class PnlRepository:
    def __init__(self, redis: Redis):
        self.redis: Redis = redis

    def add_pnl(self, pnl: int):
        timestamp = int(datetime.utcnow().timestamp()*1e3)
        val = "{}:{}".format(timestamp, pnl)
        self.redis.zadd("pnl", {val: 0})
