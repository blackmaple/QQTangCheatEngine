/*********************************************************************** /
/*
功能说明:
创建人:maple
创建日期:2014年9月2日
修改人:
修改日期:
*/
/************************************************************************/
#pragma once
#pragma pack(1)
#include "Maple.hpp"
#include "GameFloor.hpp"
#include "GameBox.hpp"
#include "GameItem.hpp"
#include "GameBomb.hpp"
#include "Player.hpp"
#include "Boss.hpp"
#define PGameInfo CGameInfo*
#define PGameRoom CGameInfo::CGameRoom*
#define PMapItem CMapItem*
#define PMap CMap*
#define PMapBox CMapBox*
#define PMapFloor CMapFloor*
#define PSculptureItem CSculptureItem *
#define PMapBomb CMapBomb*
#define PGamePVE CGamePVE*
#define PBombExplode CBombExplode*
#define PBoxCode CGameInfo::CBoxCode*
#define PPlayBomb CPlayBomb*

namespace QQTangCheatEngine
{
	template<typename T, typename U>
	class CMapElemBase
	{
		protected:
		//0
		CEncodeMember m_MaxMapX;
		//0x14
		CEncodeMember m_MaxMapY;
		//28
		CMapY<T>* m_pID;
		//2C
		CMapY<U>* m_pInfo;
		//30
		PGameInfo m_pGameInfo;
		//34
		INT32 m_0x34;
		//38
		LPVOID m_0x38;
		//3c
		LPVOID m_0x3C;
		//40
		LPVOID m_0x40;
		//44 
		INT32 m_BeginID;
		public:
		virtual void* InitBase ( bool Destroy ) = 0;

		//0
		CEncodeMember* GetMaxMapX()
		{
			return &m_MaxMapX;
		}
		//0x14
		CEncodeMember GetMaxMapY()
		{
			return &m_MaxMapY;
		}
		//28
		CMapY<T> GetID()
		{
			return m_pID;
		}
		//2C
		CMapY<U> GetInfo()
		{
			return m_pInfo;
		}
		//30
		PGameInfo GetpGameInfo()
		{
			return m_pGameInfo;
		}
	};

	class CMap :public CMapElemBase < ItemByBox, PGameBox >
	{
		public:
		void*  InitBase ( bool Destroy ) { }

		ItemByBox GetBoxID ( short x, short y )
		{
			CMapX< ItemByBox >* pCX = m_pID [ y ].m_MapX;
			return pCX [ x ].m_ID;
		}
		PGameBox GetBoxInfo ( short x, short y )
		{
			CMapX<PGameBox>* pCX = m_pInfo [ y ].m_MapX;
			return pCX [ x ].m_pInfo;
		}

		PEncodeMember  GetMaxMapX ( )
		{
			return &this->m_MaxMapX;
		}
		PEncodeMember  GetMaxMapY ( )
		{
			return &this->m_MaxMapY;
		}
		PGameInfo GetGameInfo ( )
		{
			return m_pGameInfo;
		}


	};

	class CMapBox :public CMapElemBase < ItemByBox, PGameBox >
	{

		public:
		void* InitBase ( bool Destroy ) { }
		ItemByBox GetBoxID ( short x, short y )
		{
			CMapX< ItemByBox >* pCX = m_pID [ y ].m_MapX;
			return pCX [ x ].m_ID;
		}
		PGameBox GetBoxInfo ( short x, short y )
		{
			CMapX<PGameBox>* pCX = m_pInfo [ y ].m_MapX;
			return pCX [ x ].m_pInfo;
		}
		PEncodeMember  GetMaxMapX ( )
		{
			return &this->m_MaxMapX;
		}
		PEncodeMember  GetMaxMapY ( )
		{
			return &this->m_MaxMapY;
		}
		PGameInfo  GetGameInfo ( )
		{
			return m_pGameInfo;
		}

	};

	class CMapFloor : public CMapElemBase < ItemByFloor, PGameFloor >
	{

		public:
		void*  InitBase ( bool Destroy ) { }
		ItemByFloor  GetFloorID ( short x, short y )
		{
			CMapX< ItemByFloor >* pCX = m_pID [ y ].m_MapX;
			return pCX [ x ].m_ID;
		}
		PGameFloor  GetFloorInfo ( short x, short y )
		{
			CMapX<PGameFloor>* pCX = m_pInfo [ y ].m_MapX;
			return pCX [ x ].m_pInfo;
		}
		PEncodeMember  GetMaxMapX ( )
		{
			return &this->m_MaxMapX;
		}
		PEncodeMember  GetMaxMapY ( )
		{
			return &this->m_MaxMapY;
		}
		PGameInfo GetGameInfo ( )
		{
			return m_pGameInfo;
		}

	};

