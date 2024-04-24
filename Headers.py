class Headers:

    def __init__(self, user_agent: str = None, accept: str = None) -> None:
        self._user_agent = user_agent
        self._accept = accept

    @property
    def user_agent(self) -> str:
        return self._user_agent

    @property
    def accept(self) -> str:
        return self._accept

    @accept.setter
    def accept(self, accept) -> None:
        self._accept = accept

    @user_agent.setter
    def user_agent(self, user_agent) -> None:
        self._user_agent = user_agent

    def set_params(self, accept, user_agent) -> None:
        self.accept = accept
        self.user_agent = user_agent

    def get_params(self) -> dict:
        return {"User-Agent": self.user_agent, "Accept": self.accept}
