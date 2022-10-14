
<h1 align="center">🔑 Validate proxies!</h1>

<h4 align="center">
This piece of code is part of a larger code.

It is meant to crawl websites that offer free proxies, and check if they are valid.

The code is scalable, so specified proxies can be checked.
  
</h4>

# Getting Started

1. Open terminal
2. run these commands:  
   - ```pip install -r requirements.txt``` 
   -  ```cd lib``` 
   -  ```py main.py```


# Contributing 

 - If you want to contribute with more providers (crawl proxies websites) in 
[```lib/providers```](lib/providers/), you are welcomed :)

# Additional Information

- Available changes on [main.py](lib/main.py) : 
    - Variables:
      - ```URL``` crawl url, this url will be used for test requests, if response status is `200`, request proxy is valid
      - ```HEADERS``` headers used for requests
      - ```PROXY_TYPE``` default is **http** because default aiohttp proxy type is **http**, but you can use other proxy type, such as https, 
      - ```ALL_PROXIES``` a list of not checked proxies
      - ```VALID_PROXIES``` list of checked proxies, and response status is `200`

    - Functions:
      - `append_free_proxy_list_proxies()` append proxies list from [https://free-proxy-list.org](https://free-proxy-list.net/) in `ALL_PROXIES`
      - `append_hidemy_proxies()` append proxies list from [https://hidemy.name/en](https://hidemy.name/en/proxy-list/?ports=8080&type=http#list) in `ALL_PROXIES`
      - `is_bad_proxy()` check if the proxy got a response, if not, or the response status is other than `200`, the return is `None`. If the response status is `200`, congrats, you have an valid proxy in `VALID_PROXYES`
      - `main()` setup for crawl session