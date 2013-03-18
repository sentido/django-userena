# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.utils.importlib import import_module
from django.conf.urls.defaults import patterns, url

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from userena.views import profile_detail

from .settings import USERENA_CMS_AUTO_REGISTER_APPHOOK
from .cms_menu import UserenaMenu

class classproperty(property):
    """ Taken from http://stackoverflow.com/questions/128573/using-property-on-classmethods """
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()


class UserenaApphook(CMSApp):
    name = _(u"Userena")
    menus = [UserenaMenu]
    # urls is implemented as classproperty; Override to customize

    url_default_args_overrides = {
        # "url_name" : { dict of view's default_args overrides. see documentation for more detail }
    }


    @classmethod
    def get_urls(cls):
        """
        Returns the standard urls from userena.urls.
        You can easity customize the URLs (for example - signup form) by extending the class
        and providing your overrides in *url_default_args_overrides*.
        See docs for more details and examples
        """
        module = import_module('userena.urls')
        userena_urlpatterns = module.urlpatterns
        for p in userena_urlpatterns:
            if p.name in cls.url_default_args_overrides:
                url_default_args_overrides = cls.url_default_args_overrides[p.name]
                p.default_args.update(url_default_args_overrides)

        # "Default" view is needed for DjangoCMS, otherwise when the user navigates
        # to the page this app is attached, s/he will get a 404
        return [
            patterns('',
                url(r'^$', lambda request: profile_detail(request, request.user.username), name="userena_cms_default")
            ),
            userena_urlpatterns
        ]

    urls = classproperty(get_urls)


if USERENA_CMS_AUTO_REGISTER_APPHOOK:
    apphook_pool.register(UserenaApphook)