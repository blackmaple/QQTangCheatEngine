isPreLoadRes = False
uin = -1
isLeague = 0
screenAlphaDir = 0
screenAlpha = 1.0

def screenStartIn():
    global screenAlphaDir
    global screenAlpha
    screenAlphaDir = 0.5
    screenAlpha = 0.0



def screenStartOut():
    global screenAlphaDir
    global screenAlpha
    return 
    screenAlphaDir = -4
    screenAlpha = 1.0


class TScreenMask(TStatic):
    __module__ = __name__
    initlayer = 9999999
    rect = (0,
     0,
     0,
     0)

    def OnDraw():
        global screenAlpha
        if sc_isWindow():
            return 
        if (screenAlphaDir == 0):
            return 
        screenAlpha += (((1.0 / 500.0) * sc_getDeltaTick()) * screenAlphaDir)
        if (screenAlpha > 1.0):
            screenAlpha = 1
            screenAlhpaDir = 0
        elif (screenAlpha < 0):
            screenAlpha = 0
            screenAlhpaDir = 0
        maskAlpha = ((1 - screenAlpha) * 255)
        color = (int(maskAlpha) << 24)
        sc_drawBar(0, 0, 800, 600, color)




def LoginOK():
    do(UI.children.login.children.wait, 'finish')
    print 'login ok'
    GotoUIScreen('selSect')



def LoginFailed():
    do(UI.children.login.children.wait, 'finish')
    Win_ShowWidget('UI.login.loginDlg', True)



def NotifyVNetAuthorizationResult(bSuccess):
    if (bSuccess and Win_IsVisible('UI.login.vnetDlg')):
        doUI('UI.login.vnetDlg.crossBtn', 'OnClick')
    if doUI('UI.login.wait', 'start'):
        PlaySound(soundMain, 1)



def NotifyLoginSuccessType(result):
    global loginType
    if ((result == 1) or (result == 2)):
        loginType = result
    else:
        loginType = 0



def ShowVerifyDlg():
    Win_SetText('UI.login.verifyDlg.verifyEdit', '')
    Win_SetImg('UI.login.verifyDlg.verifyPic', '')
    Win_SetImg('UI.login.verifyDlg.verifyPic', 'res/verify.bmp')
    do(UI.children.login.children.wait, 'finish')
    ui_setCapture('UI.login.verifyDlg')
    PlaySound(soundMain, 1)


