###
#
#   Full history: see below
#
#   Version: 1.1.0
#   Date: 2020-04-15
#   Author: Yves Vindevogel (vindevoy)
#
#   Added logging
#
###

import logging

from common.options import Options
from common.content import Content
from common.singleton import Singleton


class CodeVersion(metaclass=Singleton):
    __base_dir = 'codeversion'
    __logger = None

    data = None

    def __init__(self):
        self.__logger = logging.getLogger('MODEL.CODE_VERSION')
        self.__logger.setLevel(Options().default_logging_level)

        self.data = Content().load_data_settings_yaml(self.__base_dir)
        self.__logger.debug('__init__ - {0}'.format(self.data))

###
#
#   Version: 1.0.0
#   Date: 2020-04-13
#   Author: Yves Vindevogel (vindevoy)
#
#   This class was split of the DataLoader class
#
###
