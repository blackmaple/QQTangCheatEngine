isBringItem = True
bRecord = 0
chatDlgO = 550
chatDlgY = chatDlgO
isBugle = 0

def NotifyAddHint(flag, x, y, szMsg):
    if (Win_GetCurScreen() == 'game'):
        ui = 'UI.game.hint'
        Win_Move2Pos(ui, x, y)
        Win_SetText((ui + '.words'), szMsg)
        Win_SetImg(ui, ('object/ui/game/chatpopo%d.img' % flag))
        if (((flag == 1) or (flag == 3)) and Win_SetRect((ui + '.words'), value_channel_winrect, (x + 55), (y + 20), 180, 140)):
            Win_SetRect((ui + '.words'), value_channel_clientrect, 0, 0, 180, 140)
            Win_SetRect((ui + '.words'), value_channel_captionrect, 0, 0, 180, 140)
        Win_ShowWidget(ui, 1)



def NotifyRemoveHint():
    if (Win_GetCurScreen() == 'game'):
        ui = 'UI.game.hint'
        Win_ShowWidget(ui, 0)



def ClearTotem():
    i = 0
    while (i < 8):
        ui = (uiGamePlayerList + ('.kintotem%d' % i))
        Win_SetImg(ui, '')
        i += 1




def showRecordPlayer(bshow):
    global bRecord
    bRecord = bshow
    Win_ShowWidget('UI.game.RecordPlayer', (bshow != 0))
    if ((bshow != 0) and showRecordRecorder(0)):
        pass



def showRecordRecorder(bshow):
    if ((bshow != 0) and Win_ShowWidget((uiGamePlayerList + '.saveReplayBtn'), True)):
        Win_ShowWidget((uiGamePlayerList + '.cancelSaveReplayBtn'), False)



def setRecordQQNumber(qqnumber):
    Win_SetText('UI.game.RecordPlayer.QQNumber', str(qqnumber))



def sendGameChat():
    global chatDlgY
    ui = 'UI.game.chat.edit'
    text = Win_GetText(ui)
    Win_SetText(ui, '')
    Win_ShowWidget('UI.game.chat', False)
    Win_SetFocus('')
    print 'RoomChat(',
    print text
    RoomChat(0, text)
    chatDlgY = chatDlgO
    PlaySound(soundMain, 1)



def sendSectionChat():
    ui = 'UI.game.chat.edit'
    text = Win_GetText(ui)
    Win_SetText(ui, '')
    Win_ShowWidget('UI.game.chat', False)
    Win_SetFocus('')
    print 'Ingameing send bugle',
    print text
    chatDlgY = chatDlgO
    PlaySound(soundMain, 1)
    SectionChat(1, text)



def ui_NotifyShowLevelIcon(score, idx, bshow):
    ui = (uiGamePlayerList + ('.level%d' % idx))
    si = GetSeatInfo(idx)
    playerInfo = si.player
    info = CNil()
    info.uin = playerInfo.m_dwUin
    info.kinIndex = playerInfo.m_dwKinIndex
    info.totemID = playerInfo.m_stKinFlagID.m_iFlagID
    info.kinName = playerInfo.m_szKinName
    if (bshow and (bRecord == 0)):
        level = Level().getInfo(score)
        Level().setUI(ui, level)
        Win_ShowWidget(ui, 1)
        totemID = info.totemID
        if (((totemID >= 0) and (totemID <= 48)) and Win_SetImg((uiGamePlayerList + ('.kintotem%d' % idx)), ('object/ui/kinTotem/%03d.img' % totemID))):
            Win_ShowWidget((uiGamePlayerList + ('.kintotem%d' % idx)), 1)
    else:
        Win_ShowWidget(ui, 0)
        Win_ShowWidget((uiGamePlayerList + ('.kintotem%d' % idx)), 0)
    if ((info.uin == 0) and Win_ShowWidget(ui, 0)):
        Win_ShowWidget((uiGamePlayerList + ('.kintotem%d' % idx)), 0)



def ui_NotifyShowResultLevelIcon(x, y, score, idx, bshow):
    ui = ('UI.game.resultDlg.level%d' % idx)
    if (bshow and Win_Move2Pos(ui, x, y)):
        level = Level().getInfo(score)
        Level().setUI(ui, level)
        Win_ShowWidget(ui, 1)



def ui_NotifyRenderResultLevelIcon(idx, alpha):
    ui = ('UI.game.resultDlg.level%d' % idx)
    Win_SetValue(ui, min(alpha, 1.0), 42)