	class CGameInfo
	{
		private:
		//1310
		UINT8 m_0x1310 [ 0xE1C ];
		//212C
		CVector<PVOID>m_0x212C;
		//213C
		CMap m_Map;
		//2188
		CMapBox m_MapBox;
		//21D4
		CMapFloor m_MapFloor;

		//2220
		class CMapItem :public IBaseClass
		{
			private:
			INT32 m_0x2224;
			//不Get
			LPVOID m_GameItemInfo;
			INT32 m_0x222C;
			INT32 m_0x2230;
			INT32 m_MaxMapX;
			INT32 m_MaxMapY;
			INT32 m_0x223C;
			INT32 m_0x2240;
			INT32 m_0x2244;
			INT32 m_0x2248;
			CGameInfo* m_GameInfo;
			public:
			void* InitBase ( bool Destroy ) { }
			CGameInfo* GetGameInfo ( )
			{
				return m_GameInfo;
			}
			INT32 GetMaxMapX ( )
			{
				return m_MaxMapX;
			}
			INT32 GetMaxMapY ( )
			{
				return m_MaxMapY;
			}
			CVector<PGameItem>& FindGameItem ( short y, short x )
			{
				typedef CVector<CGameItem*>&( __thiscall *pFindGameItem )
					( PMapItem ThisClass, short y, short x );
				pFindGameItem pFind = ( pFindGameItem ) ( g_QQTangClient.m_FindGameItem );
				return pFind ( this, y, x );
			}
		}m_MapItem;

		//2250
		class CMapBomb :public IBaseClass
		{
			private:
			INT32 m_0x2254;
			LPVOID m_0x2258;
			INT32 m_0x225C;
			INT32 m_MapBombCountInc;
			INT32 m_0x2264;
			LPVOID m_0x2268;
			INT32 m_0x226C;
			INT32 m_MapBombCount;
			INT32 m_0x2274;
			LPVOID m_0x2278;
			INT32 m_0x227C;
			INT32 m_0x2280;
			INT32 m_0x2284;
			LPVOID m_0x2288;
			INT32 m_0x228C;
			INT32 m_BombCount;
			PGameInfo m_pGameInfo;
			//BAE
			INT32 m_BeginId;

			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( ) const
			{
				return m_pGameInfo;
			}
			CVector<PGameBomb>& FindGameBomb ( short y, short x )
			{
				typedef CVector<CGameBomb *>&( __thiscall *pFindGameBomb )
					( CMapBomb* ThisCall, short y, short x );
				pFindGameBomb pFind = ( pFindGameBomb ) ( g_QQTangClient.m_FindGameBomb );
				return pFind ( this, y, x );
			}
			INT32 GetMapBombCountInc ( ) const
			{
				return m_MapBombCountInc;
			}
			INT32 GetMapBombCount ( ) const
			{
				return m_MapBombCount;
			}
			INT32 GetBombCount ( ) const
			{
				return m_BombCount;
			}

		}m_MapBomb;

		//229C
		class CBombExplode :public IBaseClass
		{
			private:
			INT32 m_0x22A0;
			LPVOID m_0x22A4;
			INT32 m_0x22A8;
			INT32 m_0x22AC;
			INT32 m_MaxMapX;
			INT32 m_MaxMapY;
			INT32 m_0x22B8;
			INT32 m_0x22BC;
			INT32 m_0x22C0;
			INT32 m_0x22c4;
			PGameInfo m_pGameInfo;

			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( )
			{
				return m_pGameInfo;
			}
			INT32 GetMaxMapX ( )const
			{
				return m_MaxMapX;
			}
			INT32 GetMaxMapY ( )const
			{
				return m_MaxMapY;
			}
		}m_BombExplode;

