import sys
faceIconList = ['/aiq',
 '/am',
 '/bb',
 '/bei',
 '/baiy',
 '/bz',
 '/cy',
 '/dao',
 '/db',
 '/dg',
 '/dh',
 '/dk',
 '/dp',
 '/ds',
 '/dx',
 '/dy',
 '/fad',
 '/fan',
 '/fd',
 '/feid',
 '/fendou',
 '/fn',
 '/gf',
 '/gg',
 '/hanx',
 '/hx',
 '/hy',
 '/jie',
 '/jk',
 '/jy',
 '/ka',
 '/kl',
 '/kuk',
 '/kun',
 '/lh',
 '/ll',
 '/lw',
 '/maom',
 '/mg',
 '/mm',
 '/ng',
 '/pz',
 '/qianc',
 '/qiang',
 '/qiao',
 '/ruo',
 '/se',
 '/shan',
 '/shd',
 '/shl',
 '/shuai',
 '/shui',
 '/sj',
 '/tiao',
 '/tp',
 '/tu',
 '/tx',
 '/ty',
 '/wen',
 '/ws',
 '/wx',
 '/xg',
 '/xin',
 '/xs',
 '/xu',
 '/yb',
 '/yiw',
 '/yj',
 '/yl',
 '/yun',
 '/yw',
 '/yy',
 '/zhao',
 '/zhd',
 '/zhem',
 '/zhm',
 '/zj',
 '/zk',
 '/zq',
 '/zt']
faceIconList = ['/m00',
 '/m01',
 '/m02',
 '/m03',
 '/m04',
 '/m05',
 '/m06',
 '/m07',
 '/m08',
 '/m09',
 '/m10',
 '/m11',
 '/m12',
 '/m13',
 '/m14',
 '/m15',
 '/m16',
 '/m17',
 '/m18',
 '/m19',
 '/m20',
 '/m21',
 '/m22',
 '/m23',
 '/kdz',
 '/klz',
 '/kyl',
 '/kym',
 '/kyh',
 '/kxy',
 '/krh',
 '/kqq',
 '/kpx',
 '/kot',
 '/kku',
 '/kkx',
 '/khan',
 '/khx',
 '/khd',
 '/kgd',
 '/kfb',
 '/kfs',
 '/kdk',
 '/kcb',
 '/kbt',
 '/kbs',
 '/kbz',
 '/k23',
 '/jy',
 '/pz',
 '/se',
 '/fd',
 '/dy',
 '/ll',
 '/hx',
 '/bz',
 '/shui',
 '/dk',
 '/gg',
 '/fn',
 '/tp',
 '/cy',
 '/wx',
 '/ng',
 '/kuk',
 '/feid',
 '/zk',
 '/tu',
 '/tx',
 '/ka',
 '/baiy',
 '/am',
 '/jie',
 '/kun',
 '/jk',
 '/lh',
 '/hanx',
 '/db',
 '/fendou',
 '/zhm',
 '/yiw',
 '/xu',
 '/yun',
 '/zhem',
 '/shuai',
 '/kl',
 '/qiao',
 '/zj',
 '/shan',
 '/fad',
 '/aiq',
 '/tiao',
 '/zhao',
 '/mm',
 '/zt',
 '/maom',
 '/xg',
 '/yb',
 '/qianc',
 '/dp',
 '/bei',
 '/dg',
 '/shd',
 '/zhd',
 '/dao',
 '/zq',
 '/yy',
 '/bb',
 '/gf',
 '/fan',
 '/yw',
 '/mg',
 '/dx',
 '/wen',
 '/xin',
 '/xs',
 '/hy',
 '/lw',
 '/dh',
 '/sj',
 '/yj',
 '/ds',
 '/ty',
 '/yl',
 '/qiang',
 '/ruo',
 '/ws',
 '/shl',
 '/dd',
 '/mn',
 '/hl',
 '/mamao',
 '/qz',
 '/fw',
 '/oh',
 '/bj',
 '/qsh',
 '/xiq',
 '/xy',
 '/duoy',
 '/xr',
 '/xixing',
 '/nv',
 '/nan']
memberFaceIconList = ['/m00',
 '/m01',
 '/m02',
 '/m03',
 '/m04',
 '/m05',
 '/m06',
 '/m07',
 '/m08',
 '/m09',
 '/m10',
 '/m11',
 '/m12',
 '/m13',
 '/m14',
 '/m15',
 '/m16',
 '/m17',
 '/m18',
 '/m19',
 '/m20',
 '/m21',
 '/m22',
 '/m23']