def ui_SetGameMode(mode):
    print 'game mode = ',
    print mode
    if ((mode == 0) and Win_ShowWidget(uiGamePlayerList, 1)):
        Win_ShowWidget(uiPvePlayerList, 0)
        Win_ShowWidget(uiPveFuncDlg, 0)
        Win_ShowWidget('UI.game.pveTime', 0)


g_PVEBossCnt = 0
g_PVEBossID = []
g_DefBossCnt = 3
g_PVEPlayerCnt = 0
g_PVEPlayerID = []
g_DefPlayerCnt = 4
g_RoleNameList = ('',
 'xwk',
 'tt',
 'xq',
 'cl',
 'bbl',
 'hy',
 'mly',
 'hwz',
 'boy',
 'cbz',
 'xz',
 'ls',
 'kl',
 'nz',
 'wll',
 'yy',
 '',
 'yd',
 'ld',
 'ge',
 'tb',
 'girl')

def ui_InitPVEBoss():
    global g_PVEBossID
    global g_PVEBossCnt
    bossInfo = GetPVEBossInfo()
    g_PVEBossID = []
    g_PVEBossCnt = len(bossInfo)
    print 'Init boss cnt=',
    print g_PVEBossCnt
    if (g_PVEBossCnt <= 0):
        for i in range(g_DefBossCnt):
            ui = ('UI.game.pveBossInfo%d' % i)
            Win_ShowWidget(ui, 0)

        return 
    posx = 70
    posy = 25
    step = (580 / g_PVEBossCnt)
    for i in range(g_DefBossCnt):
        ui = ('UI.game.pveBossInfo%d' % i)
        if ((i >= g_PVEBossCnt) and Win_ShowWidget(ui, 0)):
            continue
        Win_SetImg((ui + '.BossPortrait'), ('object/ui/room/char/icon_%d.img' % bossInfo[i].m_iImageID))
        print 'bossInfo[i].m_iImageID = ',
        print bossInfo[i].m_iImageID
        g_PVEBossID.append(bossInfo[i].m_iNPCID)
        Win_ShowWidget(ui, 1)
        curposx = (posx + (i * step))
        Win_Move2Pos(ui, curposx, posy)
        Win_SetRect((ui + '.lifeLineBack'), value_channel_winrect, (curposx + 54), posy, (step - 55), 17)
        Win_SetRect((ui + '.lifeLineFront'), value_channel_winrect, (curposx + 56), posy, (step - 61), 17)
        Win_SetStripTotalNum((ui + '.lifeLineBack'), bossInfo[i].m_iHP)
        Win_SetStripNum((ui + '.lifeLineBack'), bossInfo[i].m_iHP)
        Win_SetStripDestNum((ui + '.lifeLineBack'), bossInfo[i].m_iHP)
        Win_SetStripTotalNum((ui + '.lifeLineFront'), bossInfo[i].m_iHP)
        Win_SetStripNum((ui + '.lifeLineFront'), bossInfo[i].m_iHP)
        Win_SetStripDestNum((ui + '.lifeLineFront'), bossInfo[i].m_iHP)




def ui_UpdatePVEBossLife(id, life):
    for i in range(len(g_PVEBossID)):
        if (g_PVEBossID[i] == id):
            print g_PVEBossID,
            print id,
            print life
            ui = ('UI.game.pveBossInfo%d' % i)
            Win_SetStripDestNum((ui + '.lifeLineFront'), life)




def ui_InitPVEPlayer():
    global g_PVEPlayerID
    global g_PVEPlayerCnt
    playerInfo = GetPVEPlayerInfo()
    g_PVEPlayerCnt = len(playerInfo)
    g_PVEPlayerID = []
    for i in range(g_PVEPlayerCnt):
        g_PVEPlayerID.append(playerInfo[i].m_nPlayerID)

    print 'Init PvE Player: count=%d, ',
    print g_PVEPlayerID
    for i in range(g_DefPlayerCnt):
        ui = ('UI.game.pvePlayerList.playerInfo%d' % i)
        if ((i >= g_PVEPlayerCnt) and Win_ShowWidget(ui, 0)):
            continue
        Win_ShowWidget(ui, 1)
        Win_SetImg((ui + '.playerIcon'), ('object/ui/room/char/icon_%s.img' % g_RoleNameList[playerInfo[i].m_nRoleID]))
        Win_SetText((ui + '.playerName'), str(playerInfo[i].m_szNickName))
        level = Level().getInfo(playerInfo[i].m_nPoints)
        Level().setUI(ui, level)
        Win_SetText((ui + '.playerLife'), str(playerInfo[i].m_nHP))
        Win_SetStripTotalNum((ui + '.playerLifeLine'), playerInfo[i].m_nHP)
        Win_SetStripNum((ui + '.playerLifeLine'), playerInfo[i].m_nHP)
        Win_SetStripDestNum((ui + '.playerLifeLine'), playerInfo[i].m_nHP)




