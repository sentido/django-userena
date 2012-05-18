# -*- coding: utf-8 -*-

from django.conf import settings


USERENA_CMS_AUTO_REGISTER_APPHOOK = getattr(settings,
                                            "USERENA_CMS_AUTO_REGISTER_APPHOOK",
                                            True)

USERENA_CMS_AUTO_REGISTER_MENU = getattr(settings,
                                         "USERENA_CMS_AUTO_REGISTER_MENU",
                                         True)

USERENA_CMS_AUTO_REGISTER_MENUMODIFIER = getattr(settings,
                                                 "USERENA_CMS_AUTO_REGISTER_MENUMODIFIER",
                                                 USERENA_CMS_AUTO_REGISTER_MENU)
