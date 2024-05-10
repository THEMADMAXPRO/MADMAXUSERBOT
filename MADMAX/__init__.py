
__version__ = "v2.1.0"



from .modules.clients.clients import (
    app, bot, call
)
app = app
bot = bot
call = call


from .modules.helpers.filters import (
    commandx, commandz
)
cdx = commandx
cdz = commandz


from .modules.helpers.events import (
    edit_or_reply
)
eor = edit_or_reply


from .console import LOGGER
logs = LOGGER


from .console import PLUGINS
plugs = PLUGINS


from . import console as config
vars = config


from .modules.helpers.wrapper import (
    super_user_only, sudo_users_only
)
super_user_only = super_user_only
sudo_users_only = sudo_users_only

