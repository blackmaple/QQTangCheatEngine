#pragma once
#pragma pack(1)
#include "Maple.hpp"
#include "RoomInfo.hpp"
#include "GameUI.hPP"
#include "CCall.hpp"
namespace QQTangCheatEngine
{


    class CQQTangCheatEngine
    {
    private:
        PMessageLayer m_pMessageLayer;
        PGameManager m_pGameManager;
        PRoom m_pRoom;
        CCall m_call;
        PGameUI m_pGameUI;
    public:
        CQQTangCheatEngine ( )
        {
            m_pMessageLayer = CMessageLayer::GetMessageLayer ( );
            m_pRoom = CRoom::GetRoom ( );
            m_pGameManager = m_pMessageLayer->GetGameManager ( );
            m_pGameUI = CGameUI::GetGameUI ( );
        }


        void GetDisPlayAddress ( )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
             for ( int i = 0; i<0xffff; i++ )
            {
                auto p = m_pGameManager->GetGameDispose ( )->GetGameDisplayInfo ( ( GameID ) ( i ) );
                if ( p != nullptr )
                {
                    m_pGameUI->GameDebugPrintf ( "%08X" , p->GetDisplayAddr ( ) );
                }
            }

        }

        void FullScreenBoxExplode ( )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
           
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            PMapBox lpMapBox = lpGameInfo->GetMapBox ( );
            PMap lpMap = lpGameInfo->GetMap ( );


            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );

            vector<CEXPLODEINFO::CBoxExplode>vecBoxExplode;
            vecBoxExplode.reserve ( MaxMapX*MaxMapY );

            for ( INT32 y = 0; y < MaxMapY; y++ )
            {
                for ( INT32 x = 0; x < MaxMapX; x++ )
                {
                    //ǽ��
                    ItemByBox BoxID = lpMapBox->GetBoxID ( x , y );
                    CEXPLODEINFO::CBoxExplode BoxExplode;
                    if ( BoxID != BOX_COMMON_00 )
                    {
                        BoxExplode.m_BoxID = BoxID;
                        BoxExplode.m_BoxX = ( INT8 ) x;
                        BoxExplode.m_BoxY = ( INT8 ) y;
                        vecBoxExplode.push_back ( BoxExplode );
                    }
                    //��ͼ�ϵ�����һ��ǽ�� ����Ұ��Ĳݴ�.WC �� 
                    BoxID = lpMap->GetBoxID ( x , y );
                    if ( BoxID != BOX_COMMON_00 )
                    {
                        BoxExplode.m_BoxID = BoxID;
                        BoxExplode.m_BoxX = ( INT8 ) x;
                        BoxExplode.m_BoxY = ( INT8 ) y;
                        vecBoxExplode.push_back ( BoxExplode );
                    }
                }
            }

            if ( vecBoxExplode.empty ( ) )
            {
                return;
            }

            CEXPLODEINFO ExplodeInfo;
            memset ( &ExplodeInfo , 0 , sizeof ( CEXPLODEINFO ) );
            ExplodeInfo.m_PlayerID = lpGameInfo->GetPlayerInfo ( )->GetArbitrator ( )->GetIDFromServer ( );
            ExplodeInfo.m_GameTime = lpGameInfo->GetGameTime ( );
            CEXPLODEINFO::CBoxExplode* pBoxExplode = ExplodeInfo.m_BoxExplode;
            for ( vector<CEXPLODEINFO::CBoxExplode>::const_iterator it = vecBoxExplode.begin ( ); it != vecBoxExplode.end ( ); it++ )
            {

                memcpy ( pBoxExplode , ( const void* ) ( it._Ptr ) , sizeof ( CEXPLODEINFO::CBoxExplode ) );
                pBoxExplode++;
                ExplodeInfo.m_BoxExplodeSize++;
                if ( ExplodeInfo.m_BoxExplodeSize == 32 )
                {
                    m_pMessageLayer->SetDataToClient ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                    m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                    pBoxExplode = ExplodeInfo.m_BoxExplode;
                    ExplodeInfo.m_BoxExplodeSize = 0;
                }
            }
            if ( ExplodeInfo.m_BoxExplodeSize != 0 )
            {
                m_pMessageLayer->SetDataToClient ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
            }
        }

        void FullScreenBombExplode ( )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }

            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            INT32 GameTime = lpGameInfo->GetGameTime ( );
            INT16 PlayerID = lpGameInfo->GetPlayerInfo ( )->GetArbitrator ( )->GetIDFromServer ( );


            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );
            vector<CEXPLODEINFO::CBombExplode>vecBombExplode ( MaxMapY *MaxMapX );
            vector<CEXPLODEINFO::CBombExplode>::iterator it = vecBombExplode.begin ( );

            for ( INT32 x = 0; x < MaxMapX; x++ )
            {
                for ( INT32 y = 0; y < MaxMapY; y++ )
                {
                    it->m_BombY = ( INT8 ) y;
                    it->m_BombUp = ( INT8 ) y;
                    it->m_BombDown = ( INT8 ) y;
                    it->m_BombX = ( INT8 ) x;
                    it->m_BombLeft = ( INT8 ) x;
                    it->m_BombRigth = ( INT8 ) x;
                    it->m_BombMode = 0x15;
                    it->m_BomberID = PlayerID;
                    it->m_BombTime = GameTime;
                    it++;
                }
            }

            CEXPLODEINFO ExplodeInfo;
            memset ( &ExplodeInfo , 0 , sizeof ( CEXPLODEINFO ) );
            ExplodeInfo.m_PlayerID = PlayerID;
            ExplodeInfo.m_GameTime = GameTime;

            CEXPLODEINFO::CBombExplode* pBombExplode = ExplodeInfo.m_BombExplode;
            for ( vector<CEXPLODEINFO::CBombExplode>::const_iterator it = vecBombExplode.begin ( ); it != vecBombExplode.end ( ); it++ )
            {
                memcpy ( pBombExplode , ( const void * ) ( it._Ptr ) , sizeof ( CEXPLODEINFO::CBombExplode ) );
                pBombExplode++;
                ExplodeInfo.m_BombExplodeSize++;
                if ( ExplodeInfo.m_BombExplodeSize == 32 )
                {
                    m_pMessageLayer->SetDataToClient ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                    m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                    ExplodeInfo.m_BombExplodeSize = 0;
                    pBombExplode = ExplodeInfo.m_BombExplode;
                }
            }
            if ( ExplodeInfo.m_BombExplodeSize != 0 )
            {
                m_pMessageLayer->SetDataToClient ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
            }
        }

        void FullScreenPropExplode ( )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }

            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );

            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );

            vector<CEXPLODEINFO::CPropExplode>vecPropExplode;
            vecPropExplode.reserve ( MaxMapY*MaxMapX );

            for ( INT32 x = 0; x < MaxMapX; x++ )
            {
                for ( INT32 y = 0; y < MaxMapY; y++ )
                {
                    CVector<PGameItem>&vecGameItem = lpGameInfo->GetMapItem ( )->FindGameItem ( y , x );
                    vector<PGameItem>::const_iterator it;
                    for ( it = vecGameItem.GetVecInfo ( )->begin ( ); it != vecGameItem.GetVecInfo ( )->end ( ); it++ )
                    {
                        CEXPLODEINFO::CPropExplode PropExplode;
                        PropExplode.m_PropID = ( *it )->GetItemID ( );
                        PropExplode.m_PropX = ( INT8 ) x;
                        PropExplode.m_PropY = ( INT8 ) y;
                        vecPropExplode.push_back ( PropExplode );
                    }
                }
            }
            if ( vecPropExplode.empty ( ) )
            {
                return;
            }
            CEXPLODEINFO ExplodeInfo;
            memset ( &ExplodeInfo , 0 , sizeof ( CEXPLODEINFO ) );
            ExplodeInfo.m_PlayerID = lpGameInfo->GetPlayerInfo ( )->GetArbitrator ( )->GetIDFromServer ( );
            ExplodeInfo.m_GameTime = lpGameInfo->GetGameTime ( );
            CEXPLODEINFO::CPropExplode* pPropExplode = ExplodeInfo.m_PropExplode;
            vector<CEXPLODEINFO::CPropExplode>::const_iterator it;
            for ( it = vecPropExplode.begin ( ); it != vecPropExplode.end ( ); it++ )
            {
                memcpy ( pPropExplode , ( const void* ) ( it._Ptr ) , sizeof ( CEXPLODEINFO::CPropExplode ) );
                pPropExplode++;
                ExplodeInfo.m_PropExplodeSize++;
                if ( ExplodeInfo.m_PropExplodeSize == 32 )
                {
                    m_pMessageLayer->SetDataToClient ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                    m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                    ExplodeInfo.m_PropExplodeSize = 0;
                    pPropExplode = ExplodeInfo.m_PropExplode;
                }
            }
            if ( ExplodeInfo.m_PropExplodeSize != 0 )
            {
                m_pMessageLayer->SetDataToClient ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_EXPLODEINFO , ExplodeInfo );
            }
        }

        void FullScreenCreateBox ( ItemByBox BoxID )
        {
            //�ж��ڲ�����Ϸ
            if ( m_pGameManager == NULL )
            {
                return;
            }

            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            //��ȡ��������
            PMapBox lpMapBox = lpGameInfo->GetMapBox ( );
            //��ȡ��Ϸ������XY
            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );

            //���������Ϣ�� ��Ԥ��һ���Ĵ�С
            vector<CCREATEBOX::CREATEBOXINFO>vecCreateBoxInfo;
            vecCreateBoxInfo.reserve ( MaxMapX*MaxMapY );

            for ( INT32 x = 0; x < MaxMapX; x++ )
            {
                for ( INT32 y = 0; y < MaxMapY; y++ )
                {
                    //�ж�xy���Ƿ�������
                    if ( BOX_COMMON_00 != lpMapBox->GetBoxID ( x , y ) )
                    {
                        continue;
                    }
                    //�������
                    CCREATEBOX::CREATEBOXINFO CreateBoxInfo;
                    //����x
                    CreateBoxInfo.m_BoxX = ( INT8 ) x;
                    //����y
                    CreateBoxInfo.m_BoxY = ( INT8 ) y;
                    //����id
                    CreateBoxInfo.m_BoxID = ( INT16 ) BoxID;
                    //��������
                    CreateBoxInfo.m_BoxCode = lpGameInfo->GetBoxCode ( )->GetCode ( y , x );
                    //����
                    vecCreateBoxInfo.push_back ( CreateBoxInfo );
                }
            }
            //�ж���û������
            if ( vecCreateBoxInfo.empty ( ) )
            {
                return;
            }
            CCREATEBOX CreateBox;
            //��ʼ��CreateBox
            memset ( &CreateBox , 0 , sizeof ( CCREATEBOX ) );
            CCREATEBOX::CREATEBOXINFO* pCreateBoxInfo = CreateBox.m_CreateBoxInfo;
            //������ݰ�
            for ( vector<CCREATEBOX::CREATEBOXINFO>::const_iterator it = vecCreateBoxInfo.begin ( ); it != vecCreateBoxInfo.end ( ); it++ )
            {
                memcpy ( pCreateBoxInfo , ( const void* ) ( it._Ptr ) , sizeof ( CCREATEBOX::CREATEBOXINFO ) );
                pCreateBoxInfo++;
                CreateBox.m_CreateBoxSize++;
                //ÿ�η���16��
                if ( CreateBox.m_CreateBoxSize == 16 )
                {
                    //���͸����
                    m_pMessageLayer->SetDataToClient ( GameID::P2P_CREATEBOX , CreateBox );
                    //������ʾ
                    m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_CREATEBOX , CreateBox );
                    CreateBox.m_CreateBoxSize = 0;
                    pCreateBoxInfo = CreateBox.m_CreateBoxInfo;
                }
            }
            //ʣ��Ĳ���16����ҲҪ����
            if ( CreateBox.m_CreateBoxSize != 0 )
            {
                m_pMessageLayer->SetDataToClient ( GameID::P2P_CREATEBOX , CreateBox );
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_CREATEBOX , CreateBox );
            }
        }

        void FullScreenGetProp ( )
        {
            //��ʼ��Ϸ����?
            if ( m_pGameManager == NULL )
            {
                return;
            }

            //��ȡ��Ϸ������XY
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );

            //��ŵ�����Ϣ�� ��Ԥ��һ���Ĵ�С
            vector<CNPCGETITEM>vecNPCGetItem;
            vecNPCGetItem.reserve ( MaxMapX*MaxMapY );

            //������ݰ�
            CNPCGETITEM NPCGetItem;
            //��Ϸʱ��
            NPCGetItem.m_GameTime = lpGameInfo->GetGameTime ( );
            //���ID
            NPCGetItem.m_PlayerID = lpGameInfo->GetPlayerInfo ( )->GetMySelf ( )->GetIDFromServer ( );

            //ȫ��ö�ٵ���
            for ( INT32 x = 0; x < MaxMapX; x++ )
            {
                for ( INT32 y = 0; y < MaxMapY; y++ )
                {
                    //Ѱ�ҵ��� ����XY�ϵ����е�����Ϣ
                    CVector<PGameItem>&vecGameItem = lpGameInfo->GetMapItem ( )->FindGameItem ( y , x );

                    //������ǰXY�ϵĵ�����Ϣ
                    for each ( PGameItem obj in *( vecGameItem.GetVecInfo ( ) ) )
                    {
                        //����ID
                        NPCGetItem.m_PropID = obj->GetItemID ( );
                        //�������ڵ�X����ֵ
                        NPCGetItem.m_GeterX = obj->GetItemInPlayerX ( );
                        //�������ڵ�Y����ֵ
                        NPCGetItem.m_GeterY = obj->GetItemInPlayerY ( );

                        if ( NPCGetItem.IsPropToServer ( ) )
                        {
                            //��Щ��������Ҫ֪ͨ������
                            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCGETITEM , &NPCGetItem );
                        }
                        //����
                        vecNPCGetItem.push_back ( NPCGetItem );
                    }
                }
            }

            //�е�����?
            if ( vecNPCGetItem.empty ( ) )
            {
                return;
            }

            for ( vector<CNPCGETITEM>::const_iterator it = vecNPCGetItem.begin ( ); it != vecNPCGetItem.end ( ); it++ )
            {
                //ѭ�����͸������ͻ���
                m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCGETITEM , *it );
                //������ʾ
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCGETITEM , *it );
            }
        }

        void FullScreenGetServerProp ( )
        {
            //��ʼ��Ϸ����?
            if ( m_pGameManager == NULL )
            {
                return;
            }

            //��Ϸ����
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );

            //������ݰ�
            CNPCGETITEM NPCGetItem;
            NPCGetItem.m_PlayerID =
                lpGameInfo->GetPlayerInfo ( )->GetMySelf ( )->GetIDFromServer ( );

            //ö��BOSS
            vector<PBoss>* pvecBoss = lpGameInfo->GetBossList ( );
            for ( vector<PBoss>::const_iterator it = pvecBoss->begin ( );
                it != pvecBoss->end ( ); it++ )
            {
                //BOSS�ڲ���������ŵ��ߵ�vector
                CVector < CItemByDrop >* pvecItem =
                    ( *it )->GetNPCItem ( )->GetvecFirstItemByDrop ( );

                //ö�ٵ�һ��
                for ( vector<CItemByDrop>::iterator item = pvecItem->GetVecInfo ( )->begin ( );
                    item != pvecItem->GetVecInfo ( )->end ( ); item++ )
                {

                    NPCGetItem.m_PropID = item->GetItemID ( );
                    if ( NPCGetItem.IsPropToServer ( ) )
                    {
                        //�Ƿ�������������N�������ĵ��� ��һ���͸�������
                        for ( int i = 0; i < item->GetItemSize ( ); i++ )
                        {
                            m_pMessageLayer->SetDataToServerEx
                                ( GameID::C2S_NPCGETITEM , &NPCGetItem );
                        }
                    }
                }
                //�ڶ���
                pvecItem = ( *it )->GetNPCItem ( )->GetvecNextItemByDrop ( );
                for ( vector<CItemByDrop>::iterator item = pvecItem->GetVecInfo ( )->begin ( );
                    item != pvecItem->GetVecInfo ( )->end ( ); item++ )
                {
                    //ͬ��
                    NPCGetItem.m_PropID = item->GetItemID ( );
                    if ( NPCGetItem.IsPropToServer ( ) )
                    {
                        for ( int i = 0; i < item->GetItemSize ( ); i++ )
                        {
                            m_pMessageLayer->SetDataToServerEx
                                ( GameID::C2S_NPCGETITEM , &NPCGetItem );
                        }
                    }
                }
            }


            //С��(�ɻ�)�ڲ��ĵ���
            vector<ItemByGame>* pvecFlyItem = lpGameInfo->GetFlyItem ( );
            for ( vector<ItemByGame>::iterator item = pvecFlyItem->begin ( );
                item != pvecFlyItem->end ( ); item++ )
            {
                //ͬ��
                NPCGetItem.m_PropID = *item;
                if ( NPCGetItem.IsPropToServer ( ) )
                {
                    m_pMessageLayer->SetDataToServerEx
                        ( GameID::C2S_NPCGETITEM , &NPCGetItem );
                }
            }

            //��ȡ��Ϸ������XY
            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );

            //ȫ��ö�ٵ���
            for ( INT32 x = 0; x < MaxMapX; x++ )
            {
                for ( INT32 y = 0; y < MaxMapY; y++ )
                {
                    //Ѱ�ҵ��� ����XY�ϵ����е�����Ϣ
                    CVector<PGameItem>&vecGameItem =
                        lpGameInfo->GetMapItem ( )->FindGameItem ( y , x );

                    //������ǰXY�ϵĵ����Ƿ���������
                    for each ( PGameItem obj in *( vecGameItem.GetVecInfo ( ) ) )
                    {
                        NPCGetItem.m_PropID = obj->GetItemID ( );
                        //�ж����ǲ��Ƿ���������
                        if ( NPCGetItem.IsPropToServer ( ) )
                        {
                            //����
                            m_pMessageLayer->SetDataToServerEx
                                ( GameID::C2S_NPCGETITEM , &NPCGetItem );
                        }
                    }
                }
            }

        }

        //��һ�ηɻ���û��� �ڶ����͸�����...
        void FullScreenPlaneDropProp ( ItemByGame PropID )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );
            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            vector<CDROPPROPINFO::CDROPPROP>vecDropItem ( MaxMapY*MaxMapX );
            vector<CDROPPROPINFO::CDROPPROP>::iterator it = vecDropItem.begin ( );
            for ( int x = 0; x < MaxMapX; x++ )
            {
                for ( int y = 0; y < MaxMapY; y++ )
                {
                    it->m_PropID = PropID;
                    it->m_PropX = ( INT8 ) x;
                    it->m_PropY = ( INT8 ) y;
                    it++;
                }
            }
            CPLANEDROPITEM PlaneDropItem;
            memset ( &PlaneDropItem , 0 , sizeof ( CPLANEDROPITEM ) );
            PlaneDropItem.m_GameTime = lpGameInfo->GetGameTime ( );
            CDROPPROPINFO::CDROPPROP* lpDropProp = PlaneDropItem.m_DropItemInfo.m_DropProp;
            for ( vector<CDROPPROPINFO::CDROPPROP>::const_iterator it = vecDropItem.begin ( ); it != vecDropItem.end ( ); it++ )
            {
                memcpy ( lpDropProp , ( const void* ) ( it._Ptr ) , sizeof ( CDROPPROPINFO::CDROPPROP ) );
                lpDropProp++;
                PlaneDropItem.m_DropItemInfo.m_DropPropSize++;
                if ( PlaneDropItem.m_DropItemInfo.m_DropPropSize == 0x20 )
                {
                    m_pMessageLayer->SetDataToClient ( GameID::P2P_PLANEDROPITEM , PlaneDropItem );
                    m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_PLANEDROPITEM , PlaneDropItem );
                    lpDropProp = PlaneDropItem.m_DropItemInfo.m_DropProp;
                    PlaneDropItem.m_DropItemInfo.m_DropPropSize = 0;
                }
            }
            if ( 0 != PlaneDropItem.m_DropItemInfo.m_DropPropSize )
            {
                m_pMessageLayer->SetDataToClient ( GameID::P2P_PLANEDROPITEM , PlaneDropItem );
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_PLANEDROPITEM , PlaneDropItem );
            }
        }

        void FullScreenGameDropBomb ( ItemByGame PropID )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );
            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            vector<CDROPPROPINFO::CDROPPROP>vecDropItem ( MaxMapY*MaxMapX );
            vector<CDROPPROPINFO::CDROPPROP>::iterator it = vecDropItem.begin ( );
            for ( INT32 x = 0; x < MaxMapX; x++ )
            {
                for ( INT32 y = 0; y < MaxMapY; y++ )
                {
                    it->m_PropID = PropID;
                    it->m_PropX = ( INT8 ) x;
                    it->m_PropY = ( INT8 ) y;
                    it++;
                }
            }
            CGAMEDROPBOMB GameDropBomb;
            memset ( &GameDropBomb , 0 , sizeof ( CGAMEDROPBOMB ) );
            GameDropBomb.m_GameTime = lpGameInfo->GetGameTime ( );
            GameDropBomb.m_PlayerID = lpGameInfo->GetPlayerInfo ( )->GetArbitrator ( )->GetIDFromServer ( );
            CDROPPROPINFO::CDROPPROP* pDropProp = GameDropBomb.m_DropPropInfo.m_DropProp;
            for ( vector<CDROPPROPINFO::CDROPPROP>::const_iterator it = vecDropItem.begin ( ); it != vecDropItem.end ( ); it++ )
            {
                memcpy ( pDropProp , ( const void* ) ( it._Ptr ) , sizeof ( CDROPPROPINFO::CDROPPROP ) );
                pDropProp++;
                GameDropBomb.m_DropPropInfo.m_DropPropSize++;
                if ( GameDropBomb.m_DropPropInfo.m_DropPropSize == 0x20 )
                {
                    m_pMessageLayer->SetDataToClient ( GameID::P2P_GAMEDROPBOMB , GameDropBomb );
                    m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_GAMEDROPBOMB , GameDropBomb );
                    GameDropBomb.m_DropPropInfo.m_DropPropSize = 0;
                    pDropProp = GameDropBomb.m_DropPropInfo.m_DropProp;
                }
            }
            if ( GameDropBomb.m_DropPropInfo.m_DropPropSize )
            {
                m_pMessageLayer->SetDataToClient ( GameID::P2P_GAMEDROPBOMB , GameDropBomb );
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_GAMEDROPBOMB , GameDropBomb );
            }
        }

        void FullScreenPlayBomb ( NPCINDEX Index )
        {
            //�ж�����Ϸ��
            if ( m_pGameManager == NULL )
            {
                return;
            }

            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            //��ͼ��û������ �Ͳ�ִ��
            if ( 0 == lpGameInfo->GetMapBomb ( )->GetMapBombCount ( ) )
            {
                return;
            }
            //Ҫ�����ĸ����
            PPlyaer lpPlayer = lpGameInfo->AtPlayer ( Index );
            if ( lpPlayer == NULL )
            {
                return;
            }
            //������ݰ�
            CPLAYBOMB PlayBomb;
            //��Ϸʱ��
            PlayBomb.m_GameTime = ( INT16 ) lpGameInfo->GetGameTime ( );
            PlayBomb.m_PlayerFace = lpPlayer->GetPlayerFace ( );
            //���id
            PlayBomb.m_PlayerID = lpPlayer->GetIDFromServer ( );
            //����λ��
            PlayBomb.m_NewYX = CLocation ( lpPlayer->GetPlayerInMapX ( ) , lpPlayer->GetPlayerInMapY ( ) );

            INT32 MaxMapX = lpGameInfo->GetMapItem ( )->GetMaxMapX ( );
            INT32 MaxMapY = lpGameInfo->GetMapItem ( )->GetMaxMapY ( );
            vector<CPLAYBOMB>vecPlayBomb;
            //���������Ϣ�� ��Ԥ��һ���Ĵ�С
            vecPlayBomb.reserve ( MaxMapX*MaxMapY );

            for ( INT32 x = 0; x < MaxMapX; x++ )
            {
                for ( INT32 y = 0; y < MaxMapY; y++ )
                {
                    //����λ�ú�����λ��һ�������ƶ���
                    if ( x == ( INT32 ) PlayBomb.m_NewYX.GetX ( ) && y == ( INT32 ) PlayBomb.m_NewYX.GetY ( ) )
                    {
                        continue;
                    }
                    //��ȡ������Ϣ
                    CVector<PGameBomb>&vecGameBomb = lpGameInfo->GetMapBomb ( )->FindGameBomb ( y , x );
                    vector<PGameBomb>::const_iterator it;
                    //������ݰ�
                    for ( it = vecGameBomb.GetVecInfo ( )->begin ( ); it != vecGameBomb.GetVecInfo ( )->end ( ); it++ )
                    {
                        //����id
                        PlayBomb.m_BomberID = ( *it )->GetBomberID ( );
                        //��Ϸʱ��
                        PlayBomb.m_BombTime = ( *it )->GetGameTime ( );
                        //����
                        PlayBomb.m_BombPower = ( INT8 ) ( *it )->GetBombPower ( );
                        //ԭ��λ��
                        PlayBomb.m_OldYX = *( ( *it )->GetBombXY ( ) );
                        //����
                        vecPlayBomb.push_back ( PlayBomb );
                    }
                }
            }
            //û�����ݾͲ�����
            if ( vecPlayBomb.empty ( ) )
            {
                return;
            }

            for ( vector<CPLAYBOMB>::const_iterator it = vecPlayBomb.begin ( ); it != vecPlayBomb.end ( ); it++ )
            {
                //�������ݰ�
                m_pMessageLayer->SetDataToClient ( GameID::P2P_PLAYBOMB , *it );
                //������ʾ
                m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_PLAYBOMB , *it );
            }
        }

        void BossSkill ( NPCINDEX Index , SkillByBoss skillid , ItemByGame Itemid )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            PPlyaer lpPlayer = lpGameInfo->AtPlayer ( Index );
            if ( lpPlayer == NULL )
            {
                return;
            }
            CBOSSSKILL Skill;
            memset ( &Skill , 0 , sizeof ( CBOSSSKILL ) );
            Skill.m_GameTime = lpGameInfo->GetGameTime ( );
            Skill.m_PlayerID = lpPlayer->GetIDFromServer ( );
            Skill.m_PlayerX = ( INT16 ) lpPlayer->GetNPCX ( );
            Skill.m_PlayerY = ( INT16 ) lpPlayer->GetNPCY ( );
            Skill.m_SkillID = skillid;

            //TODO: �����ߵ�û��Ŷ 
            switch ( skillid )
            {
                case QQTangCheatEngine::SKILL_DROPITEMD:
                case QQTangCheatEngine::SKILL_DROPITEMC:
                case QQTangCheatEngine::SKILL_DROPITEMA:
                case QQTangCheatEngine::SKILL_DROPITEMB:
                    break;
                case QQTangCheatEngine::SKILL_DROPBOMB:
                    break;
            }
            m_pMessageLayer->SetDataToClient ( GameID::P2P_BOSSSKILL , Skill );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_BOSSSKILL , Skill );
        }


        //ֱ��ʤ�� ���䲻��...
        void SuperWinGame ( )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            //INT32 GameTime = lpGameInfo->GetGameTime ( );
            PPlyaer pPlayer = lpGameInfo->GetPlayerInfo ( )->GetMySelf ( );
            switch ( m_pGameManager->GetGameModleInfo ( )->GetGameModle ( ) )
            {
                case QQTangCheatEngine::MODLE_TANK:
                {
                    CTANKROOMEXPLODE TankRoomExplode;
                    var lpGameRoom = lpGameInfo->GetTankRoomA ( );
                    if ( NULL != lpGameRoom )
                    {
                        if ( lpGameRoom->GetRoomColor ( ) == pPlayer->GetPlayerTeamColor ( ) )
                        {
                            lpGameRoom = lpGameInfo->GetTankRoomB ( );
                        }
                        //TankRoomExplode.m_GameTime = GameTime;
                        TankRoomExplode.m_PlayerID = pPlayer->GetIDFromServer ( );
                        TankRoomExplode.m_TankColor = lpGameRoom->GetRoomColor ( );
                        TankRoomExplode.m_TankHP = ( INT16 ) ( -lpGameRoom->GetTaskHp ( ) );
                        m_pMessageLayer->SetDataToServerEx ( GameID::C2S_TANKROOMEXPLODE , &TankRoomExplode );
                    }
                }
                case QQTangCheatEngine::MODLE_COMMON:
                case QQTangCheatEngine::MODLE_BOX:
                case QQTangCheatEngine::MODLE_BOMB:
                case QQTangCheatEngine::MODLE_MACHINE:
                case QQTangCheatEngine::MODLE_PVE:
                {
                    //����ѭ�� BOSS��ʺȻ�������ǹ�
                    for ( vector<PPlyaer>::const_reverse_iterator rit = lpGameInfo->GetPlayerList ( )->rbegin ( );
                        rit != lpGameInfo->GetPlayerList ( )->rend ( ); rit++ )
                    {

                        CNPCDIE npcdie;
                        npcdie.m_PlayerID = ( *rit )->GetIDFromServer ( );
                        //npcdie.m_GameTime = GameTime;
                        m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCDIE , &npcdie );
                    }
                    break;
                }
                case QQTangCheatEngine::MODLE_MATCH:
                {
                    CINJELLY InJelly;
                    //InJelly.m_GameTime = GameTime;
                    InJelly.m_HadAvatar = false;

                    CNPCSAVE npcsave;
                    //npcsave.m_GameTime = GameTime;


                    for ( vector<PPlyaer>::const_iterator it = lpGameInfo->GetPlayerList ( )->begin ( );
                        it != lpGameInfo->GetPlayerList ( )->end ( ); it++ )
                    {
                        if ( ( *it )->GetPlayerTeamColor ( ) != pPlayer->GetPlayerTeamColor ( ) )
                        {
                            INT16 PlayerID = ( *it )->GetIDFromServer ( );
                            // 							InJelly.m_PlayerX = ( INT16 ) ( *it )->GetNPCX ( );
                            // 							InJelly.m_PlayerY = ( INT16 ) ( *it )->GetNPCY ( );
                            InJelly.m_PlayerID = PlayerID;

                            npcsave.m_DeadID = PlayerID;
                            npcsave.m_PlayerID = PlayerID;
                            // 							npcsave.m_SaverX = ( INT16 ) ( *it )->GetNPCX ( );
                            // 							npcsave.m_SaverY = ( INT16 ) ( *it )->GetNPCY ( );
                            for ( int i = 0; i < 100; i++ )
                            {
                                m_pMessageLayer->SetDataToServerEx ( GameID::C2S_INJELLY , &InJelly );
                                // 								m_pMessageLayer->SetDataToClient ( GameID::C2S_INJELLY, InJelly );
                                // 								m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::C2S_INJELLY, InJelly );

                                m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCSAVE , &npcsave );
                                // 								m_pMessageLayer->SetDataToClient ( GameID::C2S_NPCSAVE, npcsave );
                                // 								m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::C2S_NPCSAVE, npcsave );
                            }
                        }
                    }
                    break;
                }
                case QQTangCheatEngine::MODLE_TREASURE:
                {
                    CNPCGETITEM NpcGetItem;
                    // 					NpcGetItem.m_GameTime = GameTime;
                    NpcGetItem.m_PlayerID = pPlayer->GetIDFromServer ( );
                    NpcGetItem.m_PropID = ItemByGame::GAME_LVBAOSHI;
                    for ( int i = 0; i < 44 / 3 + 1; i++ )
                    {
                        m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCGETITEM , &NpcGetItem );
                    }
                    break;
                }
                case QQTangCheatEngine::MODLE_SCULPTURE:
                {
                    var lpGameRoom = lpGameInfo->GetSculptureRoomA ( );
                    if ( lpGameRoom != NULL )
                    {
                        if ( lpGameRoom->GetRoomColor ( ) != pPlayer->GetPlayerTeamColor ( ) )
                        {
                            lpGameRoom = lpGameInfo->GetSculptureRoomB ( );
                        }
                        CGETBUNINROOM GetBunInRoom;
                        GetBunInRoom.m_GameIDType = 0;
                        //						GetBunInRoom.m_GameTime = GameTime;
                        GetBunInRoom.m_PlayerID = pPlayer->GetIDFromServer ( );
                        GetBunInRoom.m_SculptureType = 15;
                        GetBunInRoom.m_PlayerX = lpGameRoom->GetRoomXY ( )->GetPlayerX ( );
                        GetBunInRoom.m_PlayerY = lpGameRoom->GetRoomXY ( )->GetPlayerY ( );
                        for ( INT32 i = 0; i < 4; i++ )
                        {
                            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_GETBUNINROOM , &GetBunInRoom );
                        }
                    }
                    break;
                }
                case QQTangCheatEngine::MODLE_BUN:
                {
                    auto lpGameRoomA = lpGameInfo->GetBunRoomA ( );
                    if ( lpGameRoomA != NULL )
                    {
                        CGETBUNINROOM GetBunInRoom;
                        GetBunInRoom.m_GameIDType = 0;
                        // 						GetBunInRoom.m_GameTime = GameTime;
                        GetBunInRoom.m_PlayerID = pPlayer->GetIDFromServer ( );
                        if ( lpGameRoomA->GetRoomColor ( ) != pPlayer->GetPlayerTeamColor ( ) )
                        {
                            GetBunInRoom.m_BunColor = lpGameRoomA->GetRoomColor ( );
                        }
                        else
                        {
                            GetBunInRoom.m_BunColor = lpGameInfo->GetBunRoomB ( )->GetRoomColor ( );
                        }
                        for ( INT32 i = 0; i < 4; i++ )
                        {
                            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_GETBUNINROOM , &GetBunInRoom );
                        }
                    }
                    break;
                }
                default:
                {
                    break;
                }
            }
        }

        void PlayerInjelly ( NPCINDEX Index )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( Index );
            if ( pPlayer == NULL )
            {
                return;
            }
            CINJELLY InJelly;
            InJelly.m_PlayerID = pPlayer->GetIDFromServer ( );
            InJelly.m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
            InJelly.m_PlayerX = ( INT16 ) ( pPlayer->GetNPCX ( ) );
            InJelly.m_PlayerY = ( INT16 ) ( pPlayer->GetNPCY ( ) );
            InJelly.m_HadAvatar = pPlayer->GetAvatarInfo ( ) != NULL;
            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_INJELLY , &InJelly );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_INJELLY , InJelly );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_INJELLY , InJelly );
        }

        void PlayerKill ( NPCINDEX KillIndex , NPCINDEX DeadIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pKiller = m_pGameManager->GetGameInfo ( )->AtPlayer ( KillIndex );
            if ( pKiller == NULL )
            {
                return;
            }
            PPlyaer pDead = m_pGameManager->GetGameInfo ( )->AtPlayer ( DeadIndex );
            if ( pDead == NULL )
            {
                return;
            }
            CNPCKILL NpcKill;
            NpcKill.m_PlayerID = pKiller->GetIDFromServer ( );
            NpcKill.m_GameTime = pKiller->GetGameInfo ( )->GetGameTime ( );
            NpcKill.m_KillerX = ( INT16 ) pDead->GetNPCX ( );
            NpcKill.m_KillerY = ( INT16 ) pDead->GetNPCY ( );
            NpcKill.m_DaedID = pDead->GetIDFromServer ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCKILL , &NpcKill );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCKILL , NpcKill );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCKILL , NpcKill );
        }

        void PlayerSave ( NPCINDEX SaveIndex , NPCINDEX DeadIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pSaver = m_pGameManager->GetGameInfo ( )->AtPlayer ( SaveIndex );
            if ( pSaver == NULL )
            {
                return;
            }
            PPlyaer pDead = m_pGameManager->GetGameInfo ( )->AtPlayer ( DeadIndex );
            if ( pDead == NULL )
            {
                return;
            }
            CNPCSAVE NpcSave;
            NpcSave.m_PlayerID = pSaver->GetIDFromServer ( );
            NpcSave.m_GameTime = pSaver->GetGameInfo ( )->GetGameTime ( );
            NpcSave.m_DeadID = pDead->GetIDFromServer ( );
            NpcSave.m_SaverX = ( INT16 ) pSaver->GetNPCX ( );
            NpcSave.m_SaverY = ( INT16 ) pSaver->GetNPCY ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCSAVE , &NpcSave );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCSAVE , NpcSave );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCSAVE , NpcSave );
        }

        void PlayerSave ( NPCINDEX SaveIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pSaver = m_pGameManager->GetGameInfo ( )->GetPlayerInfo ( )->GetMySelf ( );
            CNPCSAVE NpcSave;
            NpcSave.m_PlayerID = pSaver->GetIDFromServer ( );
            NpcSave.m_GameTime = pSaver->GetGameInfo ( )->GetGameTime ( );
            NpcSave.m_DeadID = pSaver->GetIDFromServer ( );
            NpcSave.m_SaverX = ( INT16 ) pSaver->GetNPCX ( );
            NpcSave.m_SaverY = ( INT16 ) pSaver->GetNPCY ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCSAVE , &NpcSave );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCSAVE , NpcSave );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCSAVE , NpcSave );
        }

        void PlayerDead ( NPCINDEX DeadIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pDead = m_pGameManager->GetGameInfo ( )->AtPlayer ( DeadIndex );
            if ( pDead == NULL )
            {
                return;
            }
            CNPCDIE NpcDie;
            NpcDie.m_PlayerID = pDead->GetIDFromServer ( );
            NpcDie.m_GameTime = pDead->GetGameInfo ( )->GetGameTime ( );
            NpcDie.m_PlayerY = ( INT16 ) pDead->GetNPCX ( );
            NpcDie.m_PlayerX = ( INT16 ) pDead->GetNPCY ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCDIE , &NpcDie );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCDIE , NpcDie );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCDIE , NpcDie );
        }

        void PlayerRelive ( NPCINDEX ReliverIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            var pReliver = m_pGameManager->GetGameInfo ( )->AtPlayer ( ReliverIndex );
            if ( pReliver == NULL )
            {
                return;
            }
            CNPCRELIVE NpcRelive;
            NpcRelive.m_PlayerID = pReliver->GetIDFromServer ( );
            NpcRelive.m_GameTime = pReliver->GetGameInfo ( )->GetGameTime ( );
            NpcRelive.m_ReliveX = ( INT8 ) pReliver->GetReLiveX ( );
            NpcRelive.m_ReliveY = ( INT8 ) pReliver->GetReLiveY ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::C2S_NPCRELIVE , &NpcRelive );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCRELIVE , NpcRelive );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCRELIVE , NpcRelive );
        }

        void AvatarDisapper ( NPCINDEX PlayerIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( PlayerIndex );
            if ( pPlayer == NULL )
            {
                return;
            }
            CNPCAVATARDISAPPEAR NpcVatar;
            NpcVatar.m_PlayerID = pPlayer->GetIDFromServer ( );
            NpcVatar.m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
            NpcVatar.m_PlayerX = ( INT16 ) pPlayer->GetNPCX ( );
            NpcVatar.m_PlayerY = ( INT16 ) pPlayer->GetNPCY ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::P2P_NPCAVATARDISAPPEAR , &NpcVatar );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCAVATARDISAPPEAR , NpcVatar );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCAVATARDISAPPEAR , NpcVatar );
        }

        void PlayLoseHp ( NPCINDEX PlayerIndex , INT16 IsAdd )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( PlayerIndex );
            if ( pPlayer == NULL )
            {
                return;
            }
            CNPCHPLOSS NpcLoss;
            NpcLoss.m_PlayerID = pPlayer->GetIDFromServer ( );
            NpcLoss.m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
            NpcLoss.m_PlayerX = ( INT16 ) pPlayer->GetNPCX ( );
            NpcLoss.m_PlayerY = ( INT16 ) pPlayer->GetNPCY ( );
            NpcLoss.m_HadAvatar = pPlayer->GetItemInfo ( )->GetAvatar ( );

            NpcLoss.m_Hp = ( INT16 ) -pPlayer->GetNPCItem ( )->GetHP ( )->GetValue ( TRUE );
            NpcLoss.m_Hp *= IsAdd;
            m_pMessageLayer->SetDataToServerEx ( GameID::P2P_NPCHPLOSS , &NpcLoss );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCHPLOSS , NpcLoss );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCHPLOSS , NpcLoss );
        }

        void PlayerLayBomb ( NPCINDEX PlayerIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( PlayerIndex );
            if ( pPlayer == NULL )
            {
                return;
            }
            CLAYOUTBOMB NpcLayBomb;
            NpcLayBomb.m_PlayerID = pPlayer->GetIDFromClinet ( );
            NpcLayBomb.m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
            NpcLayBomb.m_BombY = ( INT8 ) pPlayer->GetPlayerInMapY ( );
            NpcLayBomb.m_BombX = ( INT8 ) pPlayer->GetPlayerInMapX ( );
            NpcLayBomb.m_BombPower = ( INT16 ) pPlayer->GetNPCItem ( )->GetBombPower ( );
            NpcLayBomb.m_IsHide = pPlayer->IsItemUsing ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::P2P_LAYOUTBOMB , &NpcLayBomb );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_LAYOUTBOMB , NpcLayBomb );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_LAYOUTBOMB , NpcLayBomb );

        }

        void PlayerLayoutBomb ( NPCINDEX Index , CLocation& Location )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( Index );
            if ( pPlayer == NULL )
            {
                return;
            }
            CLAYOUTBOMB NpcLayBomb;
            NpcLayBomb.m_PlayerID = pPlayer->GetIDFromClinet ( );
            NpcLayBomb.m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
            NpcLayBomb.m_BombY = ( INT8 ) Location.GetY ( );
            NpcLayBomb.m_BombX = ( INT8 ) Location.GetX ( );
            NpcLayBomb.m_BombPower = ( INT16 ) pPlayer->GetNPCItem ( )->GetBombPower ( );
            NpcLayBomb.m_IsHide = pPlayer->IsItemUsing ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::P2P_LAYOUTBOMB , &NpcLayBomb );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_LAYOUTBOMB , NpcLayBomb );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_LAYOUTBOMB , NpcLayBomb );

        }

        void PlayerCopyBomb ( NPCINDEX pdestIndex , NPCINDEX pscrIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pDestPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( pdestIndex );
            if ( pDestPlayer == NULL )
            {
                return;
            }
            PPlyaer pScrPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( pscrIndex );
            if ( pScrPlayer == NULL )
            {
                return;
            }
            CLAYOUTBOMB NpcCopyBomb;
            NpcCopyBomb.m_PlayerID = pScrPlayer->GetIDFromClinet ( );
            NpcCopyBomb.m_GameTime = pDestPlayer->GetGameInfo ( )->GetGameTime ( );
            NpcCopyBomb.m_BombY = ( INT8 ) pDestPlayer->GetPlayerInMapY ( );
            NpcCopyBomb.m_BombX = ( INT8 ) pDestPlayer->GetPlayerInMapX ( );
            NpcCopyBomb.m_BombPower = ( INT16 ) pDestPlayer->GetNPCItem ( )->GetBombPower ( );
            NpcCopyBomb.m_IsHide = pDestPlayer->IsItemUsing ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::P2P_LAYOUTBOMB , &NpcCopyBomb );
            m_pMessageLayer->SetDataToClient ( GameID::P2P_LAYOUTBOMB , NpcCopyBomb );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_LAYOUTBOMB , NpcCopyBomb );

        }

        void PlayerExpre ( NPCINDEX PlayerIndex , PlayerExpression Expression )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PGameInfo lpGameInfo = m_pGameManager->GetGameInfo ( );
            PPlyaer pDestPlayer = lpGameInfo->AtPlayer ( PlayerIndex );
            if ( pDestPlayer == NULL )
            {
                return;
            }
            CNPCEXPRESSION NpcExpre;
            NpcExpre.m_PlayerID = pDestPlayer->GetIDFromServer ( );
            NpcExpre.m_GameTime = lpGameInfo->GetGameTime ( );
            NpcExpre.m_Expression = Expression;
            m_pMessageLayer->SetDataToClient ( GameID::P2P_NPCEXPRESSION , NpcExpre );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_NPCEXPRESSION , NpcExpre );
        }

        void PlayerQuit ( NPCINDEX PlayerIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pDestPlayer = m_pGameManager->GetGameInfo ( )->AtPlayer ( PlayerIndex );
            if ( pDestPlayer == NULL )
            {
                return;
            }
            CNOTIFYPLAYERQUITGAME NpcQuit;
            NpcQuit.m_PlayerID = pDestPlayer->GetIDFromServer ( );
            m_pMessageLayer->SetDataToClient ( GameID::S2C_NOTIFYPLAYERQUITGAME , NpcQuit );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::S2C_NOTIFYPLAYERQUITGAME , NpcQuit );

        }

        void NotifyGameOver ( )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            //TODO:
            CNOTIFYGAMEOVER GameOver;
            m_pMessageLayer->SetDataToClient ( GameID::S2C_NOTIFYGAMEOVER , GameOver );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::S2C_NOTIFYGAMEOVER , GameOver );
        }

        void NotifyNewAribitration ( NPCINDEX PlayerIndex )
        {
            if ( m_pGameManager == NULL )
            {
                return;
            }
            PPlyaer pPlayer = m_pGameManager->GetGameInfo ( )->GetPlayerList ( )->at ( PlayerIndex );
            CNOTIFYNEWARBITRATION NewArbitration;
            NewArbitration.m_PlayerID = pPlayer->GetIDFromServer ( );
            m_pMessageLayer->SetDataToServerEx ( GameID::S2C_NOTIFYNEWARBITRATION , &NewArbitration );
            m_pMessageLayer->SetDataToClient ( GameID::S2C_NOTIFYNEWARBITRATION , NewArbitration );
            m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::S2C_NOTIFYNEWARBITRATION , NewArbitration );

        }

        void CreateRoom ( )
        {
            m_call.CreateRoom ( );
        }

        void StartGame ( )
        {
            m_call.StartGame ( );
        }

        void UseObject ( ItemByPVE ObjectID , INT32 PetID )
        {
            m_call.UseObject ( ObjectID , PetID );
        }

        void SelRoomSpeak ( INT32 nsize , char *szBuffer )
        {
            m_call.SelRoomSpeak ( nsize , szBuffer );
        }

        void RoomSpeak ( INT32 nsize , char *szBuffer )
        {
            m_call.RoomSpeak ( nsize , szBuffer );
        }

        void SetRoomMsg ( char* szInRoomName , char* szOutRoomName , char* szPassWord )
        {
            m_call.SetRoomMsg ( szInRoomName , szOutRoomName , szPassWord );
        }

        void OperateDoor ( INT32 Index , INT32 nsize )
        {
            m_call.OperateDoor ( Index , nsize );
        }

        void SelMap ( MapID MapId , GameModle nsize )
        {
            m_call.SelMap ( MapId , nsize );
        }

        void SelRoomModal ( RoomType nType )
        {
            m_call.SelRoomModal ( nType );
        }

        void EnterRoom ( INT32 SelSect , INT32 RoomID , char* szPassword )
        {
            m_call.EnterRoom ( SelSect * 400 + RoomID - 1 , szPassword );
        }

        void EnterSelRoom ( PinDao pindao , QuYu quyu , INT32 SelSect )
        {
            m_call.EnterSelRoom ( 0 , pindao , quyu , SelSect );
        }

        void MsgBox ( char* szText , char* szCaption )
        {
            m_call.MsgBox ( szText , szCaption );
        }

        void NoticeBoard ( char* szText , char* szCaption )
        {
            m_call.NoticeBoard ( szText , szCaption );
        }

        void ReleasePet ( INT32 PetID )
        {
            m_call.ReleasePet ( PetID );
        }

        void ModifyRoomID ( INT32 NewRoomID )
        {
            m_call.ModifyRoomID ( NewRoomID );
        }

        void ModifyPlayModle ( INT32 nsize , PlayerModle NewPlayModle )
        {
            m_call.ModifyPlayModle ( nsize , NewPlayModle );
        }

        void EnterRandRoom ( )
        {
            m_call.EnterRandRoom ( );
        }

        void LeaveRoom ( )
        {
            m_call.LeaveRoom ( );
        }

        void LeaveGame ( )
        {
            m_call.LeaveGame ( );
        }

        void LeaveSelRoom ( )
        {
            m_call.LeaveSelRoom ( );
        }

        void QuitGame ( )
        {
            m_call.QuitGame ( );
        }

        void CarryPet ( INT32 PetID )
        {
            m_call.CarryPet ( PetID );
        }

        void ModifyColor ( INT32 nsize , TeamColor color )
        {
            m_call.ModifyColor ( nsize , color );
        }

        void ModifyChatRoomMap ( INT32 MapId )
        {
            m_call.ModifyChatRoomMap ( MapId );
        }

        //TODO:
        // 		void PlayerTransDoor ( NPCINDEX pdestIndex )
        // 		{
        // 			if ( m_pGameManager == NULL )
        // 			{
        // 				return;
        // 			}
        // 			PPlyaer lpPlayer = m_pGameManager->GetGameInfo ( )->GetPlayerList ( )->at ( pdestIndex );
        // 			CTRANSDOOR TRANSDOOR;
        // 			TRANSDOOR.m_GameTime = m_pGameManager->GetGameInfo ( )->GetGameTime ( );
        // 			TRANSDOOR.m_PlayerID = lpPlayer->GetIDFromServer ( );
        // 			TRANSDOOR.m_TranType = 0xa;
        // 			TRANSDOOR.TX = ( INT16 ) lpPlayer->GetNPCX ( );
        // 			TRANSDOOR.TY = ( INT16 ) lpPlayer->GetNPCY ( );
        // 			TRANSDOOR.RY = ( INT16 ) lpPlayer->GetNPCX ( );
        // 			TRANSDOOR.RX = ( INT16 ) lpPlayer->GetNPCY ( );
        // 			m_pMessageLayer->SetDataToClient ( GameID::P2P_TRANSDOOR, TRANSDOOR );
        // 			m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_TRANSDOOR, TRANSDOOR );
        // 
        // 		}
        // 		void PlayerMachineArtillery ()
        // 		{
        // 			if ( m_pGameManager == NULL )
        // 			{
        // 				return;
        // 			}
        // 			CMACHINEARTILLERY MACHINEARTILLERY;
        // 			MACHINEARTILLERY.m_GameTime = m_pGameManager->GetGameInfo ( )->GetGameTime ( );
        // 			MACHINEARTILLERY.m_PlayerID = m_pGameManager->GetGameInfo ( )->GetPlayerInfo ( )->GetArbitrator ( )->GetIDFromServer ( );
        // 			MACHINEARTILLERY.m_BombLength = 0xf;
        // 			MACHINEARTILLERY.m_BombType = 0xe;
        // 			MACHINEARTILLERY.m_BombSize = 0x1;
        // 			MACHINEARTILLERY.m_BombX = ( INT8 ) m_pGameManager->GetGameInfo ( )->GetPlayerInfo ( )->GetArbitrator ( )->GetPlayerInMapX ( );
        // 			MACHINEARTILLERY.m_BombY = ( INT8 ) m_pGameManager->GetGameInfo ( )->GetPlayerInfo ( )->GetArbitrator ( )->GetPlayerInMapY ( );
        // 			m_pMessageLayer->SetDataToClient ( GameID::P2P_MACHINEARTILLERY, MACHINEARTILLERY );
        // 			m_pGameManager->GetGameDispose ( )->GameDispose ( GameID::P2P_MACHINEARTILLERY, MACHINEARTILLERY );
        // 
        // 		}


 
    };
}
