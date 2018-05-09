/************************************************************************/
/* 
功能说明:
创建人:maple
创建日期:2014年9月2日
修改日期:
*/
/************************************************************************/
#pragma once
#pragma pack(1)

#include "GameInfo.hpp"
#define PGameManager CGameManager*
#define PGameDispose CGameDispose*
#define PGameModleInfo CGameModleInfo*
#define PGameDisplayInfo CGameDisplayInfo*

namespace QQTangCheatEngine
{
    class CGameManager;
    class CGameDisplayInfo;
    typedef void ( __thiscall * GameDisplayAddress )( PGameDisplayInfo , GameID , LPVOID );

    class CBaseGameDisplayInfo :public IBaseClass
    {
    private:
        GameDisplayAddress m_DisplayAddress;
    public:
        GameDisplayAddress GetDisplayAddr ( )
        {
            return m_DisplayAddress;
        }
        void SetDisplayAddr ( GameDisplayAddress lpAddress )
        {
            DWORD dwOldProtect = 0;
            VirtualProtect ( &m_DisplayAddress , sizeof ( m_DisplayAddress ) , PAGE_READWRITE , &dwOldProtect );
            m_DisplayAddress = lpAddress;
            VirtualProtect ( &m_DisplayAddress , sizeof ( m_DisplayAddress ) , PAGE_READONLY , &dwOldProtect );
        }
//         __declspec( property( get = GetDisplayAddr , put = SetDisplayAddr ) ) GameDisplayAddress DisplayAddress;
    };

    class CGameDisplayInfo :public CBaseGameDisplayInfo
    {
    private:
        PGameManager m_pGameManager;
    public:
        PGameManager GetGameManager ( )
        {
            return m_pGameManager;
        }
        void HookGameDisplay ( GameID gameid , LPVOID pPacks )
        {

        }
    };



	__interface IHeaderBase
	{
 		void* InitBase ( bool val ) ;
		void UpDateGame ( UINT32 uElapse ) ;
		void EnterGame ( ) ;
		void ShowGameUI ( ) ;
		bool FunA ( INT32 value ) ;
		bool ShowBoss ( ) ;
		bool FunB ( ) ;
	};

	__interface IGameModleInfoBase
	{
 		void* InitBase ( bool Destroy ) ;
		bool InitGame ( LPVOID p, LPVOID gameinfo ) ;
		void InitGame ( ) ;
		bool RetTrue ( ) ;
		bool is ( ) ;
		INT32 GetA ( ) ;
		void GetPlayerDropItem ( CPlayer* pPlayer, CVector<ItemByGame>&vecItem ) ;
		void GetBossDropItem ( CBoss* pBoss, CVector<ItemByGame>&vecItem ) ;
		void Fun ( CPlayer* pPlayer ) ;
		INT32 GetB ( ) ;
		void ret ( ) ;
		INT32 ret6 ( ) ;
		void funA ( ) ;
		INT32 Ret6 ( ) ;
		INT32 Ret0 ( ) ;
		INT32 ret0 ( ) ;
		void  incm_18 ( ) ;
		void funb ( ) ;
		
		void func ( ) ;
		
		void* InitBaseA ( bool Destroy ) ;
		bool InitGameA ( LPVOID p, LPVOID gameinfo ) ;
		void InitGameA ( ) ;
		bool retA ( ) ;
		bool retB ( ) ;
		INT32 retC ( ) ;
		void GetPlayerDropItemA ( CPlayer* pPlayer, CVector<ItemByGame>&vecItem ) ;
		void GetBossDropItemA ( CBoss* pBoss, CVector<ItemByGame>&vecItem ) ;
		void FunA ( CPlayer* pPlayer ) ;
		INT32 retD ( ) ;
		void retE ( ) ;
		INT32 retE6 ( ) ;
		void retF ( ) ;
		INT32 retG6 ( ) ;
		INT32 retE5 ( ) ;
		INT32 retE0 ( ) ;
		void retG ( ) ;
		void retH ( ) ;
		
		void funD ( ) ;
		
		void* InitBaseB ( bool Destroy ) ;
		bool InitGameB ( LPVOID p, LPVOID gameinfo ) ;
		bool InitGameB ( ) ;
		bool retAA ( ) ;
		bool retAB ( ) ;
		BOOL retAC ( ) ;
		void GetPlayerDropItemB ( CPlayer* pPlayer, CVector<ItemByGame>&vecItem ) ;
		void GetBossDropItemB ( CBoss* pBoss, CVector<ItemByGame>&vecItem ) ;
		void FunAA ( INT32 value ) ;
		INT32 GetFunA ( INT32 value ) ;
		void GetFunB ( ) ;
		INT32 GetFUN6 ( ) ;
		void FunAC ( ) ;
		INT32 GetFUNA6 ( ) ;
		INT32 GetFUNA0 ( ) ;
		INT32 GetFUNB0 ( ) ;
		void FunAD ( ) ;
		void FunAE ( ) ;
		
		void FunAF ( ) ;
		//......
	};

