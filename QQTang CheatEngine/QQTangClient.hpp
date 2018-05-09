/************************************************************************/
/*
功能说明:全局类
创建人:Maple
创建日期:2014年9月1日
修改日期:
*/
/************************************************************************/
#pragma  once
#pragma  pack(1)
#include "Maple.hpp"
#define DefineOffset(OFFSETNAME,OFFSETVALUE) \
UINT32 OFFSETNAME = OFFSETVALUE;

#define InitOffset(OFFSETNAME,BASEADDRESS) \
OFFSETNAME = OFFSETNAME + (UINT32)BASEADDRESS;

#define UI_selRoom_chatArea_chatPanel_chatList "UI.selRoom.chatArea.chatPanel.chatList"
#define  UI_room_chatArea_chatPanel_chatList "UI.room.chatArea.chatPanel.chatList"
#define  UI_game_chatList "UI.game.chatList"
#define  UI_shop_refineDlg_AvatarForgeDlg_forgeInfo "UI.shop.refineDlg.AvatarForgeDlg.forgeInfo"
#define  UI_SysMsgbox "UI.SysMsgbox"
#define  UI_shop_refineDlg_composeDlg_composeInfo "UI.shop.refineDlg.composeDlg.composeInfo"

namespace QQTangCheatEngine
{
    class CQQTangClient
    {
    private:
        char szQQTangClientFullPath [ MAX_PATH ];
        char szQQTangClientPath [ MAX_PATH ];
    public:


        DefineOffset ( m_DisPlayAddress , OFFSET_DISPLAYADDRESS )

        DefineOffset ( m_ModuleBase , OFFSET_ADDRESS )

            DefineOffset ( m_MessageLayer , OFFSET_MESSAGELAYER )

            DefineOffset ( m_DataToServer , OFFSET_DATATOSETVER )

            DefineOffset ( m_DataToClient , OFFSET_DATATOCLIENT )

            DefineOffset ( m_GetTimeSub , OFFSET_GETTIMESUB )

            DefineOffset ( m_FindGameItem , OFFSET_FINDGAMEITEM )

            DefineOffset ( m_FindGameBomb , OFFSET_FINDGAMEBOMB )

            DefineOffset ( m_FindSculptureItem , OFFSET_FINDSCULPTUREITEM )

            DefineOffset ( m_GameDispose , OFFSET_GAMEDISPOSE )

            DefineOffset ( m_SendDataToPlayer , OFFSET_SENDDATATOPLAYER )

            DefineOffset ( m_CheckDataToServer , OFFSET_CHECKDATATOSERVER )

            DefineOffset ( m_GameUI , OFFSET_GAMEUI )

            DefineOffset ( m_Room , OFFSET_ROOM )

            DefineOffset ( m_CreateRoom , OFFSET_CREATEROOM )

            DefineOffset ( m_StartGame , OFFSET_STARTGAME )

            DefineOffset ( m_UseObject , OFFSET_USEOBJECT )

            DefineOffset ( m_SelRoomSpeak , OFFSET_SELROOMSPEAK )

            DefineOffset ( m_RoomSpeak , OFFSET_ROOMSPEAK )

            DefineOffset ( m_SetRoomMsg , OFFSET_SETROOMMSG )

            DefineOffset ( m_OperateDoor , OFFSET_OPERATEDOOR )

            DefineOffset ( m_SelMap , OFFSET_SELMAP )

            DefineOffset ( m_SelRoomType , OFFSET_SELROOMTYPE )

            DefineOffset ( m_EnterRoom , OFFSET_ENTERROOM )

            DefineOffset ( m_EnterSelRoom , OFFSET_ENTERSELROOM )

            DefineOffset ( m_MsgBox , OFFSET_MSGBOX )

            DefineOffset ( m_NoticeBoard , OFFSET_NOTICEBOARD )

            DefineOffset ( m_ReleasePet , OFFSET_RELEASEPET )

            DefineOffset ( m_ModifyRoomID , OFFSET_MODIFYROOMID )

            DefineOffset ( m_ModifyPlayModle , OFFSET_MODIFYPLAYMODLE )

            DefineOffset ( m_EnterRandRoom , OFFSET_ENTERRANDROOM )

            DefineOffset ( m_LeaveRoom , OFFSET_LEAVEROOM )

            DefineOffset ( m_LeaveGame , OFFSET_LEAVEGAME )

            DefineOffset ( m_LeaveSelRoom , OFFSET_LEAVESELROOM )

            DefineOffset ( m_QuitGame , OFFSET_QUITGAME )

            DefineOffset ( m_CarryPet , OFFSET_CARRYPET )

            DefineOffset ( m_StopCarryPet , OFFSET_STOPCARRYPET )

            DefineOffset ( m_ModifyColor , OFFSET_MODIFYPLAYERCOLOR )

            DefineOffset ( m_ModifyChatRoomMap , OFFSET_MODIFYCHATROOMMAP )

