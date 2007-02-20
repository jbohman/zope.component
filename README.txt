*****************************
zope.component Package Readme
*****************************

This package represents the core of the Zope Component Architecture.
Together with the 'zope.interface' package, it provides facilities for
defining, registering and looking up components.

Please see 'src/zope/component/README.txt' for a more detailed explanation
of the component architecture.

.. contents::

Releases
********

3.2.0.2 (2006/04/15)
====================

Fix packaging bug:  'package_dir' must be a *relative* path.

zope.component version 3.2.0.1 (2006/04/14)
----------------------------------------------

Packaging change:  suppress inclusion of 'setup.cfg' in 'sdist' builds.

3.2.0 (2006/01/05)
==================

Corresponds to the verison of the zope.component package shipped as part of
the Zope 3.2.0 release.

Deprecated services and related APIS. The adapter and utility registries
are now available directly via the site manager's 'adapters' and 'utilities'
attributes, respectively.  Services are accessible, but deprecated, and
will be removed in Zope 3.3.

Deprectaed all presentation-related APIS, including all view-related
API functions. Use the adapter API functions instead.
See http://dev.zope.org/Zope3/ImplementViewsAsAdapters`

Deprecated 'contextdependent' package:  site managers are now looked up
via a thread global, set during URL traversal.  The 'context' argument
is now always optional, and should no longer be passed.

3.0.0 (2004/11/07)
==================

Corresponds to the verison of the zope.component package shipped as part of
the Zope X3.0.0 release.

