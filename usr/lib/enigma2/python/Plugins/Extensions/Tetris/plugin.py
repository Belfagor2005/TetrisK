# -*- coding: utf-8 -*-
#######################################################################
#
#  Tetris
#  Version 0.1
#  Support: www.vuplus-support.org
#
#  Copyright (c) 2020 by Robert Damas
#  All rights reserved.
#
#  Permission to use, copy, modify, and distribute this software for any
#  purpose, without fee, and without a written agreement is hereby granted,
#  provided that the above copyright notice and this paragraph and the
#  following two paragraphs appear in all copies.
#
#  IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
#  SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS,
#  ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF
#  THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#  THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#  PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS IS"
#  BASIS, AND THE AUTHOR HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE, SUPPORT,
#  UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
#
#######################################################################M
# adted from Lululla 20220716 for E2 Py3

from Plugins.Plugin import PluginDescriptor
from . import Tetris

def getDesktopSize():
    from enigma import getDesktop
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isFHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1920

def main(session, **kwargs):
    if isFHD():
        from six.moves import reload_module
        reload_module(Tetris)
        # reload(Tetris) #py2
        session.open(Tetris.Board)    
    else:
        from Screens.MessageBox import MessageBox
        from Tools.Notifications import AddPopup
        AddPopup(_("Sorry but Tetris only works with FHD skins :("),MessageBox.TYPE_INFO, 10, 'Sorry')
      
def Plugins(**kwargs):
    return [PluginDescriptor(name="Tetris", description=_("Tetris Game"), where = [PluginDescriptor.WHERE_PLUGINMENU],
            icon="Tetris.png", fnc=main)]