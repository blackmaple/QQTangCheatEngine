'\nexecfile("uiConst.py")\nexecfile("uiTemplate.py")\nlightColor = 1\nzoneChooseColor = 1\nmaskColor = 1\nuiShopStorageDlg = \'\'\ndef SC_GetTipIndex(idx):\n    return 1\nuiTaskDlg = \'\'\nclass TTip:\n    pass\nmemberFaceIconList =[]\nfaceIconList = []\n'
msgcnt = 3
bmsg = ([0] * msgcnt)
msgbuf = ([''] * msgcnt)
namebuf = ([''] * msgcnt)
uinbuf = ([0] * msgcnt)
isBugle = 0
IsPopo = 0
CurXeffectSubID = 0
menuMode = 0
ChatMode = 0
ChatOrientation = 0
ChatAreaTab = 0
localShopVersion = 0
lastestShopVersion = 0
CommonType = 0
PVPType = 1
PVEType = 2
LootType = 3
GameType = 0
OldGameType = 0
IsShowStorageDlg = 0
ChatType = 4
firstEnter = 1
playerExp = 0
playerReputation = 0
isQQMember = 0
allGameModeList = [(-1,
  'none',
  '\xcb\xf9\xd3\xd0\xb7\xbf\xbc\xe4'),
 (0,
  'all',
  '\xc8\xab\xb2\xbf\xb5\xd8\xcd\xbc'),
 (1,
  'normal',
  '\xc6\xd5\xcd\xa8'),
 (2,
  'bomb',
  '\xcc\xdf\xd5\xa8\xb5\xaf'),
 (3,
  'bun',
  '\xc7\xc0\xb0\xfc\xd7\xd3'),
 (4,
  'match',
  '\xb1\xc8\xce\xe4'),
 (5,
  'treasure',
  '\xb6\xe1\xb1\xa6'),
 (6,
  'sculpture',
  '\xd3\xa2\xd0\xdb\xb4\xab\xcb\xb5'),
 (7,
  'machine',
  '\xbb\xfa\xd0\xb5\xca\xc0\xbd\xe7'),
 (8,
  'box',
  '\xcd\xc6\xcf\xe4\xd7\xd3'),
 (13,
  'tank',
  '\xcc\xc7\xbf\xcd\xd5\xbd')]
gameModeList = allGameModeList
validGameModeDict = {}
allMapTypeList = ['rand',
 'box',
 'machine',
 'treasure',
 'sculpture',
 'bomb',
 'bun',
 'tank',
 'match',
 'pig',
 'water',
 'field',
 'town',
 'desert',
 'mine',
 'snow']
mapTypeList = []

def setupValidGameMode():
    global gameModeList

    def setupValidGameModeDict():
        global validGameModeDict
        validGameModeDict = {'rand': 1}
        for i in gameModeList:
            validGameModeDict[i[1]] = 1

        if validGameModeDict.has_key('normal'):
            normalList = ['water',
             'field',
             'town',
             'desert',
             'mine',
             'snow',
             'pig']
            for name in normalList:
                validGameModeDict[name] = 1




    def setupValidMapType():
        global mapTypeList
        mapTypeList = []
        for it in allMapTypeList:
            if (validGameModeDict.has_key(it) and mapTypeList.append(it)):
                pass



    gameModeList = [allGameModeList[0]]
    validGameMode = fetch_ValidGameModes()
    for i in allGameModeList:
        if ((validGameMode.count(i[0]) > 0) and gameModeList.append(i)):
            pass

    setupValidGameModeDict()
    setupValidMapType()



def setupMapList(gameType):
    global mapTypeList
    if (gameType == 2):
        mapTypeList = ['pve']
    else:
        mapTypeList = []
        for it in allMapTypeList:
            if (validGameModeDict.has_key(it) and mapTypeList.append(it)):
                pass



curGameMode = 0
oldWinEventCnt = -1
hasInfo = 0
roomID = -1
playerMode = 0
friendPos = 0
friendCnt = 0
friendIndex = 0
kinMemberPos = 0
kinMemberCnt = 0
kinMemberIndex = 0
playerPos = 0
playerCnt = 0
defPlayerCnt = 16
uins = range((defPlayerCnt + 1))
playerMode2 = 0
playerPos2 = 0
friendPos2 = 0
kinMemberPos2 = 0
defPlayerCnt2 = 11
flexMode = 2
uins2 = range((defPlayerCnt2 + 1))
roomCnt = 0
defRoomNum = 9
roomPagePos = 1
markEnterShop = False
facePage = 0
memberFacePage = 0
memberFacePageNum = ((len(memberFaceIconList) + 23) / 24)
facePageNum = (((len(faceIconList) + 23) / 24) - memberFacePageNum)
isMemberFace = 0
chatNameInSec = '\xb4\xf3  \xcc\xfc'
chatNameInRoom = '\xb7\xbf  \xbc\xe4'
chatNameSpeaker = '\xd0\xa1\xc0\xae\xb0\xc8'
TopkinCnt = 0
TopkinCurrentPos = 0
defTopkinDlgCnt = 7
ActivetopkinPos = 999999
chinatelecom = 1
setreputation = 1
curPetId = 0
curPetName = ''
curPetState = 1
petsIdList = []
skillIdList = []
baseSkillIdList = []
petItemList = []
petItemPos = 0
defPetItemCnt = 12
curUseItem = 0
PawnTypeCnt = 0
CurrenPawnType = -1
PawnItemCnt = 0
defPawnItemCnt = 22
defPawnwareCnt = 12
PawnGoodsCnt = 0
CurrentPawnItemID = 0
defPawnGoodsCnt = 24
PawnGoodsPos = 0
totalPawnGoodsCnt = 0
defStorageInPawnCnt = 12
CurrentPropIdx = 0
defCommittedCnt = 6
check12 = 1
Commit2Pawn = 1
CancelCommit2Pawn = 3
MyPawnItemListCnt = 0
buyItemInfo = []
petbaseInfo = CNil()
ShowMyPawned = 0
IsShowingStorageTip = 0

def CHECK_BASESKILL(skillId):
    return (skillId <= 50)



def CHECK_PET(ID):
    if ((ID >= 25001) and (ID <= 26000)):
        return 1
    return 0



def CHECK_PET_RELATION(ID):
    return ((ID >= 25001) and (ID <= 29000))



def ui_GetLevelMainPath(point):
    levelInfo = Level().getInfo(point)
    print levelInfo
    if ((0 == point) and (-1 == point)):
        return ''
    return Level().getMainLevel(levelInfo[1])



def ui_GetLevelSubPath(point):
    levelInfo = Level().getInfo(point)
    if ((0 == point) and (-1 == point)):
        return ''
    return Level().getMinLevel(levelInfo[1], levelInfo[2])



def ChangeChatMode(newMode):
    global isMemberFace
    global ChatMode
    if (Win_GetCurScreen() == 'selRoom'):
        ui = 'UI.selRoom.chatArea'
    elif (Win_GetCurScreen() == 'room'):
        ui = 'UI.room.chatArea'
    else:
        return 
    num = GetBugleNumber()
    if (num <= 0):
        ChatMode = 0
        Win_SetImg((ui + '.speakerBtn'), 'object/ui/chat/btn_ldspker_disable.img')
        Win_EnableWidget((ui + '.faceBtn.faceDlg.choose'), 1)
        Win_SetText((ui + '.chatEdit'), '')
        Win_SetValue((ui + '.chatEdit'), 200, 903)
    elif (newMode == 1):
        ChatMode = 1
        isMemberFace = 0
        Win_EnableWidget((ui + '.faceBtn.faceDlg.choose'), 0)
        setFacePage(facePage, facePageNum)
        Win_SetImg((ui + '.speakerBtn'), 'object/ui/chat/btn_ldspker_pushdown.img')
        Win_SetText((ui + '.chatEdit'), '')
        Win_SetValue((ui + '.chatEdit'), 44, 903)
    else:
        ChatMode = 0
        Win_EnableWidget((ui + '.faceBtn.faceDlg.choose'), 1)
        Win_SetImg((ui + '.speakerBtn'), 'object/ui/chat/btn_speaker.img')
        Win_SetText((ui + '.chatEdit'), '')
        Win_SetValue((ui + '.chatEdit'), 200, 903)



def UpdateUIWisper():
    name = GetWisperName(0)
    if ((Win_GetCurScreen() == 'selRoom') and (name != '0')):
        if Win_SetText('UI.selRoom.chatArea.orientation', name):
            pass



def UpdateUIKinChat():
    name = GetWisperName(1)
    if ((Win_GetCurScreen() == 'selRoom') and Win_SetText('UI.selRoom.chatArea.orientation', name)):
        pass



def NotifyWisper(name, wisperuin):
    print 'SetWisperPlayer',
    print name,
    print ((' [' + str(wisperuin)) + ']')
    SetWisperPlayer(wisperuin, name)
    if ((wisperuin and ((wisperuin != uin) and (ChatMode == 1))) and ChangeChatMode(0)):
        pass
    UpdateUIWisper()



def InitChatMode():
    if ((Win_GetCurScreen() == 'selRoom') and NotifyWisper(chatNameInSec, 0)):
        pass
    ChangeChatMode(0)



def UIRefreshChatMode():
    ChangeChatMode(ChatMode)



def startGlint():
    global hasInfo
    hasInfo = 1
    ui = ''
    if ('selRoom' == Win_GetCurScreen()):
        ui = 'UI.selRoom.chatArea.donateInfo'
    elif ('room' == Win_GetCurScreen()):
        ui = 'UI.room.chatArea.donateInfo'
    Win_ShowWidget(ui, True)
    Win_Timer(ui, 400)



def endGlint():
    global hasInfo
    hasInfo = 0
    ui = ''
    if ('selRoom' == Win_GetCurScreen()):
        ui = 'UI.selRoom.chatArea.donateInfo'
    elif ('room' == Win_GetCurScreen()):
        ui = 'UI.room.chatArea.donateInfo'
    Win_Timer(ui, 0)
    Win_ShowWidget(ui, False)



def InitChatArea():
    Win_SetText('UI.selRoom.chatArea.chatPanel.chatList', '', value_channel_listitem_num)
    Win_SetText('UI.selRoom.chatArea.kinchatPanel.chatList', '', value_channel_listitem_num)
    Win_SetText('UI.selRoom.chatArea.wisperPanel.chatList', '', value_channel_listitem_num)
    if ((ChatAreaTab == 0) and Win_SelectSelf('UI.selRoom.chatArea.integration')):
        Win_ShowWidget('UI.selRoom.chatArea.chatPanel', 1)
        Win_ShowWidget('UI.selRoom.chatArea.kinchatPanel', 0)
        Win_ShowWidget('UI.selRoom.chatArea.wisperPanel', 0)



def flexChatArea(mode):
    global defPlayerCnt2
    ui = ['UI.selRoom.chatArea.chatPanel',
     'UI.selRoom.chatArea.kinchatPanel',
     'UI.selRoom.chatArea.wisperPanel']
    for k in range(len(ui)):
        if ((1 == mode) and Win_SetImg(ui[k], 'object/ui/selRoom/dlg_chatMin.img')):
            Win_Move2Pos(ui[k], 442, 354)
            Win_SetRect(ui[k], value_channel_winrect, 442, 354, 320, 116)
            Win_SetRect((ui[k] + '.chatList'), value_channel_winrect, Win_GetX((ui[k] + '.chatList')), Win_GetY((ui[k] + '.chatList')), 320, 98)
            Win_SetRect((ui[k] + '.chatList'), value_channel_clientrect, 0, 0, 320, 98)
            Win_SetRect((ui[k] + '.chatList.chatScroll'), value_channel_clientrect, 0, 0, 14, 90)
            Win_Update((ui[k] + '.chatList'))
            Win_Update((ui[k] + '.chatList.chatScroll'))
            defPlayerCnt2 = 11




def InitSpeaker():
    global isBugle
    if (Win_GetCurScreen() == 'selRoom'):
        ui = ['UI.selRoom.chatArea.chatPanel',
         'UI.selRoom.chatArea.kinchatPanel',
         'UI.selRoom.chatArea.wisperPanel']
        for k in range(len(ui)):
            if ((IsPopo == 1) and Win_SetValue((ui[k] + '.speaker0.popo'), 1.0, 42)):
                Win_SetValue((ui[k] + '.speaker0.popo'), 1, 901)
                if ((CurXeffectSubID == 0) and Win_SetImg((ui[k] + '.speaker0.popo'), 'object/ui/selRoom/img_popo.img')):
                    pass
            for i in range(msgcnt):
                if (bmsg[i] and Win_ShowWidget((ui[k] + ('.speaker%d' % i)), 1)):
                    Win_SetDrawColor((ui[k] + ('.speaker%d' % i)), 200, 100, 100, 255)
                    Win_SetValue((ui[k] + ('.speaker%d' % i)), 1.0, 41)
                    Win_SetValue((ui[k] + ('.speaker%d' % i)), 1, 901)
                    Win_SetText((ui[k] + ('.speaker%d.words' % i)), (namebuf[i] + msgbuf[i]))


    elif (Win_GetCurScreen() == 'room'):
        ui = ['UI.room.chatArea.chatPanel',
         'UI.room.chatArea.kinchatPanel',
         'UI.room.chatArea.wisperPanel']
        for k in range(len(ui)):
            if ((IsPopo == 1) and Win_SetValue((ui[k] + '.speaker0.popo'), 1.0, 42)):
                Win_SetValue((ui[k] + '.speaker0.popo'), 1, 901)
                if ((CurXeffectSubID == 0) and Win_SetImg((ui[k] + '.speaker0.popo'), 'object/ui/room/img_popo.img')):
                    pass
            i = 0
            if (bmsg[i] and Win_ShowWidget((ui[k] + ('.speaker%d' % i)), 1)):
                Win_SetDrawColor((ui[k] + ('.speaker%d' % i)), 200, 100, 100, 255)
                Win_SetValue((ui[k] + ('.speaker%d' % i)), 1.0, 41)
                Win_SetValue((ui[k] + ('.speaker%d' % i)), 1, 901)
                Win_SetText((ui[k] + ('.speaker%d.words' % i)), msgbuf[i])
                Win_SetText((ui[k] + ('.speaker%d.nameBtn' % i)), namebuf[i])
                path = (ui[k] + ('.speaker%d.nameBtn' % i))
                winrect = Win_GetRect(path, value_channel_winrect)
                caprect = Win_GetRect(path, value_channel_captionrect)
                Win_SetRect(path, value_channel_winrect, winrect[0], winrect[1], (len(namebuf[i]) * 6), winrect[3])
                Win_SetRect(path, value_channel_captionrect, caprect[0], caprect[1], (len(namebuf[i]) * 6), caprect[3])
                Win_SetRect((ui[k] + ('.speaker%d.words' % i)), value_channel_winrect, (winrect[0] + (len(namebuf[i]) * 6)), winrect[1], (465 - (len(namebuf[i]) * 6)), winrect[3])
                Win_SetRect((ui[k] + ('.speaker%d.words' % i)), value_channel_captionrect, caprect[0], caprect[1], (465 - (len(namebuf[i]) * 6)), caprect[3])

    elif (Win_GetCurScreen() == 'game'):
        ui = 'UI.game.broadcastZone.speaker'
        isBugle = 0
        if (bmsg[0] and Win_SetDrawColor(ui, 200, 100, 100, 255)):
            Win_SetValue(ui, 1.0, 41)
            Win_SetValue(ui, 1, 901)
            Win_SetText(ui, (namebuf[0] + msgbuf[0]))



def NotifyBroadcast(name, uin, msg):
    (r, g, b, a,) = broadcastColor
    for i in range(msgcnt):
        if (bmsg[i] and (i < (msgcnt - 1))):
            continue
        bmsg[i] = 1
        for j in range(i):
            k = (i - j)
            msgbuf[k] = msgbuf[(k - 1)]
            namebuf[k] = namebuf[(k - 1)]
            uinbuf[k] = uinbuf[(k - 1)]

        msgbuf[0] = msg
        namebuf[0] = name
        uinbuf[0] = uin
        break

    if (Win_GetCurScreen() == 'selRoom'):
        ui = ['UI.selRoom.chatArea.chatPanel',
         'UI.selRoom.chatArea.kinchatPanel',
         'UI.selRoom.chatArea.wisperPanel']
        for j in range(len(ui)):
            for i in range(msgcnt):
                if (bmsg[i] and Win_ShowWidget((ui[j] + ('.speaker%d' % i)), 1)):
                    Win_SetDrawColor((ui[j] + ('.speaker%d' % i)), r, g, b, a)
                    Win_SetValue((ui[j] + ('.speaker%d' % i)), 1.0, 41)
                    Win_SetValue((ui[j] + ('.speaker%d' % i)), 1, 901)
                    Win_SetText((ui[j] + ('.speaker%d.words' % i)), (namebuf[i] + msgbuf[i]))


    elif (Win_GetCurScreen() == 'room'):
        ui = ['UI.room.chatArea.chatPanel',
         'UI.room.chatArea.kinchatPanel',
         'UI.room.chatArea.wisperPanel']
        for k in range(len(ui)):
            i = 0
            if (bmsg[i] and Win_ShowWidget((ui[k] + ('.speaker%d' % i)), 1)):
                Win_SetDrawColor((ui[k] + ('.speaker%d' % i)), r, g, b, a)
                Win_SetValue((ui[k] + ('.speaker%d' % i)), 1.0, 41)
                Win_SetValue((ui[k] + ('.speaker%d' % i)), 1, 901)
                Win_SetText((ui[k] + ('.speaker%d.words' % i)), msgbuf[i])
                Win_SetText((ui[k] + ('.speaker%d.nameBtn' % i)), namebuf[i])
                path = (ui[k] + ('.speaker%d.nameBtn' % i))
                winrect = Win_GetRect(path, value_channel_winrect)
                caprect = Win_GetRect(path, value_channel_captionrect)
                Win_SetRect(path, value_channel_winrect, winrect[0], winrect[1], (len(namebuf[i]) * 6), winrect[3])
                Win_SetRect(path, value_channel_captionrect, caprect[0], caprect[1], (len(namebuf[i]) * 6), caprect[3])
                Win_SetRect((ui[k] + ('.speaker%d.words' % i)), value_channel_winrect, (winrect[0] + (len(namebuf[i]) * 6)), winrect[1], (465 - (len(namebuf[i]) * 6)), winrect[3])
                Win_SetRect((ui[k] + ('.speaker%d.words' % i)), value_channel_captionrect, caprect[0], caprect[1], (465 - (len(namebuf[i]) * 6)), caprect[3])

    elif (Win_GetCurScreen() == 'game'):
        ui = 'UI.game.broadcastZone.speaker'
        Win_SetText(ui, (name + msg))
        Win_SetValue(ui, 1.0, 41)
        Win_SetValue(ui, 1, 901)



def NotifyRemoveMsg():
    j = (msgcnt - 1)
    for i in range(msgcnt):
        j = ((msgcnt - i) - 1)
        if bmsg[j]:
            bmsg[j] = 0
            break

    if (Win_GetCurScreen() == 'selRoom'):
        ui = ['UI.selRoom.chatArea.chatPanel',
         'UI.selRoom.chatArea.kinchatPanel',
         'UI.selRoom.chatArea.wisperPanel']
        for k in range(len(ui)):
            Win_SetValue((ui[k] + ('.speaker%d' % j)), 0.01, 41)
            Win_SetValue((ui[k] + ('.speaker%d' % j)), 2, 901)

    elif (Win_GetCurScreen() == 'room'):
        ui = ['UI.room.chatArea.chatPanel',
         'UI.room.chatArea.kinchatPanel',
         'UI.room.chatArea.wisperPanel']
        for k in range(len(ui)):
            Win_SetValue((ui[k] + ('.speaker%d' % j)), 0.01, 41)
            Win_SetValue((ui[k] + ('.speaker%d' % j)), 2, 901)

    elif (Win_GetCurScreen() == 'game'):
        ui = 'UI.game.broadcastZone.speaker'
        if ((0 == j) and Win_SetValue(ui, 0.01, 41)):
            Win_SetValue(ui, 2, 901)



def NotifyAddPopo(dwXeffectID):
    global CurXeffectSubID
    global IsPopo
    IsPopo = 1
    if (dwXeffectID != 0):
        desc = itemList[dwXeffectID]
        (type, dwXeffectSubID,) = desc[0:2]
        CurXeffectSubID = dwXeffectSubID
        if (type != 'xeffect'):
            dwXeffectID = 0
            CurXeffectSubID = 0
    else:
        CurXeffectSubID = 0
    if (Win_GetCurScreen() == 'selRoom'):
        ui = ['UI.selRoom.chatArea.chatPanel.speaker0.popo',
         'UI.selRoom.chatArea.kinchatPanel.speaker0.popo',
         'UI.selRoom.chatArea.wisperPanel.speaker0.popo']
        if (dwXeffectID == 0):
            for j in range(len(ui)):
                Win_SetValue(ui[j], 0.80000000000000004, 42)
                Win_SetValue(ui[j], 0.01, 41)
                Win_SetValue(ui[j], 1, 901)
                Win_SetImg(ui[j], 'object/ui/selRoom/img_popo.img')

        else:
            for j in range(len(ui)):
                Win_SetValue(ui[j], 0.80000000000000004, 42)
                Win_SetValue(ui[j], 0.01, 41)
                Win_SetValue(ui[j], 1, 901)
                Win_SetImg(ui[j], (('object/xeffect/xeffect' + str(dwXeffectSubID)) + '_stand.img'))

    elif (Win_GetCurScreen() == 'room'):
        ui = ['UI.room.chatArea.chatPanel.speaker0.popo',
         'UI.room.chatArea.kinchatPanel.speaker0.popo',
         'UI.room.chatArea.wisperPanel.speaker0.popo']
        if (dwXeffectID == 0):
            for k in range(len(ui)):
                Win_SetValue(ui[k], 0.80000000000000004, 42)
                Win_SetValue(ui[k], 0.01, 41)
                Win_SetValue(ui[k], 1, 901)
                Win_SetImg(ui[k], 'object/ui/room/img_popo.img')

        else:
            for k in range(len(ui)):
                Win_SetValue(ui[k], 0.80000000000000004, 42)
                Win_SetValue(ui[k], 0.01, 41)
                Win_SetValue(ui[k], 1, 901)
                Win_SetImg(ui[k], (('object/xeffect/xeffect' + str(dwXeffectSubID)) + '_walk.img'))