def ui_UpdatePVEPlayerLife(id, life):
    print ('update PvE player life: playerID=%d, life=%d' % (id,
     life))
    for i in range(len(g_PVEPlayerID)):
        ui = ('UI.game.pvePlayerList.playerInfo%d' % i)
        if ((g_PVEPlayerID[i] == id) and Win_SetText((ui + '.playerLife'), str(life))):
            Win_SetStripDestNum((ui + '.playerLifeLine'), life)




def ui_UpdateTankBaseLife(id, life):
    print ('tank base %d life is %d' % (id,
     life))
    ui = ('UI.game.tankBaseInfo' + str(id))
    Win_SetText((ui + '.tankBaseLife'), str(life))
    Win_SetStripDestNum((ui + '.tankBaseLifeLine'), life)



def ui_DisposePVEPlayerLeave(id):
    for i in range(len(g_PVEPlayerID)):
        ui = ('UI.game.pvePlayerList.playerInfo%d' % i)
        if ((g_PVEPlayerID[i] == id) and Win_ShowWidget(ui, 0)):
            pass




def ui_SetItemTimeSpeed(idx, speed):
    ui = ('UI.game.statusBar.itemMask%d' % idx)
    Win_SetAngleStep(ui, speed)



def ui_SetItemTimeCur(idx, curAngle):
    ui = ('UI.game.statusBar.itemMask%d' % idx)
    Win_SetAngleCur(ui, curAngle)



def InitItemTime():
    for i in range(7):
        ui = ('UI.game.statusBar.itemMask%d' % i)
        Win_SetAngleCur(ui, 360.0)
        Win_SetAngleDest(ui, 360.0)
        Win_SetAngleStep(ui, 0.0)




def ui_SetBaseItemTimeSpeed(speed):
    ui = 'UI.game.statusBar.baseItemCycle'
    Win_SetAngleStep(ui, speed)



def ui_SetBaseItemTimeCur(curAngle):
    ui = 'UI.game.statusBar.baseItemCycle'
    Win_SetAngleCur(ui, curAngle)



def InitBaseItemTime():
    ui = 'UI.game.statusBar.baseItemCycle'
    Win_SetAngleCur(ui, 360.0)
    Win_SetAngleDest(ui, 360.0)
    Win_SetAngleStep(ui, 0.0)



def setSelectedMapType(type):
    if ((type == 'tank') and Win_ShowWidget('UI.game.tankBaseInfo1', 1)):
        Win_ShowWidget('UI.game.tankBaseInfo2', 1)
        Win_SetImg('UI.game.tankBaseInfo2.tankBaseLifeLine', 'object/ui/game/img_playerLifeBlue.img')
        ui_UpdateTankBaseLife(1, 100)
        ui_UpdateTankBaseLife(2, 100)


