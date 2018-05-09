isDispNotBuy = False
curMoneyType = 'QB'
defWareCnt = 12
isAllowMixedPay = 1
isAllowQBMixedPay = 1
isAllowPresentMixedPay = 1
removeItemID = 0
curDispWares = ([0] * 12)
wareIDs = []
buyModes = []
itemType = 2
itemSubType = 1
itemCnt = 0
itemPos = [0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0]
disableItemCnt = 0
disableItemPos = 0
activeItemInRecycler = 999999
defRecyclerCnt = 9
g_curLightSpeed = 0
myItemType = 2
myItemLastSelect = -1
bClickSaveEquip = 0
warePos = [[0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0],
 [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0]]
noneCheck = [[-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1],
 [-1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1,
  -1]]
wareCheck = noneCheck
Affectionlist = [0,
 0,
 0,
 0,
 0,
 0]
useAffections = {'1': None,
 '2': None,
 '3': None,
 '4': None,
 '5': None,
 '6': None}
useItems = {'platform': None,
 'item': None,
 'card': None,
 'bomb': None,
 'huanying': None,
 'bg': None,
 'frame': None,
 'enter': None,
 'cap': None,
 'fhadorn': None,
 'bhadorn': None,
 'thadorn': None,
 'hair': None,
 'mask': None,
 'eye': None,
 'mouth': None,
 'ear': None,
 'cloth': None,
 'cladorn': None,
 'fpack': None,
 'npack': None,
 'leg': None,
 'foot': None,
 'egg': None,
 'tool': None,
 'costume': None,
 'namecard': None,
 'footprint': None,
 'namecardbound': None,
 'xeffect': None,
 'feffect': None,
 'body': None}
selectedItems = {'bomb': None,
 'huanying': None,
 'bg': None,
 'frame': None,
 'enter': None,
 'cap': None,
 'fhadorn': None,
 'bhadorn': None,
 'thadorn': None,
 'hair': None,
 'mask': None,
 'eye': None,
 'mouth': None,
 'ear': None,
 'cloth': None,
 'cladorn': None,
 'fpack': None,
 'npack': None,
 'leg': None,
 'foot': None,
 'namecard': None,
 'footprint': None,
 'namecardbound': None}
type2MyType = {'bomb': 3,
 'huanying': 3,
 'bg': 3,
 'frame': 3,
 'enter': 3,
 'cap': 4,
 'fhadorn': 4,
 'bhadorn': 4,
 'thadorn': 4,
 'hair': 4,
 'mask': 4,
 'eye': 4,
 'mouth': 4,
 'ear': 4,
 'cloth': 4,
 'cladorn': 4,
 'fpack': 4,
 'npack': 4,
 'leg': 4,
 'foot': 4,
 'namecard': 3,
 'footprint': 4,
 'namecardbound': 3}
g_ItemsNotPreview = ('xeffect',
 'feffect',
 'platform',
 'item',
 'card')
g_ItemsPreview = ('footprint',
 'bomb',
 'huanying')
fruitState = 0
validateState = 0
isStorageVisible = 0
forgeTypeCnt = 0
forgeItemCnt = 0
forgeMeterialCnt = 0
forgeExpand = -1
forgeItemID = 0
defForgeCnt = 16
defForgeMeterCnt = 7
composeTypeCnt = 0
composeItemCnt = 0
composeExpand = -1
composeItemID = 0
defComposeCnt = 16
defComposeMeterCnt = 3
tasksIdList = []
currentTaskIdx = 0
currentEggId = 0
secrecyValidateID = 1
questionCnt = 3
questionNum = 3
currentQuestionID = 0
currentQuestionID1 = 0
currentQuestionID2 = 1
questionIDList = ['1',
 '2',
 '3']
answerList = ['',
 '',
 '']
coorList = ['0',
 '0',
 '0']
coorNum = 3
coorSize = 2
from time import time

def setNudeState():
    global useItems
    for type in equipMap.keys():
        if ((useItems[type] != None) and shopPlayer_wear(type, 0, 0, 0)):
            pass

    for type in g_ItemsPreview:
        if ((useItems[type] != None) and shopPlayer_wear(type, 0, 0, 0)):
            pass

    Win_SetImg('UI.shop.preview.bg', '')
    Win_SetImg('UI.shop.preview.enter', '')
    Win_SetImg('UI.shop.preview.frame', '')
    Win_SetImg('UI.shop.namecardPreview.namecard', '')
    Win_SetImg('UI.shop.namecardPreview.namecardbound', '')
    useItems = {'platform': None,
     'item': None,
     'card': None,
     'bomb': None,
     'huanying': None,
     'bg': None,
     'frame': None,
     'enter': None,
     'cap': None,
     'fhadorn': None,
     'bhadorn': None,
     'thadorn': None,
     'hair': None,
     'mask': None,
     'eye': None,
     'mouth': None,
     'ear': None,
     'cloth': None,
     'cladorn': None,
     'fpack': None,
     'npack': None,
     'leg': None,
     'foot': None,
     'egg': None,
     'tool': None,
     'costume': None,
     'namecard': None,
     'footprint': None,
     'namecardbound': None,
     'xeffect': None,
     'feffect': None,
     'body': None}
    clearChecks()
    for i in range(len(wareCheck)):
        for j in range(len(wareCheck[0])):
            wareCheck[i][j] = -1





def clearChecks():
    for i in range(defWareCnt):
        Win_SetCheck(('UI.shop.ware%d' % (i + 1)), False)
        Win_ShowWidget((('UI.shop.ware%d' % (i + 1)) + '.frame'), 0)




def clearAllChecks():
    for i in range(len(wareCheck)):
        for j in range(len(wareCheck[0])):
            wareCheck[i][j] = -1





def setWareCheck():
    clearChecks()
    idx = (wareCheck[itemType][itemSubType] - warePos[itemType][itemSubType])
    if ((idx in range(1, (defWareCnt + 1))) and Win_SetCheck(('UI.shop.ware%d' % idx), True)):
        Win_ShowWidget((('UI.shop.ware%d' % idx) + '.frame'), 1)



def clearAllPos():
    for i in range(len(warePos)):
        for j in range(len(warePos[i])):
            warePos[i][j] = 0




charIconList = ['xwk',
 'tt',
 'xq',
 'cl',
 'bbl',
 'hy',
 'mly',
 'hwz',
 'boy',
 '',
 '',
 '',
 'kl',
 'nz',
 'wll',
 'yy',
 '',
 'yd',
 'ld',
 'ge',
 'tb',
 'girl']

def useSth(sth, ID, canOff):
    global myItemLastSelect
    ID = int(ID)
    if (not sth.has_key(ID)):
        return 
    desc = sth[ID]
    (type, idx,) = desc[0:2]
    if ((canOff and (useItems[type] == ID)) and unUseWare(ID)):
        return 
    if (canOff and ((type in selectedItems.keys()) and (myItemLastSelect != -1))):
        selectedItems[type] = myItemLastSelect
        myItemLastSelect = -1
    if (not canOff):
        selectedItems[type] = None
    if (type in g_ItemsNotPreview):
        useItems[type] = ID
    elif (type in g_ItemsPreview):
        useItems[type] = ID
        itemInfo = GetItemInfoFromSec(ID)
        shopPlayer_wear(type, idx, itemInfo.m_bItemEffect, itemInfo.m_bItemColor)
    elif ('bg' == type):
        useItems[type] = ID
        Win_SetImg('UI.shop.preview.bg', ('object/bg/bg%d_stand.img' % idx))
    elif ('frame' == type):
        useItems[type] = ID
        Win_SetImg('UI.shop.preview.frame', ('object/frame/frame%d_stand.img' % idx))
    elif ('enter' == type):
        useItems[type] = ID
        Win_SetImg('UI.shop.preview.enter', ('object/enter/enter%d_stand.img' % idx))
    elif ('namecard' == type):
        useItems[type] = ID
        Win_SetImg('UI.shop.namecardPreview.namecard', ('object/namecard/namecard%d_stand.img' % idx))
    elif ('namecardbound' == type):
        useItems[type] = ID
        Win_SetImg('UI.shop.namecardPreview.namecardbound', ('object/namecardbound/namecardbound%d_stand.img' % idx))
    elif equipMap.has_key(type):
        useItems[type] = ID
        pos = equipMap[type]
        if ('cap' == type):
            useItems['hair'] = None
            selectedItems['hair'] = None
            shopPlayer_wear('hair', 0, 0, 0)
        if ('hair' == type):
            useItems['cap'] = None
            selectedItems['cap'] = None
            shopPlayer_wear('cap', 100, 0, 0)
        itemInfo = GetItemInfoFromSec(ID)
        shopPlayer_wear(type, idx, itemInfo.m_bItemEffect, itemInfo.m_bItemColor)
    elif ((ID >= 20000) and (ID < 23000)):
        RoleId = shopPlayer_getRoleIdx()
        if ((GetAllowWear(RoleId, ID) == -1) and NotifyNoWear()):
            return 
        shopPlayer_wear('body', idx, 0, 0)
        if (GetAffectionItem(RoleId, ID) == 0):
            return 
        useItems['body'] = ID
        i = 0
        isExistItem = 0
        for i in range(6):
            if (Affectionlist[i] == ID):
                isExistItem = 1
                j = (i + 1)
                strUI = ('UI.shop.Affection%d' % j)
                Affectionlist[i] = ID
                Win_ShowWidget(strUI, True)
                Win_SetImg(strUI, ('res/uires/icon/body/body%d.img' % ID))
                Win_SetText((strUI + '.ID'), str(ID))
                return 

        i = 0
        for key in useAffections.keys():
            i = (i + 1)
            if (useAffections[key] == None):
                useAffections[key] = ID
                strUI = ('UI.shop.Affection%d' % i)
                j = (i - 1)
                Affectionlist[j] = ID
                Win_ShowWidget(strUI, True)
                Win_SetImg(strUI, ('res/uires/icon/body/body%d.img' % ID))
                Win_SetText((strUI + '.ID'), str(ID))
                return 

    updateSelectedItems()



def unUseWare(ID):
    ID = int(ID)
    if (not itemList.has_key(ID)):
        return 
    desc = itemList[ID]
    (type, idx,) = desc[0:2]
    print 'unUseWare',
    print ID,
    print type,
    print idx
    if (type in selectedItems.keys()):
        selectedItems[type] = None
    updateSelectedItems()
    if (type in g_ItemsNotPreview):
        useItems[type] = None
    elif (type in g_ItemsPreview):
        useItems[type] = None
        shopPlayer_wear(type, 0, 0, 0)
    elif ('bg' == type):
        useItems['bg'] = None
        Win_SetImg('UI.shop.preview.bg', '')
    elif ('frame' == type):
        useItems['frame'] = None
        Win_SetImg('UI.shop.preview.frame', '')
    elif ('enter' == type):
        useItems['enter'] = None
        Win_SetImg('UI.shop.preview.enter', '')
    elif ('namecard' == type):
        useItems['namecard'] = None
        Win_SetImg('UI.shop.namecardPreview.namecard', '')
    elif ('namecardbound' == type):
        useItems['namecardbound'] = None
        Win_SetImg('UI.shop.namecardPreview.namecardbound', '')
    elif equipMap.has_key(type):
        useItems[type] = None
        shopPlayer_wear(type, 0, 0, 0)



def useWare(ID):
    useSth(commodityList, ID, 0)



def useItem(ID):
    useSth(itemList, ID, 1)



def deleteItem(ID):
    if (not itemList.has_key(ID)):
        return 
    desc = itemList[ID]
    (type, idx,) = desc[0:2]
    if ((useItems[type] == ID) and unUseWare(ID)):
        pass
    ChangeItemStatus(uin, ID, 2)



def getCharIconName():
    i = shopPlayer_getRoleIdx()
    if ((i < 1) or (i > 22)):
        return ''
    else:
        return ('object/ui/shop/charIcon/%s.img' % charIconList[(i - 1)])



def day2str(day):
    if (day > 30):
        return (str((day / 30)) + ' \xb8\xf6\xd4\xc2')
    else:
        return (str(day) + ' \xcc\xec')



def clearLightIcon():
    for type in selectedItems.keys():
        Win_ShowWidget(('UI.shop.lighticon.%s' % type), 0)




def clearSelected():
    for type in selectedItems.keys():
        selectedItems[type] = None

    for i in range(15):
        Win_ShowWidget(('UI.shop.item%d.frame' % (i + 1)), 0)




def updateSelectedItems():
    for i in range(15):
        Win_ShowWidget(('UI.shop.item%d.frame' % (i + 1)), 0)

    for type in type2MyType.keys():
        if (((type2MyType[type] == myItemType) and ((selectedItems[type] > itemPos[myItemType]) and (selectedItems[type] <= (itemPos[myItemType] + 15)))) and Win_ShowWidget(('UI.shop.item%d.frame' % (selectedItems[type] - itemPos[myItemType])), 1)):
            pass




def InitPlayerActiveItems():
    RoleID = shopPlayer_getRoleIdx()
    clearLightIcon()
    petsIdList = GetPlayerAllPetsId()
    if ((len(petsIdList) > 0) and Win_ShowWidget('UI.shop.lighticon.pet', 1)):
        pass
    for type in g_ItemsNotPreview:
        ItemID = GetRoleItem(RoleID, type)
        if (ItemID == -1):
            useItems[type] = None
        else:
            useItems[type] = ItemID

    for type in g_ItemsPreview:
        ItemID = GetRoleItem(RoleID, type)
        if (ItemID == -1):
            useItems[type] = None
        else:
            useItems[type] = ItemID
            Win_ShowWidget(('UI.shop.lighticon.%s' % type), 1)
            if itemList.has_key(ItemID):
                desc = itemList[ItemID]
                idx = desc[1]
                itemInfo = GetItemInfoFromSec(ItemID)
                shopPlayer_wear(type, idx, itemInfo.m_bItemEffect, itemInfo.m_bItemColor)

    ItemID = GetRoleItem(RoleID, 'bg')
    if (ItemID == -1):
        useItems['bg'] = None
    else:
        useItems['bg'] = ItemID
        Win_ShowWidget('UI.shop.lighticon.bg', 1)
        if itemList.has_key(ItemID):
            desc = itemList[ItemID]
            idx = desc[1]
            Win_SetImg('UI.shop.preview.bg', ('object/bg/bg%d_stand.img' % idx))
    ItemID = GetRoleItem(RoleID, 'frame')
    if (ItemID == -1):
        useItems['frame'] = None
    else:
        useItems['frame'] = ItemID
        Win_ShowWidget('UI.shop.lighticon.frame', 1)
        if itemList.has_key(ItemID):
            desc = itemList[ItemID]
            idx = desc[1]
            Win_SetImg('UI.shop.preview.frame', ('object/frame/frame%d_stand.img' % idx))
    ItemID = GetRoleItem(RoleID, 'enter')
    if (ItemID == -1):
        useItems['enter'] = None
    else:
        useItems['enter'] = ItemID
        Win_ShowWidget('UI.shop.lighticon.enter', 1)
        if itemList.has_key(ItemID):
            desc = itemList[ItemID]
            idx = desc[1]
            Win_SetImg('UI.shop.preview.enter', ('object/enter/enter%d_stand.img' % idx))
    ItemID = GetRoleItem(RoleID, 'namecard')
    if (ItemID == -1):
        useItems['namecard'] = None
    else:
        useItems['namecard'] = ItemID
        Win_ShowWidget('UI.shop.lighticon.namecard', 1)
        if itemList.has_key(ItemID):
            desc = itemList[ItemID]
            idx = desc[1]
            Win_SetImg('UI.shop.namecardPreview.namecard', ('object/namecard/namecard%d_stand.img' % idx))
    ItemID = GetRoleItem(RoleID, 'namecardbound')
    if (ItemID == -1):
        useItems['namecardbound'] = None
    else:
        useItems['namecardbound'] = ItemID
        Win_ShowWidget('UI.shop.lighticon.namecardbound', 1)
        if itemList.has_key(ItemID):
            desc = itemList[ItemID]
            idx = desc[1]
            Win_SetImg('UI.shop.namecardPreview.namecardbound', ('object/namecardbound/namecardbound%d_stand.img' % idx))
    for type in equipMap.keys():
        ItemID = GetRoleItem(RoleID, type)
        if (ItemID == -1):
            useItems[type] = None
        else:
            useItems[type] = ItemID
            Win_ShowWidget(('UI.shop.lighticon.%s' % type), 1)
            if (not itemList.has_key(ItemID)):
                continue
            desc = itemList[ItemID]
            idx = desc[1]
            itemInfo = GetItemInfoFromSec(ItemID)
            shopPlayer_wear(type, idx, itemInfo.m_bItemEffect, itemInfo.m_bItemColor)

    clearSelected()



def sendActiveItems():
    list = []
    for key in useItems.keys():
        if ((useItems[key] != None) and list.append(useItems[key])):
            pass

    num = len(list)
    ActiveItemStatus(uin, shopPlayer_getRoleIdx(), num, list)



def setItemType(type):
    global myItemType
    global itemType
    Win_ShowWidget('UI.shop.fruitMachine', 0)
    Win_ShowWidget('UI.shop.AD', 0)
    itemType = type
    if (1 < type):
        myItemType = type
    if ((1 == type) and Win_SelectSelf('UI.shop.adviceTab')):
        Win_SelectSelf('UI.shop.subTab1')
        initFruitMachine()
    if ((2 == type) and Win_SelectSelf('UI.shop.functionTab')):
        Win_SelectSelf('UI.shop.subTab1')
        Win_SelectSelf('UI.shop.myFunction')
    if ((3 == type) and Win_SelectSelf('UI.shop.costumeTab')):
        Win_SelectSelf('UI.shop.subTab1')
        Win_SelectSelf('UI.shop.myCostume')
    if ((4 == type) and Win_SelectSelf('UI.shop.equipTab')):
        Win_SelectSelf('UI.shop.subTab1')
        Win_SelectSelf('UI.shop.myEquip')
    if ((5 == type) and Win_SelectSelf('UI.shop.petTab')):
        Win_SelectSelf('UI.shop.subTab1')
        Win_SelectSelf('UI.shop.mypet')
    if ((6 == type) and Win_SelectSelf('UI.shop.purplediamondTab')):
        Win_SelectSelf('UI.shop.subTab1')
        Win_SelectSelf('UI.shop.myturplediamond')
    setItemSubType(1)
    ui_updateAll()
    setWareCheck()



def setItemSubType(subType):
    global itemSubType
    if (((itemType == 1) and (subType == 1)) and initFruitMachine()):
        pass
    if ((subType != 1) and Win_ShowWidget('UI.shop.fruitMachine', 0)):
        Win_ShowWidget('UI.shop.AD', 0)
    itemSubType = subType
    ui_updateWares()
    ui_updateWarePages()
    setWareCheck()



def setDonateDlg():
    i = curBuyWareIdx
    buyMode = buyModes[i][0]
    wareID = wareIDs[i]
    if (wareID > 0):
        curBuyWareID = wareID
        info = WareList().at(itemType, itemSubType, (i + warePos[itemType][itemSubType]))
        ui = 'UI.shop.donateDlg'
        Win_SetText((ui + '.wareName'), info.name)
        Win_SetImg((ui + '.warePic'), info.picName)
        rebate = 100
        memberRebate = 100
        if ((info.rebate >= 0) and (info.rebate < 100)):
            rebate = info.rebate
        if (isLeague and ((info.memberRebate >= 0) and (info.memberRebate < 100))):
            memberRebate = info.memberRebate
    if ((curMoneyType == 'QB') and Win_SetText((ui + '.price'), makeStr(15, ((((info.priceQQ * memberRebate) * rebate) + 9999) / 10000), ' Q\xb1\xd2', 1))):
        pass
    if Win_SetFocus((ui + '.receiveUin')):
        pass


class WareList:
    __module__ = __name__
    items = []

    def getCnt(this, type, subType):
        WareList.items = []
        cnt = fetchCommodityCnt(type, subType)
        for i in range(cnt):
            info = this._WareList__get(type, subType, i)
            if (info.hasClient and (isDispNotBuy or (((curMoneyType == 'QB') and ((info.priceQQ >= 0) or (info.priceGame >= 0))) or (((curMoneyType == 'VNet') and (info.priceQQ >= 0)) or ((curMoneyType == 'TangB') and (info.priceQQTang >= 0)))))):
                if WareList.items.append(info):
                    pass

        return len(WareList.items)



    def at(this, type, subType, wareIdx):
        if (wareIdx >= len(WareList.items)):
            return None
        return WareList.items[wareIdx]



    def __get(this, type, subType, wareIdx):
        info = CNil()
        ci = fetchCommodity(type, subType, wareIdx)
        info.name = ci.m_szCommodityName
        info.ID = ci.m_iCommodityID
        info.priceQQ = int(ci.m_iPriceQQ)
        info.priceGame = ci.m_iPriceQQGame
        info.priceQQTang = ci.m_iPriceQQTang
        info.attribute = ci.m_dwAttribute
        info.memberRebate = ci.m_bMemberRebate
        info.rebate = ci.m_bRebate
        item0 = fetchCommItem(type, subType, wareIdx, 0)
        info.period = item0.m_nAvailPeriod
        info.num = item0.m_iItemNum
        info.ID = max(info.ID, 1)
        if commodityList.has_key(info.ID):
            iconType = commodityList[info.ID][0]
            iconIdx = commodityList[info.ID][1]
            info.picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
             iconType,
             iconIdx))
            info.statement = commodityList[info.ID][3]
            info.hasClient = 1
        else:
            info.picName = 'res/uires/shop/salou.img'
            info.statement = ''
            info.hasClient = 0
        return info




def ui_updateAll():
    ui_updateMyItems()
    ui_updateWares()
    ui_updateWarePages()



def ui_updateWarePages():
    wareCnt = WareList().getCnt(itemType, itemSubType)
    curCnt = warePos[itemType][itemSubType]
    if ((itemType == 1) and (itemSubType == 1)):
        itemShowCnt = 8
    else:
        itemShowCnt = 12
    curPage = ((curCnt / itemShowCnt) + 1)
    if ((0 == (wareCnt % itemShowCnt)) and (0 != wareCnt)):
        totalPage = (wareCnt / itemShowCnt)
    else:
        totalPage = ((wareCnt / itemShowCnt) + 1)
    Win_SetText('UI.shop.warePage', ('%d/%d' % (curPage,
     totalPage)))



def num2chinese(num):
    if ((num < 10000) or ((num % 1000) != 0)):
        return str(num)
    if (0 == (num % 10000)):
        return (str((num / 10000)) + '\xcd\xf2')
    return ((str((num / 10000)) + '\xcd\xf2') + str(((num % 10000) / 1000)))



def makeStr(lenCnt, num, name, isJiao = 0):
    if isJiao:
        s = ((str((num / 10)) + '.') + str((num % 10)))
    else:
        s = num2chinese(num)
    spCnt = ((lenCnt - len(s)) - len(name))
    return ((s + (' ' * spCnt)) + name)



def ui_updateWares():
    global buyModes
    global wareIDs
    if ('shop' != Win_GetCurScreen()):
        return 
    wareCnt = WareList().getCnt(itemType, itemSubType)
    wareIDs = []
    buyModes = []
    setWareCheck()
    if ((itemType == 1) and (itemSubType == 1)):
        itemShowCnt = 8
    else:
        itemShowCnt = 12
    for i in range(12):
        Win_ShowWidget(('UI.shop.attr%d' % (i + 1)), 0)
        Win_SetImg(('UI.shop.attr%d' % (i + 1)), '')

    for i in range(itemShowCnt):
        ware = ('UI.shop.ware' + str((i + 1)))
        Win_EnableWidget(ware, 1)
        info = WareList().at(itemType, itemSubType, (i + warePos[itemType][itemSubType]))
        curDispWares[i] = info
        Win_ShowWidget(('UI.shop.attr%d' % (i + 1)), 0)
        if (((None == info) or ('' == info.name)) and Win_SetText((ware + '.ID'), '')):
            Win_ShowWidget(ware, True)
            Win_SetImg((ware + '.picture'), '')
            Win_SetText((ware + '.name'), '')
            Win_SetText((ware + '.price1'), '')
            Win_SetText((ware + '.price2'), '')
            Win_ShowWidget((ware + '.buyA'), False)
            Win_SetImg(('UI.shop.attr%d' % (i + 1)), '')
            Win_ShowWidget((ware + '.memberPic'), 0)
            Win_SetImg((ware + '.pricePic'), '')
            Win_SetText((ware + '.memberPrice'), '')
            Win_EnableWidget(ware, 0)
            continue
        wareIDs.append(info.ID)
        Win_SetText((ware + '.ID'), str(info.ID))
        Win_ShowWidget(ware, True)
        Win_SetImg((ware + '.picture'), info.picName)
        Win_SetText((ware + '.name'), info.name)
        buyMode = []
        if ((info.priceQQ > 0) and buyMode.append(1)):
            pass
        if ((info.priceGame > 0) and buyMode.append(2)):
            pass
        if ((info.priceQQTang > 0) and buyMode.append(3)):
            pass
        if (len(buyMode) > 2):
            buyMode = buyMode[0:3]
        Win_SetText((ware + '.price1'), '')
        Win_SetText((ware + '.price2'), '')
        Win_ShowWidget(('UI.shop.ware%d.memberPic' % (i + 1)), 1)
        memberRebate = 100
        rebate = 100
        Win_SetImg((ware + '.pricePic'), 'object/ui/shop/ware/originPrice.img')
        if ((info.memberRebate >= 0) and (info.memberRebate < 100)):
            memberRebate = info.memberRebate
        if ((info.rebate >= 0) and (info.rebate < 100)):
            rebate = info.rebate
            Win_SetImg((ware + '.pricePic'), 'object/ui/shop/ware/rebatePrice.img')
        if ((curMoneyType == 'QB') and Win_SetText((ware + '.price2'), makeStr(8, (((info.priceQQ * rebate) + 99) / 100), ' Q\xb1\xd2', 1))):
            Win_SetText((ware + '.memberPrice'), makeStr(8, ((((info.priceQQ * memberRebate) * rebate) + 9999) / 10000), ' Q\xb1\xd2', 1))
        buyModes.append(buyMode)
        if ((0 == len(buyMode)) and Win_ShowWidget((ware + '.buyA'), 0)):
            pass
        for attrVal in range(1, 8):
            if ((info.attribute == attrVal) and Win_SetImg(('UI.shop.attr%d.rebate' % (i + 1)), '')):
                Win_SetImg(('UI.shop.attr%d.rebateH' % (i + 1)), '')
                Win_SetImg(('UI.shop.attr%d.point' % (i + 1)), '')
                Win_SetImg(('UI.shop.attr%d.rebateL' % (i + 1)), '')
                Win_SetImg(('UI.shop.attr%d.rebateWord' % (i + 1)), '')
                Win_SetImg(('UI.shop.attr%d' % (i + 1)), ('object/ui/shop/wareAttr/%s.img' % attrMap[attrVal]))
                Win_ShowWidget(('UI.shop.attr%d' % (i + 1)), 1)

        if ((info.rebate > 0) and (info.rebate < 100)):
            rebateH = (info.rebate / 10)
            rebateL = (info.rebate % 10)
            ui = ('UI.shop.attr%d' % (i + 1))
            Win_SetImg(ui, 'object/ui/shop/wareAttr/bg_rebate.img')
            Win_SetImg((ui + '.rebateWord'), 'object/ui/shop/wareAttr/zhe.img')
            Win_ShowWidget((ui + '.rebateWord'), 1)
            Win_ShowWidget(ui, 1)
            if ((0 == rebateL) and Win_ShowWidget((ui + '.rebateH'), 0)):
                Win_ShowWidget((ui + '.point'), 0)
                Win_ShowWidget((ui + '.rebateL'), 0)
                Win_SetImg((ui + '.rebate'), ('object/ui/shop/wareAttr/%d.img' % rebateH))
                Win_ShowWidget((ui + '.rebate'), 1)



