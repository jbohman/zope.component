############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
"""Component and Component Architecture Interfaces
"""
from zope.interface import Attribute
from zope.interface import Interface
from zope.interface import implements

# BBB 2011-07-09, import interfaces from zope.registry 
from zope.registry.interfaces import ComponentLookupError
from zope.registry.interfaces import Invalid
from zope.registry.interfaces import Misused
from zope.registry.interfaces import IObjectEvent
from zope.registry.interfaces import ObjectEvent
from zope.registry.interfaces import IComponentArchitecture
from zope.registry.interfaces import IComponentLookup
from zope.registry.interfaces import IComponentRegistrationConvenience
from zope.registry.interfaces import IRegistry
from zope.registry.interfaces import IFactory
from zope.registry.interfaces import IRegistration
from zope.registry.interfaces import IUtilityRegistration
from zope.registry.interfaces import _IBaseAdapterRegistration
from zope.registry.interfaces import IAdapterRegistration
from zope.registry.interfaces import ISubscriptionAdapterRegistration
from zope.registry.interfaces import IHandlerRegistration
from zope.registry.interfaces import IRegistrationEvent
from zope.registry.interfaces import RegistrationEvent
from zope.registry.interfaces import IRegistered
from zope.registry.interfaces import Registered
from zope.registry.interfaces import IUnregistered
from zope.registry.interfaces import Unregistered
from zope.registry.interfaces import IComponentRegistry
from zope.registry.interfaces import IComponents
from zope.registry.interfaces import IPossibleSite
from zope.registry.interfaces import ISite