class UI_children_game:
    __module__ = __name__
    type = 'SCREEN'
    rect = (0,
     0,
     800,
     600)
    accel = (('OnAccel_OnEnter',
      13,
      0,
      0,
      0))
    cursor = 'normal'

    def OnInit():
        print 'game OnInit'
        Win_ShowWidget(uiGuideBar, 0)
        Win_ShowWidget(uiSocialityDlg, 0)
        Win_ShowWidget(uiMenuDlg, 0)
        Win_ShowWidget(uiPlayerInfoDlg, False)
        Win_ShowWidget('UI.game.hint', 0)
        Win_ShowWidget(uiAddFriendDlg, 0)
        Win_ShowWidget(uiBeAddedFriendDlg, 0)
        Win_ShowWidget(uiKinInfoDlg, 0)
        Win_ShowWidget(uiSetupDlg, 0)
        Win_ShowWidget(uiKinInviteDlg, 0)
        sc_HideWeb('kinMatch')
        sc_HideWeb('kinTeam')
        Win_ShowWidget(uiKinTipDlg, 0)
        Win_ShowWidget('UI.room.createkinhintDlg', 0)
        Win_ShowWidget('UI.room.createkinDlg', 0)
        Win_ShowWidget(uiRoomStorageDlg, 0)
        Win_SetText('UI.game.chatList', '', value_channel_listitem_num)
        Win_Timer('UI.game.chatList', 1500)
        Win_ShowWidget('UI.game.chat', False)
        CloseC2CDealDlg(bC2CDealShow)
        for i in range(8):
            Win_ShowWidget((uiGamePlayerList + ('.level%d' % i)), 0)

        InitSpeaker()
        ClearTotem()
        InitItemTime()
        InitBaseItemTime()
        screenStartIn()



    def OnDenit():
        print 'OnDenit() game'
        Win_ShowWidget(uiRoomStorageDlg, 0)



    def OnAccel_OnEnter():
        if Win_IsVisible('UI.SysMsgbox'):
            return 
        ui = uiPlayerInfoDlg
        if (Win_IsVisible(ui) and Win_ShowWidget(ui, 0)):
            return 
        ui = 'UI.game.chat'
        if (Win_IsVisible(ui) and (isBugle == 1)):
            if sendSectionChat():
                pass



    def OnAccel_OnEscape():
        print '<entry esc>'
        if (Win_IsVisible('UI.SysMsgbox') and Win_ShowWidget('UI.SysMsgbox', false)):
            pass
        return 1


    class children:
        __module__ = __name__
        class playerListDlg(TStatic):
            __module__ = __name__
            initlayer = -999999
            rect = (609,
             0,
             1,
             1)
            bkimage = 'object/ui/game/dlg_playerList.img'
            class children:
                __module__ = __name__
                class time:
                    __module__ = __name__
                    initlayer = 9999
                    type = 'NUMLABEL'
                    rect = (30,
                     57,
                     165,
                     52)
                    bkimage = 'object/ui/common/number3.img'
                    textsize = 27
                    textwidth = 27
                    textheight = 36
                    caption = '99:99'

                class mapIcon(TStatic):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (68,
                     10,
                     30,
                     30)
                    bkimage = 'map/icon/water.img'
                    bkImgFlag = dt_center

                class mapName(TLabel,
                 Static):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (102,
                     16,
                     82,
                     12)
                    drawcolor = lightColor
                    textstyle = dt_center

                class playerBtn0(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (46,
                     90,
                     137,
                     60)

                    def OnClick(this):
                        seatIdx = getMyIdx()
                        uin = sc_game_getPlayerUin(seatIdx)
                        if ((uin > 0) and go2playerInfo(uin)):
                            SetPlayerModeInfo(uin, 0)



                class playerBtn1(playerBtn0):
                    __module__ = __name__
                    rect = (38,
                     (91 + 48),
                     137,
                     60)

                class playerBtn2(playerBtn0):
                    __module__ = __name__
                    rect = (38,
                     (91 + (48 * 2)),
                     137,
                     60)

                class playerBtn3(playerBtn0):
                    __module__ = __name__
                    rect = (38,
                     (91 + (48 * 3)),
                     137,
                     60)

                class playerBtn4(playerBtn0):
                    __module__ = __name__
                    rect = (38,
                     (91 + (48 * 4)),
                     137,
                     60)

                class playerBtn5(playerBtn0):
                    __module__ = __name__
                    rect = (38,
                     (91 + (48 * 5)),
                     137,
                     60)

                class playerBtn6(playerBtn0):
                    __module__ = __name__
                    rect = (38,
                     (91 + (48 * 6)),
                     137,
                     60)

                class playerBtn7(playerBtn0):
                    __module__ = __name__
                    rect = (38,
                     (91 + (48 * 7)),
                     137,
                     60)

                class level0(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (98,
                     130,
                     40,
                     15)
                    class children:
                        __module__ = __name__
                        class levelIcon(TLevelIcon):
                            __module__ = __name__
                            rect = (0,
                             0,
                             40,
                             15)



                class level1(level0):
                    __module__ = __name__
                    rect = (98,
                     (130 + 51),
                     40,
                     15)

                class level2(level0):
                    __module__ = __name__
                    rect = (98,
                     (130 + (51 * 2)),
                     40,
                     15)

                class level3(level0):
                    __module__ = __name__
                    rect = (98,
                     (130 + (51 * 3)),
                     40,
                     15)

                class level4(level0):
                    __module__ = __name__
                    rect = (98,
                     (130 + (51 * 4)),
                     40,
                     15)

                class level5(level0):
                    __module__ = __name__
                    rect = (98,
                     (130 + (51 * 5)),
                     40,
                     15)

                class level6(level0):
                    __module__ = __name__
                    rect = (98,
                     (130 + (51 * 6)),
                     40,
                     15)

                class level7(level0):
                    __module__ = __name__
                    rect = (98,
                     (130 + (51 * 7)),
                     40,
                     15)

                class kintotem0(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (98,
                     110,
                     16,
                     15)

                class kintotem1(kintotem0):
                    __module__ = __name__
                    rect = (98,
                     (110 + 51),
                     16,
                     15)

                class kintotem2(kintotem0):
                    __module__ = __name__
                    rect = (98,
                     (110 + (51 * 2)),
                     16,
                     15)

                class kintotem3(kintotem0):
                    __module__ = __name__
                    rect = (98,
                     (110 + (51 * 3)),
                     16,
                     15)

                class kintotem4(kintotem0):
                    __module__ = __name__
                    rect = (98,
                     (110 + (51 * 4)),
                     16,
                     15)

                class kintotem5(kintotem0):
                    __module__ = __name__
                    rect = (98,
                     (110 + (51 * 5)),
                     16,
                     15)

                class kintotem6(kintotem0):
                    __module__ = __name__
                    rect = (98,
                     (110 + (51 * 6)),
                     16,
                     15)

                class kintotem7(kintotem0):
                    __module__ = __name__
                    rect = (98,
                     (110 + (51 * 7)),
                     16,
                     15)

                class saveReplayBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (27,
                     533,
                     90,
                     48)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/game/btn_saveReplay.img'

                    def OnClick(this):
                        BeginRecord()
                        Win_ShowWidget((uiGamePlayerList + '.saveReplayBtn'), False)
                        Win_ShowWidget((uiGamePlayerList + '.cancelSaveReplayBtn'), True)



                class cancelSaveReplayBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (27,
                     533,
                     90,
                     48)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/game/btn_cancelSaveReplay.img'
                    visible = False

                    def OnClick(this):
                        StopRecord()
                        Win_ShowWidget((uiGamePlayerList + '.saveReplayBtn'), True)
                        Win_ShowWidget((uiGamePlayerList + '.cancelSaveReplayBtn'), False)



                class leave(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (125,
                     534,
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
                    bkimage = 'object/ui/common/btn_leavegame.img'

                    def OnClick(this):
                        print '<leave> game'
                        LeaveGame()
                        PlaySound(soundLeave, 1)





        class pvePlayerList(TStatic):
            __module__ = __name__
            initlayer = 9999
            rect = (0,
             0,
             1,
             1)
            class children:
                __module__ = __name__
                class playerInfo0(TStatic):
                    __module__ = __name__
                    rect = (0,
                     80,
                     1,
                     1)
                    class children:
                        __module__ = __name__
                        class playerMask(TStatic):
                            __module__ = __name__
                            initlayer = -9999
                            rect = (0,
                             40,
                             100,
                             25)
                            bkimage = 'object/ui/game/mask_player.img'
                            alphafactor = 0.80000000000000004
                            textEdgeColor = maskColor

                        class playerIcon(TStatic):
                            __module__ = __name__
                            initlayer = -99999
                            rect = (2,
                             0,
                             50,
                             50)
                            framescheme = [(0,
                              0,
                              0,
                              0,
                              0,
                              0,
                              0,
                              0)]
                            bkimage = 'object/ui/room/char/icon_xq.img'
                            alphafactor = 0.80000000000000004

                        class playerLife(TLabel):
                            __module__ = __name__
                            rect = (1,
                             44,
                             24,
                             12)
                            bkimage = ''
                            caption = '9999'
                            drawcolor = (0,
                             255,
                             255,
                             255)
                            textEdgeType = 2
                            textEdgeColor = (0,
                             255,
                             255,
                             255)

                        class playerLifeLine:
                            __module__ = __name__
                            type = 'DYLIFESTRIP'
                            rect = (0,
                             56,
                             90,
                             5)
                            bkimage = 'object/ui/game/img_playerLife.img'
                            totalnum = 1000
                            destnum = 1000
                            stepnum = 500

                        class levelIcon(TLevelIcon):
                            __module__ = __name__
                            rect = (0,
                             60,
                             40,
                             15)

                        class playerName(TLabel):
                            __module__ = __name__
                            rect = (26,
                             66,
                             96,
                             12)
                            drawcolor = zoneChooseColor
                            textEdgeType = -1
                            caption = '\xb0\xa2\xb2\xae\xb2\xca\xb5\xe7'



                class playerInfo1(playerInfo0):
                    __module__ = __name__
                    rect = (0,
                     (80 + 80),
                     1,
                     1)

                class playerInfo2(playerInfo0):
                    __module__ = __name__
                    rect = (0,
                     (80 + (80 * 2)),
                     1,
                     1)

                class playerInfo3(playerInfo0):
                    __module__ = __name__
                    rect = (0,
                     (80 + (80 * 3)),
                     1,
                     1)



        class pveFuncDlg(TStatic):
            __module__ = __name__
            visible = 0
            rect = (620,
             538,
             181,
             64)
            bkimage = 'object/ui/game/dlg_pveFunc.img'
            class children:
                __module__ = __name__
                class storageBtn(TButton):
                    __module__ = __name__
                    rect = (15,
                     10,
                     95,
                     45)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/game/btn_storage.img'

                    def OnClick(this):
                        if (Win_IsVisible(uiRoomStorageDlg) and Win_ShowWidget(uiRoomStorageDlg, 0)):
                            pass
                        PlaySound(soundUI, 1)



                class leaveBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (112,
                     8,
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
                    bkimage = 'object/ui/common/btn_leavegame.img'

                    def OnClick(this):
                        print '<leave> game'
                        LeaveGame()
                        PlaySound(soundLeave, 1)





        class pveTime:
            __module__ = __name__
            type = 'NUMLABEL'
            rect = (650,
             20,
             135,
             36)
            bkimage = 'object/ui/common/number3.img'
            textsize = 27
            textwidth = 27
            textheight = 36
            caption = '99:99'

        class pveBossInfo0(TStatic):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)
            class children:
                __module__ = __name__
                class BossPortrait(TStatic):
                    __module__ = __name__
                    initlayer = 99999
                    rect = (0,
                     0,
                     55,
                     55)
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0)]
                    bkimage = 'object/ui/room/char/icon_xq.img'

                class lifeLineBack:
                    __module__ = __name__
                    initlayer = 999
                    type = 'DYLIFESTRIP'
                    rect = (0,
                     0,
                     1,
                     20)
                    totalnum = 1000
                    bkimage = 'object/ui/game/img_lifeNull.img'

                class lifeLineFront(lifeLineBack):
                    __module__ = __name__
                    initlayer = 9999
                    bkimage = 'object/ui/game/img_lifeRed.img'
                    stepnum = 200



        class pveBossInfo1(pveBossInfo0):
            __module__ = __name__

        class pveBossInfo2(pveBossInfo0):
            __module__ = __name__

        class RecordPlayer(TStatic):
            __module__ = __name__
            visible = 1
            initlayer = 9999
            rect = (631,
             580,
             174,
             33)
            bkimage = 'object/ui/game/record/ProcessBar.img'
            class children:
                __module__ = __name__
                class ResumeButton(TButton):
                    __module__ = __name__
                    initlayer = 10
                    rect = (3,
                     -40,
                     29,
                     20)
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      3,
                      3)]
                    bkimage = 'object/ui/game/record/btn_Resume.img'

                    def OnClick(this):
                        ResumePlayRecord()



                class X2Button(TButton):
                    __module__ = __name__
                    initlayer = 10
                    rect = (29,
                     -40,
                     29,
                     20)
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      3,
                      3)]
                    bkimage = 'object/ui/game/record/btn_2xSpeedPlay.img'

                    def OnClick(this):
                        SetPlayRecordSpeed(2)



                class X4Button(TButton):
                    __module__ = __name__
                    initlayer = 10
                    rect = (56,
                     -40,
                     29,
                     20)
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      3,
                      3)]
                    bkimage = 'object/ui/game/record/btn_4xSpeedPlay.img'

                    def OnClick(this):
                        SetPlayRecordSpeed(4)



                class PauseButton(TButton):
                    __module__ = __name__
                    initlayer = 10
                    rect = (82,
                     -40,
                     29,
                     20)
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      3,
                      3)]
                    bkimage = 'object/ui/game/record/btn_Pause.img'

                    def OnClick(this):
                        PausePlayRecord()





        class resultDlg(TStatic):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)
            class children:
                __module__ = __name__
                class level0(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (709,
                     102,
                     40,
                     15)
                    class children:
                        __module__ = __name__
                        class levelIcon(TLevelIcon):
                            __module__ = __name__
                            rect = (0,
                             0,
                             40,
                             15)



                class level1(level0):
                    __module__ = __name__
                    rect = (709,
                     (102 + 51),
                     40,
                     15)

                class level2(level0):
                    __module__ = __name__
                    rect = (709,
                     (102 + (51 * 2)),
                     40,
                     15)

                class level3(level0):
                    __module__ = __name__
                    rect = (709,
                     (102 + (51 * 3)),
                     40,
                     15)

                class level4(level0):
                    __module__ = __name__
                    rect = (709,
                     (102 + (51 * 4)),
                     40,
                     15)

                class level5(level0):
                    __module__ = __name__
                    rect = (709,
                     (102 + (51 * 5)),
                     40,
                     15)

                class level6(level0):
                    __module__ = __name__
                    rect = (709,
                     (102 + (51 * 6)),
                     40,
                     15)

                class level7(level0):
                    __module__ = __name__
                    rect = (709,
                     (102 + (51 * 7)),
                     40,
                     15)

                class level8(level0):
                    __module__ = __name__
                    rect = (709,
                     102,
                     40,
                     15)



        class tankBaseInfo1(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 9999
            rect = (495,
             478,
             1,
             1)
            class children:
                __module__ = __name__
                class tankBaseLife(TLabel):
                    __module__ = __name__
                    rect = (1,
                     50,
                     20,
                     12)
                    bkimage = ''
                    caption = '100'
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeType = 2
                    textEdgeColor = (0,
                     255,
                     255,
                     255)

                class tankBaseLifeLine:
                    __module__ = __name__
                    type = 'DYLIFESTRIP'
                    rect = (21,
                     56,
                     90,
                     5)
                    bkimage = 'object/ui/game/img_playerLifeRed.img'
                    totalnum = 100
                    destnum = 100
                    stepnum = 20



        class tankBaseInfo2(tankBaseInfo1):
            __module__ = __name__
            rect = (495,
             468,
             1,
             1)

        class statusBar(TStatic):
            __module__ = __name__
            rect = (0,
             540,
             623,
             60)
            bkimage = 'object/ui/game/dlg_statusBar.img'
            class children:
                __module__ = __name__
                class baseItemNum0(TPicLabel,
                 Static):
                    __module__ = __name__
                    initlayer = 10000
                    rect = (48,
                     42,
                     12,
                     12)
                    bkimage = 'res/uires/number/itemNum.img'
                    caption = '0'

                class baseItemNum1(baseItemNum0):
                    __module__ = __name__
                    rect = (99,
                     42,
                     12,
                     12)

                class baseItemNum2(baseItemNum0):
                    __module__ = __name__
                    rect = (150,
                     42,
                     12,
                     12)

                class itemNum0(baseItemNum0):
                    __module__ = __name__
                    rect = (200,
                     42,
                     12,
                     12)

                class itemNum1(itemNum0):
                    __module__ = __name__
                    rect = ((200 + (52 * 1)),
                     42,
                     12,
                     12)

                class itemNum2(itemNum0):
                    __module__ = __name__
                    rect = ((200 + (52 * 2)),
                     42,
                     12,
                     12)

                class itemNum3(itemNum0):
                    __module__ = __name__
                    rect = ((200 + (52 * 3)),
                     42,
                     12,
                     12)

                class itemNum4(itemNum0):
                    __module__ = __name__
                    rect = ((200 + (52 * 4)),
                     42,
                     12,
                     12)

                class itemNum5(itemNum0):
                    __module__ = __name__
                    rect = ((200 + (52 * 5)),
                     42,
                     12,
                     12)

                class itemNum6(itemNum0):
                    __module__ = __name__
                    rect = ((200 + (52 * 6)),
                     42,
                     12,
                     12)

                class baseItemIcon0(TStatic):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (185,
                     0,
                     50,
                     50)
                    bkImgFlag = 5

                class baseItemIcon1(baseItemIcon0):
                    __module__ = __name__
                    rect = ((185 + 54),
                     0,
                     50,
                     50)

                class baseItemIcon2(baseItemIcon0):
                    __module__ = __name__
                    rect = ((185 + (54 * 2)),
                     0,
                     50,
                     50)

                class baseItemIcon3(baseItemIcon0):
                    __module__ = __name__
                    rect = ((185 + (54 * 3)),
                     0,
                     50,
                     50)

                class baseItemIcon4(baseItemIcon0):
                    __module__ = __name__
                    rect = ((185 + (54 * 4)),
                     0,
                     50,
                     50)

                class baseItemIcon5(baseItemIcon0):
                    __module__ = __name__
                    rect = ((185 + (54 * 5)),
                     0,
                     50,
                     50)

                class baseItemIcon6(baseItemIcon0):
                    __module__ = __name__
                    rect = ((185 + (54 * 6)),
                     0,
                     50,
                     50)

                class itemMask0:
                    __module__ = __name__
                    initlayer = 20000
                    type = 'DYMASK'
                    rect = (177,
                     6,
                     50,
                     50)
                    bkimage = 'object/ui/game/img_itemMask.img'

                class itemMask1(itemMask0):
                    __module__ = __name__
                    rect = ((177 + 54),
                     6,
                     50,
                     50)

                class itemMask2(itemMask0):
                    __module__ = __name__
                    rect = ((177 + (54 * 2)),
                     6,
                     50,
                     50)

                class itemMask3(itemMask0):
                    __module__ = __name__
                    rect = ((177 + (54 * 3)),
                     6,
                     50,
                     50)

                class itemMask4(itemMask0):
                    __module__ = __name__
                    rect = ((177 + (54 * 4)),
                     6,
                     50,
                     50)

                class itemMask5(itemMask0):
                    __module__ = __name__
                    rect = ((177 + (54 * 5)),
                     6,
                     50,
                     50)

                class itemMask6(itemMask0):
                    __module__ = __name__
                    rect = ((177 + (54 * 6)),
                     6,
                     50,
                     50)

                class baseItemCycle:
                    __module__ = __name__
                    initlayer = 20000
                    type = 'DYMASK'
                    rect = (2,
                     2,
                     50,
                     50)
                    bkimage = 'object/ui/game/img_maskCycle.img'



        class chat(TDlg):
            __module__ = __name__
            initlayer = 99999
            alphaspeed = (1 / (40.0 * 0.20000000000000001))
            visible = 0
            rect = (200,
             500,
             332,
             22)
            bkimage = 'res/uires/gameChat/liaotianshurukuang_di.img'

            def OnFrame():
                global chatDlgY
                ui = 'UI.game.chat'
                if (not Win_IsVisible(ui)):
                    return 
                if (chatDlgY > 500):
                    chatDlgY -= (((chatDlgO - 500) * sc_getDeltaTick()) / 200)
                    Win_Move2Pos(ui, 200, int(chatDlgY))
                else:
                    chatDlgY = 500
                    Win_Move2Pos(ui, 200, chatDlgY)


            class children:
                __module__ = __name__
                class bugle(TButton):
                    __module__ = __name__
                    rect = ((284 - 22),
                     3,
                     20,
                     16)
                    num = GetBugleNumber()
                    if (num > 0):
                        bkimage = 'res/uires/gameChat/anniu_bugle_normal.img'
                    else:
                        enable = 0
                        bkimage = 'res/uires/gameChat/anniu_bugle_none.img'

                    def OnClick(this):
                        global isBugle
                        if (isBugle == 0):
                            isBugle = 1
                            Win_SetImg('UI.game.chat.bugle', 'res/uires/gameChat/anniu_bugle_hit.img')
                            Win_SetValue('UI.game.chat.edit', 44, 903)
                            Win_SetText('UI.game.chat.edit', '')
                        else:
                            isBugle = 0
                            Win_SetImg('UI.game.chat.bugle', 'res/uires/gameChat/anniu_bugle_normal.img')
                            Win_SetValue('UI.game.chat.edit', 100, 903)



                class send(TButton):
                    __module__ = __name__
                    rect = ((306 - 22),
                     3,
                     20,
                     16)
                    bkimage = 'res/uires/gameChat/anniu_fasong.img'

                    def OnClick(this):
                        if ((isBugle == 1) and sendSectionChat()):
                            pass



                class expr(TButton):
                    __module__ = __name__
                    enable = 0
                    rect = ((328 - 22),
                     3,
                     20,
                     16)
                    bkimage = 'res/uires/gameChat/anniu_biaoqing.img'

                class edit(TEdit):
                    __module__ = __name__
                    rect = (12,
                     4,
                     ((278 - 12) - 22),
                     12)
                    maxchar = 100
                    drawcolor = (51,
                     113,
                     149,
                     255)
                    textEdgeType = -1



        class chatList:
            __module__ = __name__
            textEdgeColor = (0,
             0,
             0,
             255)
            maxline = 20
            initlayer = 89999
            type = 'TEXTLIST'
            rect = (23,
             402,
             434,
             117)
            rowspace = 6
            textfont = 1

            def OnTimer(this):
                if ((Win_GetCurScreen() == 'game') and Win_SetColorText(this, '', 207, 0, 0, 0)):
                    pass



        class broadcastZone(TStatic):
            __module__ = __name__
            rect = (9,
             520,
             500,
             17)
            class children:
                __module__ = __name__
                class speaker(TRichEdit):
                    __module__ = __name__
                    initlayer = 99999
                    rect = (0,
                     0,
                     400,
                     17)
                    bkimage = 'object/ui/room/img_popo.img'
                    captionrect = (12,
                     3,
                     380,
                     12)
                    textEdgeType = -1
                    iconflag = 1
                    editable = 0



        class hint(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 99999
            rect = (0,
             0,
             334,
             165)
            class children:
                __module__ = __name__
                class words(TLabel):
                    __module__ = __name__
                    rect = (55,
                     20,
                     180,
                     140)
                    drawcolor = (51,
                     113,
                     149,
                     255)
                    textEdgeType = -1





UI.children.game = UI_children_game

#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