def NotifyRemovePopo():
    global IsPopo
    IsPopo = 0
    if (Win_GetCurScreen() == 'selRoom'):
        ui = 'UI.selRoom.chatArea.chatPanel.speaker0.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.chatPanel.speaker1.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.chatPanel.speaker2.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.kinchatPanel.speaker0.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.kinchatPanel.speaker1.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.kinchatPanel.speaker2.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.wisperPanel.speaker0.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.wisperPanel.speaker1.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.selRoom.chatArea.wisperPanel.speaker2.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
    elif (Win_GetCurScreen() == 'room'):
        ui = 'UI.room.chatArea.chatPanel.speaker0.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.chatPanel.speaker1.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.chatPanel.speaker2.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.kinchatPanel.speaker0.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.kinchatPanel.speaker1.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.kinchatPanel.speaker2.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.wisperPanel.speaker0.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.wisperPanel.speaker1.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)
        ui = 'UI.room.chatArea.wisperPanel.speaker2.popo'
        Win_SetValue(ui, 0.01, 41)
        Win_SetValue(ui, 2, 901)



def useExtItem(ID, playerNum):
    if commodityList.has_key(ID):
        type = commodityList[ID][0]
        idx = commodityList[ID][1]
        picName = ('object/%s/%s%d_stand.img' % (type,
         type,
         idx))
        if ((type == 'namecard') and Win_SetImg((uiPlayerListDlg + ('.playerInfo%d.namecard' % playerNum)), picName)):
            pass
    else:
        return 



def unUseAllExtItem(playerNum):
    Win_SetImg((uiPlayerListDlg + ('.playerInfo%d.namecard' % playerNum)), '')
    Win_SetImg((uiPlayerListDlg + ('.playerInfo%d.namecardbound' % playerNum)), '')



def closeMenu():
    ui = Win_GetCurScreen()
    Win_ShowWidget((('UI.' + ui) + '.menuDlg'), 0)



def stripStr(s):
    if ('' == s):
        return ''
    while ((len(s) > 1) and (('"' == s[0]) or ("'" == s[0]))):
        s = s[1:]

    while ((len(s) > 1) and (('"' == s[-1]) or (("'" == s[-1]) or (' ' == s[-1])))):
        s = s[:-1]

    return s


class Sect:
    __module__ = __name__

    def getName(this):
        info = sc_getCurSectInfo()
        name = info.m_szSectionName
        serverName = zoneList[curZone]
        return ((stripStr(serverName) + '  >>  ') + stripStr(name))



    def meGetPlayerInfo(this):
        return fetch_PlayerInfoInPlayerList(0, 0).m_PlayerInfo



    def meHasPassport(this):
        pi = this.meGetPlayerInfo()
        return (0 != (pi.m_dwIdentity & ((64 | 256) | 512)))



    def meGetPoint(this):
        pi = this.meGetPlayerInfo()
        gi = pi.m_stGameInfo
        return gi.m_dwPoint




def leaveSection():
    doUI('UI.selRoom', 'OnEscape')



def getMapInfo(ID):
    desc = getMapDesc(ID)
    info = CNil()
    info.ID = desc[0]
    info.type = desc[1]
    info.name = desc[2]
    info.size = ('%d X %d' % (desc[3],
     desc[4]))
    info.playerNum = desc[5]
    info.picName = ('map/' + desc[7])
    return info



def setFacePage(page, pageNum):
    global facePage
    global memberFacePage
    if (Win_GetCurScreen() == 'selRoom'):
        ui_bg = 'UI.selRoom.chatArea'
    elif (Win_GetCurScreen() == 'room'):
        ui_bg = 'UI.room.chatArea'
    else:
        return 
    Win_SetText((ui_bg + '.faceBtn.faceDlg.pageLab'), ('%d/%d' % ((page + 1),
     pageNum)))
    if isMemberFace:
        memberFacePage = page
        start = (page * 24)
        for k in range(24):
            i = (start + k)
            ui = ((ui_bg + '.faceBtn.faceDlg.box.face') + str(k))
            if ((i < len(memberFaceIconList)) and Win_SetImg(ui, ('res/uires/face/faces/member/%03d.img' % (i)))):
                Win_ShowWidget(ui, True)

    else:
        facePage = page
        start = ((page + memberFacePageNum) * 24)
        for k in range(24):
            i = (start + k)
            ui = ((ui_bg + '.faceBtn.faceDlg.box.face') + str(k))
            if ((i < len(faceIconList)) and Win_SetImg(ui, ('res/uires/face/faces/%03d.img' % (i)))):
                Win_ShowWidget(ui, True)




def playerInfo_useCommItem(ID):

    def useIt(ID):
        if (not itemList.has_key(ID)):
            print 'dont know comm item, ID=',
            print ID
            return 
        desc = itemList[ID]
        (type, idx,) = desc[0:2]
        ui = (uiPlayerInfoDlg + '.playerDemo')
        if equipMap.has_key(type):
            itemInfo = GetItemInfoFromSec(ID)
            selRoom_playerWear(type, idx, itemInfo.m_bItemEffect, itemInfo.m_bItemColor)
        else:
            if (('bg' == type) and Win_SetImg((ui + '.bg'), ('object/bg/bg%d_stand.img' % idx))):
                pass


    useIt(ID)



def ui_sectSetBtnState(buttonID, isEnable):
    if ((1 == buttonID) and Win_EnableWidget('UI.selRoom.roomLeft', isEnable)):
        pass



def myGetPlayerCnt():
    global friendCnt
    global playerCnt
    global kinMemberCnt
    cnt = GetPlayerCnt(playerMode)
    if (0 == playerMode):
        playerCnt = cnt
    elif (1 == playerMode):
        friendCnt = cnt
    elif (2 == playerMode):
        kinMemberCnt = cnt
    return cnt



def myGetPlayerPos():
    if (0 == playerMode):
        return playerPos
    elif (1 == playerMode):
        return friendPos
    elif (2 == playerMode):
        return kinMemberPos



def mySetPlayerPos(pos):
    global playerPos
    global kinMemberPos
    global friendPos
    if (0 == playerMode):
        playerPos = pos
    elif (1 == playerMode):
        friendPos = pos
    elif (2 == playerMode):
        kinMemberPos = pos



def maskPlayer(begin, end):
    ui = (uiPlayerListDlg + '.friendMask')
    x = Win_GetX(ui)
    y = 107
    if (((begin >= end) or (begin < 0)) and Win_SetDrawTexRect(ui, 0, (begin * 24), 330, 0)):
        Win_SetRect((ui + '.tipBtn'), value_channel_winrect, x, (y + (begin * 24)), 330, 0)



def updatePlayer():

    def myGetPlayerInfo(i, mode):

        def getFake(i):
            if (i >= playerCnt):
                return None
            info = CNil()
            info.isVip = True
            info.name = 'Mike Chen'
            info.isBoy = True
            info.level = 2
            info.uin = 6676317
            return info



        def get(i, mode):
            cnt = 0
            if (mode == 0):
                cnt = playerCnt
            elif (1 == mode):
                cnt = friendCnt
            elif (2 == mode):
                cnt = kinMemberCnt
            if (i >= cnt):
                return None
            info = CNil()
            pi = fetch_PlayerInfoInPlayerList(i, mode)
            a = pi.m_PlayerInfo
            gameInfo = a.m_stGameInfo
            info.state = pi.m_nPlayerStatus
            info.isVip = (a.m_dwIdentity & 8)
            info.isgoldDiamond = (a.m_dwIdentity & 8192)
            info.name = a.m_szPlayerNickname.replace('\n', '')
            info.isBoy = (1 == int(a.m_bGender))
            info.level = Level().getInfo(gameInfo.m_dwPoint)
            info.uin = a.m_dwPlayerUin
            info.extItemNum = a.m_bExtItemNum
            info.m_dwKinIndex = a.m_dwKinIndex
            info.m_nKinNameLen = a.m_nKinNameLen
            info.m_szKinName = a.m_szKinName
            info.m_stKinFlagID = a.m_stKinFlagID
            return info


        return get(i, mode)



    def show(player, b):
        Win_ShowWidget((player + '.name'), b)
        Win_ShowWidget((player + '.gender'), b)
        Win_ShowWidget((player + '.levelIcon'), b)
        Win_ShowWidget((player + '.goldDiamond'), b)
        Win_ShowWidget((player + '.kintotem'), b)


    listCnt = myGetPlayerCnt()
    listPos = myGetPlayerPos()
    for i in range(defPlayerCnt):
        player = ((uiPlayerListDlg + '.playerInfo') + str((i + 1)))
        unUseAllExtItem((i + 1))
        info = myGetPlayerInfo((i + listPos), playerMode)
        if (((info == None) or (info.uin == 0)) and show(player, 0)):
            Win_EnableWidget(player, 0)

    if (1 == playerMode):
        maskBegin = min((GetValidFriendsCount() - listPos), defPlayerCnt)
        maskEnd = min((listCnt - listPos), defPlayerCnt)
        maskPlayer(maskBegin, maskEnd)
    else:
        maskPlayer(0, 0)



def useExtItem2(ID, playerNum):
    if commodityList.has_key(ID):
        type = commodityList[ID][0]
        idx = commodityList[ID][1]
        picName = ('object/%s/%s%d_stand.img' % (type,
         type,
         idx))
        if ((type == 'namecard') and Win_SetImg((uiSelroomPlayerList + ('.playerInfo%d.namecard' % playerNum)), picName)):
            pass
    else:
        return 



def unUseAllExtItem2(playerNum):
    Win_SetImg((uiSelroomPlayerList + ('.playerInfo%d.namecard' % playerNum)), '')
    Win_SetImg((uiSelroomPlayerList + ('.playerInfo%d.namecardbound' % playerNum)), '')



def myGetPlayerCnt2():
    global friendCnt
    global playerCnt
    global kinMemberCnt
    cnt = GetPlayerCnt(playerMode2)
    if (0 == playerMode2):
        playerCnt = cnt
    elif (1 == playerMode2):
        friendCnt = cnt
    elif (2 == playerMode2):
        kinMemberCnt = cnt
    return cnt



def myGetPlayerPos2():
    if (0 == playerMode2):
        return playerPos2
    elif (1 == playerMode2):
        return friendPos2
    elif (2 == playerMode2):
        return kinMemberPos2



def mySetPlayerPos2(pos):
    global playerPos2
    global friendPos2
    global kinMemberPos2
    if (0 == playerMode2):
        playerPos2 = pos
    elif (1 == playerMode2):
        friendPos2 = pos
    elif (2 == playerMode2):
        kinMemberPos2 = pos



def maskPlayer2(begin, end):
    ui = (uiSelroomPlayerList + '.friendMask')
    x = Win_GetX(ui)
    y = 96
    if (((begin >= end) or (begin < 0)) and Win_SetDrawTexRect(ui, 0, (begin * 24), 330, 0)):
        Win_SetRect((ui + '.tipBtn'), value_channel_winrect, x, (y + (begin * 24)), 330, 0)



def updatePlayer2():

    def myGetPlayerInfo(i, mode):

        def get(i, mode):
            cnt = 0
            if (mode == 0):
                cnt = playerCnt
            elif (1 == mode):
                cnt = friendCnt
            elif (2 == mode):
                cnt = kinMemberCnt
            if (i >= cnt):
                return None
            info = CNil()
            pi = fetch_PlayerInfoInPlayerList(i, mode)
            a = pi.m_PlayerInfo
            gameInfo = a.m_stGameInfo
            info.state = pi.m_nPlayerStatus
            info.isVip = (a.m_dwIdentity & 8)
            info.isgoldDiamond = (a.m_dwIdentity & 8192)
            info.name = a.m_szPlayerNickname.replace('\n', '')
            info.isBoy = (1 == int(a.m_bGender))
            info.level = Level().getInfo(gameInfo.m_dwPoint)
            info.uin = a.m_dwPlayerUin
            info.extItemNum = a.m_bExtItemNum
            info.m_dwKinIndex = a.m_dwKinIndex
            info.m_nKinNameLen = a.m_nKinNameLen
            info.m_szKinName = a.m_szKinName
            info.m_stKinFlagID = a.m_stKinFlagID
            return info


        return get(i, mode)



    def show(player, b):
        Win_ShowWidget((player + '.name'), b)
        Win_ShowWidget((player + '.gender'), b)
        Win_ShowWidget((player + '.levelIcon'), b)
        Win_ShowWidget((player + '.goldDiamond'), b)
        Win_ShowWidget((player + '.kintotem'), b)


    listCnt = myGetPlayerCnt2()
    listPos = myGetPlayerPos2()
    for i in range(11):
        player = ((uiSelroomPlayerList + '.playerInfo') + str((i + 1)))
        if ((i >= defPlayerCnt2) and Win_ShowWidget(player, 0)):
            continue
        unUseAllExtItem2((i + 1))
        info = myGetPlayerInfo((i + listPos), playerMode2)
        if (((info == None) or (info.uin == 0)) and show(player, 0)):
            Win_EnableWidget(player, 0)

    if (1 == playerMode2):
        maskBegin = min((GetValidFriendsCount() - listPos), defPlayerCnt2)
        maskEnd = min((listCnt - listPos), defPlayerCnt2)
        maskPlayer2(maskBegin, maskEnd)
    else:
        maskPlayer2(0, 0)



def myGetRoomCnt():
    return GetRoomCnt()



def updateRoom():
    global roomCnt

    def myGetRoomInfo(i):

        def getFake(i):
            global roomCnt
            roomCnt = 8
            if (i >= roomCnt):
                return None
            info = CNil()
            info.no = 10
            info.logicID = 20
            info.name = 'nameless'
            roomFlag = 0
            info.isStandardRoom = Rand(2)
            info.hasPassword = Rand(2)
            info.time = 3
            info.playerNum = 3
            info.roomMaxPlayerNum = 3
            info.mapName = mapList[1][0]
            return info



        def get(i):
            if (i >= roomCnt):
                return None
            ri = GetRoomInfo(i, GameType)
            info = CNil()
            info.no = ri.sUIRoomID
            info.logicID = ri.shRoomLogicalID
            info.isVip = ri.sIsVIP
            info.name = ri.m_szRoomName
            info.flag = ri.iRoomFlag
            info.isStandardRoom = (0 == ri.iRuleType)
            info.hasPassword = ri.IsRoomLocked
            info.time = 3
            info.playerNum = ri.sPlayerInRoom
            info.roomMaxPlayerNum = ri.sMaxPlayer
            info.mapName = mapID2name(ri.m_nMapID)
            info.mapType = getMapInfo(ri.m_nMapID).type
            return info


        return get(i)


    roomCnt = myGetRoomCnt()
    for i in range(8):
        room = ('UI.selRoom.room' + str((i + 1)))
        info = myGetRoomInfo(i)
        if ((None == info) and Win_ShowWidget(room, False)):
            continue
        Win_ShowWidget(room, True)
        Win_EnableWidget(room, False)
        Win_SetImg(room, 'object/ui/selRoom/dlg_room.img')
        if ((1 == info.flag) and Win_EnableWidget(room, True)):
            pass
        Win_SetText((room + '.no'), ('%03d' % info.no))
        Win_ShowWidget((room + '.vip'), info.isVip)
        if ((0 == info.flag) and Win_SetValue((room + '.logicID'), -1)):
            Win_SetText((room + '.name'), '')
            Win_ShowWidget((room + '.standard'), False)
            Win_ShowWidget((room + '.password'), False)
            Win_SetText((room + '.playerNum'), '')
            Win_SetText((room + '.mapName'), '')
            Win_SetImg((room + '.mapIcon'), '')
            Win_ShowWidget((room + '.vip'), False)
        if ((4 == GameType) and Win_SetText((room + '.name'), '\xc1\xc4\xcc\xec\xca\xd2')):
            Win_SetImg((room + '.mapIcon'), 'res/uires/selRoom/icon/chat.img')




def ui_getPlayerDetail():
    global lookupKinID

    def myGetPlayerDetail():
        info = CNil()
        pi = GetPlayerDetail()
        info.uin = pi.m_dwFriendUin
        info.name = '-'
        info.nickName = pi.m_szPlayerName.replace('\n', '')
        info.isBoy = (1 == int(pi.m_cGender))
        info.m_dwKinIndex = pi.m_dwKinIndex
        info.m_nKinNameLen = pi.m_nKinNameLen
        info.m_stKinFlagID = pi.m_stKinFlagID
        info.m_szKinName = pi.m_szKinName
        info.m_iHonor = pi.m_iHonor
        info.isgoldDiamond = (pi.m_dwIdentity & 8192)
        channelName = stripStr(pi.m_szChannelName)
        sectionName = stripStr(pi.m_szSectionName)
        roomName = stripStr(pi.m_szRoomName)
        areaName = stripStr(pi.m_szZoneName)
        if (areaName == ''):
            areaName = '\xd0\xa1\xc7\xf8'
        roomNO = str(pi.m_sRoomUIID)
        if (roomNO == '0'):
            roomNO = ''
        if (1 == pi.m_bStatus):
            info.state = '\xd4\xda\xcf\xdf'
            info.state += ('\n\xa1\xbe\xc6\xb5\xb5\xc0\xa1\xbf%s(%s)' % (channelName,
             areaName))
            info.state += ('\n\xa1\xbe\xd0\xa1\xc7\xf8\xa1\xbf' + sectionName)
        elif (2 == pi.m_bStatus):
            info.state = '\xd4\xda\xb7\xbf\xbc\xe4\xc4\xda'
            info.state += ('\n\xa1\xbe\xc6\xb5\xb5\xc0\xa1\xbf%s(%s)' % (channelName,
             areaName))
            info.state += ('\n\xa1\xbe\xd0\xa1\xc7\xf8\xa1\xbf' + sectionName)
            info.state += (('\n\xa1\xbe\xb7\xbf\xbc\xe4%s\xa1\xbf' % roomNO) + roomName)
        elif (3 == pi.m_bStatus):
            info.state = '\xd5\xfd\xd4\xda\xd3\xce\xcf\xb7'
            info.state += ('\n\xa1\xbe\xc6\xb5\xb5\xc0\xa1\xbf%s(%s)' % (channelName,
             areaName))
            info.state += ('\n\xa1\xbe\xd0\xa1\xc7\xf8\xa1\xbf' + sectionName)
            info.state += (('\n\xa1\xbe\xb7\xbf\xbc\xe4%s\xa1\xbf' % roomNO) + roomName)
        elif (0 == pi.m_bStatus):
            info.state = '\xb2\xbb\xd4\xda\xcf\xdf'
            info.isBoy = -1
        else:
            info.state = '\xce\xb4\xd6\xaa'
        info.bStatus = ((pi.m_bStatus >= 1) and (pi.m_bStatus <= 3))
        info.isfriend = GetAttribute(pi.m_dwFriendUin, 0)
        gi = pi.m_stGameInfo
        info.winNum = gi.m_nWinNum
        info.loseNum = gi.m_nLossNum
        info.drawNum = gi.m_nEqualNum
        info.point = gi.m_dwPoint
        info.level = Level().getInfo(gi.m_dwPoint)
        info.exp = Level().getExp(gi.m_dwPoint)
        info.expRate = Level().getRate(gi.m_dwPoint)
        info.roleID = gi.m_bRoleID
        print info.level,
        print info.exp,
        print info.expRate
        info.pveWinNum = gi.m_dwExtWinNum
        info.pveLoseNum = gi.m_dwExtLossNum
        info.pveDrawNum = gi.m_dwExtEqualNum
        info.pvePoint = gi.m_dwExtPoint
        info.pveInfo = GetPVEData(info.pvePoint)
        return info



    def myGetPlayerDetailFake():
        info = CNil()
        info.uin = 123456789
        info.name = 'm_szPlayerName'
        info.isBoy = True
        info.winNum = 100
        info.loseNum = 90
        info.point = 998877
        info.level = 100
        return info


    ui = uiPlayerInfoDlg
    if (not Win_IsVisible(ui)):
        return 
    myInfo = GetPlayerInfoByUin(uin)
    myMarriageInfo = GetMyMarriageDetail()
    if (queryingUin == uin):
        marriageInfo = GetMyMarriageDetail()
    else:
        marriageInfo = GetMarriageDetail()
    info = myGetPlayerDetail()
    MeIsBoy = (1 == int(myInfo.m_bGender))
    Win_SetText((ui + '.QQ'), str(info.uin))
    avtUin = int(Win_GetText((ui + '.avtUin')))
    if ((avtUin != info.uin) and Win_SetText((ui + '.avtUin'), '-1')):
        if (((info.isBoy == -1) or info.isBoy) and Win_SetImg((ui + '.avt'), 'res/uiRes/avt_boy.gif')):
            pass
    if ((info.isBoy == -1) and Win_SetText((ui + '.gender'), '_')):
        Win_SetImg((ui + '.genderPic'), '')
    (r1, g1, b1, a1,) = (135,
     249,
     255,
     255)
    (r2, g2, b2, a2,) = memberNameColor
    if (info.isgoldDiamond and Win_SetImg((ui + '.playerDemo.goldDiamond'), 'res/uires/selRoom/goldDiamond.img')):
        Win_SetDrawColor((ui + '.nickName'), r1, g1, b1, a1)
    Win_SetText((ui + '.nickName'), info.nickName)
    Win_SetText((ui + '.state'), info.state)
    if ((marriageInfo.m_dwMarriageUin != 0) and Win_SetText((ui + '.spouseName'), marriageInfo.m_szSpouseNickname)):
        Win_ShowWidget((ui + '.lookupMarriage'), 1)
        Win_ShowWidget((ui + '.spark'), 0)
    lookupKinID = 0
    if (info.m_dwKinIndex != 0):
        lookupKinID = info.m_dwKinIndex
        if (((info.m_stKinFlagID.m_iFlagID >= 0) and (info.m_stKinFlagID.m_iFlagID <= 48)) and Win_SetImg((ui + '.kintotem'), ('object/ui/kinTotem/%03d.img' % (info.m_stKinFlagID.m_iFlagID)))):
            pass
    if ((info.m_nKinNameLen != 0) and Win_SetText((ui + '.kin'), info.m_szKinName)):
        pass
    Win_ShowWidget((ui + '.addFriendBtn'), (not info.isfriend))
    Win_EnableWidget((ui + '.addFriendBtn'), (not (info.uin == uin)))
    Win_ShowWidget((ui + '.deleteFriendBtn'), info.isfriend)
    Win_EnableWidget((ui + '.traceBtn'), (info.bStatus and GetAttribute(info.uin, 0)))
    Win_EnableWidget((ui + '.privateChatBtn'), info.bStatus)
    Win_EnableWidget((ui + '.privateChatBtn'), (not (info.uin == uin)))
    Win_SetDrawTexRect((uiPvpInfoDlg + '.expLine'), 0, 0, ((info.exp * 136) / 100), 12)
    Win_SetText((uiPvpInfoDlg + '.exp'), info.expRate)
    Win_SetText((uiPvpInfoDlg + '.reputation'), str(info.m_iHonor))
    Win_SetText((uiPvpInfoDlg + '.point'), str(info.point))
    Level().setUI(uiPvpInfoDlg, info.level)
    levelname = info.level[0]
    if ((info.level[1] == 25) and (not info.isBoy)):
        levelname = '\xd4\xc2\xc1\xc1\xb9\xab\xd6\xf7'
    elif ((info.level[1] == 26) and (not info.isBoy)):
        levelname = '\xcc\xab\xd1\xf4\xc5\xae\xcd\xf5'
    elif ((info.level[1] == 27) and (not info.isBoy)):
        levelname = '\xd7\xcf\xd7\xea\xc5\xae\xbb\xca'
    Win_SetText((uiPvpInfoDlg + '.level'), levelname)
    Win_SetText((uiPvpInfoDlg + '.success'), ('%d\xca\xa4 %d\xb0\xdc %d\xc6\xbd' % (info.winNum,
     info.loseNum,
     info.drawNum)))
    Win_SetText((uiPveInfoDlg + '.pveLevelLabel'), str(info.pveInfo.m_unLevel))
    Win_SetDrawTexRect((uiPveInfoDlg + '.pveLevel'), 0, 0, ((info.pveInfo.m_unLevel * 118) / 20), 12)
    Win_SetText((uiPveInfoDlg + '.pveCourage'), str(info.pvePoint))
    Win_SetText((uiPveInfoDlg + '.pveLife'), str(info.pveInfo.m_unHp))
    Win_SetDrawTexRect((uiPveInfoDlg + '.pveBomb'), 0, 0, ((info.pveInfo.m_unBombNum * 118) / 8), 12)
    Win_SetDrawTexRect((uiPveInfoDlg + '.pveBombResume'), 0, 0, int((118.0 / (2.0 * (info.pveInfo.m_fBombReSpeed + 0.0001)))), 12)
    Win_SetDrawTexRect((uiPveInfoDlg + '.pvePower'), 0, 0, ((info.pveInfo.m_unBombPow * 118) / 4000), 12)
    Win_SetDrawTexRect((uiPveInfoDlg + '.pveSpeed'), 0, 0, ((info.pveInfo.m_unSpeed * 118) / 8), 12)



