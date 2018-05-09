defBarNum = 7
defSectNum = 28
sectName = None
chIdx = 0
chAreaIdx = ([0] * 10)
bMatchChannel = 0
sectChkIdx = None
oldPos = 0
zoneList = ['a',
 'b',
 'c']
zoneSpeed = [0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0]
zoneIndex = [0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19]
zonePos = 0
defZoneNum = 9
curZone = 0
areaIdx = 0
advert = 3
bClickAdvert = 0
isShowTaskSelDlg = 0
Guide_version = 0
Guide_upper = 0

def SortZonesBySpeed():
    global zoneIndex
    zoneIndex = range(len(zoneList))
    print 'in sort'
    print 'zonespeed',
    print zoneSpeed
    print 'zoneindex',
    print zoneIndex
    for i in range((len(zoneList) - 1)):
        for j in range((i + 1), len(zoneList)):
            if (zoneSpeed[zoneIndex[i]] > zoneSpeed[zoneIndex[j]]):
                t = zoneIndex[i]
                zoneIndex[i] = zoneIndex[j]
                zoneIndex[j] = t


    print 'zoneindex',
    print zoneIndex
    print 'out sort'



def ZoneUIIndex2LogicIndex(uiIndex):
    if (uiIndex >= len(zoneList)):
        return 0
    return zoneIndex[uiIndex]



def NotifyUIRefreshPingZoneResult():
    for i in range(len(zoneList)):
        speed = fetch_ZoneSpeedByZoneName(zoneList[i])
        zoneSpeed[i] = speed

    SortZonesBySpeed()
    doUI('UI.selSect.selServerDlg', 'setList')



def AutoLoginSection():
    doUI('UI.selSect.quickJoin', 'OnClick')



def curZone2areaIdx():
    if (curZone < 0):
        return 0
    areaCnt = Channel().getAreaCnt(chIdx)
    if (curZone >= areaCnt):
        return 0
    sectCnt = Channel().getSectCnt(chIdx, curZone)
    if (sectCnt == 0):
        return 0
    return curZone


class Channel:
    __module__ = __name__

    def getChannelCnt(this):
        return fetch_ChannelCnt()



    def login(this, uin, chIdx, areaIdx, sectIdx):
        global sectName
        sectCnt = this.getSectCnt(chIdx, areaIdx)
        print 'sectCnt=',
        print sectCnt
        info = this.getInfo(sectIdx, sectCnt)
        sectName = info.name
        print 'enter:',
        print sectName
        request_LoginSection(uin, chIdx, areaIdx, sectIdx, curZone)



    def getSectCnt(this, chIdx, areaIdx):
        if ((chIdx >= fetch_ChannelCnt()) or (areaIdx >= sc_getZoneCnt(chIdx))):
            return 0
        return GetSectionCnt(chIdx, areaIdx)



    def getAreaCnt(this, chIdx):
        return sc_getZoneCnt(chIdx)



    def getAreaName(this, chIdx, areaIdx):
        return sc_getZoneName(chIdx, areaIdx)



    def getInfo(this, sectIdx, sectCnt):

        def get(sectIdx, sectCnt):
            if (sectIdx >= sectCnt):
                return None
            info = CNil()
            si = GetSectionInfo(chIdx, areaIdx, sectIdx)
            info.name = si.m_szSectionName
            if ('"' == info.name[0]):
                info.name = info.name[1:]
            while (('"' == info.name[-1]) or (' ' == info.name[-1])):
                info.name = info.name[:-1]

            info.playerNum = (str(si.m_nCurrentNumOfPlayer) + '\xc8\xcb')
            info.fillRate = min(defBarNum, (1 + ((defBarNum * si.m_nCurrentNumOfPlayer) / si.m_nMaxNumOfPlayer)))
            info.isRed = (si.m_nCurrentNumOfPlayer >= (si.m_nMaxNumOfPlayer * 0.90000000000000002))
            if (0 == si.m_nCurrentNumOfPlayer):
                info.fillRate = 0
            return info



        def getFake(sectIdx, sectCnt):
            if (sectIdx >= sectCnt):
                return None
            info = CNil()
            info.name = ('sect name %d' % sectIdx)
            info.playerNum = (str(Rand(10)) + '\xc8\xcb')
            info.fillRate = (1 + Rand(defBarNum))
            return info


        return get(sectIdx, sectCnt)