class UI_children_login:
    __module__ = __name__
    type = 'SCREEN'
    rect = (0,
     0,
     800,
     331)
    bkimage = 'ui/selSect/bg_login.img'
    accel = ()

    def OnEnter():
        if (Win_IsVisible('UI.login.wait') or Win_IsVisible('UI.login.vnetDlg')):
            return 
        if (Win_IsVisible('UI.login.verifyDlg') and doUI('UI.login.verifyDlg.confirm', 'OnClick')):
            return 
        if (Win_IsChecked('UI.login.loginDlg.userProtocolCk') and doUI('UI.login.loginDlg.confirmBtn', 'OnClick')):
            pass



    def OnEscape():
        if (Win_IsVisible('UI.login.wait') and do(UI.children.login.children.wait, 'finish')):
            LoginTimeout(1)
        return 1



    def OnInit():
        global uin
        Win_ShowWidget(uiGuideBar, 0)
        Win_ShowWidget(uiSocialityDlg, 0)
        Win_ShowWidget(uiMenuDlg, 0)
        print 'OnInit login'
        Win_Timer('UI.login.resPreLoader', 1000)
        Win_ShowWidget('UI.login.loginDlg.vnetLoginBtn', CanLoginFromVNet())
        Win_SetFocus('UI.login.loginDlg.player1.pwd')
        Win_SelectSelf('UI.login.loginDlg.player1')
        Win_ShowWidget('UI.login.loginDlg.player1', True)
        uin = GetLoginUinFromCmdLn()
        if ((uin > 0) and Win_SetText('UI.login.loginDlg.player1.id', str(uin))):
            Win_SetText('UI.login.loginDlg.player1.pwd', '********')
            do(UI.children.login.children.wait, 'start')
            LoginFromGetData()
        Win_ShowWidget('UI.login.loginDlg', 1)
        PlayMusic(musicStart, -1)
        Win_SetCheck('UI.login.loginDlg.userProtocolCk', 1)


    class children:
        __module__ = __name__
        class logo(TStatic):
            __module__ = __name__
            initlayer = 100000
            rect = (504,
             18,
             199,
             167)
            bkimage = 'object/ui/login/img_logo.img'

        class loginDlg(TStatic):
            __module__ = __name__
            initlayer = 10001
            rect = (437,
             112,
             346,
             429)
            bkimage = 'object/ui/login/dlg_login.img'
            class children:
                __module__ = __name__
                class player1(TStatic):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0)]
                    rect = (0,
                     0,
                     0,
                     0)
                    groupstop = 1
                    class children:
                        __module__ = __name__
                        class id(TEditID):
                            __module__ = __name__
                            editable = 1
                            rect = (139,
                             104,
                             140,
                             24)
                            captionrect = (0,
                             6,
                             100,
                             12)
                            drawcolor = lightColor
                            textEdgeColor = maskColor

                            def OnMsgBoxOk(h):
                                Win_SetFocus('UI.login.loginDlg.player1.id')



                            def OnTab():
                                Win_SetFocus('UI.login.loginDlg.player1.pwd')



                        class pwd(TEditPassword):
                            __module__ = __name__
                            editable = 1
                            rect = (139,
                             147,
                             140,
                             24)
                            captionrect = (0,
                             6,
                             100,
                             12)
                            drawcolor = lightColor
                            textEdgeColor = maskColor

                            def OnMsgBoxOk(h):
                                Win_SetFocus('UI.login.loginDlg.player1.pwd')



                            def OnTab():
                                Win_SetFocus('UI.login.loginDlg.player1.id')





                class playAnimBtn(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      2,
                      2)]
                    rect = ((475 - 437),
                     (321 - 112),
                     98,
                     31)
                    bkimage = 'object/ui/login/btn_playAnim.img'

                    def OnClick(this):
                        PlayCG()



                class userProtocolCk(TStdCheck):
                    __module__ = __name__
                    rect = (150,
                     185,
                     20,
                     17)
                    bkimagepos = (0,
                     5)

                    def OnClick(this):
                        ui = 'UI.login.loginDlg'
                        if (Win_IsChecked((ui + '.userProtocolCk')) and Win_EnableWidget((ui + '.confirmBtn'), True)):
                            pass
                        PlaySound(soundUI, 1)



                class agreeUserProtocal(THyperLink):
                    __module__ = __name__
                    rect = (162,
                     187,
                     130,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    URL = 'http://qqtang.qq.com/service/license.html'
                    caption = '\xd2\xd1\xd4\xc4\xb6\xc1\xb2\xa2\xcd\xac\xd2\xe2\xd3\xce\xcf\xb7\xd0\xad\xd2\xe9'

                class helpBtn(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    rect = ((466 - 437),
                     (371 - 112),
                     76,
                     31)
                    bkimage = 'object/ui/login/btn_help.img'

                    def OnClick(this):
                        ui_jumpHelpWeb()



                class confirmBtn(TButton):
                    __module__ = __name__
                    initlayer = 10003
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      2,
                      2)]
                    rect = ((624 - 437),
                     (371 - 112),
                     80,
                     31)
                    bkimage = 'object/ui/login/btn_login.img'

                    def OnClick(this):
                        global uin
                        id = int(Win_GetText('UI.login.loginDlg.player1.id'))
                        uin = id
                        pw = Win_GetText('UI.login.loginDlg.player1.pwd')
                        if ((uin < 10001) and Win_ShowMsgBox('\xc4\xfa\xca\xe4\xc8\xeb\xc1\xcb\xce\xde\xd0\xa7\xb5\xc4QQ\xba\xc5', '', 0, 'Ui.login.loginDlg.player1.id', 0)):
                            ui_msgBox(2)
                            return 
                        if (('' == pw) and Win_ShowMsgBox('\xc7\xeb\xca\xe4\xc8\xeb\xc3\xdc\xc2\xeb', '', 0, 'Ui.login.loginDlg.player1.pwd', 0)):
                            ui_msgBox(2)
                            return 
                        Login(id, 0, pw, '')
                        doUI('UI.login.wait', 'start')
                        PlaySound(soundMain, 1)



                class quitBtn(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      2,
                      2)]
                    rect = ((709 - 437),
                     (371 - 112),
                     41,
                     31)
                    bkimage = 'object/ui/login/btn_quit.img'
                    bkImgFlag = dt_center

                    def OnClick(this):
                        PlaySound(soundLeave, 1)
                        Quit()



                class vnetLoginBtn(TButton):
                    __module__ = __name__
                    visible = 1
                    rect = (150,
                     (321 - 112),
                     76,
                     31)
                    bkimage = 'object/ui/login/btn_vnetLogin.img'

                    def OnClick(this):
                        Win_EnableWidget('UI.login.loginDlg', 0)
                        Win_ShowWidget('UI.login.vnetDlg', 1)
                        sc_ShowLoginVNetWeb(435, 215, 312, 64)
                        PlaySound(soundMain, 1)





        class vnetDlg(TDlg):
            __module__ = __name__
            visible = 0
            initlayer = 200000
            rect = (420,
             200,
             364,
             104)
            bkimage = 'object/ui/login/dlg_vnetLogin.img'
            class children:
                __module__ = __name__
                class crossBtn(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    rect = (335,
                     4,
                     22,
                     22)
                    bkimage = 'object/ui/common/btn_cross.img'

                    def OnClick(this):
                        sc_DestroyLoginVNetWeb()
                        Win_ShowWidget('UI.login.vnetDlg', False)
                        Win_EnableWidget('UI.login.loginDlg', 1)





        class wait(TDlg):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            darkBG = 1
            rect = (287,
             320,
             226,
             95)
            bkimage = 'object/ui/login/dlg_wait.img'

            def start():
                global waitNum
                waitNum = 30
                Win_SetText('UI.login.wait.numberTip', ('%02d' % waitNum))
                Win_Timer('UI.login.wait.numberTip', 1000)
                ui_setCapture('UI.login.wait')



            def finish():
                Win_Timer('UI.login.wait.numberTip', 0)
                Win_ShowWidget('UI.login.wait', false)


            class children:
                __module__ = __name__
                class numberTip:
                    __module__ = __name__
                    type = 'NUMLABEL'
                    rect = (5,
                     -130,
                     206,
                     130)
                    bkimage = 'object/ui/common/number1.img'
                    textsize = 103
                    textwidth = 103
                    textheight = 130

                    def OnTimer(this):
                        global waitNum
                        waitNum -= 1
                        if ((waitNum < 0) and do(UI.children.login.children.wait, 'finish')):
                            LoginTimeout(0)
                            return 
                        Win_SetText(this, ('%02d' % waitNum))



                class linkAnim(TStatic):
                    __module__ = __name__
                    rect = (17,
                     30,
                     192,
                     21)
                    bkimage = 'object/ui/login/img_link.img'
                    framescheme = [(0,
                      1,
                      0,
                      1,
                      0,
                      1,
                      0,
                      1)]

                class cancelBtn(TButton):
                    __module__ = __name__
                    rect = (91,
                     55,
                     43,
                     31)
                    bkimage = 'object/ui/common/btn_cancel.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        do(UI.children.login.children.wait, 'finish')
                        LoginTimeout(1)





        class verifyDlg(TStatic):
            __module__ = __name__
            initlayer = 200000
            visible = 0
            rect = (((800 - 368) / 2),
             ((600 - 326) / 2),
             368,
             326)
            bkimage = 'object/ui/login/dlg_verify.img'
            class children:
                __module__ = __name__
                class verifyEdit(TEdit):
                    __module__ = __name__
                    editable = 1
                    maxchar = 4
                    rect = (50,
                     120,
                     100,
                     24)
                    captionrect = (0,
                     6,
                     100,
                     12)
                    drawcolor = darkColor
                    textEdgeType = -1

                class verifyPic(TStatic):
                    __module__ = __name__
                    rect = (43,
                     154,
                     1,
                     1)

                class nextBtn(TButton):
                    __module__ = __name__
                    rect = (190,
                     170,
                     129,
                     30)
                    bkimage = 'object/ui/login/btn_nextpic.img'

                    def OnClick(this):
                        GetVerifyCode()



                class confirm(TButton):
                    __module__ = __name__
                    rect = (160,
                     280,
                     65,
                     31)
                    bkimage = 'object/ui/common/btn_confirm.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        verifyCode = Win_GetText('UI.login.verifyDlg.verifyEdit')
                        if ((verifyCode == '') and ui_msgBox(2)):
                            Win_ShowMsgBox('\xc7\xeb\xca\xe4\xc8\xeb\xd1\xe9\xd6\xa4\xc2\xeb!', '', 0, 'UI.SysMsgbox', -1)
                            return 
                        Win_ShowWidget('UI.login.verifyDlg', False)
                        PlaySound(soundMain, 1)
                        LoginQQWithVerifyCode(verifyCode)



                class crossBtn(TButton):
                    __module__ = __name__
                    rect = (340,
                     6,
                     22,
                     22)
                    bkimage = 'object/ui/common/btn_cross.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget('UI.login.verifyDlg', False)
                        PlaySound(soundMain, 1)





        class resPreLoader(TStatic):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)

            def OnTimer(this):
                global isPreLoadRes
                Win_Timer('UI.login.resPreLoader', 0)
                if (not isPreLoadRes):
                    isPreLoadRes = True
                    PreLoadRes()





UI.children.login = UI_children_login

#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
