uiPlayerInfoDlg = 'UI.playerInfoDlg'
uiPvpInfoDlg = (uiPlayerInfoDlg + '.pvpInfoDlg')
uiPveInfoDlg = (uiPlayerInfoDlg + '.pveInfoDlg')
uiModeInfoDlg = (uiPlayerInfoDlg + '.modeInfoDlg')
uiSetupDlg = 'UI.setupDlg'
uiGuideBar = 'UI.guideBar'
uiSocialityDlg = 'UI.socialityDlg'
uiMenuDlg = 'UI.menuDlg'
uiPlayerListDlg = (uiSocialityDlg + '.playerListDlg')
uiKinDlg = (uiSocialityDlg + '.kinDlg')
uiKinMemberDlg = (uiKinDlg + '.kinmemberDlg')
uiKinManagerDlg = (uiKinDlg + '.kinmanagerDlg')
uiKinCreateHintDlg = 'UI.createkinhintDlg'
uiKinCreateDlg = 'UI.createkinDlg'
uitopKinDlg = 'UI.topkinDlg'
uiKinInfoDlg = 'UI.kinInfoDlg'
uiKinInviteDlg = 'UI.kinInviteDlg'
uiKinTipDlg = 'UI.kinTipDlg'
uiAddFriendDlg = 'UI.requestMakeFriendsDlg'
uiBeAddedFriendDlg = 'UI.friendDlg'
uiPlayerMenu = 'UI.playerMenu'
uiSparkDlg = 'UI.sparkDlg'
uiReceiveSparkDlg = 'UI.receiveSparkDlg'
uiMarriageDlg = 'UI.marriageInfoDlg'
uiDivorceDlg = 'UI.divorceDlg'
uiModifyLoveWordDlg = 'UI.modifyLoveWordDlg'
uiMarriageConfirmDlg = 'UI.marriageConfirmDlg'
uiWeddingOverDlg = 'UI.weddingOverDlg'
uiWeddingDlg = 'UI.room.weddingDlg'
uiTaskSelDlg = 'UI.taskSelectDlg'
uiSetRecorderDlg = 'UI.SetRecorderDlg'
uiSelroomPlayerList = 'UI.selRoom.playerListDlg'
uiTaskDlg = 'UI.shop.taskDlg'
uiRefineDlg = 'UI.shop.refineDlg'
uiForgeDlg = 'UI.shop.refineDlg.forgeDlg'
uiComposeDlg = 'UI.shop.refineDlg.composeDlg'
uiAvatarForgeDlg = 'UI.shop.refineDlg.AvatarForgeDlg'
uiForgeConfirmDlg = 'UI.shop.refineDlg.forgeConfirmDlg'
uiRoomStorageDlg = 'UI.storageDlg'
uiShopStorageDlg = 'UI.shop.storageDlg'
uiSelModeDlg = 'UI.room.selModeDlg'
uiModifyRoomDlg = 'UI.room.modifyRoomDlg'
uiMatchRoomDlg = 'UI.room.matchDlg'
uiGamePlayerList = 'UI.game.playerListDlg'
uiPvePlayerList = 'UI.game.pvePlayerList'
uiPveFuncDlg = 'UI.game.pveFuncDlg'
uiPetPan = 'UI.selRoom.petPan'
uiC2CInviteDlg = 'UI.C2CInvite'
uiC2CDealDlg = 'UI.C2CDealDlg'
uiPawnShopDlg = 'UI.selRoom.pawnshop'
lightColor = (255,
 255,
 255,
 255)
zoneChooseColor = (255,
 250,
 236,
 255)
darkColor = (102,
 51,
 0,
 255)
maskColor = (51,
 51,
 51,
 255)
kinColor = (153,
 244,
 255,
 255)
normalNameColor = (199,
 242,
 252,
 255)
memberNameColor = (255,
 189,
 222,
 255)
broadcastColor = maskColor
MyExecFile('res/uires/uiConst.pyc')
MyExecFile('res/uires/uiTemplate.pyc')
MyExecFile('object/itemCFG.py')
MyExecFile('object/commodityCFG.py')
MyExecFile('map/mapDesc.py')
MyExecFile('res/uires/uiFunc.pyc')
MyExecFile('res/uires/levelCFG.pyc')
yesMove = 0
mark_task = 0
mark_shopPetTab = 0
joinMemberURL = ''
exitFlag = 0
shopEntry = 0
loginType = 0
friendUin = 0
beAddUin = 0
dealUin = 0
friendName = ''
beSparkedUin = 0
beSparkedNick = ''
sparkUin = 0
sparkNick = ''
weddingModeID = 0
queryingUin = 0
beInWeddingRoom = 0
weddingEffectFile = 'effect\\lihua2.eff'
priestwords = ''
beWedding = 0
practiceMode = 0
kinMemberCnt = 0
CurrentPos = 0
defkinDlgCnt = 7
ActiveMemberPos = 999999
ShowOnline = 0
OnlineCnt = 0
oldTotemEventCnt = -1
customtotemID = 0
totemPage = 0
totemPageNum = 2
lookupKinID = 0
totalStorageCnt = 0
defShopStorageCnt = 48
shopStoragePos = 0
defRoomStorageCnt = 20
roomStoragePos = 0
defRoomEquipCnt = 7
curRoomStorageIdx = -1
curEquipIdx = -1
curStorageID = 0
uiStorageIdx = 0
defMyPropC2CDealDlgCnt = 15
MyPropC2CDealDlgPos = 0
curPropC2CDealIdx = -1
uiPropC2CInx = 0
curBiddingIdx = -1
MyBiddingList = []
totaldstGoodsListCnt = 0
C2CDealDstGoodsPos = 0
ticketitemid = 1800
residualTicket = 0
bC2CDealShow = 0
bPawnShopShow = 0
MyDealStorageListCnt = 0
totalP2PDealPropCnt = 0
InvalidIdx = -1
inviteDealUin = 0

def CHECK_PET(ID):
    if ((ID > 25001) and (ID < 26000)):
        return 1
    return 0



def CHECK_PET_RELATION(ID):
    return ((ID >= 25001) and (ID <= 29000))


class storageList:
    __module__ = __name__
    items = []

    def clear(this):
        global roomStoragePos
        global totalStorageCnt
        global shopStoragePos
        storageList.items = []
        totalStorageCnt = 0
        shopStoragePos = 0
        roomStoragePos = 0



    def update(this):
        global roomStoragePos
        global totalStorageCnt
        global shopStoragePos
        storageList.items = GetStorage()
        totalStorageCnt = len(storageList.items)
        shopStoragePos = 0
        roomStoragePos = 0
        return totalStorageCnt



    def at(this, itemIdx):
        if (itemIdx >= len(storageList.items)):
            return None
        return storageList.items[itemIdx]



g_StorageList = storageList()
class P2PDealPropList:
    __module__ = __name__
    items = []

    def clear(this):
        global totalP2PDealPropCnt
        P2PDealPropList.items = []
        totalP2PDealPropCnt = 0



    def update(this):
        global totalP2PDealPropCnt
        P2PDealPropList.items = GetP2PDealProplist()
        totalP2PDealPropCnt = len(P2PDealPropList.items)
        return totalP2PDealPropCnt



    def at(this, itemIdx):
        if (itemIdx >= len(P2PDealPropList.items)):
            return None
        return P2PDealPropList.items[itemIdx]



g_P2PDealPropList = P2PDealPropList()
class dstGoodsList:
    __module__ = __name__
    items = []

    def clear(this):
        global totaldstGoodsListCnt
        global C2CDealDstGoodsPos
        dstGoodsList.items = []
        totaldstGoodsListCnt = 0
        C2CDealDstGoodsPos = 0



    def update(this):
        global totaldstGoodsListCnt
        global C2CDealDstGoodsPos
        dstGoodsList.items = GetdstGoods()
        totaldstGoodsListCnt = len(dstGoodsList.items)
        C2CDealDstGoodsPos = 0
        return totaldstGoodsListCnt



    def at(this, itemIdx):
        if (itemIdx >= len(dstGoodsList.items)):
            return None
        return dstGoodsList.items[itemIdx]



g_DstGoodsList = dstGoodsList()
class MyDealStorageList:
    __module__ = __name__
    items = []

    def clear(this):
        global MyDealStorageListCnt
        MyDealStorageList.items = []
        MyDealStorageListCnt = 0



    def update(this):
        global MyDealStorageListCnt
        MyDealStorageList.items = GetDealStorage()
        MyDealStorageListCnt = len(MyDealStorageList.items)
        return MyDealStorageListCnt



    def at(this, itemIdx):
        if (itemIdx >= len(MyDealStorageList.items)):
            return None
        return MyDealStorageList.items[itemIdx]



g_MyDealStorageList = MyDealStorageList()

def os_join(dir, fname):
    if (dir[-1] == '\\'):
        return (dir + fname)
    else:
        return ((dir + '\\') + fname)



def os_dirname(dir):
    for i in range((len(dir) - 1), -1, -1):
        if (dir[i] == '\\'):
            return dir[0:i]

    return dir


class LogicalDrives:
    __module__ = __name__

    def getDrivers(self):
        bitmaks = int(win32_GetLogicalDrives())
        drivers = []
        for i in range(32):
            if ((bitmaks & (1 << i)) and drivers.append((chr((ord('A') + i)) + ':\\'))):
                pass

        return drivers



dr = LogicalDrives()
curFile = -1

def go2setup(_uin):
    ui_setCapture(uiSetupDlg)
    Device().restore()
    KeyLayout().restore()
    PlaySound(soundUI, 1)



def NotifyLoginSuccessType(value):
    global loginType
    loginType = value



def ShowMemoryStatus():
    sc_LogOutMemoryStatus()



def changeMenuMode(mode):
    if ((0 == mode) and Win_ShowWidget((uiPlayerMenu + '.addBtn'), 1)):
        Win_ShowWidget((uiPlayerMenu + '.deleteBtn'), 0)
        Win_EnableWidget((uiPlayerInfoDlg + '.addFriendBtn'), 1)



def ReceivedRequestAddFriend(uin):
    global beAddUin
    beAddUin = uin
    Win_SetCheck((uiBeAddedFriendDlg + '.addFriend'), 1)
    Win_SetFocus((uiBeAddedFriendDlg + '.text'))
    ui_setCapture(uiBeAddedFriendDlg)



def initAllUse():
    Win_ShowWidget(uiSetupDlg, False)
    Win_ShowWidget(uiPlayerInfoDlg, False)



def ui_OnMsgBoxResult(h, isOK):
    print 'ui_OnMsgBoxResult',
    print h,
    print isOK
    if (0 == isOK):
        return 
    if (-1 == h):
        exec execStr
    else:
        if ((-2 == h) and doUI('UI.room.selMapDlg.crossBtn', 'OnClick')):
            LeaveRoom(uin)
            ui_jumpLeagueWeb()


class Device:
    __module__ = __name__

    def __restoreUI(this):
        flag = 0
        ui = uiSetupDlg
        Win_SetCheck((ui + '.soundChk'), device.sound)
        Win_SetCheck((ui + '.musicChk'), device.music)
        Win_SetCheck((ui + '.fullScreenChk'), device.fullScreen)
        Win_SetCheck((ui + '.fxChk'), device.effect)
        Win_SetCheck((ui + '.Begindlg'), device.showNext)
        flag = device.render
        print 'flag = %d',
        print flag
        if ((flag == 3) and Win_SetCheck((ui + '.softromance'), 1)):
            pass



    def restore(this):

        def restoreDevice():
            if (device.music and ResumeMusic()):
                pass
            if (device.sound and ResumeSound()):
                pass


        this._Device__restoreUI()
        restoreDevice()



    def save(this):

        def saveSet():
            ui = uiSetupDlg
            device.sound = Win_IsChecked((ui + '.soundChk'))
            device.music = Win_IsChecked((ui + '.musicChk'))
            device.fullScreen = Win_IsChecked((ui + '.fullScreenChk'))
            device.effect = Win_IsChecked((ui + '.fxChk'))
            device.showNext = Win_IsChecked((ui + '.Begindlg'))
            if Win_IsChecked((ui + '.softromance')):
                device.render = 3
            else:
                device.render = 1



        def saveFile():
            f = open('devConfig.txt', 'wt')
            f.write('class device:\n')
            for i in device.__dict__.items():
                key = i[0]
                if ((key[:2] != '__') and f.write((('  ' + key) + '= '))):
                    f.write((str(i[1]) + '\n'))

            f.close()


        saveSet()
        saveFile()



class keyLayout:
    __module__ = __name__
    moveUp = -1
    moveDown = -1
    moveLeft = -1
    moveRight = -1
    putBomb = -1
    switchItem = -1
    smartUseItem = -1
    chat = -1
    customChat = -1
    useItem0 = -1
    useItem1 = -1
    useItem2 = -1
    useItem3 = -1
    useItem4 = -1
    useItem5 = -1
    useItem6 = -1
    shop0 = -1
    shop1 = -1
    shop2 = -1
    shop3 = -1
    shop4 = -1
    shop5 = -1
    shop6 = -1
    system = -1
    quickHelp = -1

class KeyLayout:
    __module__ = __name__

    def restore(this):
        sc_keyLayout_restore(uin)
        ui = uiSetupDlg
        Win_SetValue((ui + '.up'), keyLayout.moveUp)
        Win_SetValue((ui + '.down'), keyLayout.moveDown)
        Win_SetValue((ui + '.left'), keyLayout.moveLeft)
        Win_SetValue((ui + '.right'), keyLayout.moveRight)
        Win_SetValue((ui + '.putBomb'), keyLayout.putBomb)
        Win_SetValue((ui + '.switchItem'), keyLayout.switchItem)
        Win_SetValue((ui + '.smartUseItem'), keyLayout.smartUseItem)
        Win_SetValue((ui + '.chat'), keyLayout.chat)
        Win_SetValue((ui + '.customChat'), keyLayout.customChat)
        Win_SetValue((ui + '.useItem0'), keyLayout.useItem0)
        Win_SetValue((ui + '.useItem1'), keyLayout.useItem1)
        Win_SetValue((ui + '.useItem2'), keyLayout.useItem2)
        Win_SetValue((ui + '.useItem3'), keyLayout.useItem3)
        Win_SetValue((ui + '.useItem4'), keyLayout.useItem4)
        Win_SetValue((ui + '.useItem5'), keyLayout.useItem5)
        Win_SetValue((ui + '.useItem6'), keyLayout.useItem6)
        Win_SetValue((ui + '.shop0'), keyLayout.shop0)
        Win_SetValue((ui + '.shop1'), keyLayout.shop1)
        Win_SetValue((ui + '.shop2'), keyLayout.shop2)
        Win_SetValue((ui + '.shop3'), keyLayout.shop3)
        Win_SetValue((ui + '.shop4'), keyLayout.shop4)
        Win_SetValue((ui + '.shop5'), keyLayout.shop5)
        Win_SetValue((ui + '.shop6'), keyLayout.shop6)
        Win_SetValue((ui + '.system'), keyLayout.system)



    def save(this):
        ui = uiSetupDlg
        keyLayout.moveUp = int(Win_GetValue((ui + '.up')))
        keyLayout.moveDown = int(Win_GetValue((ui + '.down')))
        keyLayout.moveLeft = int(Win_GetValue((ui + '.left')))
        keyLayout.moveRight = int(Win_GetValue((ui + '.right')))
        keyLayout.putBomb = int(Win_GetValue((ui + '.putBomb')))
        keyLayout.switchItem = int(Win_GetValue((ui + '.switchItem')))
        keyLayout.smartUseItem = int(Win_GetValue((ui + '.smartUseItem')))
        keyLayout.chat = int(Win_GetValue((ui + '.chat')))
        keyLayout.customChat = int(Win_GetValue((ui + '.customChat')))
        keyLayout.useItem0 = int(Win_GetValue((ui + '.useItem0')))
        keyLayout.useItem1 = int(Win_GetValue((ui + '.useItem1')))
        keyLayout.useItem2 = int(Win_GetValue((ui + '.useItem2')))
        keyLayout.useItem3 = int(Win_GetValue((ui + '.useItem3')))
        keyLayout.useItem4 = int(Win_GetValue((ui + '.useItem4')))
        keyLayout.useItem5 = int(Win_GetValue((ui + '.useItem5')))
        keyLayout.useItem6 = int(Win_GetValue((ui + '.useItem6')))
        keyLayout.shop0 = int(Win_GetValue((ui + '.shop0')))
        keyLayout.shop1 = int(Win_GetValue((ui + '.shop1')))
        keyLayout.shop2 = int(Win_GetValue((ui + '.shop2')))
        keyLayout.shop3 = int(Win_GetValue((ui + '.shop3')))
        keyLayout.shop4 = int(Win_GetValue((ui + '.shop4')))
        keyLayout.shop5 = int(Win_GetValue((ui + '.shop5')))
        keyLayout.shop6 = int(Win_GetValue((ui + '.shop6')))
        keyLayout.system = int(Win_GetValue((ui + '.system')))
        sc_keyLayout_save(uin)
        LoadShopKeyboardLayout()




def ui_msgBox(type):
    global yesMove
    print 'ui_msgBox',
    print type
    sc_HideWeb('kinMatch')
    sc_HideWeb('kinTeam')
    Win_SetCapture('UI.SysMsgbox')
    Win_MovePos('UI.SysMsgbox.yesbtn', -yesMove, 0)
    yesMove = 0
    Win_ShowWidget('UI.SysMsgbox.nobtn', True)
    if ((1 == type) and Win_SetImg('UI.SysMsgbox.yesbtn', 'object/ui/common/btn_agree.img')):
        Win_SetImg('UI.SysMsgbox.nobtn', 'object/ui/common/btn_refuse.img')



def recv_FriendAvt(uin, path):
    print uin,
    print path
    Win_SetImg((uiPlayerInfoDlg + '.avt'), path)
    Win_SetText((uiPlayerInfoDlg + '.avtUin'), str(uin))


class TLevelIcon(TStatic):
    __module__ = __name__
    rect = (0,
     0,
     39,
     15)
    class children:
        __module__ = __name__
        class minLevel(TStatic):
            __module__ = __name__
            framescheme = [(0,
              99,
              0,
              99,
              0,
              99,
              0,
              99)]
            framespeed = 0.14999999999999999
            loopspeed = 4.0
            bkimage = 'object/ui/level/tie/t01.img'
            rect = (0,
             0,
             39,
             15)

        class mainLevel(minLevel):
            __module__ = __name__
            rect = (0,
             0,
             39,
             15)
            bkimage = 'object/ui/level/medal/001.img'



class TTip(TStatic):
    __module__ = __name__
    initlayer = 999999
    visible = 0
    enable = 0

class MemberList:
    __module__ = __name__

    def getCnt(this):
        global kinMemberCnt
        kinMemberCnt = GetPlayerCnt(2)
        return kinMemberCnt



    def getOnlineCnt(this):
        global OnlineCnt
        OnlineCnt = GetPlayerCnt(3)
        return OnlineCnt



    def __get(this, i):
        info = CNil()
        if (ShowOnline == 0):
            ii = fetch_PlayerInfoInPlayerList(i, 2)
        else:
            ii = fetch_PlayerInfoInPlayerList(i, 3)
        a = ii.m_PlayerInfo
        gameInfo = a.m_stGameInfo
        info.Uin = a.m_dwPlayerUin
        info.nickname = a.m_szPlayerNickname.replace('\n', '')
        if (info.Uin != 0):
            info.gender = (1 == int(a.m_bGender))
        if (info.Uin != 0):
            info.grade = Level().getInfo(gameInfo.m_dwPoint)
        info.position = GetKinPositionByUin(info.Uin)
        info.honor = GetKinMemberHonor(info.Uin, 0)
        return info



    def at(this, Idx):
        if (Idx >= kinMemberCnt):
            return None
        return this._MemberList__get(Idx)




def ui_updateMemberList():
    global kinMemberCnt
    global ActiveMemberPos
    global CurrentPos
    Win_SetText((uiKinMemberDlg + '.text'), '')
    kininfo = GetInviteKinInfo(1)
    kinname = kininfo.m_szName
    kinname = kinname.replace('\n', '')
    kinname = kinname.replace("'", "\\'")
    Win_SetText((uiKinMemberDlg + '.name'), kinname)
    notification = kininfo.m_szNotification
    notification = notification.replace("'", "\\'")
    Win_SetText((uiKinMemberDlg + '.text'), notification)
    kinMemberCnt = MemberList().getCnt()
    if (ShowOnline == 0):
        ShowCnt = MemberList().getCnt()
    else:
        ShowCnt = MemberList().getOnlineCnt()
    ActiveMemberPos = 999999
    CurrentPos = min(CurrentPos, (ShowCnt - defkinDlgCnt))
    CurrentPos = max(CurrentPos, 0)
    for i in range(defkinDlgCnt):
        ui = (uiKinMemberDlg + ('.MemberPlayer%d' % i))
        Win_SetText((ui + '.NickName'), '')
        Win_SetText((ui + '.Grade'), '')
        Win_SetImg((ui + '.genderPic'), '')
        Win_SetText((ui + '.Position'), '')
        Win_SetText((ui + '.honor'), '')
        idx = (CurrentPos + i)
        Win_SetCheck(ui, 0)
        if ((idx >= ShowCnt) and Win_SetText((ui + '.NickName'), '')):
            Win_SetText((ui + '.Grade'), '')
            Win_SetImg((ui + '.genderPic'), '')
            Win_SetText((ui + '.Position'), '')
            Win_SetText((ui + '.honor'), '')
            Win_EnableWidget(ui, 0)
            continue

    Win_SetPos((uiKinMemberDlg + '.scroll'), Win_GetPos((uiKinMemberDlg + '.scroll')))
    doUI((uiKinMemberDlg + '.scroll'), 'OnPosChange')
    Win_SetText((uiKinMemberDlg + '.kinCount'), str(kinMemberCnt))
    onlineCnt = GetPlayerCnt(3)
    Win_SetText((uiKinMemberDlg + '.OnlineCount'), str(onlineCnt))
    Win_SetText((uiKinMemberDlg + '.kinHonor'), str(GetKinParam(1)))



def ShowkininviteDlg():
    info = GetInviteKinInfo(0)
    name = info.m_szName
    if (info.m_iKinSection == 1):
        kinSection = '\xb5\xe7\xd0\xc5'
    else:
        kinSection = '\xcd\xf8\xcd\xa8'
    playerinfo = GetPlayerInfoByUin(info.m_dwUin)
    governor = (((playerinfo.m_szPlayerNickname + '[') + str(info.m_dwUin)) + ']')
    Win_SetText((uiKinInviteDlg + '.name'), name)
    Win_SetText((uiKinInviteDlg + '.kininfo_status'), kinSection)
    Win_SetText((uiKinInviteDlg + '.kininfo_governor'), governor)
    Win_SetText((uiKinInviteDlg + '.kininfo_size'), str(((info.m_dwStatus & -1048576) >> 20)))
    Win_SetText((uiKinInviteDlg + '.kininfo_grade'), str(info.m_iGrade))
    Win_SetText((uiKinInviteDlg + '.kininfo_honor'), str(info.m_iLastHonor))
    Win_SetText((uiKinInviteDlg + '.kininfo_MemberCount'), str(info.m_wMemberNum))
    if ((info.m_wContentLen > 0) and Win_SetText((uiKinInviteDlg + '.kininfo_enounce'), info.m_szContent)):
        pass
    ui_setCapture(uiKinInviteDlg)



def ClearkinInfoDlg():
    Win_SetText((uiKinInfoDlg + '.kinSection'), '')
    Win_SetText((uiKinInfoDlg + '.kinname'), '')
    Win_SetText((uiKinInfoDlg + '.governor'), '')
    Win_SetText((uiKinInfoDlg + '.Size'), '')
    Win_SetText((uiKinInfoDlg + '.Grade'), '')
    Win_SetText((uiKinInfoDlg + '.Credit'), '')
    Win_SetText((uiKinInfoDlg + '.MemberCount'), '')
    Win_SetText((uiKinInfoDlg + '.Proclaim'), '')



def ShowkinInfoDlg():
    ClearkinInfoDlg()
    info = GetInviteKinInfo(0)
    name = info.m_szName
    name = name.replace('\n', '')
    name = name.replace("'", "\\'")
    if (info.m_iKinSection == 1):
        kinSection = '\xb5\xe7\xd0\xc5'
    else:
        kinSection = '\xcd\xf8\xcd\xa8'
    playerinfo = GetPlayerInfoByUin(info.m_dwUin)
    governor = (((playerinfo.m_szPlayerNickname + '[') + str(info.m_dwUin)) + ']')
    Win_SetText((uiKinInfoDlg + '.kinSection'), kinSection)
    Win_SetText((uiKinInfoDlg + '.kinname'), name)
    Win_SetText((uiKinInfoDlg + '.governor'), governor)
    Win_SetText((uiKinInfoDlg + '.Size'), str(((info.m_dwStatus & -1048576) >> 20)))
    Win_SetText((uiKinInfoDlg + '.Grade'), str(info.m_iGrade))
    Win_SetText((uiKinInfoDlg + '.Credit'), str(info.m_iLastHonor))
    Win_SetText((uiKinInfoDlg + '.MemberCount'), str(info.m_wMemberNum))
    if ((info.m_wContentLen > 0) and Win_SetText((uiKinInfoDlg + 'Proclaim'), info.m_szContent)):
        pass
    Win_ShowWidget(uiPlayerInfoDlg, 0)
    ui_setCapture(uiKinInfoDlg)