def ui_NotifyPlayerUpdate():
    if ((Win_GetCurScreen() == 'selRoom') and updatePlayer()):
        updatePlayer2()



def ui_NotifyRoom():
    if ((Win_GetCurScreen() == 'selRoom') and updateRoom()):
        pass



def isAllowFx_selRoom():
    if Win_IsVisible('UI.SysMsgbox'):
        return False
    elif Win_IsVisible(uiSetupDlg):
        return False
    elif Win_IsVisible('UI.selRoom.pwRoom'):
        return False
    else:
        return True



def go2playerInfo(_uin, isDoFind = 1):
    global queryingUin

    def clearMyUI():
        global lookupKinID
        ui = uiPlayerInfoDlg
        lookupKinID = 0
        if (not Win_IsVisible(ui)):
            return 
        Win_SetText((ui + '.gender'), '')
        Win_SetImg((ui + '.genderPic'), '')
        Win_SetText((ui + '.QQ'), '')
        Win_SetText((ui + '.nickName'), '')
        Win_SetText((ui + '.state'), '')
        Win_SetImg((ui + '.kintotem'), '')
        Win_SetText((ui + '.kin'), '')
        Win_SetDrawTexRect((uiPvpInfoDlg + '.expLine'), 0, 0, 0, 0)
        Win_SetText((uiPvpInfoDlg + '.exp'), '')
        Win_SetText((uiPvpInfoDlg + '.reputation'), '')
        Win_SetText((uiPvpInfoDlg + '.point'), '')
        Level().clearUI(uiPvpInfoDlg)
        Win_SetText((uiPvpInfoDlg + '.level'), '')
        Win_SetText((uiPvpInfoDlg + '.success'), '')
        Win_SetText((uiPveInfoDlg + '.pveLevelLabel'), '')
        Win_SetDrawTexRect((uiPveInfoDlg + '.pveLevel'), 0, 0, 0, 0)
        Win_SetDrawTexRect((uiPveInfoDlg + '.pveCourage'), 0, 0, 0, 0)
        Win_SetDrawTexRect((uiPveInfoDlg + '.pveLife'), 0, 0, 0, 0)
        Win_SetDrawTexRect((uiPveInfoDlg + '.pveBomb'), 0, 0, 0, 0)
        Win_SetDrawTexRect((uiPveInfoDlg + '.pveBombResume'), 0, 0, 0, 0)
        Win_SetDrawTexRect((uiPveInfoDlg + '.pvePower'), 0, 0, 0, 0)
        Win_SetDrawTexRect((uiPveInfoDlg + '.pveSpeed'), 0, 0, 0, 0)
        ui += '.playerDemo'
        Win_SetImg((ui + '.bg'), '')
        Win_SetImg((ui + '.enter'), '')
        Win_SetImg((ui + '.frame'), '')


    queryingUin = _uin
    ui_setCapture(uiPlayerInfoDlg)
    clearMyUI()
    PlaySound(soundUI, 1)
    if (isDoFind and FindFriend(_uin)):
        pass


class TopkinList:
    __module__ = __name__

    def getCnt(this):
        global TopkinCnt
        TopkinCnt = 10
        return TopkinCnt



    def __get(this, i):
        info = CNil()
        kinobject = fetch_topkininfolist(chinatelecom, setreputation, i)
        kinname = kinobject.m_szName
        kinname = kinname.replace('\n', '')
        kinname = kinname.replace("'", "\\'")
        info.kinindex = kinobject.m_dwKinIndex
        info.name = kinname
        info.value = kinobject.m_iValue
        info.order = kinobject.m_nOrder
        info.ascend = kinobject.m_nAscend
        return info



    def at(this, Idx):
        if (Idx >= TopkinCnt):
            return None
        return this._TopkinList__get(Idx)




def ui_updateMykinintop():
    Win_SetText((uitopKinDlg + '.topkin7.kinName'), '')
    Win_SetText((uitopKinDlg + '.topkin7.value'), '')
    Win_SetText((uitopKinDlg + '.topkin7.Order'), '')
    Win_SetImg((uitopKinDlg + '.topkin7.isAscend'), '')
    Win_SetText((uitopKinDlg + '.topkin8.kinName'), '')
    Win_SetText((uitopKinDlg + '.topkin8.value'), '')
    Win_SetText((uitopKinDlg + '.topkin8.Order'), '')
    Win_SetImg((uitopKinDlg + '.topkin8.isAscend'), '')
    info = CNil()
    kinobject = fetch_topkininfolist(chinatelecom, setreputation, 10)
    kinname = kinobject.m_szName
    kinname = kinname.replace('\n', '')
    kinname = kinname.replace("'", "\\'")
    info.kinindex = kinobject.m_dwKinIndex
    info.name = kinname
    info.value = kinobject.m_iValue
    info.order = kinobject.m_nOrder
    info.ascend = kinobject.m_nAscend
    Win_SetText((uitopKinDlg + '.topkin7.kinName'), info.name)
    if (kinobject.m_dwKinIndex == 0):
        info.value = ''
    Win_SetText((uitopKinDlg + '.topkin7.value'), str(info.value))
    Win_SetText((uitopKinDlg + '.topkin7.Order'), str(info.order))
    if ((kinobject.m_dwKinIndex == 0) and Win_SetImg((uitopKinDlg + '.topkin7.isAscend'), '')):
        pass
    kinobject = fetch_topkininfolist(chinatelecom, setreputation, 11)
    kinname = kinobject.m_szName
    kinname = kinname.replace('\n', '')
    kinname = kinname.replace("'", "\\'")
    info.kinindex = kinobject.m_dwKinIndex
    info.name = kinname
    info.value = kinobject.m_iValue
    info.order = kinobject.m_nOrder
    info.ascend = kinobject.m_nAscend
    Win_SetText((uitopKinDlg + '.topkin8.kinName'), info.name)
    if (kinobject.m_dwKinIndex == 0):
        info.value = ''
    Win_SetText((uitopKinDlg + '.topkin8.value'), str(info.value))
    Win_SetText((uitopKinDlg + '.topkin8.Order'), str(info.order))
    if ((kinobject.m_dwKinIndex == 0) and Win_SetImg((uitopKinDlg + '.topkin8.isAscend'), '')):
        pass



def ui_updateTopkinList():
    global ActivetopkinPos
    global TopkinCurrentPos
    ShowCnt = TopkinList().getCnt()
    TopKinCnt = TopkinList().getCnt()
    ActivetopkinPos = 999999
    TopkinCurrentPos = min(TopkinCurrentPos, (ShowCnt - defTopkinDlgCnt))
    TopkinCurrentPos = max(TopkinCurrentPos, 0)
    for i in range(defTopkinDlgCnt):
        ui = (uitopKinDlg + ('.topkin%d' % i))
        Win_SetText((ui + '.kinName'), '')
        Win_SetText((ui + '.value'), '')
        Win_SetImg((ui + '.Order'), '')
        idx = (TopkinCurrentPos + i)
        Win_SetCheck(ui, 0)
        if ((idx >= ShowCnt) and Win_SetText((ui + '.kinNmae'), '')):
            Win_SetText((ui + '.value'), '')
            Win_SetImg((ui + '.Order'), '')
            Win_EnableWidget(ui, 0)
            continue

    ui_updateMykinintop()
    ui_setCapture(uitopKinDlg)



def InitGameType():
    if ((GameType == 0) and Win_SelectSelf('UI.selRoom.modeCompete')):
        Win_SelectSelf('UI.selRoom.modeCompete.modeNoItem')
        Win_ShowWidget('UI.selRoom.modeCompete.modeNoItem', 1)
        Win_ShowWidget('UI.selRoom.modeCompete.modeItem', 1)
        doUI('UI.selRoom.modeCompete.modeNoItem', 'OnClick')



def UpdatePetInfo():
    global curPetState
    global curPetId
    global skillIdList
    global petsIdList
    global curPetName
    global baseSkillIdList

    def Clear():
        Win_SetText((uiPetPan + '.petPreview'), '')
        Win_SetImg((uiPetPan + '.petPreview'), '')
        Win_SetImg((uiPetPan + '.petFace'), '')
        Win_SetText((uiPetPan + '.nameEdit'), '')
        Win_SetText((uiPetPan + '.level'), '')
        Win_EnableWidget((uiPetPan + '.freePetBtn'), 1)
        Win_EnableWidget((uiPetPan + '.changeNameBtn'), 1)
        Win_EnableWidget((uiPetPan + '.adoptPetBtn'), 1)
        Win_EnableWidget((uiPetPan + '.petStateBtn'), 1)
        Win_EnableWidget((uiPetPan + '.nameEdit'), 1)
        Win_EnableWidget((uiPetPan + '.raisePetBtn'), 1)
        Win_EnableWidget((uiPetPan + '.left'), 1)
        Win_EnableWidget((uiPetPan + '.right'), 1)
        for i in range(3):
            Win_SetText((uiPetPan + ('.baseSkillDlg.skill%d' % i)), '')

        for i in range(10):
            Win_SetText((uiPetPan + ('.skillDlg.skill%d' % i)), '')




    def ShowEmptyPan():
        Win_SetText((uiPetPan + '.petPreview'), '    \xc4\xfa\xb5\xb1\xc7\xb0\xbb\xb9\xc3\xbb\xd3\xd0\xb3\xe8\xce\xef\xb1\xa6\xb1\xa6,\xc8\xe7\xb9\xfb\xc4\xfa\xd2\xd1\xd3\xd0\xb3\xe8\xce\xef\xbf\xa8\xc5\xc6\xc7\xeb\xb4\xf2\xbf\xaa\xb3\xe8\xce\xef\xb1\xb3\xb0\xfc\xa3\xac\xb5\xe3\xbb\xf7\xd3\xd2\xbc\xfc\xd5\xd9\xbb\xbd\xb3\xf6\xc4\xfa\xb5\xc4\xb3\xe8\xce\xef\xb1\xa6\xb1\xa6\xa3\xa1 ')
        Win_SetImg((uiPetPan + '.petPreview'), '')
        Win_SetImg((uiPetPan + '.petFace'), '')
        Win_SetText((uiPetPan + '.nameEdit'), '')
        Win_SetText((uiPetPan + '.level'), '')
        Win_EnableWidget((uiPetPan + '.freePetBtn'), 0)
        Win_EnableWidget((uiPetPan + '.changeNameBtn'), 0)
        Win_EnableWidget((uiPetPan + '.adoptPetBtn'), 1)
        Win_EnableWidget((uiPetPan + '.petStateBtn'), 0)
        Win_EnableWidget((uiPetPan + '.nameEdit'), 0)
        Win_EnableWidget((uiPetPan + '.raisePetBtn'), 1)
        Win_ShowWidget((uiPetPan + '.foodDlg'), 1)
        Win_EnableWidget((uiPetPan + '.left'), 0)
        Win_EnableWidget((uiPetPan + '.right'), 0)
        Win_SetDrawTexRect((uiPetPan + '.expLine'), 0, 0, 0, 12)
        Win_SetText((uiPetPan + '.expValue'), '0 / 0')
        Win_SetDrawTexRect((uiPetPan + '.loyaltyLine'), 0, 0, 0, 12)
        Win_SetText((uiPetPan + '.loyaltyValue'), '0 / 0')
        UpdatePetItemUi()
        for i in range(3):
            Win_SetText((uiPetPan + ('.baseSkillDlg.skill%d' % i)), '')

        for i in range(10):
            Win_SetText((uiPetPan + ('.skillDlg.skill%d' % i)), '')



    Clear()
    petsIdList = GetPlayerAllPetsId()
    if (len(petsIdList) == 0):
        curPetId = 0
        ShowEmptyPan()
        return False
    if (curPetId == 0):
        petInfo = GetCurActivePetInfo()
    else:
        petInfo = GetPetBaseInfo(curPetId)
        if (petInfo.m_dwPetId == 0):
            petInfo = GetCurActivePetInfo()
    if (petInfo.m_dwPetId == 0):
        curPetId = 0
        ShowEmptyPan()
        return False
    curPetId = petInfo.m_dwPetId
    petResId = GetPetResId(petInfo.m_dwPetTypeId, petInfo.m_wPetLevel)
    Win_SetImg((uiPetPan + '.petPreview'), ('object/pet/pet%d_stand.img' % petResId))
    Win_SetText((uiPetPan + '.petPreview'), '')
    if (petInfo.m_wPetMood >= 90):
        moodUiId = 4
    elif ((petInfo.m_wPetMood >= 60) and (petInfo.m_wPetMood < 90)):
        moodUiId = 3
    elif ((petInfo.m_wPetMood >= 40) and (petInfo.m_wPetMood < 60)):
        moodUiId = 2
    elif ((petInfo.m_wPetMood >= 10) and (petInfo.m_wPetMood < 40)):
        moodUiId = 1
    else:
        moodUiId = 0
    Win_SetImg((uiPetPan + '.petFace'), ('object/ui/pet/face%d.img' % moodUiId))
    Win_SetText((uiPetPan + '.nameEdit'), petInfo.m_szPetName)
    curPetName = petInfo.m_szPetName
    Win_SetText((uiPetPan + '.level'), ('%d \xbc\xb6' % petInfo.m_wPetLevel))
    petLevelRateInfo = GetPetLevelRateInfo(petInfo.m_dwPetExperience)
    Win_SetDrawTexRect((uiPetPan + '.expLine'), 0, 0, int((petLevelRateInfo.m_fRate * 94)), 12)
    Win_SetText((uiPetPan + '.expValue'), ('%d/%d' % (petInfo.m_dwPetExperience,
     petLevelRateInfo.m_unNextLevelExp)))
    Win_SetDrawTexRect((uiPetPan + '.loyaltyLine'), 0, 0, int(((petInfo.m_dwPetLoyalty / 1000.0) * 94)), 12)
    Win_SetText((uiPetPan + '.loyaltyValue'), ('%d/1000' % petInfo.m_dwPetLoyalty))
    curPetState = petInfo.m_wPetState
    if ((petInfo.m_wPetState == 1) and Win_EnableWidget((uiPetPan + '.petStateBtn'), 1)):
        Win_SetImg((uiPetPan + '.petStateBtn'), 'object/ui/pet/btn_stop_take.img')
    skillIdList = []
    baseSkillIdList = []
    for idx in range(petInfo.m_dwSkillCount):
        id = ord(petInfo.m_szSkills[idx])
        if (CHECK_BASESKILL(id) and baseSkillIdList.append(id)):
            pass

    baseSkillIdList.sort()
    skillIdList.sort()
    index = 0
    for skillId in baseSkillIdList:
        name = GetSkillNameById(skillId)
        Win_SetText((uiPetPan + ('.baseSkillDlg.skill%d' % index)), name)
        index += 1

    index = 0
    for skillId in skillIdList:
        name = GetSkillNameById(skillId)
        Win_SetText((uiPetPan + ('.skillDlg.skill%d' % index)), name)
        index += 1

    return True



def UpdatePetItemUi():
    global petItemList
    global petItemPos

    def PetItemSort(x, y):
        return (y.m_nItemID - x.m_nItemID)


    petItemList = GetAllMyPetItems()
    if petItemList.sort(PetItemSort):
        totalItem = len(petItemList)
        if (petItemPos >= totalItem):
            petItemPos -= defPetItemCnt
            if (petItemPos < 0):
                petItemPos = 0
        totalPage = 1
        curPage = 1
        if ((totalItem > 0) and ((totalItem % defPetItemCnt) == 0)):
            totalPage = (totalItem / defPetItemCnt)
        curPage = ((petItemPos / defPetItemCnt) + 1)
    Win_SetText((uiPetPan + '.foodDlg.petItemPage'), ('%d/%d' % (curPage,
     totalPage)))
    for i in range(defPetItemCnt):
        if (((petItemPos + i) >= totalItem) and Win_SetImg((uiPetPan + ('.foodDlg.petItem%d.itemPic' % i)), '')):
            Win_SetText((uiPetPan + ('.foodDlg.petItem%d.itemNum' % i)), '')




def ShowPetInfoDlg(petInfo):
    global skillIdList
    global baseSkillIdList

    def Clear():
        Win_SetImg((uiPetPan + '.petPreview'), '')
        Win_SetText((uiPetPan + '.petPreview'), '')
        Win_SetImg((uiPetPan + '.petFace'), '')
        Win_SetText((uiPetPan + '.nameEdit'), '')
        Win_SetText((uiPetPan + '.level'), '')
        Win_EnableWidget((uiPetPan + '.freePetBtn'), 0)
        Win_EnableWidget((uiPetPan + '.changeNameBtn'), 0)
        Win_EnableWidget((uiPetPan + '.adoptPetBtn'), 0)
        Win_EnableWidget((uiPetPan + '.petStateBtn'), 0)
        Win_EnableWidget((uiPetPan + '.nameEdit'), 0)
        Win_EnableWidget((uiPetPan + '.raisePetBtn'), 0)
        Win_ShowWidget((uiPetPan + '.foodDlg'), 0)
        Win_EnableWidget((uiPetPan + '.left'), 0)
        Win_EnableWidget((uiPetPan + '.right'), 0)
        for i in range(3):
            Win_SetText((uiPetPan + ('.baseSkillDlg.skill%d' % i)), '')

        for i in range(10):
            Win_SetText((uiPetPan + ('.skillDlg.skill%d' % i)), '')



    Clear()
    petResId = GetPetResId(petInfo.m_dwPetTypeId, petInfo.m_wPetLevel)
    Win_SetImg((uiPetPan + '.petPreview'), ('object/pet/pet%d_stand.img' % petResId))
    Win_SetText((uiPetPan + '.petPreview'), '')
    if (petInfo.m_wPetMood >= 90):
        moodUiId = 4
    elif ((petInfo.m_wPetMood >= 60) and (petInfo.m_wPetMood < 90)):
        moodUiId = 3
    elif ((petInfo.m_wPetMood >= 40) and (petInfo.m_wPetMood < 60)):
        moodUiId = 2
    elif ((petInfo.m_wPetMood >= 10) and (petInfo.m_wPetMood < 40)):
        moodUiId = 1
    else:
        moodUiId = 0
    Win_SetImg((uiPetPan + '.petFace'), ('object/ui/pet/face%d.img' % moodUiId))
    Win_SetText((uiPetPan + '.nameEdit'), petInfo.m_szPetName)
    curPetName = petInfo.m_szPetName
    Win_SetText((uiPetPan + '.level'), ('%d \xbc\xb6' % petInfo.m_wPetLevel))
    petLevelRateInfo = GetPetLevelRateInfo(petInfo.m_dwPetExperience)
    Win_SetDrawTexRect((uiPetPan + '.expLine'), 0, 0, int((petLevelRateInfo.m_fRate * 94)), 12)
    Win_SetText((uiPetPan + '.expValue'), ('%d/%d' % (petInfo.m_dwPetExperience,
     petLevelRateInfo.m_unNextLevelExp)))
    Win_SetDrawTexRect((uiPetPan + '.loyaltyLine'), 0, 0, int(((petInfo.m_dwPetLoyalty / 1000.0) * 94)), 12)
    Win_SetText((uiPetPan + '.loyaltyValue'), ('%d/1000' % petInfo.m_dwPetLoyalty))
    skillIdList = []
    baseSkillIdList = []
    for idx in range(petInfo.m_dwSkillCount):
        id = ord(petInfo.m_szSkills[idx])
        if (CHECK_BASESKILL(id) and baseSkillIdList.append(id)):
            pass

    baseSkillIdList.sort()
    skillIdList.sort()
    index = 0
    for skillId in baseSkillIdList:
        name = GetSkillNameById(skillId)
        Win_SetText((uiPetPan + ('.baseSkillDlg.skill%d' % index)), name)
        index += 1

    index = 0
    for skillId in skillIdList:
        name = GetSkillNameById(skillId)
        Win_SetText((uiPetPan + ('.skillDlg.skill%d' % index)), name)
        index += 1

    Win_ShowWidget((uiPetPan + '.baseSkillDlg'), 1)
    Win_ShowWidget((uiPetPan + '.skillDlg'), 1)
    Win_ShowWidget(uiPetPan, 1)
    ui_setCapture(uiPetPan)


