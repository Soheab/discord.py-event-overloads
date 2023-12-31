"""
This type stub file was generated by pyright.
"""

import logging
from typing import Literal, NamedTuple
from .client import *
from .appinfo import *
from .user import *
from .emoji import *
from .partial_emoji import *
from .activity import *
from .channel import *
from .guild import *
from .flags import *
from .member import *
from .message import *
from .asset import *
from .errors import *
from .permissions import *
from .role import *
from .file import *
from .colour import *
from .integrations import *
from .invite import *
from .template import *
from .welcome_screen import *
from .sku import *
from .widget import *
from .object import *
from .reaction import *
from . import abc as abc, app_commands as app_commands, opus as opus, ui as ui, utils as utils
from .enums import *
from .embeds import *
from .mentions import *
from .shard import *
from .player import *
from .webhook import *
from .voice_client import *
from .audit_logs import *
from .raw_models import *
from .team import *
from .sticker import *
from .stage_instance import *
from .scheduled_event import *
from .interactions import *
from .components import *
from .threads import *
from .automod import *

"""
Discord API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Discord API.

:copyright: (c) 2015-present Rapptz
:license: MIT, see LICENSE for more details.

"""
__title__ = ...
__author__ = ...
__license__ = ...
__copyright__ = ...
__version__ = ...
__path__ = ...
class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int
    ...


version_info: VersionInfo = ...
