# -*- coding: utf-8 -*-

import logging

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Modifier
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from .settings import USERENA_CMS_AUTO_REGISTER_MENU, USERENA_CMS_AUTO_REGISTER_MENUMODIFIER

L = logging.getLogger('userena.contrib.cms_userena')
USERENA_MENU_NAMESPACE = 'userena'

class UserenaMenu(CMSAttachMenu):
    """
    """
    name = _(u"Userena menu")

    def get_nodes(self, request):
        nodes = []

        nodes.append(NavigationNode(
                        title=_(u"Personal messages"),
                        url="#", # will be replaced in the modifier with current user's URL
                        id="userena-messages",
                        attr={'is_userena': True, 'view_name': ''},
                    )
        )

        nodes.append(NavigationNode(
                        title=_(u"Edit profile"),
                        url="#", # will be replaced in the modifier with current user's URL
                        id="userena-profile-edit",
                        attr={'is_userena': True, 'view_name': 'userena_profile_edit'},
                    )
        )

        nodes.append(NavigationNode(
                        title=_(u"Change password"),
                        url="#", # will be replaced in the modifier with current user's URL
                        id="userena-password-change",
                        attr={'is_userena': True, 'view_name': 'userena_password_change'},
                    )
        )

        return nodes

if USERENA_CMS_AUTO_REGISTER_MENU:
    menu_pool.register_menu(UserenaMenu)


class UserenaMenuModifier(Modifier):
    """
    Modifier is needed, because the URLs in the menu depend on the currently logged in user
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if hasattr(request, 'user') and isinstance(request.user, User):
            if not breadcrumb:
                for n in nodes:
                    # TODO: implement - this is not working !!
                    if 'is_userena' in n.attr:
                        view_name = n.attr.get('view_name', None)
                        if view_name:
                            n.url = reverse(view_name, kwargs={'username': request.user.username})
        return nodes

if USERENA_CMS_AUTO_REGISTER_MENUMODIFIER:
    menu_pool.register_modifier(UserenaMenuModifier)