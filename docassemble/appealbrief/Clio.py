from docassemble.base.util import DAOAuth

__all__ = ['ClioAuth']

class ClioAuth(DAOAuth):
    def init(self, *pargs, **kwargs):
        super().init(*pargs, **kwargs)
        self.appname = 'Clio'
        self.token_uri = "https://app.clio.com/oauth/token"
        self.auth_uri = "https://app.clio.com/oauth/authorize"
        self.scope = "https://app.clio.com/api/v4/users/who_am_i"
    def authorize(self, web):
        headers = dict()
        self.get_credentials().apply(headers)
        if hasattr(web, 'headers'):
            web.headers.update(headers)
        else:
            web.headers = headers