def restoreMovedSect():
    global sectChkIdx
    if ((sectChkIdx != None) and Win_SetCheck(('UI.selSect.sect%d' % sectChkIdx), False)):
        sectChkIdx = None



def ui_SetGuideInfo(version, upper):
    global Guide_version
    global Guide_upper
    Guide_version = version
    Guide_upper = upper



def ui_GetGuideUpper():
    return Guide_upper


class UI_children_selSect:
    __module__ = __name__
    type = 'SCREEN'
    rect = (0,
     0,
     800,
     600)
    bkimage = 'object/ui/bg/bg_selSect.img'
    accel = (('OnAccel_OnF1',
      112,
      0,
      0,
      0),
     ('OnAccel_OnF2',
      113,
      0,
      0,
      0),
     ('OnAccel_OnF3',
      114,
      0,
      0,
      0),
     ('OnAccel_OnF6',
      117,
      0,
      0,
      0),
     ('OnAccel_OnF7',
      118,
      0,
      0,
      0),
     ('OnAccel_OnF8',
      119,
      0,
      0,
      0),
     ('OnAccel_OnF9',
      120,
      0,
      0,
      0),
     ('OnAccel_OnF10',
      121,
      0,
      0,
      0),
     ('OnAccel_OnF12',
      123,
      0,
      0,
      0))

    def OnAccel_OnF1():
        doUI('UI.selSect.helpBtn', 'OnClick')



    def OnAccel_OnF2():
        if ((not Win_IsVisible('UI.SysMsgbox')) and doUI('UI.selSect.quickJoin', 'OnClick')):
            sc_HideWeb('party')



    def OnEnter():
        doUI('UI.selRoom.chatArea.sendBtn', 'OnClick')



    def OnEscape():
        doUI('UI.selSect.leaveBtn', 'OnClick')
        return 1



    def OnInit():
        global curZone
        global bClickAdvert
        global areaIdx
        global zoneList
        global isShowTaskSelDlg
        Win_ShowWidget(uiGuideBar, 0)
        Win_ShowWidget(uiSocialityDlg, 0)
        sc_HideWeb('kinMatch')
        sc_HideWeb('kinTeam')
        Win_ShowWidget(uiMenuDlg, 0)
        if bClickAdvert:
            bClickAdvert = 0
            JumpHelpWeb('http://qqtang.qq.com')
            sc_web_close()
        Win_Timer('UI.selSect.tipChannel', 5000)
        screenStartIn()
        zoneList = fetch_ZoneNames()
        curZone = fetch_LastZoneIdx()
        areaIdx = curZone2areaIdx()
        if (curZone < 0):
            curZone = 0
            doUI('UI.selSect.selZoneBtn', 'OnClick')
        if bMatchChannel:
            chIdx = 3
        else:
            chIdx = min(fetch_LastChannelIdx(), (Channel().getChannelCnt() - 1))
        Win_SelectSelf(('UI.selSect.channel%d' % (chIdx + 1)))
        Win_SetFocus(('UI.selSect.channel%d' % (chIdx + 1)))
        s = ("doUI( 'UI.selSect.channel%d', 'OnClick')" % (chIdx + 1))
        exec s
        PlayMusic(musicDirAndSection, -1)
        isShowTaskSelDlg = 0



    def OnDenit():
        Win_Timer('UI.selSect.bannerBtn', 0)


    class children:
        __module__ = __name__
        class advertBtn(TButton):
            __module__ = __name__
            initlayer = 9999
            rect = (15,
             52,
             320,
             200)
            framescheme = [(0,
              99,
              0,
              99,
              0,
              99,
              0,
              99)]

            def OnClick(this):
                sc_HideWeb('party')
                url = GetCurAdvert()
                ui_jumpWeb(url)



        class billboard:
            __module__ = __name__
            type = 'MULTIEDIT'
            initlayer = 99999
            rowspace = 2
            editable = 0
            rect = (28,
             255,
             300,
             335)
            drawcolor = (255,
             221,
             214,
             255)
            textEdgeType = -1
            caption = ('    \xca\xca\xb6\xc8\xd3\xce\xcf\xb7\xa3\xac\xd3\xd0\xd2\xe6\xbd\xa1\xbf\xb5   \n\n' + '    QQ\xcc\xc3\xa3\xac \xbc\xb4\xbd\xab\xcd\xc6\xb3\xf6!')

            def OnClickHLink(url):
                ui_jumpWeb(url)



        class startPractice(TButton):
            __module__ = __name__
            rect = (379,
             513,
             51,
             74)
            bkimage = 'object/ui/selSect/btn_practice.img'

            def OnClick(this):
                global practiceMode
                print 'Enter StartPractice'
                restoreMovedSect()
                sectCnt = Channel().getSectCnt(chIdx, areaIdx)
                print 'sectCnt=',
                print sectCnt
                if (sectCnt > 0):
                    sectIdx = Rand(sectCnt)
                    print 'LoginSection',
                    print uin,
                    print chIdx,
                    print sectIdx
                    Channel().login(uin, chIdx, areaIdx, sectIdx)
                    PlaySound(soundMain, 1)
                    practiceMode = 1
                else:
                    PlaySound(soundFail, 1)



        class selZoneBtn(TButton):
            __module__ = __name__
            rect = (445,
             513,
             51,
             74)
            bkimage = 'object/ui/selSect/btn_selZone.img'

            def OnClick(this):
                global zoneList
                areaCnt = Channel().getAreaCnt(chIdx)
                zoneList = fetch_ZoneNames()
                ui_setCapture('UI.selSect.selServerDlg')
                doUI('UI.selSect.selServerDlg', 'setList')
                PlaySound(soundLeave, 1)
                SC_PingZones()



        class quickJoin(TButton):
            __module__ = __name__
            rect = (511,
             513,
             51,
             74)
            bkimage = 'object/ui/selSect/btn_quickJoin.img'

            def OnClick(this):
                restoreMovedSect()
                sectCnt = Channel().getSectCnt(chIdx, areaIdx)
                if (sectCnt > 0):
                    sectIdx = Rand(sectCnt)
                    print 'LoginSection',
                    print uin,
                    print chIdx,
                    print sectIdx
                    Channel().login(uin, chIdx, areaIdx, sectIdx)
                    PlaySound(soundMain, 1)
                else:
                    PlaySound(soundFail, 1)



        class sysSetupBtn(TButton):
            __module__ = __name__
            rect = (577,
             513,
             51,
             74)
            bkimage = 'object/ui/selSect/btn_sysSetup.img'

            def OnClick(this):
                go2setup(uin)



        class leaveBtn(TButton):
            __module__ = __name__
            rect = (717,
             520,
             52,
             48)
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            bkimage = 'object/ui/common/btn_quit.img'

            def OnClick(this):
                LogoutSection(uin)
                PlaySound(soundLeave, 1)
                Quit()



        class channel1(TRadio):
            __module__ = __name__
            framescheme = [(0,
              0,
              0,
              0,
              0,
              0,
              0,
              0),
             (1,
              1,
              1,
              1,
              1,
              1,
              1,
              1)]
            rect = (385,
             59,
             72,
             37)
            bkimage = 'object/ui/selSect/tab_practice.img'
            groupstop = 1

            def OnClick(this):
                global chIdx
                global areaIdx
                global isAutoJustScrollPos
                global bMatchChannel
                me = Win_GetFocusPath()
                restoreMovedSect()
                chIdx = (int(me[-1]) - 1)
                if (chIdx != 3):
                    bMatchChannel = 0
                areaIdx = curZone2areaIdx()
                Win_SetScrollPos('UI.selSect.scroll', 0)
                isAutoJustScrollPos = True
                doUI('UI.selSect.scroll', 'OnPosChange')
                sc_HideWeb('party')



        class channel2(channel1):
            __module__ = __name__
            rect = (454,
             58,
             72,
             37)
            bkimage = 'object/ui/selSect/tab_greenhand.img'
            groupstop = 2

        class channel3(channel1):
            __module__ = __name__
            rect = (524,
             58,
             72,
             37)
            bkimage = 'object/ui/selSect/tab_freedom.img'
            groupstop = 3

        class channel4(channel1):
            __module__ = __name__
            rect = (593,
             58,
             72,
             37)
            groupstop = 4
            bkimage = 'object/ui/selSect/tab_match.img'

        class channel5(channel1):
            __module__ = __name__
            rect = (661,
             59,
             72,
             37)
            groupstop = 5
            bkimage = 'object/ui/selSect/tab_party.img'

            def OnClick(this):
                sc_ShowWeb('party', 364, 95, 426, 495, 'http://qqtang.qq.com/game/event.htm')



        class scroll(TVScroll):
            __module__ = __name__
            rect = (768,
             92,
             26,
             360)
            pos = 0
            pagesize = -defSectNum

            def OnPosChange():
                global isAutoJustScrollPos
                global oldPos
                wCh = 'UI.selSect'
                sectCnt = Channel().getSectCnt(chIdx, areaIdx)
                Win_SetRange((wCh + '.scroll'), (((sectCnt - defSectNum) + 1) / 2))
                if isAutoJustScrollPos:
                    isAutoJustScrollPos = False
                    Win_SetScrollPos((wCh + '.scroll'), 0)
                    redList = []
                    for i in range(sectCnt):
                        info = Channel().getInfo(i, sectCnt)
                        redList.append(info.isRed)

                    saveRedCnt = 999
                    savePos = -1
                    for i in range(((sectCnt - defSectNum) + 1)):
                        redCnt = 0
                        for k in range(defSectNum):
                            if redList[(i + k)]:
                                redCnt += 1

                        if (redCnt > (defSectNum / 2)):
                            if (redCnt < saveRedCnt):
                                saveRedCnt = redCnt
                                savePos = i

                    if ((savePos != -1) and Win_SetScrollPos((wCh + '.scroll'), savePos)):
                        pass
                pos = Win_GetPos((wCh + '.scroll'))
                if ((pos != oldPos) and PlaySound(soundUI, 1)):
                    oldPos = pos
                for i in range(defSectNum):
                    sect = ((wCh + '.sect') + str((i + 1)))
                    info = Channel().getInfo((i + (pos * 2)), sectCnt)
                    if ((None == info) and Win_EnableWidget(sect, 0)):
                        Win_SetText((sect + '.name'), '')
                        Win_ShowWidget((sect + '.serverState'), 0)



            class children:
                __module__ = __name__
                class blockbtn(TScrollBtn):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      1,
                      1,
                      0,
                      0)]
                    rect = (0,
                     0,
                     26,
                     42)
                    bkimage = 'object/ui/common/scl_block.img'



        class sect1(TRadio):
            __module__ = __name__
            groupid = 5
            groupstop = 1
            rect = (383,
             97,
             187,
             26)
            bkimage = 'object/ui/selSect/img_sect.img'
            framescheme = [(-1,
              -1,
              0,
              0,
              -1,
              -1,
              -1,
              -1)]

            def OnClick(this):
                global practiceMode
                me = Win_GetFocusPath()
                if (('' == Win_GetText((me + '.name'))) and PlaySound(soundFail, 1)):
                    return 
                sectIdx = (((Win_GetScrollPos('UI.selSect.scroll') * 2) + getTailNum(me)) - 1)
                print 'LoginSection',
                print uin,
                print chIdx,
                print sectIdx
                Channel().login(uin, chIdx, areaIdx, sectIdx)
                PlaySound(soundMain, 1)
                practiceMode = 0


            class children:
                __module__ = __name__
                class name(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (20,
                     8,
                     150,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor

                class serverState(TStatic):
                    __module__ = __name__
                    rect = (100,
                     6,
                     63,
                     14)
                    bkimage = 'object/ui/selSect/img_state.img'



        class sect2(sect1):
            __module__ = __name__
            rect = (580,
             97,
             187,
             26)
            groupstop = 2

        class sect3(sect1):
            __module__ = __name__
            rect = (383,
             (97 + 29),
             187,
             26)
            groupstop = 3

        class sect4(sect1):
            __module__ = __name__
            rect = (580,
             (97 + 29),
             187,
             26)
            groupstop = 4

        class sect5(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 2)),
             187,
             26)
            groupstop = 5

        class sect6(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 2)),
             187,
             26)
            groupstop = 6

        class sect7(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 3)),
             187,
             26)
            groupstop = 7

        class sect8(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 3)),
             187,
             26)
            groupstop = 8

        class sect9(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 4)),
             187,
             26)
            groupstop = 9

        class sect10(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 4)),
             187,
             26)
            groupstop = 10

        class sect11(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 5)),
             187,
             26)
            groupstop = 11

        class sect12(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 5)),
             187,
             26)
            groupstop = 12

        class sect13(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 6)),
             187,
             26)
            groupstop = 13

        class sect14(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 6)),
             187,
             26)
            groupstop = 14

        class sect15(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 7)),
             187,
             26)
            groupstop = 15

        class sect16(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 7)),
             187,
             26)
            groupstop = 16

        class sect17(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 8)),
             187,
             26)
            groupstop = 17

        class sect18(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 8)),
             187,
             26)
            groupstop = 18

        class sect19(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 9)),
             187,
             26)
            groupstop = 19

        class sect20(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 9)),
             187,
             26)
            groupstop = 20

        class sect21(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 10)),
             187,
             26)
            groupstop = 21

        class sect22(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 10)),
             187,
             26)
            groupstop = 22

        class sect23(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 11)),
             187,
             26)
            groupstop = 23

        class sect24(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 11)),
             187,
             26)
            groupstop = 24

        class sect25(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 12)),
             187,
             26)
            groupstop = 25

        class sect26(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 12)),
             187,
             26)
            groupstop = 26

        class sect27(sect1):
            __module__ = __name__
            rect = (383,
             (97 + (29 * 13)),
             187,
             26)
            groupstop = 27

        class sect28(sect1):
            __module__ = __name__
            rect = (580,
             (97 + (29 * 13)),
             187,
             26)
            groupstop = 28

        class tipChannel:
            __module__ = __name__
            visible = 0
            type = 'DYLABEL'
            initlayer = 99999
            bkimage = 'object/ui/common/img_tip.img'
            rect = (550,
             40,
             130,
             1)
            captionrect = (4,
             4,
             120,
             1)
            drawcolor = maskColor
            textEdgeType = -1

            def OnInit():
                Win_SetText('UI.selSect.tipChannel', '  \xc7\xeb\xd1\xa1\xd4\xf1\xba\xcf\xca\xca\xb5\xc4\xc6\xb5\xb5\xc0')



            def OnTimer(this):
                if ((Win_GetCurScreen() == 'selSect') and Win_ShowWidget(this, (not Win_IsVisible(this)))):
                    pass
                Win_Timer(this, 5000)



        class selServerDlg(TDlg):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (500,
             200,
             229,
             331)
            bkimage = 'object/ui/selSect/dlg_selServer.img'

            def OnEnter():
                doUI('UI.selSect.selServerDlg.confirm', 'OnClick')



            def setList():
                for i in range(9):
                    ui = ('UI.selSect.selServerDlg.zone' + str(i))
                    Win_SetValue(ui, 0, value_channel_draw_flag)
                    if (((i + zonePos) >= len(zoneList)) and Win_ShowWidget(ui, 0)):
                        pass



            class children:
                __module__ = __name__
                class scroll(TVScroll):
                    __module__ = __name__
                    rect = (178,
                     60,
                     26,
                     200)
                    pos = 0

                    def OnPosChange():
                        global zonePos
                        ui = 'UI.selSect.selServerDlg'
                        zoneCnt = Channel().getAreaCnt(chIdx)
                        Win_SetRange((ui + '.scroll'), max((zoneCnt - defZoneNum), 0))
                        pos = Win_GetPos((ui + '.scroll'))
                        if ((pos != zonePos) and PlaySound(soundUI, 1)):
                            zonePos = pos
                        doUI(ui, 'setList')


                    class children:
                        __module__ = __name__
                        class blockbtn(TScrollBtn):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              0,
                              0,
                              1,
                              1,
                              0,
                              0)]
                            rect = (0,
                             0,
                             26,
                             41)
                            bkimage = 'object/ui/common/scl_block.img'



                class confirm(TButton):
                    __module__ = __name__
                    rect = (90,
                     285,
                     43,
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
                        global areaIdx
                        global isAutoJustScrollPos
                        Win_ShowWidget('UI.selSect.selServerDlg', 0)
                        areaIdx = curZone2areaIdx()
                        isAutoJustScrollPos = True
                        Win_SetScrollPos('UI.selSect.scroll', 0)
                        doUI('UI.selSect.scroll', 'OnPosChange')



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (200,
                     4,
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
                        Win_ShowWidget('UI.selSect.selServerDlg', False)
                        PlaySound(soundLeave, 1)



                class zone0(TRadio):
                    __module__ = __name__
                    bkcolor = (222,
                     255,
                     36,
                     255)
                    rect = (28,
                     57,
                     142,
                     22)
                    bkimage = 'object/ui/selSect/btn_choose.img'
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      -1,
                      -1,
                      -1,
                      -1),
                     (0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      -1,
                      -1)]
                    groupstop = 0

                    def OnClick(this):
                        global curZone
                        curZone = ZoneUIIndex2LogicIndex((getMyIdx() + zonePos))
                        doUI('UI.selSect.selServerDlg', 'setList')
                        me = Win_GetMyPath()
                        PlaySound(soundUI, 1)



                    def OnDBClick():
                        curZone = ZoneUIIndex2LogicIndex((getMyIdx() + zonePos))
                        me = Win_GetMyPath()
                        doUI('UI.selSect.selServerDlg.confirm', 'OnClick')


                    class children:
                        __module__ = __name__
                        class name(TLabel,
                         Static):
                            __module__ = __name__
                            textstyle = (dt_center + dt_vcenter)
                            rect = (0,
                             0,
                             100,
                             22)
                            drawcolor = (255,
                             255,
                             255,
                             255)

                        class speedicon(TStatic):
                            __module__ = __name__
                            rect = (100,
                             4,
                             40,
                             22)
                            bkimage = 'res/uiRes/selSect/netspeed_test.img'



                class zone1(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 1)),
                     142,
                     22)
                    groupstop = 1

                class zone2(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 2)),
                     142,
                     22)
                    groupstop = 2

                class zone3(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 3)),
                     142,
                     22)
                    groupstop = 3

                class zone4(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 4)),
                     142,
                     22)
                    groupstop = 4

                class zone5(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 5)),
                     142,
                     22)
                    groupstop = 5

                class zone6(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 6)),
                     142,
                     22)
                    groupstop = 6

                class zone7(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 7)),
                     142,
                     22)
                    groupstop = 7

                class zone8(zone0):
                    __module__ = __name__
                    rect = (28,
                     (57 + (23 * 8)),
                     142,
                     22)
                    groupstop = 8





UI.children.selSect = UI_children_selSect

#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