class PawnTypeList:
    __module__ = __name__
    items = []

    def clear(this):
        global PawnTypeCnt
        PawnTypeList.items = []
        PawnTypeCnt = 0



    def update(this):
        global PawnTypeCnt
        PawnTypeList.items = GetPawnTypeList()
        PawnTypeCnt = len(PawnTypeList.items)
        return PawnTypeCnt



    def at(this, itemIdx):
        if (itemIdx >= len(PawnTypeList.items)):
            return None
        return PawnTypeList.items[itemIdx]



g_PawnTypeList = PawnTypeList()
class PawnItemList:
    __module__ = __name__
    items = []

    def clear(this):
        global PawnItemCnt
        PawnItemList.items = []
        PawnItemCnt = 0



    def update(this):
        global PawnItemCnt
        PawnItemList.items = GetPawnItemList((CurrenPawnType + 1))
        PawnItemCnt = len(PawnItemList.items)
        return PawnItemCnt



    def at(this, itemIdx):
        if (itemIdx >= len(PawnItemList.items)):
            return None
        return PawnItemList.items[itemIdx]



g_PawnItemList = PawnItemList()
class PawnGoodsList:
    __module__ = __name__
    items = []

    def clear(this):
        global PawnGoodsCnt
        PawnGoodsList.items = []
        PawnGoodsCnt = 0



    def update(this):
        global PawnGoodsCnt
        PawnGoodsList.items = GetPawnGoodsListbyID(CurrentPawnItemID)
        PawnGoodsCnt = len(PawnGoodsList.items)
        return PawnGoodsCnt



    def at(this, itemIdx):
        if (itemIdx >= len(PawnGoodsList.items)):
            return None
        return PawnGoodsList.items[itemIdx]



g_PawnGoodsList = PawnGoodsList()
class MyPawnItemList:
    __module__ = __name__
    items = []

    def clear(this):
        global MyPawnItemListCnt
        MyPawnItemList.items = []
        MyPawnItemListCnt = 0



    def update(this):
        global MyPawnItemListCnt
        MyPawnItemList.items = GetMyPawnItemList()
        MyPawnItemListCnt = len(MyPawnItemList.items)
        return MyPawnItemListCnt



    def at(this, itemIdx):
        if (itemIdx >= len(MyPawnItemList.items)):
            return None
        return MyPawnItemList.items[itemIdx]



g_MyPawnItemList = MyPawnItemList()

def ClearWareList():
    for i in range(defPawnwareCnt):
        ui = (uiPawnShopDlg + ('.ware%d' % (i + 1)))
        Win_EnableWidget(ui, 1)
        Win_SetText((ui + '.name'), '')
        Win_SetText((ui + '.price1'), '')
        Win_SetText((ui + '.price'), '')
        Win_SetImg((ui + '.picture'), '')
        Win_SetText((ui + '.ID'), '')
        Win_SetText((ui + '.saleIndex'), '')
        Win_SetImg((ui + '.memberPic'), '')
        Win_SetText((ui + '.Num'), '')
        Win_SetText((ui + '.dstUin'), '')
        Win_SetImg((ui + '.PetInfo'), '')
        Win_SetImg((ui + '.buyBtn'), '')
        Win_EnableWidget((ui + '.petInfo'), 0)
        Win_EnableWidget((ui + '.buyBtn'), 0)

    Win_SetText((uiPawnShopDlg + '.PawnGoodsPage'), '')



def ui_updatePawnTypeList():
    global PawnTypeCnt
    global CurrenPawnType
    print 'ui_updatePawnTypeList begin'
    CurrenPawnType = -1
    PawnTypeCnt = 0
    g_PawnItemList.clear()
    g_PawnTypeList.clear()
    g_PawnTypeList.update()
    print ('[ui_updatePawnTypeList]PawnTypeCnt=%d' % PawnTypeCnt)
    Win_SetText((uiPawnShopDlg + '.SearchPropName'), '')
    Win_SetText((uiPawnShopDlg + '.Rank'), '')
    Win_ShowWidget((uiPawnShopDlg + '.CommitPanel'), 0)
    ClearWareList()
    print ('PawnTypeCnt = %d' % PawnTypeCnt)
    Win_SetPos((uiPawnShopDlg + '.itemScroll'), 0)
    doUI((uiPawnShopDlg + '.itemScroll'), 'OnPosChange')



def ui_updatePawnGoodsList(CurrentPos, TotalCount):
    global totalPawnGoodsCnt
    global PawnGoodsPos
    global bPawnShopShow
    PawnItemCnt = 0
    bPawnShopShow = 1
    totalPawnGoodsCnt = TotalCount
    PawnGoodsPos = CurrentPos
    g_PawnGoodsList.clear()
    g_PawnGoodsList.update()
    print ('PawnGoodsCnt = %d' % PawnGoodsCnt)
    Win_SetPos((uiPawnShopDlg + '.wareScroll'), 0)
    doUI((uiPawnShopDlg + '.wareScroll'), 'OnPosChange')
    ui_UpdatePawnGoods()



def ui_ShowMyPawnedInWare(currentPos):
    global PawnGoodsCnt
    global totalPawnGoodsCnt
    global MyPawnItemListCnt
    global PawnGoodsPos
    global bPawnShopShow
    bPawnShopShow = 1
    g_MyPawnItemList.clear()
    PawnGoodsPos = currentPos
    MyPawnItemListCnt = g_MyPawnItemList.update()
    totalPawnGoodsCnt = MyPawnItemListCnt
    if (MyPawnItemListCnt > defPawnGoodsCnt):
        PawnGoodsCnt = defPawnGoodsCnt
    else:
        PawnGoodsCnt = MyPawnItemListCnt
    print ('[ui_ShowMyPawnedInWare]totalPawnGoodsCnt = %d,PawnGoodsCnt = %d' % (totalPawnGoodsCnt,
     PawnGoodsCnt))
    print ('[ui_ShowMyPawnedInWare] PawnGoodsPos= %d' % PawnGoodsPos)
    Win_SetPos((uiPawnShopDlg + '.wareScroll'), 0)
    doUI((uiPawnShopDlg + '.wareScroll'), 'OnPosChange')
    ui_UpdatePawnGoods()



def ui_updateMyPawnedInWare(currentPos):
    if (Win_IsChecked((uiPawnShopDlg + '.pawnedBtn')) and ClearWareList()):
        ui_ShowMyPawnedInWare(currentPos)



def ui_UpdatePawnGoods():
    print ('[ui_UpdatePawnGoods]totalPawnGoodsCnt = %d,PawnGoodsCnt = %d' % (totalPawnGoodsCnt,
     PawnGoodsCnt))
    if ((totalPawnGoodsCnt == 0) and Win_SetText((uiPawnShopDlg + '.PawnGoodsPage'), '1/1')):
        pass
    for i in range(defPawnGoodsCnt):
        ui = (uiPawnShopDlg + ('.ware%d' % (i + 1)))
        idx = (i + PawnGoodsPos)
        if (idx >= totalPawnGoodsCnt):
            continue




def updateMyStorageInPawn():
    g_MyDealStorageList.clear()
    g_MyDealStorageList.update()
    print ('[updateMyStorageInPawn] MyDealStorageListCnt = %d' % MyDealStorageListCnt)
    Win_SetPos((uiPawnShopDlg + '.CommitPanel.StorageScroll'), 0)
    doUI((uiPawnShopDlg + '.CommitPanel.StorageScroll'), 'OnPosChange')
    residualTicket = GetMyBill()
    print residualTicket
    Win_SetText((uiPawnShopDlg + '.residualBill'), ('%12f' % residualTicket))



def ui_updateCommitBox():
    g_MyPawnItemList.clear()
    g_MyPawnItemList.update()
    for i in range(defCommittedCnt):
        ui = (uiPawnShopDlg + ('.CommitPanel.CommittedItem%d' % i))
        Win_SetText((ui + '.PropName'), '')
        Win_SetText((ui + '.PropNum'), '')
        Win_SetText((ui + '.interval'), '')
        Win_SetText((ui + '.price'), '')
        Win_ShowWidget(ui, 0)

    Win_SetPos((uiPawnShopDlg + '.CommitPanel.CommittedScroll'), 0)
    doUI((uiPawnShopDlg + '.CommitPanel.CommittedScroll'), 'OnPosChange')



def updateCurrentPropID(PropID):
    global CurrentPawnItemID
    CurrentPawnItemID = PropID



def Responsepawnpetinfo():
    global petbaseInfo
    petbaseInfo = GetPawnPetInfo()
    if ((petbaseInfo.m_dwPetTypeId > 0) and ShowPetInfoDlg(petbaseInfo)):
        pass



def ui_SetGameType(gameType):
    global GameType
    global OldGameType
    SetGameType(gameType)
    OldGameType = GameType
    GameType = gameType



def NewPlayerPractice():
    ui = 'UI.selRoom.practiceBtn'
    doUI(ui, 'OnClick')
    Win_ShowWidget('UI.newPlayerDirectionDlg', 1)


