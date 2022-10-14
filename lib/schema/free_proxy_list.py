from dataclasses import dataclass

@dataclass
class FreeProxyListModel:
    ip: str
    port: int
    code: str
    country: str
    anonymity: str
    google: str
    https: str
    last_check: str
