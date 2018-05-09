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
#include "NPCItem.hpp"
#include "GameItem.hpp"
#define PNPC CNPC*

namespace QQTangCheatEngine
{
	class CGameInfo;
	class CNPC;

	__interface IBasicBase
	{
		void* InitBaseA ( bool Destroy );
		void* InitBaseB ( );
		void* InitBaseC ( );
		void* ShowA ( );
		void* ShowB ( );
		bool IsInvincible ( );

	};
	__interface IInfoBase
	{
		void InitBaseA ( );
		void InitBaseB ( );

	};
	__interface INPCBase
	{
		void* InitBaseA ( bool Destroy );

	};

	class CNPC :public IBasicBase
	{
		private:
		CItemInfo m_ItemInfo;

		class CBasic :public IBasicBase
		{
			private:
			INT32 m_31C;
			INT32 m_320;
			CGameInfo* m_pGameInfo;
			INT16 m_IDFromClinet;
			INT16 m_IDFromServer;
			PNPC m_pNPC;
			BOOL m_Invincible;
			INT32 m_InvincibleTime;
			float m_NPCX;
			float m_NPCY;
			INT32 m_340;
			INT32 m_344;
			INT32 m_348;

			public:
			CGameInfo* GetGameInfo ( )
			{
				return m_pGameInfo;
			}
			INT16 GetIDFromClinet ( )
			{
				return m_IDFromClinet;
			}
			INT16 GetIDFromServer ( )
			{
				return m_IDFromServer;
			}
			PNPC GetNPC ( )
			{
				return m_pNPC;
			}
			BOOL GetInvincible ( )
			{
				return m_Invincible;
			}
			INT32 GetInvincibleTime ( )
			{
				return m_InvincibleTime;
			}
			float GetNPCX ( )
			{
				return m_NPCX;
			}
			float GetNPCY ( )
			{
				return m_NPCY;
			}

			void* InitBaseA ( bool Destroy )
			{ }
			void* InitBaseB ( )
			{ }
			void* InitBaseC ( )
			{ }
			void* ShowA ( )
			{ }
			void* ShowB ( )
			{ }
			bool IsInvincible ( )
			{ }
		}m_Basic;

		class CInfo :public IInfoBase
		{
			private:
			INT32 m_350;
			INT32 m_X;
			INT32 m_Y;
			INT32 m_35C;
			INT32 m_360;
			INT32 m_364;
			INT32 m_368;
			LPVOID m_36C;
			//CONST 2
			INT32 m_370;
			INT32 m_374;
			INT32 m_378;
			UINT32 m_PlayerQQ;
			char m_PlayerName [ 0x14 ];
			//PlayerModle
			UINT8 m_PlayerModle;
			//TeamColor
			UINT8 m_PlayerTeamColor;
			INT16 m_396;
			INT32 m_398;
			INT32 m_39C;
			INT32 m_3A0;
			INT32 m_3A4;
			INT32 m_PlayerX;
			INT32 m_PlayerY;
			INT32 m_3B0;
			UINT8 m_PlayerFaceA;
			UINT8 m_PlayerFaceB;
			UINT8 m_PlayerFaceC;
			UINT8 m_PlayerStatus;
			UINT8 m_PlayerMoving;
			INT8 m_3B9;
			INT8 m_3BA;
			INT8 m_3BB;
			INT32 m_3BCH;
			INT32 m_3C0;
			INT32 m_3C4;
			INT32 m_3C8;
			INT32 m_3CC;
			INT32 m_3D0;
			INT32 m_3D4;
			INT32 m_3D8;
			INT32 m_3DC;
			INT32 m_3E0;
			INT32 m_3E4;
			INT32 m_3E8;
			CVector<CGameItem>m_vecGameItem;

			public:
			CVector<CGameItem>* GetGameItem ( )
			{
				return &m_vecGameItem;
			}

			bool IsItemUsing ( )
			{
				vector<CGameItem>* vecItem = m_vecGameItem.GetVecInfo ( );
				vector<CGameItem>::iterator it;
				for ( it = vecItem->begin ( ); it != vecItem->end ( ); it++ )
				{
					return ( *it ).IsUsing ( );
				}
			}