	__interface I4F00Base
	{
		void* InitBaseA ( );
		void* InitBaseB ( );
	};

	class CGameManager
	{
		private:

		class CHeader :public IHeaderBase
		{
			private:
			//4
			UINT32 m_uElapse;
			//8
			INT32 m_RunGameEvent;
			//0xC
			INT64 m_GameTime;
			//0x14
			INT32 m_0x14;
			//0x18
			MapID m_GameMapID;
			//0x1C
			UINT8 m_0x1C [ 0xA ];
			//0x26
			UINT8 m_PlayerCount;
			//0x27
			UINT8 m_0x27 [ 0x12E9 ];
			public:
			UINT32 GetElapse ( ) const
			{
				return m_uElapse;
			}
			INT32 GetRunGameEvent ( ) const
			{
				return m_RunGameEvent;
			}
			INT64 GetGameTime ( ) const
			{
				return m_GameTime;
			}

			MapID GetGameMapID ( ) const
			{
				return m_GameMapID;
			}
			UINT8 GetPlayerCount ( ) const
			{
				return m_PlayerCount;
			}

			void* InitBase ( bool val ) {}
			void UpDateGame ( UINT32 uElapse ) {}
			void EnterGame ( ) {}
			void ShowGameUI ( ) {}
			bool FunA ( INT32 value ) {}
			bool ShowBoss ( ) {}
			bool FunB ( ) {}
		}m_Header;

		//0x1310
		CGameInfo m_GameInfo;

		//0x4EA4
		class CGameModleInfo :public IGameModleInfoBase
		{
			private:
			CGameInfo* m_pGameInfo;
			GameModle m_GameModle;
			INT32 m_MaxMapX;
			INT32 m_MaxMapY;
			INT32 m_inc;
			public:
			CGameInfo* GetGameInfo ( )
			{
				return m_pGameInfo;
			}
			GameModle GetGameModle ( )
			{
				return m_GameModle;
			}
			INT32 GetMaxMapX ( )
			{
				return m_MaxMapX;
			}
			INT32 GetMaxMapY ( )
			{
				return m_MaxMapY;
			}

			void* InitBase ( bool Destroy ) { }
			bool InitGame ( LPVOID p, LPVOID gameinfo ) { }
			void InitGame ( ) { }
			bool RetTrue ( ) { }
			bool is ( ) { }
			INT32 GetA ( ) { }
			void GetPlayerDropItem ( CPlayer* pPlayer, CVector<ItemByGame>&vecItem ) { }
			void GetBossDropItem ( CBoss* pBoss, CVector<ItemByGame>&vecItem ) { }
			void Fun ( CPlayer* pPlayer ) { }
			INT32 GetB ( ) { }
			void ret ( ) { }
			INT32 ret6 ( ) { }
			void funA ( ) { }
			INT32 Ret6 ( ) { }
			INT32 Ret0 ( ) { }
			INT32 ret0 ( ) { }
			void  incm_18 ( ) { }
			void funb ( ) { }
			
			void func ( ) { }
			
			void* InitBaseA ( bool Destroy ) { }
			bool InitGameA ( LPVOID p, LPVOID gameinfo ) { }
			void InitGameA ( ) { }
			bool retA ( ) { }
			bool retB ( ) { }
			INT32 retC ( ) { }
			void GetPlayerDropItemA ( CPlayer* pPlayer, CVector<ItemByGame>&vecItem ) { }
			void GetBossDropItemA ( CBoss* pBoss, CVector<ItemByGame>&vecItem ) { }
			void FunA ( CPlayer* pPlayer ) { }
			INT32 retD ( ) { }
			void retE ( ) { }
			INT32 retE6 ( ) { }
			void retF ( ) { }
			INT32 retG6 ( ) { }
			INT32 retE5 ( ) { }
			INT32 retE0 ( ) { }
			void retG ( ) { }
			void retH ( ) { }
			
			void funD ( ) { }
			