class ItemList:
    __module__ = __name__
    items = []

    def getCnt(this, type):
        global itemCnt
        ItemList.items = []
        cnt = GetEnableItemCnt(type)
        for i in range(cnt):
            info = this._ItemList__get(type, i)
            if (info.hasClient and ItemList.items.append(info)):
                pass

        itemCnt = len(ItemList.items)
        return itemCnt



    def at(this, type, itemIdx):
        if (itemIdx >= len(ItemList.items)):
            return None
        return ItemList.items[itemIdx]



    def __get(this, type, i):
        info = CNil()
        ii = GetEnableItemInfo(type, i)
        id = ii.m_nItemID
        info.ID = id
        info.roleID = ii.m_bItemRoleID
        info.status = ii.m_bItemStatus
        info.buyTime = ii.m_dwBuyTime
        info.effectID = ii.m_bItemEffect
        if itemList.has_key(id):
            info.hasClient = 1
            iconType = itemList[id][0]
            iconIdx = itemList[id][1]
            info.picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
             iconType,
             iconIdx))
        else:
            info.hasClient = 0
            info.picName = 'res/uires/shop/salou.img'
        return info




def updateLightIcon():
    RoleID = shopPlayer_getRoleIdx()
    clearLightIcon()
    for type in g_ItemsPreview:
        ItemID = GetRoleItem(RoleID, type)
        if ((ItemID != -1) and Win_ShowWidget(('UI.shop.lighticon.%s' % type), 1)):
            pass

    ItemID = GetRoleItem(RoleID, 'bg')
    if ((ItemID != -1) and Win_ShowWidget('UI.shop.lighticon.bg', 1)):
        pass
    ItemID = GetRoleItem(RoleID, 'frame')
    if ((ItemID != -1) and Win_ShowWidget('UI.shop.lighticon.frame', 1)):
        pass
    ItemID = GetRoleItem(RoleID, 'enter')
    if ((ItemID != -1) and Win_ShowWidget('UI.shop.lighticon.enter', 1)):
        pass
    ItemID = GetRoleItem(RoleID, 'namecard')
    if ((ItemID != -1) and Win_ShowWidget('UI.shop.lighticon.namecard', 1)):
        pass
    ItemID = GetRoleItem(RoleID, 'namecardbound')
    if ((ItemID != -1) and Win_ShowWidget('UI.shop.lighticon.namecardbound', 1)):
        pass
    for type in equipMap.keys():
        ItemID = GetRoleItem(RoleID, type)
        if ((ItemID != -1) and Win_ShowWidget(('UI.shop.lighticon.%s' % type), 1)):
            pass




def ui_updateMyItems():
    global bClickSaveEquip
    global itemCnt
    itemCnt = ItemList().getCnt(myItemType)
    itemPos[myItemType] = max(itemPos[myItemType], 0)
    for i in range(15):
        itemUI = ('UI.shop.item%d' % (i + 1))
        idx = (itemPos[myItemType] + i)
        Win_SetImg((itemUI + '.hasEquiped'), '')
        Win_SetImg((itemUI + '.hasForged'), '')
        if ((idx >= itemCnt) and Win_ShowWidget(itemUI, False)):
            pass

    updateSelectedItems()
    if (bClickSaveEquip == 1):
        bClickSaveEquip = 0
        updateLightIcon()


class Recycler:
    __module__ = __name__
    items = []

    def getCnt(this):
        global disableItemCnt
        Recycler.items = []
        cnt = GetDisableItemCnt()
        for i in range(cnt):
            info = this._Recycler__get(type, i)
            if (info.hasClient and Recycler.items.append(info)):
                pass

        disableItemCnt = len(Recycler.items)
        return disableItemCnt



    def __get(this, type, i):
        info = CNil()
        ii = GetDisableItemInfo(i)
        id = ii.m_nItemID
        info.status = ii.m_bItemStatus
        info.buyTime = ii.m_dwBuyTime
        if itemList.has_key(id):
            info.hasClient = 1
            iconType = itemList[id][0]
            iconIdx = itemList[id][1]
            info.picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
             iconType,
             iconIdx))
            info.name = itemList[id][2]
        else:
            info.hasClient = 0
            info.picName = 'res/uires/shop/salou.img'
            info.name = ''
        info.ID = id
        return info



    def at(this, itemIdx):
        if (itemIdx >= len(Recycler.items)):
            return None
        return Recycler.items[itemIdx]




def ui_updateRecycler():
    global disableItemCnt
    global activeItemInRecycler
    global disableItemPos
    disableItemCnt = Recycler().getCnt()
    activeItemInRecycler = 999999
    disableItemPos = min(disableItemPos, (disableItemCnt - defRecyclerCnt))
    disableItemPos = max(disableItemPos, 0)
    for i in range(defRecyclerCnt):
        ui = ('UI.shop.recycler.item%d' % i)
        idx = (disableItemPos + i)
        Win_SetCheck(ui, 0)
        if ((idx >= disableItemCnt) and Win_SetText((ui + '.name'), '')):
            Win_EnableWidget(ui, 0)
            continue

    Win_SetPos('UI.shop.recycler.scroll', Win_GetPos('UI.shop.recycler.scroll'))
    doUI('UI.shop.recycler.scroll', 'OnPosChange')



def buyFail(text):
    ui = 'UI.shop.buyFailDlg'
    Win_SetText((ui + '.text'), text)
    Win_ShowWidget(ui, 1)



def ui_refreshState(bState):
    global fruitState
    ui = 'UI.shop.fruitMachine'
    fruitState = bState
    Win_ShowWidget((ui + '.startBtn'), ((fruitState == 0) or (fruitState == 1)))
    Win_EnableWidget((ui + '.startBtn'), (fruitState == 0))
    Win_ShowWidget((ui + '.stopBtn'), ((fruitState == 2) or (fruitState == 3)))
    Win_EnableWidget((ui + '.stopBtn'), (fruitState == 2))
    if (((fruitState == 0) and (Win_GetFocusPath() == ui)) and Win_SetFocus('')):
        Win_SetCapture('')



def ui_refreshItem():
    ui = 'UI.shop.fruitMachine'
    for i in range(3):
        paramList = [i]
        item = HandleFruitMachine(2, paramList)
        picName = 'res/uires/shop/salou.img'
        if commodityList.has_key(item[0]):
            iconType = commodityList[item[0]][0]
            iconIdx = commodityList[item[0]][1]
            picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
             iconType,
             iconIdx))
        Win_SetImg((ui + ('.item%d' % (i + 1))), picName)




def initFruitMachine():
    global bFruitUpdate
    ui = 'UI.shop.fruitMachine'
    IsLucky = IsFruitMechine()
    if ((IsLucky <= 0) and Win_ShowWidget(ui, 0)):
        Win_ShowWidget('UI.shop.AD', 1)
        return 
    if bFruitUpdate:
        bFruitUpdate = 0
        Win_ShowWidget('UI.shop.fruitTip', 1)
        Win_Timer('UI.shop.fruitTip', 20000)
    else:
        Win_ShowWidget('UI.shop.fruitTip', 0)
    Win_ShowWidget(ui, 1)
    ui_refreshState(0)
    paramList = []
    HandleFruitMachine(5, paramList)



def buyFruitMachine():
    BuyCommodity(999, 2, 1, 0)



def ui_startFruitMachine():
    ui = 'UI.shop.fruitMachine'
    Win_ShowWidget((ui + '.frame'), 1)
    Win_ShowWidget((ui + '.light'), 1)
    Win_SetValue((ui + '.light'), 0.14999999999999999, 49)
    paramList = [400,
     150,
     10]
    HandleFruitMachine(1, paramList)
    ui_refreshState(2)



def stopFruitMachine():
    paramList = [450,
     12]
    HandleFruitMachine(3, paramList)
    ui_refreshState(3)



def ui_showFruitResult(resultStr):
    ui = 'UI.shop.fruitResult'
    Win_SetText((ui + '.text'), resultStr)
    ui_setCapture(ui)
    ui = 'UI.shop.fruitMachine'
    Win_ShowWidget((ui + '.light'), 0)
    UpdateMyItem()
    ui_updateMyItems()



def ui_UpdateShopStorage():
    g_StorageList.update()
    UpdateShopStorage()



def UpdateShopStorage():
    if ((totalStorageCnt == 0) and Win_SetText((uiShopStorageDlg + '.storagePage'), '1/1')):
        pass
    for i in range(defShopStorageCnt):
        ui = (uiShopStorageDlg + ('.storageItem%d' % i))
        idx = (i + shopStoragePos)
        if ((idx >= totalStorageCnt) and Win_SetImg(ui, '')):
            Win_SetText((ui + '.itemNum'), '')
            continue
        info = g_StorageList.at(idx).m_stItem
        Win_SetImg(ui, ('res/uires/icon/item/item%d.img' % info.m_nItemID))
        Win_SetText((ui + '.itemNum'), ('%4d' % info.m_iNumOfItem))



class forgeTypeList:
    __module__ = __name__
    items = []

    def clear(this):
        global forgeTypeCnt
        forgeTypeList.items = []
        forgeTypeCnt = 0



    def update(this):
        global forgeTypeCnt
        forgeTypeList.items = GetForgeType()
        forgeTypeCnt = len(forgeTypeList.items)
        return forgeTypeCnt



    def at(this, itemIdx):
        if (itemIdx >= len(forgeTypeList.items)):
            return None
        return forgeTypeList.items[itemIdx]



class forgeItemList:
    __module__ = __name__
    items = []

    def clear(this):
        global forgeItemCnt
        forgeItemList.items = []
        forgeItemCnt = 0



    def update(this):
        global forgeItemCnt
        forgeItemList.items = GetForgeItem(forgeExpand)
        forgeItemCnt = len(forgeItemList.items)
        return forgeItemCnt



    def at(this, itemIdx):
        if (itemIdx >= len(forgeItemList.items)):
            return None
        return forgeItemList.items[itemIdx]



class forgeMeterialList:
    __module__ = __name__
    items = []

    def clear(this):
        global forgeMeterialCnt
        forgeMeterialList.items = []
        forgeMeterialCnt = 0



    def update(this):
        global forgeMeterialCnt
        forgeMeterialList.items = GetForgeMeterial(forgeItemID)
        forgeMeterialCnt = len(forgeMeterialList.items)
        return forgeMeterialCnt



    def at(this, itemIdx):
        if (itemIdx >= len(forgeMeterialList.items)):
            return None
        return forgeMeterialList.items[itemIdx]



g_ForgeTypeList = forgeTypeList()
g_ForgeItemList = forgeItemList()
g_ForgeMeterialList = forgeMeterialList()

def ui_UpdateForgeType():
    global forgeItemID
    global forgeExpand
    g_ForgeMeterialList.clear()
    g_ForgeItemList.clear()
    g_ForgeTypeList.update()
    forgeExpand = -1
    forgeItemID = 0
    Win_SetPos((uiForgeDlg + '.itemScroll'), 0)
    doUI((uiForgeDlg + '.itemScroll'), 'OnPosChange')
    Win_SetPos((uiForgeDlg + '.materialScroll'), 0)
    doUI((uiForgeDlg + '.materialScroll'), 'OnPosChange')
    Win_SetImg((uiForgeDlg + '.curItemIcon'), '')
    Win_SetText((uiForgeDlg + '.curItemName'), '')
    Win_SetText((uiForgeDlg + '.curItemInfo'), '')
    Win_SetText((uiForgeDlg + '.forgeInfo'), '', value_channel_listitem_num)


class composeTypeList:
    __module__ = __name__
    items = []

    def clear(this):
        global composeTypeCnt
        composeTypeList.items = []
        composeTypeCnt = 0



    def update(this):
        global composeTypeCnt
        composeTypeList.items = GetCombineType()
        composeTypeCnt = len(composeTypeList.items)
        return composeTypeCnt



    def at(this, itemIdx):
        if (itemIdx >= len(composeTypeList.items)):
            return None
        return composeTypeList.items[itemIdx]



class composeItemList:
    __module__ = __name__
    items = []

    def clear(this):
        global composeItemCnt
        composeItemList.items = []
        composeItemCnt = 0



    def update(this):
        global composeItemCnt
        composeItemList.items = GetCombineItem(composeExpand)
        composeItemCnt = len(composeItemList.items)
        return composeItemCnt



    def at(this, itemIdx):
        if (itemIdx >= len(composeItemList.items)):
            return None
        return composeItemList.items[itemIdx]



class composeMeterialList:
    __module__ = __name__
    items = []

    def clear(this):
        global composeMeterialCnt
        composeMeterialList.items = []
        composeMeterialCnt = 0



    def update(this):
        global composeMeterialCnt
        composeMeterialList.items = GetCombineMeterial(composeItemID)
        composeMeterialCnt = len(composeMeterialList.items)
        return composeMeterialCnt



    def at(this, itemIdx):
        if (itemIdx >= len(composeMeterialList.items)):
            return None
        return composeMeterialList.items[itemIdx]



g_ComposeTypeList = composeTypeList()
g_ComposeItemList = composeItemList()
g_ComposeMeterialList = composeMeterialList()

def ui_UpdateComposeType():
    global composeExpand
    global composeItemID
    g_ComposeMeterialList.clear()
    g_ComposeItemList.clear()
    g_ComposeTypeList.update()
    composeExpand = -1
    composeItemID = 0
    Win_SetPos((uiComposeDlg + '.itemScroll'), 0)
    doUI((uiComposeDlg + '.itemScroll'), 'OnPosChange')
    for i in range(defComposeMeterCnt):
        Win_SetImg((uiComposeDlg + ('.meterialList.meterialIcon%d' % i)), '')
        Win_SetText((uiComposeDlg + ('.meterialList.meterialInfo%d' % i)), '')

    Win_SetImg((uiComposeDlg + '.curItemIcon'), '')
    Win_SetText((uiComposeDlg + '.curItemName'), '')
    Win_SetText((uiComposeDlg + '.curItemInfo'), '')
    Win_SetText((uiComposeDlg + '.composeInfo'), '', value_channel_listitem_num)



def ui_ReceiveForgeResult(result, info):
    g_ForgeItemList.update()
    doUI((uiForgeDlg + '.itemScroll'), 'OnPosChange')
    g_ForgeMeterialList.update()
    doUI((uiForgeDlg + '.materialScroll'), 'OnPosChange')
    Win_SetColorText((uiForgeDlg + '.forgeInfo'), info, value_channel_itemtext, 255, 250, 236)



def ui_ReceiveComResult(result, info):
    g_ComposeItemList.update()
    doUI((uiComposeDlg + '.itemScroll'), 'OnPosChange')
    g_ComposeMeterialList.update()
    for i in range(defComposeMeterCnt):
        materialInfo = g_ComposeMeterialList.at(i)
        Win_SetImg((uiComposeDlg + ('.meterialList.meterialIcon%d' % i)), ('res/uires/icon/item/item%d.img' % materialInfo.iMaterialID))
        Win_SetText((uiComposeDlg + ('.meterialList.meterialInfo%d' % i)), (materialInfo.szMaterialName + ('\n\n%d/%d' % (materialInfo.unHadMatNum,
         materialInfo.unNeedMatlNum))))

    Win_SetColorText((uiComposeDlg + '.composeInfo'), info, value_channel_itemtext, 255, 250, 236)


g_AvatarForgePage = [[0,
  0,
  0,
  0],
 5]
g_AvatarRevertPage = [[0,
  0,
  0,
  0],
 5]
g_AvatarMaterialPage = [0,
 5]
g_AvatarForgeCurrentType = 0
g_ForgeDragInfo = [-1,
 -1,
 '']
g_ForgeInfo = [-1,
 -1,
 -1,
 -1]
g_Operator = (1,
 3,
 4)
class AvatarForge:
    __module__ = __name__
    AvatarList = [[],
     []]

    def update(this):
        global g_AvatarTypeList
        AvatarForge.AvatarList = [[],
         []]
        g_AvatarTypeList = GetAvatarForgeType()
        for i in range(len(g_AvatarTypeList)):
            tempAvatarList = GetAvatarForgeItem(i)
            AvatarForge.AvatarList[0].append(tempAvatarList[0])
            AvatarForge.AvatarList[1].append(tempAvatarList[1])




    def at(this, ForgeorRevert, typeIdx, itemIdx):
        return AvatarForge.AvatarList[ForgeorRevert][typeIdx][itemIdx]



    def getItemCnt(this, ForgeorRevert, typeIdx):
        if (typeIdx < len(AvatarForge.AvatarList[ForgeorRevert])):
            return len(AvatarForge.AvatarList[ForgeorRevert][typeIdx])
        return 0



    def addAvatar(this, ForgeorRevert, typeIdx, itemID):
        for i in range(len(AvatarForge.AvatarList[ForgeorRevert][typeIdx])):
            if (AvatarForge.AvatarList[ForgeorRevert][typeIdx][i].m_nItemID == itemID):
                AvatarForge.AvatarList[ForgeorRevert][typeIdx][i] = GetItemInfoFromSec(itemID)
                return 

        AvatarForge.AvatarList[ForgeorRevert][typeIdx].append(GetItemInfoFromSec(itemID))



    def removeAvatar(this, ForgeorRevert, typeIdx, itemID):
        for i in range(len(AvatarForge.AvatarList[ForgeorRevert][typeIdx])):
            if ((AvatarForge.AvatarList[ForgeorRevert][typeIdx][i].m_nItemID == itemID) and AvatarForge.AvatarList[ForgeorRevert][typeIdx].remove(AvatarForge.AvatarList[ForgeorRevert][typeIdx][i])):
                return 




g_AvatarForge = AvatarForge()

def ui_updateForgePage():
    forgePage1 = ((g_AvatarForgePage[0][g_AvatarForgeCurrentType] + g_AvatarForgePage[1]) / g_AvatarForgePage[1])
    itemCnt = g_AvatarForge.getItemCnt(0, g_AvatarForgeCurrentType)
    if ((itemCnt != 0) and ((itemCnt % g_AvatarForgePage[1]) == 0)):
        forgePage2 = (itemCnt / g_AvatarForgePage[1])
    else:
        forgePage2 = ((itemCnt / g_AvatarForgePage[1]) + 1)
    Win_SetText((uiAvatarForgeDlg + '.forgePage'), ('%d/%d' % (forgePage1,
     forgePage2)))
    revertPage1 = ((g_AvatarRevertPage[0][g_AvatarForgeCurrentType] + g_AvatarRevertPage[1]) / g_AvatarRevertPage[1])
    itemCnt = g_AvatarForge.getItemCnt(1, g_AvatarForgeCurrentType)
    if ((itemCnt != 0) and ((itemCnt % g_AvatarRevertPage[1]) == 0)):
        revertPage2 = (itemCnt / g_AvatarRevertPage[1])
    else:
        revertPage2 = ((itemCnt / g_AvatarRevertPage[1]) + 1)
    Win_SetText((uiAvatarForgeDlg + '.revertPage'), ('%d/%d' % (revertPage1,
     revertPage2)))



def ui_showAvatar():
    ui_updateForgePage()
    sourceIdx = g_AvatarForgePage[0][g_AvatarForgeCurrentType]
    itemCnt = g_AvatarForge.getItemCnt(0, g_AvatarForgeCurrentType)
    for i in range(g_AvatarForgePage[1]):
        itemIdx = (i + sourceIdx)
        if (itemIdx < itemCnt):
            itemID = g_AvatarForge.at(0, g_AvatarForgeCurrentType, itemIdx).m_nItemID
            if itemList.has_key(itemID):
                iconType = itemList[itemID][0]
                iconIdx = itemList[itemID][1]
                picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
                 iconType,
                 iconIdx))
            else:
                picName = 'res/uires/shop/salou.img'
            Win_SetImg((uiAvatarForgeDlg + ('.forgeItem%d' % i)), picName)
            Win_EnableWidget((uiAvatarForgeDlg + ('.forgeItem%d' % i)), 1)
        else:
            Win_SetImg((uiAvatarForgeDlg + ('.forgeItem%d' % i)), '')
            Win_EnableWidget((uiAvatarForgeDlg + ('.forgeItem%d' % i)), 0)

    sourceIdx = g_AvatarRevertPage[0][g_AvatarForgeCurrentType]
    itemCnt = g_AvatarForge.getItemCnt(1, g_AvatarForgeCurrentType)
    for i in range(g_AvatarRevertPage[1]):
        itemIdx = (i + sourceIdx)
        if (itemIdx < itemCnt):
            itemID = g_AvatarForge.at(1, g_AvatarForgeCurrentType, itemIdx).m_nItemID
            if itemList.has_key(itemID):
                iconType = itemList[itemID][0]
                iconIdx = itemList[itemID][1]
                picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
                 iconType,
                 iconIdx))
            else:
                picName = 'res/uires/shop/salou.img'
            Win_SetImg((uiAvatarForgeDlg + ('.revertItem%d' % i)), picName)
            Win_EnableWidget((uiAvatarForgeDlg + ('.revertItem%d' % i)), 1)
        else:
            Win_SetImg((uiAvatarForgeDlg + ('.revertItem%d' % i)), '')
            Win_EnableWidget((uiAvatarForgeDlg + ('.revertItem%d' % i)), 0)




def ui_addAvatar(ForgeorRevert, typeIdx, itemID):
    g_AvatarForge.addAvatar(ForgeorRevert, typeIdx, itemID)



def ui_removeAvatar(ForgeorRevert, typeIdx, itemID):
    g_AvatarForge.removeAvatar(ForgeorRevert, typeIdx, itemID)


class AvatarForgeMaterial:
    __module__ = __name__
    MaterialList = []

    def update(this):
        AvatarForgeMaterial.MaterialList = GetAvatarForgeMaterial()



    def getMaterialCnt(this):
        return len(AvatarForgeMaterial.MaterialList)



    def at(this, itemIdx):
        return AvatarForgeMaterial.MaterialList[itemIdx]



    def addMaterial(this, itemID):
        for i in range(len(AvatarForgeMaterial.MaterialList)):
            if (AvatarForgeMaterial.MaterialList[i].m_stItem.m_nItemID == itemID):
                AvatarForgeMaterial.MaterialList[i] = GetItemInfoInStorage(itemID)
                return 

        AvatarForgeMaterial.MaterialList.append(GetItemInfoInStorage(itemID))



    def removeMaterial(this, itemID):
        for i in range(len(AvatarForgeMaterial.MaterialList)):
            if ((AvatarForgeMaterial.MaterialList[i].m_stItem.m_nItemID == itemID) and AvatarForgeMaterial.MaterialList.remove(AvatarForgeMaterial.MaterialList[i])):
                return 




g_AvatarForgeMaterial = AvatarForgeMaterial()

def ui_updateMaterialPage():
    materialPage1 = ((g_AvatarMaterialPage[0] + g_AvatarMaterialPage[1]) / g_AvatarMaterialPage[1])
    itemCnt = g_AvatarForgeMaterial.getMaterialCnt()
    if ((itemCnt != 0) and ((itemCnt % g_AvatarMaterialPage[1]) == 0)):
        materialPage2 = (itemCnt / g_AvatarMaterialPage[1])
    else:
        materialPage2 = ((itemCnt / g_AvatarMaterialPage[1]) + 1)
    Win_SetText((uiAvatarForgeDlg + '.materialPage'), ('%d/%d' % (materialPage1,
     materialPage2)))