def settotemPage(page, pageNum):
    Win_SetText((uiKinManagerDlg + '.totemBtn.totemDlg.pageLab'), ('%d/%d' % ((page + 1),
     pageNum)))
    facePage = page
    start = (page * 24)
    for k in range(24):
        i = (start + k)
        ui = ((uiKinManagerDlg + '.totemBtn.totemDlg.box.face') + str(k))
        if ((i < len(faceIconList)) and Win_SetImg(ui, ('object/ui/kinTotem/%03d.img' % ((i + 1))))):
            Win_ShowWidget(ui, True)



class TTipDown(TLabel,
 Static):
    __module__ = __name__
    enable = 0
    initlayer = 999999
    bkimage = 'res/uires/help/help_small.img'
    rect = (0,
     0,
     138,
     71)
    drawcolor = (0,
     0,
     0,
     255)
    textEdgeColor = (10,
     0,
     0,
     0)
    caption = 'nameLess1\nnameLess2'
    captionrect = (9,
     24,
     121,
     38)
    class children:
        __module__ = __name__
        class title(TStatic):
            __module__ = __name__
            bkimage = 'res/uires/help/help_tittle.img'
            rect = (9,
             4,
             40,
             16)

        class point(TStatic):
            __module__ = __name__
            bkimage = 'res/uires/help/arrow_up_left.img'
            rect = (41,
             -11,
             10,
             10)




def InitRecordFileDlg():
    doUI(uiSetRecorderDlg, 'initMe')
    ui_setCapture(uiSetRecorderDlg)



def updateKinManagerDlg():
    doUI((uiKinDlg + '.kinmanagerTab'), 'OnClick')



def C2CInviteNegotiate(dstUin, iNegotiate):
    global dealUin
    if bC2CDealShow:
        return 
    dealUin = dstUin
    C2CInviteDeal(dstUin, iNegotiate)



def ShowC2CInviteDlg(Uin):
    global inviteDealUin
    print ('bC2CDealShow = %d' % bC2CDealShow)
    if (bC2CDealShow == 1):
        return 
    inviteDealUin = Uin
    Win_ShowWidget(uiSocialityDlg, 0)
    sc_HideWeb('kinMatch')
    sc_HideWeb('kinTeam')
    Win_ShowWidget(uiMenuDlg, 0)
    Win_ShowWidget(uiPlayerInfoDlg, False)
    Win_ShowWidget(uiAddFriendDlg, 0)
    Win_ShowWidget(uiBeAddedFriendDlg, 0)
    Win_ShowWidget(uiKinInfoDlg, 0)
    Win_ShowWidget(uiSetupDlg, 0)
    Win_ShowWidget(uiKinInviteDlg, 0)
    Win_ShowWidget(uiKinTipDlg, 0)
    Win_ShowWidget(uiRoomStorageDlg, 0)
    Win_ShowWidget(uiPetPan, 0)
    ui_setCapture(uiC2CInviteDlg)



def UpdateMyPropC2CDealDlg():
    if ((totalP2PDealPropCnt == 0) and Win_SetText((uiC2CDealDlg + '.MyPropPage'), '1/1')):
        pass
    for i in range(defMyPropC2CDealDlgCnt):
        ui = (uiC2CDealDlg + ('.funcItem%d' % i))
        idx = (i + MyPropC2CDealDlgPos)
        if ((idx >= totalP2PDealPropCnt) and Win_SetImg((ui + '.itemPic'), '')):
            if Win_SetText((ui + '.itemNum'), ''):
                continue
            info = g_P2PDealPropList.at(idx).m_stItem
            if (CHECK_PET_RELATION(info.m_nItemID) and CHECK_PET(info.m_nItemID)):
                Win_SetText((ui + '.itemNum'), ('%4d' % 1))
                petResId = GetPetResId(info.m_nItemID, 10)
                Win_SetImg((ui + '.itemPic'), ('res/uiRes/icon/pet/pet%d.img' % petResId))




def ui_UpdateMyBidding():
    ClearMyBiddingList()
    if (len(MyBiddingList) == 0):
        print 'in ui_UpdateMyBidding MyBiddingList is Null'
        return 
    BiddingCount = min(len(MyBiddingList), 6)
    Found = 0
    for i in range(BiddingCount):
        info = MyBiddingList[i]
        ui = (uiC2CDealDlg + ('.Mybidding%d' % i))
        if (info[0] == ticketitemid):
            Found = 1
            Win_SetText((uiC2CDealDlg + '.srcBill'), ('%12f' % info[1]))
            continue
        if (Found == 1):
            ui = (uiC2CDealDlg + ('.Mybidding%d' % (i - 1)))
        if ((info[0] <= 0) and Win_SetImg((ui + '.itemPic'), '')):
            Win_SetText((ui + '.itemNum'), '')




def UpdateMyBiddingList(obj, Num):
    Found = 0
    for i in range(len(MyBiddingList)):
        if (obj[0] == MyBiddingList[i][0]):
            if (MyBiddingList[i][1] < Num):
                MyBiddingList[i][1] += 1
            Found = 1
            break

    FoundTicket = 0
    ticketinfo = [ticketitemid,
     0]
    for i in range(len(MyBiddingList)):
        if (MyBiddingList[i][0] == ticketitemid):
            FoundTicket = 1
            ticketinfo[1] = MyBiddingList[i][1]
            del MyBiddingList[i]
            break

    MaxBiddingCount = 5
    if (((not Found) and (len(MyBiddingList) < MaxBiddingCount)) and MyBiddingList.append(obj)):
        pass
    if (FoundTicket and MyBiddingList.append(ticketinfo)):
        pass
    print len(MyBiddingList)



def ui_UpdateDstBidding():
    InitDstBiddingList()
    g_DstGoodsList.update()
    BiddingCount = min(totaldstGoodsListCnt, 6)
    for i in range(BiddingCount):
        ui = (uiC2CDealDlg + ('.DstBidding%d' % i))
        if ((g_DstGoodsList.at(i).m_iItemID == ticketitemid) and Win_SetText((uiC2CDealDlg + '.dstBill'), ('%12f' % g_DstGoodsList.at(i).m_iItemNum))):
            continue
        print ('ui_UpdateDstBidding %s' % ui)
        if ((g_DstGoodsList.at(i).m_iItemID <= 0) and Win_SetImg((ui + '.itemPic'), '')):
            Win_SetText((ui + '.itemNum'), '')




def removeBiddingItem(idx):
    if (idx < len(MyBiddingList)):
        if (MyBiddingList[idx][1] > 0):
            MyBiddingList[idx][1] = (MyBiddingList[idx][1] - 1)
            if (MyBiddingList[idx][1] == 0):
                del MyBiddingList[idx]
        else:
            del MyBiddingList[idx]



def ClearMyBiddingList():
    for i in range(5):
        ui = (uiC2CDealDlg + ('.Mybidding%d' % i))
        Win_SetImg((ui + '.itemPic'), '')
        Win_SetText((ui + '.itemNum'), '')

    Win_SetText((uiC2CDealDlg + '.srcBill'), str(0))



def InitDstBiddingList():
    g_DstGoodsList.clear()
    for i in range(5):
        ui = (uiC2CDealDlg + ('.DstBidding%d' % i))
        Win_SetImg((ui + '.itemPic'), '')
        Win_SetText((ui + '.itemNum'), '')

    Win_SetText((uiC2CDealDlg + '.dstBill'), str(0))



def ShowC2CDealDlg(Uin):
    global bC2CDealShow
    global residualTicket
    global MyBiddingList
    global dealUin
    if bC2CDealShow:
        return 
    bC2CDealShow = 1
    SetC2CDlgFlag(bC2CDealShow)
    residualTicket = GetMyBill()
    dealUin = Uin
    g_P2PDealPropList.update()
    MyBiddingList = []
    g_DstGoodsList.clear()
    UpdateMyPropC2CDealDlg()
    InitDstBiddingList()
    ClearMyBiddingList()
    Win_SetText((uiC2CDealDlg + '.residualBill'), ('%12f' % residualTicket))
    Win_ShowWidget(uiC2CDealDlg, 1)
    RequestStartDeal(dealUin, 1)



def UpdateC2CDealDlgAfterBargain():
    global residualTicket
    global MyBiddingList
    residualTicket = GetMyBill()
    Win_SetText((uiC2CDealDlg + '.residualBill'), ('%12f' % residualTicket))
    g_P2PDealPropList.update()
    MyBiddingList = []
    g_DstGoodsList.clear()
    UpdateMyPropC2CDealDlg()
    InitDstBiddingList()
    ClearMyBiddingList()



def CloseC2CDealDlg(iFlag):
    global bC2CDealShow
    global dealUin
    if (bC2CDealShow == 0):
        return 
    Win_ShowWidget(uiC2CDealDlg, 0)
    if ((iFlag and (dealUin != 0)) and C2CInviteDeal(dealUin, 4)):
        pass
    RequestStartDeal(dealUin, 2)
    bC2CDealShow = 0
    dealUin = 0
    SetC2CDlgFlag(bC2CDealShow)



def UpdateAfterNegotiate():
    global residualTicket
    residualTicket = GetMyBill()
    print ('...............................................................residualTicket = %d' % residualTicket)
    for i in range(len(MyBiddingList)):
        if (MyBiddingList[i][0] == ticketitemid):
            residualTicket -= MyBiddingList[i][1]
            break

    Win_SetText((uiC2CDealDlg + '.residualBill'), ('%12f' % residualTicket))



def UpdateStorageinDealDlg(bid, MyBidIdx):
    for i in range(defMyPropC2CDealDlgCnt):
        ui = (uiC2CDealDlg + ('.funcItem%d' % i))
        idx = (i + MyPropC2CDealDlgPos)
        if ((idx >= totalP2PDealPropCnt) and Win_SetImg((ui + '.itemPic'), '')):
            Win_SetText((ui + '.itemNum'), '')
            continue
        if (MyBidIdx == InvalidIdx):
            for j in range(len(MyBiddingList)):
                if ((g_P2PDealPropList.at(idx).m_stItem.m_nItemID == MyBiddingList[j][0]) and (bid == 1)):
                    if CHECK_PET(g_P2PDealPropList.at(idx).m_stItem.m_nItemID):
                        if Win_SetText((ui + '.itemNum'), ('%4d' % 0)):
                            pass

        else:
            if ((MyBidIdx < len(MyBiddingList)) and (bid == 0)):
                if ((MyBiddingList[MyBidIdx][1] > 0) and (g_P2PDealPropList.at(idx).m_stItem.m_nItemID == MyBiddingList[MyBidIdx][0])):
                    if CHECK_PET(g_P2PDealPropList.at(idx).m_stItem.m_nItemID):
                        if Win_SetText((ui + '.itemNum'), ('%4d' % 1)):
                            pass




def DealInitialize():
    InitializeDealer()



def UnInializeDealerException():
    UnInitialDealer()



def CloseC2CDealDlgFromCpp():
    CloseC2CDealDlg(bC2CDealShow)



def DisableEnterRoom():
    Win_ShowWidget('UI.selRoom.practiceBtn', 0)
    Win_ShowWidget('UI.selRoom.fastJoinRoomBtn', 0)
    Win_ShowWidget('UI.selRoom.newRoomBtn', 0)



def ReceiveSpark(uin):
    global sparkUin
    if doUI((uiSocialityDlg + '.crossBtn'), 'OnClick'):
        Win_ShowWidget(uiKinCreateHintDlg, 0)
        Win_ShowWidget(uiKinCreateDlg, 0)
        if (Win_IsVisible('UI.shop') and ((fruitState != 0) and (fruitState != 1))):
            return 
        if (validateState == 1):
            return 
    if Win_IsVisible('UI.web'):
        return 
    word = Win_GetText('UI.TextBuffer')
    name = Win_GetText('UI.TextBuffer2')
    txt = ((((name + '[') + str(uin)) + ']:\n') + word)
    Win_SetText((uiReceiveSparkDlg + '.sparkword'), txt)
    sparkUin = uin
    ui_setCapture(uiReceiveSparkDlg)



def ReceiveMarriageConfirm():
    Win_ShowWidget('UI.SysMsgbox', 0)
    txt = Win_GetText('UI.TextBuffer')
    Win_SetText((uiMarriageConfirmDlg + '.marriageWord'), txt)
    ui_setCapture(uiMarriageConfirmDlg)



def ui_UpdateMyMarriageInfo():
    if (queryingUin != uin):
        return 
    if (Win_IsVisible(uiPlayerInfoDlg) and ui_getPlayerDetail()):
        pass



def ShowMarriageDlg():

    def showLevelIcon(level):
        ui = (uiMarriageDlg + '.marriageLevel')
        heart = 'object/ui/marriage/marriageLevel/dlg_heart.img'
        diamond = 'object/ui/marriage/marriageLevel/dlg_diamond.img'
        coronet = 'object/ui/marriage/marriageLevel/dlg_coronet.img'
        if ((level < 2) and Win_SetImg((ui + '.level1'), heart)):
            Win_ShowWidget((ui + '.level1'), 1)
            Win_ShowWidget((ui + '.level2'), 0)
            Win_ShowWidget((ui + '.level3'), 0)
            Win_ShowWidget((ui + '.level4'), 0)
            Win_ShowWidget((ui + '.level5'), 0)


    ui = uiMarriageDlg
    if (queryingUin == uin):
        marInfo = GetMyMarriageDetail()
        Win_EnableWidget((uiMarriageDlg + '.divorce'), 1)
        Win_EnableWidget((uiMarriageDlg + '.modify'), 1)
    else:
        marInfo = GetMarriageDetail()
        Win_EnableWidget((uiMarriageDlg + '.divorce'), 0)
        Win_EnableWidget((uiMarriageDlg + '.modify'), 0)
    Win_SetText((ui + '.spouseName'), marInfo.m_szSpouseNickname)
    Win_SetText((ui + '.marriageAge'), (str(marInfo.m_dwMarriageAge) + ' \xcc\xec'))
    Win_SetText((ui + '.closeNum'), str(marInfo.m_dwMarriageLoyalty))
    showLevelIcon(marInfo.m_wMarriageLevel)
    lineLen = int(((135 * marInfo.m_dwMarriageLoyalty) / marInfo.m_dwLevelValue))
    txt = ((str(marInfo.m_dwMarriageLoyalty) + '/') + str(marInfo.m_dwLevelValue))
    Win_SetDrawTexRect((ui + '.closeLine'), 0, 0, lineLen, 17)
    Win_SetText((ui + '.closeLineValue.value'), txt)
    Win_SetText((ui + '.loveword'), marInfo.m_szLoveWord)
    if (marInfo.m_dwRingID > 0):
        ring = ('object/ui/marriage/ring/ring%d.img' % marInfo.m_dwRingID)
        Win_SetImg((ui + '.ring'), ring)
        Win_ShowWidget((ui + '.ring'), 1)
        Win_ShowWidget((ui + '.noRing'), 0)
    else:
        Win_ShowWidget((ui + '.noRing'), 1)
        Win_ShowWidget((ui + '.ring'), 0)
        if ((((uin == queryingUin) or (uin == marInfo.m_dwMarriageUin)) and ((not (Win_GetCurScreen() == 'game')) and (not (Win_GetCurScreen() == 'room')))) and Win_EnableWidget((ui + '.noRing'), 1)):
            pass
    ui_setCapture(uiMarriageDlg)



def SetWeddingStart(wMode, uin, TargetUin):
    global beWedding
    global sparkUin
    global weddingModeID
    global beSparkedNick
    global sparkNick
    global beSparkedUin
    weddingModeID = wMode
    if ((weddingModeID < 0) or (weddingModeID > 1)):
        weddingModeID = 0
    sparkUin = uin
    sparkNick = Win_GetText('UI.TextBuffer')
    beSparkedUin = TargetUin
    beSparkedNick = Win_GetText('UI.TextBuffer2')
    beWedding = 1
    SetWeddingRoom()



def SetWeddingRoom():
    doUI('UI.room.helpKB.crossBtn', 'OnClick')
    doUI('UI.taskSelectDlg.cancel', 'OnClick')
    if ((beWedding == 1) and Win_EnableWidget((uiWeddingDlg + '.startWedding'), 0)):
        Win_EnableWidget((uiWeddingDlg + '.modeLeft'), 0)
        Win_EnableWidget((uiWeddingDlg + '.modeRight'), 0)
    Win_ShowWidget('UI.room.selChatBg', 0)
    if (not weddingMode.has_key(weddingModeID)):
        return 
    desc = weddingMode[weddingModeID]
    (bg, bgIcon, priest, priestSmall, marriageConfirm, weddingMusic,) = desc[0:6]
    Win_SetImg('UI.room.chatRoomBg', bg)
    Win_SetImg((uiWeddingDlg + '.priest'), priest)
    Win_SetImg('UI.room.priestSmall', priestSmall)
    Win_ShowWidget('UI.room.priestSmall', 0)
    Win_SetImg((uiWeddingDlg + '.bgPreview'), bgIcon)
    Win_SetImg(uiMarriageConfirmDlg, marriageConfirm)
    PlayMusic(weddingMusic, -1)
    print 'PlayMusic(weddingMusic,-1):',
    print weddingMusic
    Win_ShowWidget(uiWeddingDlg, 1)



def ChangeWeddingMode(change):
    global weddingModeID
    num = len(weddingMode)
    if (change == 1):
        weddingModeID = (weddingModeID + 1)
        weddingModeID = (weddingModeID % num)
    elif (change == -1):
        weddingModeID = (weddingModeID - 1)
        if (weddingModeID < 0):
            weddingModeID = (weddingModeID + num)
    SetWeddingRoom()



def MyWeddingOver():
    txt = Win_GetText('UI.TextBuffer3')
    print 'word:',
    print txt
    Win_SetText((uiWeddingOverDlg + '.congratulations'), txt)
    ui_setCapture(uiWeddingOverDlg)
    PlaySound('weddingOver.wav', 1)



def WeddingOver(uin, targetUin):
    global sparkNick
    global sparkUin
    global priestwordNum
    global beSparkedNick
    global priestwords
    global beSparkedUin
    Win_ShowWidget('UI.room.priestSmall', 1)
    Win_SetValue('UI.room.priestSmall', 1.0, 41)
    Win_SetValue('UI.room.priestSmall', 1, 901)
    sparkUin = uin
    sparkNick = Win_GetText('UI.TextBuffer')
    beSparkedUin = targetUin
    beSparkedNick = Win_GetText('UI.TextBuffer2')
    priestwordNum = 1
    priestwords = (((sparkNick + ':\n\xc4\xe3\xd4\xb8\xd2\xe2\xd3\xeb') + beSparkedNick) + '\xbd\xe1\xce\xaa\xb7\xf2\xc6\xde\xc2\xf0\xa3\xbf')
    ui = 'UI.room.priestword'
    Win_SetText((ui + '.words'), priestwords)
    Win_ShowWidget(ui, 1)
    Win_SetValue(ui, 1.0, 41)
    Win_SetValue(ui, 1, 901)
    Win_Timer(ui, 2000)



def PlayerWord():
    global priestwords
    global priestwordNum
    uin = 0
    if (priestwordNum == 1):
        uin = sparkUin
    elif (priestwordNum == 2):
        uin = beSparkedUin
    elif (priestwordNum == 3):
        priestwordNum = (priestwordNum + 1)
        Win_Timer('UI.room.tempTimer', 2000)
        return 
    else:
        return 
    seatID = -1
    seatID = GetSeatIDByUin(uin)
    if (seatID < 0):
        return 
    ui = ('UI.room.playerChat' + str(seatID))
    Win_SetText(ui, '\xce\xd2\xd4\xb8\xd2\xe2^^')
    ui_playerChat(seatID)
    if (priestwordNum == 1):
        priestwords = (((beSparkedNick + ':\n\xc4\xe3\xd4\xb8\xd2\xe2\xd3\xeb') + sparkNick) + '\xbd\xe1\xce\xaa\xb7\xf2\xc6\xde\xc2\xf0\xa3\xbf')
    elif (priestwordNum == 2):
        priestwords = '\xb9\xa7\xcf\xb2\xc4\xe3\xc3\xc7\xd2\xd1\xbe\xad\xb3\xc9\xce\xaaQQ\xcc\xc3\xba\xcf\xb7\xa8\xb7\xf2\xc6\xde!'
    else:
        return 
    priestwordNum = (priestwordNum + 1)
    Win_Timer('UI.room.tempTimer', 2000)



def UpdateLoveword():
    txt = Win_GetText((uiModifyLoveWordDlg + '.loveword'))
    Win_SetText((uiMarriageDlg + '.loveword'), txt)



def RestartWedding():
    global beWedding
    beWedding = 0
    Win_ShowWidget(uiMarriageConfirmDlg, 0)
    SetWeddingRoom()



def UpdateWeddingMode(mode):
    global beWedding
    global weddingModeID
    beWedding = 0
    weddingModeID = mode
    if ((weddingModeID < 0) or (weddingModeID > 1)):
        weddingModeID = 0
    SetWeddingRoom()


weddingMode = {0: ('object/ui/marriage/bg/dlg_westBG.img',
     'object/ui/marriage/bg/dlg_westIcon.img',
     'object/ui/marriage/priest/dlg_westPriest.img',
     'object/ui/marriage/priest/dlg_westPriestS.img',
     'object/ui/marriage/dlg_marriageConfirmWest.img',
     'weddingWest.ogg'),
 1: ('object/ui/marriage/bg/dlg_chinaBG.img',
     'object/ui/marriage/bg/dlg_chinaIcon.img',
     'object/ui/marriage/priest/dlg_chinaPriest.img',
     'object/ui/marriage/priest/dlg_chinaPriestS.img',
     'object/ui/marriage/dlg_marriageConfirmChina.img',
     'weddingWest.ogg')}
playerModeDlg = ['bunModeDlg',
 'matchModeDlg',
 'sculptureModeDlg']
playerModeImg = ['img_bun.img',
 'img_match.img',
 'img_sculpture.img']
levelNum = 7
modeNum = 14

def InitPlayerModeInfo():
    for j in range(len(playerModeDlg)):
        ui = ((uiModeInfoDlg + '.') + playerModeDlg[j])
        imgPath = ('object/ui/guideBar/player/' + playerModeImg[j])
        Win_SetImg((ui + '.level1'), imgPath)
        Win_SetText((ui + '.exp'), '0.00%')
        Win_SetDrawTexRect((ui + '.expLine'), 0, 0, 0, 12)

    for level in range((levelNum - 1)):
        Win_SetImg(((uiModeInfoDlg + '.bunModeDlg.level') + str((level + 2))), 'object/ui/guideBar/player/img_mask.img')
        Win_SetImg(((uiModeInfoDlg + '.matchModeDlg.level') + str((level + 2))), 'object/ui/guideBar/player/img_mask.img')
        Win_SetImg(((uiModeInfoDlg + '.sculptureModeDlg.level') + str((level + 2))), 'object/ui/guideBar/player/img_mask.img')




def SetPlayerModeInfo(nUin, iFlag):
    InitPlayerModeInfo()
    info = CNil()
    num = GetPlayerModeInfoByUin(nUin, iFlag)
    if ((num > modeNum) or (num == 0)):
        return 
    for i in range(num):
        ui = ((uiModeInfoDlg + '.') + playerModeDlg[i])
        imgPath = ('object/ui/guideBar/player/' + playerModeImg[i])
        info = GetPlayerModeInfoByModeIndex(nUin, i, iFlag)
        curPoints = info.m_dwPatternPoint
        curLevel = info.m_wPatternLevel
        nextLevelPoint = info.m_dwLevelValue
        strRate = ('%.2f%%' % ((curPoints * 100.0) / nextLevelPoint))
        Win_SetText((ui + '.exp'), strRate)
        Win_SetDrawTexRect((ui + '.expLine'), 0, 0, ((curPoints * 180) / nextLevelPoint), 12)
        for level in range(curLevel):
            Win_SetImg(((ui + '.level') + str((level + 1))), imgPath)

        for otherLevel in range((levelNum - curLevel)):
            Win_SetImg(((ui + '.level') + str(((otherLevel + curLevel) + 1))), 'object/ui/guideBar/player/img_mask.img')




