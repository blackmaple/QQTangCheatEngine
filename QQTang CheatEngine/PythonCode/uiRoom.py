class UI_children_logo:
    __module__ = __name__
    type = 'SCREEN'
    rect = (0,
     0,
     800,
     600)

    def OnInit():
        Win_ShowWidget(uiGuideBar, 0)
        Win_ShowWidget(uiSocialityDlg, 0)
        Win_ShowWidget(uiMenuDlg, 0)
        NotifyMainWndReady(int(500))
        Win_SetValue('UI.logo.bgLogo', 1, 41)
        Win_SetValue('UI.logo.bgLogo', 2, 901)
        Win_Timer('UI.logo.InTimer', 200)


    class children:
        __module__ = __name__
        class bgLogo(TStatic):
            __module__ = __name__
            initlayer = 100000
            rect = (0,
             0,
             800,
             600)
            bkimage = 'object/ui/bg/bg_logo.img'

        class InTimer(TStatic):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)

            def OnTimer(this):
                Win_SetValue('UI.logo.bgLogo', 0.02, 41)
                Win_SetValue('UI.logo.bgLogo', 1, 901)
                Win_Timer(this, 0)
                Win_Timer('UI.logo.StopTimer', 3000)



        class StopTimer(TStatic):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)

            def OnTimer(this):
                Win_SetValue('UI.logo.bgLogo', 0.01, 41)
                Win_SetValue('UI.logo.bgLogo', 2, 901)
                Win_Timer(this, 0)
                Win_Timer('UI.logo.OutTimer', 2000)



        class OutTimer(TStatic):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)

            def OnTimer(this):
                GotoUIScreen('login')
                Win_Timer(this, 0)





UI.children.logo = UI_children_logo

#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