def ui_showMaterial():
    ui_updateMaterialPage()
    sourceIdx = g_AvatarMaterialPage[0]
    itemCnt = g_AvatarForgeMaterial.getMaterialCnt()
    for i in range(g_AvatarMaterialPage[1]):
        itemIdx = (i + sourceIdx)
        if (itemIdx < itemCnt):
            info = g_AvatarForgeMaterial.at(itemIdx)
            Win_SetImg((uiAvatarForgeDlg + ('.materialItem%d' % i)), ('res/uires/icon/item/item%d.img' % info.m_stItem.m_nItemID))
            Win_SetText((uiAvatarForgeDlg + ('.materialItem%d.itemNum' % i)), str(info.m_stItem.m_iNumOfItem))
            Win_ShowWidget((uiAvatarForgeDlg + ('.materialItem%d' % i)), 1)
        else:
            Win_ShowWidget((uiAvatarForgeDlg + ('.materialItem%d' % i)), 0)




def ui_addMaterial(itemID):
    g_AvatarForgeMaterial.addMaterial(itemID)



def ui_removeMaterial(itemID):
    g_AvatarForgeMaterial.removeMaterial(itemID)



def ui_InitForgeDlg():
    global g_ForgeInfo
    global g_AvatarForgeCurrentType
    global g_AvatarForgePage
    global g_AvatarMaterialPage
    global g_AvatarRevertPage
    global g_ForgeDragInfo
    g_AvatarForgePage = [[0,
      0,
      0,
      0],
     5]
    g_AvatarRevertPage = [[0,
      0,
      0,
      0],
     5]
    g_AvatarMaterialPage = [0,
     5]
    g_AvatarForgeCurrentType = 0
    g_ForgeDragInfo = [-1,
     -1,
     '']
    g_ForgeInfo = [-1,
     -1,
     -1,
     -1]
    ui_UpdateAvatarForge()
    ui_showMaterial()
    ui_showAvatar()
    AvatarForge_wear(0, 0, 0)
    AvatarForge_Pos(100, 394)
    Win_SelectSelf((uiAvatarForgeDlg + '.forgeType0'))
    Win_SetCheck((uiAvatarForgeDlg + '.forgeType0'), 1)
    Win_SetImg((uiAvatarForgeDlg + '.sourceMaterial'), '')
    Win_SetImg((uiAvatarForgeDlg + '.sourceAvatar'), '')
    Win_ShowWidget(uiForgeConfirmDlg, 0)



def ui_UpdateAvatarForge():
    g_AvatarForge.update()
    g_AvatarForgeMaterial.update()



def ui_UpdateAvatarEffect(itemID, effectIdx, colorIdx, result, info):
    global g_ForgeInfo
    if itemList.has_key(itemID):
        desc = itemList[itemID]
        (type, idx,) = desc[0:2]
        if ((useItems[type] == itemID) and shopPlayer_wear(type, idx, effectIdx, colorIdx)):
            pass
    AvatarForge_wear(itemID, effectIdx, colorIdx)
    AvatarForge_Pos(100, 394)
    g_ForgeInfo = [-1,
     -1,
     -1,
     itemID]
    Win_SetImg((uiAvatarForgeDlg + '.sourceMaterial'), '')
    Win_SetImg((uiAvatarForgeDlg + '.sourceAvatar'), '')
    Win_ShowWidget(uiForgeConfirmDlg, 0)
    Win_SetColorText((uiAvatarForgeDlg + '.forgeInfo'), info, value_channel_itemtext, 255, 250, 236)



def UpdateTaskSysUi():
    global tasksIdList

    def ClearTaskUi():
        global tasksIdList
        tasksIdList = []
        for i in range(6):
            taskBtn = (uiTaskDlg + ('.taskBtn%d.taskCtrBtn' % i))
            Win_EnableWidget(taskBtn, 0)



    ClearTaskUi()
    tasksIdList = GetAllTaskId()
    for i in range(len(tasksIdList)):
        taskStatus = GetState(tasksIdList[i])
        taskBtn = (uiTaskDlg + ('.taskBtn%d.taskCtrBtn' % i))
        taskNameBtn = (uiTaskDlg + ('.taskBtn%d.taskNameBtn' % i))
        Win_SetText(taskNameBtn, GetTaskName(tasksIdList[i]))
        if ((taskStatus == 0) and Win_EnableWidget(taskBtn, 1)):
            Win_SetImg(taskBtn, 'object/ui/task/btn_startTask.img')

    UpdateCurTaskPanel()



def UpdateCurTaskPanel():
    if (currentTaskIdx >= len(tasksIdList)):
        return 
    curTaskId = tasksIdList[currentTaskIdx]
    imgPath = ('object/ui/task/' + GetTaskMark(curTaskId))
    Win_SetImg((uiTaskDlg + '.taskMark'), imgPath)
    Win_SetText((uiTaskDlg + '.taskName'), GetTaskName(curTaskId))
    imgPath = ('res/uires/icon/npcIcon/' + GetNpcImgPath(curTaskId))
    Win_SetImg((uiTaskDlg + '.npcPic'), imgPath)
    Win_SetText((uiTaskDlg + '.taskIntroduction'), GetTaskDescription(curTaskId))
    Win_SetText((uiTaskDlg + '.deadLine'), GetTaskDeadLineStr(curTaskId))
    Win_SetText((uiTaskDlg + '.progressDes'), GetProgressDes(curTaskId))
    Win_SetText((uiTaskDlg + '.awardDes'), GetAwardDescription(curTaskId))
    itemId = GetAwardId(curTaskId)
    if itemList.has_key(itemId):
        iconType = itemList[itemId][0]
        iconIdx = itemList[itemId][1]
        Win_SetImg((uiTaskDlg + '.awardPic'), ('res/uires/icon/%s/%s%d.img' % (iconType,
         iconType,
         iconIdx)))
    else:
        Win_SetImg((uiTaskDlg + '.awardPic'), '')
    Win_ShowWidget(uiTaskDlg, 1)
    PlaySound(soundUI, 1)



def NotifyBreakEggResult(bSuccess, showItemId, strInfo):
    global currentEggId
    print 'NotifyBreakEggResult'
    currentEggId = -1
    Win_SetText('UI.shop.breakEggDlg.description', strInfo)
    Win_SetImg('UI.shop.breakEggDlg.eggPic', '')
    if ((bSuccess > 0) and itemList.has_key(showItemId)):
        iconType = itemList[showItemId][0]
        iconIdx = itemList[showItemId][1]
        Win_SetImg('UI.shop.breakEggDlg.eggPic', ('res/uires/icon/%s/%s%d.img' % (iconType,
         iconType,
         iconIdx)))
    ui = 'UI.shop.breakEggDlg.hammer'
    Win_EnableWidget((ui + '1'), 0)
    Win_SetImg((ui + '1.hammerPic'), 'res/uiRes/icon/platform/platform9011.img')
    Win_SetText((ui + '1.hammerCnt'), str(GetItemLeaveCount(9011)))
    Win_EnableWidget((ui + '2'), 0)
    Win_SetImg((ui + '2.hammerPic'), 'res/uiRes/icon/platform/platform9012.img')
    Win_SetText((ui + '2.hammerCnt'), str(GetItemLeaveCount(9012)))
    Win_EnableWidget((ui + '3'), 0)
    Win_SetImg((ui + '3.hammerPic'), 'res/uiRes/icon/platform/platform9013.img')
    Win_SetText((ui + '3.hammerCnt'), str(GetItemLeaveCount(9013)))
    Win_ShowWidget('UI.shop.breakEggDlg', 1)
    if ((bSuccess > 0) and PlaySound('X12_01.wav', 1)):
        Win_SetImg('UI.shop.breakEggDlg.resultPic', 'object/ui/shop/breakEgg/success.img')



def setLRPosition():
    print 'itemType,itemSubType:  ',
    print itemType,
    print itemSubType
    if (((itemType == 1) and (itemSubType == 1)) and Win_Move2Pos('UI.shop.left', 258, 375)):
        Win_Move2Pos('UI.shop.right', 383, 375)
        Win_Move2Pos('UI.shop.warePage', 288, 381)



def ui_refreshLightspeed(accel):
    global g_curLightSpeed
    ui = 'UI.shop.fruitMachine'
    g_curLightSpeed = Win_GetValue((ui + '.light'), 49)
    g_curLightSpeed = (g_curLightSpeed + (accel * 0.001))
    Win_SetValue((ui + '.light'), g_curLightSpeed, 49)



def resetFruitMachine():
    ui = 'UI.shop.fruitMachine'
    Win_ShowWidget((ui + '.frame'), 0)
    Win_EnableWidget((ui + '.startBtn'), 1)



def hideWareForFruitMachine():
    ui = 'UI.shop'
    if (((itemType == 1) and (itemSubType == 1)) and Win_ShowWidget((ui + '.ware9'), 0)):
        Win_ShowWidget((ui + '.ware10'), 0)
        Win_ShowWidget((ui + '.ware11'), 0)
        Win_ShowWidget((ui + '.ware12'), 0)
        Win_ShowWidget((ui + '.attr9'), 0)
        Win_ShowWidget((ui + '.attr10'), 0)
        Win_ShowWidget((ui + '.attr11'), 0)
        Win_ShowWidget((ui + '.attr12'), 0)


btn = ['UI.shop.defaultSecrecyValidateDlg.secrecyQuestionRad',
 'UI.shop.defaultSecrecyValidateDlg.mobileMessageRad',
 'UI.shop.defaultSecrecyValidateDlg.secrecyCardRad',
 'UI.shop.defaultSecrecyValidateDlg.mobileTokenRad',
 'UI.shop.defaultSecrecyValidateDlg.telephoneIVRRad']
validateDlg = ['UI.shop.secrecyQuestionDlg',
 'UI.shop.mobileMessageDlg',
 'UI.shop.secrecyCardDlg',
 'UI.shop.mobileTokenDlg',
 'UI.shop.telephoneIVRDlg']

def SetValidateState():
    global validateState
    validateState = 0



def showDefaultPaymentMode(defaultID):
    global secrecyValidateID
    global validateState
    validateState = 1
    secrecyValidateID = defaultID
    ui_setCapture('UI.shop.defaultSecrecyValidateDlg')
    for i in range(5):
        if (((i + 1) == defaultID) and Win_SetCheck(btn[i], 1)):
            pass




def showErrorResult(secValidateID, resultContent):
    if ((secValidateID > 0) and Win_ShowWidget(validateDlg[(secValidateID - 1)], 0)):
        CancelVerify()



def VerifyTimeout():
    Win_ShowWidget('UI.shop.defaultSecrecyValidateDlg', 0)
    for i in range(5):
        Win_ShowWidget(validateDlg[i], 0)

    showErrorResult(0, '\xb6\xd4\xb2\xbb\xc6\xf0\xa3\xac\xc4\xfa\xb5\xc4\xb2\xd9\xd7\xf7\xb3\xac\xca\xb1!')



def showSecrecyValidateDlg(secValidateID):
    global currentQuestionID
    global coorNum
    global coorSize
    global currentQuestionID2
    global currentQuestionID1
    global questionCnt
    global questionNum
    for i in range(5):
        if (((i + 1) == secValidateID) and ui_setCapture(validateDlg[i])):
            pass

    uiDlg = validateDlg[(secValidateID - 1)]
    if ((1 == secValidateID) and Win_SetText((uiDlg + '.questionDlg1.answerText'), '')):
        Win_SetText((uiDlg + '.questionDlg2.answerText'), '')
        Win_SetText((uiDlg + '.questionDlg3.answerText'), '')
        Win_ShowWidget((uiDlg + '.questionDlg1'), 0)
        Win_ShowWidget((uiDlg + '.questionDlg2'), 0)
        Win_ShowWidget((uiDlg + '.questionDlg3'), 0)
        Win_ShowWidget((uiDlg + '.changeQuestion1'), 0)
        Win_ShowWidget((uiDlg + '.changeQuestion2'), 0)
        questionInfo = GetQuestionData()
        questionCnt = int(questionInfo.m_bQuestionCount)
        if ((questionCnt == 0) and showErrorResult(secValidateID, '\xb6\xd4\xb2\xbb\xc6\xf0\xa3\xac\xce\xb4\xc4\xdc\xb3\xc9\xb9\xa6\xbb\xf1\xc8\xa1\xc3\xdc\xb1\xa3\xce\xca\xcc\xe2\xd1\xe9\xd6\xa4\xd0\xc5\xcf\xa2\xa3\xac\xb4\xcb\xb4\xce\xcf\xfb\xb7\xd1\xca\xa7\xb0\xdc')):
            return 
        questionNum = int(questionInfo.m_bQuestionNum)
        for j in range(questionCnt):
            info = GetTheQuestionData(j)
            questionIDList[j] = info.m_cQuestionId

        if (questionNum > 1):
            for j in range(questionNum):
                Win_ShowWidget(((uiDlg + '.questionDlg') + str((j + 1))), 1)
                info = GetTheQuestionData(j)
                question = info.m_szQuestionDes
                Win_SetText((((uiDlg + '.questionDlg') + str((j + 1))) + '.question'), question)

            if ((2 == questionNum) and Win_ShowWidget((uiDlg + '.changeQuestion1'), 1)):
                Win_ShowWidget((uiDlg + '.changeQuestion2'), 1)
            currentQuestionID1 = 0
            currentQuestionID2 = 1
        else:
            if ((1 == questionNum) and Win_ShowWidget((uiDlg + '.questionDlg2'), 1)):
                Win_ShowWidget((uiDlg + '.changeQuestion2'), 1)
                question = GetTheQuestionData(0).m_szQuestionDes
                Win_SetText((uiDlg + '.questionDlg2.question'), question)
                currentQuestionID = 0