		//22CC
		class CBoxCode :public IBaseClass
		{
			private:
			INT32 m_0x22D0;
			INT32 m_0x22D4;
			INT32 m_0x22D8;
			INT32 m_0x22DC;
			INT32 m_0x22E0;
			INT32 m_0x22E4;
			INT32 m_0x22E8;
			INT32 m_0x22EC;
			PGameInfo m_pGameInfo;
			INT32 m_Code [ 15 * 13 ];
			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( )
			{
				return m_pGameInfo;
			}
			INT32 GetCode(volatile INT32 y, volatile INT32 x)
			{
				INT32 BoxCode = 1;
				if ( ( y >= 0 && y <= 12 ) && ( x >= 0 && x <= 14 ) )
				{
					INT32 Index = ( y << 4 ) - y + x;
					BoxCode += ( m_Code [ Index ] >> 8 );
				}
				BoxCode <<= 4;
				BoxCode += y;
				BoxCode <<= 4;
				BoxCode += x;
				return BoxCode;
			}
		}m_BoxCode;

		//2600
		//基类墙壁....
		class CGameRoom :public IBaseClass
		{
			private:
			ItemByBox m_RoomType;
			CLocation m_RoomXY;
			INT32 m_RoomStatus;
			UINT32 m_0x10;
			UINT32 m_0x14;
			UINT32 m_0x18;
			UINT32 m_0x1C;
			UINT32 m_0x20;
			UINT32 m_0x24;
			UINT32 m_0x28;
			UINT32 m_0x2c;
			UINT32 m_0x30;
			UINT8 m_0x34;
			UINT8 m_0x35 [ 3 ];
			UINT8 m_RoomID;
			UINT8 m_RoomColor;
			UINT8 m_0x3A [ 2 ];
			INT32 m_TaskHp;
			UINT8 m_0x40 [ 0x20 ];
			UINT32 m_0x60;
			UINT32 m_0x64;
			UINT32 m_0x68;
			UINT32 m_0x6C;
			UINT32 m_0x70;
			public:
			void* InitBase ( bool Destroy ) { }
			ItemByBox GetRoomType ( ) //0x4 =2ee8
			{
				return m_RoomType;
			}
			CLocation* GetRoomXY ( )
			{
				return &m_RoomXY;
			}
			INT32 GetRoomStatus ( ) const//0xc
			{
				return m_RoomStatus;
			}
			UINT8 GetRoomID ( ) const//0x38
			{
				return m_RoomID;
			}
			UINT8 GetRoomColor ( ) const//0x39
			{
				return m_RoomColor;
			}
			INT32 GetTaskHp ( ) const//0x3c
			{
				return m_TaskHp;
			}
		}*m_pBunRoomA, *m_pBunRoomB, *m_pSculptureRoomA,
			*m_pSculptureRoomB, *m_pTankRoomA, *m_pTankRoomB;

		//2618
		class CSculptureItem :public IBaseClass
		{

			private:
			INT32 m_0x261C;
			LPVOID m_0x2620;
			INT32 m_0x2624;
			INT32 m_0x2628;
			INT32 m_MaxMapX;
			INT32 m_MaxMapY;
			PGameInfo m_pGameInfo;
			INT32 m_0x2638;
			INT32 m_0x263C;
			INT32 m_0x2640;
			INT32 m_0x2644;

			public:
			void* InitBase ( bool Destroy ) { }
			CVector<PGameItem>& FindSculptureItem ( short y, short x )
			{
				typedef CVector<CGameItem*>&( __thiscall *pFindSculptureItem )
					( PSculptureItem ThisClass, short y, short x );

				pFindSculptureItem pFind = ( pFindSculptureItem ) ( g_QQTangClient.m_FindSculptureItem );
				return pFind ( this, y, x );
			}
			PGameInfo GetGameInfo ( )
			{
				return m_pGameInfo;
			}
			INT32 GetMaxMapX ( )
			{
				return m_MaxMapX;
			}
			INT32 GetMaxMapY ( )
			{
				return m_MaxMapY;
			}

		}m_SculptureItem;

		//2648
		CVector<CPlayer*> m_PlayerList;
		//2658
		CVector<CBoss*> m_BossList;

		//2668
		class CPlayBomb :public IBaseClass
		{
			private:
			PGameInfo m_pCGameInfo;
			INT32 m_PlayTime;
			UINT8 m_0x2674 [ 0x1C40 ];
			UINT8 m_0x42B4 [ 192 ];
			INT32 m_0x4374;
			INT32 m_0x4378;
			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( )
			{
				return m_pCGameInfo;
			}
			INT32 GetPlayTime ( )
			{
				return m_PlayTime;
			}

		}m_PlayBomb;

		//437C
		class C437C :public IBaseClass
		{
			private:
			PGameInfo m_pGameInfo;
			INT32 m_0x4384;
			INT8 m_0x4388 [ 0x46 ];
			INT16 m_0x43CE;
			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( )
			{
				return m_pGameInfo;
			}
		}m_0x437C;