class UI:
    __module__ = __name__
    AllCursor = ({'name': 'normal',
      'path': 'object/ui/cursor/arror.img',
      'step': 0.59999999999999998},
     {'name': 'Click',
      'path': 'object/ui/cursor/dianji.img',
      'step': 0.59999999999999998,
      'holdframe': 1},
     {'name': 'attack',
      'path': 'object/ui/cursor/fight.gsa',
      'step': 0.80000000000000004})
    AllScreen = ({'id': 'logo',
      'path': 'res/uires/uiLogo.pyc'},
     {'id': 'login',
      'path': 'res/uires/uiLogin.pyc'},
     {'id': 'selRoom',
      'path': 'res/uires/uiSelRoom.pyc'},
     {'id': 'selSect',
      'path': 'res/uires/uiSelSect.pyc'},
     {'id': 'room',
      'path': 'res/uires/uiRoom.pyc'},
     {'id': 'shop',
      'path': 'res/uires/uiShop.pyc'},
     {'id': 'web',
      'path': 'res/uires/uiWeb.pyc'},
     {'id': 'game',
      'path': 'res/uires/uiGame.pyc'})
    accel = (('OnAccel_FocusPaste',
      86,
      17,
      0,
      0),
     ('OnAccel_FocusCut',
      88,
      17,
      0,
      0),
     ('OnAccel_FocusCopy',
      67,
      17,
      0,
      0),
     ('OnAccel_OnF6',
      117,
      0,
      0,
      0),
     ('OnAccel_OnF10',
      121,
      0,
      0,
      0),
     ('OnAccel_OnF11',
      122,
      0,
      0,
      0))
    buddy = ({'type': buddy_widget_tipwgt,
      'style': buddy_style_self,
      'id': 'UI.SysTooltip'},
     {'type': buddy_widget_msgbox,
      'style': buddy_style_self,
      'id': 'UI.SysMsgbox'},
     {'type': buddy_widget_console,
      'style': buddy_style_self,
      'id': 'UI.SysConsole'})

    def OnInit():
        Device().restore()
        Device().save()
        settotemPage(0, totemPageNum)
        Win_SelectSelf((uiPlayerInfoDlg + '.pvpInfoTab'))
        Win_SetCheck((uiPlayerInfoDlg + '.pvpInfoTab'), 1)
        doUI((uiPlayerInfoDlg + '.pvpInfoTab'), 'OnClick')
        Win_SelectSelf((uiSocialityDlg + '.playerTab'))
        Win_SetCheck((uiSocialityDlg + '.playerTab'), 1)
        InitPlayerModeInfo()



    def OnAccel_FocusPaste():
        Win_FocusOnPaste()



    def OnAccel_FocusCut():
        print 'cut'
        Win_FocusOnCut()



    def OnAccel_FocusCopy():
        print 'copy'
        Win_FocusOnCopy()



    def OnAccel_OnF6():
        CloseC2CDealDlg(bC2CDealShow)
        go2playerInfo(uin)



    def OnAccel_OnF10():
        print 'OnF10'
        CloseC2CDealDlg(bC2CDealShow)
        go2setup(uin)



    def OnAccel_OnF11():
        sc_printScreen()


    class children:
        __module__ = __name__
        class TextBuffer(TLabel):
            __module__ = __name__
            visible = 0

        class TextBuffer2(TLabel):
            __module__ = __name__
            visible = 0

        class TextBuffer3(TLabel):
            __module__ = __name__
            visible = 0

        class SysConsole:
            __module__ = __name__
            type = 'CONSOLE'
            rect = (0,
             0,
             800,
             250)
            bkcolor = (0,
             196,
             0,
             128)
            initlayer = console_layer
            srcpos = (0,
             -250)
            dstpos = (0,
             0)
            speed = 12.0
            visible = 0
            drawflag = (drawflag_win_edge + drawflag_win_fill)

            def OnSelfShow():
                Win_SetFocus('UI.SysConsole.downinput')



            def OnSelfHide():
                Win_SetFocus()



            def OnTrigger(state):
                if ((state == flyer_scroll_sate_start) and Win_ShowWidget('UI.SysConsole', false)):
                    pass


            class children:
                __module__ = __name__
                class downinput:
                    __module__ = __name__
                    type = 'EDIT'
                    rect = (0,
                     0,
                     600,
                     16)
                    drawcolor = lightColor
                    bkcolor = (0,
                     0,
                     0,
                     128)
                    tabstop = 0
                    textstyle = (dt_left + dt_vcenter)
                    maxchar = 128
                    aligntype = (aligntype_winrect + aligntype_father)
                    alignstyle = (alignstyle_bottom_in + alignstyle_left_in)
                    marginh = 20
                    drawflag = (drawflag_win_edge + drawflag_win_fill)

                    def OnEnter():
                        info = Win_GetText('UI.SysConsole.downinput')
                        if ((info != '') and Win_SetText('UI.SysConsole', info, value_channel_console_enter_string)):
                            pass
                        Win_SetText('UI.SysConsole.downinput', '')



                class cmdlabel:
                    __module__ = __name__
                    type = 'LABEL'
                    rect = (0,
                     0,
                     20,
                     16)
                    textstyle = (dt_center + dt_vcenter)
                    drawcolor = lightColor
                    bkcolor = (0,
                     0,
                     0,
                     0)
                    caption = '>>'
                    aligntype = (aligntype_winrect + aligntype_father)
                    alignstyle = (alignstyle_bottom_in + alignstyle_left_in)



        class SysTooltip:
            __module__ = __name__
            type = 'LABEL'
            drawcolor = lightColor
            bkcolor = (0,
             0,
             128,
             128)
            edgecolor = (0,
             0,
             0,
             128)
            maxwidth = 160
            sizeable = 1
            visible = 0
            marginh = 3
            marginv = 3
            textsize = 12
            initlayer = systooltip_layer
            textfont = 1
            drawflag = (drawflag_win_edge + drawflag_win_fill)
            alphaspeed = 0.02

        class SysMsgbox:
            __module__ = __name__
            type = 'MESSAGEBOX'
            darkBG = 1
            rect = (((800 - 368) / 2),
             ((600 - 326) / 2),
             368,
             326)
            bkimage = 'object/ui/common/dlg_msgBox.img'
            textsize = 12
            textstyle = (dt_center + dt_vcenter)
            initlayer = 999999
            visible = 0
            drawcolor = zoneChooseColor
            textEdgeType = -1

            def OnMsgBoxCancel(h):
                print 'OnMsgBoxCancel',
                print h,
                print 0
                if ((h >= 0) and OnMsgBoxResult(h, 0)):
                    pass



            def OnMsgBoxOk(h):
                print 'OnMsgBoxOk',
                print h,
                print 1
                if ((h >= 0) and OnMsgBoxResult(h, 1)):
                    pass


            class children:
                __module__ = __name__
                class yesbtn:
                    __module__ = __name__
                    type = 'BUTTON'
                    rect = (100,
                     280,
                     65,
                     31)
                    bkimage = 'object/ui/common/btn_agree.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    defaultok = 1

                class nobtn:
                    __module__ = __name__
                    type = 'BUTTON'
                    rect = (225,
                     280,
                     65,
                     31)
                    bkimage = 'object/ui/common/btn_refuse.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    defaultcancel = 1

                class textlabel:
                    __module__ = __name__
                    type = 'LABEL'
                    rowspace = 2
                    rect = (40,
                     82,
                     280,
                     130)
                    bkimagepos = (0,
                     0)
                    textsize = 12
                    textstyle = (dt_left + dt_top)
                    textEdgeType = -1
                    drawcolor = zoneChooseColor



        class playerInfoDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            darkBG = 1
            visible = 0
            rect = (((800 - 392) / 2),
             ((600 - 497) / 2),
             392,
             497)

            def OnEnter():
                path = Win_GetFocusPath()
                doUI((uiPlayerInfoDlg + '.closeBtn'), 'OnClick')



            def OnEscape():
                path = Win_GetFocusPath()
                doUI((uiPlayerInfoDlg + '.closeBtn'), 'OnClick')



            def OnInit():
                Win_SelectSelf((uiPlayerInfoDlg + '.pvpInfoTab'))
                Win_SetCheck((uiPlayerInfoDlg + '.pvpInfoTab'), 1)
                doUI((uiPlayerInfoDlg + '.pvpInfoTab'), 'OnClick')


            class children:
                __module__ = __name__
                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (350,
                     0,
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
                        Win_ShowWidget(uiPlayerInfoDlg, False)
                        PlaySound(soundLeave, 1)



                class addFriendBtn(TButton):
                    __module__ = __name__
                    enable = 1
                    rect = (12,
                     248,
                     66,
                     27)
                    bkimage = 'object/ui/guideBar/player/btn_addFriend.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        global friendUin
                        uin = Win_GetText((uiPlayerInfoDlg + '.QQ'))
                        Win_ShowWidget(uiPlayerInfoDlg, 0)
                        friendUin = int(uin)
                        NickName = GetPlayerNickNamebyUin(friendUin, 0)
                        NickName = NickName.replace('\n', '')
                        Win_ShowWidget(uiPlayerInfoDlg, 0)
                        Win_SetText((uiAddFriendDlg + '.text'), '')
                        Win_SetFocus((uiAddFriendDlg + '.text'))
                        Win_SetText((uiAddFriendDlg + '.name'), NickName)
                        ui_setCapture(uiAddFriendDlg)



                class deleteFriendBtn(TButton):
                    __module__ = __name__
                    rect = (12,
                     248,
                     66,
                     27)
                    bkimage = 'object/ui/guideBar/player/btn_deleteFriend.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        uin = Win_GetText((uiPlayerInfoDlg + '.QQ'))
                        Win_ShowWidget(uiPlayerInfoDlg, 0)
                        DoFriendTask('', 0, int(uin), 2)



                class privateChatBtn(TButton):
                    __module__ = __name__
                    enable = 1
                    rect = (86,
                     248,
                     66,
                     27)
                    bkimage = 'object/ui/guideBar/player/btn_privateChat.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        name = Win_GetText((uiPlayerInfoDlg + '.nickName'))
                        uin = Win_GetText((uiPlayerInfoDlg + '.QQ'))
                        Win_ShowWidget(uiPlayerInfoDlg, 0)
                        NotifyWisper(name, int(uin))



                class traceBtn(TButton):
                    __module__ = __name__
                    enable = 1
                    rect = (159,
                     248,
                     66,
                     27)
                    bkimage = 'object/ui/guideBar/player/btn_trace.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        uin = Win_GetText((uiPlayerInfoDlg + '.QQ'))
                        Win_ShowWidget(uiPlayerInfoDlg, 0)
                        DoFriendTask('', 0, int(uin), 3)



                class avtUin(TLabel):
                    __module__ = __name__
                    caption = '-99'

                class QQ(TLabel):
                    __module__ = __name__
                    caption = '123456789'
                    rect = (75,
                     53,
                     120,
                     12)
                    drawcolor = darkColor
                    textEdgeType = -1

                class nickName(TLabel):
                    __module__ = __name__
                    caption = '\xce\xd2\xb0\xae\xb1\xb1\xbe\xa9\xcc\xec\xc3\xc5'
                    rect = (75,
                     76,
                     (233 - 88),
                     12)
                    textEdgeColor = maskColor

                class genderPic(TStatic):
                    __module__ = __name__
                    rect = (75,
                     96,
                     16,
                     15)
                    bkimage = 'res/uires/selRoom/icon/nv.img'

                class gender(TLabel):
                    __module__ = __name__
                    caption = '\xc5\xae\xc9\xfa'
                    rect = (105,
                     98,
                     60,
                     12)
                    drawcolor = darkColor
                    textEdgeType = -1

                class marriagetotem(TStatic):
                    __module__ = __name__
                    rect = (65,
                     116,
                     16,
                     15)

                class spouseName(TLabel):
                    __module__ = __name__
                    rect = (86,
                     121,
                     100,
                     12)
                    drawcolor = darkColor
                    textEdgeType = -1
                    caption = ''

                class spark(TButton):
                    __module__ = __name__
                    enable = 1
                    rect = (186,
                     111,
                     37,
                     22)
                    bkimage = 'object/ui/guideBar/player/btn_spark.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        global beSparkedNick
                        global beSparkedUin
                        uin = Win_GetText((uiPlayerInfoDlg + '.QQ'))
                        nick = Win_GetText((uiPlayerInfoDlg + '.nickName'))
                        Win_ShowWidget(uiPlayerInfoDlg, 0)
                        PlaySound(soundLeave, 1)
                        beSparkedUin = int(uin)
                        beSparkedNick = nick
                        Win_SetText((uiSparkDlg + '.spouseName'), beSparkedNick)
                        ui_setCapture(uiSparkDlg)
                        PlaySound(soundLeave, 1)



                class lookupMarriage(TButton):
                    __module__ = __name__
                    enable = 1
                    rect = (186,
                     111,
                     37,
                     22)
                    bkimage = 'object/ui/guideBar/player/btn_lookup.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerInfoDlg, 0)
                        ShowMarriageDlg()
                        PlaySound(soundLeave, 1)



                class kintotem(TStatic):
                    __module__ = __name__
                    rect = (70,
                     140,
                     16,
                     15)
                    bkimage = 'object/ui/kinTotem/001.img'

                class kin(TLabel):
                    __module__ = __name__
                    rect = (95,
                     145,
                     100,
                     12)
                    drawcolor = darkColor
                    textEdgeType = -1
                    caption = ''

                class lookup(TButton):
                    __module__ = __name__
                    enable = 1
                    rect = (186,
                     135,
                     37,
                     22)
                    bkimage = 'object/ui/guideBar/player/btn_lookup.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        ClearkinInfoDlg()
                        kininfo = GetInviteKinInfo(1)
                        if (lookupKinID == 0):
                            print '1:   Win_ShowWidget(uiPlayerInfoDlg, 0)'
                            Win_ShowWidget(uiPlayerInfoDlg, 0)
                            ui_setCapture(uiKinInfoDlg)
                        elif (kininfo.m_dwKinIndex != lookupKinID):
                            print 'kininfo.m_dwKinIndex != lookupKinID: ',
                            print kininfo.m_dwKinIndex,
                            print ' != ',
                            print lookupKinID
                            DoKinTask('', '', 0, lookupKinID, 1)
                        else:
                            name = kininfo.m_szName
                            if (kininfo.m_iKinSection == 1):
                                kinSection = '\xb5\xe7\xd0\xc5'
                            else:
                                kinSection = '\xcd\xf8\xcd\xa8'
                            playerinfo = GetPlayerInfoByUin(kininfo.m_dwUin)
                            governor = (((playerinfo.m_szPlayerNickname + '[') + str(kininfo.m_dwUin)) + ']')
                            Win_SetText((uiKinInfoDlg + '.kinSection'), kinSection)
                            Win_SetText((uiKinInfoDlg + '.kinname'), name)
                            Win_SetText((uiKinInfoDlg + '.governor'), governor)
                            Win_SetText((uiKinInfoDlg + '.Size'), str(((kininfo.m_dwStatus & -1048576) >> 20)))
                            Win_SetText((uiKinInfoDlg + '.Grade'), str(kininfo.m_iGrade))
                            Win_SetText((uiKinInfoDlg + '.Credit'), str(kininfo.m_iLastHonor))
                            Win_SetText((uiKinInfoDlg + '.MemberCount'), str(kininfo.m_wMemberNum))
                            if ((kininfo.m_wContentLen > 0) and Win_SetText((uiKinInfoDlg + '.Proclaim'), kininfo.m_szContent)):
                                pass
                            print '2:   Win_ShowWidget(uiPlayerInfoDlg, 0)'
                            Win_ShowWidget(uiPlayerInfoDlg, 0)
                            ui_setCapture(uiKinInfoDlg)
                        PlaySound(soundLeave, 1)



                class state(TLabel,
                 Static):
                    __module__ = __name__
                    rowspace = 2
                    caption = '123456789'
                    rect = (71,
                     172,
                     (150 - 20),
                     77)
                    drawcolor = darkColor
                    textEdgeType = -1

                class pvpInfoTab(TTabWin):
                    __module__ = __name__
                    initlayer = 200000
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (30,
                     285,
                     86,
                     31)
                    hotcover = 'object/ui/guideBar/player/tab_pvpInfo.img'
                    groupstop = 0
                    groupid = 7

                    def OnClick(this):
                        Win_ShowWidget(uiPvpInfoDlg, 1)
                        Win_ShowWidget(uiPveInfoDlg, 0)
                        Win_ShowWidget(uiModeInfoDlg, 0)
                        PlaySound(soundUI, 1)



                class pveInfoTab(pvpInfoTab):
                    __module__ = __name__
                    initlayer = 200000
                    hotrect = (122,
                     285,
                     86,
                     31)
                    hotcover = 'object/ui/guideBar/player/tab_pveInfo.img'
                    groupstop = 1
                    groupid = 7

                    def OnClick(this):
                        Win_ShowWidget(uiPvpInfoDlg, 0)
                        Win_ShowWidget(uiModeInfoDlg, 0)
                        Win_ShowWidget(uiPveInfoDlg, 1)
                        PlaySound(soundUI, 1)



                class modeInfoTab(pvpInfoTab):
                    __module__ = __name__
                    initlayer = 200000
                    hotrect = (214,
                     285,
                     86,
                     31)
                    hotcover = 'object/ui/guideBar/player/tab_modeInfo.img'
                    groupstop = 2
                    groupid = 7

                    def OnClick(this):
                        Win_ShowWidget(uiPvpInfoDlg, 0)
                        Win_ShowWidget(uiPveInfoDlg, 0)
                        Win_ShowWidget(uiModeInfoDlg, 1)
                        PlaySound(soundUI, 1)



                class pvpInfoDlg(TStatic):
                    __module__ = __name__
                    rect = (0,
                     298,
                     264,
                     173)
                    class children:
                        __module__ = __name__
                        class expLine(TStatic):
                            __module__ = __name__
                            rect = (65,
                             23,
                             136,
                             12)
                            bkimage = 'object/ui/guideBar/player/img_expLine.img'

                        class exp(TLabel):
                            __module__ = __name__
                            initlayer = 1000
                            rect = (110,
                             23,
                             50,
                             12)
                            drawcolor = lightColor
                            textEdgeType = 1
                            textEdgeColor = maskColor
                            caption = '99%'

                        class reputation(TLabel):
                            __module__ = __name__
                            rect = (110,
                             46,
                             50,
                             12)
                            drawcolor = darkColor
                            textEdgeType = -1
                            caption = '1000'

                        class levelIcon(TLevelIcon):
                            __module__ = __name__
                            rect = (74,
                             92,
                             16,
                             15)

                        class level(TLabel,
                         Static):
                            __module__ = __name__
                            caption = '\xd0\xc2\xb1\xf8'
                            rect = (118,
                             98,
                             140,
                             12)
                            drawcolor = darkColor
                            textEdgeType = -1

                        class point(TLabel,
                         Static):
                            __module__ = __name__
                            caption = '10000'
                            rect = (110,
                             72,
                             159,
                             12)
                            drawcolor = darkColor
                            textEdgeType = -1

                        class success(TLabel,
                         Static):
                            __module__ = __name__
                            caption = '100\xca\xa491\xb0\xdc'
                            rect = (76,
                             125,
                             200,
                             12)
                            drawcolor = darkColor
                            textEdgeType = -1



                class pveInfoDlg(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (0,
                     314,
                     258,
                     173)
                    bkimage = 'object/ui/guideBar/player/dlg_pveInfo.img'
                    bkimagepos = (3,
                     -9)
                    class children:
                        __module__ = __name__
                        class pveLevelLabel(TLabel):
                            __module__ = __name__
                            rect = (70,
                             5,
                             12,
                             12)
                            drawcolor = (135,
                             249,
                             255,
                             255)
                            textEdgeType = 0

                        class pveLevel(TStatic):
                            __module__ = __name__
                            rect = (92,
                             5,
                             118,
                             12)
                            bkimage = 'object/ui/guideBar/player/img_expLine2.img'

                        class pveCourage(TLabel):
                            __module__ = __name__
                            rect = (100,
                             26,
                             118,
                             12)
                            drawcolor = darkColor
                            textEdgeType = -1

                        class pveLife(TLabel):
                            __module__ = __name__
                            rect = (100,
                             46,
                             118,
                             12)
                            drawcolor = darkColor
                            textEdgeType = -1

                        class pveBomb(TStatic):
                            __module__ = __name__
                            rect = (92,
                             64,
                             118,
                             12)
                            bkimage = 'object/ui/guideBar/player/img_expLine2.img'

                        class pveBombResume(TStatic):
                            __module__ = __name__
                            rect = (92,
                             83,
                             118,
                             12)
                            bkimage = 'object/ui/guideBar/player/img_expLine2.img'

                        class pvePower(TStatic):
                            __module__ = __name__
                            rect = (92,
                             103,
                             118,
                             12)
                            bkimage = 'object/ui/guideBar/player/img_expLine2.img'

                        class pveSpeed(TStatic):
                            __module__ = __name__
                            rect = (92,
                             122,
                             118,
                             12)
                            bkimage = 'object/ui/guideBar/player/img_expLine2.img'



                class modeInfoDlg(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (0,
                     314,
                     258,
                     173)
                    bkimage = 'object/ui/guideBar/player/dlg_modeInfo.img'
                    class children:
                        __module__ = __name__
                        class bunModeDlg(TStatic):
                            __module__ = __name__
                            rect = (0,
                             0,
                             258,
                             45)
                            class children:
                                __module__ = __name__
                                class level1(TStatic):
                                    __module__ = __name__
                                    rect = (71,
                                     12,
                                     22,
                                     25)
                                    bkimage = 'object/ui/guideBar/player/img_bun.img'

                                class level2(level1):
                                    __module__ = __name__
                                    rect = (95,
                                     12,
                                     22,
                                     25)
                                    bkimage = 'object/ui/guideBar/player/img_bun.img'

                                class level3(level1):
                                    __module__ = __name__
                                    rect = (118,
                                     12,
                                     22,
                                     25)

                                class level4(level1):
                                    __module__ = __name__
                                    rect = (141,
                                     12,
                                     22,
                                     25)

                                class level5(level1):
                                    __module__ = __name__
                                    rect = (164,
                                     12,
                                     22,
                                     25)

                                class level6(level1):
                                    __module__ = __name__
                                    rect = (187,
                                     12,
                                     22,
                                     25)

                                class level7(level1):
                                    __module__ = __name__
                                    rect = (210,
                                     12,
                                     22,
                                     25)

                                class expLine(TStatic):
                                    __module__ = __name__
                                    rect = (70,
                                     39,
                                     180,
                                     12)
                                    bkimage = 'object/ui/guideBar/player/img_modeExpLine.img'

                                class exp(TLabel):
                                    __module__ = __name__
                                    initlayer = 1000
                                    rect = (140,
                                     38,
                                     50,
                                     12)
                                    drawcolor = lightColor
                                    textEdgeType = 1
                                    textEdgeColor = maskColor
                                    caption = '99%'



                        class matchModeDlg(bunModeDlg):
                            __module__ = __name__
                            rect = (0,
                             48,
                             258,
                             45)

                        class sculptureModeDlg(bunModeDlg):
                            __module__ = __name__
                            rect = (0,
                             92,
                             258,
                             45)



                class mask(TStatic):
                    __module__ = __name__
                    initlayer = -999
                    rect = (-10,
                     -16,
                     1,
                     1)
                    bkimage = 'object/ui/guideBar/player/dlg_playerInfo.img'

                class demoMask(TStatic):
                    __module__ = __name__
                    initlayer = -99999
                    rect = (244,
                     321,
                     99,
                     99)
                    bkimage = 'object/ui/guideBar/player/mask_demo.img'

                class avt(TStatic):
                    __module__ = __name__
                    framespeed = 0.25
                    framescheme = [(0,
                      99,
                      0,
                      99,
                      0,
                      99,
                      0,
                      99)]
                    initlayer = -9999
                    rect = (220,
                     18,
                     (125 - 266),
                     (365 - 27))
                    bkimage = 'res/uiRes/avt_girl.gif'

                class playerDemo(TStatic):
                    __module__ = __name__
                    initlayer = -9999
                    rect = (245,
                     317,
                     96,
                     96)
                    class children:
                        __module__ = __name__
                        class demo(TStatic):
                            __module__ = __name__
                            initlayer = 99999
                            rect = (0,
                             10,
                             71,
                             85)
                            callbackdraw = 'SC_selRoom_drawPlayer'

                        class bg(TStatic):
                            __module__ = __name__
                            bkImgFlag = dt_center
                            framespeed = 0.25
                            initlayer = -9999
                            rect = (0,
                             10,
                             96,
                             96)

                        class frame(TStatic):
                            __module__ = __name__
                            bkImgFlag = dt_center
                            framespeed = 0.25
                            initlayer = 999
                            framescheme = [(0,
                              99,
                              0,
                              99,
                              0,
                              99,
                              0,
                              99)]
                            rect = (0,
                             10,
                             96,
                             96)

                        class enter(TStatic):
                            __module__ = __name__
                            framescheme = [(0,
                              99,
                              0,
                              99,
                              0,
                              99,
                              0,
                              99)]
                            bkImgFlag = (dt_center | eBkImgPlayOnce)
                            framespeed = 0.25
                            initlayer = 999
                            rect = (0,
                             10,
                             96,
                             96)

                        class goldDiamond(TStatic):
                            __module__ = __name__
                            rect = (70,
                             20,
                             20,
                             19)
                            framescheme = [(0,
                              13,
                              0,
                              13,
                              0,
                              13,
                              0,
                              13)]
                            initlayer = 99999





        class setupDlg(TStatic):
            __module__ = __name__
            initlayer = 99999
            darkBG = 1
            visible = 0
            rect = (((800 - 402) / 2),
             ((600 - 468) / 2),
             402,
             468)
            bkimage = 'object/ui/common/dlg_setup.img'
            bkimagepos = (-8,
             -6)

            def OnEnter():
                doUI((uiSetupDlg + '.modifyBtn'), 'OnClick')



            def OnEscape():
                doUI((uiSetupDlg + '.cancelBtn'), 'OnClick')


            class children:
                __module__ = __name__
                class modifyBtn(TButton):
                    __module__ = __name__
                    rect = (130,
                     (474 - 53),
                     66,
                     27)
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
                        Win_ShowWidget(uiSetupDlg, False)
                        PlaySound(soundLeave, 1)
                        KeyLayout().save()
                        Device().save()



                class crossBtn(TButton):
                    __module__ = __name__
                    rect = (367,
                     14,
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
                        doUI((uiSetupDlg + '.cancelBtn'), 'OnClick')



                class cancelBtn(TButton):
                    __module__ = __name__
                    rect = ((212 - 8),
                     (474 - 53),
                     66,
                     27)
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
                        Win_ShowWidget(uiSetupDlg, False)
                        PlaySound(soundLeave, 1)
                        Device().restore()
                        KeyLayout().restore()



                class up(TKeyEdit):
                    __module__ = __name__
                    rect = (75,
                     77,
                     (123 - 80),
                     12)
                    caption = 'error'
                    textstyle = dt_center
                    drawcolor = (51,
                     113,
                     149,
                     255)
                    textEdgeType = -1

                class down(up):
                    __module__ = __name__
                    rect = (75,
                     141,
                     (123 - 80),
                     12)

                class left(up):
                    __module__ = __name__
                    rect = (20,
                     117,
                     (74 - 32),
                     12)

                class right(up):
                    __module__ = __name__
                    rect = (131,
                     116,
                     (180 - 137),
                     12)

                class putBomb(up):
                    __module__ = __name__
                    rect = (52,
                     204,
                     (103 - 52),
                     12)

                class switchItem(up):
                    __module__ = __name__
                    rect = (138,
                     204,
                     (190 - 138),
                     12)

                class smartUseItem(up):
                    __module__ = __name__
                    rect = (55,
                     245,
                     48,
                     12)

                class chat(up):
                    __module__ = __name__
                    rect = (141,
                     245,
                     48,
                     12)

                class customChat(up):
                    __module__ = __name__
                    rect = (85,
                     270,
                     60,
                     12)

                class useItem0(up):
                    __module__ = __name__
                    rect = (250,
                     95,
                     35,
                     12)

                class useItem1(up):
                    __module__ = __name__
                    rect = (250,
                     111,
                     35,
                     12)

                class useItem2(up):
                    __module__ = __name__
                    rect = (250,
                     127,
                     35,
                     12)

                class useItem3(up):
                    __module__ = __name__
                    rect = (250,
                     143,
                     35,
                     12)

                class useItem4(up):
                    __module__ = __name__
                    rect = (250,
                     159,
                     35,
                     12)

                class useItem5(up):
                    __module__ = __name__
                    rect = (250,
                     175,
                     35,
                     12)

                class useItem6(up):
                    __module__ = __name__
                    rect = (250,
                     191,
                     35,
                     12)

                class shop0(up):
                    __module__ = __name__
                    rect = (347,
                     95,
                     35,
                     12)

                class shop1(up):
                    __module__ = __name__
                    rect = (347,
                     111,
                     35,
                     12)

                class shop2(up):
                    __module__ = __name__
                    rect = (347,
                     127,
                     35,
                     12)

                class shop3(up):
                    __module__ = __name__
                    rect = (347,
                     143,
                     35,
                     12)

                class shop4(up):
                    __module__ = __name__
                    rect = (347,
                     157,
                     35,
                     12)

                class shop5(up):
                    __module__ = __name__
                    rect = (347,
                     173,
                     35,
                     12)

                class shop6(up):
                    __module__ = __name__
                    rect = (347,
                     189,
                     35,
                     12)

                class system(up):
                    __module__ = __name__
                    rect = (80,
                     294,
                     60,
                     12)

                class soundChk(TStdCheck):
                    __module__ = __name__
                    rect = (20,
                     (374 - 14),
                     60,
                     20)

                    def OnClick(this):
                        if (Win_IsChecked((uiSetupDlg + '.soundChk')) and ResumeSound()):
                            PlaySound(soundUI, 1)



                class musicChk(soundChk):
                    __module__ = __name__
                    rect = (108,
                     (374 - 14),
                     60,
                     20)

                    def OnClick(this):
                        if (Win_IsChecked((uiSetupDlg + '.musicChk')) and ResumeMusic()):
                            pass



                class fxChk(soundChk):
                    __module__ = __name__
                    rect = (198,
                     (374 - 14),
                     60,
                     20)

                    def OnClick(this):
                        PlaySound(soundUI, 1)



                class fullScreenChk(soundChk):
                    __module__ = __name__
                    rect = (272,
                     (374 - 14),
                     60,
                     20)

                    def OnClick(this):
                        PlaySound(soundUI, 1)



                class Begindlg(soundChk):
                    __module__ = __name__
                    rect = (20,
                     378,
                     60,
                     20)

                    def OnClick(this):
                        PlaySound(soundUI, 1)



                class softromance(TRadio):
                    __module__ = __name__
                    framescheme = [(1,
                      1,
                      1,
                      1,
                      1,
                      1,
                      1,
                      1),
                     (0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0)]
                    rect = (198,
                     377,
                     60,
                     20)
                    bkimage = 'object/ui/common/btn_ratio.img'
                    groupstop = 1

                class hardromance(softromance):
                    __module__ = __name__
                    framescheme = [(1,
                      1,
                      1,
                      1,
                      1,
                      1,
                      1,
                      1),
                     (0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0)]
                    rect = (198,
                     395,
                     60,
                     20)
                    bkimage = 'object/ui/common/btn_ratio.img'
                    groupstop = 2



        class guideBar(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            rect = (0,
             -1,
             800,
             36)
            bkimage = 'object/ui/guideBar/img_guide.img'
            class children:
                __module__ = __name__
                __doc__ = "\n                class shopBtn(TButton):\n                    rect = (5, 1, 102, 31)\n                    bkimage = 'object/ui/guideBar/btn_shop.img'\n                    tipwidget = uiGuideBar+'.tipShop'\n                    def OnClick(this):\n                        global bC2CDealShow\n                        CloseC2CDealDlg(bC2CDealShow)\n                        if Win_GetCurScreen() == 'selRoom':\n                            SC_ClickShopBtn()\n                            go2shop()\n                        elif Win_GetCurScreen() == 'room':\n                            global markEnterShop \n                            markEnterShop = True\n                            LeaveRoom(uin)\n                            PlayMusic( musicStart, -1)\n                class tipShop(TStatic):\n                    visible = 0\n                    initlayer = 999999\n                    bkimage = 'object/ui/guideBar/tip_enterShop.img'\n                    rect = ( 115, 2, 1, 1)\n                    def OnTimer(this):\n                        Win_ShowWidget(this, not Win_IsVisible(this))\n                "
                class tradeBtn(TButton):
                    __module__ = __name__
                    rect = (5,
                     1,
                     102,
                     31)
                    bkimage = 'object/ui/guideBar/btn_trade.img'

                    def OnClick(this):
                        CloseC2CDealDlg(bC2CDealShow)
                        print ('bPawnShopShow = %d' % bPawnShopShow)
                        if ((Win_GetCurScreen() == 'room') and LeaveRoom(uin)):
                            pass
                        if (bPawnShopShow == 1):
                            return 
                        LoginDeal()
                        residualmoeny = GetMyBill()
                        Win_SetText((uiPawnShopDlg + '.residualBill'), ('%12f' % residualmoeny))
                        Win_ShowWidget(uiPawnShopDlg, 1)
                        PlaySound(soundUI, 1)


                    class children:
                        __module__ = __name__
                        class tradeTip:
                            __module__ = __name__
                            type = 'DYLABEL'
                            initlayer = 99999
                            rect = (0,
                             60,
                             130,
                             1)
                            captionrect = (4,
                             4,
                             120,
                             1)
                            drawcolor = maskColor
                            textEdgeType = -1
                            bkimage = 'object/ui/common/img_tip.img'

                            def OnTimer(this):
                                Win_ShowWidget(this, 0)
                                Win_Timer(this, 0)





                class socialityBtn(TButton):
                    __module__ = __name__
                    rect = (142,
                     -2,
                     84,
                     39)
                    bkimage = 'object/ui/guideBar/btn_sociality.img'

                    def OnClick(this):
                        CloseC2CDealDlg(bC2CDealShow)
                        ui_setCapture(uiSocialityDlg)
                        Win_SelectSelf((uiSocialityDlg + '.kinMatchTab'))
                        Win_SetCheck((uiSocialityDlg + '.kinMatchTab'), 1)
                        sc_LoadWeb('kinMatch', 61, 108, 329, 401, ChangeURL('http%3A%2F%2Fapp.qqtang.qq.com%2Fcgi-bin%2Fa20071119jzls%2Fmy_family_rank.cgi'))
                        sc_LoadWeb('kinTeam', 61, 108, 329, 401, ChangeURL('http%3A%2F%2Fapp.qqtang.qq.com%2Fcgi-bin%2Fa20071119jzls%2Fmy_team.cgi'))
                        doUI((uiSocialityDlg + '.kinMatchTab'), 'OnClick')
                        PlaySound(soundUI, 1)



                class taskBtn(TButton):
                    __module__ = __name__
                    rect = (252,
                     -2,
                     84,
                     39)
                    bkimage = 'object/ui/guideBar/btn_task.img'
                    tipwidget = (uiGuideBar + '.tipTask')

                    def OnClick(this):
                        global markEnterShop
                        global mark_task
                        CloseC2CDealDlg(bC2CDealShow)
                        mark_task = 1
                        if ((Win_GetCurScreen() == 'selRoom') and SC_ClickShopBtn()):
                            go2shop()



                    def OnMouseMoveIn():
                        me = Win_GetMyPath()
                        x = (Win_GetX(me) + 20)
                        y = (Win_GetY(me) + 54)
                        tipIndex = SC_GetTipName()
                        ui = (uiGuideBar + '.tipTask')
                        if (tipIndex == 1):
                            text = '  \xc8\xce\xce\xf1\xb4\xfd\xc1\xec\xc8\xa1'
                        elif (tipIndex == 2):
                            text = '  \xc8\xce\xce\xf1\xbd\xf8\xd0\xd0\xd6\xd0'
                        elif (tipIndex == 3):
                            text = '  \xc8\xce\xce\xf1\xcd\xea\xb3\xc9'
                        elif (tipIndex == 4):
                            text = '  \xce\xde\xbf\xc9\xc1\xec\xc8\xa1\xc8\xce\xce\xf1'
                        else:
                            text = ''
                        Win_Move2Pos(ui, x, y)
                        Win_SetText(ui, text)



                class tipTask:
                    __module__ = __name__
                    visible = 0
                    type = 'DYLABEL'
                    initlayer = 999999
                    bkimage = 'object/ui/common/img_tip.img'
                    rect = (0,
                     0,
                     130,
                     71)
                    captionrect = (4,
                     4,
                     120,
                     1)
                    drawcolor = maskColor
                    textEdgeType = -1

                class memberBtn(TButton):
                    __module__ = __name__
                    rect = (362,
                     -2,
                     84,
                     39)
                    bkimage = 'object/ui/guideBar/btn_member.img'

                    def OnClick(this):
                        CloseC2CDealDlg(bC2CDealShow)
                        Navigate(0)



                class infoBtn(TButton):
                    __module__ = __name__
                    rect = (472,
                     -2,
                     84,
                     39)
                    bkimage = 'object/ui/guideBar/btn_info.img'

                    def OnClick(this):
                        CloseC2CDealDlg(bC2CDealShow)
                        uin = GetLocalUin()
                        print ('(%d)' % uin)
                        go2playerInfo(uin)
                        SetPlayerModeInfo(uin, 0)



                class PetBtn(TButton):
                    __module__ = __name__
                    rect = (582,
                     -2,
                     84,
                     39)
                    bkimage = 'object/ui/guideBar/btn_pet.img'

                    def OnClick(this):
                        CloseC2CDealDlg(bC2CDealShow)
                        PlaySound(soundUI, 1)
                        if ((Win_GetCurScreen() == 'room') and ui_msgBox(1)):
                            Win_ShowMsgBox('   \xb4\xf2\xbf\xaa\xb3\xe8\xce\xef\xd6\xae\xbc\xd2\xbd\xab\xcd\xcb\xb3\xf6\xb5\xb1\xc7\xb0\xb7\xbf\xbc\xe4', '\xce\xc2\xdc\xb0\xcc\xe1\xca\xbe', 0, 'UI.SysMsgbox', -6)



                class menuBtn(TCheck):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      1,
                      1,
                      2,
                      2,
                      2,
                      2),
                     (0,
                      0,
                      1,
                      1,
                      0,
                      0,
                      0,
                      0)]
                    rect = (691,
                     1,
                     90,
                     31)
                    bkimage = 'object/ui/guideBar/btn_menu.img'

                    def OnClick(this):
                        CloseC2CDealDlg(bC2CDealShow)
                        if (Win_IsChecked((uiGuideBar + '.menuBtn')) and Win_ShowWidget(uiMenuDlg, 1)):
                            print 'show'





        class menuDlg(TDlg):
            __module__ = __name__
            initlayer = 888888
            visible = 0
            style = wgtstyle_popup
            rect = (705,
             1,
             80,
             174)
            bkimagepos = (0,
             34)
            bkimage = 'object/ui/guideBar/dlg_menu.img'

            def OnSelfHide():
                Win_SetCheck((uiGuideBar + '.menuBtn'), 0)
                print 'onSelfHide    menudlg'



            def OnMouseMoveOut():
                Win_ShowWidget(uiMenuDlg, 0)


            class children:
                __module__ = __name__
                class setupBtn(TButton):
                    __module__ = __name__
                    rect = (5,
                     40,
                     70,
                     33)
                    bkimage = 'object/ui/guideBar/btn_setup.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        SC_ClickCustomSettingBtn()
                        Win_ShowWidget(uiMenuDlg, False)
                        go2setup(uin)



                class helpBtn(TButton):
                    __module__ = __name__
                    rect = (5,
                     (40 + 36),
                     70,
                     33)
                    bkimage = 'object/ui/guideBar/btn_help.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        SC_ClickHelperInfoBtn()
                        Win_ShowWidget(uiMenuDlg, False)
                        ui_jumpHelpWeb()



                class GCSBtn(TButton):
                    __module__ = __name__
                    rect = (5,
                     (40 + (36 * 2)),
                     70,
                     33)
                    bkimage = 'object/ui/guideBar/btn_GCS.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiMenuDlg, False)
                        Navigate(3)



                class recordBtn(TButton):
                    __module__ = __name__
                    rect = (5,
                     (40 + (36 * 3)),
                     70,
                     33)
                    bkimage = 'object/ui/guideBar/btn_record.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        SC_ClickWatchVedioBtn()
                        Win_ShowWidget(uiMenuDlg, False)
                        InitRecordFileDlg()
                        PlaySound(soundUI, 1)



                class QQTWebBtn(TButton):
                    __module__ = __name__
                    rect = (5,
                     (40 + (36 * 4)),
                     70,
                     33)
                    bkimage = 'object/ui/guideBar/btn_web.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiMenuDlg, False)
                        ui_jumpOfficialWeb()



                class topkinBtn(TButton):
                    __module__ = __name__
                    rect = (5,
                     (40 + (36 * 5)),
                     70,
                     33)
                    bkimage = 'object/ui/guideBar/btn_top_kin.img'

                    def OnClick(this):
                        Win_ShowWidget(uiMenuDlg, False)
                        DoKinTask('', '', 0, lookupKinID, 15)
                        ui_updateTopkinList()
                        PlaySound(soundUI, 1)





        class socialityDlg(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 60000
            rect = (30,
             45,
             400,
             500)
            darkBG = 1
            bkimage = 'object/ui/guideBar/dlg_player.img'

            def OnDenit():
                sc_HideWeb('kinMatch')
                sc_HideWeb('kinTeam')


            class children:
                __module__ = __name__
                class crossBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (360,
                     30,
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
                        Win_ShowWidget(uiSocialityDlg, 0)
                        sc_HideWeb('kinTeam')
                        sc_HideWeb('kinMatch')
                        PlaySound(soundUI, 1)



                class kinMatchTab(TTabWin):
                    __module__ = __name__
                    groupid = 3
                    groupstop = 1
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (11,
                     1,
                     64,
                     28)
                    hotcover = 'object/ui/guideBar/tab_kinMatch.img'

                    def OnClick(this):
                        sc_HideWeb('kinTeam')
                        Win_ShowWidget(uiKinDlg, 0)
                        Win_ShowWidget(uiPlayerListDlg, 0)
                        Win_SetImg(uiSocialityDlg, 'object/ui/guideBar/dlg_player.img')
                        sc_ShowWeb('kinMatch', 61, 108, 329, 401, ChangeURL('http%3A%2F%2Fapp.qqtang.qq.com%2Fcgi-bin%2Fa20071119jzls%2Fmy_family_rank.cgi'))



                class teamTab(TTabWin):
                    __module__ = __name__
                    groupid = 3
                    groupstop = 2
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (76,
                     1,
                     64,
                     28)
                    hotcover = 'object/ui/guideBar/tab_team.img'

                    def OnClick(this):
                        sc_HideWeb('kinMatch')
                        Win_ShowWidget(uiKinDlg, 0)
                        Win_ShowWidget(uiPlayerListDlg, 0)
                        Win_SetImg(uiSocialityDlg, 'object/ui/guideBar/dlg_player.img')
                        sc_ShowWeb('kinTeam', 61, 108, 329, 401, ChangeURL('http%3A%2F%2Fapp.qqtang.qq.com%2Fcgi-bin%2Fa20071119jzls%2Fmy_team.cgi'))



                class allKinMemberTab(TTabWin):
                    __module__ = __name__
                    groupid = 3
                    groupstop = 3
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (141,
                     1,
                     64,
                     28)
                    hotcover = 'object/ui/guideBar/tab_allKinMember.img'

                    def OnClick(this):
                        global playerMode
                        sc_HideWeb('kinTeam')
                        sc_HideWeb('kinMatch')
                        Win_ShowWidget(uiKinDlg, 0)
                        Win_SetImg(uiSocialityDlg, 'object/ui/guideBar/dlg_player.img')
                        KinID = GetKinParam(0)
                        if ((KinID == 0) and Win_ShowWidget(uiPlayerListDlg, 0)):
                            Win_SelectSelf((uiSocialityDlg + '.playerTab'))
                            ui_setCapture(uiKinCreateHintDlg)
                            playerMode = 0
                            updatePlayer()
                        PlaySound(soundUI, 1)



                class kinTab(TTabWin):
                    __module__ = __name__
                    groupid = 3
                    groupstop = 4
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (206,
                     1,
                     64,
                     28)
                    hotcover = 'object/ui/guideBar/tab_kin.img'

                    def OnClick(this):
                        global playerMode
                        sc_HideWeb('kinTeam')
                        sc_HideWeb('kinMatch')
                        kinID = GetKinParam(0)
                        if ((kinID <= 0) and ui_setCapture(uiKinCreateHintDlg)):
                            Win_ShowWidget(uiPlayerListDlg, 0)
                            Win_SelectSelf((uiSocialityDlg + '.playerTab'))
                            playerMode = 0
                            updatePlayer()
                        PlaySound(soundUI, 1)



                class playerListDlg(TStatic):
                    __module__ = __name__
                    rect = (4,
                     28,
                     382,
                     490)
                    class children:
                        __module__ = __name__
                        class friendMask(TStatic):
                            __module__ = __name__
                            initlayer = 50000
                            rect = (27,
                             34,
                             1,
                             1)
                            bkimage = 'object/ui/guideBar/img_friendMask.img'
                            class children:
                                __module__ = __name__
                                class tipBtn(TButton):
                                    __module__ = __name__
                                    initlayer = 20000
                                    rect = (0,
                                     0,
                                     1,
                                     1)

                                    def OnClick(this):
                                        if ((playerMode == 1) and InvalidOperation()):
                                            pass





                        class playerInfo1(TButton):
                            __module__ = __name__
                            initlayer = 20000
                            rect = (31,
                             44,
                             321,
                             23)
                            bkimage = 'object/ui/guideBar/btn_player.img'
                            framescheme = [(0,
                              0,
                              0,
                              0,
                              -1,
                              -1,
                              -1,
                              -1)]
                            bkImgFlag = dt_center

                            def OnClick(this):
                                i = getMyIdx2()
                                print 'FindFriend  ',
                                print uins[(i - 1)],
                                print '...',
                                print i
                                go2playerInfo(uins[(i - 1)])



                            def OnRBtnUp(pos):
                                global friendName
                                global friendUin
                                (x, y,) = pos
                                if ((x + 77) > 800):
                                    x = (800 - 77)
                                Win_Move2Pos(uiPlayerMenu, x, y)
                                i = getMyIdx2()
                                friendUin = uins[(i - 1)]
                                friendName = Win_GetText((Win_GetMyPath() + '.name'))
                                kinID = GetKinParam(0)
                                if ((kinID > 0) and Win_ShowWidget((uiPlayerMenu + '.kininviteBtn'), kinID)):
                                    pass
                                Win_ShowWidget((uiPlayerMenu + '.addBtn'), (not GetAttribute(friendUin, 0)))
                                Win_ShowWidget((uiPlayerMenu + '.deleteBtn'), GetAttribute(friendUin, 0))
                                Win_ShowWidget((uiPlayerMenu + '.shieldBtn'), (not GetAttribute(friendUin, 1)))
                                Win_ShowWidget((uiPlayerMenu + '.unshieldBtn'), GetAttribute(friendUin, 1))
                                Win_ShowWidget(uiPlayerMenu, 1)



                            def OnMouseMoveIn():
                                idx = getMyIdx2()
                                if ((idx > 1) and Win_SetValue((uiPlayerListDlg + ('.playerInfo%d' % (idx - 1))), 20000.0, 902)):
                                    pass
                                if ((idx < 16) and Win_SetValue((uiPlayerListDlg + ('.playerInfo%d' % (idx + 1))), 20000.0, 902)):
                                    pass
                                Win_SetValue((uiPlayerListDlg + ('.playerInfo%d' % idx)), 35000.0, 902)


                            class children:
                                __module__ = __name__
                                class gender(TStatic):
                                    __module__ = __name__
                                    rect = (292,
                                     3,
                                     16,
                                     15)
                                    bkimage = 'res/uires/selRoom/icon/nan.img'

                                class levelIcon(TLevelIcon):
                                    __module__ = __name__
                                    rect = (30,
                                     1,
                                     39,
                                     15)

                                class goldDiamond(TStatic):
                                    __module__ = __name__
                                    visible = 0
                                    rect = (53,
                                     4,
                                     20,
                                     19)
                                    framescheme = [(0,
                                      15,
                                      0,
                                      15,
                                      0,
                                      15,
                                      0,
                                      15)]
                                    bkimage = 'res/uires/selRoom/goldDiamond.img'

                                class kintotem(TStatic):
                                    __module__ = __name__
                                    visible = 0
                                    rect = (8,
                                     2,
                                     16,
                                     15)
                                    framescheme = [(0,
                                      13,
                                      0,
                                      13,
                                      0,
                                      13,
                                      0,
                                      13)]

                                class league(TStatic):
                                    __module__ = __name__
                                    visible = 0
                                    rect = (92,
                                     4,
                                     16,
                                     15)
                                    framescheme = [(0,
                                      13,
                                      0,
                                      13,
                                      0,
                                      13,
                                      0,
                                      13)]
                                    bkimage = 'res/uires/selRoom/diamond_bk.img'

                                class name(TLabel,
                                 Static):
                                    __module__ = __name__
                                    rect = (168,
                                     6,
                                     120,
                                     12)
                                    drawcolor = lightColor
                                    textEdgeType = 1
                                    textEdgeColor = maskColor
                                    textstyle = dt_right

                                class namecard(TStatic):
                                    __module__ = __name__
                                    framescheme = [(0,
                                      99,
                                      0,
                                      99,
                                      0,
                                      99,
                                      0,
                                      99)]
                                    initlayer = -100
                                    rect = (7,
                                     1,
                                     1,
                                     1)

                                class namecardbound(TStatic):
                                    __module__ = __name__
                                    framescheme = [(0,
                                      99,
                                      0,
                                      99,
                                      0,
                                      99,
                                      0,
                                      99)]
                                    rect = (7,
                                     1,
                                     1,
                                     1)



                        class playerInfo2(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + 24),
                             321,
                             23)

                        class playerInfo3(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 2)),
                             321,
                             23)

                        class playerInfo4(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 3)),
                             321,
                             23)

                        class playerInfo5(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 4)),
                             321,
                             23)

                        class playerInfo6(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 5)),
                             321,
                             23)

                        class playerInfo7(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 6)),
                             321,
                             23)

                        class playerInfo8(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 7)),
                             321,
                             23)

                        class playerInfo9(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 8)),
                             321,
                             23)

                        class playerInfo10(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 9)),
                             321,
                             23)

                        class playerInfo11(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 10)),
                             321,
                             23)

                        class playerInfo12(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 11)),
                             321,
                             23)

                        class playerInfo13(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 12)),
                             321,
                             23)

                        class playerInfo14(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 13)),
                             321,
                             23)

                        class playerInfo15(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 14)),
                             321,
                             23)

                        class playerInfo16(playerInfo1):
                            __module__ = __name__
                            rect = (31,
                             (44 + (24 * 15)),
                             321,
                             23)

                        class left(TButton):
                            __module__ = __name__
                            rect = (280,
                             435,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_left.img'
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]

                            def OnClick(this):
                                pos = myGetPlayerPos()
                                if ((pos != 0) and PlaySound(soundUI, 1)):
                                    pos = max((pos - (defPlayerCnt - 1)), 0)
                                    mySetPlayerPos(pos)
                                    updatePlayer()



                        class right(TButton):
                            __module__ = __name__
                            rect = (311,
                             435,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_right.img'
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]

                            def OnClick(this):
                                PlayerList_right()
                                pos = myGetPlayerPos()
                                cnt = myGetPlayerCnt()
                                if (((pos + (defPlayerCnt - 1)) < cnt) and PlaySound(soundUI, 1)):
                                    pos += (defPlayerCnt - 1)
                                    mySetPlayerPos(pos)
                                    updatePlayer()





                class kinDlg(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (4,
                     28,
                     382,
                     490)
                    class children:
                        __module__ = __name__
                        class kinmemberTab(TTabWin):
                            __module__ = __name__
                            groupid = 4
                            groupstop = 1
                            rect = (0,
                             0,
                             1,
                             1)
                            hotrect = (20,
                             5,
                             63,
                             34)
                            hotcover = 'object/ui/guideBar/tab_kinMember.img'

                            def OnClick(this):
                                Win_SetImg(uiSocialityDlg, 'object/ui/guideBar/dlg_kinMember.img')
                                Win_ShowWidget(uiKinManagerDlg, 0)
                                Win_ShowWidget(uiKinMemberDlg, 1)
                                ui_updateMemberList()
                                info = GetInviteKinInfo(1)
                                uin = GetLocalUin()
                                if ((uin == info.m_dwUin) and Win_ShowWidget((uiKinManagerDlg + '.amend'), 1)):
                                    Win_ShowWidget((uiKinManagerDlg + '.issue'), 1)
                                PlaySound(soundUI, 1)



                        class kinmanagerTab(TTabWin):
                            __module__ = __name__
                            groupid = 4
                            groupstop = 2
                            rect = (0,
                             0,
                             1,
                             1)
                            hotrect = (85,
                             5,
                             63,
                             34)
                            hotcover = 'object/ui/guideBar/tab_kinMgr.img'

                            def OnClick(this):
                                Win_SetImg(uiSocialityDlg, 'object/ui/guideBar/dlg_kinMgr.img')
                                Win_ShowWidget(uiKinManagerDlg, 1)
                                Win_ShowWidget(uiKinMemberDlg, 0)
                                for i in range(5):
                                    Win_SetText((uiKinManagerDlg + ('.customPosition%d' % i)), GetKinPosition(i))

                                info = GetInviteKinInfo(1)
                                uin = GetLocalUin()
                                maxKinmemberCnt = ((info.m_dwStatus & -1048576) >> 20)
                                MemberNum = info.m_wMemberNum
                                kinmemcntstatus = ((str(MemberNum) + '/') + str(maxKinmemberCnt))
                                Win_SetText((uiKinManagerDlg + '.KinMemberCntStatus'), kinmemcntstatus)
                                Win_SetText((uiKinManagerDlg + '.text'), info.m_szContent)
                                totemID = info.m_stKinFlagID.m_iFlagID
                                Win_SetImg((uiKinManagerDlg + '.totemBtn'), ('object/ui/kinTotem/%03d.img' % (totemID)))
                                if ((uin == info.m_dwUin) and Win_SetFocus((uiKinManagerDlg + '.customPosition0'))):
                                    IsDismiss = GetKinMemberHonor(uin, 2)
                                    if ((IsDismiss == 1) and Win_ShowWidget((uiKinManagerDlg + '.dismissBtn'), 0)):
                                        Win_ShowWidget((uiKinManagerDlg + '.quitBtn'), 0)
                                        Win_ShowWidget((uiKinManagerDlg + '.canceldismissBtn'), 1)
                                        Win_SetImg((uiKinManagerDlg + '.canceldismissBtn'), 'object/ui/guideBar/btn_cancel_dismiss.img')
                                PlaySound(soundUI, 1)



                        class kinmanagerDlg(TStatic):
                            __module__ = __name__
                            visible = 0
                            rect = (0,
                             30,
                             377,
                             429)
                            class children:
                                __module__ = __name__
                                class confirm(TButton):
                                    __module__ = __name__
                                    rect = (212,
                                     388,
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
                                        placeholder = ('%c' % 7)
                                        if ((Win_GetText((uiKinManagerDlg + '.customPosition0')) != '') and ((Win_GetText((uiKinManagerDlg + '.customPosition1')) != '') and ((Win_GetText((uiKinManagerDlg + '.customPosition2')) != '') and ((Win_GetText((uiKinManagerDlg + '.customPosition3')) != '') and (Win_GetText((uiKinManagerDlg + '.customPosition4')) != ''))))):
                                            positioninfo = (((((((((Win_GetText((uiKinManagerDlg + '.customPosition0')) + placeholder) + Win_GetText((uiKinManagerDlg + '.customPosition1'))) + placeholder) + Win_GetText((uiKinManagerDlg + '.customPosition2'))) + placeholder) + Win_GetText((uiKinManagerDlg + '.customPosition3'))) + placeholder) + Win_GetText((uiKinManagerDlg + '.customPosition4'))) + placeholder)
                                            DoKinTask('', positioninfo, len(positioninfo), 0, 9)
                                        DoKinTask('', str(customtotemID), len(str(customtotemID)), 0, 3)
                                        proclaim = Win_GetText((uiKinManagerDlg + '.text'))
                                        if ((proclaim != '') and DoKinTask('', proclaim, len(proclaim), 0, 13)):
                                            pass
                                        PlaySound(soundUI, 1)



                                class dismissBtn(TButton):
                                    __module__ = __name__
                                    rect = (34,
                                     388,
                                     69,
                                     32)
                                    bkimage = 'object/ui/guideBar/btn_dismiss.img'
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]

                                    def OnClick(this):
                                        uin = GetLocalUin()
                                        Win_SetText((uiKinTipDlg + '.prompt'), '\xc4\xfa\xc8\xb7\xb6\xa8\xd2\xaa\xbd\xe2\xc9\xa2\xc4\xfa\xb5\xc4\xbc\xd2\xd7\xe5\xc2\xf0?')
                                        Win_SetText((uiKinTipDlg + '.pParam1'), '')
                                        Win_SetText((uiKinTipDlg + '.pParam2'), '')
                                        Win_SetText((uiKinTipDlg + '.uin'), str(uin))
                                        Win_SetText((uiKinTipDlg + '.TaskMode'), '7')
                                        ui_setCapture(uiKinTipDlg)
                                        PlaySound(soundUI, 1)
                                        doUI((uiKinDlg + '.kinmanagerTab'), 'OnClick')



                                class canceldismissBtn(dismissBtn):
                                    __module__ = __name__
                                    bkimage = 'object/ui/guideBar/btn_cancel_dismiss.img'
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]

                                    def OnClick(this):
                                        DoKinTask('', '', 0, uin, 7)
                                        doUI((uiKinDlg + '.kinmanagerTab'), 'OnClick')



                                class quitBtn(TButton):
                                    __module__ = __name__
                                    rect = (34,
                                     388,
                                     66,
                                     27)
                                    bkimage = 'object/ui/guideBar/btn_quitKin.img'
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]

                                    def OnClick(this):
                                        print 'Click the kininvitedlg confirm'
                                        uin = GetLocalUin()
                                        Win_SetText((uiKinTipDlg + '.prompt'), '\xc4\xfa\xc8\xb7\xb6\xa8\xd2\xaa\xcd\xcb\xb3\xf6\xbc\xd2\xd7\xe5\xc2\xf0?')
                                        Win_SetText((uiKinTipDlg + '.pParam1'), '')
                                        Win_SetText((uiKinTipDlg + '.pParam2'), '')
                                        Win_SetText((uiKinTipDlg + '.uin'), str(uin))
                                        Win_SetText((uiKinTipDlg + '.TaskMode'), '6')
                                        ui_setCapture(uiKinTipDlg)
                                        PlaySound(soundUI, 1)
                                        doUI((uiKinDlg + '.kinmanagerTab'), 'OnClick')



                                class KinMemberCntStatus(TLabel):
                                    __module__ = __name__
                                    textstyle = (dt_center + dt_vcenter)
                                    rect = (306,
                                     332,
                                     60,
                                     24)
                                    drawcolor = kinColor

                                class totemBtn(TCheck):
                                    __module__ = __name__
                                    initlayer = 9000
                                    extendstyle = ui_btn_style_none
                                    framescheme = [(0,
                                      0,
                                      1,
                                      1,
                                      2,
                                      2,
                                      2,
                                      2),
                                     (2,
                                      2,
                                      1,
                                      1,
                                      0,
                                      0,
                                      2,
                                      2)]
                                    rect = (122,
                                     342,
                                     (24 - 5),
                                     (26 - 4))

                                    def OnClick(this):
                                        info = GetInviteKinInfo(1)
                                        uin = GetLocalUin()
                                        if ((uin == info.m_dwUin) and Win_IsChecked((uiKinManagerDlg + '.totemBtn'))):
                                            if (oldWinEventCnt == Win_GetEventCnt()):
                                                if Win_SetCheck((uiKinManagerDlg + '.totemBtn'), False):
                                                    pass
                                            else:
                                                Win_ShowWidget((uiKinManagerDlg + '.totemBtn.totemDlg'), False)


                                    class children:
                                        __module__ = __name__
                                        class totemDlg(TWidget):
                                            __module__ = __name__
                                            visible = 0
                                            style = wgtstyle_popup
                                            rect = (23,
                                             (-137 + 17),
                                             174,
                                             137)
                                            bkimage = 'object/ui/chat/dlg_face.img'

                                            def OnSelfHide():
                                                global oldWinEventCnt
                                                oldWinEventCnt = Win_GetEventCnt()
                                                Win_SetCheck((uiKinManagerDlg + '.totemBtn'), False)


                                            class children:
                                                __module__ = __name__
                                                class box(TStatic):
                                                    __module__ = __name__
                                                    rect = (0,
                                                     0,
                                                     10,
                                                     10)
                                                    class children:
                                                        __module__ = __name__
                                                        class face0(TButton):
                                                            __module__ = __name__
                                                            framescheme = [(0,
                                                              0,
                                                              0,
                                                              99,
                                                              0,
                                                              0,
                                                              0,
                                                              0)]
                                                            rect = (8,
                                                             6,
                                                             26,
                                                             26)
                                                            bkImgFlag = dt_center
                                                            bkimage = 'object/ui/kinTotem/001.img'

                                                            def OnClick(this):
                                                                global customtotemID
                                                                i = ((totemPage * 24) + getMyIdx())
                                                                customtotemID = (i + 1)
                                                                Win_SetImg((uiKinManagerDlg + '.totemBtn'), ('object/ui/kinTotem/%03d.img' % (customtotemID)))
                                                                Win_ShowWidget((uiKinManagerDlg + '.totemBtn.totemDlg'), 0)



                                                        class face1(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + 27),
                                                             6,
                                                             26,
                                                             26)

                                                        class face2(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 2)),
                                                             6,
                                                             26,
                                                             26)

                                                        class face3(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 3)),
                                                             6,
                                                             26,
                                                             26)

                                                        class face4(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 4)),
                                                             6,
                                                             26,
                                                             26)

                                                        class face5(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 5)),
                                                             6,
                                                             26,
                                                             26)

                                                        class face6(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 0)),
                                                             (6 + (27 * 1)),
                                                             26,
                                                             26)

                                                        class face7(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 1)),
                                                             (6 + (27 * 1)),
                                                             26,
                                                             26)

                                                        class face8(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 2)),
                                                             (6 + (27 * 1)),
                                                             26,
                                                             26)

                                                        class face9(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 3)),
                                                             (6 + (27 * 1)),
                                                             26,
                                                             26)

                                                        class face10(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 4)),
                                                             (6 + (27 * 1)),
                                                             26,
                                                             26)

                                                        class face11(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 5)),
                                                             (6 + (27 * 1)),
                                                             26,
                                                             26)

                                                        class face12(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 0)),
                                                             (6 + (27 * 2)),
                                                             26,
                                                             26)

                                                        class face13(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 1)),
                                                             (6 + (27 * 2)),
                                                             26,
                                                             26)

                                                        class face14(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 2)),
                                                             (6 + (27 * 2)),
                                                             26,
                                                             26)

                                                        class face15(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 3)),
                                                             (6 + (27 * 2)),
                                                             26,
                                                             26)

                                                        class face16(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 4)),
                                                             (6 + (27 * 2)),
                                                             26,
                                                             26)

                                                        class face17(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 5)),
                                                             (6 + (27 * 2)),
                                                             26,
                                                             26)

                                                        class face18(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 0)),
                                                             (6 + (27 * 3)),
                                                             26,
                                                             26)

                                                        class face19(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 1)),
                                                             (6 + (27 * 3)),
                                                             26,
                                                             26)

                                                        class face20(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 2)),
                                                             (6 + (27 * 3)),
                                                             26,
                                                             26)

                                                        class face21(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 3)),
                                                             (6 + (27 * 3)),
                                                             26,
                                                             26)

                                                        class face22(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 4)),
                                                             (6 + (27 * 3)),
                                                             26,
                                                             26)

                                                        class face23(face0):
                                                            __module__ = __name__
                                                            rect = ((8 + (27 * 5)),
                                                             (6 + (27 * 3)),
                                                             26,
                                                             26)



                                                class pageLab(TLabel):
                                                    __module__ = __name__
                                                    rect = ((102 + 22),
                                                     117,
                                                     18,
                                                     12)
                                                    drawcolor = lightColor
                                                    textEdgeColor = (6,
                                                     102,
                                                     231,
                                                     255)

                                                class leftBtn(TButton):
                                                    __module__ = __name__
                                                    rect = (102,
                                                     115,
                                                     17,
                                                     17)
                                                    bkimage = 'res/uires/face/biaoq_zuo.img'

                                                    def OnClick(this):
                                                        global totemPage
                                                        totemPage -= 1
                                                        if (totemPage < 0):
                                                            totemPage = (totemPageNum - 1)
                                                        settotemPage(totemPage, totemPageNum)
                                                        PlaySound(soundUI, 1)



                                                class rightBtn(TButton):
                                                    __module__ = __name__
                                                    rect = (148,
                                                     115,
                                                     17,
                                                     17)
                                                    bkimage = 'res/uires/face/biaoq_you.img'

                                                    def OnClick(this):
                                                        global totemPage
                                                        totemPage += 1
                                                        if (totemPage >= totemPageNum):
                                                            totemPage = 0
                                                        settotemPage(totemPage, totemPageNum)
                                                        PlaySound(soundUI, 1)







                                class customPosition0(TRichEdit):
                                    __module__ = __name__
                                    textstyle = (dt_center + dt_vcenter)
                                    maxchar = 8
                                    rect = (200,
                                     173,
                                     145,
                                     24)
                                    drawcolor = (255,
                                     123,
                                     44,
                                     255)
                                    textEdgeColor = maskColor
                                    captionrect = (40,
                                     8,
                                     100,
                                     12)

                                    def OnTab():
                                        idx = getMyIdx2()
                                        Win_SetFocus((uiKinManagerDlg + ('.customPosition%d' % ((idx + 1) % 5))))



                                class customPosition1(customPosition0):
                                    __module__ = __name__
                                    rect = (200,
                                     (173 + 26),
                                     145,
                                     24)
                                    drawcolor = (247,
                                     65,
                                     255,
                                     255)

                                class customPosition2(customPosition0):
                                    __module__ = __name__
                                    rect = (200,
                                     (173 + (2 * 26)),
                                     145,
                                     24)
                                    drawcolor = (69,
                                     139,
                                     255,
                                     255)

                                class customPosition3(customPosition0):
                                    __module__ = __name__
                                    rect = (200,
                                     (173 + (3 * 26)),
                                     145,
                                     24)
                                    drawcolor = (179,
                                     203,
                                     15,
                                     255)

                                class customPosition4(customPosition0):
                                    __module__ = __name__
                                    rect = (200,
                                     (173 + (4 * 26)),
                                     145,
                                     24)
                                    drawcolor = (24,
                                     201,
                                     99,
                                     255)

                                class text:
                                    __module__ = __name__
                                    type = 'MULTIEDIT'
                                    maxchar = 250
                                    rect = (37,
                                     52,
                                     308,
                                     80)
                                    drawcolor = (153,
                                     244,
                                     255,
                                     255)
                                    bkcolor = (0,
                                     0,
                                     0,
                                     0)
                                    textEdgeColor = (255,
                                     0,
                                     0,
                                     0)
                                    textsize = 12
                                    rowspace = 4
                                    editable = 1
                                    returnflag = 1
                                    maxline = 4
                                    richmode = 0
                                    accel = (('OnAccel_FocusPaste',
                                      86,
                                      17,
                                      0,
                                      0),
                                     ('OnAccel_FocusCut',
                                      88,
                                      17,
                                      0,
                                      0),
                                     ('OnAccel_FocusCopy',
                                      67,
                                      17,
                                      0,
                                      0))

                                    def OnAccel_FocusPaste():
                                        Win_FocusOnPaste()



                                    def OnAccel_FocusCut():
                                        Win_FocusOnCut()



                                    def OnAccel_FocusCopy():
                                        Win_FocusOnCopy()





                        class kinmemberDlg(TStatic):
                            __module__ = __name__
                            visible = 0
                            rect = (0,
                             30,
                             400,
                             500)
                            class children:
                                __module__ = __name__
                                class kinHonor(TLabel):
                                    __module__ = __name__
                                    textstyle = (dt_center + dt_vcenter)
                                    rect = (250,
                                     32,
                                     70,
                                     25)
                                    caption = '\xb4\xf3\xcc\xec\xca\xb9'
                                    drawcolor = kinColor
                                    textEdgeColor = maskColor

                                class name(TLabel):
                                    __module__ = __name__
                                    textstyle = (dt_center + dt_vcenter)
                                    rect = (20,
                                     32,
                                     120,
                                     25)
                                    caption = '\xb4\xf3\xcc\xec\xca\xb9'
                                    drawcolor = kinColor
                                    textEdgeColor = maskColor

                                class OnlineCount(TLabel):
                                    __module__ = __name__
                                    textstyle = (dt_center + dt_vcenter)
                                    rect = (284,
                                     410,
                                     50,
                                     25)
                                    caption = 'abc'
                                    drawcolor = kinColor
                                    textEdgeColor = maskColor

                                class kinCount(TLabel,
                                 Static):
                                    __module__ = __name__
                                    textstyle = (dt_center + dt_vcenter)
                                    rect = (202,
                                     410,
                                     50,
                                     25)
                                    caption = 'abc'
                                    drawcolor = kinColor
                                    textEdgeColor = maskColor

                                class OnlineChk(TCheck):
                                    __module__ = __name__
                                    rect = (20,
                                     418,
                                     60,
                                     20)
                                    framescheme = [(-1,
                                      -1,
                                      -1,
                                      -1,
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
                                      0,
                                      0)]
                                    bkimage = 'object/ui/common/btn_check.img'

                                    def OnClick(this):
                                        global ShowOnline
                                        if Win_IsChecked(this):
                                            ShowOnline = 1
                                            ui_updateMemberList()
                                        else:
                                            ShowOnline = 0
                                            ui_updateMemberList()
                                        PlaySound(soundUI, 1)



                                class kinOprMenu(TWidget):
                                    __module__ = __name__
                                    initlayer = 9001
                                    visible = 0
                                    style = wgtstyle_popup
                                    rect = (0,
                                     0,
                                     77,
                                     99)
                                    bkimage = 'object/ui/guideBar/kin/bg_kin_menu.img'
                                    class children:
                                        __module__ = __name__
                                        class promotion(TButton):
                                            __module__ = __name__
                                            rect = (5,
                                             6,
                                             50,
                                             14)
                                            bkimage = 'object/ui/guideBar/btn_playermenuChoose.img'
                                            framescheme = [(0,
                                              0,
                                              0,
                                              0,
                                              -1,
                                              -1,
                                              -1,
                                              -1)]
                                            caption = '\xd6\xb0\xce\xbb\xcc\xe1\xc9\xfd'
                                            drawcolor = lightColor
                                            textEdgeType = -1

                                            def OnClick(this):
                                                Win_ShowWidget((uiKinMemberDlg + '.kinOprMenu'), 0)
                                                PlaySound(soundUI, 1)
                                                info = MemberList().at(ActiveMemberPos)
                                                uin = info.Uin
                                                print ('uin = %d' % uin)
                                                position = GetKinPositionByUin(info.Uin)
                                                DoKinTask('Y', position, len(position), uin, 2)



                                        class demotion(TButton):
                                            __module__ = __name__
                                            rect = (5,
                                             ((4 + 25) + 1),
                                             50,
                                             14)
                                            bkimage = 'object/ui/guideBar/btn_playermenuChoose.img'
                                            framescheme = [(0,
                                              0,
                                              0,
                                              0,
                                              -1,
                                              -1,
                                              -1,
                                              -1)]
                                            caption = '\xd6\xb0\xce\xbb\xcf\xc2\xb5\xf7'
                                            drawcolor = lightColor
                                            textEdgeType = -1

                                            def OnClick(this):
                                                Win_ShowWidget((uiKinMemberDlg + '.kinOprMenu'), 0)
                                                PlaySound(soundUI, 1)
                                                info = MemberList().at(ActiveMemberPos)
                                                uin = info.Uin
                                                print ('uin = %d' % uin)
                                                position = GetKinPositionByUin(info.Uin)
                                                DoKinTask('N', position, len(position), uin, 2)



                                        class fire(TButton):
                                            __module__ = __name__
                                            rect = (5,
                                             (4 + 50),
                                             50,
                                             14)
                                            bkimage = 'object/ui/guideBar/btn_playermenuChoose.img'
                                            framescheme = [(0,
                                              0,
                                              0,
                                              0,
                                              -1,
                                              -1,
                                              -1,
                                              -1)]
                                            caption = '\xbf\xaa\xb3\xfd\xb3\xc9\xd4\xb1'
                                            drawcolor = lightColor
                                            textEdgeType = -1

                                            def OnClick(this):
                                                Win_ShowWidget((uiKinMemberDlg + '.kinOprMenu'), 0)
                                                PlaySound(soundUI, 1)
                                                info = MemberList().at(ActiveMemberPos)
                                                uin = info.Uin
                                                Win_SetText((uiKinTipDlg + '.prompt'), ('\xc4\xfa\xc8\xb7\xb6\xa8\xd2\xaa\xbf\xaa\xb3\xfd%s[%d]\xc2\xf0?' % (info.nickname,
                                                 uin)))
                                                Win_SetText((uiKinTipDlg + '.pParam1'), '')
                                                Win_SetText((uiKinTipDlg + '.pParam2'), '')
                                                Win_SetText((uiKinTipDlg + '.uin'), str(uin))
                                                Win_SetText((uiKinTipDlg + '.TaskMode'), '5')
                                                ui_setCapture(uiKinTipDlg)





                                class scroll(TVScroll):
                                    __module__ = __name__
                                    rect = (345,
                                     77,
                                     26,
                                     198)
                                    pos = 0

                                    def OnPosChange():
                                        global kinMemberCnt
                                        global CurrentPos
                                        kinMemberCnt = MemberList().getCnt()
                                        if (ShowOnline == 0):
                                            ShowCnt = MemberList().getCnt()
                                        else:
                                            ShowCnt = MemberList().getOnlineCnt()
                                        ui = uiKinMemberDlg
                                        Win_SetRange((ui + '.scroll'), max((ShowCnt - defkinDlgCnt), 0))
                                        pos = Win_GetPos((ui + '.scroll'))
                                        if ((pos != CurrentPos) and PlaySound(soundUI, 1)):
                                            CurrentPos = pos
                                            for i in range(defkinDlgCnt):
                                                ui = (uiKinMemberDlg + ('.MemberPlayer%d' % i))
                                                Win_SetText((ui + '.NickName'), '')
                                                Win_SetText((ui + '.Grade'), '')
                                                Win_SetImg((ui + '.genderPic'), '')
                                                Win_SetText((ui + '.Position'), '')
                                                Win_SetText((ui + '.honor'), '')
                                                idx = (CurrentPos + i)
                                                if ((idx >= ShowCnt) and Win_SetText((ui + '.NickName'), '')):
                                                    Win_SetText((ui + '.Grade'), '')
                                                    Win_SetImg((ui + '.genderPic'), '')
                                                    Win_SetText((ui + '.Position'), '')
                                                    Win_SetText((ui + '.honor'), '')
                                                    Win_EnableWidget(ui, 0)
                                                    continue
                                                Win_SetCheck(ui, (idx == ActiveMemberPos))



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



                                class MemberPlayer0(TButton):
                                    __module__ = __name__
                                    bkcolor = (222,
                                     255,
                                     36,
                                     255)
                                    rect = (22,
                                     100,
                                     314,
                                     24)
                                    groupstop = 0
                                    framescheme = [(0,
                                      0,
                                      0,
                                      0,
                                      -1,
                                      -1,
                                      -1,
                                      -1)]
                                    bkimage = 'object/ui/guideBar/btn_player.img'
                                    bkimagepos = (0,
                                     -5)

                                    def OnClick(this):
                                        global ActiveMemberPos
                                        idx = getTailNum(this)
                                        ActiveMemberPos = (CurrentPos + idx)
                                        PlaySound(soundUI, 1)



                                    def OnRBtnUp(pos):
                                        global ActiveMemberPos
                                        PlaySound(soundUI, 1)
                                        me = Win_GetMyPath()
                                        idx = getTailNum(me)
                                        ActiveMemberPos = (CurrentPos + idx)
                                        (x, y,) = pos
                                        if ((x + 77) > 600):
                                            x = (600 - 77)
                                        Win_EnableWidget((uiKinMemberDlg + '.kinOprMenu.fire'), 1)
                                        myUin = GetLocalUin()
                                        kininfo = GetInviteKinInfo(1)
                                        if ((myUin != kininfo.m_dwUin) and Win_EnableWidget((uiKinMemberDlg + '.kinOprMenu.fire'), 0)):
                                            pass
                                        Win_Move2Pos((uiKinMemberDlg + '.kinOprMenu'), x, y)
                                        Win_ShowWidget((uiKinMemberDlg + '.kinOprMenu'), 1)
                                        Win_SetFocus((uiKinMemberDlg + '.kinOprMenu.promotion'))


                                    class children:
                                        __module__ = __name__
                                        class NickName(TLabel,
                                         Static):
                                            __module__ = __name__
                                            textstyle = (dt_center + dt_vcenter)
                                            rect = (0,
                                             0,
                                             77,
                                             24)
                                            drawcolor = kinColor
                                            textEdgeType = -1

                                        class genderPic(TStatic):
                                            __module__ = __name__
                                            rect = (88,
                                             0,
                                             34,
                                             24)
                                            textEdgeType = -1

                                        class Grade(TLabel,
                                         Static):
                                            __module__ = __name__
                                            textstyle = (dt_center + dt_vcenter)
                                            rect = (115,
                                             0,
                                             60,
                                             24)
                                            textEdgeType = -1
                                            drawcolor = kinColor

                                        class Position(TLabel,
                                         Static):
                                            __module__ = __name__
                                            textstyle = (dt_center + dt_vcenter)
                                            rect = (175,
                                             0,
                                             57,
                                             24)
                                            textEdgeType = -1
                                            drawcolor = kinColor

                                        class honor(TLabel,
                                         Static):
                                            __module__ = __name__
                                            textstyle = (dt_center + dt_vcenter)
                                            rect = (230,
                                             0,
                                             85,
                                             24)
                                            textEdgeType = -1
                                            drawcolor = kinColor



                                class MemberPlayer1(MemberPlayer0):
                                    __module__ = __name__
                                    rect = (22,
                                     (100 + 24),
                                     314,
                                     24)
                                    groupstop = 1

                                class MemberPlayer2(MemberPlayer0):
                                    __module__ = __name__
                                    rect = (22,
                                     (100 + (2 * 24)),
                                     314,
                                     24)
                                    groupstop = 2

                                class MemberPlayer3(MemberPlayer0):
                                    __module__ = __name__
                                    rect = (22,
                                     (100 + (3 * 24)),
                                     314,
                                     24)
                                    groupstop = 3

                                class MemberPlayer4(MemberPlayer0):
                                    __module__ = __name__
                                    rect = (22,
                                     (100 + (4 * 24)),
                                     314,
                                     24)
                                    groupstop = 4

                                class MemberPlayer5(MemberPlayer0):
                                    __module__ = __name__
                                    rect = (22,
                                     (100 + (5 * 24)),
                                     314,
                                     24)
                                    groupstop = 5

                                class MemberPlayer6(MemberPlayer0):
                                    __module__ = __name__
                                    rect = (22,
                                     (100 + (6 * 24)),
                                     314,
                                     24)
                                    groupstop = 6

                                class amend(TButton):
                                    __module__ = __name__
                                    rect = (315,
                                     322,
                                     43,
                                     31)
                                    bkimage = 'object/ui/guideBar/btn_amend.img'
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]

                                    def OnClick(this):
                                        Win_SetValue((uiKinMemberDlg + '.text'), 1, 905)
                                        Win_SetDrawColor((uiKinMemberDlg + '.text'), 255, 255, 255, 255)
                                        Win_SetFocus((uiKinMemberDlg + '.text'))
                                        PlaySound(soundUI, 1)



                                class issue(TButton):
                                    __module__ = __name__
                                    rect = (315,
                                     368,
                                     43,
                                     31)
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]
                                    bkimage = 'object/ui/guideBar/btn_issue.img'

                                    def OnClick(this):
                                        broadcast = Win_GetText((uiKinMemberDlg + '.text'))
                                        if ((broadcast != '') and DoKinTask('', broadcast, len(broadcast), 0, 14)):
                                            pass
                                        Win_SetValue((uiKinMemberDlg + '.text'), 0, 905)
                                        Win_SetDrawColor((uiKinMemberDlg + '.text'), 255, 123, 44, 255)
                                        PlaySound(soundUI, 1)



                                class text:
                                    __module__ = __name__
                                    type = 'MULTIEDIT'
                                    maxchar = 134
                                    rect = (28,
                                     316,
                                     260,
                                     80)
                                    drawcolor = kinColor
                                    textEdgeColor = maskColor
                                    textsize = 12
                                    rowspace = 4
                                    editable = 0
                                    returnflag = 1
                                    maxline = 4
                                    richmode = 0
                                    accel = (('OnAccel_FocusPaste',
                                      86,
                                      17,
                                      0,
                                      0),
                                     ('OnAccel_FocusCut',
                                      88,
                                      17,
                                      0,
                                      0),
                                     ('OnAccel_FocusCopy',
                                      67,
                                      17,
                                      0,
                                      0))

                                    def OnAccel_FocusPaste():
                                        Win_FocusOnPaste()



                                    def OnAccel_FocusCut():
                                        Win_FocusOnCut()



                                    def OnAccel_FocusCopy():
                                        Win_FocusOnCopy()









        class createkinhintDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            darkBG = 1
            visible = 0
            rect = (200,
             100,
             368,
             326)
            bkimage = 'object/ui/guideBar/kin/dlg_createHint.img'

            def OnEscape():
                doUI((uiKinCreateHintDlg + '.cancel'), 'OnClick')



            def OnEnter():
                doUI((uiKinCreateHintDlg + '.confirm'), 'OnClick')


            class children:
                __module__ = __name__
                class confirm(TButton):
                    __module__ = __name__
                    rect = (110,
                     280,
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
                        Win_ShowWidget(uiKinCreateHintDlg, 0)
                        ui_setCapture(uiKinCreateDlg)
                        Win_SetText((uiKinCreateDlg + '.kinName'), '')
                        Win_SetText((uiKinCreateDlg + '.text'), '')
                        Win_SetCheck((uiKinCreateDlg + '.dianxin'), 1)
                        Win_SetFocus((uiKinCreateDlg + '.kinName'))
                        PlaySound(soundLeave, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (220,
                     280,
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
                        Win_ShowWidget(uiKinCreateHintDlg, 0)
                        doUI((uiSocialityDlg + '.crossBtn'), 'OnClick')
                        PlaySound(soundLeave, 1)





        class createkinDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            darkBG = 1
            visible = 0
            rect = (200,
             100,
             327,
             378)
            bkimage = 'object/ui/guideBar/kin/dlg_createKin.img'

            def OnEscape():
                doUI((uiKinCreateDlg + '.cancel'), 'OnClick')



            def OnEnter():
                doUI((uiKinCreateDlg + '.confirm'), 'OnClick')


            class children:
                __module__ = __name__
                class confirm(TButton):
                    __module__ = __name__
                    rect = (100,
                     330,
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
                        text = Win_GetText((uiKinCreateDlg + '.text'))
                        text = filterChatMsg(text)
                        text = text.replace('\n', ' ')
                        name = Win_GetText((uiKinCreateDlg + '.kinName'))
                        name = filterChatMsg(name)
                        name = name.replace('\n', '')
                        name = name.replace(' ', '')
                        if Win_IsChecked((uiKinCreateDlg + '.dianxin')):
                            kinSection = 1
                        else:
                            kinSection = 2
                        strlen = len(text)
                        DoKinTask(name, text, strlen, kinSection, 0)
                        Win_ShowWidget(uiKinCreateDlg, 0)
                        PlaySound(soundLeave, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (180,
                     330,
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
                        Win_ShowWidget(uiKinCreateDlg, 0)
                        doUI((uiSocialityDlg + '.crossBtn'), 'OnClick')
                        PlaySound(soundLeave, 1)



                class dianxin(TRadio):
                    __module__ = __name__
                    rect = (108,
                     285,
                     60,
                     20)
                    bkimage = 'object/ui/common/btn_check.img'
                    framescheme = [(-1,
                      -1,
                      -1,
                      -1,
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
                      0,
                      0)]
                    bkimagepos = (0,
                     5)
                    groupstop = 1

                class wangtong(dianxin):
                    __module__ = __name__
                    rect = (169,
                     285,
                     60,
                     20)
                    bkimage = 'object/ui/common/btn_check.img'
                    framescheme = [(-1,
                      -1,
                      -1,
                      -1,
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
                      0,
                      0)]
                    bkimagepos = (0,
                     5)
                    groupstop = 2

                class kinName(TRichEdit):
                    __module__ = __name__
                    initlayer = 10000
                    maxchar = 14
                    rect = (100,
                     80,
                     122,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    caption = 'abcd'

                    def OnTab():
                        Win_SetFocus((uiKinCreateDlg + '.text'))



                class text:
                    __module__ = __name__
                    type = 'MULTIEDIT'
                    maxchar = 160
                    rect = (40,
                     155,
                     240,
                     80)
                    drawcolor = zoneChooseColor
                    bkcolor = (0,
                     0,
                     0,
                     0)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    textsize = 12
                    rowspace = 4
                    editable = 1
                    returnflag = 1
                    maxline = 4
                    richmode = 0
                    caption = 'abcd'
                    accel = (('OnAccel_FocusPaste',
                      86,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCut',
                      88,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCopy',
                      67,
                      17,
                      0,
                      0))

                    def OnAccel_FocusPaste():
                        Win_FocusOnPaste()



                    def OnAccel_FocusCut():
                        Win_FocusOnCut()



                    def OnAccel_FocusCopy():
                        Win_FocusOnCopy()



                    def OnTab():
                        Win_SetFocus((uiKinCreateDlg + '.kinName'))





        class topkinDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            darkBG = 1
            visible = 0
            rect = (200,
             50,
             384,
             450)
            bkimage = 'object/ui/guideBar/kin/dlg_topkin.img'

            def OnEscape():
                doUI((uitopKinDlg + '.closeBtn'), 'OnClick')



            def OnEnter():
                doUI((uitopKinDlg + '.closeBtn'), 'OnClick')


            class children:
                __module__ = __name__
                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (360,
                     31,
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
                        Win_ShowWidget(uitopKinDlg, 0)
                        PlaySound(soundLeave, 1)



                class telecomBtn(TTabWin):
                    __module__ = __name__
                    groupid = 5
                    groupstop = 1
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (15,
                     0,
                     64,
                     28)
                    hotcover = 'object/ui/guideBar/kin/btn_telecom.img'

                    def OnClick(this):
                        global chinatelecom
                        chinatelecom = 1
                        ui_updateTopkinList()
                        PlaySound(soundUI, 1)



                class unicomBtn(TTabWin):
                    __module__ = __name__
                    groupid = 5
                    groupstop = 2
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (80,
                     0,
                     64,
                     28)
                    hotcover = 'object/ui/guideBar/kin/btn_netcom.img'

                    def OnClick(this):
                        global chinatelecom
                        chinatelecom = 0
                        ui_updateTopkinList()
                        PlaySound(soundUI, 1)



                class honorBtn(TTabWin):
                    __module__ = __name__
                    groupid = 6
                    groupstop = 1
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (15,
                     33,
                     63,
                     34)
                    hotcover = 'object/ui/guideBar/kin/btn_honor.img'

                    def OnClick(this):
                        global setreputation
                        setreputation = 1
                        Win_ShowWidget((uitopKinDlg + '.activity'), 0)
                        ui_updateTopkinList()
                        PlaySound(soundUI, 1)



                class activityBtn(TTabWin):
                    __module__ = __name__
                    groupid = 6
                    groupstop = 2
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (81,
                     33,
                     63,
                     34)
                    hotcover = 'object/ui/guideBar/kin/btn_activity.img'

                    def OnClick(this):
                        global setreputation
                        setreputation = 0
                        Win_ShowWidget((uitopKinDlg + '.activity'), 1)
                        ui_updateTopkinList()
                        PlaySound(soundUI, 1)



                class activity(TLabel):
                    __module__ = __name__
                    rect = (160,
                     67,
                     43,
                     24)
                    bkimage = 'object/ui/guideBar/kin/img_activity.img'

                class topkin0(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      -1,
                      -1,
                      -1,
                      -1)]
                    bkimage = 'object/ui/guideBar/btn_player.img'
                    bkimagepos = (0,
                     -4)
                    rect = (24,
                     106,
                     314,
                     24)

                    def OnClick(this):
                        global lookupKinID
                        global ActivetopkinPos
                        idx = getTailNum(this)
                        ActivetopkinPos = (TopkinCurrentPos + idx)
                        info = TopkinList().at(ActivetopkinPos)
                        lookupKinID = info.kinindex
                        doUI((uiPlayerInfoDlg + '.lookup'), 'OnClick')
                        PlaySound(soundUI, 1)


                    class children:
                        __module__ = __name__
                        class kinName(TLabel,
                         Static):
                            __module__ = __name__
                            textstyle = (dt_center + dt_vcenter)
                            rect = (2,
                             0,
                             86,
                             24)
                            drawcolor = normalNameColor
                            textEdgeType = 0
                            textEdgeColor = maskColor

                        class value(TLabel,
                         Static):
                            __module__ = __name__
                            textstyle = (dt_center + dt_vcenter)
                            rect = (135,
                             0,
                             60,
                             24)
                            drawcolor = normalNameColor
                            textEdgeType = 0
                            textEdgeColor = maskColor

                        class Order(TLabel,
                         Static):
                            __module__ = __name__
                            textstyle = (dt_center + dt_vcenter)
                            rect = (240,
                             0,
                             40,
                             24)
                            drawcolor = normalNameColor
                            textEdgeType = 0
                            textEdgeColor = maskColor

                        class isAscend(TStatic):
                            __module__ = __name__
                            rect = (280,
                             4,
                             20,
                             20)



                class topkin1(topkin0):
                    __module__ = __name__
                    rect = (24,
                     (106 + 24),
                     314,
                     24)

                class topkin2(topkin0):
                    __module__ = __name__
                    rect = (24,
                     (106 + (2 * 24)),
                     314,
                     24)

                class topkin3(topkin0):
                    __module__ = __name__
                    rect = (24,
                     (106 + (3 * 24)),
                     314,
                     24)

                class topkin4(topkin0):
                    __module__ = __name__
                    rect = (24,
                     (106 + (4 * 24)),
                     314,
                     24)

                class topkin5(topkin0):
                    __module__ = __name__
                    rect = (24,
                     (106 + (5 * 24)),
                     314,
                     24)

                class topkin6(topkin0):
                    __module__ = __name__
                    rect = (24,
                     (106 + (6 * 24)),
                     314,
                     24)

                class topkin7(topkin0):
                    __module__ = __name__
                    bkimage = ''
                    rect = (24,
                     (109 + (7 * 24)),
                     314,
                     27)

                    def OnClick(this):
                        global lookupKinID
                        kinobject = fetch_topkininfolist(chinatelecom, setreputation, 10)
                        lookupKinID = kinobject.m_dwKinIndex
                        doUI((uiPlayerInfoDlg + '.lookup'), 'OnClick')
                        PlaySound(soundUI, 1)



                class topkin8(topkin7):
                    __module__ = __name__
                    bkimage = ''
                    rect = (24,
                     (110 + (8 * 24)),
                     314,
                     27)

                    def OnClick(this):
                        global lookupKinID
                        kinobject = fetch_topkininfolist(chinatelecom, setreputation, 11)
                        lookupKinID = kinobject.m_dwKinIndex
                        doUI((uiPlayerInfoDlg + '.lookup'), 'OnClick')
                        PlaySound(soundUI, 1)



                class scroll(TVScroll):
                    __module__ = __name__
                    rect = (352,
                     96,
                     26,
                     216)
                    pos = 0

                    def OnPosChange():
                        global TopkinCnt
                        global TopkinCurrentPos
                        TopkinCnt = TopkinList().getCnt()
                        ShowCnt = TopkinList().getCnt()
                        ui = uitopKinDlg
                        Win_SetRange((ui + '.scroll'), max((ShowCnt - defTopkinDlgCnt), 0))
                        pos = Win_GetPos((ui + '.scroll'))
                        if ((pos != TopkinCurrentPos) and PlaySound(soundUI, 1)):
                            TopkinCurrentPos = pos
                            for i in range(defTopkinDlgCnt):
                                ui = (uitopKinDlg + ('.topkin%d' % i))
                                Win_SetText((ui + '.kinName'), '')
                                Win_SetText((ui + '.value'), '')
                                Win_SetText((ui + '.Order'), '')
                                idx = (TopkinCurrentPos + i)
                                if ((idx >= ShowCnt) and Win_SetText((ui + '.kinName'), '')):
                                    Win_SetText((ui + '.value'), '')
                                    Win_SetText((ui + '.Order'), '')
                                    Win_SetImg((ui + '.isAscend'), '')
                                    Win_EnableWidget(ui, 0)
                                    continue
                                Win_SetCheck(ui, (idx == ActivetopkinPos))



                    class children:
                        __module__ = __name__
                        class blockbtn(TScrollBtn):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              1,
                              1,
                              0,
                              0,
                              0,
                              0)]
                            rect = (0,
                             0,
                             26,
                             41)
                            bkimage = 'object/ui/common/scl_block.img'





        class kinInfoDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             393,
             361)
            bkimage = 'object/ui/guideBar/kin/dlg_kinInfo.img'
            class children:
                __module__ = __name__
                class kinname(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (110,
                     60,
                     160,
                     12)
                    drawcolor = normalNameColor
                    ttextEdgeColor = (0,
                     49,
                     174,
                     255)
                    textstyle = dt_center

                class kinSection(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (150,
                     90,
                     211,
                     12)
                    drawcolor = maskColor
                    textEdgeType = -1

                class governor(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (150,
                     (90 + 24),
                     211,
                     12)
                    drawcolor = maskColor
                    textEdgeType = -1

                class Size(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (150,
                     (90 + (2 * 24)),
                     211,
                     12)
                    drawcolor = maskColor
                    textEdgeType = -1

                class Grade(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (150,
                     (90 + (3 * 24)),
                     211,
                     12)
                    drawcolor = maskColor
                    textEdgeType = -1

                class Credit(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (150,
                     (90 + (4 * 24)),
                     211,
                     12)
                    drawcolor = maskColor
                    textEdgeType = -1

                class MemberCount(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (150,
                     (90 + (5 * 24)),
                     211,
                     12)
                    drawcolor = maskColor
                    textEdgeType = -1

                class Proclaim(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (150,
                     (90 + (6 * 24)),
                     211,
                     32)
                    textstyle = (dt_left + dt_top)
                    drawcolor = maskColor
                    textEdgeType = -1
                    rowspace = 7

                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (362,
                     7,
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
                        Win_ShowWidget(uiKinInfoDlg, False)
                        Win_ShowWidget(uiPlayerInfoDlg, False)
                        PlaySound(soundLeave, 1)





        class marriageInfoDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             364,
             385)
            bkimage = 'object/ui/marriage/dlg_marriageInfo.img'
            class children:
                __module__ = __name__
                class spouseName(TLabel):
                    __module__ = __name__
                    rect = (83,
                     70,
                     128,
                     12)
                    caption = ''
                    drawcolor = normalNameColor
                    ttextEdgeColor = (0,
                     49,
                     174,
                     255)
                    textstyle = dt_center

                class marriageAge(TLabel):
                    __module__ = __name__
                    rect = (83,
                     (68 + 24),
                     128,
                     12)
                    caption = '0'
                    drawcolor = maskColor
                    textEdgeType = -1
                    textstyle = dt_center

                class marriageLevel(TStatic):
                    __module__ = __name__
                    rect = (89,
                     (68 + 42),
                     125,
                     30)
                    drawcolor = maskColor
                    textEdgeType = -1
                    class children:
                        __module__ = __name__
                        class level1(TStatic):
                            __module__ = __name__
                            visible = 1
                            rect = (0,
                             0,
                             20,
                             24)

                        class level2(level1):
                            __module__ = __name__
                            rect = ((0 + 24),
                             0,
                             20,
                             24)

                        class level3(level1):
                            __module__ = __name__
                            rect = ((0 + (24 * 2)),
                             0,
                             20,
                             24)

                        class level4(level1):
                            __module__ = __name__
                            rect = ((0 + (24 * 3)),
                             0,
                             20,
                             24)

                        class level5(level1):
                            __module__ = __name__
                            rect = ((0 + (24 * 4)),
                             0,
                             20,
                             24)



                class closeLine(TButton):
                    __module__ = __name__
                    rect = (83,
                     (68 + 66),
                     125,
                     17)
                    bkimage = 'object/ui/marriage/dlg_closeLine.img'

                    def OnMouseMoveIn():
                        print 'mousemovein!'
                        Win_ShowWidget((uiMarriageDlg + '.closeLineValue'), 1)



                    def OnMouseMoveOut():
                        print 'mousemoveout!'
                        Win_ShowWidget((uiMarriageDlg + '.closeLineValue'), 0)



                class closeLineValue(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (87,
                     (68 + 36),
                     128,
                     35)
                    bkimage = 'object/ui/marriage/dlg_closeLineValue.img'
                    class children:
                        __module__ = __name__
                        class value(TLabel):
                            __module__ = __name__
                            rect = (10,
                             0,
                             128,
                             25)
                            caption = ''
                            drawcolor = maskColor
                            textEdgeType = -1
                            textstyle = dt_center



                class closeNum(TLabel):
                    __module__ = __name__
                    rect = (83,
                     (68 + 92),
                     128,
                     12)
                    caption = ''
                    drawcolor = maskColor
                    textEdgeType = -1
                    textstyle = dt_center

                class loveword(TLabel,
                 Static):
                    __module__ = __name__
                    rowspace = 2
                    caption = ''
                    rect = (41,
                     (68 + 165),
                     295,
                     95)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1

                class modify(TButton):
                    __module__ = __name__
                    rect = (180,
                     187,
                     37,
                     20)
                    bkimage = 'object/ui/marriage/btn_modify.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        ui_setCapture(uiModifyLoveWordDlg)
                        PlaySound(soundUI, 1)



                class divorce(TButton):
                    __module__ = __name__
                    rect = (83,
                     348,
                     65,
                     25)
                    bkimage = 'object/ui/marriage/btn_divorce.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiMarriageDlg, 0)
                        ui_setCapture(uiDivorceDlg)
                        PlaySound(soundUI, 1)



                class close(TButton):
                    __module__ = __name__
                    rect = (235,
                     348,
                     65,
                     25)
                    bkimage = 'object/ui/marriage/btn_close.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiMarriageDlg, 0)
                        PlaySound(soundLeave, 1)



                class ring(TStatic):
                    __module__ = __name__
                    rect = (231,
                     61,
                     20,
                     19)
                    framescheme = [(0,
                      13,
                      0,
                      13,
                      0,
                      13,
                      0,
                      13)]

                class noRing(TButton):
                    __module__ = __name__
                    initlayer = -99999
                    rect = (238,
                     63,
                     99,
                     99)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/marriage/btn_noRing.img'

                    def OnClick(this):
                        Win_ShowWidget(uiMarriageDlg, 0)
                        doUI('UI.selRoom.shopBtn', 'OnClick')
                        PlaySound(soundUI, 1)





        class modifyLoveWordDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             393,
             361)
            bkimage = 'object/ui/marriage/dlg_loveWord.img'
            class children:
                __module__ = __name__
                class loveword:
                    __module__ = __name__
                    type = 'MULTIEDIT'
                    maxchar = 198
                    rect = (42,
                     110,
                     235,
                     80)
                    caption = 'for ever\xa1\xad\xa1\xad'
                    drawcolor = zoneChooseColor
                    bkcolor = (0,
                     0,
                     0,
                     0)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    textsize = 12
                    rowspace = 4
                    editable = 1
                    returnflag = 1
                    maxline = 5
                    richmode = 0
                    accel = (('OnAccel_FocusPaste',
                      86,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCut',
                      88,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCopy',
                      67,
                      17,
                      0,
                      0))

                    def OnAccel_FocusPaste():
                        Win_FocusOnPaste()



                    def OnAccel_FocusCut():
                        Win_FocusOnCut()



                    def OnAccel_FocusCopy():
                        Win_FocusOnCopy()



                class save(TButton):
                    __module__ = __name__
                    rect = (85,
                     280,
                     65,
                     31)
                    bkimage = 'object/ui/marriage/btn_save.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        txt = Win_GetText((uiModifyLoveWordDlg + '.loveword'))
                        SaveLoveWord(len(txt), txt)
                        Win_ShowWidget(uiModifyLoveWordDlg, 0)
                        PlaySound(soundUI, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (225,
                     280,
                     65,
                     31)
                    bkimage = 'object/ui/marriage/btn_divorceCancel.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiModifyLoveWordDlg, 0)
                        PlaySound(soundLeave, 1)





        class sparkDlg(TStatic):
            __module__ = __name__
            initlayer = 99999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             393,
             361)
            bkimage = 'object/ui/marriage/dlg_spark.img'
            class children:
                __module__ = __name__
                class spouseName(TLabel):
                    __module__ = __name__
                    rect = (115,
                     65,
                     105,
                     20)
                    drawcolor = normalNameColor
                    ttextEdgeColor = (0,
                     49,
                     174,
                     255)
                    textstyle = dt_center

                class sparkword:
                    __module__ = __name__
                    type = 'MULTIEDIT'
                    maxchar = 198
                    rect = (45,
                     140,
                     270,
                     70)
                    drawcolor = zoneChooseColor
                    bkcolor = (0,
                     0,
                     0,
                     0)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    textsize = 12
                    rowspace = 4
                    editable = 1
                    returnflag = 1
                    maxline = 5
                    richmode = 0
                    accel = (('OnAccel_FocusPaste',
                      86,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCut',
                      88,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCopy',
                      67,
                      17,
                      0,
                      0))

                    def OnAccel_FocusPaste():
                        Win_FocusOnPaste()



                    def OnAccel_FocusCut():
                        Win_FocusOnCut()



                    def OnAccel_FocusCopy():
                        Win_FocusOnCopy()



                class send(TButton):
                    __module__ = __name__
                    rect = (70,
                     280,
                     65,
                     25)
                    bkimage = 'object/ui/marriage/btn_sparkSend.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        txt = Win_GetText((uiSparkDlg + '.sparkword'))
                        Win_ShowWidget(uiSparkDlg, 0)
                        Spark(len(txt), txt, beSparkedUin)
                        PlaySound(soundUI, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (220,
                     280,
                     65,
                     25)
                    bkimage = 'object/ui/marriage/btn_sparkCancel.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiSparkDlg, 0)
                        PlaySound(soundLeave, 1)





        class weddingOverDlg(TStatic):
            __module__ = __name__
            initlayer = 99999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             327,
             378)
            bkimage = 'object/ui/marriage/dlg_weddingSuccess.img'
            class children:
                __module__ = __name__
                class congratulations:
                    __module__ = __name__
                    type = 'MULTIEDIT'
                    maxchar = 198
                    rect = (40,
                     90,
                     240,
                     170)
                    drawcolor = zoneChooseColor
                    bkcolor = (0,
                     0,
                     0,
                     0)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    textsize = 12
                    rowspace = 4
                    editable = 1
                    returnflag = 1
                    maxline = 5
                    richmode = 0
                    accel = (('OnAccel_FocusPaste',
                      86,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCut',
                      88,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCopy',
                      67,
                      17,
                      0,
                      0))

                    def OnAccel_FocusPaste():
                        Win_FocusOnPaste()



                    def OnAccel_FocusCut():
                        Win_FocusOnCut()



                    def OnAccel_FocusCopy():
                        Win_FocusOnCopy()



                class confirm(TButton):
                    __module__ = __name__
                    rect = (126,
                     323,
                     53,
                     32)
                    bkimage = 'object/ui/marriage/btn_divorceConfirm.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiWeddingOverDlg, 0)
                        SetWeddingEffect(weddingEffectFile)





        class marriageConfirmDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             393,
             361)
            bkimage = 'object/ui/marriage/dlg_marriageConfirm.img'
            class children:
                __module__ = __name__
                class marriageWord(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (44,
                     85,
                     215,
                     105)
                    rowspace = 2
                    caption = '\xbc\xde\xb8\xf8\xce\xd2\xb0\xc9'
                    drawcolor = darkColor
                    textEdgeType = -1

                class accept(TButton):
                    __module__ = __name__
                    rect = (75,
                     250,
                     65,
                     31)
                    bkimage = 'object/ui/marriage/btn_Iaccept.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        print 'sparkUin:',
                        print sparkUin,
                        print '   uin:',
                        print uin,
                        print '  beSparkedUin:',
                        print beSparkedUin
                        if ((uin == sparkUin) and AnswerWedding(0, beSparkedUin)):
                            pass
                        Win_ShowWidget(uiMarriageConfirmDlg, 0)
                        PlaySound(soundUI, 1)



                class reject(TButton):
                    __module__ = __name__
                    rect = (290,
                     250,
                     65,
                     31)
                    bkimage = 'object/ui/marriage/btn_Ireject.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        if ((uin == sparkUin) and AnswerWedding(1, beSparkedUin)):
                            pass
                        Win_ShowWidget(uiMarriageConfirmDlg, 0)
                        PlaySound(soundLeave, 1)





        class divorceDlg(TStatic):
            __module__ = __name__
            initlayer = 99999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             393,
             361)
            bkimage = 'object/ui/marriage/dlg_divorce.img'
            class children:
                __module__ = __name__
                class confirm(TButton):
                    __module__ = __name__
                    rect = (70,
                     203,
                     65,
                     25)
                    bkimage = 'object/ui/marriage/btn_divorceConfirm.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiDivorceDlg, 0)
                        Divorce()
                        PlaySound(soundUI, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (220,
                     203,
                     65,
                     25)
                    bkimage = 'object/ui/marriage/btn_divorceCancel.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiDivorceDlg, 0)
                        PlaySound(soundLeave, 1)





        class receiveSparkDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 393) / 2),
             ((600 - 361) / 2),
             393,
             361)
            bkimage = 'object/ui/marriage/dlg_receiveSpark.img'
            class children:
                __module__ = __name__
                class sparkword(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (40,
                     130,
                     235,
                     110)
                    rowspace = 2
                    caption = '\xbc\xde\xb8\xf8\xce\xd2\xb0\xc9'
                    drawcolor = zoneChooseColor
                    textEdgeType = -1

                class accept(TButton):
                    __module__ = __name__
                    rect = (53,
                     325,
                     65,
                     31)
                    bkimage = 'object/ui/marriage/btn_Iaccept.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        AnswerSpark(0, sparkUin)
                        Win_ShowWidget(uiReceiveSparkDlg, 0)
                        PlaySound(soundUI, 1)



                class reject(TButton):
                    __module__ = __name__
                    rect = (190,
                     325,
                     65,
                     31)
                    bkimage = 'object/ui/marriage/btn_Ireject.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        AnswerSpark(1, sparkUin)
                        Win_ShowWidget(uiReceiveSparkDlg, 0)
                        PlaySound(soundLeave, 1)





        class kinInviteDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (200,
             100,
             393,
             361)
            bkimage = 'object/ui/guideBar/kin/dlg_kinInvite.img'
            class children:
                __module__ = __name__
                class name(TLabel):
                    __module__ = __name__
                    rect = (45,
                     63,
                     175,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = dt_center

                class cross(TButton):
                    __module__ = __name__
                    rect = (362,
                     8,
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
                        Win_ShowWidget(uiKinInviteDlg, 0)
                        PlaySound(soundUI, 1)



                class confirm(TButton):
                    __module__ = __name__
                    rect = (120,
                     309,
                     63,
                     31)
                    bkimage = 'object/ui/common/btn_agree.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiKinInviteDlg, 0)
                        DoKinTask('', 'Y', 1, 0, 11)
                        PlaySound(soundUI, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (210,
                     309,
                     63,
                     31)
                    bkimage = 'object/ui/common/btn_refuse.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiKinInviteDlg, 0)
                        DoKinTask('', 'N', 1, 0, 11)
                        PlaySound(soundUI, 1)



                class kininfo_status(TLabel):
                    __module__ = __name__
                    rect = (150,
                     90,
                     180,
                     12)
                    textstyle = (dt_left + dt_vcenter)
                    drawcolor = maskColor
                    textEdgeType = -1

                class kininfo_governor(kininfo_status):
                    __module__ = __name__
                    rect = (150,
                     (90 + 24),
                     180,
                     12)

                class kininfo_size(kininfo_status):
                    __module__ = __name__
                    rect = (150,
                     (90 + (24 * 2)),
                     180,
                     12)

                class kininfo_grade(kininfo_status):
                    __module__ = __name__
                    rect = (150,
                     (90 + (24 * 3)),
                     180,
                     12)

                class kininfo_honor(kininfo_status):
                    __module__ = __name__
                    rect = (150,
                     (90 + (24 * 4)),
                     180,
                     12)

                class kininfo_MemberCount(kininfo_status):
                    __module__ = __name__
                    rect = (150,
                     (90 + (24 * 5)),
                     180,
                     12)

                class kininfo_enounce(kininfo_status):
                    __module__ = __name__
                    rect = (150,
                     (90 + (24 * 6)),
                     180,
                     32)
                    textstyle = (dt_left + dt_top)
                    rowspace = 7



        class kinTipDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 368) / 2),
             ((600 - 326) / 2),
             368,
             326)
            bkimage = 'object/ui/common/dlg_msgBox.img'
            class children:
                __module__ = __name__
                class confirm(TButton):
                    __module__ = __name__
                    rect = (100,
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
                        pPar1 = Win_GetText((uiKinTipDlg + '.pParam1'))
                        pPar2 = Win_GetText((uiKinTipDlg + '.pParam2'))
                        Uin = int(Win_GetText((uiKinTipDlg + '.uin')))
                        iMode = int(Win_GetText((uiKinTipDlg + '.TaskMode')))
                        DoKinTask(pPar1, pPar2, len(pPar2), Uin, iMode)
                        Win_ShowWidget(uiKinTipDlg, 0)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (225,
                     280,
                     65,
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
                        Win_ShowWidget(uiKinTipDlg, 0)



                class prompt(TLabel):
                    __module__ = __name__
                    rect = (42,
                     84,
                     280,
                     130)
                    textEdgeType = -1
                    drawcolor = zoneChooseColor

                class pParam1(TLabel):
                    __module__ = __name__
                    visible = 0

                class pParam2(TLabel):
                    __module__ = __name__
                    visible = 0

                class uin(TLabel):
                    __module__ = __name__
                    visible = 0

                class TaskMode(TLabel):
                    __module__ = __name__
                    visible = 0



        class requestMakeFriendsDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 368) / 2),
             ((600 - 326) / 2),
             368,
             326)
            bkimage = 'object/ui/guideBar/friend/dlg_addFriends.img'
            class children:
                __module__ = __name__
                class name(TButton):
                    __module__ = __name__
                    rect = (122,
                     76,
                     120,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor
                    textstyle = dt_left

                    def OnClick(this):
                        go2playerInfo(friendUin)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (196,
                     280,
                     66,
                     27)
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
                        Win_ShowWidget(uiAddFriendDlg, 0)



                class confirm(TButton):
                    __module__ = __name__
                    rect = (120,
                     280,
                     66,
                     27)
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
                        txt = Win_GetText((uiAddFriendDlg + '.text'))
                        txt = filterChatMsg(txt)
                        placeholder = ('%c' % 7)
                        txt = txt.replace('\n', placeholder)
                        strlen = len(txt)
                        DoFriendTask(txt, strlen, friendUin, 1)
                        Win_ShowWidget(uiAddFriendDlg, 0)



                class text:
                    __module__ = __name__
                    type = 'MULTIEDIT'
                    maxchar = 50
                    rect = (42,
                     136,
                     280,
                     76)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor
                    textsize = 12
                    rowspace = 4
                    editable = 1
                    returnflag = 1
                    maxline = 3
                    richmode = 0
                    accel = (('OnAccel_FocusPaste',
                      86,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCut',
                      88,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCopy',
                      67,
                      17,
                      0,
                      0))

                    def OnAccel_FocusPaste():
                        Win_FocusOnPaste()



                    def OnAccel_FocusCut():
                        Win_FocusOnCut()



                    def OnAccel_FocusCopy():
                        Win_FocusOnCopy()





        class friendDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 368) / 2),
             ((600 - 326) / 2),
             368,
             326)
            bkimage = 'object/ui/guideBar/friend/dlg_beAddedFriends.img'
            class children:
                __module__ = __name__
                class name(TButton):
                    __module__ = __name__
                    rect = (122,
                     76,
                     120,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor
                    textstyle = dt_left

                    def OnClick(this):
                        print 'Click response on name'
                        go2playerInfo(beAddUin)



                class refuse(TButton):
                    __module__ = __name__
                    rect = (196,
                     280,
                     66,
                     27)
                    bkimage = 'object/ui/common/btn_refuse.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiBeAddedFriendDlg, 0)
                        DoFriendTask('n', 0, beAddUin, 6)



                class confirm(TButton):
                    __module__ = __name__
                    rect = (120,
                     280,
                     66,
                     27)
                    bkimage = 'object/ui/common/btn_agree.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget(uiBeAddedFriendDlg, 0)
                        if Win_IsChecked((uiBeAddedFriendDlg + '.addFriend')):
                            txt = Win_GetText((uiBeAddedFriendDlg + '.text'))
                            txt = filterChatMsg(txt)
                            strlen = len(txt)
                            DoFriendTask(txt, strlen, beAddUin, 1)
                        DoFriendTask('y', 0, beAddUin, 6)



                class addFriend(TCheck):
                    __module__ = __name__
                    framescheme = [(-1,
                      -1,
                      -1,
                      -1,
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
                      0,
                      0)]
                    rect = (32,
                     212,
                     120,
                     16)
                    bkimagepos = (0,
                     5)
                    bkimage = 'object/ui/common/btn_check.img'

                    def OnClick(this):
                        PlaySound(soundUI, 1)



                class text:
                    __module__ = __name__
                    type = 'MULTIEDIT'
                    maxchar = 50
                    rect = (42,
                     136,
                     280,
                     60)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor
                    textsize = 12
                    rowspace = 4
                    editable = 1
                    returnflag = 1
                    maxline = 3
                    richmode = 0
                    accel = (('OnAccel_FocusPaste',
                      86,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCut',
                      88,
                      17,
                      0,
                      0),
                     ('OnAccel_FocusCopy',
                      67,
                      17,
                      0,
                      0))

                    def OnAccel_FocusPaste():
                        Win_FocusOnPaste()



                    def OnAccel_FocusCut():
                        Win_FocusOnCut()



                    def OnAccel_FocusCopy():
                        Win_FocusOnCopy()





        class joinMemberWeb(TDlg):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 365) / 2),
             ((600 - 290) / 2),
             368,
             326)
            bkimage = 'object/ui/common/dlg_msgBox.img'
            bkimagepos = (-5,
             -19)
            darkBG = 1
            class children:
                __module__ = __name__
                class crossBtn(TButton):
                    __module__ = __name__
                    rect = (160,
                     260,
                     43,
                     31)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/common/btn_close.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget('UI.joinMemberWeb', 0)
                        sc_HideWeb('joinmember')
                        PlaySound(soundLeave, 1)
                        if ((1 == exitFlag) and OnMsgBoxResult(((2 << 24) + 1), 1)):
                            pass





        class playerMenu(TWidget):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            style = wgtstyle_popup
            rect = (110,
             110,
             67,
             108)
            bkimage = 'object/ui/guideBar/dlg_playermenu.img'
            class children:
                __module__ = __name__
                class messageBtn(TButton):
                    __module__ = __name__
                    rect = (0,
                     2,
                     67,
                     14)
                    bkimage = 'object/ui/guideBar/btn_playermenuChoose.img'
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      -1,
                      -1,
                      -1,
                      -1)]
                    caption = '\xb7\xa2\xcb\xcd\xc3\xdc\xd3\xef'
                    drawcolor = lightColor
                    textEdgeType = -1

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        NotifyWisper(friendName, friendUin)



                class traceBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     17,
                     67,
                     14)
                    caption = '\xba\xc3\xd3\xd1\xd7\xb7\xd7\xd9'

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        DoFriendTask('', 0, friendUin, 3)



                class addBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     35,
                     67,
                     14)
                    caption = '\xcc\xed\xbc\xd3\xba\xc3\xd3\xd1'

                    def OnClick(this):
                        NickName = GetPlayerNickNamebyUin(friendUin, 0)
                        NickName = NickName.replace('\n', '')
                        Win_ShowWidget(uiPlayerMenu, 0)
                        Win_SetText((uiAddFriendDlg + '.text'), '')
                        Win_SetFocus((uiAddFriendDlg + '.text'))
                        Win_SetText((uiAddFriendDlg + '.name'), NickName)
                        ui_setCapture(uiAddFriendDlg)



                class deleteBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     35,
                     67,
                     14)
                    caption = '\xc9\xbe\xb3\xfd\xba\xc3\xd3\xd1'

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        DoFriendTask('', 0, friendUin, 2)



                class infoBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     53,
                     67,
                     14)
                    caption = '\xb2\xe9\xbf\xb4\xd7\xca\xc1\xcf'

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        go2playerInfo(friendUin)



                class shieldBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     71,
                     67,
                     14)
                    caption = '\xc6\xc1\xb1\xce\xcd\xe6\xbc\xd2'

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        DoFriendTask('', 0, friendUin, 5)



                class unshieldBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     71,
                     67,
                     14)
                    caption = '\xc8\xa1\xcf\xfb\xc6\xc1\xb1\xce'

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        DoFriendTask('', 0, friendUin, 7)



                class kininviteBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     89,
                     67,
                     14)
                    caption = '\xbc\xd2\xd7\xe5\xd1\xfb\xc7\xeb'

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        DoKinTask('', '', 0, friendUin, 4)



                class C2CInviteBtn(messageBtn):
                    __module__ = __name__
                    rect = (0,
                     106,
                     67,
                     14)
                    caption = '\xd3\xeb\xcb\xfb\xbd\xbb\xd2\xd7'

                    def OnClick(this):
                        Win_ShowWidget(uiPlayerMenu, 0)
                        NotifyWisper(friendName, friendUin)
                        SectionChat(0, ('/c2c ' + str(friendUin)))





        class taskSelectDlg(TStatic):
            __module__ = __name__
            initlayer = 99999
            darkBG = 1
            visible = 0
            rect = (200,
             100,
             368,
             326)
            bkimage = 'object/ui/task/dlg_taskSelect.img'
            class children:
                __module__ = __name__
                class taskPractic(TButton):
                    __module__ = __name__
                    rect = (52,
                     132,
                     112,
                     91)
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      -1,
                      -1,
                      -1,
                      -1)]
                    bkimage = 'object/ui/task/btn_greenHand.img'

                    def OnClick(this):
                        print 'select practice task...........'
                        Win_ShowWidget(uiTaskSelDlg, 0)
                        Win_ShowWidget('UI.newPlayerDirectionDlg', 0)
                        PlaySound(soundLeave, 1)
                        DisableEnterRoom()
                        print 'enter practice room'
                        sc_beginTutorial()



                class freePractice(TButton):
                    __module__ = __name__
                    rect = (198,
                     132,
                     112,
                     91)
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      -1,
                      -1,
                      -1,
                      -1)]
                    bkimage = 'object/ui/task/btn_free.img'

                    def OnClick(this):
                        print 'select free practice.............'
                        Win_ShowWidget(uiTaskSelDlg, 0)
                        Win_ShowWidget('UI.newPlayerDirectionDlg', 0)
                        PlaySound(soundLeave, 1)
                        DisableEnterRoom()
                        print 'enter freePractice room'
                        sc_beginFreePractice()



                class cancel(TButton):
                    __module__ = __name__
                    rect = (160,
                     280,
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
                        Win_ShowWidget(uiTaskSelDlg, 0)
                        Win_ShowWidget('UI.newPlayerDirectionDlg', 0)
                        PlaySound(soundLeave, 1)





        class newPlayerDirectionDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (518,
             105,
             280,
             85)
            bkimage = 'object/ui/game/newplayerpopo.img'
            class children:
                __module__ = __name__
                class text(TLabel):
                    __module__ = __name__
                    rect = (58,
                     22,
                     200,
                     50)
                    drawcolor = (51,
                     113,
                     149,
                     255)
                    textEdgeType = -1
                    caption = '\xc4\xfa\xcf\xd6\xd4\xda\xbf\xc9\xd2\xd4\xd6\xd8\xb8\xb4\xd0\xc2\xca\xd6\xc8\xce\xce\xf1\xa3\xac\n\xd2\xb2\xbf\xc9\xd2\xd4\xd1\xa1\xd4\xf1\xbd\xf8\xd0\xd0\xd7\xd4\xd3\xc9\xc1\xb7\xcf\xb0\xa1\xa3\n\xc8\xe7\xb9\xfb\xc4\xfa\xb2\xd9\xd7\xf7\xb6\xbc\xd2\xd1\xca\xec\xc1\xb7\xb5\xc4\xbb\xb0\xa3\xac\n\xb9\xa7\xcf\xb2\xc4\xe3\xbf\xc9\xd2\xd4\xb8\xfa\xc6\xe4\xcb\xfb\xcd\xe6\xbc\xd2PK\xc1\xcb'



        class SetRecorderDlg(TDlg):
            __module__ = __name__
            initlayer = 999999
            darkBG = 1
            visible = 0
            rect = (130,
             60,
             393,
             361)
            bkimage = 'object/ui/guideBar/dlg_record.img'

            def initMe():
                Win_SetText((uiSetRecorderDlg + '.CurrentDirLabel'), os_join(os_getmoduledir(), 'Record'))
                Win_SetPos((uiSetRecorderDlg + '.scroll'), 0)
                doUI((uiSetRecorderDlg + '.scroll'), 'OnPosChange')


            class children:
                __module__ = __name__
                class CurrentDirLabel(TEdit):
                    __module__ = __name__
                    editable = 0
                    maxchar = 200
                    rect = (64,
                     50,
                     245,
                     12)
                    drawcolor = lightColor
                    caption = os_join(os_getmoduledir(), 'Record')
                    class children:
                        __module__ = __name__
                        class icon(TStatic):
                            __module__ = __name__
                            framescheme = [(1,
                              1,
                              1,
                              1,
                              1,
                              1,
                              1,
                              1)]
                            rect = (-26,
                             -3,
                             17,
                             12)
                            bkimage = 'object/ui/record/icon_folder.img'



                class GotoUpButton(TButton):
                    __module__ = __name__
                    rect = (320,
                     44,
                     34,
                     22)
                    bkimage = 'object/ui/guideBar/btn_folderUp.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        curDirname = Win_GetText((uiSetRecorderDlg + '.CurrentDirLabel'))
                        if (curDirname == '\xce\xd2\xb5\xc4\xb5\xe7\xc4\xd4'):
                            print '\xce\xd2\xb5\xc4\xb5\xe7\xc4\xd4'
                            return ''
                        parentDirname = os_dirname(curDirname)
                        print parentDirname
                        print 'not ismount'
                        Win_SetText((uiSetRecorderDlg + '.CurrentDirLabel'), parentDirname)
                        doUI((uiSetRecorderDlg + '.scroll'), 'OnPosChange')



                class OK(TButton):
                    __module__ = __name__
                    rect = (116,
                     370,
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
                        currentDirname = Win_GetText((uiSetRecorderDlg + '.CurrentDirLabel'))
                        print currentDirname
                        print curFile
                        if (curFile == -1):
                            print 'no selected file'
                        else:
                            pos = Win_GetPos((uiSetRecorderDlg + '.scroll'))
                            currFilename = Win_GetText((((uiSetRecorderDlg + '.file') + str((curFile + 1))) + '.name'))
                            print 'isdir',
                            print os_isdir(os_join(currentDirname, currFilename))
                            print currFilename
                            if os_isdir(os_join(currentDirname, currFilename)):
                                print 'dir'
                            else:
                                Win_ShowWidget(uiSetRecorderDlg, False)
                                print 'PlayRecord',
                                print os_join(currentDirname, currFilename)
                                PlayRecord(os_join(currentDirname, currFilename))



                class Cancel(TButton):
                    __module__ = __name__
                    rect = (225,
                     370,
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
                        Win_ShowWidget(uiSetRecorderDlg, False)
                        PlaySound(soundLeave, 1)



                class closeBtn(Cancel):
                    __module__ = __name__
                    rect = (364,
                     5,
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

                class scroll(TVScroll):
                    __module__ = __name__
                    rect = (356,
                     74,
                     26,
                     288)
                    pos = 0
                    visible = 1
                    pagesize = -5

                    def OnPosChange():
                        fileCnt = 0
                        selFileList = []
                        tempFilelist = []
                        tempFilelist1 = []
                        curDirname = Win_GetText((uiSetRecorderDlg + '.CurrentDirLabel'))
                        ui = uiSetRecorderDlg
                        if (curDirname == '\xce\xd2\xb5\xc4\xb5\xe7\xc4\xd4'):
                            selFileList = dr.getDrivers()
                        else:
                            try:
                                tempFilelist = os_listdir(curDirname)
                                print 'step1'
                                for f in tempFilelist:
                                    if (os_isdir(os_join(curDirname, f)) and selFileList.append(f)):
                                        pass
                                    if ((f[-4:].lower() == '.qbv') and tempFilelist1.append(f)):
                                        pass

                                for i in tempFilelist1:
                                    selFileList.append(i)

                            except:
                                print 'Cant open'
                        fileCnt = len(selFileList)
                        pos = Win_GetPos((ui + '.scroll'))
                        print 'pos=',
                        print pos
                        driveList = []
                        isDrive = 0
                        driveList = dr.getDrivers()
                        driveCnt = len(driveList)
                        print 'driveCnt=',
                        print driveCnt
                        for i in range(driveCnt):
                            if (driveList[i] == curDirname):
                                isDrive = 1
                                break

                        if (curDirname == '\xce\xd2\xb5\xc4\xb5\xe7\xc4\xd4'):
                            print 'Computer'
                            Win_SetImg((ui + '.CurrentDirLabel.icon'), 'res/uires/selRoom/recorder/computer_icon.img')
                        elif (isDrive == 1):
                            print 'Mount'
                            Win_SetImg((ui + '.CurrentDirLabel.icon'), 'res/uires/selRoom/recorder/hardrive_icon.img')
                        else:
                            print 'folder'
                            Win_SetImg((ui + '.CurrentDirLabel.icon'), 'object/ui/record/icon_folder.img')
                        Win_SetRange((ui + '.scroll'), (fileCnt - 12))
                        for i in range(12):
                            fileUI = ((ui + '.file') + str((i + 1)))
                            if (((pos + i) < fileCnt) and (curFile == i)):
                                if Win_SetBkColor(fileUI, 24, 24, 192, 127):
                                    pass
                                if ((curDirname == '\xce\xd2\xb5\xc4\xb5\xe7\xc4\xd4') and Win_SetImg((fileUI + '.icon'), 'res/uires/selRoom/recorder/hardrive_icon.img')):
                                    pass
                                Win_SetText((fileUI + '.name'), selFileList[(pos + i)])



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



                class file1(TButton):
                    __module__ = __name__
                    drawflag = drawflag_win_fill
                    rect = (43,
                     74,
                     300,
                     19)

                    def OnClick(this):
                        global curFile
                        curFile = (getMyIdx() - 1)
                        print curFile
                        doUI((uiSetRecorderDlg + '.scroll'), 'OnPosChange')
                        PlaySound(soundUI, 1)



                    def OnDBClick():
                        global curFile
                        print 'OnDBClick'
                        curFile = (getMyIdx() - 1)
                        currDirname = Win_GetText((uiSetRecorderDlg + '.CurrentDirLabel'))
                        currFilename = Win_GetText((((uiSetRecorderDlg + '.file') + str((curFile + 1))) + '.name'))
                        if (os_isdir(os_join(currDirname, currFilename)) and Win_SetText((uiSetRecorderDlg + '.CurrentDirLabel'), os_join(currDirname, currFilename))):
                            pass
                        Win_SetPos((uiSetRecorderDlg + '.scroll'), 0)
                        doUI((uiSetRecorderDlg + '.scroll'), 'OnPosChange')


                    class children:
                        __module__ = __name__
                        class icon(TStatic):
                            __module__ = __name__
                            framescheme = [(1,
                              1,
                              1,
                              1,
                              1,
                              1,
                              1,
                              1)]
                            rect = (0,
                             1,
                             12,
                             18)
                            bkimage = 'object/ui/record/icon_folder.img'

                        class name(TLabel,
                         Static):
                            __module__ = __name__
                            rect = (30,
                             3,
                             240,
                             12)
                            drawcolor = lightColor



                class file2(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + 24),
                     300,
                     19)

                class file3(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 2)),
                     300,
                     19)

                class file4(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 3)),
                     300,
                     19)

                class file5(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 4)),
                     300,
                     19)

                class file6(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 5)),
                     300,
                     19)

                class file7(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 6)),
                     300,
                     19)

                class file8(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 7)),
                     300,
                     19)

                class file9(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 8)),
                     300,
                     19)

                class file10(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 9)),
                     300,
                     19)

                class file11(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 10)),
                     300,
                     19)

                class file12(file1):
                    __module__ = __name__
                    rect = (43,
                     (74 + (24 * 11)),
                     300,
                     19)



        class storageDlg(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            rect = (178,
             196,
             325,
             286)
            bkimage = 'object/ui/storage/dlg_roomStorage.img'

            def OnSelfHide():
                ui = (uiRoomStorageDlg + ('.funcItem%d' % uiStorageIdx))
                Win_SetDragImg(ui, '')


            class children:
                __module__ = __name__
                class storageLeft(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    rect = (10,
                     254,
                     33,
                     36)
                    bkimage = 'object/ui/common/btn_left.img'

                    def OnClick(this):
                        global roomStoragePos
                        roomStoragePos = max((roomStoragePos - defRoomStorageCnt), 0)
                        UpdateRoomStorage()
                        PlaySound(soundUI, 1)



                class storageRight(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    rect = (121,
                     254,
                     33,
                     35)
                    bkimage = 'object/ui/common/btn_right.img'

                    def OnClick(this):
                        global roomStoragePos
                        if ((roomStoragePos + defRoomStorageCnt) >= totalStorageCnt):
                            return 
                        roomStoragePos = (roomStoragePos + defRoomStorageCnt)
                        UpdateRoomStorage()
                        PlaySound(soundUI, 1)



                class storagePage:
                    __module__ = __name__
                    type = 'NUMLABEL'
                    rect = (43,
                     260,
                     80,
                     24)
                    bkimage = 'object/ui/common/number2.img'
                    textstyle = dt_center
                    textsize = 16
                    textwidth = 19
                    textheight = 24

                class storageDescription:
                    __module__ = __name__
                    type = 'DYLABEL'
                    initlayer = 99999
                    rect = (0,
                     0,
                     130,
                     1)
                    captionrect = (4,
                     4,
                     120,
                     1)
                    bkimage = 'object/ui/common/img_tip.img'
                    textEdgeType = -1
                    drawcolor = maskColor

                class funcItem0(TRadio):
                    __module__ = __name__
                    groupid = 3
                    groupstop = 0
                    rect = (5,
                     2,
                     60,
                     60)
                    dragtype = 6
                    bkimage = 'object/ui/storage/img_choose.img'
                    framescheme = [(-1,
                      -1,
                      -1,
                      -1,
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
                      0,
                      0)]
                    tipwidget = (uiRoomStorageDlg + '.storageDescription')

                    def OnDBClick():
                        global curRoomStorageIdx
                        me = getMyIdx2()
                        curRoomStorageIdx = (roomStoragePos + me)
                        EquipOneProp(-1, g_StorageList.at(curRoomStorageIdx).m_stItem.m_nItemID)
                        curEquipIdx = -1
                        curRoomStorageIdx = -1
                        ui_UpdateRoomEquip()



                    def OnBeginItemDrag():
                        global curRoomStorageIdx
                        global uiStorageIdx
                        uiStorageIdx = getMyIdx2()
                        print uiStorageIdx
                        curRoomStorageIdx = (roomStoragePos + uiStorageIdx)
                        info = g_StorageList.at(curRoomStorageIdx).m_stItem
                        path = Win_GetMyPath()
                        Win_SetDragImg(path, ('res/uires/icon/item/item%d.img' % info.m_nItemID))



                    def OnRClick():
                        global curRoomStorageIdx
                        path = Win_GetMyPath()
                        me = getMyIdx2()
                        if (curRoomStorageIdx == (roomStoragePos + me)):
                            curRoomStorageIdx = -1
                            Win_SetCheck(path, 0)



                    def OnMouseMoveIn():
                        me = Win_GetMyPath()
                        idx = (getMyIdx2() + roomStoragePos)
                        if (idx >= totalStorageCnt):
                            return 
                        info = g_StorageList.at(idx)
                        ui = (uiRoomStorageDlg + '.storageDescription')
                        Win_SetText(ui, ((info.m_szName + '\n') + info.m_szDescrip))
                        winrect = Win_GetRect(me, value_channel_winrect)
                        caprect = Win_GetRect(ui, value_channel_captionrect)
                        Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))


                    class children:
                        __module__ = __name__
                        class itemPic(TStatic):
                            __module__ = __name__
                            rect = (0,
                             0,
                             60,
                             56)
                            bkImgFlag = dt_center

                        class itemNum(TLabel):
                            __module__ = __name__
                            rect = (30,
                             40,
                             24,
                             12)
                            drawcolor = lightColor
                            textEdgeColor = maskColor



                class funcItem1(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 1)),
                     2,
                     60,
                     60)
                    groupstop = 1

                class funcItem2(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 2)),
                     2,
                     60,
                     60)
                    groupstop = 2

                class funcItem3(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 3)),
                     2,
                     60,
                     60)
                    groupstop = 3

                class funcItem4(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 4)),
                     2,
                     60,
                     60)
                    groupstop = 4

                class funcItem5(funcItem0):
                    __module__ = __name__
                    rect = (5,
                     (2 + (62 * 1)),
                     60,
                     60)
                    groupstop = 5

                class funcItem6(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 1)),
                     (2 + (62 * 1)),
                     60,
                     60)
                    groupstop = 6

                class funcItem7(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 2)),
                     (2 + (62 * 1)),
                     60,
                     60)
                    groupstop = 7

                class funcItem8(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 3)),
                     (2 + (62 * 1)),
                     60,
                     60)
                    groupstop = 8

                class funcItem9(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 4)),
                     (2 + (62 * 1)),
                     60,
                     60)
                    groupstop = 9

                class funcItem10(funcItem0):
                    __module__ = __name__
                    rect = (5,
                     (2 + (62 * 2)),
                     60,
                     60)
                    groupstop = 10

                class funcItem11(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 1)),
                     (2 + (62 * 2)),
                     60,
                     60)
                    groupstop = 11

                class funcItem12(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 2)),
                     (2 + (62 * 2)),
                     60,
                     60)
                    groupstop = 12

                class funcItem13(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 3)),
                     (2 + (62 * 2)),
                     60,
                     60)
                    groupstop = 13

                class funcItem14(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 4)),
                     (2 + (62 * 2)),
                     60,
                     60)
                    groupstop = 14

                class funcItem15(funcItem0):
                    __module__ = __name__
                    rect = (5,
                     (2 + (62 * 3)),
                     60,
                     60)
                    groupstop = 15

                class funcItem16(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 1)),
                     (2 + (62 * 3)),
                     60,
                     60)
                    groupstop = 16

                class funcItem17(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 2)),
                     (2 + (62 * 3)),
                     60,
                     60)
                    groupstop = 17

                class funcItem18(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 3)),
                     (2 + (62 * 3)),
                     60,
                     60)
                    groupstop = 18

                class funcItem19(funcItem0):
                    __module__ = __name__
                    rect = ((5 + (62 * 4)),
                     (2 + (62 * 3)),
                     60,
                     60)
                    groupstop = 19



        class C2CInvite(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (200,
             300,
             198,
             103)
            bkimage = 'object/ui/deal/RequestDealPanel.img'
            class children:
                __module__ = __name__
                class name(TButton):
                    __module__ = __name__
                    rect = (51,
                     20,
                     120,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor
                    textstyle = dt_left

                    def OnClick(this):
                        print 'Click response on name'
                        go2playerInfo(inviteDealUin)



                class confirm(TButton):
                    __module__ = __name__
                    rect = (40,
                     60,
                     47,
                     34)
                    bkimage = 'object/ui/deal/LittleAgreeBtn.img'

                    def OnClick(this):
                        global dealUin
                        if (not bC2CDealShow):
                            dealUin = inviteDealUin
                            C2CInviteDeal(dealUin, 2)
                            ShowC2CDealDlg(dealUin)
                        Win_ShowWidget(uiC2CInviteDlg, 0)
                        PlaySound(soundUI, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (110,
                     60,
                     47,
                     34)
                    bkimage = 'object/ui/deal/LittleRefuseBtn.img'

                    def OnClick(this):
                        C2CInviteDeal(inviteDealUin, 3)
                        Win_ShowWidget(uiC2CInviteDlg, 0)
                        PlaySound(soundUI, 1)





        class C2CDealDlg(TStatic):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (26,
             44,
             381,
             594)
            bkimage = 'object/ui/deal/C2CDealPanel.img'
            class children:
                __module__ = __name__
                class name(TLabel):
                    __module__ = __name__
                    rect = ((51 + 32),
                     (20 + 15),
                     120,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor
                    textstyle = dt_left

                class cancel(TButton):
                    __module__ = __name__
                    rect = (350,
                     11,
                     31,
                     31)
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
                        CloseC2CDealDlg(1)



                class NegotiateBtn(TButton):
                    __module__ = __name__
                    rect = (264,
                     246,
                     80,
                     31)
                    bkimage = 'object/ui/deal/DisagreeBtn.img'

                    def OnClick(this):
                        if (Win_GetText((uiC2CDealDlg + '.srcBill')) == ''):
                            srcBiddingBill = 0
                        else:
                            lastBidding = [ e for e in MyBiddingList if (e[0] == ticketitemid) ]
                            srcBiddingBill = int(Win_GetText((uiC2CDealDlg + '.srcBill')))
                        if ((srcBiddingBill > residualTicket) and ui_msgBox(3)):
                            Win_ShowMsgBox('\xc4\xfa\xb5\xc4\xbf\xe1\xb1\xc8\xb1\xa6\xca\xaf\xb2\xbb\xd7\xe3,\xb1\xbe\xb4\xce\xb3\xf6\xbc\xdb\xc3\xbb\xd3\xd0\xb3\xc9\xb9\xa6', '', 3, 'UI.SysMsgbox', -1)
                            Win_SetText((uiC2CDealDlg + '.srcBill'), ('%12f' % 0))
                            if (lastBidding != None):
                                srcBiddingBill = lastBidding[0][1]
                                Win_SetText((uiC2CDealDlg + '.srcBill'), ('%12f' % srcBiddingBill))
                            return 
                            print srcBiddingBill
                        for i in range(len(MyBiddingList)):
                            if (ticketitemid == MyBiddingList[i][0]):
                                del MyBiddingList[i]
                                break

                        MyBiddingList.append([ticketitemid,
                         srcBiddingBill])
                        Negotiate = [len(MyBiddingList),
                         MyBiddingList,
                         0,
                         0]
                        RequestNegotiate(dealUin, Negotiate)
                        UpdateAfterNegotiate()
                        UpdateStorageinDealDlg(1, InvalidIdx)
                        Win_EnableWidget((uiC2CDealDlg + '.NegotiateBtn'), 0)
                        Win_Timer((uiC2CDealDlg + '.NegotiateBtn'), 1500)



                    def OnTimer(this):
                        Win_Timer(this, 0)
                        Win_EnableWidget((uiC2CDealDlg + '.NegotiateBtn'), 1)



                    def OnMouseMoveIn():
                        ui = (uiC2CDealDlg + '.PropDescription')
                        me = Win_GetMyPath()
                        Win_SetText(ui, '\xcf\xf2\xb6\xd4\xb7\xbd\xbf\xaa\xb3\xf6\xd7\xd4\xbc\xba\xcf\xeb\xc2\xf4\xb3\xf6\xb5\xc4\xce\xef\xc6\xb7')
                        winrect = Win_GetRect(me, value_channel_winrect)
                        caprect = Win_GetRect(ui, value_channel_captionrect)
                        Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))
                        Win_ShowWidget(ui, 1)
                        Win_Timer(ui, 3000)



                class BargainingBtn(TButton):
                    __module__ = __name__
                    rect = (164,
                     246,
                     80,
                     31)
                    bkimage = 'object/ui/deal/AgreeBtn.img'

                    def OnClick(this):
                        Bargainning = [len(MyBiddingList),
                         MyBiddingList]
                        RequestBargaining(dealUin, Bargainning)
                        Win_EnableWidget((uiC2CDealDlg + '.BargainingBtn'), 0)
                        Win_Timer((uiC2CDealDlg + '.BargainingBtn'), 3000)



                    def OnTimer(this):
                        Win_Timer(this, 0)
                        Win_EnableWidget((uiC2CDealDlg + '.BargainingBtn'), 1)



                    def OnMouseMoveIn():
                        ui = (uiC2CDealDlg + '.PropDescription')
                        me = Win_GetMyPath()
                        Win_SetText(ui, '\xc8\xb7\xb6\xa8\xba\xcd\xb6\xd4\xb7\xbd\xbd\xbb\xbb\xbb\xcb\xab\xb7\xbd\xb3\xf6\xbc\xdb\xce\xef\xc6\xb7')
                        winrect = Win_GetRect(me, value_channel_winrect)
                        caprect = Win_GetRect(ui, value_channel_captionrect)
                        Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))
                        Win_ShowWidget(ui, 1)
                        Win_Timer(ui, 3000)



                class dstBill(TEditID):
                    __module__ = __name__
                    editable = 0
                    initlayer = 550001
                    maxchar = 9
                    rect = ((207 - 20),
                     70,
                     81,
                     16)
                    drawcolor = lightColor
                    textEdgeColor = maskColor
                    captionrect = (2,
                     4,
                     78,
                     16)
                    textstyle = dt_right
                    caption = '0.0'

                class srcBill(TEditID):
                    __module__ = __name__
                    initlayer = 550001
                    maxchar = 9
                    rect = ((207 - 20),
                     152,
                     81,
                     16)
                    drawcolor = lightColor
                    textEdgeColor = maskColor
                    captionrect = (2,
                     4,
                     78,
                     16)
                    textstyle = dt_right
                    caption = '0.0'

                class residualBill(TEditID):
                    __module__ = __name__
                    editable = 0
                    initlayer = 550001
                    maxchar = 12
                    rect = ((207 - 20),
                     495,
                     81,
                     16)
                    drawcolor = lightColor
                    textEdgeColor = maskColor
                    captionrect = (2,
                     4,
                     78,
                     16)
                    textstyle = dt_right

                class DstBidding0(TRadio):
                    __module__ = __name__
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
                      0,
                      0)]
                    rect = (33,
                     93,
                     60,
                     56)
                    bkimage = 'object/ui/room/btn_equipItem.img'
                    groupid = 6
                    groupstop = 0
                    dragtype = 7
                    class children:
                        __module__ = __name__
                        class itemPic(TStatic):
                            __module__ = __name__
                            rect = (0,
                             0,
                             60,
                             56)
                            bkImgFlag = dt_center

                        class itemNum(TLabel):
                            __module__ = __name__
                            rect = (36,
                             36,
                             24,
                             12)
                            drawcolor = lightColor
                            textEdgeColor = maskColor



                class DstBidding1(DstBidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 1)),
                     93,
                     60,
                     56)
                    groupstop = 1

                class DstBidding2(DstBidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 2)),
                     93,
                     60,
                     56)
                    groupstop = 2

                class DstBidding3(DstBidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 3)),
                     93,
                     60,
                     56)
                    groupstop = 3

                class DstBidding4(DstBidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 4)),
                     93,
                     60,
                     56)
                    groupstop = 4

                class Mybidding0(TRadio):
                    __module__ = __name__
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
                      0,
                      0)]
                    rect = (33,
                     181,
                     60,
                     56)
                    bkimage = 'object/ui/room/btn_equipItem.img'
                    groupid = 6
                    groupstop = 0
                    dragtype = 7

                    def OnDragItemDrop():
                        global curBiddingIdx
                        global curPropC2CDealIdx
                        me = getMyIdx2()
                        if (Win_IsVisible(uiC2CDealDlg) and ((curPropC2CDealIdx >= 0) and (curPropC2CDealIdx < totalP2PDealPropCnt))):
                            if (len(MyBiddingList) > 6):
                                return 
                            if Win_SetCheck(Win_GetMyPath(), 0):
                                Win_SetCheck((uiC2CDealDlg + ('.funcItem%d' % (curPropC2CDealIdx - MyPropC2CDealDlgPos))), 0)
                                info = [g_P2PDealPropList.at(curPropC2CDealIdx).m_stItem.m_nItemID,
                                 1]
                                Num = g_P2PDealPropList.at(curPropC2CDealIdx).m_stItem.m_iNumOfItem
                                UpdateMyBiddingList(info, Num)
                                curBiddingIdx = -1
                                curPropC2CDealIdx = -1
                                ui_UpdateMyBidding()
                                UpdateStorageinDealDlg(1, InvalidIdx)



                    def OnRClick():
                        global curEquipIdx
                        print 'MyBidding is right click'
                        path = Win_GetMyPath()
                        me = getMyIdx2()
                        UpdateStorageinDealDlg(0, me)
                        removeBiddingItem(me)
                        ui_UpdateMyBidding()
                        if (curEquipIdx == me):
                            curEquipIdx = -1
                            Win_SetCheck(path, 0)


                    class children:
                        __module__ = __name__
                        class itemPic(TStatic):
                            __module__ = __name__
                            rect = (0,
                             0,
                             60,
                             56)
                            bkImgFlag = dt_center

                        class itemNum(TLabel):
                            __module__ = __name__
                            rect = (36,
                             36,
                             24,
                             12)
                            drawcolor = lightColor
                            textEdgeColor = maskColor



                class Mybidding1(Mybidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 1)),
                     181,
                     60,
                     56)
                    groupstop = 1

                class Mybidding2(Mybidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 2)),
                     181,
                     60,
                     56)
                    groupstop = 2

                class Mybidding3(Mybidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 3)),
                     181,
                     60,
                     56)
                    groupstop = 3

                class Mybidding4(Mybidding0):
                    __module__ = __name__
                    rect = ((33 + (62 * 4)),
                     181,
                     60,
                     56)
                    groupstop = 4

                class Left(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    rect = (33,
                     485,
                     33,
                     36)
                    bkimage = 'object/ui/common/btn_left.img'

                    def OnClick(this):
                        global MyPropC2CDealDlgPos
                        MyPropC2CDealDlgPos = max((MyPropC2CDealDlgPos - defMyPropC2CDealDlgCnt), 0)
                        UpdateMyPropC2CDealDlg()
                        PlaySound(soundUI, 1)



                class Right(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    rect = (146,
                     485,
                     33,
                     36)
                    bkimage = 'object/ui/common/btn_right.img'

                    def OnClick(this):
                        global MyPropC2CDealDlgPos
                        if ((MyPropC2CDealDlgPos + defMyPropC2CDealDlgCnt) >= totalP2PDealPropCnt):
                            return 
                        MyPropC2CDealDlgPos = (MyPropC2CDealDlgPos + defMyPropC2CDealDlgCnt)
                        UpdateMyPropC2CDealDlg()
                        PlaySound(soundUI, 1)



                class MyPropPage:
                    __module__ = __name__
                    type = 'NUMLABEL'
                    rect = (63,
                     490,
                     80,
                     24)
                    bkimage = 'object/ui/common/number2.img'
                    textstyle = dt_center
                    textsize = 16
                    textwidth = 19
                    textheight = 24

                class PropDescription:
                    __module__ = __name__
                    type = 'DYLABEL'
                    initlayer = 99999
                    rect = (0,
                     0,
                     130,
                     1)
                    captionrect = (4,
                     4,
                     120,
                     1)
                    bkimage = 'object/ui/common/img_tip.img'
                    textEdgeType = -1
                    drawcolor = maskColor

                    def OnTimer(this):
                        Win_ShowWidget(this, 0)
                        Win_Timer(this, 0)



                class funcItem0(TRadio):
                    __module__ = __name__
                    groupid = 3
                    groupstop = 0
                    rect = (33,
                     296,
                     60,
                     60)
                    dragtype = 7
                    bkimage = 'object/ui/storage/img_choose.img'
                    framescheme = [(-1,
                      -1,
                      -1,
                      -1,
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
                      0,
                      0)]
                    tipwidget = (uiC2CDealDlg + '.PropDescription')

                    def OnDBClick():
                        global curPropC2CDealIdx
                        if (len(MyBiddingList) > 6):
                            return 
                        me = getMyIdx2()
                        curPropC2CDealIdx = (MyPropC2CDealDlgPos + me)
                        if (g_P2PDealPropList.at(curPropC2CDealIdx) == None):
                            return 
                        info = [g_P2PDealPropList.at(curPropC2CDealIdx).m_stItem.m_nItemID,
                         1]
                        Num = g_P2PDealPropList.at(curPropC2CDealIdx).m_stItem.m_iNumOfItem
                        UpdateMyBiddingList(info, Num)
                        curBiddingIdx = -1
                        curPropC2CDealIdx = -1
                        UpdateStorageinDealDlg(1, InvalidIdx)
                        ui_UpdateMyBidding()



                    def OnBeginItemDrag():
                        global uiPropC2CInx
                        global curPropC2CDealIdx
                        uiPropC2CInx = getMyIdx2()
                        print uiPropC2CInx
                        curPropC2CDealIdx = (MyPropC2CDealDlgPos + uiPropC2CInx)
                        if (g_P2PDealPropList.at(curPropC2CDealIdx) == None):
                            return 
                        info = g_P2PDealPropList.at(curPropC2CDealIdx).m_stItem
                        path = Win_GetMyPath()
                        if CHECK_PET(info.m_nItemID):
                            petResId = GetPetResId(info.m_nItemID, 10)
                            Win_SetDragImg(path, ('res/uiRes/icon/pet/pet%d.img' % petResId))
                        else:
                            Win_SetDragImg(path, ('res/uires/icon/item/item%d.img' % info.m_nItemID))



                    def OnRClick():
                        global curPropC2CDealIdx
                        path = Win_GetMyPath()
                        me = getMyIdx2()
                        if (curPropC2CDealIdx == (MyPropC2CDealDlgPos + me)):
                            curPropC2CDealIdx = -1
                            Win_SetCheck(path, 0)



                    def OnMouseMoveIn():
                        me = Win_GetMyPath()
                        idx = (getMyIdx2() + MyPropC2CDealDlgPos)
                        if (idx >= totalP2PDealPropCnt):
                            return 
                        info = g_P2PDealPropList.at(idx)
                        ui = (uiC2CDealDlg + '.PropDescription')
                        Win_SetText(ui, ((info.m_szName + '\n') + info.m_szDescrip))
                        winrect = Win_GetRect(me, value_channel_winrect)
                        caprect = Win_GetRect(ui, value_channel_captionrect)
                        Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))


                    class children:
                        __module__ = __name__
                        class itemPic(TStatic):
                            __module__ = __name__
                            rect = (0,
                             0,
                             60,
                             56)
                            bkImgFlag = dt_center

                        class itemNum(TLabel):
                            __module__ = __name__
                            rect = (30,
                             40,
                             24,
                             12)
                            drawcolor = lightColor
                            textEdgeColor = maskColor



                class funcItem1(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 1)),
                     296,
                     60,
                     60)
                    groupstop = 1

                class funcItem2(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 2)),
                     296,
                     60,
                     60)
                    groupstop = 2

                class funcItem3(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 3)),
                     296,
                     60,
                     60)
                    groupstop = 3

                class funcItem4(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 4)),
                     296,
                     60,
                     60)
                    groupstop = 4

                class funcItem5(funcItem0):
                    __module__ = __name__
                    rect = (33,
                     (296 + (62 * 1)),
                     60,
                     60)
                    groupstop = 5

                class funcItem6(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 1)),
                     (296 + (62 * 1)),
                     60,
                     60)
                    groupstop = 6

                class funcItem7(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 2)),
                     (296 + (62 * 1)),
                     60,
                     60)
                    groupstop = 7

                class funcItem8(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 3)),
                     (296 + (62 * 1)),
                     60,
                     60)
                    groupstop = 8

                class funcItem9(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 4)),
                     (296 + (62 * 1)),
                     60,
                     60)
                    groupstop = 9

                class funcItem10(funcItem0):
                    __module__ = __name__
                    rect = (33,
                     (296 + (62 * 2)),
                     60,
                     60)
                    groupstop = 10

                class funcItem11(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 1)),
                     (296 + (62 * 2)),
                     60,
                     60)
                    groupstop = 11

                class funcItem12(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 2)),
                     (296 + (62 * 2)),
                     60,
                     60)
                    groupstop = 12

                class funcItem13(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 3)),
                     (296 + (62 * 2)),
                     60,
                     60)
                    groupstop = 13

                class funcItem14(funcItem0):
                    __module__ = __name__
                    rect = ((33 + (62 * 4)),
                     (296 + (62 * 2)),
                     60,
                     60)
                    groupstop = 14






#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
