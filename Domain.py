import requests
import re
from Headers import Headers
from typing import Union
from requests import Response
import exrex

class Domain:

    def __init__(self, domain_name: str, headers: Headers = None, ip: str = None,
                 port: str = None, address: str = None) -> None:
        self._domain_name = domain_name
        self._headers = headers
        self._ip = ip
        self._port = port
        self._address = address

    @property
    def headers(self) -> Headers:
        return self._headers

    @property
    def domain_name(self) -> str:
        return self._domain_name

    @property
    def address(self) -> str:
        return self._address

    @property
    def ip(self) -> str:
        return self._ip

    def get_headers_params(self) -> dict:
        return self.headers.get_params()

    def set_ip(self, ip: str) -> None:
        self._ip = ip

    def set_port(self, port: str) -> None:
        self._port = port

    def set_address(self, address: str) -> None:
        self._address = address

    def set_headers(self, accept, user_agent):
        self.headers.set_params(accept, user_agent)

    def set_server_params(self, req: Response) -> None:
        self.set_ip(req.raw.connection.sock.getpeername()[0])
        self.set_port(req.raw.connection.sock.getpeername()[1])
        self.set_address(req.url)

    def get_request(self) -> Union[Response, bool]:
        try:
            req = requests.head(url=f"http://{self.domain_name}", headers=self.get_headers_params(), stream=True,
                                allow_redirects=True, timeout=5)
            return req
        except Exception as ex:
            print(ex)
            return False

    def check_phone_number(self, pattern) -> str:
        req = requests.get(self.address)
        ans = re.search(pattern, req.text)
        if ans.group(0) is None:
            return "Номер телефона соответствует стандарту"
        else:
            return "Номер телефона в соответствии со стандартом " + ans.group().replace(' ', '')
