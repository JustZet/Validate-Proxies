import sys
from dataclasses import dataclass, field

import requests
from bs4 import BeautifulSoup

sys.path.append("lib")
from schema.free_proxy_list import FreeProxyListModel


def free_proxy_list_request(url: str = "https://free-proxy-list.net/") -> list[FreeProxyListModel]:
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
            code = container[2].text
            country = container[3].text
            anonymity  = container[4].text
            google = container[5].text
            https = container[6].text
            last_check = container[7].text
            
            model = FreeProxyListModel(ip, port, code, country, anonymity, google, https, last_check)
            all_proxies.append(model)
        else:
            
            return all_proxies
        
    else:
        return f"The response status for {url} is {response.status_code}, \
        expected is 200, please send a bug report."
        

        
@dataclass
class GetProxiesFromFreeProxyList:
    proxies_info: list[FreeProxyListModel] = field(init=False)
    url: str = "https://free-proxy-list.net/"
    with_port: str = None
    with_type: str = None
    
    
    def __post_init__(self):
        if self.with_port is None or self.with_type is None:
            self.proxies_info = free_proxy_list_request(self.url)
            
    @property
    def proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            proxy_format = f"{proxy.ip}:{proxy.port}"
            all_proxies.append(proxy_format)
            
        return all_proxies
    
    
    @property
    def https_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.https == "yes":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    @property
    def no_https_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.https == "no":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    
    
    @property
    def elite_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.anonymity == "elite proxy":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    @property
    def anonymous_proxies(self) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.anonymity == "anonymous":
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    
    def country_proxies(self, country: str) -> list[str]:
        all_proxies = []
        for proxy in self.proxies_info:
            if proxy.country.lower() == country.lower():
                proxy_format = f"{proxy.ip}:{proxy.port}"
                all_proxies.append(proxy_format)
                
            
        return all_proxies
    