			void* InitBaseB ( bool Destroy ) { }
			bool InitGameB ( LPVOID p, LPVOID gameinfo ) { }
			bool InitGameB ( ) { }
			bool retAA ( ) { }
			bool retAB ( ) { }
			BOOL retAC ( ) { }
			void GetPlayerDropItemB ( CPlayer* pPlayer, CVector<ItemByGame>&vecItem ) { }
			void GetBossDropItemB ( CBoss* pBoss, CVector<ItemByGame>&vecItem ) { }
			void FunAA ( INT32 value ) { }
			INT32 GetFunA ( INT32 value ) { }
			void GetFunB ( ) { }
			INT32 GetFUN6 ( ) { }
			void FunAC ( ) { }
			INT32 GetFUNA6 ( ) { }
			INT32 GetFUNA0 ( ) { }
			INT32 GetFUNB0 ( ) { }
			void FunAD ( ) { }
			void FunAE ( ) { }
			
			void FunAF ( ) { }

		}*m_pGameModleInfo;

		//0x4EA8
		class CGameDispose :public IBaseClass
		{
			private:
			INT32 m_4EAC;
			LPVOID m_4EB0;
			INT32 m_4EB4;
			INT32 m_4EB8;
			PGameManager m_pGameManager;

			public:
			void* InitBase ( bool Destroy ) { }

			template<typename T>
			void GameDispose ( GameID gameid, T& Package )
			{
				typedef void ( __thiscall *pGameDispose )
					( PGameDispose ThisClass, GameID gameid, T& Package );
				pGameDispose pDispose = ( pGameDispose ) ( g_QQTangClient.m_GameDispose );
				pDispose ( this, gameid, Package );
			}

            
            PGameDisplayInfo GetGameDisplayInfo ( GameID gameid )
            {
                typedef  PGameDisplayInfo ( __thiscall *pGetGameDisplayInfo )
                    ( PGameDispose ThisClass , GameID gameid );
                pGetGameDisplayInfo pInfo = ( pGetGameDisplayInfo ) ( g_QQTangClient.m_DisPlayAddress );
                return pInfo ( this , gameid );
            }

		}m_GameDispose;

		//0x4EC0
		class C4EC0 :public IBaseClass
		{
			private:
			//0x4EC4
			CHeader* m_Header;
			//0x4EC8
			CVector<LPVOID>m_4EC8;
			//0x4ED8
			CVector<LPVOID>m_4ED8;
			//0x4EE8
			CVector<LPVOID>m_4EE8;

			public:
			void* InitBase ( bool Destroy ) { };

		}m_0x4EC0;

		//0x4EF8
		class C4EF8
		{
			private:
			INT32 m_0x4EF8;
			INT32 m_0x4EFC;
			class C4F00 :public I4F00Base
			{
				private:
				INT32 m_0x4F04;
				INT32 m_0x4F08;
				INT32 m_0x4F0C;
				INT8 m_0x4F10 [ 0x60 ];
				INT32 m_0x4F70;
				INT32 m_0x4F74;
				INT32 m_0x4F78;
				INT32 m_0x4F7C;

				public:
				void* InitBaseA ( ) { }
				void* InitBaseB ( ) { }

			}m_0x4F00;
		}m_0x4EF8;
		
		//0x4F80
		class C4F80 :public IBaseClass
		{
			private:
			C4EF8 m_4F84;
			INT32 m_500C;
			INT32 m_5010;
			INT32 m_5014;
			INT32 m_5018;
			INT32 m_501C;
			INT8 m_5020 [ 0x168 ];
			public:
			void* InitBase ( bool Destroy ) { }
		}m_0x4F80;

		//0x5188
		class C5188 :public IBaseClass
		{
			private:
			CVector<LPVOID>m_518C;
			public:
			void* InitBase ( bool Destroy ) { }
		} m_0x5188;

		//0x519C
		class C519C
		{
			private:
			INT8 m_519C;
			INT8 m_519D;
			INT8 m_519E;
			INT8 m_519F;
			INT8 m_51A0;
			INT8 m_51A1;
			INT8 m_51A2;
			INT8 m_51A3;
			INT32 m_51A4;
			INT32 m_51A8;
		}m_0x519C;

		public:
		CGameInfo* GetGameInfo ( )
		{
			return &m_GameInfo;
		}
		PGameModleInfo GetGameModleInfo ( )
		{
			return m_pGameModleInfo;
		}
		CGameDispose* GetGameDispose ( )
		{
			return &m_GameDispose;
		}
	};
	enum 
	{
		//20908
		CGameManagerSize = sizeof ( CGameManager ),
	};
	static_assert( CGameManagerSize == 20908, "CGameManagerSize is error" );
}