initFaceIconList(faceIconList)

def do(wgt, func):
    do2(wgt, func)



def do2(wgt, func):
    if (wgt.__dict__.has_key(func) and wgt.__dict__[func]()):
        pass



def do3(wgt, func, arg):
    if (wgt.__dict__.has_key(func) and wgt.__dict__[func](arg)):
        pass



def do4(wgt, func, arg1, arg2):
    if (wgt.__dict__.has_key(func) and wgt.__dict__[func](arg1, arg2)):
        pass



def doUI(ui, func):
    value = ''
    i = 0
    while 1:
        j = ui.find('.', i)
        if (j == -1):
            value += ui[i:]
            break
        else:
            value += (ui[i:j] + '.children.')
            i = (j + 1)

    if ((func == 'OnClick') and do3(eval(value), func, ui)):
        pass


class MyStdout:
    __module__ = __name__

    def write(self, s):
        Win_ConsolePrint(s)



sys.stdout = MyStdout()
sys.stderr = MyStdout()

def getMyIdx():
    me = Win_GetFocusPath()
    return getTailNum(me)



def getMyIdx2():
    me = Win_GetMyPath()
    return getTailNum(me)



def getTailNum(s):
    if ((s[-2] >= '0') and (s[-2] <= '9')):
        return int(s[-2:])
    elif ((s[-1] >= '0') and (s[-1] <= '9')):
        return int(s[-1:])
    else:
        return 0



def getMidIdx(s):
    for i in range(len(s)):
        if ((s[i] >= '0') and (s[i] <= '9')):
            if ((i + 1) >= len(s)):
                return int(s[i])
            if ((s[(i + 1)] >= '0') and (s[(i + 1)] <= '9')):
                return int(s[i:(i + 2)])
            else:
                return int(s[i])




def getMyMidIdx():
    me = Win_GetMyPath()
    return getMidIdx(me)



def ui_setCapture(widget):
    Win_ShowWidget(widget, True)
    Win_SetFocus(widget)
    Win_SetCapture(widget)



def getLevelPic(level):
    level = min(max(1, level), 225)
    return ('res/uires/level/%03d.img' % level)



def go2shop():
    global localShopVersion
    serverID = GetRandShopServerID()
    localShopVersion = lastestShopVersion
    SetLocalShopVertion(uin, lastestShopVersion)
    if (0 != serverID):
        print 'EnterShop,',
        print uin,
        print serverID
        print 'InitializeShop()'
        InitializeShop()
        EnterShop(uin, serverID)
        PlaySound(soundMain, 1)



def isMapExist(ID):
    index = -1
    for i in range(len(mapDesc)):
        if (mapDesc[i][0] == ID):
            index = i
            break

    if (index == -1):
        return 0
    else:
        return 1



def getMapDesc(ID):
    for i in range(len(mapDesc)):
        if (mapDesc[i][0] == ID):
            return mapDesc[i]

    for i in range(len(mapDesc)):
        if (mapDesc[i][5] == 8):
            return mapDesc[i]




def getMapTypeByID(ID):
    return getMapDesc(ID)[1]



def getMapDescByID(ID):
    return getMapDesc(ID)[2]



def getMapSizeXByID(ID):
    return getMapDesc(ID)[3]



def getMapSizeYByID(ID):
    return getMapDesc(ID)[4]



def getMapMaxPlayerNumByID(ID):
    return getMapDesc(ID)[5]



def getMapFilenameByID(ID):
    return getMapDesc(ID)[6]



def getThumbnailFilenameByID(ID):
    return getMapDesc(ID)[7]



def getSoundFxFilenameByID(ID):
    return getMapDesc(ID)[8]



def getMapPointByID(ID):
    return getMapDesc(ID)[9]



def getDetailDescByID(ID):
    return getMapDesc(ID)[10]



def getTotalMapCount():
    return len(mapDesc)



def getMapIdByIndex(index):
    '\n    \xb8\xf9\xbe\xddindex\xb5\xc3\xb5\xbd\xb5\xd8\xcd\xbc\xb5\xc4ID\n    '
    if ((index < 0) or (index >= len(mapDesc))):
        return 0
    return mapDesc[index][0]



def getMapFilenameByIndex(index):
    '\n    \xb8\xf9\xbe\xddindex\xb5\xc3\xb5\xbd\xb5\xd8\xcd\xbc\xc3\xfb\xb3\xc6\n    '
    if ((index < 0) or (index >= len(mapDesc))):
        return ''
    return mapDesc[index][6]



