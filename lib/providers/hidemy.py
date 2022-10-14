from dataclasses import dataclass, field
import sys

import requests
from bs4 import BeautifulSoup

sys.path.append("lib")
from schema.hidemy import HidemyModel


def hidemy_request(url: str = "https://hidemy.name/en/proxy-list/#list") -> list[HidemyModel]:
    response = requests.get(url, headers={"User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    if response.status_code == 200:
        all_proxies = []
        
        soup = BeautifulSoup(response.text, "html.parser")
        body = soup.find("tbody")
        proxies = body.find_all("tr")
        for proxy in proxies:
            container = proxy.find_all("td")
            
            ip = container[0].text
            port = container[1].text
            country = container[2].text
            speed = container[3].text
            proxy_type  = container[4].text
            anonymity  = container[5].text
            last_update  = container[6].text
            model = HidemyModel(ip, port, country, speed, proxy_type, anonymity, last_update)
            all_proxies.append(model)
            
        else:

            return all_proxies
        
    else:
        return f"The response status for {url} is {response.status_code}, \
        expected is 200, please send a bug report."
        
        
valid = []
    
@dataclass
class GetProxiesFromHidemy:
    proxies_info: list[HidemyModel] = field(init=False)
    url: str = "https://hidemy.name/en/proxy-list/#list"
    with_port: str = None
    with_type: str = None
    
    
    def __post_init__(self):
        if self.with_port is None or self.with_type is None:
            self.proxies_info = hidemy_request(self.url)
            
    @property
    def proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            proxy_format = f"{proxy.ip}:{proxy.port}"
            all_proxies.append(proxy_format)
            
        return all_proxies
    
    
    @property
    def http_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.proxy_type == "HTTP":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    @property
    def https_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.proxy_type == "HTTP":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    
    @property
    def socks4_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.proxy_type == "SOCKS4":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    @property
    def socks5_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.proxy_type == "SOCKS5":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    @property
    def socks45_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.proxy_type == "SOCKS4, SOCKS5":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    
    

    
if __name__ == "__main__":
        
    def test():
        h = GetProxiesFromHidemy()
        print(h.http_proxies)
        # for a in h.proxies_info:
        #     print(a.proxy_type)

    test()