		//43D0
		class C43D0 :public IBaseClass
		{
			private:
			PGameInfo m_pGameInfo;
			INT32 m_0x43D8;
			INT32 m_0x43DC;
			INT32 m_MaxMapX;
			INT32 m_MaxMapY;
			INT32 m_0x43E8;
			INT32 m_0x43EC;
			INT32 m_MaxMapXEx;
			INT32 m_MaxMapYEx;
			CVector<LPVOID> m_vec0x43F8;
			CVector<LPVOID> m_vec0x4408;
			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( )
			{
				return m_pGameInfo;
			}
			INT32 GetMaxMapX ( )const
			{
				return m_MaxMapX;
			}
			INT32 GetMaxMapY ( )const
			{
				return m_MaxMapY;
			}
		}m_0x43D0;

		//4418
		class C4418 :public IBaseClass
		{
			private:
			INT32 m_0x441C;
			INT32 m_0x4420;
			INT32 m_0x4424;
			INT32 m_0x4428;
			PGameInfo m_pGameInfo;
			INT32 m_0x4430;
			CVector<LPVOID>m_vec0x4434;
			INT8 m_0x4444 [ 0x200 ];
			INT32 m_0x4644;
			CVector<ItemByGame>m_vecFlyItem;
			INT8 m_0x4658 [ 0x184 ];
			//47DC
			INT32 m_FlyItemTime;
			INT32 m_0x47E0;
			INT32 m_0x47E4;
			INT8 m_0x47E8 [ 0x318 ];
			INT32 m_0x4B00;
			INT32 m_0x4B04;
			INT32 m_0x4B08;
			UINT8 m_MachineSkill;
			INT8 m_0x4B0D [ 3 ];

			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( )const
			{
				return m_pGameInfo;
			}
			vector<ItemByGame>* GetFlyItem ( )
			{
				return m_vecFlyItem.GetVecInfo ( );
			}
			INT32 GetFlyTime ( )const
			{
				return m_FlyItemTime;
			}
			UINT8 GetMachineSkill ( ) const
			{
				return m_MachineSkill;
			}
		} m_0x4418;

		//4B10
		class CReLive
		{
			private:
			CVector<CLocation> m_ReLiveXY;
			CVector<CLocation> m_XY;
			public:
			vector<CLocation>* GetReLiveXY ( )
			{
				return m_ReLiveXY.GetVecInfo();
			}
			vector<CLocation>* GetXY ( )
			{
				return m_XY.GetVecInfo ( );
			}

		}m_ReLive;

		//4B30
		class CPlayerInfo
		{
			private:
			//4B30
			INT16 m_MySelfID;
			INT16 m_0x4B32;
			//4B34
			CPlayer* m_pMySelf;
			//4B38
			CPlayer* m_pCurrentPlayer;
			//4B3C
			INT16 m_FirstPlayerID;
			INT16 m_0x4B3E;
			//4B40
			CPlayer* m_pArbitrator;
			//4B44
			INT32 m_PlayerCount;
			//4B48
			INT32 m_GameTime;
			INT32 m_0x4B4C;
			INT32 m_0x4B50;
			INT32 m_0x4B54;
			public:
			INT16 GetMySelfID ( )
			{
				return m_MySelfID;
			}
			CPlayer* GetMySelf ( )
			{
				return m_pMySelf;
			}
			CPlayer* GetArbitrator ( )
			{
				return m_pArbitrator;
			}
			INT32 GetPlayerCount ()const
			{
				return m_PlayerCount;
			}
			INT32 GetGameTime ( ) const
			{
				return m_GameTime;
			}
		}m_PlayerInfo;

		//4B58
		class C4B58 :public IBaseClass
		{
			private:
			PGameInfo m_pGameInfo;
			INT32 m_0x4B60 [ 0x10 ];
			vector<LPVOID>m_0x4BA0;
			INT32 m_0x4BAC [ 7 + 7 ];
			INT32 m_0x4BE4;
			INT32 m_0x4BE8 [ 7 + 7 ];
			INT8 m_0x4C20;
			INT8 m_0x4C21 [ 3 ];
			INT32 m_0x4C24;
			INT8 m_0x4C28;
			INT8 m_0x4C29 [ 3 ];
			float m_0x4C2C;
			public:
			void* InitBase ( bool Destroy ) { }
			PGameInfo GetGameInfo ( )const
			{
				return m_pGameInfo;
			}
		}m_0x4B58;