			INT32 GetX ( )
			{
				return m_X;
			}
			INT32 GetY ( )
			{
				return m_Y;
			}
			UINT32 GetPlayerQQ ( )
			{
				return m_PlayerQQ;
			}
			char* GetPlayerName ( )
			{
				return m_PlayerName;
			}
			UINT8 GetPlayerModle ( )
			{
				return m_PlayerModle;
			}
			UINT8 GetPlayerTeamColor ( )
			{
				return m_PlayerTeamColor;
			}
			INT32 GetPlayerX ( )
			{
				return m_PlayerX;
			}
			INT32 GetPlayerY ( )
			{
				return m_PlayerY;
			}
			UINT8 GetPlayerStatus ( )
			{
				return m_PlayerStatus;
			}

			UINT8 GetPlayerMoving ( )
			{
				return m_PlayerMoving;
			}
			UINT8 GetPlayerFace ( )
			{
				return m_PlayerFaceA;
			}

			void InitBaseA ( )
			{ }
			void InitBaseB ( )
			{ }

		}m_INFO;

		CGameInfo* m_pGameInfo;
		PNPCItem m_pNPCItem;
		LPVOID m_pAvatarInfo;
		INT32 m_408;
		LPVOID m_40C;
		INT32 m_410;
		INT32 m_414;
		INT32 m_418;
		LPVOID m_41C;
		LPVOID m_420;
		BOOL m_XBomb;
		INT32 m_428;
		INT32 m_42C;
		INT32 m_430;
		INT32 m_434;
		INT32 m_438;
		INT32 m_43C;
		INT32 m_440;
		INT32 m_444;
		INT32 m_448;
		INT32 m_44C;
		INT32 m_450;
		INT32 m_454;
		INT32 m_458;
		INT32 m_45C;
		INT32 m_460;
		INT32 m_464;
		INT32 m_468;
		INT32 m_46C;
		INT16 m_ReLiveY;
		INT16 m_ReLiveX;
		INT32 m_474;
		INT32 m_478;
		INT32 m_47C;
		INT32 m_480;
		INT32 m_484;
		INT32 m_488;
		INT32 m_48C;
		INT8 m_bytes [ 0x200 ];

		INT32 m_WUGUI;
		INT32 m_694;
		INT32 m_698;
		INT32 m_69C;

		INT32 m_6A0;
		INT32 m_6A4;
		INT32 m_6A8;
		INT32 m_6AC;

		INT32 m_6B0;
		INT32 m_6B4;
		INT32 m_6B8;
		INT32 m_6BC;

		//机械技能时间
		INT32 m_MachineSkillCD;
		BOOL m_CanMachineSkill;
		BOOL m_ReversalControl;
		BOOL m_ThroughMapItem;

		BOOL m_DetectPower;
		BOOL m_CanGetItem;
		INT32 m_6D8;
		INT32 m_6DC;

		INT32 m_6E0;
		INT32 m_6E4;
		INT32 m_6E8;
		INT32 m_6EC;

		INT32 m_6F0;
		INT32 m_6F4;
		INT32 m_6F8;
		INT32 m_6FC;

		INT32 m_700;
		INT32 m_704;
		INT32 m_708;
		INT32 m_70C;

		INT32 m_710;
		INT32 m_714;
		INT32 m_718;
		INT32 m_71C;

		INT32 m_720;
		INT32 m_724;
		INT32 m_728;
		INT32 m_72C;

		INT32 m_730;
		INT32 m_734;
		INT32 m_738;
		INT32 m_73C;

		INT32 m_740;
		INT32 m_744;
		INT32 m_748;
		INT32 m_74C;

		INT32 m_750;
		union
		{
			BOOL m_PVEInvincible;
			struct
			{
				INT16 m_754;
				INT16 m_756;

			};
		};
		INT32 m_PVEInvincibleTime;
		INT32 m_75C;
		// 		union
		// 		{
		// 			struct 
		// 			{
		// 				
		INT32 m_LayoutBombSpeed;
		INT32 m_764;
		INT32 m_768;
		// 			};
		//cl不给力啊

		//vector<LPVOID> m_vecInfo;
		// 		};