class UI_children_selRoom:
    __module__ = __name__
    type = 'SCREEN'
    rect = (0,
     0,
     800,
     600)
    bkimage = 'object/ui/bg/bg_selRoom.img'
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
     ('OnAccel_OnF4',
      115,
      0,
      0,
      0),
     ('OnAccel_OnF7',
      118,
      0,
      0,
      0))

    def OnAccel_OnF1():
        ui_jumpHelpWeb()
        PlaySound(soundMain, 1)



    def OnAccel_OnF2():
        if ((isAllowFx_selRoom() and (not Win_IsVisible(uiTaskSelDlg))) and doUI('UI.selRoom.fastJoinRoomBtn', 'OnClick')):
            pass



    def OnAccel_OnF4():
        if (isAllowFx_selRoom() and doUI('UI.selRoom.shopBtn', 'OnClick')):
            pass



    def OnAccel_OnF7():
        if ((isAllowFx_selRoom() and (not Win_IsVisible(uiTaskSelDlg))) and doUI('UI.selRoom.newRoomBtn', 'OnClick')):
            pass



    def OnEnter():
        if (Win_IsVisible('UI.selRoom.pwRoom') and doUI('UI.selRoom.pwRoom.confirm', 'OnClick')):
            return 
        doUI('UI.selRoom.chatArea.sendBtn', 'OnClick')



    def OnEscape():
        if Win_IsVisible('UI.selRoom.pwRoom'):
            return 
        doUI('UI.selRoom.leaveBtn', 'OnClick')



    def OnInit():
        global isQQMember
        global localShopVersion
        global ChatAreaTab
        global playerPos
        global playerMode2
        global playerMode
        global markEnterShop
        global practiceMode
        global playerPos2
        global firstEnter
        global lastestShopVersion
        global isLeague
        global bPawnShopShow
        global isShowTaskSelDlg
        Win_ShowWidget(uiMarriageConfirmDlg, 0)
        bPawnShopShow = 0
        if markEnterShop:
            markEnterShop = False
            SC_ClickShopBtn()
            go2shop()
            return 
        if ((GameType == ChatType) and Win_ShowWidget('UI.selRoom.mapFilterMask', 1)):
            pass
        Win_ShowWidget(uiGuideBar, 1)
        Win_EnableWidget(uiGuideBar, 1)
        Win_ShowWidget(uiSocialityDlg, 0)
        sc_HideWeb('kinMatch')
        sc_HideWeb('kinTeam')
        Win_ShowWidget(uiMenuDlg, 0)
        initAllUse()
        Win_ShowWidget('UI.selRoom.chatArea.speakerTip', 0)
        if firstEnter:
            localShopVersion = GetLocalShopVertion(uin)
            lastestShopVersion = GetLastShopVertion()
        if ((localShopVersion < lastestShopVersion) and Win_ShowWidget('UI.selRoom.tipShop', 1)):
            pass
        identity = fetch_PlayerIdentityByUin(uin)
        isLeague = (identity & 8192)
        isQQMember = (identity & 32)
        ChatAreaTab = 0
        setupValidGameMode()
        if firstEnter:
            firstEnter = 0
            KeyLayout().restore()
        PlayMusic(musicDirAndSection, -1)
        if (isMemberFace and setFacePage(0, memberFacePageNum)):
            pass
        playerMode = 0
        playerPos = 0
        updatePlayer()
        flexChatArea(flexMode)
        playerMode2 = 0
        Win_SelectSelf('UI.selRoom.playerTab')
        playerPos2 = 0
        updatePlayer2()
        InitGameType()
        updateRoom()
        Win_SetCheck('UI.selRoom.roomState', True)
        Win_SetText('UI.selRoom.name', Sect().getName())
        Win_SetFocus('UI.selRoom.chatArea.chatEdit')
        Win_SetImg('UI.selRoom.mapFilterBtn.icon', ('map/icon/%s.img' % gameModeList[1][1]))
        Win_SetText('UI.selRoom.mapFilterBtn.text', gameModeList[1][2])
        InitSpeaker()
        InitChatArea()
        InitChatMode()
        if ((GetLeaveWordCount() > 0) and startGlint()):
            pass
        screenStartIn()
        if (practiceMode and Win_ShowWidget(uiTaskSelDlg, 1)):
            ui_setCapture(uiTaskSelDlg)
            practiceMode = 0
        if ((chinatelecom == 1) and Win_SetCheck((uitopKinDlg + '.unicomBtn'), 0)):
            Win_SetCheck((uitopKinDlg + '.telecomBtn'), 1)
        if ((setreputation == 1) and Win_ShowWidget((uitopKinDlg + '.activity'), 0)):
            Win_SetCheck((uitopKinDlg + '.honorBtn'), 1)
            Win_SetCheck((uitopKinDlg + '.activityBtn'), 0)
        if ((chIdx == 1) and (isShowTaskSelDlg == 0)):
            isShowTaskSelDlg = 1
            ui_setCapture(uiTaskSelDlg)
            PlaySound(soundMain, 1)
        SC_SetBeGuide(Sect().meGetPoint(), 0)



    def OnDenit():
        Win_ShowWidget(uiC2CInviteDlg, False)
        Win_Timer('UI.selRoom.chatArea.speakerTip', 0)
        Win_ShowWidget('UI.selRoom.chatArea.speakerTip', False)
        doUI((uiPawnShopDlg + '.crossBtn'), 'OnClick')
        Win_ShowWidget('UI.selRoom.practiceBtn', 1)
        Win_ShowWidget('UI.selRoom.fastJoinRoomBtn', 1)
        Win_ShowWidget('UI.selRoom.newRoomBtn', 1)


    class children:
        __module__ = __name__
        class name(TLabel,
         Static):
            __module__ = __name__
            rect = (36,
             562,
             200,
             12)
            drawcolor = lightColor
            textEdgeColor = (66,
             95,
             133,
             255)
            textEdgeType = 1

        class modeCompete(TTabWin):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)
            hotrect = (20,
             39,
             98,
             30)
            groupid = 1
            groupstop = 0
            hotcover = 'object/ui/selRoom/tab_compete.img'

            def OnClick(this):
                Win_ShowWidget('UI.selRoom.mapFilterMask', 0)
                Win_ShowWidget((this + '.modeNoItem'), 1)
                Win_ShowWidget((this + '.modeItem'), 1)
                Win_ShowWidget('UI.selRoom.mapFilterBtn', 1)
                Win_SelectSelf('UI.selRoom.modeCompete.modeNoItem')
                doUI('UI.selRoom.modeCompete.modeNoItem', 'OnClick')


            class children:
                __module__ = __name__
                class modeNoItem(TTabWin):
                    __module__ = __name__
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (30,
                     70,
                     57,
                     25)
                    hotcover = 'object/ui/selRoom/tab_noItem.img'
                    groupid = 2
                    groupstop = 0

                    def OnClick(this):
                        ui_SetGameType(CommonType)
                        NotifyRoom(CommonType)



                class modeItem(TTabWin):
                    __module__ = __name__
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (94,
                     70,
                     57,
                     25)
                    hotcover = 'object/ui/selRoom/tab_item.img'
                    groupid = 2
                    groupstop = 1

                    def OnClick(this):
                        ui_SetGameType(PVPType)
                        NotifyRoom(PVPType)



                class modeHonor(TTabWin):
                    __module__ = __name__
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (158,
                     70,
                     57,
                     25)
                    hotcover = 'object/ui/selRoom/tab_honor.img'
                    groupid = 2
                    groupstop = 2

                    def OnClick(this):
                        ui_SetGameType(LootType)
                        NotifyRoom(LootType)





        class modeExplore(TTabWin):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)
            hotrect = (122,
             39,
             98,
             30)
            groupid = 1
            groupstop = 1
            hotcover = 'object/ui/selRoom/tab_explore.img'

            def OnClick(this):
                Win_ShowWidget('UI.selRoom.mapFilterMask', 0)
                Win_ShowWidget('UI.selRoom.modeCompete.modeNoItem', 0)
                Win_ShowWidget('UI.selRoom.modeCompete.modeItem', 0)
                Win_ShowWidget('UI.selRoom.mapFilterBtn', 1)
                ui_SetGameType(PVEType)
                print ('behind %d,%d' % (OldGameType,
                 GameType))
                updateRoom()



        class modeChat(TTabWin):
            __module__ = __name__
            rect = (0,
             0,
             1,
             1)
            hotrect = (224,
             39,
             98,
             30)
            groupid = 1
            groupstop = 2
            hotcover = 'object/ui/selRoom/tab_chat.img'

            def OnClick(this):
                Win_ShowWidget('UI.selRoom.modeCompete.modeNoItem', 0)
                Win_ShowWidget('UI.selRoom.modeCompete.modeItem', 0)
                Win_ShowWidget('UI.selRoom.mapFilterMask', 1)
                Win_ShowWidget('UI.selRoom.mapFliterBtn', 0)
                ui_SetGameType(ChatType)
                NotifyRoom(ChatType)



        class room1(TButton):
            __module__ = __name__
            framescheme = [(1,
              1,
              1,
              1,
              2,
              2,
              0,
              0)]
            rect = (27,
             101,
             181,
             111)
            bkimage = 'object/ui/selRoom/dlg_room.img'

            def OnClick(this):
                global roomID
                me = Win_GetFocusPath()
                print '<enter room>',
                print me,
                roomID = int(Win_GetValue((me + '.logicID')))
                print '<room>=',
                print roomID
                if (not Win_IsVisible((me + '.password'))):
                    print 'EnterRoom(',
                    print roomID,
                    print ''
                    EnterRoom(roomID, '')
                    PlaySound(soundMain, 1)
                else:
                    ui_setCapture('UI.selRoom.pwRoom')
                    Win_SetText('UI.selRoom.pwRoom.pw', '')
                    Win_SetFocus('UI.selRoom.pwRoom.pw')
                    PlaySound(soundUI, 1)



            def OnDBClick():
                me = Win_GetMyPath()
                doUI(me, 'OnClick')


            class children:
                __module__ = __name__
                class no(TPicLabel,
                 Static):
                    __module__ = __name__
                    rect = (15,
                     13,
                     (48 - 18),
                     12)
                    textsize = 10
                    bkimage = 'object/ui/selRoom/num.img'

                class logicID(TEditNum,
                 Static):
                    __module__ = __name__
                    visible = 0
                    rect = (0,
                     0,
                     0,
                     0)
                    value = 10

                class name(TLabel,
                 Static):
                    __module__ = __name__
                    drawcolor = maskColor
                    textEdgeType = -1
                    textEdgeColor = (0,
                     0,
                     0,
                     255)
                    rect = (58,
                     15,
                     (154 - 61),
                     12)

                class standard(TStatic):
                    __module__ = __name__
                    rect = (146,
                     (40 - 3),
                     28,
                     27)

                class password(TStatic):
                    __module__ = __name__
                    rect = (151,
                     10,
                     19,
                     20)
                    bkimage = 'res/uires/selRoom/icon/fangjiananniu_suo.img'

                class time(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (88,
                     62,
                     34,
                     30)
                    bkimage = 'res/uires/selRoom/fangjian_time.img'

                class playerNum(TPicLabel,
                 Static):
                    __module__ = __name__
                    bkimage = 'res/uires/selRoom/room/num_player.img'
                    textsize = 10
                    rect = (60,
                     70,
                     (15 * 4),
                     19)

                class mapIcon(TStatic):
                    __module__ = __name__
                    rect = (8,
                     40,
                     78,
                     20)
                    bkimage = 'map/icon/water.img'

                class mapName(TLabel,
                 Static):
                    __module__ = __name__
                    drawcolor = (255,
                     224,
                     82,
                     255)
                    textEdgeColor = (0,
                     49,
                     174,
                     255)
                    rect = (60,
                     44,
                     150,
                     12)

                class vip(TStatic):
                    __module__ = __name__
                    rect = (102,
                     70,
                     62,
                     20)
                    bkimage = 'object/ui/selRoom/icon_vip.img'



        class room2(room1):
            __module__ = __name__
            rect = (223,
             101,
             181,
             111)

        class room3(room1):
            __module__ = __name__
            rect = (27,
             213,
             181,
             111)

        class room4(room1):
            __module__ = __name__
            rect = (223,
             213,
             181,
             111)

        class room5(room1):
            __module__ = __name__
            rect = (27,
             325,
             181,
             111)

        class room6(room1):
            __module__ = __name__
            rect = (223,
             325,
             181,
             111)

        class room7(room1):
            __module__ = __name__
            rect = (27,
             437,
             181,
             111)

        class room8(room1):
            __module__ = __name__
            rect = (223,
             437,
             181,
             111)

        class roomLeft(TButton):
            __module__ = __name__
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            initlayer = -9999
            rect = (332,
             550,
             33,
             35)
            bkimage = 'object/ui/common/btn_left.img'

            def OnClick(this):
                global roomPagePos
                SectUserClickBtn(1)
                PlaySound(soundUI, 1)
                if (roomPagePos > 0):
                    roomPagePos -= 1



        class roomRight(TButton):
            __module__ = __name__
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            initlayer = -9999
            rect = (367,
             550,
             33,
             35)
            bkimage = 'object/ui/common/btn_right.img'

            def OnClick(this):
                global roomPagePos
                SectUserClickBtn(2)
                PlaySound(soundUI, 1)
                roomPagePos += 1



        class mapFilterBtn(TButton):
            __module__ = __name__
            initlayer = 90001
            rect = (279,
             71,
             114,
             18)

            def OnClick(this):
                ui_setCapture('UI.selRoom.mapFilterDlg')
                do(UI.children.selRoom.children.mapFilterDlg.children.scroll, 'OnPosChange')
                PlaySound(soundUI, 1)


            class children:
                __module__ = __name__
                class icon(TStatic):
                    __module__ = __name__
                    rect = (10,
                     0,
                     16,
                     18)
                    bkimage = ('map/icon/%s.img' % gameModeList[1][1])

                class text(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (36,
                     3,
                     60,
                     12)
                    caption = gameModeList[1][2]
                    drawcolor = (255,
                     255,
                     255,
                     255)

                class downArrow(TButton):
                    __module__ = __name__
                    rect = (94,
                     0,
                     18,
                     18)
                    bkimage = 'object/ui/selRoom/btn_mapFilter.img'

                    def OnClick(this):
                        doUI('UI.selRoom.mapFilterBtn', 'OnClick')





        class mapFilterMask(TStatic):
            __module__ = __name__
            initlayer = 99999
            rect = (278,
             71,
             115,
             18)
            bkimage = 'object/ui/chatRoom/dlg_mapFilterMask.img'

        class practiceBtn(TButton):
            __module__ = __name__
            rect = (505,
             538,
             51,
             54)
            bkimage = 'object/ui/selSect/btn_practice.img'

            def OnClick(this):
                if (not Win_IsVisible(this)):
                    return 
                CloseC2CDealDlg(bC2CDealShow)
                ui_setCapture(uiTaskSelDlg)
                PlaySound(soundMain, 1)



        class fastJoinRoomBtn(TButton):
            __module__ = __name__
            rect = (560,
             538,
             51,
             54)
            bkimage = 'object/ui/selSect/btn_quickJoin.img'

            def OnClick(this):
                if (not Win_IsVisible(this)):
                    return 
                CloseC2CDealDlg(bC2CDealShow)
                SetGameType(GameType)
                SC_ClickAutoEnterRoomBtn()
                AutoJoinRoom()
                PlaySound(soundMain, 1)
                screenStartOut()



        class newRoomBtn(TButton):
            __module__ = __name__
            rect = (615,
             538,
             51,
             54)
            bkimage = 'object/ui/selRoom/btn_createRoom.img'

            def OnClick(this):
                if (not Win_IsVisible(this)):
                    return 
                CloseC2CDealDlg(bC2CDealShow)
                SC_ClickCreateRoomBtn()
                PlaySound(soundUI, 1)
                CreateRoom('', 2, 1, '')
                return 



        class matchBtn(TButton):
            __module__ = __name__
            rect = (670,
             538,
             51,
             54)
            bkimage = 'object/ui/selRoom/btn_match.img'

            def OnClick(this):
                global bMatchChannel
                if (not Win_IsVisible(this)):
                    return 
                bMatchChannel = 1
                doUI('UI.selRoom.leaveBtn', 'OnClick')



        class shopBtn(TButton):
            __module__ = __name__
            rect = (435,
             536,
             65,
             58)
            bkimage = 'object/ui/selRoom/btn_shop.img'

            def OnClick(this):
                CloseC2CDealDlg(bC2CDealShow)
                SC_ClickShopBtn()
                go2shop()



        class tipGuide(TStatic):
            __module__ = __name__
            visible = 1
            initlayer = 999999
            bkimage = 'object/ui/selRoom/tip_GuideMid.img'
            rect = (430,
             496,
             1,
             1)

            def OnTimer(this):
                print 'tipGuide: ontimer()'
                Win_SetValue(this, 0.050000000000000003, 41)
                Win_SetValue(this, 2, 901)
                Win_Timer(this, 0)


            class children:
                __module__ = __name__
                class word(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (20,
                     13,
                     150,
                     50)
                    rowspace = 5
                    drawcolor = (69,
                     69,
                     69,
                     255)
                    textEdgeType = -1



        class tipEnterShop(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            bkimage = 'object/ui/selRoom/tip_enterShop.img'
            rect = (430,
             496,
             1,
             1)

            def OnTimer(this):
                Win_ShowWidget(this, (not Win_IsVisible(this)))



        class leaveBtn(TButton):
            __module__ = __name__
            rect = (735,
             542,
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
            bkimage = 'object/ui/common/btn_leave.img'

            def OnClick(this):
                global bmsg
                CloseC2CDealDlg(bC2CDealShow)
                UnInitialDealer()
                SC_ClickExitBtnInSection()
                UnInitializeShop()
                LogoutSection(uin)
                GotoUIScreen('selSect')
                PlaySound(soundLeave, 1)
                PlayMusic(musicDirAndSection, -1)
                bmsg = ([0] * msgcnt)



        class tipShop(TTip):
            __module__ = __name__
            visible = 0
            rect = (520,
             578,
             500,
             500)
            bkimage = 'object/ui/common/tip_new.img'

        class playerTab(TTabWin):
            __module__ = __name__
            groupid = 3
            groupstop = 1
            rect = (-2,
             0,
             1,
             1)
            hotrect = (432,
             67,
             76,
             19)
            hotcover = 'object/ui/selRoom/tab_player.img'

            def OnClick(this):
                global playerMode2
                PlaySound(soundUI, 1)
                playerMode2 = 0
                updatePlayer2()



        class friendTab(TTabWin):
            __module__ = __name__
            groupid = 3
            groupstop = 2
            rect = (-2,
             0,
             1,
             1)
            hotrect = (509,
             67,
             76,
             19)
            hotcover = 'object/ui/selRoom/tab_friend.img'

            def OnClick(this):
                global playerMode2
                playerMode2 = 1
                DoFriendTask('', 0, friendUin, 0)
                updatePlayer2()
                PlaySound(soundUI, 1)



        class allKinMemberTab(TTabWin):
            __module__ = __name__
            groupid = 3
            groupstop = 3
            rect = (-2,
             0,
             1,
             1)
            hotrect = (587,
             66,
             76,
             19)
            hotcover = 'object/ui/selRoom/tab_allKinMember.img'

            def OnClick(this):
                global playerMode2
                KinID = GetKinParam(0)
                if ((KinID == 0) and Win_SelectSelf('UI.selRoom.playerTab')):
                    ui_setCapture(uiKinCreateHintDlg)
                    playerMode2 = 0
                    updatePlayer2()
                PlaySound(soundUI, 1)



        class playerListDlg(TStatic):
            __module__ = __name__
            initlayer = 10000
            rect = (450,
             97,
             330,
             260)
            class children:
                __module__ = __name__
                class friendMask(TStatic):
                    __module__ = __name__
                    initlayer = 50000
                    rect = (0,
                     0,
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
                                if ((playerMode2 == 1) and InvalidOperation()):
                                    pass





                class playerInfo1(TButton):
                    __module__ = __name__
                    initlayer = 20000
                    rect = (0,
                     0,
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
                        print uins2[(i - 1)],
                        print '...',
                        print i
                        go2playerInfo(uins2[(i - 1)])
                        if ((false == Win_IsChecked('UI.selRoom.friendTab')) and SetPlayerModeInfo(uins2[(i - 1)], 0)):
                            pass



                    def OnRBtnUp(pos):
                        global friendName
                        global friendUin
                        (x, y,) = pos
                        if ((x + 77) > 800):
                            x = (800 - 77)
                        Win_Move2Pos(uiPlayerMenu, x, y)
                        i = getMyIdx2()
                        friendUin = uins2[(i - 1)]
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
                    rect = (0,
                     (0 + 24),
                     321,
                     23)

                class playerInfo3(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 2)),
                     321,
                     23)

                class playerInfo4(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 3)),
                     321,
                     23)

                class playerInfo5(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 4)),
                     321,
                     23)

                class playerInfo6(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 5)),
                     321,
                     23)

                class playerInfo7(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 6)),
                     321,
                     23)

                class playerInfo8(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 7)),
                     321,
                     23)

                class playerInfo9(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 8)),
                     321,
                     23)

                class playerInfo10(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 9)),
                     321,
                     23)

                class playerInfo11(playerInfo1):
                    __module__ = __name__
                    rect = (0,
                     (0 + (24 * 10)),
                     321,
                     23)

                class left(TButton):
                    __module__ = __name__
                    rect = (-19,
                     4,
                     16,
                     57)
                    bkimage = 'object/ui/selRoom/btn_left.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        pos = myGetPlayerPos2()
                        if ((pos != 0) and PlaySound(soundUI, 1)):
                            pos = max((pos - defPlayerCnt2), 0)
                            mySetPlayerPos2(pos)
                            updatePlayer2()



                class right(TButton):
                    __module__ = __name__
                    rect = (334,
                     4,
                     16,
                     57)
                    bkimage = 'object/ui/selRoom/btn_right.img'
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
                        pos = myGetPlayerPos2()
                        cnt = myGetPlayerCnt2()
                        if (((pos + defPlayerCnt2) < cnt) and PlaySound(soundUI, 1)):
                            pos += defPlayerCnt2
                            mySetPlayerPos2(pos)
                            updatePlayer2()





        class chatArea(TPoser):
            __module__ = __name__
            initlayer = 100000
            rect = (0,
             0,
             350,
             455)
            class children:
                __module__ = __name__
                class chatPanel(TStatic):
                    __module__ = __name__
                    initlayer = 500000
                    rect = (442,
                     354,
                     320,
                     116)
                    bkimage = 'object/ui/selRoom/dlg_chatMin.img'
                    class children:
                        __module__ = __name__
                        class flexUpBtn(TButton):
                            __module__ = __name__
                            rect = (173,
                             2,
                             40,
                             13)
                            bkimage = 'object/ui/selRoom/btn_flexUp.img'

                            def OnClick(this):
                                global flexMode
                                flexMode = min(3, (flexMode + 1))
                                flexChatArea(flexMode)



                        class flexDownBtn(TButton):
                            __module__ = __name__
                            rect = (132,
                             2,
                             40,
                             13)
                            bkimage = 'object/ui/selRoom/btn_flexDown.img'

                            def OnClick(this):
                                global flexMode
                                flexMode = max(1, (flexMode - 1))
                                flexChatArea(flexMode)



                        class speaker0(TLabel):
                            __module__ = __name__
                            initlayer = 100000
                            rect = (-4,
                             17,
                             350,
                             17)
                            bkimage = 'object/ui/selRoom/mask_speaker.img'

                            def OnDisappear():
                                me = Win_GetMyPath()
                                Win_ShowWidget(me, 0)


                            class children:
                                __module__ = __name__
                                class popo(TStatic):
                                    __module__ = __name__
                                    rect = (0,
                                     0,
                                     350,
                                     17)
                                    alphafactor = 0.59999999999999998
                                    minalphafactor = 0.59999999999999998
                                    bkimage = 'object/ui/selRoom/img_popo.img'

                                class words:
                                    __module__ = __name__
                                    type = 'MULTIEDIT'
                                    rowspace = 0
                                    editable = 0
                                    textEdgeType = -1
                                    drawcolor = broadcastColor
                                    rect = (0,
                                     0,
                                     350,
                                     12)
                                    captionrect = (12,
                                     3,
                                     336,
                                     12)
                                    maxline = 1

                                class nameBtn(TButton):
                                    __module__ = __name__
                                    initlayer = 200000
                                    rect = (0,
                                     0,
                                     310,
                                     18)
                                    textEdgeType = -1
                                    captionrect = (4,
                                     2,
                                     120,
                                     12)
                                    drawcolor = broadcastColor

                                    def OnClick(this):
                                        idx = getTailNum(this[:-len('.nameBtn')])
                                        name = namebuf[idx]
                                        uin = uinbuf[idx]
                                        NotifyWisper(name, uin)
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')



                                    def OnDBClick():
                                        me = Win_GetMyPath()
                                        idx = getTailNum(me[:-len('.nameBtn')])
                                        uin = uinbuf[idx]
                                        Win_FocusOnInsert('UI.selRoom.chatArea.chatEdit', str(uin))
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')



                                    def OnRClick():
                                        me = Win_GetMyPath()
                                        winrect = Win_GetRect(me, 906)
                                        idx = getTailNum(me[:-len('.nameBtn')])
                                        y = winrect[1]
                                        if (y > 400):
                                            y = 400
                                        Win_Move2Pos(uiPlayerMenu, (winrect[0] + 30), y)
                                        friendUin = uinbuf[idx]
                                        friendName = namebuf[idx]
                                        kinID = GetKinParam(0)
                                        if ((kinID > 0) and Win_ShowWidget((uiPlayerMenu + '.kininviteBtn'), kinID)):
                                            pass
                                        Win_ShowWidget((uiPlayerMenu + '.addBtn'), (not GetAttribute(friendUin, 0)))
                                        Win_ShowWidget((uiPlayerMenu + '.deleteBtn'), GetAttribute(friendUin, 0))
                                        Win_ShowWidget((uiPlayerMenu + '.shieldBtn'), (not GetAttribute(friendUin, 1)))
                                        Win_ShowWidget((uiPlayerMenu + '.unshieldBtn'), GetAttribute(friendUin, 1))
                                        Win_ShowWidget(uiPlayerMenu, 1)





                        class speaker1(speaker0):
                            __module__ = __name__
                            rect = (-4,
                             34,
                             350,
                             17)

                        class speaker2(speaker0):
                            __module__ = __name__
                            rect = (-4,
                             51,
                             350,
                             17)

                        class chatList:
                            __module__ = __name__
                            type = 'TEXTLIST'
                            rect = (3,
                             20,
                             320,
                             98)
                            captionrect = (0,
                             0,
                             320,
                             98)
                            drawcolor = (199,
                             242,
                             252,
                             255)
                            rowspace = 6
                            textfont = 1
                            textEdgeType = -1
                            scrollspace = 18

                            def OnClick(this):
                                if ((not Win_IsVisible(uiPlayerInfoDlg)) and Win_SetFocus('UI.selRoom.chatArea.chatEdit')):
                                    pass



                            def OnClickName(name, uin):
                                print 'OnClickName',
                                print name,
                                print uin
                                NotifyWisper(name, uin)
                                Win_SetFocus('UI.selRoom.chatArea.chatEdit')



                            def OnClickHLink(url):
                                ui_jumpWeb(url)



                            def OnDBClick(me):
                                print me
                                uin = Win_GetText(me)
                                Win_FocusOnInsert('UI.selRoom.chatArea.chatEdit', uin)
                                Win_SetFocus('UI.selRoom.chatArea.chatEdit')



                            def OnRClickName(name, uin):
                                global friendName
                                global friendUin
                                print '[OnRClick]'
                                me = Win_GetMyPath()
                                winrect = Win_GetRect(me, 906)
                                y = winrect[1]
                                if (y > 400):
                                    y = 400
                                Win_Move2Pos(uiPlayerMenu, (winrect[0] + 30), y)
                                friendUin = uin
                                friendName = name
                                kinID = GetKinParam(0)
                                if ((kinID > 0) and Win_ShowWidget((uiPlayerMenu + '.kininviteBtn'), kinID)):
                                    pass
                                Win_ShowWidget((uiPlayerMenu + '.addBtn'), (not GetAttribute(friendUin, 0)))
                                Win_ShowWidget((uiPlayerMenu + '.deleteBtn'), GetAttribute(friendUin, 0))
                                Win_ShowWidget((uiPlayerMenu + '.shieldBtn'), (not GetAttribute(friendUin, 1)))
                                Win_ShowWidget((uiPlayerMenu + '.unshieldBtn'), GetAttribute(friendUin, 1))
                                Win_ShowWidget(uiPlayerMenu, 1)
                                Win_SetFocus('UI.selRoom.chatArea.chatEdit')


                            class children:
                                __module__ = __name__
                                class chatScroll(TVScroll):
                                    __module__ = __name__
                                    extendstyle = 0
                                    rect = (326,
                                     0,
                                     14,
                                     90)
                                    pagesize = 8
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
                                             14,
                                             23)
                                            bkimage = 'object/ui/room/scl_block.img'







                class chatEdit(TRichEdit):
                    __module__ = __name__
                    initlayer = 550001
                    maxchar = 200
                    rect = (546,
                     500,
                     234,
                     20)
                    drawcolor = lightColor
                    textEdgeColor = maskColor
                    captionrect = (0,
                     4,
                     234,
                     12)

                class orientation(TButton):
                    __module__ = __name__
                    initlayer = 550001
                    rect = (465,
                     500,
                     80,
                     20)
                    drawcolor = zoneChooseColor
                    textEdgeColor = maskColor
                    textstyle = (dt_center + dt_vcenter)

                    def OnClick(this):
                        global ChatOrientation
                        if ((ChatMode == 0) and Win_SetText('UI.selRoom.chatArea.chatEdit', '')):
                            kininfo = GetInviteKinInfo(1)
                            if ((kininfo.m_dwKinIndex != 0) and (ChatOrientation == 0)):
                                SectionChat(0, '/kinchat on')
                                ChatOrientation = 1
                        if Win_SetFocus('UI.selRoom.chatArea.chatEdit'):
                            pass



                class commandPrompt(TCheck):
                    __module__ = __name__
                    initlayer = 650001
                    extendstyle = ui_btn_style_none
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1),
                     (0,
                      0,
                      2,
                      2,
                      0,
                      0,
                      1,
                      1)]
                    rect = (443,
                     496,
                     23,
                     24)
                    bkimage = 'object/ui/chat/btn_commandPrompt.img'

                    def OnClick(this):
                        if (Win_IsChecked('UI.selRoom.chatArea.commandPrompt') and (oldWinEventCnt == Win_GetEventCnt())):
                            if Win_SetCheck('UI.selRoom.chatArea.commandPrompt', False):
                                pass
                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')


                    class children:
                        __module__ = __name__
                        class comDlg(TWidget):
                            __module__ = __name__
                            visible = 0
                            style = wgtstyle_popup
                            rect = (3,
                             -140,
                             92,
                             140)
                            bkimage = 'object/ui/chat/img_commandPrompt.img'

                            def OnSelfHide():
                                global oldWinEventCnt
                                oldWinEventCnt = Win_GetEventCnt()
                                Win_SetCheck('UI.selRoom.chatArea.commandPrompt', False)


                            class children:
                                __module__ = __name__
                                class profileView(TButton):
                                    __module__ = __name__
                                    framescheme = [(0,
                                      0,
                                      0,
                                      0,
                                      -1,
                                      -1,
                                      -1,
                                      -1)]
                                    rect = (0,
                                     10,
                                     92,
                                     16)
                                    bkimage = 'object/ui/chat/img_cmdChoose.img'
                                    bkImgFlag = dt_center
                                    caption = '\xb2\xe9\xbf\xb4\xcd\xe6\xbc\xd2\xd7\xca\xc1\xcf'
                                    textstyle = (dt_center + dt_vcenter)

                                    def OnClick(this):
                                        Win_SetText('UI.selRoom.chatArea.chatEdit', '/who ')
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')
                                        Win_ShowWidget('UI.selRoom.chatArea.commandPrompt.comDlg', False)



                                class enterRoom(profileView):
                                    __module__ = __name__
                                    rect = (0,
                                     31,
                                     92,
                                     16)
                                    caption = '\xbc\xd3\xc8\xeb\xd3\xce\xcf\xb7\xb7\xbf\xbc\xe4'

                                    def OnClick(this):
                                        Win_SetText('UI.selRoom.chatArea.chatEdit', '/go ')
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')
                                        Win_ShowWidget('UI.selRoom.chatArea.commandPrompt.comDlg', False)



                                class refuseInvite(profileView):
                                    __module__ = __name__
                                    rect = (0,
                                     52,
                                     92,
                                     16)
                                    caption = '\xbe\xdc\xbe\xf8\xcb\xfb\xc8\xcb\xd1\xfb\xc7\xeb'

                                    def OnClick(this):
                                        Win_SetText('UI.selRoom.chatArea.chatEdit', '/refuse ')
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')
                                        Win_ShowWidget('UI.selRoom.chatArea.commandPrompt.comDlg', False)



                                class unrefuseInvite(profileView):
                                    __module__ = __name__
                                    rect = (0,
                                     73,
                                     92,
                                     16)
                                    caption = '\xbd\xe2\xb3\xfd\xbe\xdc\xbe\xf8\xd1\xfb\xc7\xeb'

                                    def OnClick(this):
                                        Win_SetText('UI.selRoom.chatArea.chatEdit', '/unrefuse ')
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')
                                        Win_ShowWidget('UI.selRoom.chatArea.commandPrompt.comDlg', False)



                                class ignoreWisper(profileView):
                                    __module__ = __name__
                                    rect = (0,
                                     94,
                                     92,
                                     16)
                                    caption = '\xc6\xc1\xb1\xce\xcb\xfb\xc8\xcb\xc3\xdc\xd3\xef'

                                    def OnClick(this):
                                        Win_SetText('UI.selRoom.chatArea.chatEdit', '/M ')
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')
                                        Win_ShowWidget('UI.selRoom.chatArea.commandPrompt.comDlg', False)



                                class unignoreWisper(profileView):
                                    __module__ = __name__
                                    rect = (0,
                                     115,
                                     92,
                                     16)
                                    caption = '\xbd\xe2\xb3\xfd\xb5\xa5\xc3\xdc\xc6\xc1\xb1\xce'

                                    def OnClick(this):
                                        Win_SetText('UI.selRoom.chatArea.chatEdit', '/U ')
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')
                                        Win_ShowWidget('UI.selRoom.chatArea.commandPrompt.comDlg', False)







                class sendBtn(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    initlayer = 550001
                    rect = (698,
                     475,
                     34,
                     22)
                    bkimage = 'object/ui/chat/btn_send.img'

                    def OnClick(this):
                        global ChatMode
                        txt = Win_GetText('UI.selRoom.chatArea.chatEdit')
                        txt = filterChatMsg(txt)
                        if ((txt != '') and (ChatMode == 0)):
                            if SectionChat(0, txt):
                                print 'SectionChat',
                                print txt
                            Win_SetText('UI.selRoom.chatArea.chatEdit', txt, value_channel_edithistory)
                            Win_SetText('UI.selRoom.chatArea.chatEdit', '')
                        if ((not Win_IsVisible(uiPlayerInfoDlg)) and Win_SetFocus('UI.selRoom.chatArea.chatEdit')):
                            pass



                class donateInfo(TButton):
                    __module__ = __name__
                    initlayer = 550001
                    rect = (629,
                     471,
                     30,
                     30)
                    visible = 0
                    choice = 0

                    def OnClick(this):
                        GetLeaveWord()



                    def OnTimer(this):
                        ui = this
                        mychoice = UI.children.selRoom.children.chatArea.children.donateInfo.choice
                        if (1 == mychoice):
                            UI.children.selRoom.children.chatArea.children.donateInfo.choice = 0
                            Win_SetImg(ui, '')
                        else:
                            UI.children.selRoom.children.chatArea.children.donateInfo.choice = 1
                            Win_SetImg(ui, 'object/ui/selRoom/btn_message.img')



                class faceBtn(TCheck):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1),
                     (0,
                      0,
                      2,
                      2,
                      0,
                      0,
                      1,
                      1)]
                    initlayer = 550001
                    extendstyle = ui_btn_style_none
                    rect = (670,
                     475,
                     24,
                     22)
                    bkimage = 'object/ui/chat/btn_expression.img'

                    def OnClick(this):
                        if (Win_IsChecked('UI.selRoom.chatArea.faceBtn') and (oldWinEventCnt == Win_GetEventCnt())):
                            if Win_SetCheck('UI.selRoom.chatArea.faceBtn', False):
                                pass
                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')


                    class children:
                        __module__ = __name__
                        class faceDlg(TWidget):
                            __module__ = __name__
                            visible = 0
                            style = wgtstyle_popup
                            rect = ((406 - 547),
                             -137,
                             174,
                             137)
                            bkimage = 'object/ui/chat/dlg_face.img'

                            def OnSelfHide():
                                global oldWinEventCnt
                                oldWinEventCnt = Win_GetEventCnt()
                                Win_SetCheck('UI.selRoom.chatArea.faceBtn', False)


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
                                            bkimage = 'res/uires/face/faces/000.img'

                                            def OnClick(this):
                                                if isMemberFace:
                                                    i = ((memberFacePage * 24) + getMyIdx())
                                                else:
                                                    i = (((facePage + memberFacePageNum) * 24) + getMyIdx())
                                                Win_FocusOnInsert('UI.selRoom.chatArea.chatEdit', faceIconList[i])
                                                Win_SetFocus('UI.selRoom.chatArea.chatEdit')



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
                                    drawcolor = (255,
                                     255,
                                     255,
                                     255)
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
                                        global facePage
                                        global memberFacePage
                                        if isMemberFace:
                                            memberFacePage -= 1
                                            if (memberFacePage < 0):
                                                memberFacePage = (memberFacePageNum - 1)
                                            setFacePage(memberFacePage, memberFacePageNum)
                                        else:
                                            facePage -= 1
                                            if (facePage < 0):
                                                facePage = (facePageNum - 1)
                                            setFacePage(facePage, facePageNum)
                                        PlaySound(soundUI, 1)
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')



                                class rightBtn(TButton):
                                    __module__ = __name__
                                    rect = (148,
                                     115,
                                     17,
                                     17)
                                    bkimage = 'res/uires/face/biaoq_you.img'

                                    def OnClick(this):
                                        global facePage
                                        global memberFacePage
                                        if isMemberFace:
                                            memberFacePage += 1
                                            if (memberFacePage >= memberFacePageNum):
                                                memberFacePage = 0
                                            setFacePage(memberFacePage, memberFacePageNum)
                                        else:
                                            facePage += 1
                                            if (facePage >= facePageNum):
                                                facePage = 0
                                            setFacePage(facePage, facePageNum)
                                        PlaySound(soundUI, 1)
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')



                                class choose(TButton):
                                    __module__ = __name__
                                    rect = (10,
                                     115,
                                     44,
                                     18)
                                    bkimage = 'object/ui/chat/btn_facemember.img'

                                    def OnClick(this):
                                        global isMemberFace
                                        if ((ChatMode == 0) and isMemberFace):
                                            isMemberFace = 0
                                            if Win_SetImg('UI.selRoom.chatArea.faceBtn.faceDlg.choose', 'object/ui/chat/btn_facemember.img'):
                                                setFacePage(facePage, facePageNum)
                                        PlaySound(soundUI, 1)
                                        Win_SetFocus('UI.selRoom.chatArea.chatEdit')







                class speakerBtn(TButton):
                    __module__ = __name__
                    initlayer = 550001
                    rect = (735,
                     473,
                     45,
                     24)

                    def OnClick(this):
                        global ChatMode
                        global ChatOrientation
                        ChatOrientation = 0
                        num = GetBugleNumber()
                        if Win_SetFocus('UI.selRoom.chatArea.chatEdit'):
                            if ((num > 0) and (ChatMode == 0)):
                                ChangeChatMode(1)
                                NotifyWisper(chatNameSpeaker, 0)



                class speakerTip:
                    __module__ = __name__
                    visible = 0
                    type = 'DYLABEL'
                    initlayer = 999999
                    bkimage = 'object/ui/common/img_tip.img'
                    rect = (646,
                     450,
                     130,
                     1)
                    captionrect = (4,
                     4,
                     120,
                     1)
                    drawcolor = maskColor
                    textEdgeType = -1

                    def OnInit():
                        Win_SetText('UI.selRoom.chatArea.speakerTip', '\xc4\xfa\xcf\xd6\xd4\xda\xc3\xbb\xd3\xd0\xd0\xa1\xc0\xae\xb0\xc8\xb5\xc0\xbe\xdf\xa3\xac\xc7\xeb\xcf\xc8\xd4\xda\xc9\xcc\xb5\xea\xb9\xba\xc2\xf2\xba\xf3\xd4\xd9\xca\xb9\xd3\xc3\xa3\xac\xd0\xbb\xd0\xbb\xa3\xa1')



                    def OnTimer(this):
                        Win_Timer(this, 0)
                        Win_ShowWidget(this, False)



                class integration(TTabWin):
                    __module__ = __name__
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (443,
                     471,
                     40,
                     20)
                    groupstop = 0
                    initlayer = 600010
                    hotcover = 'object/ui/chat/tab_integration.img'

                    def OnClick(this):
                        global ChatAreaTab
                        ChatAreaTab = 0
                        Win_ShowWidget('UI.selRoom.chatArea.chatPanel', 1)
                        Win_ShowWidget('UI.selRoom.chatArea.kinchatPanel', 0)
                        Win_ShowWidget('UI.selRoom.chatArea.wisperPanel', 0)
                        PlaySound(soundUI, 1)



                class kinchat(TTabWin):
                    __module__ = __name__
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (483,
                     471,
                     40,
                     20)
                    groupstop = 1
                    initlayer = 600015
                    hotcover = 'object/ui/chat/tab_kin.img'

                    def OnClick(this):
                        global ChatAreaTab
                        ChatAreaTab = 1
                        Win_ShowWidget('UI.selRoom.chatArea.chatPanel', 0)
                        Win_ShowWidget('UI.selRoom.chatArea.kinchatPanel', 1)
                        Win_ShowWidget('UI.selRoom.chatArea.wisperPanel', 0)
                        PlaySound(soundUI, 1)



                class wisper(kinchat):
                    __module__ = __name__
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (523,
                     471,
                     40,
                     20)
                    groupstop = 2
                    initlayer = 600010
                    hotcover = 'object/ui/chat/tab_whisper.img'

                    def OnClick(this):
                        global ChatAreaTab
                        ChatAreaTab = 2
                        Win_ShowWidget('UI.selRoom.chatArea.chatPanel', 0)
                        Win_ShowWidget('UI.selRoom.chatArea.kinchatPanel', 0)
                        Win_ShowWidget('UI.selRoom.chatArea.wisperPanel', 1)
                        PlaySound(soundUI, 1)



                class kinchatPanel(chatPanel):
                    __module__ = __name__

                class wisperPanel(chatPanel):
                    __module__ = __name__



        class pwRoom(TStatic):
            __module__ = __name__
            initlayer = 99999
            visible = 0
            darkBG = 1
            rect = (267,
             196,
             365,
             205)
            bkimage = 'object/ui/selRoom/dlg_pwRoom.img'
            class children:
                __module__ = __name__
                class pw(TEditPassword):
                    __module__ = __name__
                    drawcolor = zoneChooseColor
                    rect = (42,
                     84,
                     300,
                     12)
                    maxchar = 15

                class confirm(TButton):
                    __module__ = __name__
                    rect = (140,
                     165,
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
                        CloseC2CDealDlg(bC2CDealShow)
                        Win_ShowWidget('UI.selRoom.pwRoom', False)
                        pw = Win_GetText('UI.selRoom.pwRoom.pw')
                        EnterRoom(roomID, pw)
                        print 'EnterRoom(',
                        print roomID,
                        print pw
                        PlaySound(soundMain, 1)



                class cancel(TButton):
                    __module__ = __name__
                    rect = (200,
                     165,
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
                        Win_ShowWidget('UI.selRoom.pwRoom', False)
                        PlaySound(soundLeave, 1)





        class mapFilterDlg(TDlg):
            __module__ = __name__
            style = wgtstyle_popup
            initlayer = 80000
            visible = 0
            rect = (278,
             88,
             92,
             197)
            bkimage = 'object/ui/selRoom/map/dlg_mapFilter.img'

            def initMe():
                doUI('UI.room.selMap.scroll', 'OnPosChange')


            class children:
                __module__ = __name__
                class scroll(TVScroll):
                    __module__ = __name__
                    visible = 1
                    rect = ((442 - 338),
                     (61 - 44),
                     16,
                     73)
                    pos = 0
                    pagesize = -5

                    def OnPosChange():
                        scrollCnt = 11
                        ui = 'UI.selRoom.mapFilterDlg'
                        pos = Win_GetPos((ui + '.scroll'))
                        gameModeCnt = len(gameModeList)
                        print ('gameModeCnt is %d' % gameModeCnt)
                        Win_SetRange((ui + '.scroll'), (gameModeCnt - scrollCnt))
                        for i in range(scrollCnt):
                            mapUI = ((ui + '.mapMode') + str(i))
                            Win_SetValue(mapUI, 0, value_channel_draw_flag)
                            iPos = (i + pos)
                            if ((iPos >= gameModeCnt) and Win_ShowWidget(mapUI, False)):
                                pass




                class mapMode0(TButton):
                    __module__ = __name__
                    visible = 0
                    bkcolor = (222,
                     255,
                     36,
                     255)
                    rect = (0,
                     3,
                     100,
                     17)
                    framescheme = [(-1,
                      -1,
                      0,
                      0,
                      -1,
                      -1,
                      -1,
                      -1)]
                    bkimage = 'object/ui/chat/img_cmdChoose.img'

                    def OnClick(this):
                        global curGameMode
                        ui = 'UI.selRoom.mapFilterDlg'
                        pos = Win_GetPos((ui + '.scroll'))
                        curGameMode = (getMyIdx() + pos)
                        Win_ShowWidget(ui, 0)
                        info = gameModeList[curGameMode]
                        Win_SetText('UI.selRoom.mapFilterBtn.text', info[2])
                        Win_SetImg('UI.selRoom.mapFilterBtn.icon', ('map/icon/%s.img' % info[1]))
                        request_UserSelGameModeList(info[0])
                        PlaySound(soundUI, 1)


                    class children:
                        __module__ = __name__
                        class icon(TStatic):
                            __module__ = __name__
                            rect = (9,
                             0,
                             16,
                             17)
                            bkimage = 'map/icon/water.img'

                        class name(TLabel,
                         Static):
                            __module__ = __name__
                            rect = ((286 - 250),
                             (69 - 66),
                             80,
                             12)
                            drawcolor = (255,
                             255,
                             255,
                             255)



                class mapMode1(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 1)),
                     100,
                     17)

                class mapMode2(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 2)),
                     100,
                     17)

                class mapMode3(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 3)),
                     100,
                     17)

                class mapMode4(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 4)),
                     100,
                     17)

                class mapMode5(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 5)),
                     100,
                     17)

                class mapMode6(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 6)),
                     100,
                     17)

                class mapMode7(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 7)),
                     100,
                     17)

                class mapMode8(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 8)),
                     100,
                     17)

                class mapMode9(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 9)),
                     100,
                     17)

                class mapMode10(mapMode0):
                    __module__ = __name__
                    rect = (0,
                     (3 + (17 * 10)),
                     100,
                     17)



        class petPan(TStatic):
            __module__ = __name__
            visible = 0
            darkBG = 1
            initlayer = 999999
            rect = (80,
             100,
             353,
             530)
            bkimage = 'object/ui/pet/dlg_pet.img'

            def OnDenit():
                Win_ShowWidget(uiPetPan, 0)
                Win_ShowWidget((uiPetPan + '.foodDlg'), 0)


            class children:
                __module__ = __name__
                class petPreview(TLabel):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (55,
                     48,
                     94,
                     94)
                    framescheme = [(0,
                      15,
                      0,
                      15,
                      0,
                      15,
                      0,
                      15)]
                    drawcolor = lightColor
                    bkimage = ''

                class petFace(TStatic):
                    __module__ = __name__
                    initlayer = 9998
                    rect = (114,
                     50,
                     40,
                     40)
                    framescheme = [(0,
                      15,
                      0,
                      15,
                      0,
                      15,
                      0,
                      15)]
                    bkimage = ''

                class crossBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (214,
                     9,
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
                        Win_ShowWidget(uiPetPan, 0)
                        PlaySound(soundUI, 1)



                class adoptPetBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (196,
                     46,
                     40,
                     30)
                    bkimage = 'object/ui/pet/btn_adopt.img'

                    def OnClick(this):
                        global mark_shopPetTab
                        PlaySound(soundUI, 1)
                        mark_shopPetTab = 1
                        doUI('UI.selRoom.shopBtn', 'OnClick')



                class petStateBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (196,
                     80,
                     40,
                     30)
                    bkimage = 'object/ui/pet/btn_take.img'

                    def OnClick(this):
                        PlaySound(soundUI, 1)
                        if ((curPetState == 1) and Win_EnableWidget(this, 0)):
                            StopTakePet(curPetId)



                class freePetBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (196,
                     114,
                     40,
                     30)
                    bkimage = 'object/ui/pet/btn_free.img'

                    def OnClick(this):
                        PlaySound(soundUI, 1)
                        ui_msgBox(1)
                        Win_ShowMsgBox('    \xc4\xfa\xc8\xb7\xc8\xcf\xc8\xc3\xc4\xfa\xb5\xc4\xb3\xe8\xce\xef\xb1\xa6\xb1\xa6\xc0\xeb\xbf\xaa\xc4\xfa\xc2\xf0', '\xce\xc2\xdc\xb0\xcc\xe1\xca\xbe', 0, 'UI.SysMsgbox', -9)



                class nameEdit(TEdit):
                    __module__ = __name__
                    editable = 1
                    maxchar = 10
                    rect = (57,
                     158,
                     123,
                     16)
                    drawcolor = lightColor

                class changeNameBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (182,
                     150,
                     55,
                     26)
                    bkimage = 'object/ui/pet/btn_change_name.img'

                    def OnClick(this):
                        strName = Win_GetText((uiPetPan + '.nameEdit'))
                        if (curPetName == strName):
                            return 
                        Win_EnableWidget(this, 0)
                        ChangePetName(curPetId, strName)
                        PlaySound(soundUI, 1)



                class level(TLabel):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (84,
                     186,
                     100,
                     18)
                    drawcolor = darkColor
                    textEdgeType = -1
                    caption = ''

                class expLine(TStatic):
                    __module__ = __name__
                    bkimage = 'object/ui/pet/img_exp.img'
                    rect = (74,
                     209,
                     94,
                     12)

                class expValue(TLabel):
                    __module__ = __name__
                    rect = (174,
                     209,
                     100,
                     12)
                    drawcolor = lightColor
                    textEdgeColor = maskColor

                class loyaltyLine(TStatic):
                    __module__ = __name__
                    bkimage = 'object/ui/pet/img_exp.img'
                    rect = (74,
                     227,
                     94,
                     12)

                class loyaltyValue(TLabel):
                    __module__ = __name__
                    rect = (174,
                     227,
                     100,
                     12)
                    drawcolor = lightColor
                    textEdgeColor = maskColor

                class raisePetBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (13,
                     246,
                     109,
                     27)
                    bkimage = 'object/ui/pet/btn_raise.img'

                    def OnClick(this):
                        PlaySound(soundUI, 1)
                        ui = (uiPetPan + '.foodDlg')
                        if ((not Win_IsVisible(ui)) and UpdatePetItemUi()):
                            Win_ShowWidget(ui, 1)
                            Win_SetImg(this, 'object/ui/pet/btn_raise1.img')



                class foodDlg(TStatic):
                    __module__ = __name__
                    visible = 0
                    initlayer = 9999
                    rect = (1,
                     280,
                     250,
                     217)
                    bkimage = 'object/ui/pet/dlg_food.img'
                    class children:
                        __module__ = __name__
                        class firstPageBtn(TButton):
                            __module__ = __name__
                            initlayer = 9999
                            rect = (18,
                             195,
                             34,
                             21)
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            bkimage = 'object/ui/pet/btn_first_page.img'

                            def OnClick(this):
                                global petItemPos
                                petItemPos = 0
                                UpdatePetItemUi()
                                PlaySound(soundUI, 1)



                        class lastPageBtn(TButton):
                            __module__ = __name__
                            initlayer = 9999
                            rect = (206,
                             195,
                             34,
                             21)
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            bkimage = 'object/ui/pet/btn_last_page.img'

                            def OnClick(this):
                                global petItemPos
                                petItemPos = ((len(petItemList) / defPetItemCnt) * defPetItemCnt)
                                UpdatePetItemUi()
                                PlaySound(soundUI, 1)



                        class prePageBtn(TButton):
                            __module__ = __name__
                            initlayer = 9999
                            rect = (48,
                             195,
                             34,
                             21)
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            bkimage = 'object/ui/pet/btn_pre_page.img'

                            def OnClick(this):
                                global petItemPos
                                petItemPos -= defPetItemCnt
                                if (petItemPos < 0):
                                    petItemPos = 0
                                UpdatePetItemUi()
                                PlaySound(soundUI, 1)



                        class nextPageBtn(TButton):
                            __module__ = __name__
                            initlayer = 9999
                            rect = (186,
                             195,
                             25,
                             21)
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            bkimage = 'object/ui/pet/btn_next_page.img'

                            def OnClick(this):
                                global petItemPos
                                if ((petItemPos + defPetItemCnt) >= len(petItemList)):
                                    return 
                                petItemPos += defPetItemCnt
                                UpdatePetItemUi()
                                PlaySound(soundUI, 1)



                        class petItemPage:
                            __module__ = __name__
                            type = 'NUMLABEL'
                            rect = (85,
                             194,
                             80,
                             24)
                            bkimage = 'object/ui/common/number6.img'
                            textstyle = dt_center
                            textsize = 16
                            textwidth = 14
                            textheight = 18

                        class petItem0(TButton):
                            __module__ = __name__
                            rect = (5,
                             2,
                             60,
                             60)
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
                            tipwidget = (uiPetPan + '.description')

                            def OnRClick():
                                global curUseItem
                                PlaySound(soundUI, 1)
                                me = getMyIdx2()
                                index = (petItemPos + me)
                                if (index >= len(petItemList)):
                                    return 
                                curUseItem = petItemList[index].m_nItemID
                                ui_msgBox(1)
                                Win_ShowMsgBox('   \xc4\xfa\xc8\xb7\xc8\xcf\xd2\xaa\xca\xb9\xd3\xc3\xb3\xe8\xce\xef\xb5\xc0\xbe\xdf\xc2\xf0?', '\xce\xc2\xdc\xb0\xcc\xe1\xca\xbe', 0, 'UI.SysMsgbox', -8)



                            def OnMouseMoveIn():
                                ui = (uiPetPan + '.description')
                                index = (petItemPos + getMyIdx2())
                                if ((index >= len(petItemList)) and Win_ShowWidget(ui, 0)):
                                    return 
                                Win_ShowWidget(ui, 1)
                                item = petItemList[index].m_nItemID
                                if itemList.has_key(item):
                                    description = ((itemList[item][2] + ' \xa3\xba ') + itemList[item][3])
                                else:
                                    Win_ShowWidget(ui, 0)
                                    return 
                                Win_SetText(ui, description)
                                me = Win_GetMyPath()
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



                        class petItem1(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 1)),
                             2,
                             60,
                             60)

                        class petItem2(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 2)),
                             2,
                             60,
                             60)

                        class petItem3(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 3)),
                             2,
                             60,
                             60)

                        class petItem4(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 0)),
                             (2 + (62 * 1)),
                             60,
                             60)

                        class petItem5(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 1)),
                             (2 + (62 * 1)),
                             60,
                             60)

                        class petItem6(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 2)),
                             (2 + (62 * 1)),
                             60,
                             60)

                        class petItem7(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 3)),
                             (2 + (62 * 1)),
                             60,
                             60)

                        class petItem8(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 0)),
                             (2 + (62 * 2)),
                             60,
                             60)

                        class petItem9(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 1)),
                             (2 + (62 * 2)),
                             60,
                             60)

                        class petItem10(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 2)),
                             (2 + (62 * 2)),
                             60,
                             60)

                        class petItem11(petItem0):
                            __module__ = __name__
                            rect = ((5 + (62 * 3)),
                             (2 + (62 * 2)),
                             60,
                             60)



                class sKillBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (128,
                     246,
                     109,
                     27)
                    bkimage = 'object/ui/pet/btn_skill.img'

                    def OnClick(this):
                        PlaySound(soundUI, 1)
                        ui = (uiPetPan + '.skillDlg')
                        if ((not Win_IsVisible(ui)) and Win_ShowWidget((uiPetPan + '.baseSkillDlg'), 1)):
                            Win_ShowWidget(ui, 1)
                            Win_SetImg(this, 'object/ui/pet/btn_skill1.img')



                class baseSkillDlg(TStatic):
                    __module__ = __name__
                    visible = 0
                    initlayer = 9999
                    rect = (244,
                     -2,
                     108,
                     100)
                    bkimage = 'object/ui/pet/dlg_baseskill.img'
                    class children:
                        __module__ = __name__
                        class skill0(TButton):
                            __module__ = __name__
                            editable = 0
                            visible = 1
                            initlayer = 10000
                            rect = (20,
                             18,
                             73,
                             22)
                            drawcolor = lightColor
                            tipwidget = (uiPetPan + '.description')

                            def OnMouseMoveIn():
                                me = Win_GetMyPath()
                                idx = getMyIdx2()
                                ui = (uiPetPan + '.description')
                                skillDes = ''
                                if (idx >= len(baseSkillIdList)):
                                    skillDes = ''
                                    Win_SetText(ui, skillDes)
                                    Win_ShowWidget(ui, 0)
                                    return 
                                else:
                                    skillDes = GetSkillDescription(baseSkillIdList[idx])
                                Win_SetText(ui, skillDes)
                                winrect = Win_GetRect(me, value_channel_winrect)
                                caprect = Win_GetRect(ui, value_channel_captionrect)
                                Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))
                                Win_ShowWidget(ui, 1)



                        class skill1(skill0):
                            __module__ = __name__
                            rect = (20,
                             (18 + 28),
                             73,
                             22)

                        class skill2(skill0):
                            __module__ = __name__
                            rect = (20,
                             (18 + (28 * 2)),
                             73,
                             22)



                class skillDlg(TStatic):
                    __module__ = __name__
                    visible = 0
                    initlayer = 9999
                    rect = (244,
                     96,
                     108,
                     282)
                    bkimage = 'object/ui/pet/dlg_skill.img'
                    class children:
                        __module__ = __name__
                        class skill0(TButton):
                            __module__ = __name__
                            editable = 0
                            visible = 1
                            initlayer = 10000
                            rect = (20,
                             5,
                             73,
                             22)
                            drawcolor = lightColor
                            tipwidget = (uiPetPan + '.description')

                            def OnMouseMoveIn():
                                me = Win_GetMyPath()
                                idx = getMyIdx2()
                                ui = (uiPetPan + '.description')
                                skillDes = ''
                                if (idx >= len(skillIdList)):
                                    skillDes = ''
                                    Win_SetText(ui, skillDes)
                                    Win_ShowWidget(ui, 0)
                                    return 
                                else:
                                    skillDes = GetSkillDescription(skillIdList[idx])
                                Win_SetText(ui, skillDes)
                                winrect = Win_GetRect(me, value_channel_winrect)
                                caprect = Win_GetRect(ui, value_channel_captionrect)
                                Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))
                                Win_ShowWidget(ui, 1)



                        class skill1(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + 28),
                             73,
                             22)

                        class skill2(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 2)),
                             73,
                             22)

                        class skill3(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 3)),
                             73,
                             22)

                        class skill4(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 4)),
                             73,
                             22)

                        class skill5(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 5)),
                             73,
                             22)

                        class skill6(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 6)),
                             73,
                             22)

                        class skill7(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 7)),
                             73,
                             22)

                        class skill8(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 8)),
                             73,
                             22)

                        class skill9(skill0):
                            __module__ = __name__
                            rect = (20,
                             (5 + (28 * 9)),
                             73,
                             22)



                class left(TButton):
                    __module__ = __name__
                    rect = (34,
                     71,
                     16,
                     57)
                    bkimage = 'object/ui/selRoom/btn_left.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        global curPetId
                        PlaySound(soundUI, 1)
                        ui = (uiPetPan + '.skillDlg')
                        if (len(petsIdList) < 2):
                            return 
                        index = 0
                        for x in petsIdList:
                            if (curPetId == x):
                                break
                            index += 1

                        index -= 1
                        if (index < 0):
                            index = (len(petsIdList) - 1)
                        curPetId = petsIdList[index]
                        UpdatePetInfo()



                class right(TButton):
                    __module__ = __name__
                    rect = (156,
                     71,
                     16,
                     57)
                    bkimage = 'object/ui/selRoom/btn_right.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        global curPetId
                        PlaySound(soundUI, 1)
                        ui = (uiPetPan + '.skillDlg')
                        if (len(petsIdList) < 2):
                            return 
                        index = 0
                        for x in petsIdList:
                            if (curPetId == x):
                                break
                            index += 1

                        index += 1
                        if (index >= len(petsIdList)):
                            index = 0
                        curPetId = petsIdList[index]
                        UpdatePetInfo()



                class description:
                    __module__ = __name__
                    type = 'DYLABEL'
                    initlayer = 99999999
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



        class pawnshop(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            rect = (0,
             40,
             800,
             560)
            bkimage = 'object/ui/deal/bg_pawnshop.img'

            def OnInit():
                global PawnItemCnt
                PawnItemCnt = 0
                print 'pawnshop OnInit'
                Win_SetCheck((uiPawnShopDlg + '.pawnedBtn'), 0)
                Win_SetCheck((uiPawnShopDlg + '.pawningBtn'), 1)


            class children:
                __module__ = __name__
                class advertBtn(TButton):
                    __module__ = __name__
                    initlayer = 9999
                    rect = (18,
                     71,
                     163,
                     463)
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
                        print url
                        ui_jumpWeb(url)



                class crossBtn(TButton):
                    __module__ = __name__
                    initlayer = 999999
                    rect = (770,
                     10,
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
                        global CurrenPawnType
                        global bPawnShopShow
                        CurrenPawnType = -1
                        bPawnShopShow = 0
                        LogoutDeal()
                        Win_SetCheck((uiPawnShopDlg + '.pawnedBtn'), 0)
                        Win_SetCheck((uiPawnShopDlg + '.pawningBtn'), 1)
                        Win_ShowWidget(uiPawnShopDlg, 0)
                        PlaySound(soundUI, 1)



                class ware1(TCheck):
                    __module__ = __name__
                    initlayer = 2
                    rect = (368,
                     77,
                     198,
                     72)
                    bkimage = 'object/ui/shop/img_ware.img'
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
                    groupstop = 1

                    def OnClick(me):
                        pass

                    class children:
                        __module__ = __name__
                        class buyBtn(TButton):
                            __module__ = __name__
                            initlayer = -99
                            rect = (158,
                             25,
                             36,
                             42)
                            bkimage = 'object/ui/shop/btn_buy.img'
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]

                            def OnClick(me):
                                global buyItemInfo
                                pos = Win_GetPos((uiPawnShopDlg + '.wareScroll'))
                                wareIdx = getMyMidIdx()
                                print wareIdx,
                                print pos
                                print ('wareIdx=%d' % wareIdx)
                                ui = (uiPawnShopDlg + ('.ware%d' % wareIdx))
                                propId = int(Win_GetText((ui + '.ID')))
                                propname = Win_GetText((ui + '.name'))
                                price = int(Win_GetText((ui + '.price')))
                                saleindex = int(Win_GetText((ui + '.saleIndex')))
                                num = int(Win_GetText((ui + '.realNum')))
                                dstUin = int(Win_GetText((ui + '.dstUin')))
                                buyItemInfo = []
                                print ('propId = %(1)d propname = %(2)s price = %(3)d saleindex = %(4)d num = %(5)d dstUin = %(6)d' % {'1': propId,
                                 '2': propname,
                                 '3': price,
                                 '4': saleindex,
                                 '5': num,
                                 '6': dstUin})
                                buyItemInfo.append(propId)
                                buyItemInfo.append(price)
                                buyItemInfo.append(saleindex)
                                buyItemInfo.append(num)
                                buyItemInfo.append(dstUin)
                                if (ShowMyPawned and Win_SetText((uiPawnShopDlg + '.buyTipDlg.prompt'), '\xc4\xfa\xc8\xb7\xb6\xa8\xd2\xaa\xc8\xa1\xcf\xfb\xbc\xc4\xca\xdb\xb8\xc3\xb5\xc0\xbe\xdf\xc2\xf0?')):
                                    pass
                                ui_setCapture((uiPawnShopDlg + '.buyTipDlg'))



                        class frame(TStatic):
                            __module__ = __name__
                            visible = 0
                            initlayer = -999
                            rect = (0,
                             0,
                             1,
                             1)
                            framescheme = [(0,
                              0,
                              0,
                              0,
                              0,
                              0,
                              0,
                              0)]
                            bkimage = 'object/ui/shop/img_wareFrame.img'

                        class ID(TString):
                            __module__ = __name__
                            caption = '-1'

                        class picture(TStatic):
                            __module__ = __name__
                            bkImgFlag = dt_center
                            rect = (3,
                             3,
                             66,
                             66)

                        class name(TLabel,
                         Static):
                            __module__ = __name__
                            rect = (80,
                             (70 - 60),
                             (227 - 114),
                             12)
                            drawcolor = (255,
                             255,
                             0,
                             255)

                        class price1(TLabel,
                         Static):
                            __module__ = __name__
                            rect = (72,
                             29,
                             100,
                             12)
                            drawcolor = (255,
                             255,
                             255,
                             255)
                            textstyle = dt_left
                            textLineType = 0

                        class Num(TLabel,
                         Static):
                            __module__ = __name__
                            rect = (72,
                             45,
                             100,
                             12)
                            drawcolor = (255,
                             255,
                             255,
                             255)
                            textstyle = dt_left
                            textLineType = 0

                        class realNum(TString):
                            __module__ = __name__
                            caption = '-1'

                        class memberPic(TStatic):
                            __module__ = __name__
                            rect = (((97 - 19) - 6),
                             50,
                             27,
                             12)
                            bkimage = 'object/ui/shop/wareAttr/memberPic.img'

                        class saleIndex(TString):
                            __module__ = __name__
                            caption = '-1'

                        class price(TString):
                            __module__ = __name__
                            caption = '-1'

                        class dstUin(TString):
                            __module__ = __name__
                            caption = '-1'

                        class PetInfo(TButton):
                            __module__ = __name__
                            initlayer = -99
                            rect = (139,
                             46,
                             36,
                             36)
                            bkimage = 'object/ui/deal/lookuppetBtn.img'
                            framescheme = [(0,
                              0,
                              1,
                              1,
                              2,
                              2,
                              3,
                              3)]

                            def OnClick(me):
                                wareIdx = getMyMidIdx()
                                print ('[PetInfo] wareIdx=%d' % wareIdx)
                                ui = (uiPawnShopDlg + ('.ware%d' % wareIdx))
                                saeIdx = saleindex = int(Win_GetText((ui + '.saleIndex')))
                                RequestPawnPetInfo(saeIdx)





                class ware2(ware1):
                    __module__ = __name__
                    rect = (567,
                     77,
                     198,
                     72)
                    groupstop = 2
                    initlayer = 1

                class ware3(ware1):
                    __module__ = __name__
                    rect = (368,
                     (77 + 73),
                     198,
                     72)
                    groupstop = 3
                    initlayer = 4

                class ware4(ware1):
                    __module__ = __name__
                    rect = (567,
                     (77 + 73),
                     198,
                     72)
                    groupstop = 4
                    initlayer = 3

                class ware5(ware1):
                    __module__ = __name__
                    rect = (368,
                     (77 + (73 * 2)),
                     198,
                     72)
                    groupstop = 5
                    initlayer = 6

                class ware6(ware1):
                    __module__ = __name__
                    rect = (567,
                     (77 + (73 * 2)),
                     198,
                     72)
                    groupstop = 6
                    initlayer = 5

                class ware7(ware1):
                    __module__ = __name__
                    rect = (368,
                     (77 + (73 * 3)),
                     198,
                     72)
                    groupstop = 7
                    initlayer = 8

                class ware8(ware1):
                    __module__ = __name__
                    rect = (567,
                     (77 + (73 * 3)),
                     198,
                     72)
                    groupstop = 8
                    initlayer = 7

                class ware9(ware1):
                    __module__ = __name__
                    rect = (368,
                     (77 + (73 * 4)),
                     198,
                     72)
                    groupstop = 9
                    initlayer = 10

                class ware10(ware1):
                    __module__ = __name__
                    rect = (567,
                     (77 + (73 * 4)),
                     198,
                     72)
                    groupstop = 10
                    initlayer = 9

                class ware11(ware1):
                    __module__ = __name__
                    rect = (368,
                     (77 + (73 * 5)),
                     198,
                     72)
                    groupstop = 11
                    initlayer = 12

                class ware12(ware1):
                    __module__ = __name__
                    rect = (567,
                     (77 + (73 * 5)),
                     198,
                     72)
                    groupstop = 12
                    initlayer = 11

                class itemList0(TButton):
                    __module__ = __name__
                    rect = (190,
                     75,
                     132,
                     19)
                    bkimage = 'object/ui/forge/btn_type.img'
                    textEdgeColor = (80,
                     80,
                     80,
                     255)
                    teststyle = dt_left

                    def OnClick(this):
                        global CurrentPawnItemID
                        global PawnItemCnt
                        global CurrenPawnType
                        if ShowMyPawned:
                            return 
                        pos = Win_GetPos((uiPawnShopDlg + '.itemScroll'))
                        idx = (getMyIdx2() + pos)
                        print ('idx = %d,CurrenPawnType = %d' % (idx,
                         CurrenPawnType))
                        if (idx < CurrenPawnType):
                            CurrenPawnType = idx
                            g_PawnItemList.clear()
                            g_PawnItemList.update()
                            doUI((uiPawnShopDlg + '.itemScroll'), 'OnPosChange')
                        elif (idx == CurrenPawnType):
                            CurrenPawnType = -1
                            PawnItemCnt = 0
                            doUI((uiPawnShopDlg + '.itemScroll'), 'OnPosChange')
                        elif ((CurrenPawnType >= 0) and (idx <= (CurrenPawnType + PawnItemCnt))):
                            print ('[itemList0]idx- CurrenPawnType = %d' % (idx - CurrenPawnType))
                            CurrentPawnItemID = g_PawnItemList.at(((idx - CurrenPawnType) - 1)).m_nPropID
                            RequestGetPawnGoodsbyID(CurrentPawnItemID, 0)
                            print ('CurrentItem Prop = %(n)d,PropName = %(x)s' % {'n': g_PawnItemList.at(((idx - CurrenPawnType) - 1)).m_nPropID,
                             'x': g_PawnItemList.at(((idx - CurrenPawnType) - 1)).m_sPropName})
                        elif (idx < (PawnTypeCnt + PawnItemCnt)):
                            CurrenPawnType = (idx - PawnItemCnt)
                            g_PawnItemList.clear()
                            g_PawnItemList.update()
                            print ('idx = %d,CurrenPawnType = %d,PawnTypeCnt = %d,PawnItemCnt = %d' % (idx,
                             CurrenPawnType,
                             PawnTypeCnt,
                             PawnItemCnt))
                            doUI((uiPawnShopDlg + '.itemScroll'), 'OnPosChange')



                class itemList1(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 1)),
                     132,
                     19)

                class itemList2(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 2)),
                     132,
                     19)

                class itemList3(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 3)),
                     132,
                     19)

                class itemList4(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 4)),
                     132,
                     19)

                class itemList5(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 5)),
                     132,
                     19)

                class itemList6(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 6)),
                     132,
                     19)

                class itemList7(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 7)),
                     132,
                     19)

                class itemList8(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 8)),
                     132,
                     19)

                class itemList9(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 9)),
                     132,
                     19)

                class itemList9(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 9)),
                     132,
                     19)

                class itemList10(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 10)),
                     132,
                     19)

                class itemList11(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 11)),
                     132,
                     19)

                class itemList12(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 12)),
                     132,
                     19)

                class itemList13(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 13)),
                     132,
                     19)

                class itemList14(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 14)),
                     132,
                     19)

                class itemList15(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 15)),
                     132,
                     19)

                class itemList16(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 16)),
                     132,
                     19)

                class itemList17(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 17)),
                     132,
                     19)

                class itemList18(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 18)),
                     132,
                     19)

                class itemList19(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 19)),
                     132,
                     19)

                class itemList20(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 20)),
                     132,
                     19)

                class itemList21(itemList0):
                    __module__ = __name__
                    rect = (190,
                     (75 + (20 * 21)),
                     132,
                     19)

                class itemScroll(TVScroll):
                    __module__ = __name__
                    rect = ((340 - 14),
                     (75 + 16),
                     26,
                     408)
                    pos = 0

                    def OnPosChange():
                        (PawnTypeCnt,
                         PawnItemCnt,
                         CurrenPawnType,
                         defPawnItemCnt)
                        pos = Win_GetPos((uiPawnShopDlg + '.itemScroll'))
                        sclRange = PawnTypeCnt
                        if (CurrenPawnType >= 0):
                            print ('[itemScroll::OnPosChange]pos = %d,PawnItemCnt = %d' % (pos,
                             PawnItemCnt))
                            sclRange += PawnItemCnt
                        Win_SetRange((uiPawnShopDlg + '.itemScroll'), max((sclRange - defPawnItemCnt), 0))
                        for i in range(defPawnItemCnt):
                            idx = (pos + i)
                            Win_SetDrawColor((uiPawnShopDlg + ('.itemList%d' % i)), 255, 255, 255, 255)
                            if ((idx <= CurrenPawnType) and Win_SetImg((uiPawnShopDlg + ('.itemList%d' % i)), 'object/ui/forge/btn_type.img')):
                                Win_SetText((uiPawnShopDlg + ('.itemList%d' % i)), g_PawnTypeList.at(idx).m_TypeName)



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

                        class spinup(TSpinDec):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (5,
                             -17,
                             18,
                             18)
                            bkimage = 'object/ui/forge/scl_up.img'

                            def OnClick(this):
                                PlaySound(soundUI, 1)



                        class spindown(TSpinInc):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (5,
                             (420 - 13),
                             18,
                             18)
                            bkimage = 'object/ui/forge/scl_down.img'

                            def OnClick(this):
                                PlaySound(soundUI, 1)





                class wareScroll(TVScroll):
                    __module__ = __name__
                    rect = (763,
                     (75 + 16),
                     26,
                     408)
                    pos = 0

                    def OnPosChange():
                        currentpos = 0
                        if ShowMyPawned:
                            ShowList = g_MyPawnItemList
                            currentpos = PawnGoodsPos
                        else:
                            ShowList = g_PawnGoodsList
                        print PawnGoodsCnt
                        Win_SetRange((uiPawnShopDlg + '.wareScroll'), (((PawnGoodsCnt - defPawnwareCnt) + 1) / 2))
                        pos = Win_GetPos((uiPawnShopDlg + '.wareScroll'))
                        print '[wareScroll::OnPosChange]pos=',
                        print pos
                        for i in range(defPawnwareCnt):
                            ui = (uiPawnShopDlg + ('.ware%d' % (i + 1)))
                            info = ShowList.at(((currentpos + i) + (pos * 2)))
                            if ((None == info) and Win_EnableWidget(ui, 0)):
                                Win_SetText((ui + '.name'), '')
                                Win_SetText((ui + '.ID'), '')
                                Win_SetImg((ui + '.picture'), '')
                                Win_SetText((ui + '.price1'), '')
                                Win_SetImg((ui + '.memberPic'), '')
                                Win_SetText((ui + '.Num'), '')
                                Win_SetText((ui + '.dstUin'), '')
                                Win_SetImg((ui + '.buyBtn'), '')
                                Win_SetImg((ui + '.PetInfo'), '')
                                Win_EnableWidget((ui + '.PetInfo'), 0)
                                Win_EnableWidget((ui + '.buyBtn'), 0)



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

                        class spinup(TSpinDec):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (5,
                             -17,
                             18,
                             18)
                            bkimage = 'object/ui/forge/scl_up.img'

                            def OnClick(this):
                                PlaySound(soundUI, 1)



                        class spindown(TSpinInc):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (5,
                             (420 - 13),
                             18,
                             18)
                            bkimage = 'object/ui/forge/scl_down.img'

                            def OnClick(this):
                                PlaySound(soundUI, 1)





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
                    rect = ((600 - 165),
                     518,
                     33,
                     36)
                    bkimage = 'object/ui/common/btn_left.img'

                    def OnClick(this):
                        global PawnGoodsPos
                        if ((not ShowMyPawned) and RequestGetPawnGoodsbyID(CurrentPawnItemID, 1)):
                            pass
                        PlaySound(soundUI, 1)
                        Win_EnableWidget((uiPawnShopDlg + '.Left'), 0)
                        Win_Timer((uiPawnShopDlg + '.Left'), 3000)



                    def OnTimer(this):
                        Win_Timer(this, 0)
                        Win_EnableWidget((uiPawnShopDlg + '.Left'), 1)



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
                    rect = ((700 - 68),
                     518,
                     33,
                     36)
                    bkimage = 'object/ui/common/btn_right.img'

                    def OnClick(this):
                        global PawnGoodsPos
                        if ((not ShowMyPawned) and RequestGetPawnGoodsbyID(CurrentPawnItemID, 2)):
                            pass
                        PlaySound(soundUI, 1)
                        Win_EnableWidget((uiPawnShopDlg + '.Right'), 0)
                        Win_Timer((uiPawnShopDlg + '.Right'), 3000)



                    def OnTimer(this):
                        Win_Timer(this, 0)
                        Win_EnableWidget((uiPawnShopDlg + '.Right'), 1)



                class PawnGoodsPage:
                    __module__ = __name__
                    type = 'NUMLABEL'
                    rect = (508,
                     522,
                     80,
                     24)
                    bkimage = 'object/ui/common/number2.img'
                    textstyle = dt_center
                    textsize = 16
                    textwidth = 19
                    textheight = 24

                class MyStorage(TButton):
                    __module__ = __name__
                    rect = (497,
                     38,
                     76,
                     31)
                    bkimage = 'object/ui/deal/mystoragebtn.img'

                    def OnClick(this):
                        global IsShowStorageDlg
                        print 'MyStorage onclick'
                        doUI((uiPawnShopDlg + '.crossBtn'), 'OnClick')
                        doUI('UI.selRoom.shopBtn', 'OnClick')
                        IsShowStorageDlg = 1
                        PlaySound(soundUI, 1)



                class Commit(TButton):
                    __module__ = __name__
                    rect = (387,
                     38,
                     76,
                     31)
                    bkimage = 'object/ui/deal/commitbtn.img'

                    def OnClick(this):
                        print 'Commit click'
                        updateMyStorageInPawn()
                        ui_setCapture((uiPawnShopDlg + '.CommitPanel'))
                        PlaySound(soundUI, 1)



                class CommitPanel(TStatic):
                    __module__ = __name__
                    visible = 0
                    initlayer = 999999
                    rect = (15,
                     45,
                     346,
                     513)
                    bkimage = 'object/ui/deal/commitpanel.img'
                    class children:
                        __module__ = __name__
                        __doc__ = "class confirmBtn(TButton):\n                            initlayer = 999999\n                            rect = (140,466, 76, 31)\n                            bkimage = 'object/ui/deal/confirmbtn.img'\n                            def OnClick(this):\n                                Win_ShowWidget( uiPawnShopDlg+'.CommitPanel', 0)\n                                Win_SetCheck(uiPawnShopDlg + '.pawnedBtn',0)\n                                Win_SetCheck(uiPawnShopDlg + '.pawningBtn',1)\n                                ui_updatePawnTypeList()\n                                PlaySound( soundUI, 1)"
                        class cancelBtn(TButton):
                            __module__ = __name__
                            initlayer = 999999
                            rect = ((230 + 20),
                             466,
                             76,
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

                            def OnClick(this):
                                Win_ShowWidget((uiPawnShopDlg + '.CommitPanel'), 0)
                                Win_SetCheck((uiPawnShopDlg + '.pawnedBtn'), 0)
                                Win_SetCheck((uiPawnShopDlg + '.pawningBtn'), 1)
                                ui_updatePawnTypeList()
                                PlaySound(soundUI, 1)



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
                            rect = (35,
                             265,
                             53,
                             53)
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
                            tipwidget = (uiPawnShopDlg + '.CommitPanel.storageDescription')

                            def OnClick(this):
                                global CurrentPropIdx
                                me = Win_GetFocusPath()
                                CurrentPropIdx = ((Win_GetScrollPos((uiPawnShopDlg + '.CommitPanel.StorageScroll')) * 4) + getTailNum(me))
                                if (g_MyDealStorageList.at(CurrentPropIdx) == None):
                                    return 
                                print ('CurrentPropIdx = %d' % CurrentPropIdx)
                                if (check12 and Win_SetCheck((uiPawnShopDlg + '.CommitPanel.PawnSettings.halfday'), 1)):
                                    Win_SetCheck((uiPawnShopDlg + '.CommitPanel.PawnSettings.aday'), 0)
                                ui_setCapture((uiPawnShopDlg + '.CommitPanel.PawnSettings'))
                                Win_SetFocus((uiPawnShopDlg + '.CommitPanel.PawnSettings.srcBill'))



                            def OnMouseMoveIn():
                                me = Win_GetMyPath()
                                idx = ((Win_GetScrollPos((uiPawnShopDlg + '.CommitPanel.StorageScroll')) * 4) + getTailNum(me))
                                if (idx >= MyDealStorageListCnt):
                                    return 
                                info = g_MyDealStorageList.at(idx)
                                ui = (uiPawnShopDlg + '.CommitPanel.storageDescription')
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
                                     53,
                                     53)
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
                            rect = ((35 + (63 * 1)),
                             265,
                             53,
                             53)
                            groupstop = 1

                        class funcItem2(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (63 * 2)),
                             265,
                             53,
                             53)
                            groupstop = 2

                        class funcItem3(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (63 * 3)),
                             265,
                             53,
                             53)
                            groupstop = 3

                        class funcItem4(funcItem0):
                            __module__ = __name__
                            rect = (35,
                             (265 + (63 * 1)),
                             53,
                             53)
                            groupstop = 4

                        class funcItem5(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (63 * 1)),
                             (265 + (63 * 1)),
                             53,
                             53)
                            groupstop = 5

                        class funcItem6(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (63 * 2)),
                             (265 + (63 * 1)),
                             53,
                             53)
                            groupstop = 6

                        class funcItem7(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (63 * 3)),
                             (265 + (63 * 1)),
                             53,
                             53)
                            groupstop = 7

                        class funcItem8(funcItem0):
                            __module__ = __name__
                            rect = (35,
                             (265 + (63 * 2)),
                             53,
                             53)
                            groupstop = 8

                        class funcItem9(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (63 * 1)),
                             (265 + (63 * 2)),
                             53,
                             53)
                            groupstop = 9

                        class funcItem10(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (63 * 2)),
                             (265 + (63 * 2)),
                             53,
                             53)
                            groupstop = 10

                        class funcItem11(funcItem0):
                            __module__ = __name__
                            rect = ((35 + (62 * 3)),
                             (265 + (63 * 2)),
                             53,
                             53)
                            groupstop = 11

                        class StorageScroll(TVScroll):
                            __module__ = __name__
                            rect = (305,
                             261,
                             26,
                             192)
                            pos = 0

                            def OnPosChange():
                                Win_SetRange((uiPawnShopDlg + '.CommitPanel.StorageScroll'), ((((MyDealStorageListCnt - defStorageInPawnCnt) + 1) / 4) + 1))
                                pos = Win_GetPos((uiPawnShopDlg + '.CommitPanel.StorageScroll'))
                                for i in range(defStorageInPawnCnt):
                                    ui = (uiPawnShopDlg + ('.CommitPanel.funcItem%d' % i))
                                    info = g_MyDealStorageList.at((i + (pos * 4)))
                                    if ((None == info) and Win_SetImg((ui + '.itemPic'), '')):
                                        Win_SetText((ui + '.itemNum'), '')



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
                                    rect = (2,
                                     0,
                                     26,
                                     42)
                                    bkimage = 'object/ui/common/scl_block.img'

                                class spinup(TSpinDec):
                                    __module__ = __name__
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]
                                    rect = (6,
                                     -17,
                                     18,
                                     18)
                                    bkimage = 'object/ui/forge/scl_up.img'

                                    def OnClick(this):
                                        PlaySound(soundUI, 1)



                                class spindown(TSpinInc):
                                    __module__ = __name__
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]
                                    rect = (6,
                                     192,
                                     18,
                                     18)
                                    bkimage = 'object/ui/forge/scl_down.img'

                                    def OnClick(this):
                                        PlaySound(soundUI, 1)





                        class PawnSettings(TStatic):
                            __module__ = __name__
                            visible = 0
                            initlayer = 999999
                            rect = (60,
                             140,
                             226,
                             132)
                            bkimage = 'object/ui/deal/pawnSettingPanel.img'

                            def OnInit():
                                print 'PawnSettings OnInit'


                            class children:
                                __module__ = __name__
                                class confirm(TButton):
                                    __module__ = __name__
                                    initlayer = 999999
                                    rect = (65,
                                     90,
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
                                    bkimage = 'object/ui/common/btn_confirm.img'

                                    def OnClick(this):
                                        global check12
                                        info = g_MyDealStorageList.at(CurrentPropIdx)
                                        iteminfo = info.m_stItem
                                        itemname = info.m_szName
                                        price = int(Win_GetText((uiPawnShopDlg + '.CommitPanel.PawnSettings.srcBill')))
                                        Num = int(Win_GetText((uiPawnShopDlg + '.CommitPanel.PawnSettings.SaleNum')))
                                        if (((not CHECK_PET(info.m_stItem.m_nItemID)) and (Num > info.m_stItem.m_iNumOfItem)) and ui_msgBox(3)):
                                            Win_ShowMsgBox('\xc4\xfa\xc7\xeb\xc7\xf3\xbc\xc4\xca\xdb\xb5\xc4\xca\xfd\xc1\xbf\xd2\xd1\xbe\xad\xb3\xac\xb9\xfd\xc1\xcb\xc4\xfa\xcb\xf9\xd3\xb5\xd3\xd0\xb5\xc4\xca\xfd\xc1\xbf', '', 3, 'UI.SysMsgbox', -1)
                                            return 
                                        interval = 24
                                        check12 = 0
                                        if Win_IsChecked((uiPawnShopDlg + '.CommitPanel.PawnSettings.halfday')):
                                            interval = 12
                                            check12 = 1
                                        if ((price == 0) or ((Num == 0) or (iteminfo.m_nItemID == 0))):
                                            return 
                                        PrepareCommititem = [iteminfo.m_nItemID,
                                         itemname,
                                         price,
                                         Num,
                                         interval,
                                         0]
                                        print ('PrepareCommititem%(1)d,%(2)s,%(3)d,%(4)d,%(5)d' % {'1': iteminfo.m_nItemID,
                                         '2': itemname,
                                         '3': price,
                                         '4': Num,
                                         '5': interval})
                                        RequestCommitGoods2Pawn(Commit2Pawn, PrepareCommititem)
                                        Win_ShowWidget((uiPawnShopDlg + '.CommitPanel.PawnSettings'), 0)
                                        PlaySound(soundUI, 1)



                                class cancel(TButton):
                                    __module__ = __name__
                                    initlayer = 999999
                                    rect = (140,
                                     90,
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
                                    bkimage = 'object/ui/common/btn_cancel.img'

                                    def OnClick(this):
                                        Win_ShowWidget((uiPawnShopDlg + '.CommitPanel.PawnSettings'), 0)
                                        PlaySound(soundUI, 1)



                                class srcBill(TEditID):
                                    __module__ = __name__
                                    initlayer = 999999
                                    maxchar = 9
                                    rect = (89,
                                     14,
                                     77,
                                     14)
                                    drawcolor = lightColor
                                    textEdgeColor = maskColor
                                    captionrect = (0,
                                     2,
                                     77,
                                     14)
                                    textstyle = dt_right
                                    caption = '0.0'

                                    def OnTab():
                                        Win_SetFocus((uiPawnShopDlg + '.CommitPanel.PawnSettings.SaleNum'))



                                class SaleNum(TEditID):
                                    __module__ = __name__
                                    initlayer = 999999
                                    maxchar = 4
                                    rect = (103,
                                     39,
                                     36,
                                     14)
                                    drawcolor = lightColor
                                    textEdgeColor = maskColor
                                    captionrect = (0,
                                     2,
                                     36,
                                     14)
                                    textstyle = dt_right
                                    caption = '0.0'

                                    def OnTab():
                                        Win_SetFocus((uiPawnShopDlg + '.CommitPanel.PawnSettings.halfday'))



                                class halfday(TRadio):
                                    __module__ = __name__
                                    rect = (88,
                                     60,
                                     23,
                                     17)
                                    bkimage = 'object/ui/common/btn_ratio.img'
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
                                    tipwidget = (uiModifyRoomDlg + '.chooseTip')
                                    groupstop = 1

                                    def OnTab():
                                        Win_SetFocus((uiPawnShopDlg + '.CommitPanel.PawnSettings.aday'))



                                class aday(TRadio):
                                    __module__ = __name__
                                    rect = (148,
                                     60,
                                     23,
                                     17)
                                    bkimage = 'object/ui/common/btn_ratio.img'
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
                                    tipwidget = (uiModifyRoomDlg + '.chooseTip')
                                    groupstop = 2

                                    def OnTab():
                                        Win_SetFocus((uiPawnShopDlg + '.CommitPanel.PawnSettings.srcBill'))





                        class CommittedItem0(TStatic):
                            __module__ = __name__
                            visible = 0
                            initlayer = 999998
                            rect = (21,
                             17,
                             282,
                             32)
                            bkimage = 'object/ui/deal/commiteditem.img'
                            class children:
                                __module__ = __name__
                                class PropName(TLabel,
                                 Static):
                                    __module__ = __name__
                                    rect = (5,
                                     4,
                                     90,
                                     25)
                                    drawcolor = lightColor
                                    textEdgeColor = maskColor
                                    textEdgeType = 1
                                    textstyle = dt_center
                                    caption = 'abc'

                                class PropNum(TLabel,
                                 Static):
                                    __module__ = __name__
                                    rect = (98,
                                     4,
                                     50,
                                     25)
                                    drawcolor = lightColor
                                    textEdgeColor = maskColor
                                    textEdgeType = 1
                                    textstyle = dt_center
                                    caption = '123'

                                class interval(TLabel,
                                 Static):
                                    __module__ = __name__
                                    rect = (150,
                                     4,
                                     30,
                                     25)
                                    drawcolor = lightColor
                                    textEdgeColor = maskColor
                                    textEdgeType = 1
                                    textstyle = dt_center
                                    caption = '12'

                                class price(TLabel,
                                 Static):
                                    __module__ = __name__
                                    rect = (188,
                                     4,
                                     51,
                                     25)
                                    drawcolor = lightColor
                                    textEdgeColor = maskColor
                                    textEdgeType = 1
                                    textstyle = dt_center
                                    caption = '5'

                                class cancel(TButton):
                                    __module__ = __name__
                                    initlayer = 999999
                                    rect = (235,
                                     4,
                                     39,
                                     31)
                                    bkimage = 'object/ui/deal/cancelhorizontal.img'

                                    def OnClick(this):
                                        pos = Win_GetPos((uiPawnShopDlg + '.CommitPanel.CommittedScroll'))
                                        idx = (getMyMidIdx() + pos)
                                        print pos,
                                        print idx
                                        item = g_MyPawnItemList.at(idx)
                                        cancelitem = [item.m_nPropID,
                                         item.m_szPropName,
                                         item.m_nPrice,
                                         item.m_nNum,
                                         item.m_nInterval,
                                         item.m_iSaleIndex]
                                        print item.m_nNum
                                        RequestCommitGoods2Pawn(CancelCommit2Pawn, cancelitem)
                                        PlaySound(soundUI, 1)





                        class CommittedItem1(CommittedItem0):
                            __module__ = __name__
                            rect = (21,
                             (17 + (33 * 1)),
                             282,
                             32)

                        class CommittedItem2(CommittedItem0):
                            __module__ = __name__
                            rect = (21,
                             (17 + (33 * 2)),
                             282,
                             32)

                        class CommittedItem3(CommittedItem0):
                            __module__ = __name__
                            rect = (21,
                             (17 + (33 * 3)),
                             282,
                             32)

                        class CommittedItem4(CommittedItem0):
                            __module__ = __name__
                            rect = (21,
                             (17 + (33 * 4)),
                             282,
                             32)

                        class CommittedItem5(CommittedItem0):
                            __module__ = __name__
                            rect = (21,
                             (17 + (33 * 5)),
                             282,
                             32)

                        class CommittedScroll(TVScroll):
                            __module__ = __name__
                            rect = (305,
                             20,
                             26,
                             192)
                            pos = 0

                            def OnPosChange():
                                scrRange = max((MyPawnItemListCnt - defCommittedCnt), 0)
                                Win_SetRange((uiPawnShopDlg + '.CommitPanel.CommittedScroll'), scrRange)
                                pos = Win_GetPos((uiPawnShopDlg + '.CommitPanel.CommittedScroll'))
                                Cnt = min(defCommittedCnt, MyPawnItemListCnt)
                                for i in range(Cnt):
                                    ui = (uiPawnShopDlg + ('.CommitPanel.CommittedItem%d' % i))
                                    info = g_MyPawnItemList.at((i + pos))
                                    if ((None == info) and Win_SetText((ui + '.PropName'), '')):
                                        Win_SetText((ui + '.PropNum'), '')
                                        Win_SetText((ui + '.interval'), '')
                                        Win_SetText((ui + '.price'), '')
                                        Win_ShowWidget(ui, 0)



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
                                    rect = (2,
                                     2,
                                     26,
                                     42)
                                    bkimage = 'object/ui/common/scl_block.img'

                                class spinup(TSpinDec):
                                    __module__ = __name__
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]
                                    rect = (6,
                                     -15,
                                     18,
                                     18)
                                    bkimage = 'object/ui/forge/scl_up.img'

                                    def OnClick(this):
                                        PlaySound(soundUI, 1)



                                class spindown(TSpinInc):
                                    __module__ = __name__
                                    framescheme = [(0,
                                      0,
                                      2,
                                      2,
                                      3,
                                      3,
                                      1,
                                      1)]
                                    rect = (6,
                                     191,
                                     18,
                                     18)
                                    bkimage = 'object/ui/forge/scl_down.img'

                                    def OnClick(this):
                                        PlaySound(soundUI, 1)







                class SearchPropName(TEdit):
                    __module__ = __name__
                    initlayer = 99999
                    rect = (98,
                     44,
                     100,
                     18)
                    captionrect = (0,
                     5,
                     100,
                     12)
                    drawcolor = lightColor
                    textEdgeColor = maskColor
                    textstyle = (dt_left + dt_bottom)
                    caption = ''
                    maxchar = 30

                    def OnClick(this):
                        Win_SetFocus((uiPawnShopDlg + '.SearchPropName'))



                    def OnTab():
                        Win_SetFocus((uiPawnShopDlg + '.Rank'))



                class Rank(TEditID):
                    __module__ = __name__
                    initlayer = 99999
                    rect = (260,
                     43,
                     24,
                     18)
                    captionrect = (-2,
                     7,
                     26,
                     18)
                    drawcolor = lightColor
                    textEdgeColor = maskColor
                    textstyle = dt_right
                    maxchar = 3

                    def OnClick(this):
                        Win_SetFocus((uiPawnShopDlg + '.Rank'))



                    def OnTab():
                        Win_SetFocus((uiPawnShopDlg + '.SearchPropName'))



                class updateSearchBtn(TButton):
                    __module__ = __name__
                    rect = (300,
                     38,
                     76,
                     31)
                    bkimage = 'object/ui/deal/updateBtn.img'

                    def OnClick(this):
                        propname = Win_GetText((uiPawnShopDlg + '.SearchPropName'))
                        rank = int(Win_GetText((uiPawnShopDlg + '.Rank')))
                        print ('[updateSearchBtn]propName = %s,rank = %d' % (propname,
                         rank))
                        namelist = [propname,
                         rank]
                        RequestSearchItemByName(namelist)
                        PlaySound(soundUI, 1)



                class residualBill(TEditID):
                    __module__ = __name__
                    editable = 0
                    initlayer = 550001
                    maxchar = 12
                    rect = (684,
                     48,
                     81,
                     16)
                    drawcolor = lightColor
                    textEdgeColor = maskColor
                    captionrect = (2,
                     2,
                     78,
                     16)
                    textstyle = dt_right

                class buyTipDlg(TStatic):
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
                                if ShowMyPawned:
                                    cancelitem = [buyItemInfo[0],
                                     '',
                                     buyItemInfo[1],
                                     buyItemInfo[3],
                                     12,
                                     buyItemInfo[2]]
                                    RequestCommitGoods2Pawn(CancelCommit2Pawn, cancelitem)
                                else:
                                    RequestBuyGoodsInPawnShop(buyItemInfo)
                                Win_ShowWidget((uiPawnShopDlg + '.buyTipDlg'), 0)



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
                                Win_ShowWidget((uiPawnShopDlg + '.buyTipDlg'), 0)



                        class prompt(TLabel):
                            __module__ = __name__
                            rect = (42,
                             84,
                             280,
                             130)
                            textEdgeType = -1
                            drawcolor = zoneChooseColor



                class pawnedBtn(TTabWin):
                    __module__ = __name__
                    rect = (0,
                     0,
                     80,
                     33)
                    hotrect = (271,
                     513,
                     80,
                     33)
                    groupstop = 0
                    initlayer = 600010
                    hotcover = 'object/ui/deal/tab_pawned.img'

                    def OnClick(this):
                        global ShowMyPawned
                        ShowMyPawned = 1
                        ClearWareList()
                        ui_updatePawnTypeList()
                        ui_ShowMyPawnedInWare(0)



                class pawningBtn(TTabWin):
                    __module__ = __name__
                    rect = (0,
                     0,
                     80,
                     33)
                    hotrect = (189,
                     513,
                     80,
                     33)
                    groupstop = 1
                    initlayer = 600010
                    hotcover = 'object/ui/deal/tab_pawning.img'

                    def OnClick(this):
                        global ShowMyPawned
                        ShowMyPawned = 0
                        print 'begin call ui_updatePawnTypeList'
                        ui_updatePawnTypeList()







UI.children.selRoom = UI_children_selRoom

#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