		//4C30
		class C4C30
		{
			private:
			CVector<LPVOID>m_vec0x4C30;
			CVector<LPVOID>m_vec0x4C40;
			INT8 m_0x4C50 [ 0x1C ];
			CVector<CLocation>m_vec4C6C;
			INT16 m_PlayerCount;
			// (eq 0x4E21)
			INT16 m_0x4C7E;
			INT32 m_4C80;
			INT8 m_4C84 [ 0x18B ];
		}m_0x4C30;

		//4E0F
		class C4E0F
		{
			private:
			INT8 m_0x4E0F;
			INT8 m_0x4E10;
			INT8 m_0x4E11;
			INT16 m_0x4E12;

			INT32 m_0x4E14;
			INT32 m_0x4E18;
			INT32 m_0x4E1C;

			INT32 m_0x4E20;
			INT32 m_0x4E24;
			INT32 m_0x4E28;
			INT32 m_0x4E2C;

			INT8 m_0x4E30 [ 0x44 ];
			INT32 m_0x4E74;
			INT32 m_0x4E78;
			INT32 m_0x4E7C;

			//eq 258
			INT32 m_0x4E80;
			//eq 208
			INT32 m_0x4E84;
			INT32 m_0x4E88;
			INT32 m_0x4E8C;

			//4e90
			class CGamePVE :public IBaseClass
			{
				private:
				//4
				BOOL m_CanNextMap;
				//8 c 10 14
				CVector<INT32> m_vecLockArea;
				//18 地图信息
				LPVOID m_pMapInfo;
				//1c
				CGameInfo* m_pGameInfo;
				//20
				INT32 m_LookMinX;
				INT32 m_LookMinY;
				INT32 m_LookMaxX;
				INT32 m_LookMaxY;
				INT32 m_LookSizeMinX;
				INT32 m_LookSizeMinY;
				INT32 m_LookSizeMaxX;
				INT32 m_LookSizeMaxY;
				CVector<CPVEBossInfo> m_vecBossInfo;
				INT32 m_50;
				INT32 m_54;
				INT32 m_58;
				INT32 m_5C;

				INT32 m_60;
				INT32 m_64;
				INT32 m_68;
				INT32 m_6C;

				INT32 m_70;
				INT32 m_74;
				INT32 m_78;
				INT32 m_7C;

				INT32 m_80;
				INT32 m_84;
				INT32 m_ContinueID;
				INT32 m_MapIndex;
				INT32 m_90;
				CVector<LPVOID> m_vecInfoC;
				INT32 m_A4;
				public:

				//4
				BOOL GetCanNextMap ( )
				{
					return m_CanNextMap;
				}
				//8 c 10 14
				CVector<INT32>* GetvecLockArea ( )
				{
					return &m_vecLockArea;
				}
				//18 地图信息
				LPVOID GetpMapInfo ( )
				{
					return m_pMapInfo;
				}
				//1c
				CGameInfo* GetpGameInfo ( )
				{
					return m_pGameInfo;
				}
				//20
				INT32 GetLookMinX ( )
				{
					return m_LookMinX;
				}
				INT32 GetLookMinY ( )
				{
					return m_LookMinY;
				}
				INT32 GetLookMaxX ( )
				{
					return m_LookMaxX;
				}
				INT32 GetLookMaxY ( )
				{
					return m_LookMaxY;
				}
				INT32 GetLookSizeMinX ( )
				{
					return m_LookSizeMinX;
				}
				INT32 GetLookSizeMinY ( )
				{
					return m_LookSizeMinY;
				}
				INT32 GetLookSizeMaxX ( )
				{
					return m_LookSizeMaxX;
				}
				INT32 GetLookSizeMaxY ( )
				{
					return m_LookSizeMaxY;
				}
				CVector<CPVEBossInfo>* GetvecBossInfo ( )
				{
					return &m_vecBossInfo;
				}

				INT32 GetContinueID ( )
				{
					return m_ContinueID;
				}
				INT32 GetMapIndex ( )
				{
					return m_MapIndex;
				}

				CVector<LPVOID>* GetvecInfoC ( )
				{
					return &m_vecInfoC;
				}

				void* InitBase ( bool Destroy ) { }

			}*m_pGamePVE;

			INT16 m_PVENextMapX;
			INT16 m_PVENextMapY;
			INT8 m_0x4E98 [ 0xC ];

