import warnings
warnings.simplefilter('once', DeprecationWarning)
warnings.warn("OCC.XmlMNaming is deprecated since pythonocc-0.18.2. Use OCC.Core.XmlMNaming", DeprecationWarning)

from OCC.Core.XmlMNaming import *
