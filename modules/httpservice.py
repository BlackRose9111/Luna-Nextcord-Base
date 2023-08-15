import flask
from nextcord.ext.commands import Cog

import main


class http_service_cog(Cog):
    def __init__(self, bot):
        self.bot = bot
        print("http_service_cog loaded")
        self.port = 64000 #I recommend 60000 range ports as they are less likely to be used by something else
        self.app = flask.Flask(main.bot_name)
        self.add_paths()
        self.app.run(port=self.port)

    def add_paths(self):
        self.app.add_url_rule("/test", "test", self.test)

    def test(self):
        return "test"

def setup(bot):
    bot.add_cog(http_service_cog(bot))