			public:
			PGamePVE GetGamePVE ( )
			{
				return m_pGamePVE;
			}

		}m_0x4E0F;

		public:
		PMap GetMap( )
		{
			return &m_Map;
		}

		PMapBox GetMapBox ( )
		{
			return &m_MapBox;
		}

		PMapFloor GetMapFloor ( )
		{
			return &m_MapFloor;
		}

		PMapItem GetMapItem ( )
		{
			return &m_MapItem;
		}

		PMapBomb GetMapBomb ( )
		{
			return &m_MapBomb;
		}

		PBombExplode GetBombExplode ( )
		{
			return &m_BombExplode;
		}

		PBoxCode GetBoxCode ( )
		{
			return &m_BoxCode;
		}
		//2600
		PGameRoom GetBunRoomA ( ) const
		{
			return m_pBunRoomA;
		}
		PGameRoom GetBunRoomB ( ) const
		{
			return m_pBunRoomB;
		}
		PGameRoom GetSculptureRoomA ( ) const
		{
			return m_pSculptureRoomA;
		}
		PGameRoom GetSculptureRoomB ( ) const
		{
			return m_pSculptureRoomB;
		}
		PGameRoom GetTankRoomA ( ) const
		{
			return m_pTankRoomA;
		}
		PGameRoom GetTankRoomB ( ) const
		{
			return m_pTankRoomB;
		}

		//2618
		PSculptureItem GetSculptureItem ( )
		{
			return &m_SculptureItem;
		}

		//2648
		vector<CPlayer*>* GetPlayerList ( )
		{
			return m_PlayerList.GetVecInfo ( );
		}

		CPlayer* AtPlayer ( NPCINDEX index )
		{
			vector<CPlayer*>*pvecPlayer = GetPlayerList ( );
			if ( pvecPlayer->size ( ) > index )
			{
				return ( *pvecPlayer ) [ index ];
			}
			return NULL;
		}

		CPlayer* FindPlayer ( INT16 IdFromClient )
		{
			vector<CPlayer*>*pvecPlayer = GetPlayerList ( );
			vector<CPlayer*>::iterator it;
			for ( it = pvecPlayer->begin ( ); it != pvecPlayer->end ( ); it++ )
			{
				if ( IdFromClient == ( *it )->GetIDFromClinet ( ) )
				{
					return ( *it );
				}
			}
			return NULL;
		}

		//2658
		vector<CBoss*>* GetBossList ( )
		{
			return m_BossList.GetVecInfo ( );
		}

		CBoss* AtBOSS ( NPCINDEX index )
		{
			vector<CBoss*>*pvecBOSS = GetBossList ( );
			if ( pvecBOSS->size ( ) > index )
			{
				return ( *pvecBOSS ) [ index ];
			}
			return NULL;
		}

		CBoss* FindBOSS ( INT16 IdFromClient )
		{
			vector<CBoss*>*pvecBOSS = GetBossList ( );
			vector<CBoss*>::iterator it;
			for ( it = pvecBOSS->begin ( ); it != pvecBOSS->end ( ); it++ )
			{
				if ( IdFromClient == ( *it )->GetIDFromClinet ( ) )
				{
					return ( *it );
				}
			}
			return NULL;
		}
		bool IsBossID ( INT16 IdFromClient )
		{
			vector<CBoss*>*pvecBOSS = GetBossList ( );
			vector<CBoss*>::iterator it;
			for ( it = pvecBOSS->begin ( ); it != pvecBOSS->end ( ); it++ )
			{
				if ( IdFromClient == ( *it )->GetIDFromClinet ( ) )
				{
					return true;
				}
			}
			return false;
		}

		//2668
		PPlayBomb GetPlayBomb ( )
		{
			return &m_PlayBomb;
		}

        vector<ItemByGame>* GetFlyItem ( )
        {
            return m_0x4418.GetFlyItem ( );
        }

		UINT8 GetMachineSkill ( ) const
		{
			return m_0x4418.GetMachineSkill ( );
		}
		INT32 GetGameTime ( )const
		{
			return m_PlayerInfo.GetGameTime ( );
		}

		CPlayerInfo* GetPlayerInfo ( )
		{
			return &m_PlayerInfo;
		}

	};

	enum
	{
		CGameInfoSize = sizeof ( CGameInfo ),
	};
	static_assert( CGameInfoSize == 15252, "CGameInfoSize is error" );
}