            CQQTangClient ( )
        {
            //完整路径

            GetModuleFileName ( NULL , szQQTangClientFullPath , MAX_PATH );
            strcpy ( szQQTangClientPath , szQQTangClientFullPath );
            strrchr ( szQQTangClientPath , '\\' ) [ 1 ] = '\0';
            //基址
            HMODULE hModule = GetClientHandle ( );
            //偏移
            InitOffset ( m_ModuleBase , hModule )

                InitOffset ( m_DisPlayAddress , hModule )

                InitOffset ( m_MessageLayer , hModule )

                InitOffset ( m_DataToServer , hModule )

                InitOffset ( m_DataToClient , hModule )

                InitOffset ( m_GetTimeSub , hModule )

                InitOffset ( m_FindGameItem , hModule )

                InitOffset ( m_FindGameBomb , hModule )

                InitOffset ( m_FindSculptureItem , hModule )

                InitOffset ( m_GameDispose , hModule )

                InitOffset ( m_SendDataToPlayer , hModule )

                InitOffset ( m_CheckDataToServer , hModule )

                InitOffset ( m_GameUI , hModule )

                InitOffset ( m_Room , hModule )

                InitOffset ( m_CreateRoom , hModule )

                InitOffset ( m_StartGame , hModule )

                InitOffset ( m_UseObject , hModule )

                InitOffset ( m_SelRoomSpeak , hModule )

                InitOffset ( m_RoomSpeak , hModule )

                InitOffset ( m_SetRoomMsg , hModule )

                InitOffset ( m_OperateDoor , hModule )

                InitOffset ( m_SelMap , hModule )

                InitOffset ( m_SelRoomType , hModule )

                InitOffset ( m_EnterRoom , hModule )

                InitOffset ( m_EnterSelRoom , hModule )

                InitOffset ( m_MsgBox , hModule )

                InitOffset ( m_NoticeBoard , hModule )

                InitOffset ( m_ReleasePet , hModule )

                InitOffset ( m_ModifyRoomID , hModule )

                InitOffset ( m_ModifyPlayModle , hModule )

                InitOffset ( m_EnterRandRoom , hModule )

                InitOffset ( m_LeaveRoom , hModule )

                InitOffset ( m_LeaveGame , hModule )

                InitOffset ( m_LeaveSelRoom , hModule )

                InitOffset ( m_QuitGame , hModule )

                InitOffset ( m_CarryPet , hModule )

                InitOffset ( m_StopCarryPet , hModule )

                InitOffset ( m_ModifyColor , hModule )

                InitOffset ( m_ModifyChatRoomMap , hModule )
        }

        void  CanOpenNext ( )
        {
            if ( szQQTangClientPath [ 0 ] == '\0' )
            {
                return;
            }
            char szFullPath [ MAX_PATH ];
            wsprintf ( szFullPath , "%s%s" , szQQTangClientPath , "update.cfg" );
            char szTimeInfo [ 16 ];
            wsprintf ( szTimeInfo , "%08X" , GetTickCount ( ) );
            if ( 0 == WritePrivateProfileString ( "public" , "app" , szTimeInfo , szFullPath ) )
            {
                return;
            }

            //查找所有的可能是QT的窗口
            while ( TRUE )
            {
                HWND hQQTang = FindWindow ( NULL , "qqtmydir" );
                if ( hQQTang == NULL )
                {
                    break;
                }
                //可能会堵塞
                SendMessage ( hQQTang , WM_SETTEXT , NULL , ( LPARAM ) szTimeInfo );
            }

            return;
        }

        static  void  DebugPrint ( const char* lpszFmt , ... )
        {
            char szOutPutText [ 2048 ];
            va_list args;
            va_start ( args , lpszFmt );
            wvsprintfA ( szOutPutText , ( LPCSTR ) lpszFmt , args );
            OutputDebugStringA ( szOutPutText );
            va_end ( args );
            return;
        }

        static  HMODULE GetClientHandle ( )
        {
            HMODULE hModule;
            _asm
            {
                mov	eax , dword ptr fs : [0x18];
                mov	eax , dword ptr ds : [eax + 0x30];
                mov	eax , dword ptr ds : [eax + 0x8];
                mov hModule , eax;
            }

            return hModule;
        }

        static  PINT8 Algorithm (
            _In_ const PINT8 lpKeyOfEncode ,
            _In_ BOOL IsEncode ,
            _Inout_ PINT8 lpItemOfEncode ,
            _In_ UINT32 ItemSizeof )
        {
            for ( UINT32 i = 0; i < ItemSizeof; i++ )
            {
                if ( IsEncode )
                {
                    lpItemOfEncode [ i ] ^= i;
                }
                lpItemOfEncode [ i ] ^= lpKeyOfEncode [ i % 4 ];
                if ( !IsEncode )
                {
                    lpItemOfEncode [ i ] ^= i;
                }
            }
            return lpItemOfEncode;
        }
    };


    enum MyEnum
    {
        CQQTangClientSize = sizeof ( CQQTangClient ) ,
    };
    CQQTangClient g_QQTangClient;
}