		//maple 2014-09-27 22:08:53
		//0x76C
		class CNewBossInfo
		{

			CVector<LPVOID>m_0x76C;
			INT32 m_0x77C;

			INT32 m_0x780;
			INT32 m_0x784;
			INT32 m_0x788;
			INT32 m_0x78C;

			INT32 m_0x790;
			INT32 m_0x794;
			INT32 m_0x798;
			INT32 m_0x79C;


			INT32 m_0x7A0;
			INT32 m_0x7A4;
			INT32 m_0x7A8;
			INT32 m_0x7AC;

			INT32 m_0x7B0;
			INT32 m_0x7B4;
			CVector<LPVOID>m_0x7B8;

			INT32 m_0x7C8;
			CLocation m_LiveXY;

			INT32 m_0x7D0;
			INT32 m_0x7D4;
			INT32 m_Fuvk;
			INT32 m_0x7DC;

			INT32 m_0x7E0;
			INT32 m_0x7E4;
			INT32 m_0x7E8;
			INT32 m_0x7EC;

			INT32 m_0x7F0;
			INT32 m_0x7F4;
			INT32 m_0x7F8;
			INT32 m_0x7FC;

			INT32 m_0x800;
			INT32 m_0x804;
			INT32 m_0x808;
			INT32 m_0x80C;

			INT32 m_0x810;
			INT32 m_0x814;
			INT32 m_0x818;
			INT32 m_0x81C;

			INT32 m_0x820;
			INT32 m_0x824;
			INT32 m_0x828;
			INT32 m_0x82C;

			INT32 m_0x830;
			INT32 m_0x834;
			INT32 m_0x838;
			INT32 m_0x83C;

			INT32 m_0x840;
			INT32 m_0x844;
			INT32 m_0x848;
			INT32 m_0x84C;

			INT32 m_0x850;
			INT32 m_0x854;
			INT32 m_0x858;
			INT32 m_0x85C;


			INT32 m_0x860;
			INT32 m_0x864;
			INT32 m_0x868;
			INT32 m_0x86C;

			INT32 m_0x870;
			INT32 m_0x874;
			INT32 m_0x878;
			INT32 m_0x87C;

			INT32 m_0x880;
			INT32 m_0x884;
			INT32 m_0x888;
			INT32 m_0x88C;

			INT32 m_0x890;
			INT32 m_0x894;
			INT32 m_0x898;
			INT32 m_0x89C;

			INT32 m_0x8A0;
			INT32 m_0x8A4;
			INT32 m_0x8A8;
			INT32 m_0x8AC;

			INT32 m_0x8B0;
			INT32 m_0x8B4;
			INT32 m_0x8B8;
			INT32 m_0x8BC;

			INT32 m_0x8C0;
			INT32 m_0x8C4;
			INT32 m_0x8C8;
			INT32 m_0x8CC;

			INT32 m_0x8D0;
			INT32 m_0x8D4;
			INT32 m_0x8D8;
			INT32 m_0x8DC;


			INT32 m_0x8E0;
			INT32 m_0x8E4;
			INT32 m_0x8E8;
			INT32 m_0x8EC;

			INT32 m_0x8F0;
			INT32 m_0x8F4;
			INT32 m_0x8F8;
			INT32 m_0x8FC;

			INT32 m_0x900;
			INT32 m_0x904;
			INT32 m_0x908;
			INT32 m_0x90C;

			INT32 m_0x910;
			INT32 m_0x914;
			INT32 m_0x918;
			INT32 m_0x91C;

			INT32 m_0x920;
			INT32 m_0x924;
			INT32 m_0x928;
			INT32 m_0x92C;

			INT32 m_0x930;
			INT32 m_0x934;
			INT32 m_0x938;
			INT32 m_0x93C;

			INT32 m_0x940;
			INT32 m_0x944;







		}m_NewBossInfo;