class UI_children_shop:
    __module__ = __name__
    type = 'SCREEN'
    rect = (0,
     0,
     800,
     600)
    bkimage = 'object/ui/bg/bg_shop.img'
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
     ('OnAccel_OnF5',
      116,
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
     ('OnAccel_OnF11',
      122,
      0,
      0,
      0),
     ('OnAccel_OnF12',
      123,
      0,
      0,
      0))

    def OnAccel_OnF1():
        doUI('UI.shop.help', 'OnClick')



    def OnEscape():
        doUI('UI.shop.leaveBtn', 'OnClick')



    def OnAccel_act():
        print '<act>'
        sc_shopPlayer_act(6)



    def OnAccel_stand():
        print '<Win>'
        shopPlayer_stand()



    def OnAccel_jump():
        print '<Win>'
        shopPlayer_jump()



    def OnAccel_freeze():
        print '<Win>'
        shopPlayer_freeze()



    def OnAccel_die():
        print '<Win>'
        shopPlayer_die()



    def OnAccel_changeColor():
        print 'C'
        shopPlayer_changeColor()



    def OnAccel_win():
        print '<Win>'
        shopPlayer_win()



    def OnAccel_putBomb():
        print '<bomb>'
        shopPlayer_putBomb()



    def OnAccel_down():
        print '<Down>'
        shopPlayer_walk(3)



    def OnAccel_left():
        shopPlayer_walk(2)



    def OnAccel_right():
        shopPlayer_walk(0)



    def OnAccel_up():
        shopPlayer_walk(1)



    def OnAccel_keyUp():
        shopPlayer_stop()



    def OnInit():
        global isAllowPresentMixedPay
        global itemType
        global mark_shopPetTab
        global myItemType
        global itemSubType
        global isAllowMixedPay
        global curMoneyType
        global mark_task
        global secrecyValidateID
        global isAllowQBMixedPay
        print 'shop init'
        secrecyValidateID = 1
        Win_ShowWidget(uiGuideBar, 0)
        Win_ShowWidget(uiSocialityDlg, 0)
        sc_HideWeb('kinMatch')
        sc_HideWeb('kinTeam')
        Win_ShowWidget(uiMenuDlg, 0)
        Win_SetCheck('UI.shop.buyDlg.checkRectQD.checkBtn', 1)
        Win_SetCheck('UI.shop.buyDlg.checkRectQB.checkBtn', 1)
        Win_SetCheck('UI.shop.donateDlg.checkRectQBPresent.checkBtn', 1)
        isAllowMixedPay = 1
        isAllowQBMixedPay = 1
        isAllowPresentMixedPay = 1
        Win_ShowWidget(uiRefineDlg, 0)
        if (isStorageVisible and doUI('UI.shop.storageBtn', 'OnClick')):
            pass
        UpdateMyItem()
        ui_refreshItem()
        ui_updateTicket()
        initFruitMachine()
        if ((loginType == 1) or (loginType == 2)):
            curMoneyType = 'VNet'
            Win_ShowWidget('UI.shop.useQBRad', False)
        else:
            curMoneyType = 'QB'
            Win_ShowWidget('UI.shop.useVNetRad', False)
        itemType = 1
        itemSubType = 1
        myItemType = 2
        Win_SelectSelf('UI.shop.adviceTab')
        doUI('UI.shop.adviceTab', 'OnClick')
        Win_SelectSelf('UI.shop.myFunction')
        clearAllPos()
        ui_updateAll()
        screenStartIn()
        InitPlayerActiveItems()
        if ((curMoneyType == 'QB') and Win_SelectSelf('UI.shop.useQBRad')):
            Win_SetCheck('UI.shop.useQBRad', 1)
        LoadShopKeyboardLayout()
        Win_SetImg('UI.shop.charIcon', getCharIconName())
        InitTaskSys()
        Win_ShowWidget(uiTaskDlg, 0)
        if (mark_task and doUI('UI.shop.taskBtn', 'OnClick')):
            mark_task = 0
        if ((IsShowStorageDlg > 0) and doUI('UI.shop.storageBtn', 'OnClick')):
            pass
        if (mark_shopPetTab > 0):
            mark_shopPetTab = 0
            doUI('UI.shop.petTab', 'OnClick')



    def OnDenit():
        global IsShowStorageDlg
        IsShowStorageDlg = 0
        UnInitTaskSys()


    class children:
        __module__ = __name__
        class defaultSecrecyValidateDlg(TStatic):
            __module__ = __name__
            darkBG = 1
            visible = 0
            initlayer = 999999
            rect = (219,
             91,
             450,
             315)
            bkimage = 'object/ui/shop/secrecyValidate/dlg_DefaultSecrecyValidate.img'
            class children:
                __module__ = __name__
                class title(TLabel):
                    __module__ = __name__
                    rect = (190,
                     40,
                     200,
                     12)
                    drawcolor = lightColor
                    textEdgeType = 1
                    textEdgeColor = (66,
                     95,
                     133,
                     255)
                    caption = '\xc7\xeb\xd1\xa1\xd4\xf1\xd1\xe9\xd6\xa4\xb7\xbd\xca\xbd'

                class secrecyQuestionRad(TRadio):
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
                      0,
                      0,
                      0,
                      0,
                      0,
                      0)]
                    rect = ((50 + 10),
                     70,
                     50,
                     25)
                    bkimage = 'object/ui/shop/secrecyValidate/btn_Ratio.img'
                    groupstop = 0

                    def OnClick(this):
                        global secrecyValidateID
                        secrecyValidateID = 1



                class secrecyQuestionLabel(TLabel):
                    __module__ = __name__
                    rect = ((75 + 10),
                     75,
                     80,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc3\xdc\xb1\xa3\xce\xca\xcc\xe2\xd1\xe9\xd6\xa4'

                class mobileMessageRad(secrecyQuestionRad):
                    __module__ = __name__
                    rect = ((50 + 10),
                     100,
                     50,
                     25)
                    groupstop = 1

                    def OnClick(this):
                        global secrecyValidateID
                        secrecyValidateID = 2



                class mobileMessageLabel(secrecyQuestionLabel):
                    __module__ = __name__
                    rect = ((75 + 10),
                     105,
                     200,
                     12)
                    caption = '\xc3\xdc\xb1\xa3\xca\xd6\xbb\xfa\xd1\xe9\xd6\xa4'

                class secrecyCardRad(secrecyQuestionRad):
                    __module__ = __name__
                    rect = ((50 + 10),
                     130,
                     50,
                     25)
                    groupstop = 2

                    def OnClick(this):
                        global secrecyValidateID
                        secrecyValidateID = 3



                class secrecyCardLabel(secrecyQuestionLabel):
                    __module__ = __name__
                    rect = ((75 + 10),
                     135,
                     200,
                     12)
                    caption = '\xc3\xdc\xb1\xa3\xbf\xa8\xd1\xe9\xd6\xa4'

                class mobileTokenRad(secrecyQuestionRad):
                    __module__ = __name__
                    rect = ((50 + 10),
                     160,
                     50,
                     25)
                    groupstop = 3

                    def OnClick(this):
                        global secrecyValidateID
                        secrecyValidateID = 4



                class mobileTokenLabel(secrecyQuestionLabel):
                    __module__ = __name__
                    rect = ((75 + 10),
                     165,
                     200,
                     12)
                    caption = '\xc3\xdc\xb1\xa3\xc1\xee\xc5\xc6\xd1\xe9\xd6\xa4'

                class telephoneIVRRad(secrecyQuestionRad):
                    __module__ = __name__
                    rect = ((50 + 10),
                     190,
                     50,
                     25)
                    groupstop = 4

                    def OnClick(this):
                        global secrecyValidateID
                        secrecyValidateID = 5



                class telephoneIVRLabel(secrecyQuestionLabel):
                    __module__ = __name__
                    rect = ((75 + 10),
                     195,
                     200,
                     12)
                    caption = '\xc3\xdc\xb1\xa3\xb5\xe7\xbb\xb0\xd1\xe9\xd6\xa4'

                class nextBtn(TButton):
                    __module__ = __name__
                    rect = (221,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_next.img'

                    def OnClick(this):
                        showSecrecyValidateDlg(secrecyValidateID)
                        Win_ShowWidget('UI.shop.defaultSecrecyValidateDlg', 0)



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (327,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_cancel.img'

                    def OnClick(this):
                        CancelVerify()
                        Win_ShowWidget('UI.shop.defaultSecrecyValidateDlg', 0)





        class secrecyQuestionDlg(TStatic):
            __module__ = __name__
            darkBG = 1
            visible = 0
            initlayer = 999999
            rect = (219,
             91,
             450,
             315)
            bkimage = 'object/ui/shop/secrecyValidate/dlg_DefaultSecrecyValidate.img'
            class children:
                __module__ = __name__
                class title(TLabel):
                    __module__ = __name__
                    rect = (150,
                     40,
                     250,
                     20)
                    drawcolor = lightColor
                    textEdgeType = 1
                    textEdgeColor = (66,
                     95,
                     133,
                     255)
                    caption = '\xb8\xf9\xbe\xdd\xc4\xfa\xb5\xc4\xd1\xa1\xd4\xf1\xa3\xac\xd0\xe8\xbd\xf8\xd0\xd0\xcf\xfb\xb7\xd1\xd1\xe9\xd6\xa4'

                class IDText(TLabel):
                    __module__ = __name__
                    rect = (50,
                     70,
                     200,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc3\xdc\xb1\xa3\xce\xca\xcc\xe2\xd1\xe9\xd6\xa4'

                class questionDlg1(TStatic):
                    __module__ = __name__
                    rect = (50,
                     90,
                     250,
                     45)
                    class children:
                        __module__ = __name__
                        class questionLabel(TLabel):
                            __module__ = __name__
                            rect = (0,
                             5,
                             30,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            caption = '\xce\xca\xcc\xe2:'

                        class question(TLabel):
                            __module__ = __name__
                            rect = (30,
                             5,
                             350,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            caption = '\xc4\xfa\xc9\xd0\xce\xb4\xc9\xe8\xd6\xc3\xce\xca\xcc\xe2'

                        class answerLabel(TLabel):
                            __module__ = __name__
                            rect = (0,
                             25,
                             30,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            caption = '\xb4\xf0\xb0\xb8'

                        class answerText(TEdit):
                            __module__ = __name__
                            rect = (30,
                             21,
                             220,
                             24)
                            captionrect = (4,
                             5,
                             200,
                             14)
                            maxchar = 150
                            bkimage = 'object/ui/shop/secrecyValidate/txt_long.img'
                            textEdgeType = -1



                class changeQuestion1(THyperLink):
                    __module__ = __name__
                    rect = (300,
                     115,
                     60,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xbb\xbb\xb8\xf6\xce\xca\xcc\xe2'

                    def OnClick(this):
                        global currentQuestionID1
                        print ('before(%d,%d)' % (currentQuestionID1,
                         currentQuestionID2))
                        for i in range(questionCnt):
                            if ((i != currentQuestionID1) and (i != currentQuestionID2)):
                                currentQuestionID1 = i
                                break

                        print ('after(%d,%d)' % (currentQuestionID1,
                         currentQuestionID2))
                        question = GetTheQuestionData(currentQuestionID1).m_szQuestionDes
                        Win_SetText('UI.shop.secrecyQuestionDlg.questionDlg1.question', question)



                class questionDlg2(TStatic):
                    __module__ = __name__
                    rect = (50,
                     135,
                     250,
                     45)
                    class children:
                        __module__ = __name__
                        class questionLabel(TLabel):
                            __module__ = __name__
                            rect = (0,
                             5,
                             30,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            caption = '\xce\xca\xcc\xe2:'

                        class question(TLabel):
                            __module__ = __name__
                            rect = (30,
                             5,
                             350,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)

                        class answerLabel(TLabel):
                            __module__ = __name__
                            rect = (0,
                             25,
                             30,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            caption = '\xb4\xf0\xb0\xb8'

                        class answerText(TEdit):
                            __module__ = __name__
                            rect = (30,
                             21,
                             220,
                             24)
                            captionrect = (4,
                             5,
                             200,
                             14)
                            maxchar = 150
                            bkimage = 'object/ui/shop/secrecyValidate/txt_long.img'
                            textEdgeType = -1



                class changeQuestion2(THyperLink):
                    __module__ = __name__
                    rect = (300,
                     160,
                     60,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xbb\xbb\xb8\xf6\xce\xca\xcc\xe2'

                    def OnClick(this):
                        global currentQuestionID2
                        global currentQuestionID
                        if (1 == questionNum):
                            for i in range(questionCnt):
                                if (i == currentQuestionID):
                                    currentQuestionID = ((i + 1) % 3)
                                    break

                            question2ID = currentQuestionID
                        if (2 == questionNum):
                            for i in range(questionCnt):
                                if ((i != currentQuestionID1) and (i != currentQuestionID2)):
                                    currentQuestionID2 = i
                                    break

                            question2ID = currentQuestionID2
                        question = GetTheQuestionData(question2ID).m_szQuestionDes
                        Win_SetText('UI.shop.secrecyQuestionDlg.questionDlg2.question', question)



                class questionDlg3(TStatic):
                    __module__ = __name__
                    rect = (50,
                     180,
                     350,
                     45)
                    class children:
                        __module__ = __name__
                        class questionLabel(TLabel):
                            __module__ = __name__
                            rect = (0,
                             5,
                             30,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            caption = '\xce\xca\xcc\xe2:'

                        class question(TLabel):
                            __module__ = __name__
                            rect = (30,
                             5,
                             350,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)

                        class answerLabel(TLabel):
                            __module__ = __name__
                            rect = (0,
                             25,
                             30,
                             12)
                            drawcolor = (40,
                             40,
                             40,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            caption = '\xb4\xf0\xb0\xb8'

                        class answerText(TEdit):
                            __module__ = __name__
                            rect = (30,
                             21,
                             220,
                             24)
                            captionrect = (4,
                             5,
                             200,
                             14)
                            maxchar = 150
                            bkimage = 'object/ui/shop/secrecyValidate/txt_long.img'
                            textEdgeType = -1



                class forwardBtn(TButton):
                    __module__ = __name__
                    rect = (140,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_forward.img'

                    def OnClick(this):
                        ui_setCapture('UI.shop.defaultSecrecyValidateDlg')
                        Win_ShowWidget('UI.shop.secrecyQuestionDlg', 0)



                class nextBtn(TButton):
                    __module__ = __name__
                    rect = (221,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_next.img'

                    def OnClick(this):
                        realQuestionID = ['1',
                         '2',
                         '3']
                        realQuestionID[0] = questionIDList[currentQuestionID1]
                        realQuestionID[1] = questionIDList[currentQuestionID2]
                        for i in range(questionNum):
                            if ((i != currentQuestionID1) and (i != currentQuestionID2)):
                                realQuestionID[2] = questionIDList[i]

                        if (questionNum == 1):
                            answer = Win_GetText('UI.shop.secrecyQuestionDlg.questionDlg2.answerText')
                            if ((len(answer) == 0) and showErrorResult(0, '\xb4\xf0\xb0\xb8\xb2\xbb\xc4\xdc\xce\xaa\xbf\xd5\xa3\xac\xc7\xeb\xba\xcb\xca\xb5\xba\xf3\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xb4\xf0\xb0\xb8')):
                                pass
                        else:
                            for i in range(questionNum):
                                answer = Win_GetText((('UI.shop.secrecyQuestionDlg.questionDlg' + str((i + 1))) + '.answerText'))
                                if ((len(answer) == 0) and showErrorResult(0, (('\xb5\xda' + str((i + 1))) + '\xb8\xf6\xce\xca\xcc\xe2\xb5\xc4\xb4\xf0\xb0\xb8\xb2\xbb\xc4\xdc\xce\xaa\xbf\xd5\xa3\xac\xc7\xeb\xba\xcb\xca\xb5\xba\xf3\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb\xb4\xf0\xb0\xb8'))):
                                    return 

                            for i in range(questionNum):
                                answer = Win_GetText((('UI.shop.secrecyQuestionDlg.questionDlg' + str((i + 1))) + '.answerText'))
                                SetAnswerData(questionNum, realQuestionID[i], len(answer), answer)

                            Win_ShowWidget('UI.shop.secrecyQuestionDlg', 0)



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (327,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_cancel.img'

                    def OnClick(this):
                        CancelVerify()
                        Win_ShowWidget('UI.shop.secrecyQuestionDlg', 0)





        class mobileMessageDlg(TStatic):
            __module__ = __name__
            darkBG = 1
            visible = 0
            initlayer = 999999
            rect = (219,
             91,
             450,
             315)
            bkimage = 'object/ui/shop/secrecyValidate/dlg_DefaultSecrecyValidate.img'
            class children:
                __module__ = __name__
                class title(TLabel):
                    __module__ = __name__
                    rect = (150,
                     40,
                     250,
                     12)
                    drawcolor = lightColor
                    textEdgeType = 1
                    textEdgeColor = (66,
                     95,
                     133,
                     255)
                    caption = '\xb8\xf9\xbe\xdd\xc4\xfa\xb5\xc4\xd1\xa1\xd4\xf1\xa3\xac\xd0\xe8\xbd\xf8\xd0\xd0\xcf\xfb\xb7\xd1\xd1\xe9\xd6\xa4'

                class IDText(TLabel):
                    __module__ = __name__
                    rect = (50,
                     70,
                     200,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc3\xdc\xb1\xa3\xca\xd6\xbb\xfa\xb7\xa2\xb6\xcc\xd0\xc5\xd1\xe9\xd6\xa4'

                class labelNumber(TLabel):
                    __module__ = __name__
                    rect = (50,
                     100,
                     102,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc4\xfa\xb5\xc4\xc3\xdc\xb1\xa3\xca\xd6\xbb\xfa\xba\xc5\xca\xc7:'

                class mobileNumber(TLabel):
                    __module__ = __name__
                    rect = (155,
                     100,
                     100,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)

                class contentLabel1(TLabel):
                    __module__ = __name__
                    rect = (50,
                     125,
                     300,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)

                class checkCodeLabel(TLabel):
                    __module__ = __name__
                    rect = (50,
                     165,
                     200,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc7\xeb\xca\xe4\xc8\xeb\xc4\xfa\xca\xd5\xb5\xbd\xb5\xc4\xd1\xe9\xd6\xa4\xc2\xeb\xbb\xd8\xb8\xb4'

                class checkCodeText(TEditCharNum):
                    __module__ = __name__
                    caption = ''
                    editable = 1
                    textstyle = 0
                    rect = (50,
                     182,
                     200,
                     24)
                    captionrect = (4,
                     5,
                     50,
                     14)
                    maxchar = 8
                    bkimage = 'object/ui/shop/secrecyValidate/txt_long.img'
                    textEdgeType = -1
                    drawcolor = maskColor

                class checkCodeIndex(TLabel):
                    __module__ = __name__
                    rect = (50,
                     212,
                     300,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xd1\xe9\xd6\xa4\xc2\xeb\xca\xc7\xc4\xfa\xb7\xa2\xcb\xcd\xb6\xcc\xd0\xc5\xba\xf3\xca\xd5\xb5\xbd\xb5\xc48\xce\xbb\xca\xfd\xd7\xd6\xbb\xd8\xb8\xb4'

                class forwardBtn(TButton):
                    __module__ = __name__
                    rect = (140,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_forward.img'

                    def OnClick(this):
                        ui_setCapture('UI.shop.defaultSecrecyValidateDlg')
                        Win_ShowWidget('UI.shop.mobileMessageDlg', 0)



                class nextBtn(TButton):
                    __module__ = __name__
                    rect = (221,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_next.img'

                    def OnClick(this):
                        text = Win_GetText('UI.shop.mobileMessageDlg.checkCodeText')
                        if ((len(text) < 8) and showErrorResult(0, '\xc4\xfa\xc3\xbb\xd3\xd0\xca\xe4\xc8\xeb\xbb\xf2\xca\xe4\xc8\xeb\xb5\xc4\xd1\xe9\xd6\xa4\xc2\xeb\xb2\xbb\xb9\xbb8\xce\xbb\xa3\xac\xc7\xeb\xba\xcb\xca\xb5\xba\xf3\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb')):
                            pass



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (327,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_cancel.img'

                    def OnClick(this):
                        CancelVerify()
                        Win_ShowWidget('UI.shop.mobileMessageDlg', 0)





        class secrecyCardDlg(TStatic):
            __module__ = __name__
            darkBG = 1
            visible = 0
            initlayer = 999999
            rect = (219,
             91,
             450,
             315)
            bkimage = 'object/ui/shop/secrecyValidate/dlg_DefaultSecrecyValidate.img'
            class children:
                __module__ = __name__
                class title(TLabel):
                    __module__ = __name__
                    rect = (150,
                     40,
                     250,
                     12)
                    drawcolor = lightColor
                    textEdgeType = 1
                    textEdgeColor = (66,
                     95,
                     133,
                     255)
                    caption = '\xb8\xf9\xbe\xdd\xc4\xfa\xb5\xc4\xd1\xa1\xd4\xf1\xa3\xac\xd0\xe8\xbd\xf8\xd0\xd0\xcf\xfb\xb7\xd1\xd1\xe9\xd6\xa4'

                class IDText(TLabel):
                    __module__ = __name__
                    rect = (50,
                     70,
                     200,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc3\xdc\xb1\xa3\xbf\xa8\xd1\xe9\xd6\xa4'

                class licenseLabel(TLabel):
                    __module__ = __name__
                    rect = (50,
                     100,
                     110,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc4\xfa\xb5\xc4\xc3\xdc\xb1\xa3\xbf\xa8\xd0\xf2\xc1\xd0\xba\xc5:'

                class licenseText(licenseLabel):
                    __module__ = __name__
                    rect = (160,
                     100,
                     100,
                     12)

                class cardPosLabel(licenseLabel):
                    __module__ = __name__
                    rect = (50,
                     150,
                     100,
                     12)
                    caption = '\xc3\xdc\xb1\xa3\xbf\xa8\xce\xbb\xd6\xc3:'

                class cardPos1(licenseLabel):
                    __module__ = __name__
                    rect = (123,
                     150,
                     30,
                     12)

                class cardPos2(licenseLabel):
                    __module__ = __name__
                    rect = (164,
                     150,
                     30,
                     12)

                class cardPos3(licenseLabel):
                    __module__ = __name__
                    rect = (203,
                     150,
                     30,
                     12)

                class cardNumberLabel(licenseLabel):
                    __module__ = __name__
                    rect = (50,
                     180,
                     70,
                     12)
                    caption = '\xc3\xdc\xb1\xa3\xbf\xa8\xca\xfd\xd7\xd6:'

                class cardNumber1(TEditCharNum):
                    __module__ = __name__
                    caption = ''
                    editable = 1
                    textstyle = 0
                    rect = (120,
                     175,
                     30,
                     24)
                    captionrect = (6,
                     5,
                     30,
                     14)
                    maxchar = 2
                    bkimage = 'object/ui/shop/secrecyValidate/txt_small.img'
                    textEdgeType = -1
                    drawcolor = maskColor

                class cardNumber2(cardNumber1):
                    __module__ = __name__
                    rect = (158,
                     175,
                     30,
                     24)

                class cardNumber3(cardNumber1):
                    __module__ = __name__
                    rect = (196,
                     175,
                     30,
                     24)

                class resetCardLink(THyperLink):
                    __module__ = __name__
                    rect = (270,
                     181,
                     100,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    URL = 'https://mibaoka.qq.com/cgi-bin/index'
                    caption = '\xd6\xd8\xd0\xc2\xc9\xe8\xd6\xc3\xc3\xdc\xb1\xa3\xbf\xa8'

                class forwardBtn(TButton):
                    __module__ = __name__
                    rect = (140,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_forward.img'

                    def OnClick(this):
                        ui_setCapture('UI.shop.defaultSecrecyValidateDlg')
                        Win_ShowWidget('UI.shop.secrecyCardDlg', 0)



                class nextBtn(TButton):
                    __module__ = __name__
                    rect = (221,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_next.img'

                    def OnClick(this):
                        ui = 'UI.shop.secrecyCardDlg'
                        cardValue = ['',
                         '',
                         '',
                         '']
                        for i in range(coorNum):
                            cardValue[i] = Win_GetText(((ui + '.cardNumber') + str((i + 1))))
                            if ((len(cardValue[i]) != coorSize) and showErrorResult(0, (((('\xc4\xfa\xca\xe4\xc8\xeb\xb5\xc4\xb5\xda' + str((i + 1))) + '\xb8\xf6\xc3\xdc\xb1\xa3\xbf\xa8\xca\xfd\xd7\xd6\xce\xde\xd0\xa7\xa3\xac\xc7\xeb\xca\xe4\xc8\xeb') + str(coorSize)) + '\xce\xbb\xc3\xdc\xb1\xa3\xca\xfd\xd7\xd6'))):
                                return 

                        cardCoorList = ''
                        cardPwdList = ''
                        pwdLen = 0
                        for i in range(coorNum):
                            cardCoorList = (cardCoorList + coorList[i])
                            cardPwdList = (cardPwdList + cardValue[i])
                            pwdLen = (pwdLen + len(cardValue[i]))

                        SetCardData(coorNum, coorSize, cardCoorList, pwdLen, cardPwdList)
                        Win_ShowWidget('UI.shop.secrecyCardDlg', 0)



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (327,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_cancel.img'

                    def OnClick(this):
                        CancelVerify()
                        Win_ShowWidget('UI.shop.secrecyCardDlg', 0)





        class mobileTokenDlg(TStatic):
            __module__ = __name__
            darkBG = 1
            visible = 0
            initlayer = 999999
            rect = (219,
             91,
             450,
             315)
            bkimage = 'object/ui/shop/secrecyValidate/dlg_DefaultSecrecyValidate.img'
            class children:
                __module__ = __name__
                class title(TLabel):
                    __module__ = __name__
                    rect = (150,
                     40,
                     250,
                     12)
                    drawcolor = lightColor
                    textEdgeType = 1
                    textEdgeColor = (66,
                     95,
                     133,
                     255)
                    caption = '\xb8\xf9\xbe\xdd\xc4\xfa\xb5\xc4\xd1\xa1\xd4\xf1\xa3\xac\xd0\xe8\xbd\xf8\xd0\xd0\xcf\xfb\xb7\xd1\xd1\xe9\xd6\xa4'

                class IDText(TLabel):
                    __module__ = __name__
                    rect = (50,
                     85,
                     200,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc3\xdc\xb1\xa3\xc1\xee\xc5\xc6\xd1\xe9\xd6\xa4'

                class tokenLabel(TLabel):
                    __module__ = __name__
                    rect = (50,
                     120,
                     350,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc7\xeb\xc4\xfa\xb6\xd4\xd5\xd5\xc4\xfa\xca\xd6\xbb\xfa\xc9\xcf\xb5\xc4\xc3\xdc\xb1\xa3\xc1\xee\xc5\xc6\xc8\xed\xbc\xfe\xa3\xac\xb0\xb4\xd5\xd5\xcf\xd4\xca\xbe\xb5\xc46\xce\xbb\xca\xfd\xd7\xd6\xca\xe4\xc8\xeb'

                class tokenText(TEditCharNum):
                    __module__ = __name__
                    textstyle = 0
                    editable = 1
                    rect = (50,
                     140,
                     274,
                     24)
                    captionrect = (4,
                     5,
                     50,
                     14)
                    maxchar = 6
                    bkimage = 'object/ui/shop/secrecyValidate/txt_long.img'
                    textEdgeType = -1
                    drawcolor = maskColor

                class forwardBtn(TButton):
                    __module__ = __name__
                    rect = (140,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_forward.img'

                    def OnClick(this):
                        ui_setCapture('UI.shop.defaultSecrecyValidateDlg')
                        Win_ShowWidget('UI.shop.mobileTokenDlg', 0)



                class nextBtn(TButton):
                    __module__ = __name__
                    rect = (221,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_next.img'

                    def OnClick(this):
                        text = Win_GetText('UI.shop.mobileTokenDlg.tokenText')
                        if ((len(text) < 6) and showErrorResult(0, '\xc4\xfa\xc3\xbb\xd3\xd0\xca\xe4\xc8\xeb\xbb\xf2\xca\xe4\xc8\xeb\xb5\xc4Token\xc2\xeb\xb2\xbb\xb9\xbb6\xce\xbb,\xc7\xeb\xba\xcb\xca\xb5\xba\xf3\xd6\xd8\xd0\xc2\xca\xe4\xc8\xeb')):
                            pass



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (327,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_cancel.img'

                    def OnClick(this):
                        CancelVerify()
                        Win_ShowWidget('UI.shop.mobileTokenDlg', 0)





        class telephoneIVRDlg(TStatic):
            __module__ = __name__
            darkBG = 1
            visible = 0
            initlayer = 999999
            rect = (219,
             91,
             450,
             315)
            bkimage = 'object/ui/shop/secrecyValidate/dlg_DefaultSecrecyValidate.img'
            class children:
                __module__ = __name__
                class title(TLabel):
                    __module__ = __name__
                    rect = (150,
                     40,
                     250,
                     12)
                    drawcolor = lightColor
                    textEdgeType = 1
                    textEdgeColor = (66,
                     95,
                     133,
                     255)
                    caption = '\xb8\xf9\xbe\xdd\xc4\xfa\xb5\xc4\xd1\xa1\xd4\xf1\xa3\xac\xd0\xe8\xbd\xf8\xd0\xd0\xcf\xfb\xb7\xd1\xd1\xe9\xd6\xa4'

                class IDText(TLabel):
                    __module__ = __name__
                    rect = (50,
                     70,
                     200,
                     12)
                    drawcolor = (0,
                     0,
                     255,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)
                    caption = '\xc3\xdc\xb1\xa3\xb5\xe7\xbb\xb0\xd1\xe9\xd6\xa4'

                class telephoneNumLabel(TLabel):
                    __module__ = __name__
                    rect = (50,
                     120,
                     300,
                     12)
                    drawcolor = (40,
                     40,
                     40,
                     255)
                    textEdgeColor = (255,
                     0,
                     0,
                     0)

                class telephoneIVRLabel(telephoneNumLabel):
                    __module__ = __name__
                    rect = (50,
                     140,
                     350,
                     12)

                class forwardBtn(TButton):
                    __module__ = __name__
                    rect = (140,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_forward.img'

                    def OnClick(this):
                        ui_setCapture('UI.shop.defaultSecrecyValidateDlg')
                        Win_ShowWidget('UI.shop.telephoneIVRDlg', 0)



                class nextBtn(TButton):
                    __module__ = __name__
                    rect = (221,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_next.img'

                    def OnClick(this):
                        SetIVRResult()
                        Win_ShowWidget('UI.shop.telephoneIVRDlg', 0)



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (327,
                     264,
                     80,
                     41)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/secrecyValidate/btn_cancel.img'

                    def OnClick(this):
                        CancelVerify()
                        Win_ShowWidget('UI.shop.telephoneIVRDlg', 0)





        class errorResultDlg(TStatic):
            __module__ = __name__
            darkBG = 1
            visible = 0
            initlayer = (999999 + 1)
            rect = (219,
             91,
             363,
             338)
            bkimage = 'object/ui/common/dlg_msgBox.img'
            class children:
                __module__ = __name__
                class content(TLabel):
                    __module__ = __name__
                    rect = (35,
                     100,
                     300,
                     30)
                    drawcolor = lightColor
                    textEdgeType = 1
                    textEdgeColor = (40,
                     40,
                     40,
                     255)
                    caption = ''

                class confirmBtn(TButton):
                    __module__ = __name__
                    rect = (150,
                     275,
                     41,
                     41)
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
                        Win_ShowWidget('UI.shop.errorResultDlg', 0)





        class useQBRad(TRadio):
            __module__ = __name__
            initlayer = -9999
            rect = (438,
             3,
             92,
             30)
            bkimage = 'object/ui/shop/rad_QB.img'
            (groupid, groupstop,) = (77,
             1)

            def OnClick(this):
                global curMoneyType
                PlaySound(soundUI, 1)
                curMoneyType = 'QB'
                clearAllChecks()
                clearAllPos()
                ui_updateWares()
                ui_updateWarePages()



        class useTangBRad(useQBRad):
            __module__ = __name__
            initlayer = -9999
            groupstop = 2
            rect = (535,
             3,
             92,
             30)
            bkimage = 'object/ui/shop/rad_TangB.img'

            def OnClick(this):
                global curMoneyType
                PlaySound(soundUI, 1)
                curMoneyType = 'TangB'
                clearAllChecks()
                clearAllPos()
                ui_updateWares()
                ui_updateWarePages()



        class useVNetRad(useQBRad):
            __module__ = __name__
            initlayer = -9999
            rect = (438,
             0,
             95,
             23)
            bkimage = 'object/ui/shop/rad_VNet.img'
            groupstop = 3

            def OnClick(this):
                global curMoneyType
                PlaySound(soundUI, 1)
                curMoneyType = 'VNet'
                clearAllChecks()
                ui_updateWares()
                ui_updateWarePages()



        class sugarMoney:
            __module__ = __name__
            rect = (679,
             32,
             110,
             13)
            type = 'NUMLABEL'
            bkimage = 'object/ui/common/numberMoney.img'
            textsize = 10
            textwidth = 9
            textheight = 13

            def OnInit():
                (qb, game, sugar,) = getMoney()
                if ((-1 == sugar) and Win_SetText('UI.shop.sugarMoney', '')):
                    pass



        class shopTicket:
            __module__ = __name__
            rect = (699,
             8,
             110,
             13)
            type = 'NUMLABEL'
            bkimage = 'object/ui/common/numberMoney.img'
            textsize = 10
            textwidth = 9
            textheight = 13
            textstyle = dt_left

            def OnInit():
                if ((QQTTicket < 0) and Win_SetText('UI.shop.shopTicket', '')):
                    pass



        class functionTab(TTabWin):
            __module__ = __name__
            initlayer = 999
            rect = (0,
             0,
             1,
             1)
            hotrect = (82,
             7,
             63,
             28)
            hotcover = 'object/ui/shop/tab_func.img'
            groupstop = 1

            def OnClick(this):
                Win_SetText('UI.shop.subTab1', '\xb9\xa6\xc4\xdc\xb5\xc0\xbe\xdf')
                Win_SetText('UI.shop.subTab2', '\xd3\xce\xcf\xb7\xb5\xc0\xbe\xdf')
                Win_SetText('UI.shop.subTab3', '\xc6\xe4 \xcb\xfc')
                Win_SetText('UI.shop.subTab4', '\xbf\xe1\xb1\xc8\xb1\xa6\xca\xaf')
                Win_SetText('UI.shop.subTab5', '')
                setItemType(2)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)
                updateSelectedItems()



        class adviceTab(functionTab):
            __module__ = __name__
            initlayer = 999
            rect = (0,
             0,
             1,
             1)
            hotrect = (16,
             7,
             63,
             28)
            hotcover = 'object/ui/shop/tab_advice.img'
            groupstop = 0

            def OnClick(this):
                Win_SetText('UI.shop.subTab1', '\xd0\xc2\xc6\xb7\xcd\xc6\xbc\xf6')
                Win_SetText('UI.shop.subTab2', '\xb5\xcd\xbc\xdb\xb4\xd9\xcf\xfa')
                Win_SetText('UI.shop.subTab3', '\xcc\xd7\xd7\xb0\xc8\xc8\xc2\xf4')
                Win_SetText('UI.shop.subTab4', '\xcf\xb5\xc1\xd0\xd5\xb9\xca\xbe')
                Win_SetText('UI.shop.subTab5', '')
                setItemType(1)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)
                updateSelectedItems()



        class costumeTab(functionTab):
            __module__ = __name__
            initlayer = 999
            rect = (0,
             0,
             1,
             1)
            hotrect = (149,
             7,
             63,
             28)
            hotcover = 'object/ui/shop/tab_adorn.img'
            groupstop = 2

            def OnClick(this):
                Win_SetText('UI.shop.subTab1', '\xcc\xc7 \xc5\xdd')
                Win_SetText('UI.shop.subTab2', '\xbb\xc3 \xd3\xb0')
                Win_SetText('UI.shop.subTab3', '\xb1\xb3 \xbe\xb0')
                Win_SetText('UI.shop.subTab4', '\xb1\xdf\xbf\xf2\xc8\xeb\xb3\xa1')
                Win_SetText('UI.shop.subTab5', '\xc3\xfb \xc6\xac')
                setItemType(3)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)
                updateSelectedItems()



        class equipTab(functionTab):
            __module__ = __name__
            initlayer = 999
            rect = (0,
             0,
             1,
             1)
            hotrect = (216,
             7,
             63,
             28)
            hotcover = 'object/ui/shop/tab_equip.img'
            groupstop = 3

            def OnClick(this):
                Win_SetText('UI.shop.subTab1', '\xcd\xb7 \xb2\xbf')
                Win_SetText('UI.shop.subTab2', '\xd5\xfd \xc3\xe6')
                Win_SetText('UI.shop.subTab3', '\xb1\xb3 \xc3\xe6')
                Win_SetText('UI.shop.subTab4', '\xc9\xed \xcc\xe5')
                Win_SetText('UI.shop.subTab5', '\xbd\xc5 \xd3\xa1')
                setItemType(4)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)
                updateSelectedItems()



        class petTab(functionTab):
            __module__ = __name__
            initlayer = 999
            rect = (0,
             0,
             1,
             1)
            hotrect = (283,
             7,
             63,
             28)
            hotcover = 'object/ui/shop/tab_pet.img'
            groupstop = 4

            def OnClick(this):
                Win_SetText('UI.shop.subTab1', '\xb3\xe8\xce\xef\xca\xb3\xc6\xb7')
                Win_SetText('UI.shop.subTab2', '\xb3\xe8\xce\xef\xbc\xbc\xc4\xdc')
                Win_SetText('UI.shop.subTab3', '\xb3\xe8\xce\xef\xbf\xa8\xc6\xac')
                Win_SetText('UI.shop.subTab4', '')
                Win_SetText('UI.shop.subTab5', '')
                setItemType(5)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)
                updateSelectedItems()



        class purplediamondTab(functionTab):
            __module__ = __name__
            initlayer = 999
            rect = (0,
             0,
             1,
             1)
            hotrect = (350,
             7,
             63,
             28)
            hotcover = 'object/ui/shop/tab_zizuan.img'
            groupstop = 5

            def OnClick(this):
                Win_SetText('UI.shop.subTab1', '\xd7\xa8\xca\xf4\xb5\xc0\xbe\xdf')
                Win_SetText('UI.shop.subTab2', '')
                Win_SetText('UI.shop.subTab3', '')
                Win_SetText('UI.shop.subTab4', '')
                Win_SetText('UI.shop.subTab5', '')
                setItemType(6)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)
                updateSelectedItems()



        class subTab1(TRadio):
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
            groupid = 2
            groupstop = 0
            rect = (21,
             44,
             57,
             25)
            bkimage = 'object/ui/shop/tab_sub.img'
            captionrect = (0,
             4,
             57,
             12)
            drawcolor = (106,
             94,
             86,
             255)
            textEdgeColor = lightColor
            textEdgeType = 0
            textstyle = dt_center

            def OnClick(this):
                Win_SetFocus()
                setItemSubType(1)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)



        class subTab2(subTab1):
            __module__ = __name__
            groupstop = 1
            rect = (84,
             44,
             57,
             25)

            def OnClick(this):
                Win_SetFocus()
                setItemSubType(2)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)



        class subTab3(subTab1):
            __module__ = __name__
            groupstop = 2
            rect = (147,
             44,
             57,
             25)

            def OnClick(this):
                Win_SetFocus()
                setItemSubType(3)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)



        class subTab4(subTab1):
            __module__ = __name__
            groupstop = 3
            rect = (210,
             44,
             57,
             25)

            def OnClick(this):
                Win_SetFocus()
                setItemSubType(4)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)



        class subTab5(subTab1):
            __module__ = __name__
            groupstop = 4
            rect = (273,
             44,
             57,
             25)

            def OnClick(this):
                Win_SetFocus()
                setItemSubType(5)
                hideWareForFruitMachine()
                setLRPosition()
                PlaySound(soundUI, 1)



        class ware1(TCheck):
            __module__ = __name__
            initlayer = 2
            rect = (16,
             84,
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
            tipwidget = 'UI.shop.description'

            def OnMouseMoveIn():
                ui = 'UI.shop.description'
                i = (getMyMidIdx() - 1)
                wareID = wareIDs[i]
                if (wareID > 0):
                    statement = curDispWares[i].statement
                    info = WareList().at(itemType, itemSubType, (warePos[itemType][itemSubType] + i))
                    Win_ShowWidget(ui, 1)
                    Win_SetText(ui, (statement[0:34] + '......'))
                    me = Win_GetMyPath()
                    winrect = Win_GetRect(me, value_channel_winrect)
                    caprect = Win_GetRect(ui, value_channel_captionrect)
                    Win_Move2Pos(ui, (winrect[0] + 70), ((winrect[1] + caprect[3]) - 10))
                else:
                    Win_ShowWidget(ui, 0)
                    return 



            def OnClick(me):
                ID = Win_GetText((me + '.ID'))
                if (Win_IsChecked(me) and clearChecks()):
                    Win_SetCheck(me, True)
                    useWare(ID)
                    wareCheck[itemType][itemSubType] = (getMyIdx() + warePos[itemType][itemSubType])
                    Win_ShowWidget((me + '.frame'), 1)
                Win_SetFocus()


            class children:
                __module__ = __name__
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

                class pricePic(TStatic):
                    __module__ = __name__
                    rect = (((97 - 19) - 6),
                     ((104 - 55) - 20),
                     24,
                     12)

                class price1(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (((97 - 19) - 6),
                     ((104 - 55) - 20),
                     24,
                     12)
                    drawcolor = (255,
                     255,
                     255,
                     255)
                    textstyle = dt_left
                    textLineType = 1

                class price2(TLabel,
                 Static):
                    __module__ = __name__
                    rect = ((((97 - 19) - 6) + 31),
                     ((104 - 55) - 20),
                     48,
                     12)
                    drawcolor = (255,
                     255,
                     255,
                     255)
                    caption = ''
                    textstyle = dt_right

                class memberPic(TStatic):
                    __module__ = __name__
                    rect = (((97 - 19) - 6),
                     50,
                     27,
                     12)
                    bkimage = 'object/ui/shop/wareAttr/memberPic.img'

                class memberPrice(TLabel,
                 Static):
                    __module__ = __name__
                    rect = ((((97 - 19) - 6) + 25),
                     50,
                     ((178 - 144) + 20),
                     12)
                    drawcolor = (255,
                     255,
                     255,
                     255)
                    textstyle = dt_right

                class buyA(TButton):
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

                    def OnClick(this):
                        global curBuyWareID
                        global execStr
                        global curBuyWareIdx
                        if SC_ClickBuyBtn():
                            i = (getMyMidIdx() - 1)
                            wareID = wareIDs[i]
                            buyMode = buyModes[i][0]
                            if (wareID > 0):
                                curBuyWareIdx = i
                                execStr = ('BuyCommodity(%d, 2, %d, 0)' % (wareID,
                                 buyMode))
                                curBuyWareID = wareID
                                name = Win_GetText(('UI.shop.ware%d.name' % (i + 1)))
                                fee = Win_GetText(('UI.shop.ware%d.price1' % (i + 1)))
                                fee2 = Win_GetText(('UI.shop.ware%d.price2' % (i + 1)))
                                statement = curDispWares[i].statement
                                info = WareList().at(itemType, itemSubType, (warePos[itemType][itemSubType] + i))
                                if (curDispWares[i].period >= 0):
                                    periodStr = day2str(curDispWares[i].period)
                                    txt = ((('\xca\xb9\xd3\xc3\xca\xb1\xbc\xe4: %s\n' % periodStr) + '\xc9\xcc\xc6\xb7\xc3\xe8\xca\xf6: ') + statement)
                                else:
                                    numStr = (str(info.num) + ' \xb8\xf6')
                                    txt = ((('\xb5\xc0\xbe\xdf\xca\xfd\xc1\xbf: %s\n' % numStr) + '\xc9\xcc\xc6\xb7\xc3\xe8\xca\xf6: ') + statement)
                                ui = 'UI.shop.buyDlg'
                                Win_SetText((ui + '.name'), name)
                                rebate = 100
                                memberRebate = 100
                                if ((info.rebate >= 0) and (info.rebate < 100)):
                                    rebate = info.rebate
                                if ((isLeague or isQQMember) and ((info.memberRebate >= 0) and (info.memberRebate < 100))):
                                    memberRebate = info.memberRebate
                            if ((curMoneyType == 'QB') and Win_SetText((ui + '.price1'), makeStr(15, ((((info.priceQQ * memberRebate) * rebate) + 9999) / 10000), ' Q\xb1\xd2', 1))):
                                Win_SetText((ui + '.price2'), makeStr(15, ((((info.priceQQ * memberRebate) * rebate) + 999) / 1000), '\xbf\xe1\xb1\xc8\xb1\xa6\xca\xaf'))
                                Win_SetText((ui + '.price3'), makeStr(15, ((((info.priceGame * memberRebate) * rebate) + 9999) / 10000), 'Q\xb5\xe3'))
                            Win_SetText((ui + '.txt'), txt)
                            Win_ShowWidget((ui + '.buy2Btn'), (curMoneyType == 'QB'))
                            Win_ShowWidget((ui + '.price2'), (curMoneyType == 'QB'))
                            Win_ShowWidget((ui + '.buy3Btn'), (curMoneyType == 'QB'))
                            Win_ShowWidget((ui + '.price3'), (curMoneyType == 'QB'))
                            desc = commodityList[curBuyWareID]
                            (type, idx,) = desc[0:2]
                            if (((type == 'xeffect') or (type == 'feffect')) and Win_SetImg((ui + '.preview'), ((('object/xeffect/' + type) + str(idx)) + '_pre.img'))):
                                Win_ShowWidget((ui + '.preview'), True)
                            Win_EnableWidget((ui + '.donateBtn'), ((curMoneyType != 'VNet') or (loginType == 0)))
                            ui_setCapture(ui)





        class ware2(ware1):
            __module__ = __name__
            rect = (217,
             84,
             198,
             72)
            groupstop = 2
            initlayer = 1

        class ware3(ware1):
            __module__ = __name__
            rect = (16,
             (84 + 73),
             198,
             72)
            groupstop = 3
            initlayer = 4

        class ware4(ware1):
            __module__ = __name__
            rect = (217,
             (84 + 73),
             198,
             72)
            groupstop = 4
            initlayer = 3

        class ware5(ware1):
            __module__ = __name__
            rect = (16,
             (84 + (73 * 2)),
             198,
             72)
            groupstop = 5
            initlayer = 6

        class ware6(ware1):
            __module__ = __name__
            rect = (217,
             (84 + (73 * 2)),
             198,
             72)
            groupstop = 6
            initlayer = 5

        class ware7(ware1):
            __module__ = __name__
            rect = (16,
             (84 + (73 * 3)),
             198,
             72)
            groupstop = 7
            initlayer = 8

        class ware8(ware1):
            __module__ = __name__
            rect = (217,
             (84 + (73 * 3)),
             198,
             72)
            groupstop = 8
            initlayer = 7

        class ware9(ware1):
            __module__ = __name__
            rect = (16,
             (84 + (73 * 4)),
             198,
             72)
            groupstop = 9
            initlayer = 10

        class ware10(ware1):
            __module__ = __name__
            rect = (217,
             (84 + (73 * 4)),
             198,
             72)
            groupstop = 10
            initlayer = 9

        class ware11(ware1):
            __module__ = __name__
            rect = (16,
             (84 + (73 * 5)),
             198,
             72)
            groupstop = 11
            initlayer = 12

        class ware12(ware1):
            __module__ = __name__
            rect = (217,
             (84 + (73 * 5)),
             198,
             72)
            groupstop = 12
            initlayer = 11

        class attr1(TStatic):
            __module__ = __name__
            initlayer = 99999
            visible = 1
            rect = (174,
             55,
             61,
             57)
            bkimage = ''
            class children:
                __module__ = __name__
                class rebate(TStatic):
                    __module__ = __name__
                    rect = (20,
                     27,
                     11,
                     15)
                    bkimage = ''

                class rebateH(TStatic):
                    __module__ = __name__
                    rect = (5,
                     27,
                     11,
                     15)
                    bkimage = ''

                class point(TStatic):
                    __module__ = __name__
                    rect = (16,
                     27,
                     11,
                     15)
                    bkimage = 'object/ui/shop/wareAttr/point.img'

                class rebateL(TStatic):
                    __module__ = __name__
                    rect = (23,
                     27,
                     11,
                     15)
                    bkimage = ''

                class rebateWord(TStatic):
                    __module__ = __name__
                    rect = (35,
                     27,
                     18,
                     18)
                    bkimage = 'object/ui/shop/wareAttr/zhe.img'



        class attr2(attr1):
            __module__ = __name__
            rect = (374,
             55,
             61,
             57)

        class attr3(attr1):
            __module__ = __name__
            rect = (174,
             (55 + 73),
             61,
             57)

        class attr4(attr1):
            __module__ = __name__
            rect = (374,
             (55 + 73),
             61,
             57)

        class attr5(attr1):
            __module__ = __name__
            rect = (174,
             (55 + (73 * 2)),
             61,
             57)

        class attr6(attr1):
            __module__ = __name__
            rect = (374,
             (55 + (73 * 2)),
             61,
             57)

        class attr7(attr1):
            __module__ = __name__
            rect = (174,
             (55 + (73 * 3)),
             61,
             57)

        class attr8(attr1):
            __module__ = __name__
            rect = (374,
             (55 + (73 * 3)),
             61,
             57)

        class attr9(attr1):
            __module__ = __name__
            rect = (174,
             (55 + (73 * 4)),
             61,
             57)

        class attr10(attr1):
            __module__ = __name__
            rect = (374,
             (55 + (73 * 4)),
             61,
             57)

        class attr11(attr1):
            __module__ = __name__
            rect = (174,
             (55 + (73 * 5)),
             61,
             57)

        class attr12(attr1):
            __module__ = __name__
            rect = (374,
             (55 + (73 * 5)),
             61,
             57)

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

        class warePage:
            __module__ = __name__
            initlayer = 100000
            type = 'NUMLABEL'
            rect = (290,
             378,
             100,
             24)
            bkimage = 'object/ui/common/number2.img'
            textstyle = dt_center
            textsize = 19
            textwidth = 19
            textheight = 24

        class left(TButton):
            __module__ = __name__
            initlayer = 100000
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            rect = (260,
             372,
             33,
             35)
            bkimage = 'object/ui/common/btn_left.img'

            def OnClick(this):
                if ((itemType == 1) and (itemSubType == 1)):
                    itemShowCnt = 8
                else:
                    itemShowCnt = 12
                if (warePos[itemType][itemSubType] >= itemShowCnt):
                    warePos[itemType][itemSubType] -= itemShowCnt
                    ui_updateWares()
                    PlaySound(soundUI, 1)
                else:
                    PlaySound(soundFail, 1)
                ui_updateWarePages()



        class right(TButton):
            __module__ = __name__
            initlayer = 100000
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            rect = (380,
             372,
             33,
             35)
            bkimage = 'object/ui/common/btn_right.img'

            def OnClick(this):
                if ((itemType == 1) and (itemSubType == 1)):
                    itemShowCnt = 8
                else:
                    itemShowCnt = 12
                wareCnt = WareList().getCnt(itemType, itemSubType)
                if ((warePos[itemType][itemSubType] + itemShowCnt) < wareCnt):
                    warePos[itemType][itemSubType] += itemShowCnt
                    ui_updateWares()
                    PlaySound(soundUI, 1)
                else:
                    PlaySound(soundFail, 1)
                ui_updateWarePages()



        class buyDlg(TDlg):
            __module__ = __name__
            darkBG = 1
            initlayer = 999999
            visible = 0
            rect = (((800 - 327) / 2),
             ((600 - 378) / 2),
             327,
             378)
            bkimage = 'object/ui/shop/dlg_buy.img'

            def OnEscape():
                doUI('UI.shop.buyDlg.closeBtn', 'OnClick')


            class children:
                __module__ = __name__
                class name(TLabel,
                 Static):
                    __module__ = __name__
                    drawcolor = lightColor
                    textEdgeType = -1
                    rect = (35,
                     28,
                     250,
                     28)
                    textstyle = (dt_center + dt_vcenter)

                class txt(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (35,
                     65,
                     250,
                     115)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    rowspace = 2

                class price1(TLabel,
                 Static):
                    __module__ = __name__
                    initlayer = -99
                    rect = (100,
                     246,
                     150,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = dt_right

                class checkRectQB(TStatic):
                    __module__ = __name__
                    rect = (20,
                     272,
                     250,
                     15)
                    initlayer = -100
                    class children:
                        __module__ = __name__
                        class checkBtn(TStdCheck):
                            __module__ = __name__
                            rect = (6,
                             0,
                             12,
                             15)
                            bkimagepos = (0,
                             5)

                            def OnClick(this):
                                global isAllowQBMixedPay
                                ui = 'UI.shop.buyDlg.checkRectQB'
                                if Win_IsChecked((ui + '.checkBtn')):
                                    isAllowQBMixedPay = 1
                                else:
                                    isAllowQBMixedPay = 0
                                PlaySound(soundUI, 1)



                        class text(TLabel):
                            __module__ = __name__
                            rect = (22,
                             2,
                             200,
                             15)
                            drawcolor = (0,
                             0,
                             255,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            textstyle = dt_right
                            caption = '\xc8\xf4Q\xb1\xd2\xb2\xbb\xd7\xe3\xca\xb1,\xd3\xc3Q\xb5\xe3\xd6\xa7\xb8\xb6\xb2\xbb\xd7\xe3\xb2\xbf\xb7\xd6\xb7\xd1\xd3\xc3'



                class price2(TLabel,
                 Static):
                    __module__ = __name__
                    initlayer = -99
                    rect = (100,
                     305,
                     150,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = dt_right

                class price3(TLabel,
                 Static):
                    __module__ = __name__
                    initlayer = -99
                    rect = (100,
                     186,
                     150,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = dt_right

                class checkRectQD(TStatic):
                    __module__ = __name__
                    rect = (20,
                     214,
                     250,
                     15)
                    initlayer = -100
                    class children:
                        __module__ = __name__
                        class checkBtn(TStdCheck):
                            __module__ = __name__
                            rect = (6,
                             0,
                             12,
                             15)
                            bkimagepos = (0,
                             5)

                            def OnClick(this):
                                global isAllowMixedPay
                                ui = 'UI.shop.buyDlg.checkRectQD'
                                if Win_IsChecked((ui + '.checkBtn')):
                                    isAllowMixedPay = 1
                                else:
                                    isAllowMixedPay = 0
                                PlaySound(soundUI, 1)



                        class text(TLabel):
                            __module__ = __name__
                            rect = (22,
                             2,
                             200,
                             15)
                            drawcolor = (0,
                             0,
                             255,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            textstyle = dt_right
                            caption = '\xc8\xf4Q\xb5\xe3\xb2\xbb\xd7\xe3\xca\xb1,\xd3\xc3Q\xb1\xd2\xd6\xa7\xb8\xb6\xb2\xbb\xd7\xe3\xb2\xbf\xb7\xd6\xb7\xd1\xd3\xc3'



                class preview(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (12,
                     251,
                     149,
                     270)
                    alphafactor = 1.0
                    minalphafactor = 0.0

                class buy1Btn(TButton):
                    __module__ = __name__
                    rect = (260,
                     234,
                     33,
                     34)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/btn_buy.img'

                    def OnClick(this):
                        Win_ShowWidget('UI.shop.buyDlg', 0)
                        PlaySound(soundLeave, 1)
                        if ((curMoneyType == 'QB') and BuyCommodity(curBuyWareID, 2, 1, isAllowQBMixedPay)):
                            pass



                class buy2Btn(buy1Btn):
                    __module__ = __name__
                    rect = (260,
                     290,
                     33,
                     34)

                    def OnClick(this):
                        Win_ShowWidget('UI.shop.buyDlg', 0)
                        PlaySound(soundLeave, 1)
                        BuyCommodity(curBuyWareID, 2, 6, 0)



                class buy3Btn(buy1Btn):
                    __module__ = __name__
                    rect = (260,
                     177,
                     33,
                     40)

                    def OnClick(this):
                        Win_ShowWidget('UI.shop.buyDlg', 0)
                        PlaySound(soundLeave, 1)
                        BuyCommodity(curBuyWareID, 2, 7, isAllowMixedPay)



                class requireBtn(TButton):
                    __module__ = __name__
                    enable = 0
                    rect = (27,
                     328,
                     63,
                     31)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/btn_require.img'

                class donateBtn(TButton):
                    __module__ = __name__
                    enable = 1
                    rect = (100,
                     328,
                     63,
                     31)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/btn_donate.img'

                    def OnClick(this):
                        setDonateDlg()
                        ui_setCapture('UI.shop.donateDlg')



                class closeBtn(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    rect = (190,
                     328,
                     43,
                     31)
                    bkimage = 'object/ui/common/btn_close.img'

                    def OnClick(this):
                        Win_ShowWidget('UI.shop.buyDlg', 0)
                        PlaySound(soundLeave, 1)





        class buyFailDlg(TDlg):
            __module__ = __name__
            darkBG = 1
            initlayer = 999999
            visible = 0
            rect = (((800 - 368) / 2),
             ((600 - 326) / 2),
             368,
             326)
            bkimage = 'object/ui/common/dlg_msgBox.img'
            class children:
                __module__ = __name__
                class close(TButton):
                    __module__ = __name__
                    rect = (93,
                     280,
                     43,
                     31)
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
                        Win_ShowWidget('UI.shop.buyFailDlg', 0)



                class QB(TButton):
                    __module__ = __name__
                    rect = (200,
                     278,
                     87,
                     31)
                    bkimage = 'object/ui/shop/btn_addQB.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget('UI.shop.buyFailDlg', 0)
                        ui_jumpWeb('http://pay.qq.com/')



                class text:
                    __module__ = __name__
                    type = 'LABEL'
                    rowspace = 2
                    rect = (45,
                     85,
                     270,
                     120)
                    bkimagepos = (0,
                     0)
                    textsize = 12
                    textstyle = (dt_left + dt_top)
                    textEdgeType = -1
                    drawcolor = zoneChooseColor



        class donateDlg(TDlg):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 327) / 2),
             ((600 - 378) / 2),
             327,
             378)
            bkimage = 'object/ui/shop/dlg_donate.img'
            class children:
                __module__ = __name__
                class price(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (110,
                     82,
                     100,
                     12)
                    drawcolor = maskColor
                    textEdgeType = -1
                    textstyle = dt_left

                class receiveUin(TEditID):
                    __module__ = __name__
                    rect = (110,
                     106,
                     100,
                     12)
                    drawcolor = (255,
                     255,
                     255,
                     255)
                    textEdgeColor = (255,
                     1,
                     255,
                     0)

                    def OnTab():
                        Win_SetFocus('UI.shop.donateDlg.text')



                class checkRectQBPresent(TStatic):
                    __module__ = __name__
                    rect = (20,
                     128,
                     250,
                     15)
                    initlayer = -100
                    class children:
                        __module__ = __name__
                        class checkBtn(TStdCheck):
                            __module__ = __name__
                            rect = (6,
                             0,
                             12,
                             15)
                            bkimagepos = (0,
                             5)

                            def OnClick(this):
                                global isAllowPresentMixedPay
                                ui = 'UI.shop.donateDlg.checkRectQBPresent'
                                if Win_IsChecked((ui + '.checkBtn')):
                                    isAllowPresentMixedPay = 1
                                else:
                                    isAllowPresentMixedPay = 0
                                PlaySound(soundUI, 1)



                        class text(TLabel):
                            __module__ = __name__
                            rect = (20,
                             2,
                             200,
                             15)
                            drawcolor = (0,
                             0,
                             255,
                             255)
                            textEdgeColor = (255,
                             0,
                             0,
                             0)
                            textstyle = dt_left
                            caption = '\xc8\xf4Q\xb1\xd2\xb2\xbb\xd7\xe3,\xd3\xc3Q\xb5\xe3\xd6\xa7\xb8\xb6\xb2\xbb\xd7\xe3\xb2\xbf\xb7\xd6\xb7\xd1\xd3\xc3'



                class text:
                    __module__ = __name__
                    type = 'MULTIEDIT'
                    maxchar = 100
                    rect = (45,
                     190,
                     235,
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



                class warePic(TStatic):
                    __module__ = __name__
                    bkImgFlag = dt_center
                    rect = (233,
                     72,
                     66,
                     66)

                class wareName(TLabel,
                 Static):
                    __module__ = __name__
                    rect = (216,
                     140,
                     100,
                     20)
                    drawcolor = (255,
                     255,
                     0,
                     255)
                    textstyle = dt_center

                class confirm(TButton):
                    __module__ = __name__
                    rect = (87,
                     329,
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
                        ui = 'UI.shop.donateDlg'
                        recUin = Win_GetText((ui + '.receiveUin'))
                        text = Win_GetText((ui + '.text'))
                        Win_ShowWidget('UI.shop.donateDlg', 0)
                        Win_ShowWidget('UI.shop.buyDlg', 0)
                        PlaySound(soundLeave, 1)
                        if ((curMoneyType == 'QB') and PresentCommodity(int(recUin), curBuyWareID, len(text), text, 2, 1, isAllowPresentMixedPay)):
                            pass



                class cancel(TButton):
                    __module__ = __name__
                    rect = (188,
                     329,
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
                        Win_ShowWidget('UI.shop.donateDlg', 0)
                        ui_setCapture('UI.shop.buyDlg')





        class charUpBtn(TButton):
            __module__ = __name__
            initlayer = -9999
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            rect = (440,
             35,
             33,
             35)
            bkimage = 'object/ui/common/btn_left.img'

            def OnClick(this):
                setNudeState()
                shopPlayer_changeRole(-1, 1)
                Win_SetImg('UI.shop.charIcon', getCharIconName())
                PlaySound(soundUI, 1)
                InitPlayerActiveItems()
                Win_SetFocus()



        class charDownBtn(charUpBtn):
            __module__ = __name__
            initlayer = -9999
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            rect = (595,
             35,
             33,
             35)
            bkimage = 'object/ui/common/btn_right.img'

            def OnClick(this):
                setNudeState()
                shopPlayer_changeRole(1, 1)
                Win_SetImg('UI.shop.charIcon', getCharIconName())
                PlaySound(soundUI, 1)
                InitPlayerActiveItems()
                Win_SetFocus()



        class charIcon(TStatic):
            __module__ = __name__
            initlayer = -99999
            rect = (476,
             37,
             66,
             27)

        class preview(TStatic):
            __module__ = __name__
            initlayer = -999
            rect = (351,
             92,
             275,
             95)
            class children:
                __module__ = __name__
                class bg(TStatic):
                    __module__ = __name__
                    framescheme = [(0,
                      99,
                      0,
                      99,
                      0,
                      99,
                      0,
                      99)]
                    bkImgFlag = dt_center
                    framespeed = 0.25
                    initlayer = -9999
                    rect = (94,
                     11,
                     96,
                     96)

                class bgCover(TStatic):
                    __module__ = __name__
                    initlayer = -999
                    rect = (0,
                     0,
                     275,
                     95)

                class enter(TStatic):
                    __module__ = __name__
                    bkImgFlag = (dt_center | eBkImgPlayOnce)
                    framespeed = 0.25
                    initlayer = 999
                    framespeed = 0.25
                    framescheme = [(0,
                      99,
                      0,
                      99,
                      0,
                      99,
                      0,
                      99)]
                    rect = (94,
                     11,
                     96,
                     96)

                class frame(TStatic):
                    __module__ = __name__
                    bkImgFlag = dt_center
                    initlayer = 999
                    framespeed = 0.25
                    framescheme = [(0,
                      99,
                      0,
                      99,
                      0,
                      99,
                      0,
                      99)]
                    rect = (94,
                     11,
                     96,
                     96)

                class demo(TStatic):
                    __module__ = __name__
                    initlayer = 9999
                    rect = ((563 - 508),
                     (123 - 138),
                     46,
                     62)
                    callbackdraw = 'SC_shopDemo_draw'



        class lighticon(TStatic):
            __module__ = __name__
            initlayer = -99999
            rect = (556,
             94,
             232,
             25)
            class children:
                __module__ = __name__
                class cap(TStatic):
                    __module__ = __name__
                    rect = (0,
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_cap.img'

                class fhadorn(cap):
                    __module__ = __name__
                    None

                class bhadorn(cap):
                    __module__ = __name__
                    None

                class thadorn(cap):
                    __module__ = __name__
                    None

                class hair(cap):
                    __module__ = __name__
                    None

                class mask(TStatic):
                    __module__ = __name__
                    rect = (23,
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_face.img'

                class eye(mask):
                    __module__ = __name__
                    None

                class mouth(mask):
                    __module__ = __name__
                    None

                class cladorn(TStatic):
                    __module__ = __name__
                    rect = ((23 * 2),
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_cloth.img'

                class ear(cladorn):
                    __module__ = __name__
                    None

                class foot(cladorn):
                    __module__ = __name__
                    None

                class leg(cladorn):
                    __module__ = __name__
                    None

                class cloth(cladorn):
                    __module__ = __name__
                    None

                class npack(TStatic):
                    __module__ = __name__
                    rect = ((23 * 3),
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_back.img'

                class fpack(npack):
                    __module__ = __name__
                    None

                class footprint(TStatic):
                    __module__ = __name__
                    rect = ((23 * 4),
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_foot.img'

                class bomb(TStatic):
                    __module__ = __name__
                    rect = ((1 + (23 * 5)),
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_bomb.img'

                class huanying(TStatic):
                    __module__ = __name__
                    rect = ((23 * 6),
                     2,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_huanying.img'

                class bg(TStatic):
                    __module__ = __name__
                    rect = ((23 * 7),
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_bg.img'

                class frame(bg):
                    __module__ = __name__
                    None

                class enter(bg):
                    __module__ = __name__
                    None

                class namecard(TStatic):
                    __module__ = __name__
                    rect = ((23 * 8),
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_namecard.img'

                class namecardbound(namecard):
                    __module__ = __name__
                    None

                class pet(TStatic):
                    __module__ = __name__
                    rect = ((23 * 9),
                     1,
                     1,
                     1)
                    bkimage = 'object/ui/shop/lightIcon/dlg_pet.img'



        class cancelEquip(TButton):
            __module__ = __name__
            initlayer = -99999
            rect = (720,
             143,
             63,
             31)
            bkimage = 'object/ui/shop/btn_cancelEquip.img'
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]

            def OnClick(this):
                setNudeState()
                clearSelected()
                PlaySound(soundUI, 1)



        class saveEquip(TButton):
            __module__ = __name__
            initlayer = -99999
            rect = (720,
             181,
             63,
             31)
            bkimage = 'object/ui/shop/btn_saveEquip.img'
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]

            def OnClick(this):
                global bClickSaveEquip
                sendActiveItems()
                clearSelected()
                bClickSaveEquip = 1
                PlaySound(soundLeave, 1)



        class namecardPreview(TStatic):
            __module__ = __name__
            initlayer = -9999
            rect = (468,
             217,
             310,
             25)
            class children:
                __module__ = __name__
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



        class myFunction(TTabWin):
            __module__ = __name__
            initlayer = -9999
            hotrect = (436,
             243,
             57,
             30)
            hotcover = 'object/ui/shop/tab_itemFunc.img'
            groupid = 1
            groupstop = 0

            def OnClick(this):
                doUI('UI.shop.functionTab', 'OnClick')
                setLRPosition()



        class myCostume(myFunction):
            __module__ = __name__
            hotrect = (495,
             243,
             57,
             30)
            hotcover = 'object/ui/shop/tab_itemAdorn.img'
            groupstop = 1

            def OnClick(this):
                doUI('UI.shop.costumeTab', 'OnClick')
                setLRPosition()



        class myEquip(myFunction):
            __module__ = __name__
            hotrect = (554,
             243,
             57,
             30)
            hotcover = 'object/ui/shop/tab_itemEquip.img'
            groupstop = 2

            def OnClick(this):
                doUI('UI.shop.equipTab', 'OnClick')
                setLRPosition()



        class mypet(myFunction):
            __module__ = __name__
            hotrect = (613,
             243,
             57,
             30)
            hotcover = 'object/ui/shop/tab_itemPet.img'
            groupstop = 3

            def OnClick(this):
                doUI('UI.shop.petTab', 'OnClick')
                setLRPosition()



        class myturplediamond(myFunction):
            __module__ = __name__
            hotrect = (672,
             243,
             57,
             30)
            hotcover = 'object/ui/shop/tab_itemZizuan.img'
            groupstop = 4

            def OnClick(this):
                doUI('UI.shop.purplediamondTab', 'OnClick')
                setLRPosition()



        class item1(TCheck):
            __module__ = __name__
            rect = (441,
             285,
             66,
             66)

            def OnClick(me):
                global myItemLastSelect
                ID = Win_GetText((me + '.ID'))
                myItemLastSelect = (itemPos[myItemType] + getTailNum(Win_GetMyPath()))
                useItem(ID)



            def OnRClick():
                global currentEggId
                me = Win_GetMyPath()
                itemID = int(Win_GetText((me + '.ID')))
                if ((itemID > 9000) and (itemID < 9011)):
                    currentEggId = itemID
                    if itemList.has_key(itemID):
                        iconType = itemList[itemID][0]
                        iconIdx = itemList[itemID][1]
                        Win_SetImg('UI.shop.breakEggDlg.eggPic', ('res/uires/icon/%s/%s%d.img' % (iconType,
                         iconType,
                         iconIdx)))
                        Win_SetText('UI.shop.breakEggDlg.description', itemList[itemID][3])
                    else:
                        currentEggId = 0
                        Win_SetImg('UI.shop.breakEggDlg.eggPic', '')
                        Win_SetText('UI.shop.breakEggDlg.description', '')
                    ui = 'UI.shop.breakEggDlg.hammer'
                    Win_EnableWidget((ui + '1'), 1)
                    Win_SetImg((ui + '1.hammerPic'), 'res/uiRes/icon/platform/platform9011.img')
                    Win_SetText((ui + '1.hammerCnt'), str(GetItemLeaveCount(9011)))
                    Win_EnableWidget((ui + '2'), 1)
                    Win_SetImg((ui + '2.hammerPic'), 'res/uiRes/icon/platform/platform9012.img')
                    Win_SetText((ui + '2.hammerCnt'), str(GetItemLeaveCount(9012)))
                    Win_EnableWidget((ui + '3'), 1)
                    Win_SetImg((ui + '3.hammerPic'), 'res/uiRes/icon/platform/platform9013.img')
                    Win_SetText((ui + '3.hammerCnt'), str(GetItemLeaveCount(9013)))
                    Win_SetImg('UI.shop.breakEggDlg.resultPic', '')
                    ui_setCapture('UI.shop.breakEggDlg')
                    PlaySound(soundUI, 1)
                    return 
                if itemList.has_key(itemID):
                    name = itemList[itemID][2]
                    statement = itemList[itemID][3]
                    idx = ((itemPos[myItemType] + getTailNum(Win_GetMyPath())) - 1)
                    info = ItemList().at(myItemType, idx)
                    leftTime = GetItemLeaveTime(itemID)
                    ui = 'UI.shop.repairDlg'
                    if ((leftTime >= 0) and Win_SetText((ui + '.time'), (str(leftTime) + '     \xcc\xec'))):
                        pass
                    price = GetRepairPrice(itemID)
                    Win_SetText((ui + '.price'), (str(price) + '   \xcc\xc7\xb1\xd2'))
                    Win_SetText((ui + '.title'), name)
                    Win_SetText((ui + '.text'), statement)
                    Win_SetText((ui + '.ID'), str(itemID))
                    ui_setCapture(ui)


            class children:
                __module__ = __name__
                class ID(TString):
                    __module__ = __name__
                    caption = '-1'

                class frame(TStatic):
                    __module__ = __name__
                    visible = 0
                    initlayer = -999
                    rect = (-3,
                     -3,
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

                class picture(TStatic):
                    __module__ = __name__
                    bkImgFlag = dt_center
                    rect = (32,
                     31,
                     1,
                     1)
                    bkimage = ''

                class hasEquiped(TStatic):
                    __module__ = __name__
                    initlayer = 11111
                    rect = (13,
                     40,
                     40,
                     17)
                    bkimage = ''

                class hasForged(TStatic):
                    __module__ = __name__
                    rect = (40,
                     3,
                     12,
                     12)

                class number(TLabel):
                    __module__ = __name__
                    initlayer = 11111
                    rect = (40,
                     3,
                     24,
                     12)
                    textEdgeType = 0
                    drawcolor = (135,
                     249,
                     255,
                     255)
                    textEdgeColor = maskColor



        class item2(item1):
            __module__ = __name__
            rect = ((442 + 69),
             285,
             66,
             66)

        class item3(item1):
            __module__ = __name__
            rect = ((442 + (69 * 2)),
             285,
             66,
             66)

        class item4(item1):
            __module__ = __name__
            rect = ((442 + (69 * 3)),
             285,
             66,
             66)

        class item5(item1):
            __module__ = __name__
            rect = ((442 + (69 * 4)),
             285,
             66,
             66)

        class item6(item1):
            __module__ = __name__
            rect = (441,
             354,
             66,
             66)

        class item7(item1):
            __module__ = __name__
            rect = ((442 + 69),
             354,
             66,
             66)

        class item8(item1):
            __module__ = __name__
            rect = ((442 + (69 * 2)),
             354,
             66,
             66)

        class item9(item1):
            __module__ = __name__
            rect = ((442 + (69 * 3)),
             354,
             66,
             66)

        class item10(item1):
            __module__ = __name__
            rect = ((442 + (69 * 4)),
             354,
             66,
             66)

        class item11(item1):
            __module__ = __name__
            rect = (441,
             423,
             66,
             66)

        class item12(item1):
            __module__ = __name__
            rect = ((442 + 69),
             423,
             66,
             66)

        class item13(item1):
            __module__ = __name__
            rect = ((442 + (69 * 2)),
             423,
             66,
             66)

        class item14(item1):
            __module__ = __name__
            rect = ((442 + (69 * 3)),
             423,
             66,
             66)

        class item15(item1):
            __module__ = __name__
            rect = ((442 + (69 * 4)),
             423,
             66,
             66)

        class myLeft(TButton):
            __module__ = __name__
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            rect = (717,
             490,
             33,
             35)
            bkimage = 'object/ui/common/btn_left.img'

            def OnClick(this):
                itemPos[myItemType] = max((itemPos[myItemType] - 15), 0)
                ui_updateMyItems()
                PlaySound(soundUI, 1)



        class myRight(TButton):
            __module__ = __name__
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            rect = (749,
             490,
             33,
             35)
            bkimage = 'object/ui/common/btn_right.img'

            def OnClick(this):
                if ((itemPos[myItemType] + 15) >= itemCnt):
                    return 
                itemPos[myItemType] = (itemPos[myItemType] + 15)
                ui_updateMyItems()
                PlaySound(soundUI, 1)



        class storageBtn(TButton):
            __module__ = __name__
            rect = (442,
             493,
             63,
             31)
            bkimage = 'object/ui/shop/btn_storage.img'
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]

            def OnClick(this):
                global step
                global IsShowStorageDlg
                global isStorageVisible
                IsShowStorageDlg = 0
                if ((0 == isStorageVisible) and Win_ShowWidget(uiRefineDlg, 0)):
                    isStorageVisible = 1
                    step = 30
                    Win_Timer(uiShopStorageDlg, 1)
                    ui_UpdateShopStorage()
                PlaySound(soundUI, 1)



        class storageDlg(TStatic):
            __module__ = __name__
            rect = (0,
             (0 - 598),
             427,
             598)
            initlayer = 999999
            bkimage = 'object/ui/storage/dlg_shopStorage.img'

            def OnTimer(this):
                Win_MovePos(uiShopStorageDlg, 0, step)
                if ((isStorageVisible and (Win_GetY(uiShopStorageDlg) >= 0)) and Win_Move2Pos(uiShopStorageDlg, 0, 0)):
                    Win_Timer(uiShopStorageDlg, 0)


            class children:
                __module__ = __name__
                class cleanUpBtn(TButton):
                    __module__ = __name__
                    rect = (10,
                     561,
                     63,
                     31)
                    bkimage = 'object/ui/storage/btn_cleanUp.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        RequestSettleStorage()
                        ui_UpdateShopStorage()



                class crossBtn(TButton):
                    __module__ = __name__
                    rect = (399,
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

                    def OnClick(this):
                        doUI('UI.shop.storageBtn', 'OnClick')



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
                    rect = (246,
                     558,
                     33,
                     35)
                    bkimage = 'object/ui/common/btn_left.img'

                    def OnClick(this):
                        global shopStoragePos
                        shopStoragePos = max((shopStoragePos - defShopStorageCnt), 0)
                        UpdateShopStorage()
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
                    rect = (365,
                     558,
                     33,
                     35)
                    bkimage = 'object/ui/common/btn_right.img'

                    def OnClick(this):
                        global shopStoragePos
                        if ((shopStoragePos + defShopStorageCnt) >= totalStorageCnt):
                            return 
                        shopStoragePos = (shopStoragePos + defShopStorageCnt)
                        UpdateShopStorage()
                        PlaySound(soundUI, 1)



                class storagePage:
                    __module__ = __name__
                    type = 'NUMLABEL'
                    rect = (280,
                     560,
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

                class storageItem0(TButton):
                    __module__ = __name__
                    framescheme = [(0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0)]
                    rect = (14,
                     47,
                     55,
                     55)
                    bkImgFlag = dt_center
                    tipwidget = (uiShopStorageDlg + '.storageDescription')

                    def OnRClick():
                        global curStorageID
                        me = getMyIdx2()
                        info = g_StorageList.at((me + shopStoragePos)).m_stItem
                        if IsBook(info.m_nItemID):
                            curStorageID = info.m_nItemID
                            ui_msgBox(1)
                            Win_ShowMsgBox('   \xc4\xe3\xc8\xb7\xc8\xcf\xd2\xaa\xd1\xa7\xcf\xb0\xb8\xc3\xbe\xed\xd6\xe1\xc2\xf0?', '', 0, 'UI.SysMsgbox', -5)



                    def OnMouseMoveIn():
                        me = Win_GetMyPath()
                        idx = (getMyIdx2() + shopStoragePos)
                        if (idx >= totalStorageCnt):
                            return 
                        info = g_StorageList.at(idx)
                        ui = (uiShopStorageDlg + '.storageDescription')
                        Win_SetText(ui, ((info.m_szName + '\n') + info.m_szDescrip))
                        winrect = Win_GetRect(me, value_channel_winrect)
                        caprect = Win_GetRect(ui, value_channel_captionrect)
                        Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))


                    class children:
                        __module__ = __name__
                        class itemNum(TLabel):
                            __module__ = __name__
                            rect = (30,
                             40,
                             24,
                             12)
                            drawcolor = zoneChooseColor
                            textEdgeType = 0
                            textEdgeColor = maskColor



                class storageItem1(storageItem0):
                    __module__ = __name__
                    rect = ((14 + 63),
                     47,
                     55,
                     55)

                class storageItem2(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     47,
                     55,
                     55)

                class storageItem3(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     47,
                     55,
                     55)

                class storageItem4(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     47,
                     55,
                     55)

                class storageItem5(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     47,
                     55,
                     55)

                class storageItem6(storageItem0):
                    __module__ = __name__
                    rect = (14,
                     (47 + (63 * 1)),
                     55,
                     55)

                class storageItem7(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 1)),
                     (47 + (63 * 1)),
                     55,
                     55)

                class storageItem8(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     (47 + (63 * 1)),
                     55,
                     55)

                class storageItem9(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     (47 + (63 * 1)),
                     55,
                     55)

                class storageItem10(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     (47 + (63 * 1)),
                     55,
                     55)

                class storageItem11(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     (47 + (63 * 1)),
                     55,
                     55)

                class storageItem12(storageItem0):
                    __module__ = __name__
                    rect = (14,
                     (47 + (63 * 2)),
                     55,
                     55)

                class storageItem13(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 1)),
                     (47 + (63 * 2)),
                     55,
                     55)

                class storageItem14(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     (47 + (63 * 2)),
                     55,
                     55)

                class storageItem15(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     (47 + (63 * 2)),
                     55,
                     55)

                class storageItem16(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     (47 + (63 * 2)),
                     55,
                     55)

                class storageItem17(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     (47 + (63 * 2)),
                     55,
                     55)

                class storageItem18(storageItem0):
                    __module__ = __name__
                    rect = (14,
                     (47 + (63 * 3)),
                     55,
                     55)

                class storageItem19(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 1)),
                     (47 + (63 * 3)),
                     55,
                     55)

                class storageItem20(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     (47 + (63 * 3)),
                     55,
                     55)

                class storageItem21(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     (47 + (63 * 3)),
                     55,
                     55)

                class storageItem22(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     (47 + (63 * 3)),
                     55,
                     55)

                class storageItem23(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     (47 + (63 * 3)),
                     55,
                     55)

                class storageItem24(storageItem0):
                    __module__ = __name__
                    rect = (14,
                     (47 + (63 * 4)),
                     55,
                     55)

                class storageItem25(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 1)),
                     (47 + (63 * 4)),
                     55,
                     55)

                class storageItem26(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     (47 + (63 * 4)),
                     55,
                     55)

                class storageItem27(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     (47 + (63 * 4)),
                     55,
                     55)

                class storageItem28(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     (47 + (63 * 4)),
                     55,
                     55)

                class storageItem29(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     (47 + (63 * 4)),
                     55,
                     55)

                class storageItem30(storageItem0):
                    __module__ = __name__
                    rect = (14,
                     (47 + (63 * 5)),
                     55,
                     55)

                class storageItem31(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 1)),
                     (47 + (63 * 5)),
                     55,
                     55)

                class storageItem32(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     (47 + (63 * 5)),
                     55,
                     55)

                class storageItem33(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     (47 + (63 * 5)),
                     55,
                     55)

                class storageItem34(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     (47 + (63 * 5)),
                     55,
                     55)

                class storageItem35(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     (47 + (63 * 5)),
                     55,
                     55)

                class storageItem36(storageItem0):
                    __module__ = __name__
                    rect = (14,
                     (47 + (63 * 6)),
                     55,
                     55)

                class storageItem37(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 1)),
                     (47 + (63 * 6)),
                     55,
                     55)

                class storageItem38(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     (47 + (63 * 6)),
                     55,
                     55)

                class storageItem39(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     (47 + (63 * 6)),
                     55,
                     55)

                class storageItem40(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     (47 + (63 * 6)),
                     55,
                     55)

                class storageItem41(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     (47 + (63 * 6)),
                     55,
                     55)

                class storageItem42(storageItem0):
                    __module__ = __name__
                    rect = (14,
                     (47 + (63 * 7)),
                     55,
                     55)

                class storageItem43(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 1)),
                     (47 + (63 * 7)),
                     55,
                     55)

                class storageItem44(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 2)),
                     (47 + (63 * 7)),
                     55,
                     55)

                class storageItem45(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 3)),
                     (47 + (63 * 7)),
                     55,
                     55)

                class storageItem46(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 4)),
                     (47 + (63 * 7)),
                     55,
                     55)

                class storageItem47(storageItem0):
                    __module__ = __name__
                    rect = ((14 + (63 * 5)),
                     (47 + (63 * 7)),
                     55,
                     55)



        class recyclerBtn(TButton):
            __module__ = __name__
            rect = (512,
             493,
             63,
             31)
            bkimage = 'object/ui/shop/btn_recycler.img'
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]

            def OnClick(this):
                ui_setCapture('UI.shop.recycler')
                ui_updateRecycler()



        class forgeBtn(TButton):
            __module__ = __name__
            rect = (582,
             493,
             63,
             31)
            bkimage = 'object/ui/shop/btn_forge.img'
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]

            def OnClick(this):
                if (Win_IsVisible(uiRefineDlg) and Win_ShowWidget(uiRefineDlg, 0)):
                    pass
                PlaySound(soundUI, 1)



        class repairDlg(TDlg):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 262) / 2),
             ((600 - 308) / 2),
             262,
             308)
            bkimage = 'object/ui/shop/dlg_repair.img'
            class children:
                __module__ = __name__
                class ID(TLabel):
                    __module__ = __name__
                    visible = 0
                    rect = (0,
                     0,
                     0,
                     0)

                class title(TLabel):
                    __module__ = __name__
                    rect = (37,
                     48,
                     250,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = dt_center

                class text(TLabel):
                    __module__ = __name__
                    rect = (37,
                     80,
                     250,
                     120)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1

                class time(TLabel):
                    __module__ = __name__
                    rect = (100,
                     225,
                     190,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = dt_right

                class price(TLabel):
                    __module__ = __name__
                    rect = (100,
                     269,
                     190,
                     12)
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = dt_right

                class repairBtn(TButton):
                    __module__ = __name__
                    rect = (30,
                     309,
                     63,
                     31)
                    bkimage = 'object/ui/shop/btn_repair.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        Win_ShowWidget('UI.shop.repairDlg', False)
                        PlaySound(soundUI, 1)
                        RepairCommodity(int(Win_GetText('UI.shop.repairDlg.ID')), 2, 3)



                class deleteBtn(TButton):
                    __module__ = __name__
                    rect = (102,
                     309,
                     63,
                     31)
                    bkimage = 'object/ui/shop/btn_collect.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        ui = 'UI.shop.repairDlg'
                        itemID = Win_GetText((ui + '.ID'))
                        itemName = Win_GetText((ui + '.title'))
                        ui = 'UI.shop.deleteItemDlg'
                        Win_SetText((ui + '.itemID'), itemID)
                        Win_SetText((ui + '.text'), ('\xc8\xb7\xca\xb5\xd2\xaa\xb0\xd1"%s"\xb5\xc0\xbe\xdf\xb7\xc5\xc8\xeb\xca\xd5\xb2\xd8\xb9\xf1\xd6\xd0\xc2\xf0?' % itemName))
                        ui_setCapture(ui)
                        PlaySound(soundUI, 1)



                class removeBtn(TButton):
                    __module__ = __name__
                    visible = 0
                    rect = (11,
                     225,
                     69,
                     29)

                    def OnClick(this):
                        global removeItemID
                        ui = 'UI.shop.repairDlg'
                        itemID = Win_GetText((ui + '.ID'))
                        name = Win_GetText((ui + '.title'))
                        removeItemID = int(itemID)
                        Win_ShowWidget('UI.shop.repairDlg', False)
                        PlaySound(soundUI, 1)
                        ui_msgBox(0)
                        Win_ShowMsgBox(('\xc8\xb7\xc8\xcf\xd2\xaa\xc9\xbe\xb3\xfd\xb5\xc0\xbe\xdf"%s"\xc2\xf0?' % name), '\xc9\xbe\xb3\xfd\xb5\xc0\xbe\xdf', 0, 'UI.SysMsgbox', -4)



                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (236,
                     309,
                     43,
                     31)
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
                        Win_ShowWidget('UI.shop.repairDlg', False)
                        PlaySound(soundLeave, 1)





        class deleteItemDlg(TDlg):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            rect = (((800 - 368) / 2),
             ((600 - 198) / 2),
             368,
             326)
            bkimage = 'object/ui/common/dlg_msgBox.img'
            class children:
                __module__ = __name__
                class itemID(TString):
                    __module__ = __name__
                    caption = '-1'

                class text(TLabel):
                    __module__ = __name__
                    rowspace = 2
                    rect = (40,
                     82,
                     280,
                     130)
                    textsize = 12
                    textstyle = (dt_left + dt_top)
                    textEdgeType = -1
                    drawcolor = zoneChooseColor

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
                        ui = 'UI.shop.deleteItemDlg'
                        itemID = int(Win_GetText((ui + '.itemID')))
                        deleteItem(itemID)
                        Win_ShowWidget(ui, 0)
                        Win_ShowWidget('UI.shop.repairDlg', 0)



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
                        ui = 'UI.shop.deleteItemDlg'
                        Win_ShowWidget(ui, 0)
                        PlaySound(soundLeave, 1)





        class recycler(TDlg):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            rect = (((800 - 229) / 2),
             ((600 - 370) / 2),
             229,
             370)
            bkimage = 'object/ui/shop/img_recycler.img'
            class children:
                __module__ = __name__
                class item0(TRadio):
                    __module__ = __name__
                    rect = (30,
                     80,
                     142,
                     22)
                    groupstop = 0
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
                    bkimage = 'object/ui/selSect/btn_choose.img'

                    def OnClick(this):
                        global activeItemInRecycler
                        idx = getTailNum(this)
                        activeItemInRecycler = (disableItemPos + idx)


                    class children:
                        __module__ = __name__
                        class name:
                            __module__ = __name__
                            type = 'LABEL'
                            style = wgtstyle_static
                            rect = (0,
                             0,
                             142,
                             22)
                            drawcolor = zoneChooseColor
                            textEdgeType = -1
                            textstyle = (dt_center + dt_vcenter)



                class item1(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 1)),
                     142,
                     22)
                    groupstop = 1

                class item2(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 2)),
                     142,
                     22)
                    groupstop = 2

                class item3(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 3)),
                     142,
                     22)
                    groupstop = 3

                class item4(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 4)),
                     142,
                     22)
                    groupstop = 4

                class item5(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 5)),
                     142,
                     22)
                    groupstop = 5

                class item6(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 6)),
                     142,
                     22)
                    groupstop = 6

                class item7(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 7)),
                     142,
                     22)
                    groupstop = 7

                class item8(item0):
                    __module__ = __name__
                    rect = (30,
                     (80 + (23 * 8)),
                     142,
                     22)
                    groupstop = 8

                class scroll(TVScroll):
                    __module__ = __name__
                    rect = (178,
                     81,
                     26,
                     200)
                    pos = 0

                    def OnPosChange():
                        global disableItemPos
                        ui = 'UI.shop.recycler'
                        Win_SetRange((ui + '.scroll'), max((disableItemCnt - defRecyclerCnt), 0))
                        pos = Win_GetPos((ui + '.scroll'))
                        if ((pos != disableItemPos) and PlaySound(soundUI, 1)):
                            disableItemPos = pos
                            for i in range(defRecyclerCnt):
                                ui = ('UI.shop.recycler.item%d' % i)
                                idx = (disableItemPos + i)
                                if ((idx >= disableItemCnt) and Win_SetText((ui + '.name'), '')):
                                    Win_EnableWidget(ui, 0)
                                    continue
                                Win_SetCheck(ui, (idx == activeItemInRecycler))



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



                class resumeBtn(TButton):
                    __module__ = __name__
                    rect = (83,
                     323,
                     69,
                     29)
                    bkimage = 'object/ui/shop/btn_resume.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]

                    def OnClick(this):
                        info = Recycler().at(activeItemInRecycler)
                        if ((info != None) and ChangeItemStatus(uin, info.ID, 0)):
                            pass



                class cross(TButton):
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
                        ui = 'UI.shop.recycler'
                        Win_ShowWidget(ui, 0)
                        PlaySound(soundLeave, 1)





        class joinMember(TButton):
            __module__ = __name__
            rect = (509,
             540,
             48,
             50)
            bkimage = 'object/ui/shop/btn_joinMember.img'

            def OnClick(this):
                Navigate(0)



        class leaveBtn(TButton):
            __module__ = __name__
            rect = (733,
             543,
             41,
             41)
            framescheme = [(0,
              0,
              2,
              2,
              3,
              3,
              1,
              1)]
            bkimage = 'object/ui/common/btn_return.img'

            def OnClick(this):
                setNudeState()
                LeaveShop()
                PlaySound(soundLeave, 1)



        class depositQB(TButton):
            __module__ = __name__
            rect = (447,
             540,
             48,
             50)
            bkimage = 'object/ui/shop/btn_depositQB.img'

            def OnClick(this):
                ui_jumpWeb('http://pay.qq.com/zft/paycenter_qb.shtml')



        class taskBtn(TButton):
            __module__ = __name__
            rect = (571,
             540,
             48,
             50)
            bkimage = 'object/ui/task/btn_task.img'
            framescheme = [(0,
              0,
              1,
              1,
              2,
              2,
              -1,
              -1)]

            def OnClick(this):
                if (Win_IsVisible(uiTaskDlg) and Win_ShowWidget(uiTaskDlg, 0)):
                    PlaySound(soundUI, 1)



        class taskDlg(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 300000
            rect = (401,
             12,
             400,
             500)
            bkimage = 'object/ui/task/dlg_task.img'
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
                    rect = (354,
                     35,
                     22,
                     22)
                    bkimage = 'object/ui/common/btn_cross.img'

                    def OnClick(this):
                        Win_ShowWidget(uiTaskDlg, 0)
                        PlaySound(soundUI, 1)



                class taskMark(TStatic):
                    __module__ = __name__
                    initlayer = 2
                    rect = (49,
                     40,
                     37,
                     32)
                    bkImgFlag = dt_center
                    bkimage = 'object/ui/task/bg_taskLevel1.img'

                class taskName(TLabel):
                    __module__ = __name__
                    initlayer = 2
                    rect = (100,
                     52,
                     180,
                     25)
                    drawcolor = (255,
                     255,
                     255,
                     255)
                    textstyle = dt_left
                    textsize = 12
                    caption = ''

                class npcPic(TStatic):
                    __module__ = __name__
                    initlayer = 2
                    bkImgFlag = dt_center
                    rect = (38,
                     75,
                     97,
                     129)
                    bkimage = 'res/uiRes/icon/npcIcon/npcIcon1.img'

                class taskIntroduction(TLabel):
                    __module__ = __name__
                    textstyle = (dt_left + dt_top)
                    initlayer = 2
                    rect = (146,
                     90,
                     215,
                     85)
                    drawcolor = (102,
                     71,
                     39,
                     230)
                    textEdgeType = -1
                    caption = ''

                class deadLine(TLabel):
                    __module__ = __name__
                    textstyle = dt_left
                    initlayer = 2
                    drawcolor = (102,
                     71,
                     39,
                     255)
                    textEdgeType = -1
                    rect = (220,
                     215,
                     180,
                     25)
                    caption = ''

                class progressDes(TLabel):
                    __module__ = __name__
                    textstyle = (dt_left + dt_top)
                    initlayer = 2
                    drawcolor = (102,
                     71,
                     39,
                     255)
                    textEdgeType = -1
                    rect = (70,
                     235,
                     275,
                     50)
                    caption = ''

                class awardPic(TStatic):
                    __module__ = __name__
                    initlayer = 2
                    rect = (73,
                     295,
                     75,
                     75)
                    bkImgFlag = dt_center
                    bkimage = 'res/uiRes/icon/bomb/bomb5.img'

                class awardDes(TLabel):
                    __module__ = __name__
                    textstyle = (dt_left + dt_top)
                    initlayer = 2
                    drawcolor = (229,
                     217,
                     184,
                     255)
                    textEdgeType = -1
                    rect = (160,
                     330,
                     190,
                     40)
                    caption = ''

                class taskBtn0(TCheck):
                    __module__ = __name__
                    initlayer = 2
                    groupstop = 1
                    bkimage = ''
                    rect = (68,
                     387,
                     138,
                     33)
                    class children:
                        __module__ = __name__
                        class taskNameBtn(TButton):
                            __module__ = __name__
                            initlayer = 2
                            rect = (0,
                             0,
                             107,
                             25)
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            bkimage = 'object/ui/task/btn_taskName.img'
                            drawcolor = (102,
                             71,
                             39,
                             230)
                            textEdgeType = -1
                            textstyle = dt_center
                            caption = '\xce\xde\xc8\xce\xce\xf1'

                            def OnClick(this):
                                global currentTaskIdx
                                idx = getMyMidIdx()
                                if (idx != currentTaskIdx):
                                    currentTaskIdx = idx
                                    UpdateCurTaskPanel()



                        class taskCtrBtn(TButton):
                            __module__ = __name__
                            initlayer = 2
                            rect = (108,
                             1,
                             30,
                             30)
                            bkimage = 'object/ui/task/btn_startTask.img'

                            def OnClick(this):
                                global currentTaskIdx
                                idx = getMyMidIdx()
                                print idx,
                                print currentTaskIdx
                                if (idx != currentTaskIdx):
                                    currentTaskIdx = idx
                                    UpdateCurTaskPanel()
                                RequestDoTask(tasksIdList[currentTaskIdx])





                class taskBtn1(taskBtn0):
                    __module__ = __name__
                    rect = ((68 + 145),
                     387,
                     138,
                     33)
                    groupstop = 2

                class taskBtn2(taskBtn0):
                    __module__ = __name__
                    rect = (68,
                     (387 + 35),
                     138,
                     33)
                    groupstop = 3

                class taskBtn3(taskBtn0):
                    __module__ = __name__
                    rect = ((68 + 145),
                     (387 + 35),
                     138,
                     33)
                    groupstop = 4

                class taskBtn4(taskBtn0):
                    __module__ = __name__
                    rect = (68,
                     (387 + (35 * 2)),
                     138,
                     33)
                    groupstop = 5

                class taskBtn5(taskBtn0):
                    __module__ = __name__
                    rect = ((68 + 145),
                     (387 + (35 * 2)),
                     138,
                     33)
                    groupstop = 6



        class fruitMachine(TDlg):
            __module__ = __name__
            initlayer = 200000
            rect = (15,
             (114 + (73 * 4)),
             398,
             170)
            bkimage = 'object/ui/shop/luckyStar/img_luckyStar.img'
            bkimagepos = (-15,
             -52)
            tipwidget = 'UI.shop.fruitMachine.tip'
            class children:
                __module__ = __name__
                class frame(TStatic):
                    __module__ = __name__
                    initlayer = -1000
                    visible = 0
                    rect = (81,
                     56,
                     80,
                     80)
                    bkimage = 'object/ui/shop/luckyStar/frame.img'

                class item1(TStatic):
                    __module__ = __name__
                    rect = (13,
                     63,
                     64,
                     64)
                    bkimage = ''
                    bkImgFlag = dt_center

                class item2(item1):
                    __module__ = __name__
                    rect = (88,
                     63,
                     64,
                     64)
                    bkimage = ''

                class item3(item1):
                    __module__ = __name__
                    rect = (163,
                     63,
                     64,
                     64)
                    bkimage = ''

                class startBtn(TButton):
                    __module__ = __name__
                    initlayer = 300000
                    rect = (309,
                     108,
                     75,
                     65)
                    bkimage = 'object/ui/shop/luckyStar/btn_startLuck.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    tipwidget = 'UI.shop.fruitMachine.tip'

                    def OnClick(this):
                        buyFruitMachine()



                class stopBtn(TButton):
                    __module__ = __name__
                    initlayer = 300000
                    visible = 0
                    rect = (309,
                     108,
                     75,
                     65)
                    bkimage = 'object/ui/shop/luckyStar/btn_stopLuck.img'
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    tipwidget = 'UI.shop.fruitMachine.tip'

                    def OnClick(this):
                        stopFruitMachine()



                class tip(TTip):
                    __module__ = __name__
                    visible = 0
                    initlayer = 200000
                    rect = (-15,
                     182,
                     1,
                     1)
                    bkimage = 'object/ui/shop/luckyStar/tip.img'
                    bkImgFlag = 5

                class lightback(TStatic):
                    __module__ = __name__
                    rect = (7,
                     19,
                     210,
                     125)
                    bkimage = 'object/ui/shop/luckyStar/img_lightback.img'

                class light(TStatic):
                    __module__ = __name__
                    initlayer = 10000
                    framescheme = [(0,
                      6,
                      0,
                      6,
                      0,
                      6,
                      0,
                      6)]
                    visible = 0
                    rect = (7,
                     19,
                     210,
                     125)
                    bkimage = 'object/ui/shop/luckyStar/img_light.img'



        class AD(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 200000
            rect = (6,
             (71 + (73 * 4)),
             398,
             144)
            bkimage = 'object/ui/shop/advert.img'

        class fruitResult(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            rect = (((800 - 363) / 2),
             ((600 - 418) / 2),
             363,
             338)
            bkimage = 'object/ui/shop/dlg_luckResult.img'
            class children:
                __module__ = __name__
                class text(TLabel):
                    __module__ = __name__
                    rect = (54,
                     113,
                     255,
                     100)
                    editable = 0
                    drawcolor = zoneChooseColor
                    textEdgeType = -1
                    textstyle = (dt_center + dt_vcenter)

                class closeBtn(TButton):
                    __module__ = __name__
                    rect = (((363 - 43) / 2),
                     295,
                     43,
                     31)
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
                        Win_ShowWidget('UI.shop.fruitResult', 0)
                        resetFruitMachine()
                        PlaySound(soundLeave, 1)





        class fruitTip(TTip):
            __module__ = __name__
            rect = (55,
             315,
             1,
             1)
            bkimage = 'object/ui/shop/luckyStar/tip_luckyStar.img'

            def OnTimer(this):
                ui = this
                Win_Timer(ui, 0)
                Win_SetValue(ui, 0.050000000000000003, 41)
                Win_SetValue(ui, 2, 901)



        class refineDlg(TStatic):
            __module__ = __name__
            visible = 0
            initlayer = 999999
            rect = (2,
             2,
             427,
             587)
            class children:
                __module__ = __name__
                class crossBtn(TButton):
                    __module__ = __name__
                    initlayer = 21000
                    rect = (400,
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

                    def OnClick(this):
                        Win_ShowWidget(uiRefineDlg, 0)
                        PlaySound(soundLeave, 1)



                class forgeTab(TTabWin):
                    __module__ = __name__
                    initlayer = 21000
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (119,
                     2,
                     93,
                     27)
                    hotcover = 'object/ui/forge/tab_forge.img'
                    groupstop = 0

                    def OnClick(this):
                        Win_ShowWidget(uiAvatarForgeDlg, 1)
                        Win_ShowWidget(uiComposeDlg, 0)
                        PlaySound(soundUI, 1)



                class composeTab(TTabWin):
                    __module__ = __name__
                    initlayer = 21000
                    rect = (0,
                     0,
                     1,
                     1)
                    hotrect = (20,
                     2,
                     93,
                     27)
                    hotcover = 'object/ui/forge/tab_compose.img'
                    groupstop = 1

                    def OnClick(this):
                        Win_ShowWidget(uiAvatarForgeDlg, 0)
                        Win_ShowWidget(uiComposeDlg, 1)
                        PlaySound(soundUI, 1)



                class AvatarForgeDlg(TStatic):
                    __module__ = __name__
                    visible = 1
                    rect = (0,
                     0,
                     427,
                     587)
                    bkimage = 'object/ui/forge/dlg_avatarforge.img'
                    class children:
                        __module__ = __name__
                        class materialDescription:
                            __module__ = __name__
                            type = 'DYLABEL'
                            initlayer = 2000000
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

                        class materialItem0(TButton):
                            __module__ = __name__
                            rect = (18,
                             47,
                             56,
                             56)
                            dragtype = 7
                            bkImgFlag = dt_center
                            tipwidget = (uiAvatarForgeDlg + '.materialDescription')

                            def OnBeginItemDrag():
                                info = g_AvatarForgeMaterial.at((g_AvatarMaterialPage[0] + getMyIdx2()))
                                g_ForgeDragInfo[0] = 2
                                g_ForgeDragInfo[1] = info.m_stItem.m_nItemID
                                g_ForgeDragInfo[2] = ('res/uires/icon/item/item%d.img' % info.m_stItem.m_nItemID)
                                path = Win_GetMyPath()
                                Win_SetDragImg(path, g_ForgeDragInfo[2])



                            def OnMouseMoveIn():
                                me = Win_GetMyPath()
                                itemIdx = (getMyIdx2() + g_AvatarMaterialPage[0])
                                if (itemIdx >= g_AvatarForgeMaterial.getMaterialCnt()):
                                    return 
                                info = g_AvatarForgeMaterial.at(itemIdx)
                                ui = (uiAvatarForgeDlg + '.materialDescription')
                                Win_SetText(ui, ((info.m_szName + '\n') + info.m_szDescrip))
                                winrect = Win_GetRect(me, value_channel_winrect)
                                caprect = Win_GetRect(ui, value_channel_captionrect)
                                Win_Move2Pos(ui, (winrect[0] + 50), (winrect[1] + caprect[3]))



                            def OnDBClick():
                                idx = getMyIdx2()
                                itemIdx = (idx + g_AvatarMaterialPage[0])
                                info = g_AvatarForgeMaterial.at(itemIdx)
                                g_ForgeInfo[0] = info.m_stItem.m_nItemID
                                Win_SetImg((uiAvatarForgeDlg + '.sourceMaterial'), ('res/uires/icon/item/item%d.img' % g_ForgeInfo[0]))


                            class children:
                                __module__ = __name__
                                class itemNum(TLabel):
                                    __module__ = __name__
                                    rect = (30,
                                     40,
                                     24,
                                     12)
                                    drawcolor = zoneChooseColor
                                    textEdgeType = 0
                                    textEdgeColor = maskColor



                        class materialItem1(materialItem0):
                            __module__ = __name__
                            rect = ((18 + 61),
                             47,
                             56,
                             56)

                        class materialItem2(materialItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 2)),
                             47,
                             56,
                             56)

                        class materialItem3(materialItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 3)),
                             47,
                             56,
                             56)

                        class materialItem4(materialItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 4)),
                             47,
                             56,
                             56)

                        class materialPage:
                            __module__ = __name__
                            type = 'NUMLABEL'
                            rect = (320,
                             51,
                             62,
                             18)
                            bkimage = 'object/ui/common/number4.img'
                            textstyle = dt_center
                            textsize = 16
                            textwidth = 16
                            textheight = 18

                        class materialLeft(TButton):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (320,
                             70,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_left.img'

                            def OnClick(this):
                                g_AvatarMaterialPage[0] = max((g_AvatarMaterialPage[0] - g_AvatarMaterialPage[1]), 0)
                                ui_showMaterial()
                                PlaySound(soundUI, 1)



                        class materialRight(TButton):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (354,
                             70,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_right.img'

                            def OnClick(this):
                                if ((g_AvatarMaterialPage[0] + g_AvatarMaterialPage[1]) >= g_AvatarForgeMaterial.getMaterialCnt()):
                                    return 
                                g_AvatarMaterialPage[0] = (g_AvatarMaterialPage[0] + g_AvatarMaterialPage[1])
                                ui_showMaterial()
                                PlaySound(soundUI, 1)



                        class forgeType0(TTabWin):
                            __module__ = __name__
                            rect = (0,
                             0,
                             1,
                             1)
                            hotrect = (15,
                             115,
                             57,
                             30)
                            hotcover = 'object/ui/forge/tab_forgetype0.img'
                            groupstop = 0

                            def OnClick(this):
                                global g_AvatarForgeCurrentType
                                g_AvatarForgeCurrentType = getMyIdx2()
                                ui_showAvatar()
                                PlaySound(soundUI, 1)



                        class forgeType1(forgeType0):
                            __module__ = __name__
                            hotrect = ((15 + 61),
                             115,
                             57,
                             30)
                            hotcover = 'object/ui/forge/tab_forgetype1.img'
                            groupstop = 1

                        class forgeType2(forgeType0):
                            __module__ = __name__
                            hotrect = ((15 + (61 * 2)),
                             115,
                             57,
                             30)
                            hotcover = 'object/ui/forge/tab_forgetype2.img'
                            groupstop = 2

                        class forgeType3(forgeType0):
                            __module__ = __name__
                            hotrect = ((15 + (61 * 3)),
                             115,
                             57,
                             30)
                            hotcover = 'object/ui/forge/tab_forgetype3.img'
                            groupstop = 3

                        class forgeItem0(TButton):
                            __module__ = __name__
                            dragtype = 7
                            rect = (18,
                             150,
                             56,
                             56)
                            bkImgFlag = dt_center

                            def OnClick(this):
                                idx = (getMyIdx2() + g_AvatarForgePage[0][g_AvatarForgeCurrentType])
                                itemID = g_AvatarForge.at(0, g_AvatarForgeCurrentType, idx).m_nItemID
                                useItem(itemID)



                            def OnRClick():
                                idx = (getMyIdx2() + g_AvatarForgePage[0][g_AvatarForgeCurrentType])
                                itemID = g_AvatarForge.at(0, g_AvatarForgeCurrentType, idx).m_nItemID
                                if itemList.has_key(itemID):
                                    name = itemList[itemID][2]
                                    statement = itemList[itemID][3]
                                    leftTime = GetItemLeaveTime(itemID)
                                    ui = 'UI.shop.repairDlg'
                                    if ((leftTime >= 0) and Win_SetText((ui + '.time'), (str(leftTime) + '     \xcc\xec'))):
                                        pass
                                    price = GetRepairPrice(itemID)
                                    Win_SetText((ui + '.price'), (str(price) + '   \xcc\xc7\xb1\xd2'))
                                    Win_SetText((ui + '.title'), name)
                                    Win_SetText((ui + '.text'), statement)
                                    Win_SetText((ui + '.ID'), str(itemID))
                                    ui_setCapture(ui)



                            def OnDBClick():
                                idx = (getMyIdx2() + g_AvatarForgePage[0][g_AvatarForgeCurrentType])
                                itemID = g_AvatarForge.at(0, g_AvatarForgeCurrentType, idx).m_nItemID
                                if itemList.has_key(itemID):
                                    iconType = itemList[itemID][0]
                                    iconIdx = itemList[itemID][1]
                                    picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
                                     iconType,
                                     iconIdx))
                                else:
                                    picName = 'res/uires/shop/salou.img'
                                g_ForgeInfo[1] = itemID
                                Win_SetImg((uiAvatarForgeDlg + '.sourceAvatar'), picName)
                                g_ForgeInfo[3] = -1
                                AvatarForge_wear(0, 0, 0)



                            def OnBeginItemDrag():
                                g_ForgeDragInfo[0] = 0
                                g_ForgeDragInfo[1] = g_AvatarForge.at(0, g_AvatarForgeCurrentType, (g_AvatarForgePage[0][g_AvatarForgeCurrentType] + getMyIdx2())).m_nItemID
                                if itemList.has_key(g_ForgeDragInfo[1]):
                                    iconType = itemList[g_ForgeDragInfo[1]][0]
                                    iconIdx = itemList[g_ForgeDragInfo[1]][1]
                                    picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
                                     iconType,
                                     iconIdx))
                                else:
                                    picName = 'res/uires/shop/salou.img'
                                g_ForgeDragInfo[2] = picName
                                path = Win_GetMyPath()
                                Win_SetDragImg(path, picName)



                        class forgeItem1(forgeItem0):
                            __module__ = __name__
                            rect = ((18 + 61),
                             150,
                             56,
                             56)

                        class forgeItem2(forgeItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 2)),
                             150,
                             56,
                             56)

                        class forgeItem3(forgeItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 3)),
                             150,
                             56,
                             56)

                        class forgeItem4(forgeItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 4)),
                             150,
                             56,
                             56)

                        class forgePage:
                            __module__ = __name__
                            type = 'NUMLABEL'
                            rect = (320,
                             154,
                             62,
                             18)
                            bkimage = 'object/ui/common/number4.img'
                            textstyle = dt_center
                            textsize = 16
                            textwidth = 16
                            textheight = 18

                        class forgeLeft(TButton):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (320,
                             175,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_left.img'

                            def OnClick(this):
                                g_AvatarForgePage[0][g_AvatarForgeCurrentType] = max((g_AvatarForgePage[0][g_AvatarForgeCurrentType] - g_AvatarForgePage[1]), 0)
                                ui_showAvatar()
                                PlaySound(soundUI, 1)



                        class forgeRight(TButton):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (354,
                             175,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_right.img'

                            def OnClick(this):
                                if ((g_AvatarForgePage[0][g_AvatarForgeCurrentType] + g_AvatarForgePage[1]) >= g_AvatarForge.getItemCnt(0, g_AvatarForgeCurrentType)):
                                    return 
                                g_AvatarForgePage[0][g_AvatarForgeCurrentType] = (g_AvatarForgePage[0][g_AvatarForgeCurrentType] + g_AvatarForgePage[1])
                                ui_showAvatar()
                                PlaySound(soundUI, 1)



                        class revertItem0(TButton):
                            __module__ = __name__
                            dragtype = 7
                            rect = (18,
                             220,
                             56,
                             56)
                            bkImgFlag = dt_center

                            def OnClick(this):
                                idx = (getMyIdx2() + g_AvatarRevertPage[0][g_AvatarForgeCurrentType])
                                itemID = g_AvatarForge.at(1, g_AvatarForgeCurrentType, idx).m_nItemID
                                useItem(itemID)



                            def OnRClick():
                                idx = (getMyIdx2() + g_AvatarRevertPage[0][g_AvatarForgeCurrentType])
                                itemID = g_AvatarForge.at(1, g_AvatarForgeCurrentType, idx).m_nItemID
                                if itemList.has_key(itemID):
                                    name = itemList[itemID][2]
                                    statement = itemList[itemID][3]
                                    leftTime = GetItemLeaveTime(itemID)
                                    ui = 'UI.shop.repairDlg'
                                    if ((leftTime >= 0) and Win_SetText((ui + '.time'), (str(leftTime) + '     \xcc\xec'))):
                                        pass
                                    price = GetRepairPrice(itemID)
                                    Win_SetText((ui + '.price'), (str(price) + '   \xcc\xc7\xb1\xd2'))
                                    Win_SetText((ui + '.title'), name)
                                    Win_SetText((ui + '.text'), statement)
                                    Win_SetText((ui + '.ID'), str(itemID))
                                    ui_setCapture(ui)



                            def OnDBClick():
                                idx = (getMyIdx2() + g_AvatarRevertPage[0][g_AvatarForgeCurrentType])
                                itemID = g_AvatarForge.at(1, g_AvatarForgeCurrentType, idx).m_nItemID
                                if itemList.has_key(itemID):
                                    iconType = itemList[itemID][0]
                                    iconIdx = itemList[itemID][1]
                                    picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
                                     iconType,
                                     iconIdx))
                                else:
                                    picName = 'res/uires/shop/salou.img'
                                g_ForgeInfo[1] = itemID
                                Win_SetImg((uiAvatarForgeDlg + '.sourceAvatar'), picName)
                                g_ForgeInfo[3] = -1
                                AvatarForge_wear(0, 0, 0)



                            def OnBeginItemDrag():
                                g_ForgeDragInfo[0] = 0
                                g_ForgeDragInfo[1] = g_AvatarForge.at(1, g_AvatarForgeCurrentType, (g_AvatarRevertPage[0][g_AvatarForgeCurrentType] + getMyIdx2())).m_nItemID
                                if itemList.has_key(g_ForgeDragInfo[1]):
                                    iconType = itemList[g_ForgeDragInfo[1]][0]
                                    iconIdx = itemList[g_ForgeDragInfo[1]][1]
                                    picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
                                     iconType,
                                     iconIdx))
                                else:
                                    picName = 'res/uires/shop/salou.img'
                                g_ForgeDragInfo[2] = picName
                                path = Win_GetMyPath()
                                Win_SetDragImg(path, picName)



                        class revertItem1(revertItem0):
                            __module__ = __name__
                            rect = ((18 + 61),
                             220,
                             56,
                             56)

                        class revertItem2(revertItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 2)),
                             220,
                             56,
                             56)

                        class revertItem3(revertItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 3)),
                             220,
                             56,
                             56)

                        class revertItem4(revertItem0):
                            __module__ = __name__
                            rect = ((18 + (61 * 4)),
                             220,
                             56,
                             56)

                        class revertPage:
                            __module__ = __name__
                            type = 'NUMLABEL'
                            rect = (320,
                             224,
                             62,
                             18)
                            bkimage = 'object/ui/common/number4.img'
                            textstyle = dt_center
                            textsize = 16
                            textwidth = 16
                            textheight = 18

                        class revertLeft(TButton):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (320,
                             244,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_left.img'

                            def OnClick(this):
                                g_AvatarRevertPage[0][g_AvatarForgeCurrentType] = max((g_AvatarRevertPage[0][g_AvatarForgeCurrentType] - g_AvatarRevertPage[1]), 0)
                                ui_showAvatar()
                                PlaySound(soundUI, 1)



                        class revertRight(TButton):
                            __module__ = __name__
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            rect = (354,
                             244,
                             33,
                             35)
                            bkimage = 'object/ui/common/btn_right.img'

                            def OnClick(this):
                                if ((g_AvatarRevertPage[0][g_AvatarForgeCurrentType] + g_AvatarRevertPage[1]) >= g_AvatarForge.getItemCnt(1, g_AvatarForgeCurrentType)):
                                    return 
                                g_AvatarRevertPage[0][g_AvatarForgeCurrentType] = (g_AvatarRevertPage[0][g_AvatarForgeCurrentType] + g_AvatarRevertPage[1])
                                ui_showAvatar()
                                PlaySound(soundUI, 1)



                        class sourceMaterial(TButton):
                            __module__ = __name__
                            dragtype = 7
                            rect = [208,
                             303,
                             62,
                             62]
                            bkImgFlag = dt_center

                            def OnDragItemDrop():
                                if ((g_ForgeDragInfo[0] == 2) and (g_ForgeDragInfo[1] >= 0)):
                                    g_ForgeInfo[0] = g_ForgeDragInfo[1]
                                    path = Win_GetMyPath()
                                    Win_SetImg(path, g_ForgeDragInfo[2])



                        class sourceAvatar(TButton):
                            __module__ = __name__
                            dragtype = 7
                            rect = [208,
                             371,
                             62,
                             62]
                            bkImgFlag = dt_center

                            def OnDragItemDrop():
                                if (((g_ForgeDragInfo[0] == 0) or (g_ForgeDragInfo[0] == 1)) and (g_ForgeDragInfo[1] >= 0)):
                                    g_ForgeInfo[1] = g_ForgeDragInfo[1]
                                    path = Win_GetMyPath()
                                    Win_SetImg(path, g_ForgeDragInfo[2])
                                    AvatarForge_wear(0, 0, 0)



                        class destAvatar(TButton):
                            __module__ = __name__
                            rect = [50,
                             311,
                             100,
                             100]
                            callbackdraw = 'SC_AvatarForge_draw'

                            def OnClick(this):
                                if ((g_ForgeInfo[3] > 0) and useItem(g_ForgeInfo[3])):
                                    pass



                            def OnDBClick():
                                itemID = g_ForgeInfo[3]
                                if ((itemID > 0) and itemList.has_key(itemID)):
                                    iconType = itemList[itemID][0]
                                    iconIdx = itemList[itemID][1]
                                    picName = ('res/uires/icon/%s/%s%d.img' % (iconType,
                                     iconType,
                                     iconIdx))
                                g_ForgeInfo[1] = itemID
                                if Win_SetImg((uiAvatarForgeDlg + '.sourceAvatar'), picName):
                                    pass
                                g_ForgeInfo[3] = -1
                                AvatarForge_wear(0, 0, 0)



                        class forgeBtn(TButton):
                            __module__ = __name__
                            rect = [288,
                             300,
                             103,
                             47]
                            bkimage = 'object/ui/forge/btn_avatarforge.img'
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]

                            def OnClick(this):
                                errorTip = ''
                                if ((g_ForgeInfo[1] <= 0) and (g_ForgeInfo[0] <= 0)):
                                    errorTip = '\xc7\xeb\xd1\xa1\xd4\xf1\xd2\xaa\xb6\xcd\xd4\xec\xb5\xc4\xd7\xb0\xb1\xb8\xba\xcd\xb6\xcd\xd4\xec\xcb\xf9\xd0\xe8\xd2\xaa\xb5\xc4\xb2\xc4\xc1\xcf!'
                                elif (g_ForgeInfo[1] <= 0):
                                    errorTip = '\xc7\xeb\xd1\xa1\xd4\xf1\xd2\xaa\xb6\xcd\xd4\xec\xb5\xc4\xd7\xb0\xb1\xb8!'
                                elif (g_ForgeInfo[0] <= 0):
                                    errorTip = '\xc7\xeb\xd1\xa1\xd4\xf1\xb6\xcd\xd4\xec\xcb\xf9\xd0\xe8\xd2\xaa\xb5\xc4\xb2\xc4\xc1\xcf!'
                                else:
                                    itemInfo = GetItemInfoFromSec(g_ForgeInfo[1])
                                    if ((itemInfo.m_bItemEffect > 0) and (itemInfo.m_bItemColor > 0)):
                                        errorTip = '\xb8\xc3\xd7\xb0\xb1\xb8\xd2\xd1\xb1\xbb\xb6\xcd\xd4\xec,\xc7\xeb\xcf\xc8\xbb\xb9\xd4\xad\xbb\xf2\xb2\xf0\xb7\xd6\xba\xf3\xd4\xd9\xbd\xf8\xd0\xd0\xb6\xcd\xd4\xec!'
                                if ((errorTip != '') and Win_SetColorText((uiAvatarForgeDlg + '.forgeInfo'), errorTip, value_channel_itemtext, 255, 0, 0)):
                                    return 
                                g_ForgeInfo[2] = g_Operator[0]
                                if itemList.has_key(g_ForgeInfo[1]):
                                    itemName = itemList[g_ForgeInfo[1]][2]
                                else:
                                    itemName = '\xb8\xc3\xb5\xc0\xbe\xdf'
                                materialInfo = GetItemInfoInStorage(g_ForgeInfo[0])
                                materialName = materialInfo.m_szName
                                if (len(materialName) == 0):
                                    materialName = '\xb8\xc3\xb2\xc4\xc1\xcf'
                                Win_SetText((uiForgeConfirmDlg + '.forgeText'), ('\xc8\xb7\xc8\xcf\xca\xb9\xd3\xc3 "%s" \xb6\xcd\xd4\xec "%s" \xa3\xa1' % (materialName,
                                 itemName)))
                                ui_setCapture(uiForgeConfirmDlg)
                                PlaySound(soundUI, 1)



                        class splitBtn(TButton):
                            __module__ = __name__
                            rect = [288,
                             347,
                             103,
                             47]
                            bkimage = 'object/ui/forge/btn_avatarsplit.img'
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]

                            def OnClick(this):
                                errorTip = ''
                                if (g_ForgeInfo[1] <= 0):
                                    errorTip = '\xc7\xeb\xd1\xa1\xd4\xf1\xd2\xaa\xb2\xf0\xb7\xd6\xb5\xc4\xd7\xb0\xb1\xb8!'
                                else:
                                    itemInfo = GetItemInfoFromSec(g_ForgeInfo[1])
                                    if (itemInfo.m_bItemEffect <= 0):
                                        errorTip = '\xb8\xc3\xd7\xb0\xb1\xb8\xce\xb4\xb1\xbb\xb6\xcd\xd4\xec,\xcb\xf9\xd2\xd4\xb2\xbb\xc4\xdc\xb2\xf0\xb7\xd6!'
                                    elif (itemInfo.m_bItemColor == 0):
                                        errorTip = '\xb8\xc3\xd7\xb0\xb1\xb8\xd2\xd1\xb1\xbb\xb2\xf0\xb7\xd6!'
                                if ((errorTip != '') and Win_SetColorText((uiAvatarForgeDlg + '.forgeInfo'), errorTip, value_channel_itemtext, 255, 0, 0)):
                                    return 
                                g_ForgeInfo[2] = g_Operator[2]
                                if itemList.has_key(g_ForgeInfo[1]):
                                    itemName = itemList[g_ForgeInfo[1]][2]
                                else:
                                    itemName = '\xb8\xc3\xb5\xc0\xbe\xdf'
                                splitInfo = GetSplitInfo()
                                Win_SetText((uiForgeConfirmDlg + '.forgeText'), ('\xb2\xf0\xb7\xd6 "%s" \xbd\xab\xbb\xa8\xb7\xd1\xc4\xfa %d %s\xa3\xac\xc7\xeb\xb5\xe3\xbb\xf7\xc8\xb7\xc8\xcf\xa3\xa1' % (itemName,
                                 splitInfo[1],
                                 splitInfo[2])))
                                ui_setCapture(uiForgeConfirmDlg)
                                PlaySound(soundUI, 1)



                        class revertBtn(TButton):
                            __module__ = __name__
                            rect = [288,
                             394,
                             103,
                             47]
                            bkimage = 'object/ui/forge/btn_avatarrevert.img'
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]

                            def OnClick(this):
                                errorTip = ''
                                if (g_ForgeInfo[1] <= 0):
                                    errorTip = '\xc7\xeb\xd1\xa1\xd4\xf1\xd2\xaa\xbb\xb9\xd4\xad\xb5\xc4\xd7\xb0\xb1\xb8!'
                                else:
                                    itemInfo = GetItemInfoFromSec(g_ForgeInfo[1])
                                    if (itemInfo.m_bItemEffect <= 0):
                                        errorTip = '\xb8\xc3\xd7\xb0\xb1\xb8\xce\xb4\xb1\xbb\xb6\xcd\xd4\xec,\xcb\xf9\xd2\xd4\xb2\xbb\xc4\xdc\xbb\xb9\xd4\xad!'
                                if ((errorTip != '') and Win_SetColorText((uiAvatarForgeDlg + '.forgeInfo'), errorTip, value_channel_itemtext, 255, 0, 0)):
                                    return 
                                g_ForgeInfo[2] = g_Operator[1]
                                if itemList.has_key(g_ForgeInfo[1]):
                                    itemName = itemList[g_ForgeInfo[1]][2]
                                else:
                                    itemName = '\xb8\xc3\xb5\xc0\xbe\xdf'
                                revertInfo = GetRevertInfo()
                                Win_SetText((uiForgeConfirmDlg + '.forgeText'), ('\xbb\xb9\xd4\xad "%s" \xbd\xab\xbb\xa8\xb7\xd1\xc4\xfa %d %s\xa3\xac\xc7\xeb\xb5\xe3\xbb\xf7\xc8\xb7\xc8\xcf\xa3\xa1' % (itemName,
                                 revertInfo[1],
                                 revertInfo[2])))
                                ui_setCapture(uiForgeConfirmDlg)
                                PlaySound(soundUI, 1)



                        class forgeInfo:
                            __module__ = __name__
                            type = 'TEXTLIST'
                            rect = (20,
                             469,
                             380,
                             90)
                            rowspace = 6
                            textfont = 1
                            textEdgeType = -1
                            scrollspace = 18
                            maxline = 30
                            class children:
                                __module__ = __name__
                                class chatScroll(TVScroll):
                                    __module__ = __name__
                                    extendstyle = 0
                                    rect = (364,
                                     13,
                                     26,
                                     55)
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
                                            rect = (1,
                                             0,
                                             26,
                                             42)
                                            bkimage = 'object/ui/common/scl_block.img'

                                        class spinup(TSpinInc):
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



                                        class spindown(TSpinDec):
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
                                             55,
                                             18,
                                             18)
                                            bkimage = 'object/ui/forge/scl_down.img'

                                            def OnClick(this):
                                                PlaySound(soundUI, 1)









                class forgeConfirmDlg(TDlg):
                    __module__ = __name__
                    visible = 0
                    initlayer = 200000
                    rect = (100,
                     200,
                     225,
                     122)
                    bkimage = 'object/ui/forge/dlg_forgeconfirm.img'
                    class children:
                        __module__ = __name__
                        class forgeText(TLabel,
                         Static):
                            __module__ = __name__
                            rect = (10,
                             10,
                             180,
                             28)
                            textEdgeType = -1
                            drawcolor = (135,
                             113,
                             87,
                             255)

                        class confirmBtn(TButton):
                            __module__ = __name__
                            rect = (70,
                             55,
                             93,
                             50)
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]
                            bkimage = 'object/ui/forge/btn_forgeconfirm.img'

                            def OnClick(this):
                                if ((g_ForgeInfo[2] == g_Operator[0]) and RequestAvatarForge(g_ForgeInfo[1], g_ForgeInfo[0], g_ForgeInfo[2])):
                                    pass
                                Win_ShowWidget(uiForgeConfirmDlg, 0)
                                PlaySound(soundLeave, 1)



                        class crossBtn(TButton):
                            __module__ = __name__
                            rect = (198,
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
                                Win_ShowWidget(uiForgeConfirmDlg, 0)
                                PlaySound(soundLeave, 1)





                class composeDlg(TStatic):
                    __module__ = __name__
                    visible = 0
                    rect = (0,
                     0,
                     427,
                     587)
                    bkimage = 'object/ui/forge/dlg_forge.img'
                    class children:
                        __module__ = __name__
                        class itemList0(TButton):
                            __module__ = __name__
                            rect = (20,
                             70,
                             132,
                             19)
                            bkimage = 'object/ui/forge/btn_type.img'
                            textEdgeColor = (80,
                             80,
                             80,
                             255)
                            teststyle = dt_left

                            def OnClick(this):
                                global composeItemCnt
                                global composeExpand
                                global composeItemID
                                pos = Win_GetPos((uiComposeDlg + '.itemScroll'))
                                idx = (getMyIdx2() + pos)
                                if (idx < composeExpand):
                                    composeExpand = idx
                                    g_ComposeItemList.update()
                                    doUI((uiComposeDlg + '.itemScroll'), 'OnPosChange')
                                elif (idx == composeExpand):
                                    composeExpand = -1
                                    composeItemCnt = 0
                                    doUI((uiComposeDlg + '.itemScroll'), 'OnPosChange')
                                elif ((composeExpand >= 0) and (idx <= (composeExpand + composeItemCnt))):
                                    composeItemID = g_ComposeItemList.at(((idx - composeExpand) - 1)).iPropID
                                    g_ComposeMeterialList.update()
                                    Win_SetImg((uiComposeDlg + '.curItemIcon'), ('res/uires/icon/item/item%d.img' % composeItemID))
                                    Win_SetText((uiComposeDlg + '.curItemName'), g_ComposeItemList.at(((idx - composeExpand) - 1)).szPropName)
                                    Win_SetText((uiComposeDlg + '.curItemInfo'), g_ComposeItemList.at(((idx - composeExpand) - 1)).szPropDescription)
                                    for i in range(defComposeMeterCnt):
                                        materialInfo = g_ComposeMeterialList.at(i)
                                        Win_SetImg((uiComposeDlg + ('.meterialList.meterialIcon%d' % i)), ('res/uires/icon/item/item%d.img' % materialInfo.iMaterialID))
                                        Win_SetText((uiComposeDlg + ('.meterialList.meterialInfo%d' % i)), (materialInfo.szMaterialName + ('\n\n%d/%d' % (materialInfo.unHadMatNum,
                                         materialInfo.unNeedMatlNum))))

                                elif (idx < (composeTypeCnt + composeItemCnt)):
                                    composeExpand = (idx - composeItemCnt)
                                    g_ComposeItemList.update()
                                    doUI((uiComposeDlg + '.itemScroll'), 'OnPosChange')



                        class itemList1(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 1)),
                             132,
                             19)

                        class itemList2(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 2)),
                             132,
                             19)

                        class itemList3(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 3)),
                             132,
                             19)

                        class itemList4(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 4)),
                             132,
                             19)

                        class itemList5(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 5)),
                             132,
                             19)

                        class itemList6(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 6)),
                             132,
                             19)

                        class itemList7(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 7)),
                             132,
                             19)

                        class itemList8(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 8)),
                             132,
                             19)

                        class itemList9(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 9)),
                             132,
                             19)

                        class itemList10(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 10)),
                             132,
                             19)

                        class itemList11(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 11)),
                             132,
                             19)

                        class itemList12(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 12)),
                             132,
                             19)

                        class itemList13(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 13)),
                             132,
                             19)

                        class itemList14(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 14)),
                             132,
                             19)

                        class itemList15(itemList0):
                            __module__ = __name__
                            rect = (20,
                             (70 + (20 * 15)),
                             132,
                             19)

                        class itemScroll(TVScroll):
                            __module__ = __name__
                            rect = (155,
                             82,
                             26,
                             300)
                            pos = 0

                            def OnPosChange():
                                pos = Win_GetPos((uiComposeDlg + '.itemScroll'))
                                sclRange = composeTypeCnt
                                if (composeExpand >= 0):
                                    sclRange += composeItemCnt
                                Win_SetRange((uiComposeDlg + '.itemScroll'), max((sclRange - defComposeCnt), 0))
                                for i in range(defComposeCnt):
                                    idx = (pos + i)
                                    Win_SetDrawColor((uiComposeDlg + ('.itemList%d' % i)), 255, 255, 255, 255)
                                    if ((idx <= composeExpand) and Win_SetImg((uiComposeDlg + ('.itemList%d' % i)), 'object/ui/forge/btn_type.img')):
                                        Win_SetText((uiComposeDlg + ('.itemList%d' % i)), g_ComposeTypeList.at(idx))



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
                                     301,
                                     18,
                                     18)
                                    bkimage = 'object/ui/forge/scl_down.img'

                                    def OnClick(this):
                                        PlaySound(soundUI, 1)





                        class curItemIcon(TStatic):
                            __module__ = __name__
                            rect = (188,
                             84,
                             66,
                             66)
                            bkImgFlag = dt_center

                        class curItemName(TLabel):
                            __module__ = __name__
                            rect = (270,
                             67,
                             120,
                             12)
                            textEdgeType = -1

                        class curItemInfo(TLabel):
                            __module__ = __name__
                            rect = (270,
                             87,
                             120,
                             60)
                            textEdgeType = -1

                        class meterialList(TStatic):
                            __module__ = __name__
                            rect = (189,
                             200,
                             200,
                             212)
                            bkimage = 'object/ui/forge/dlg_meterial.img'
                            class children:
                                __module__ = __name__
                                class meterialIcon0(TStatic):
                                    __module__ = __name__
                                    rect = (0,
                                     -5,
                                     66,
                                     66)
                                    bkImgFlag = dt_center

                                class meterialIcon1(meterialIcon0):
                                    __module__ = __name__
                                    rect = (0,
                                     60,
                                     66,
                                     66)

                                class meterialIcon2(meterialIcon0):
                                    __module__ = __name__
                                    rect = (0,
                                     129,
                                     66,
                                     66)

                                class meterialInfo0(TLabel):
                                    __module__ = __name__
                                    rect = (80,
                                     20,
                                     100,
                                     40)
                                    drawcolor = (255,
                                     255,
                                     255,
                                     255)
                                    textEdgeType = -1
                                    caption = 'abc\n\n123'

                                class meterialInfo1(meterialInfo0):
                                    __module__ = __name__
                                    rect = (80,
                                     90,
                                     100,
                                     40)

                                class meterialInfo2(meterialInfo0):
                                    __module__ = __name__
                                    rect = (80,
                                     160,
                                     100,
                                     40)



                        class composeInfo:
                            __module__ = __name__
                            type = 'TEXTLIST'
                            rect = (20,
                             430,
                             380,
                             90)
                            drawcolor = zoneChooseColor
                            rowspace = 6
                            textfont = 1
                            textEdgeType = -1
                            scrollspace = 18
                            maxline = 30
                            class children:
                                __module__ = __name__
                                class chatScroll(TVScroll):
                                    __module__ = __name__
                                    extendstyle = 0
                                    rect = (366,
                                     13,
                                     26,
                                     55)
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

                                        class spinup(TSpinInc):
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



                                        class spindown(TSpinDec):
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
                                             55,
                                             18,
                                             18)
                                            bkimage = 'object/ui/forge/scl_down.img'

                                            def OnClick(this):
                                                PlaySound(soundUI, 1)







                        class composeBtn(TButton):
                            __module__ = __name__
                            rect = (152,
                             523,
                             102,
                             50)
                            bkimage = 'object/ui/forge/btn_startCompose.img'
                            framescheme = [(0,
                              0,
                              2,
                              2,
                              3,
                              3,
                              1,
                              1)]

                            def OnClick(this):
                                if ((composeItemID <= 0) and Win_SetText((uiComposeDlg + '.forgeInfo'), '\xc7\xeb\xcf\xc8\xd1\xa1\xd4\xf1\xd0\xe8\xd2\xaa\xba\xcf\xb3\xc9\xb5\xc4\xce\xef\xc6\xb7', value_channel_itemtext)):
                                    return 







        class breakEggDlg(TDlg):
            __module__ = __name__
            initlayer = 999999
            visible = 0
            rect = (((800 - 262) / 2),
             ((600 - 408) / 2),
             262,
             308)
            bkimage = 'object/ui/shop/breakEgg/dlg_breakEgg.img'
            darkBG = 1
            class children:
                __module__ = __name__
                class description(TLabel):
                    __module__ = __name__
                    rect = (24,
                     90,
                     302,
                     60)
                    drawcolor = (255,
                     255,
                     0,
                     255)
                    textEdgeType = 0
                    textstyle = (dt_left + dt_top)
                    textsize = 12
                    caption = ''

                class eggPic(TStatic):
                    __module__ = __name__
                    rect = (151,
                     135,
                     83,
                     79)

                class resultPic(TStatic):
                    __module__ = __name__
                    rect = (10,
                     60,
                     200,
                     150)
                    bkimage = ''

                class hammer1(TButton):
                    __module__ = __name__
                    visible = 1
                    rect = (17,
                     230,
                     83,
                     79)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/breakEgg/btn_hammerFrame1.img'
                    tipwidget = 'UI.shop.description'

                    def OnMouseMoveIn():
                        ui = 'UI.shop.description'
                        idx = getMyIdx2()
                        hammerId = 0
                        if (idx == 1):
                            hammerId = 9011
                        elif (idx == 2):
                            hammerId = 9012
                        elif (idx == 3):
                            hammerId = 9013
                        Win_ShowWidget(ui, 1)
                        Win_SetText(ui, itemList[hammerId][3])
                        me = Win_GetMyPath()
                        winrect = Win_GetRect(me, value_channel_winrect)
                        caprect = Win_GetRect(ui, value_channel_captionrect)
                        Win_Move2Pos(ui, (winrect[0] + 70), ((winrect[1] + caprect[3]) - 10))



                    def OnClick(this):
                        idx = getMyIdx2()
                        hammerId = 0
                        if (idx == 1):
                            hammerId = 9011
                        elif (idx == 2):
                            hammerId = 9012
                        elif (idx == 3):
                            hammerId = 9013
                        cnt = GetItemLeaveCount(hammerId)
                        if ((cnt > 0) and RequestBreakEgg(currentEggId, hammerId)):
                            ui = 'UI.shop.breakEggDlg.hammer'
                            Win_EnableWidget((ui + '1'), 0)
                            Win_EnableWidget((ui + '2'), 0)
                            Win_EnableWidget((ui + '3'), 0)


                    class children:
                        __module__ = __name__
                        class hammerPic(TStatic):
                            __module__ = __name__
                            rect = (10,
                             10,
                             83,
                             79)
                            bkimage = ''

                        class hammerCnt(TLabel):
                            __module__ = __name__
                            rect = (50,
                             0,
                             30,
                             16)
                            drawcolor = (255,
                             255,
                             255,
                             255)
                            textstyle = dt_center
                            textsize = 12
                            caption = ''



                class hammer2(hammer1):
                    __module__ = __name__
                    rect = ((17 + 89),
                     230,
                     83,
                     79)
                    bkimage = 'object/ui/shop/breakEgg/btn_hammerFrame2.img'

                class hammer3(hammer1):
                    __module__ = __name__
                    rect = ((17 + (89 * 2)),
                     230,
                     83,
                     79)
                    bkimage = 'object/ui/shop/breakEgg/btn_hammerFrame3.img'

                class title(TStatic):
                    __module__ = __name__
                    rect = (32,
                     10,
                     200,
                     100)
                    framescheme = [(0,
                      99,
                      0,
                      99,
                      0,
                      99,
                      0,
                      99)]
                    bkimage = 'object/ui/shop/breakEgg/title.img'

                class closeBtn(TButton):
                    __module__ = __name__
                    visible = 1
                    rect = (287,
                     255,
                     48,
                     33)
                    framescheme = [(0,
                      0,
                      2,
                      2,
                      3,
                      3,
                      1,
                      1)]
                    bkimage = 'object/ui/shop/breakEgg/btn_close.img'

                    def OnClick(this):
                        currentEggId = 0
                        Win_ShowWidget('UI.shop.breakEggDlg', 0)
                        PlaySound(soundUI, 1)







UI.children.shop = UI_children_shop

#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