def getThumbnailFilenameByIndex(index):
    '\n    \xb8\xf9\xbe\xddindex\xb5\xc3\xb5\xbd\xb5\xd8\xcd\xbc\xcb\xf5\xc2\xd4\xcd\xbc\xb5\xc4\xc3\xfb\xb3\xc6\n    '
    if ((index < 0) or (index >= len(mapDesc))):
        return ''
    return mapDesc[index][7]



def mapID2name(ID):
    if (0 == ID):
        return '\xcb\xe6\xbb\xfa\xb5\xd8\xcd\xbc'
    index = 0
    for i in range(len(mapDesc)):
        if (mapDesc[i][0] == ID):
            index = i
            break

    name = mapDesc[index][2]
    type = mapDesc[index][1]
    return name


screenEnterWeb = ''

def ui_jumpHelpWeb():
    global screenEnterWeb
    screenEnterWeb = Win_GetCurScreen()
    PlaySound(soundMain, 1)
    GotoUIScreen('web')
    JumpHelpWeb('http://qqtang.qq.com/game/help/operation.htm')



def ui_jumpOfficialWeb():
    global screenEnterWeb
    screenEnterWeb = Win_GetCurScreen()
    PlaySound(soundMain, 1)
    GotoUIScreen('web')
    JumpHelpWeb('http://qqtang.qq.com')



def ui_jumpLeagueWeb():
    global screenEnterWeb
    screenEnterWeb = Win_GetCurScreen()
    PlaySound(soundMain, 1)
    GotoUIScreen('web')
    JumpHelpWeb('http://newqqtang.qq.com/vip/')



def ui_jumpWeb(url):
    global screenEnterWeb
    screenEnterWeb = Win_GetCurScreen()
    PlaySound(soundMain, 1)
    GotoUIScreen('web')
    JumpHelpWeb(url)



def ui_showMemberWeb(url, flag):
    global joinMemberURL
    global exitFlag
    exitFlag = flag
    joinMemberURL = url
    ui_setCapture('UI.joinMemberWeb')
    sc_ShowWeb('joinmember', 230, 198, 325, 200, joinMemberURL)



def GetItemTypeName(ID):
    if (not itemList.has_key(ID)):
        type = ''
    else:
        type = itemList[ID][0]
    return type



def GetSubIDByItemID(ID):
    if (not itemList.has_key(ID)):
        return 0
    else:
        return itemList[ID][1]


QB = -1
gameMoney = -1
sugarMoney = -1
QQTTicket = 0

def getMoney():
    return (QB,
     gameMoney,
     sugarMoney)



def ui_NotifyMoney(iQB, iGameMoney, iSugarMoney):
    global sugarMoney
    global QQTTicket
    global QB
    global gameMoney
    print 'ui_NotifyMoney'
    QB = iQB
    gameMoney = iGameMoney
    sugarMoney = iSugarMoney
    ticketInfo = GetMyTicket()
    QQTTicket = ticketInfo.m_iNumOfItem
    if ((-1 == sugarMoney) and Win_SetText('UI.shop.sugarMoney', '')):
        pass
    if ((QQTTicket < 0) and Win_SetText('UI.shop.shopTicket', '')):
        pass



def ui_updateTicket():
    global QQTTicket
    print 'ui_updateTicket()'
    ticketInfo = GetMyTicket()
    QQTTicket = ticketInfo.m_iNumOfItem
    if ((QQTTicket < 0) and Win_SetText('UI.shop.shopTicket', '')):
        pass


game_mapID = 0

def game_setMapID(mapID):
    global game_mapID
    if (Win_GetCurScreen() == 'game'):
        info = getMapDesc(mapID)
        Win_SetImg((uiGamePlayerList + '.mapIcon'), ('map/icon/%s.img' % info[1]))
        setSelectedMapType(info[1])
        name = info[2].replace('\n', '')
        Win_SetText((uiGamePlayerList + '.mapName'), name)
        game_mapID = mapID



def getMyUin():
    return uin



def NotifyMyUin(myUin):
    global uin
    print 'NotifyMyUin',
    print myUin
    uin = myUin



def filterChatMsg(msg):
    if (msg != ''):
        msg = msg.replace('/<h>', '')
        msg = msg.replace('/<H>', '')
    return msg


bFruitUpdate = 0

def ui_NotifyUpdateFruit():
    global bFruitUpdate
    bFruitUpdate = 1



def onStopEffect(id):
    pass


#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
