###
#
#   Full history: see below
#
#   Version: 1.1.0
#   Date: 2020-04-09
#   Author: Yves Vindevogel (vindevoy)
#
#   Features:
#       - Uses a dynamic root directory where to retrieve the settings
#       - Dynamic paths to themes and data
#       - Path for index.yml updated and renamed to settings.yml
#
###

import os
import yaml

from controller.options import Options
from common.singleton import Singleton


class Settings(metaclass=Singleton):
    __index_settings = None

    def __init__(self):
        settings_dir = os.path.join(Options().data_dir, 'index')
        file = open(os.path.join(settings_dir, 'settings.yml'), 'r')

        self.__index_settings = yaml.load(file, Loader=yaml.SafeLoader)

    @property
    def index_max_posts(self):
        return int(self.__index_settings['max_posts'])

    @property
    def index_spotlight_posts(self):
        return int(self.__index_settings['spotlight_posts'])

    @property
    def index_highlight_posts(self):
        return int(self.__index_settings['highlight_posts'])

###
#
#   Version: 1.0.1
#   Date: 2020-04-08
#   Author: Yves Vindevogel (vindevoy)
#
#   Fixes:
#       - Hard-coded values
#
#   Version: 1.0.0
#   Date: 2020-04-07
#   Author: Yves Vindevogel (vindevoy)
#
#   Original code
#
###