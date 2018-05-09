class UI_children_web:
    __module__ = __name__
    type = 'SCREEN'
    rect = (0,
     0,
     800,
     600)
    bkimage = 'object/ui/web/bg_web.img'
    accel = ()

    def OnInit():
        Win_ShowWidget(uiGuideBar, 0)
        Win_ShowWidget(uiSocialityDlg, 0)
        sc_HideWeb('kinMatch')
        sc_HideWeb('kinTeam')
        Win_ShowWidget(uiMenuDlg, 0)
        return 



    def OnDenit():
        print 'OnDenit() web'
        sc_web_close()
        print 'sc_closeWeb()'



    def OnEnter():
        return 



    def OnEscape():
        return 


    class children:
        __module__ = __name__
        class bg(TStatic):
            __module__ = __name__
            initlayer = -9999

        class leaveBtn(TButton):
            __module__ = __name__
            rect = (705,
             (573 - 569),
             58,
             19)
            bkimage = 'object/ui/web/btn_leave.img'

            def OnClick(this):
                PlaySound(soundLeave, 1)
                GotoUIScreen(screenEnterWeb)



        class backwardBtn(TButton):
            __module__ = __name__
            rect = (13,
             (571 - 567),
             58,
             19)
            bkimage = 'object/ui/web/btn_backward.img'

            def OnClick(this):
                PlaySound(soundUI, 1)
                sc_web_goBack()
                print 'sc_web_goBack()'



        class forwardBtn(TButton):
            __module__ = __name__
            rect = (89,
             (571 - 567),
             58,
             19)
            bkimage = 'object/ui/web/btn_forward.img'

            def OnClick(this):
                PlaySound(soundUI, 1)
                sc_web_goForward()
                print 'sc_web_goForward()'





UI.children.web = UI_children_web

#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
