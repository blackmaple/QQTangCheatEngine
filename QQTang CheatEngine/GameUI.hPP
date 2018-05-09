#pragma once
#pragma pack(1)
#include "Maple.hpp"
#include "QQTangClient.hpp"
#define PGameUI CGameUI*
namespace QQTangCheatEngine
{
	__interface IGameUIBase
	{
		void Init ( );
		void  InitGlobal ( int a , int b , int c , int d );
		void  ImportUIScript ( int a , int b , int c , int d );
		void  UnLoad ( );//??
		void  RefurbishGameUI ( float a );
		void  GFX ( );//???
		void  GameEvent ( int a , int b , char* butter );
		void  GameEventEx ( );
		void  CheatUIRoom ( char* pszRoomType );
		void  ShowMouse ( BOOL bShow );
		char*  GetUIRoom ( );
		void  UnKnowA ( int a , int b );
		void  UnKnowB ( int a , int b , int c );
		void  GameSay (
			const char* pszChatType ,
			char* pszChatText , INT32 EventValue ,
			UINT8 Red , UINT8 Green , UINT8 Blue );
		void  GameMsgBox ( char* pszText , char* pszCaption , int Zero , const char* pszMsgbox , int Event );
		void  InitGameUIItem ( char*pszGameUIItem , char* pszItemNumber );
		void  LoadGameUIImg ( char*pszUIName , char* pszImg );
		void  GameUIShow ( char* pszGameUIShow );
		void  ShowPlayerCheat ( int a , int b , int c );
		void  UnKnowC ( int a , int b );
		void  UnLoadEx ( int a );
	};

	class CGameUI :public IGameUIBase
	{
		public:
		static PGameUI GetGameUI ( )
		{
			return( PGameUI ) ( *( PUINT32 ) ( g_QQTangClient.m_GameUI ) );
		}


		void Init ( )
		{ }
		void  InitGlobal ( int a , int b , int c , int d )
		{ }
		void  ImportUIScript ( int a , int b , int c , int d )
		{ }
		void  UnLoad ( )
		{ }//??
		void  RefurbishGameUI ( float a )
		{ }
		void  GFX ( )
		{ }//???
		void  GameEvent ( int a , int b , char* butter )
		{ }
		void  GameEventEx ( )
		{ }
		void  CheatUIRoom ( char* pszRoomType )
		{ }
		void  ShowMouse ( BOOL bShow )
		{ }
        char*  GetUIRoom ( )
        {
            return nullptr;
        }
		void  UnKnowA ( int a , int b )
		{ }
		void  UnKnowB ( int a , int b , int c )
		{ }
		void  GameSay (
			const char* pszChatType ,
			char* pszChatText , INT32 EventValue ,
			UINT8 Red , UINT8 Green , UINT8 Blue )
		{ }
		void  GameMsgBox ( char* pszText , char* pszCaption , int Zero , const char* pszMsgbox , int Event )
		{ }
		void  InitGameUIItem ( char*pszGameUIItem , char* pszItemNumber )
		{ }
		void  LoadGameUIImg ( char*pszUIName , char* pszImg )
		{ }
		void  GameUIShow ( char* pszGameUIShow )
		{ }
		void  ShowPlayerCheat ( int a , int b , int c )
		{ }
		void  UnKnowC ( int a , int b )
		{ }
		void  UnLoadEx ( int a )
		{ }

        //
     public:
         void GameDebugPrintf ( const LPSTR lpszFmt , ... )
        {
            char szOutPutText [ 4096 ];
            va_list args;
            va_start ( args , lpszFmt );
            wvsprintf ( szOutPutText , lpszFmt , args );
            va_end ( args );
            DebugPrintf ( ( const LPSTR ) szOutPutText );
        }
    private:
        void DebugPrintf ( const LPSTR szOutPutText )
        {
            char* pszRoomType = GetUIRoom ( );
            if ( pszRoomType  == nullptr )
            {
                return;
            }
            if ( lstrcmp ( pszRoomType , "selSect" ) == 0 ||
                lstrcmp ( pszRoomType , "shop" ) == 0 ||
                lstrcmp ( pszRoomType , "web" ) == 0 ||
                lstrcmp ( pszRoomType , "login" ) == 0 )
            {
                GameMsgBox (
                    ( char* ) szOutPutText , pszRoomType ,
                    NULL , UI_SysMsgbox , NULL );
                return;
            }
            if ( lstrcmp ( pszRoomType , "selRoom" ) == 0 )
            {
                GameSay ( UI_selRoom_chatArea_chatPanel_chatList , ( char* ) szOutPutText , 0xCF , 0x0 , 0xFF , 0xFF );
                return;
            }
            if ( lstrcmp ( pszRoomType , "room" ) == 0 )
            {
                GameSay ( UI_room_chatArea_chatPanel_chatList , ( char* ) szOutPutText , 0xCF , 0x0 , 0xFF , 0xFF );
                return;
            }
            if ( lstrcmp ( pszRoomType , "game" ) == 0 )
            {
                GameSay ( UI_game_chatList , ( char* ) szOutPutText , 0xCF , 0x0 , 0xFF , 0xFF );
                return;
            }

        }

	};

}


