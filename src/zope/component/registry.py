##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Basic components support
"""
# BBB 2011-07-10, import registry from zope.registry
from zope.registry import Components
from zope.registry import _getUtilityProvided
from zope.registry import _getAdapterProvided
from zope.registry import _getAdapterRequired
from zope.registry import UtilityRegistration
from zope.registry import AdapterRegistration
from zope.registry import SubscriptionRegistration
from zope.registry import HandlerRegistration

from zope.component._api import handle
from zope.component._declaration import adapter

from zope.component.interfaces import IAdapterRegistration
from zope.component.interfaces import IHandlerRegistration
from zope.component.interfaces import IRegistrationEvent
from zope.component.interfaces import ISubscriptionAdapterRegistration
from zope.component.interfaces import IUtilityRegistration

@adapter(IUtilityRegistration, IRegistrationEvent)
def dispatchUtilityRegistrationEvent(registration, event):
    handle(registration.component, event)

@adapter(IAdapterRegistration, IRegistrationEvent)
def dispatchAdapterRegistrationEvent(registration, event):
    handle(registration.factory, event)

@adapter(ISubscriptionAdapterRegistration, IRegistrationEvent)
def dispatchSubscriptionAdapterRegistrationEvent(registration, event):
    handle(registration.factory, event)

@adapter(IHandlerRegistration, IRegistrationEvent)
def dispatchHandlerRegistrationEvent(registration, event):
    handle(registration.handler, event)
