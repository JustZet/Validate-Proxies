from dataclasses import dataclass

@dataclass
class HidemyModel:
    ip : str
    port : int
    country : str
    speed : str
    proxy_type: str
    anonymity: str
    latest_update: str