		public:
		CItemInfo* GetItemInfo ( )
		{
			return &m_ItemInfo;
		}
		CBasic* GetBasic ( )
		{
			return &m_Basic;
		}
		CInfo* GetINFO ( )
		{
			return &m_INFO;
		}
		CGameInfo* GetGameInfo ( )
		{
			return this->m_pGameInfo;
		}
		PNPCItem  GetNPCItem ( )
		{
			return this->m_pNPCItem;
		}
		LPVOID GetAvatarInfo ( )
		{
			return this->m_pAvatarInfo;
		}
		BOOL  GetXBomb ( )
		{
			return this->m_XBomb;
		}
		INT16 GetReLiveY ( )
		{
			return this->m_ReLiveY;
		}
		INT16 GetReLiveX ( )
		{
			return this->m_ReLiveX;
		}
		INT32 GetWUGUI ( )
		{
			return this->m_WUGUI;
		}
		BOOL  GetReversalControl ( )
		{
			return this->m_ReversalControl;
		}
		BOOL  GetThroughMapItem ( )
		{
			return this->m_ThroughMapItem;
		}
		INT32 GetMachineSkillCD ( )
		{
			return m_MachineSkillCD;
		}
		BOOL GetCanMachineSkill ( )
		{
			return m_CanMachineSkill;
		}

		BOOL  GetDetectPower ( )
		{
			return this->m_DetectPower;
		}
		BOOL  GetCanGetItem ( )
		{
			return this->m_CanGetItem;
		}
		BOOL  GetPVEInvincible ( )
		{
			return this->m_PVEInvincible;
		}
		INT32 GetPVEInvincibleTime ( )
		{
			return this->m_PVEInvincibleTime;
		}
		INT32 GetLayoutBombSpeed ( )
		{
			return this->m_LayoutBombSpeed;
		}

		INT16 GetIDFromClinet ( )
		{
			return m_Basic.GetIDFromClinet ( );
		}
		INT16 GetIDFromServer ( )
		{
			return m_Basic.GetIDFromServer ( );
		}
		PNPC GetNPC ( )
		{
			return m_Basic.GetNPC ( );
		}
		BOOL GetInvincible ( )
		{
			return m_Basic.GetInvincible ( );
		}
		INT32 GetInvincibleTime ( )
		{
			return m_Basic.GetInvincibleTime ( );
		}
		float GetNPCX ( )
		{
			return m_Basic.GetNPCX ( );
		}

		float GetNPCY ( )
		{
			return m_Basic.GetNPCY ( );
		}

		bool IsInvincible ( )
		{
			return m_Basic.IsInvincible ( );
		}

		CVector<CGameItem>* GetGameItem ( )
		{
			return m_INFO.GetGameItem ( );
		}

		INT32 GetX ( )
		{
			return m_INFO.GetX ( );
		}
		INT32 GetY ( )
		{
			return m_INFO.GetY ( );
		}
		UINT32 GetPlayerQQ ( )
		{
			return m_INFO.GetPlayerQQ ( );
		}
		char* GetPlayerName ( )
		{
			return m_INFO.GetPlayerName ( );
		}
		UINT8 GetPlayerModle ( )
		{
			return m_INFO.GetPlayerModle ( );
		}
		UINT8 GetPlayerTeamColor ( )
		{
			return m_INFO.GetPlayerTeamColor ( );
		}
		INT32 GetPlayerX ( )
		{
			return m_INFO.GetPlayerX ( );
		}
		INT32 GetPlayerY ( )
		{
			return m_INFO.GetPlayerY ( );
		}
		UINT8 GetPlayerFace ( )
		{
			return m_INFO.GetPlayerFace ( );
		}

		UINT8 GetPlayerStatus ( )
		{
			return m_INFO.GetPlayerStatus ( );
		}

		UINT8 GetPlayerMoving ( )
		{
			return m_INFO.GetPlayerMoving ( );
		}

		INT16 GetPlayerInMapX ( )
		{
			return ( ( INT16 ) ( this->GetNPCX ( ) ) / 40 );
		}

		INT16 GetPlayerInMapY ( )
		{
			return ( ( INT16 ) ( this->GetNPCY ( ) ) / 40 );
		}

		bool IsItemUsing ( )
		{
			return m_INFO.IsItemUsing ( );
		}

	};

	enum
	{
		CNPCSize = sizeof ( CNPC ) ,
	};
	static_assert( CNPCSize == 0x948 , "CNPCSize is error" );
}


