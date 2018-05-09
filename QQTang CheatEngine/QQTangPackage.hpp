/************************************************************************/
/*
功能说明:数据包
创建人:maple
创建日期:2014年9月2日
修改日期:
*/
/************************************************************************/
#pragma once
#pragma  pack(1) 
#include "Maple.hpp"
#include "MessageLayer.hpp"

#define InitPackage(ClassName)\
ClassName ( )\
{\
memset ( this, 0, sizeof ( ClassName) );\
}

namespace QQTangCheatEngine
{	
	//BASE
	class CDROPPROPINFO
	{
		public:
		INT8 m_DropPropSize;
		class CDROPPROP
		{
			public:
			ItemByGame m_PropID;
			INT8 m_PropY;
			INT8 m_PropX;
		}m_DropProp [ 0x40 ];

	};
	class CPACKAGEBASE
	{
		public:
		INT16 m_PlayerID;
		INT32 m_GameTime;
	};

	//
	class CSendPackageInGame :public CPACKAGEBASE
	{
		public:


		INT32 m_GetTickCount;
		GameID m_GameID;
		INT16 m_Length;
		INT32 m_SendCount;
		UINT8 m_byPackage [ 0x2028 ];
	};

	class CSendPackageInRoom
	{
		public:
		INT32 m_GetTickCount;
		INT16 m_GameID;
		INT16 m_Length;
		INT32 m_SendCount;
		UINT8 m_byPackage [ 0xFF4 ];
		 
	};
 
	class CALLPLAYERINFOINROOM
	{
		public:
		INT32 m_PlayerCount;
		UINT32 m_QQ [ 8 ];
		INT16 m_PlayerID [ 8 ];
	};

	// 	//玩家移动 房间里
	// 	P2P_PLAYERMOVEINROOM = 0xBB8,
	class CPLAYERMOVEINROOM
	{
		public:
		INT8 m_PlayerNO;
		INT32 m_PlayerX;
		INT32 m_PlayerY;
		INT32 m_PlayerFace;
		float m_PlayerMove;
	};

	// 	//玩家放泡泡 房间里
	// 	P2P_PLAYERLAYOUTBOMBINROOM = 0xBB9,
	class CPLAYERLAYOUTBOMBINROOM
	{
		public:
		UINT8 m_PlayerNO;
		INT32 m_PlayerX;
		INT32 m_PlayerY;
	};

	// 	//玩家移动数据包
	// 	P2P_NPCMOVE = 0xFA2,
	class npcmove
	{

	};


	// 	//放泡泡
	// 	P2P_LAYOUTBOMB = 0xFA3,
	class CLAYOUTBOMB :public CPACKAGEBASE
	{
		public:
		UINT32 m_BombType;
		INT8 m_BombY;
		INT8 m_BombX;
		INT16 m_BombPower;
		bool m_IsHide;

		public:
		CLAYOUTBOMB(){}
		//放泡泡
		CLAYOUTBOMB ( PPlyaer pPlayer )
		{
			m_PlayerID = pPlayer->GetIDFromClinet ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
			m_BombY = ( INT8 ) pPlayer->GetPlayerInMapY ( );
			m_BombX = ( INT8 ) pPlayer->GetPlayerInMapX ( );
			m_BombPower = ( INT16 ) pPlayer->GetNPCItem ( )->GetBombPower ( );
			m_IsHide = pPlayer->IsItemUsing ( );
		}
		//复制泡泡
		CLAYOUTBOMB ( PPlyaer pdest, PPlyaer pscr )
		{
			m_PlayerID = pscr->GetIDFromClinet ( );
			m_GameTime = pdest->GetGameInfo ( )->GetGameTime ( );
			m_BombY = ( INT8 ) pdest->GetPlayerInMapY ( );
			m_BombX = ( INT8 ) pdest->GetPlayerInMapX ( );
			m_BombPower = ( INT16 ) pdest->GetNPCItem ( )->GetBombPower ( );
			m_IsHide = pdest->IsItemUsing ( );
		}
		//放泡泡指定位置
		CLAYOUTBOMB ( PPlyaer pPlayer, CLocation& XY )
		{
			m_PlayerID = pPlayer->GetIDFromClinet ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
			m_BombY = ( INT8 ) XY.GetY ( );
			m_BombX = ( INT8 ) XY.GetX ( );
			m_BombPower = ( INT16 ) pPlayer->GetNPCItem ( )->GetBombPower ( );
			m_IsHide = pPlayer->IsItemUsing ( );
		}


	};

	// 	//爆炸信息
	// 	P2P_EXPLODEINFO = 0xFA4,
	class CEXPLODEINFO :public CPACKAGEBASE
	{
		public:
		INT8 m_BombExplodeSize;
		class CBombExplode
		{
			public:
			INT16 m_BomberID;
			INT32 m_BombTime;
			INT8 m_BombMode;
			INT8 m_BombY;
			INT8 m_BombX;
			INT8 m_BombUp;
			INT8 m_BombDown;
			INT8 m_BombLeft;
			INT8 m_BombRigth;
		}m_BombExplode [ 64 ];

		INT8 m_BoxExplodeSize;
		class CBoxExplode
		{
			public:
			INT16 m_BoxID;
			INT8 m_BoxY;
			INT8 m_BoxX;
		}m_BoxExplode [ 32 ];

		INT8 m_PropExplodeSize;
		class CPropExplode
		{
			public:
			ItemByGame m_PropID;
			INT8 m_PropY;
			INT8 m_PropX;
		}m_PropExplode [ 32 ];
		CEXPLODEINFO ( ) { }
		CEXPLODEINFO ( PPlyaer pPlayer )
		{
			m_PlayerID = pPlayer->GetIDFromServer ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
		}

	};
	enum 
	{
		CEXPLODEINFOSIZE = sizeof ( CEXPLODEINFO ),
	};

	// 	//进果冻
	// 	P2P_INJELLY = 0xFA5,
	class CINJELLY :public CPACKAGEBASE
	{
		public:
		INT16 m_PlayerX;
		INT16 m_PlayerY;
		bool m_HadAvatar;
		public:
		CINJELLY ( ){ }
		CINJELLY ( PPlyaer pPlayer )
		{
			m_PlayerID = pPlayer->GetIDFromServer ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
			m_PlayerX = ( INT16 ) ( pPlayer->GetNPCX ( ) );
			m_PlayerY = ( INT16 ) ( pPlayer->GetNPCY ( ) );
			m_HadAvatar = pPlayer->GetAvatarInfo ( ) != NULL;
		}
	};

	// 	//NPC屎亡
	// 	P2P_NPCDIE = 0xFA7,
	class CNPCDIE :public CPACKAGEBASE
	{
		public:
		INT16 m_PlayerY;
		INT16 m_PlayerX;

		CDROPPROPINFO m_DropPropInfo;
		CNPCDIE(){}
		CNPCDIE ( PPlyaer pPlayer )
		{
			m_PlayerID = pPlayer->GetIDFromServer ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
			m_PlayerY = ( INT16 ) pPlayer->GetNPCX ( );
			m_PlayerX = ( INT16 ) pPlayer->GetNPCY ( );

		};
	};

	// 	//通知KO玩家
	// 	P2P_NOTIFYNPCKILL = 0xFA8,
	// 	//KO玩家
	// 	P2P_NPCKILL = 0xFA9,
#define CNOTIFYNPCKILL CNPCKILL
	class CNPCKILL :public CPACKAGEBASE
	{
		public:
		INT16 m_DaedID;
		INT16 m_KillerX;
		INT16 m_KillerY;
		CDROPPROPINFO m_DropPropInfo;
		CNPCKILL(){}
		CNPCKILL ( PPlyaer pKiller, PPlyaer pDaedID )
		{
			m_PlayerID = pKiller->GetIDFromServer ( );
			m_GameTime = pKiller->GetGameInfo ( )->GetGameTime ( );
			m_KillerX = ( INT16 ) pDaedID->GetNPCX ( );
			m_KillerY = ( INT16 ) pDaedID->GetNPCY ( );
			m_DaedID = pDaedID->GetIDFromServer ( );
		}
	};

	// 	//通知玩家救人
	// 	P2P_NOTIFYNPCSAVE = 0xFAA,
	// 	//玩家救人
	// 	P2P_NPCSAVE = 0xFAB,
#define CNOTIFYNPCSAVE CNPCSAVE
	class CNPCSAVE :public CPACKAGEBASE
	{
		public:
		INT16 m_DeadID;
		INT16 m_SaverX;
		INT16 m_SaverY;
		//自己9刷分
		CNPCSAVE(){}

		CNPCSAVE ( PPlyaer pSaver )
		{
			m_PlayerID = pSaver->GetIDFromServer ( );
			m_GameTime = pSaver->GetGameInfo ( )->GetGameTime ( );
			m_DeadID = pSaver->GetIDFromServer ( );
			m_SaverX = ( INT16 ) pSaver->GetNPCX ( );
			m_SaverY = ( INT16 ) pSaver->GetNPCY ( );
		}
		//9别人
		CNPCSAVE ( PPlyaer pSaver, PPlyaer pDead )
		{
			m_PlayerID = pSaver->GetIDFromServer ( );
			m_GameTime = pSaver->GetGameInfo ( )->GetGameTime ( );
			m_DeadID = pDead->GetIDFromServer ( );
			m_SaverX = ( INT16 ) pSaver->GetNPCX ( );
			m_SaverY = ( INT16 ) pSaver->GetNPCY ( );
		}
	};

	// 	//通知获取道具
	// 	P2P_NOTIFYNPCGETITEM = 0xFAC,
	//	//获取道具
	//	P2P_NPCGETITEM = 0xFAD,
#define CNOTIFYNPCGETITEM NPCGETITEM
	class CNPCGETITEM :public CPACKAGEBASE
	{
		public:
		ItemByGame m_PropID;
		union 
		{
			struct 
			{
				INT16 m_GeterX;
				INT16 m_GeterY;
			};
			struct
			{
				INT16 m_ItemX;
				INT16 m_ItemY;
			};
		};

		CNPCGETITEM ( ) { }
		CNPCGETITEM ( PPlyaer pGeter, ItemByGame propid )
		{
			m_PlayerID = pGeter->GetIDFromClinet ( );
			m_GameTime = pGeter->GetGameInfo ( )->GetGameTime ( );
			m_GeterX = (INT16)pGeter->GetNPCX ( );
			m_GeterY = (INT16)pGeter->GetNPCY ( );
			m_PropID = propid;
		}
		CNPCGETITEM ( PPlyaer pGeter, PGameItem pProp )
		{
			m_PlayerID = pGeter->GetIDFromClinet ( );
			m_GameTime = pGeter->GetGameInfo ( )->GetGameTime ( );
			m_PropID = pProp->GetItemID ( );
			m_GeterX = pProp->GetItemInPlayerX ( );
			m_GeterY = pProp->GetItemInPlayerY ( );
		}
		BOOL IsPropToServer ( )
		{
			switch ( m_PropID )
			{
				//81
				case QQTangCheatEngine::GAME_TONGBI:
				{
					return TRUE;
				}
					//82
				case QQTangCheatEngine::GAME_YINBI:
				{
					return TRUE;
				}
					//83
				case QQTangCheatEngine::GAME_JINBI:
				{
					return TRUE;
				}
					//84
				case QQTangCheatEngine::GAME_QIANDAI:
				{
					return TRUE;
				}
					//85
				case QQTangCheatEngine::GAME_BAOXIANG1000TB:
				{
					return TRUE;
				}
					//91
				case QQTangCheatEngine::GAME_HONGZUANSHI:
				{
					return TRUE;
				}
					//92
				case QQTangCheatEngine::GAME_LANZUANSHI:
				{
					return TRUE;
				}
					//211
				case QQTangCheatEngine::GAME_ZIZUANSHI:
				{
					return TRUE;
				}
					//212
				case QQTangCheatEngine::GAME_XUEPINGZI:
				{
					return TRUE;
				}
					//213
				case QQTangCheatEngine::GAME_HUANGLUOSI:
				{
					return TRUE;
				}
					//93
				case QQTangCheatEngine::GAME_TANGBI1000:
				{
					return TRUE;
				}
					//94
				case QQTangCheatEngine::GAME_TANGBI500:
				{
					return TRUE;
				}
					//86
				case QQTangCheatEngine::GAME_JINGYAN20:
				{
					return TRUE;
				}
					//87
				case QQTangCheatEngine::GAME_JINGYAN50:
				{
					return TRUE;
				}
					//88
				case QQTangCheatEngine::GAME_JINGYAN100:
				{
					return TRUE;
				}
					//89
				case QQTangCheatEngine::GAME_JINGYAN200:
				{
					return TRUE;
				}
					//96
				case QQTangCheatEngine::GAME_MEIGUI1:
				{
					return TRUE;
				}
					//97
				case QQTangCheatEngine::GAME_LVSHUIJING:
				{
					return TRUE;
				}
					//98
				case QQTangCheatEngine::GAME_KUBI:
				{
					return TRUE;
				}
					//150
				case QQTangCheatEngine::GAME_HONGBAOSHI:
				{
					return TRUE;
				}
					//151
				case QQTangCheatEngine::GAME_HUANGBAOSHI:
				{
					return TRUE;
				}
					//152
				case QQTangCheatEngine::GAME_LVBAOSHI:
				{
					return TRUE;
				}
					//402
				case QQTangCheatEngine::GAME_MEIGUI2:
				{
					return TRUE;
				}
					//403
				case QQTangCheatEngine::GAME_DIARY:
				{
					return TRUE;
				}
			}

			if ( ( m_PropID < 400 || m_PropID > 1000 ) &&
				 ( m_PropID <= 24000 || m_PropID >= 24500 ) &&
				 ( m_PropID <= 30000 || m_PropID >= 32000 ) &&
				 ( m_PropID < 25001 || m_PropID > 29000 ) &&
				 ( m_PropID < 9001 || m_PropID > 9010 ) )
			{
				return FALSE;
			}
			return TRUE;
		}
	};

	// 	//飞机爆道具
	// 	P2P_PLANEDROPITEM = 0xFAE,
	class CPLANEDROPITEM
	{
		public:
		INT32 m_GameTime;
		CDROPPROPINFO m_DropItemInfo;

		INT8 m_DropItemSize;
		class CDropItemInfoEx
		{
			ItemByGame m_PropItem;
			ItemByGame m_PropItemEx;
			INT8 m_PropY;
			INT8 m_PropX;
		}m_DropItemInfoEx [ 0x20 ];

	};

	// 	//通知使用技能
	// 	P2P_NOTIFYNPCUSESKILL = 0xFAF,
	// 	//通知使用道具
	// 	P2P_NOTIFYNPCUSEPROP = 0xFAF,
	// 	//使用技能
	// 	P2P_NPCUSESKILL = 0xFB0,
	// 	//使用道具
	// 	P2P_NPCUSEPROP = 0xFB0,
#define CNOTIFYNPCUSESKILL CNPCUSEPROP
#define CNOTIFYNPCUSEPROP CNPCUSEPROP
#define CNPCUSESKILL CNPCUSEPROP
	class CNPCUSEPROP :public CPACKAGEBASE
	{
		public:
		union
		{
			INT32 m_PropID;
			INT32 m_SkillID;
		};
		INT16 m_PlayerX;
		INT16 m_PlayerY;
		BOOL m_GlobalSkill;
		INT32 m_PlayerFace;
		INT32 m_SkillY;
		INT32 m_SkillX;

	};
	enum
	{
		CNPCUSEPROPSIZE = sizeof ( CNPCUSEPROP ),
	};


#define CNOTIFYPUSHBOX cpushbox
	class cpushbox
	{

	};

	// 	//玩家固定位置
	// 	P2P_PLAYERFIXED = 0xFB5,
	class CPLAYERFIXED :public CPACKAGEBASE
	{
		public:
		ItemByGame m_PropID;
		INT16 m_PlyaerX;
		INT16 m_PlayerY;
		INT32 m_v1;
		INT32 m_v2;
		INT32 m_v3;
		INT32 m_v4;
		//INT16 m_v2;
	};

	// 	//通知包子出房间
	// 	P2P_NOTIFYGETBUNOUTROOM = 0xFB6,
	// 		//包子出房间
	// 		P2P_GETBUNOUTROOM = 0xFB7,
	// 		//通知包子进房间
	// 		P2P_NOTIFYGETBUNINROOM = 0xFB8,
	// 		//包子进房间
	// 		P2P_GETBUNINROOM = 0xFB9,
#define  CNOTIFYGETBUNOUTROOM CGETBUNOUTROOM
#define  CNOTIFYGETBUNINROOM CGETBUNOUTROOM
#define  CGETBUNINROOM CGETBUNOUTROOM
	class CGETBUNOUTROOM :public CPACKAGEBASE
	{
		public:
		INT16 m_PlayerX;
		INT16 m_PlayerY;
		INT8 m_GameIDType;
		union
		{
			UINT8 m_BunColor;
			UINT8 m_SculptureType;
		};
	};
	enum
	{
		CGETBUNOUTROOMSIZE = sizeof ( CGETBUNOUTROOM ),
	};

	// 	//玩家复活
	// 	P2P_NPCRELIVE = 0xFBA,
	class CNPCRELIVE :public CPACKAGEBASE
	{
		public:
		INT8 m_ReliveX;
		INT8 m_ReliveY;
		CNPCRELIVE() {}
		CNPCRELIVE ( PPlyaer pPlayer )
		{
			m_PlayerID = pPlayer->GetIDFromServer ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
			m_ReliveX = ( INT8 ) pPlayer->GetReLiveX ( );
			m_ReliveY = ( INT8 ) pPlayer->GetReLiveY ( );
		}
	};

	// 	//推箱子爆炸
	// 	P2P_PUSHBOXEXPLODE = 0xFBE,
	class cpushboxexplode
	{

	};

	// 	//玩家变身结束
	// 	P2P_NPCAVATARDISAPPEAR = 0x10E0,
	class CNPCAVATARDISAPPEAR :public CPACKAGEBASE
	{
		public:
		INT16 m_PlayerX;
		INT16 m_PlayerY;
		CNPCAVATARDISAPPEAR(){}
		CNPCAVATARDISAPPEAR ( PPlyaer pPlayer )
		{
			m_PlayerID = pPlayer->GetIDFromServer ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
			m_PlayerX = ( INT16 ) pPlayer->GetNPCX ( );
			m_PlayerY = ( INT16 ) pPlayer->GetNPCY ( );
		}
	};

	// 	//足球飞泡泡
	// 	P2P_GAMEDROPBOMB = 0x10E1,
	class cgamedropbomb
	{

	};

	// 	//玩家掉血
	// 	P2P_NPCHPLOSS = 0x10F4,
	class CNPCHPLOSS :public CPACKAGEBASE
	{
		public:
		INT16 m_PlayerX;
		INT16 m_PlayerY;
		bool m_HadAvatar;
		INT16 m_Hp;
		CNPCHPLOSS(){}
		CNPCHPLOSS ( PPlyaer pPlayer, INT16 IsAdd )
		{
			m_PlayerID = pPlayer->GetIDFromServer ( );
			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
			m_PlayerX = ( INT16 ) pPlayer->GetNPCX ( );
			m_PlayerY = ( INT16 ) pPlayer->GetNPCY ( );
			m_HadAvatar = pPlayer->GetItemInfo ( )->GetAvatar ( );

			m_Hp = ( INT16 ) -pPlayer->GetNPCItem ( )->GetHP ( )->GetValue ( TRUE );
			m_Hp *= IsAdd;
		}
	};

	// 	//创建箱子
	// 	P2P_CREATEBOX = 0x1168,
	class CCREATEBOX
	{
		public:
		INT8 m_CreateBoxSize;
		class CREATEBOXINFO
		{
			public:
			INT16 m_BoxID;
			INT32 m_BoxCode;
			INT8 m_BoxY;
			INT8 m_BoxX;
		}m_CreateBoxInfo [ 0x20 ];
	};

	// 	//BOSS 技能
	// 	P2P_BOSSSKILL = 0x1169,
	class CBOSSSKILL :public CPACKAGEBASE
	{
		public:
		short m_PlayerX;
		short m_PlayerY;
		SkillByBoss m_SkillID;
		CDROPPROPINFO m_DropPropInfo;
	};
 
	// 	//BOSS 说话
	// 	P2P_BOSSSPEAK = 0x116A,
	class CBOSSSPEAK
	{
		public:
		INT16 m_PlayerID;
		INT16 m_Length;
		char szText [ 0x200 ];
		CBOSSSPEAK ( PPlyaer pPlayer, char* pszText )
		{
			m_PlayerID = pPlayer->GetIDFromServer ( );
			m_Length = strlen ( pszText );
			strcpy ( szText, pszText );
		}
	};

	// 	//BOSS爆道具
	// 	P2P_BOSSDROPITEM = 0x116B,
	class CBOSSDROPITEM
	{
		public:
		INT16 m_BossID;
		INT16 m_BossX;
		INT16 m_BossY;
		CDROPPROPINFO m_DropPropInfo;
	};

	// 	//位置跨门
	// 	P2P_TRANSDOOR = 0x1176,
	class CTRANSDOOR
	{
		public:
		INT16 m_TranType;
		INT16 m_PlayerID;
		INT32 m_GameTime;
		INT16 TX;
		INT16 TY;
		INT16 RX;
		INT16 RY;
	};

	// 	//玩家表情
	// 	P2P_NPCEXPRESSION = 0x1194,
	class CNPCEXPRESSION :public CPACKAGEBASE
	{
		public:
		PlayerExpression m_Expression;
		CNPCEXPRESSION(){}
		CNPCEXPRESSION(PPlyaer pPlayer, PlayerExpression Expression)
		{
			m_PlayerID = pPlayer->GetIDFromServer();
			m_GameTime = pPlayer->GetGameInfo()->GetGameTime();
			m_Expression = Expression;
		}
	};

	// 	//创建BOSS
	// 	P2P_CREATEBOSS = 0x1389,
	class CCREATEBOSS
	{
		public:
		INT32 m_define;
		INT16 m_BossID;
		UINT8 m_Model;
		UINT8 m_Color;
		INT32 m_Status;
		INT16 m_BOSSX;
		INT16 m_BOSSY;
		INT16 m_Hp;

		INT32 m_MinSpeed;
		INT32 m_MinBomb;
		INT16 m_MinPower;
		CDROPPROPINFO m_DropPropItemA [ 0xA ];
		INT8 m_bytes [ 0x4C ];
		INT32 m_defineA;
		CDROPPROPINFO m_DropPropItemB [ 0xA ];
		INT16 m_Size;
		INT32 m_SizeInfo [ 0xA ];
		INT8 m_bytesA [ 0x84 ];

	};

	// 	//通知玩家退出
	// 	S2C_NOTIFYPLAYERQUITGAME = 0x10EC,
	class CNOTIFYPLAYERQUITGAME
	{
		public:
		INT16 m_PlayerID;
		CNOTIFYPLAYERQUITGAME(){}
		CNOTIFYPLAYERQUITGAME(PPlyaer pPlayer)
		{
			m_PlayerID = pPlayer->GetIDFromServer();
		}
	};



	// 		//通知游戏结束
	// 	S2C_NOTIFYGAMEOVER = 0xFBB,
	class CNOTIFYGAMEOVER
	{
		public:
		CNOTIFYGAMEOVER(){}

	};

	// 		//通知新仲裁
	// 	S2C_NOTIFYNEWARBITRATION = 0xFB1,
	class CNOTIFYNEWARBITRATION
	{
		public:
		INT16 m_PlayerID;
		CNOTIFYNEWARBITRATION(){}
	};


	// 	//使用道具调整位置
	// 	S2C_0xADJUSTPOSITION = 0x1175,
	class CADJUSTPOSITION
	{
		public:
		INT16 m_PlayerID;
		ItemByGame m_PropID;
		INT16 m_PlayerX;
		INT16 m_PlayerY;
		INT32 m_GameTime;
		UINT8 m_PlayerFace;
	};


	// 	//探险进图
	// 	C2S_NEXTPVEMAP = 0x1178,
	class CNEXTPVEMAP :public CPACKAGEBASE
	{
		public:
		INT32 m_ContinueID = 0;
		INT32 m_MapIndex = 0;

	};

	//	//糖果站房子爆炸
	//	C2S_TANKROOMEXPLODE = 0x15B3,
	class CTANKROOMEXPLODE :public CPACKAGEBASE
	{
		public:
		INT16 m_TankColor = 0;
		INT16 m_TankHP = 0;
		CTANKROOMEXPLODE(){}
		CTANKROOMEXPLODE ( PPlyaer pMySelf )
		{
			auto *pRoom = pMySelf->GetGameInfo ( )->GetTankRoomA ( );
			if ( pRoom->GetRoomColor ( ) == pMySelf->GetPlayerTeamColor ( ) )
			{
				pRoom = pMySelf->GetGameInfo ( )->GetTankRoomB ( );
			}
			m_TankColor = pRoom->GetRoomColor ( );
			m_TankHP = -pRoom->GetTaskHp ( );
		}
	};

// 	//足球飞泡泡
// 	P2P_GAMEDROPBOMB = 0x10E1,
	class CGAMEDROPBOMB :public CPACKAGEBASE
	{
		public:
		INT8 m_DropBombSize;
		class CDROPBOMBINFO
		{
			INT32 m_BombType;
			INT8 m_BombPower;
			INT8 m_BombY;
			INT8 m_BombX;
		}m_DropBombInfo [ 0x20 ];
		CDROPPROPINFO m_DropPropInfo;
	};
// 	class CNOTIFYMACHINESKILL
// 	{
// 		protected:
// 		UINT8 EncodeOfPlayerFace;
// 		bool isMachineSkill;
// 		UINT8 XY;
// 		INT16 PlayerID;
// 		public:
// 		CNOTIFYMACHINESKILL ( CMessageLayer* pLayer, CPlayer* pPlayer )
// 		{
// 			PlayerID = pPlayer->GetIDFromClinet ( );
// 
// 			EncodeOfPlayerFace = pPlayer->GetPlayerFace ( );;
// 			EncodeOfPlayerFace <<= 4;
// 			EncodeOfPlayerFace += ( UINT8 ) pLayer->GetTimeSub ( );
// 
// 			isMachineSkill = pPlayer->GetGameInfo ( )->
// 				GetMachineSkill ( ) == pPlayer->GetPlayerTeamColor ( );
// 
// 			XY = ( INT8 ) pPlayer->GetPlayerInMapY ( );
// 			XY <<= 4;
// 			XY += pPlayer->GetPlayerInMapX ( );
// 		}
// 	};
// 
// 	class CMACHINESKILL :public CNOTIFYMACHINESKILL
// 	{
// 		public:
// 		CMACHINESKILL ( CMessageLayer* pLayer, CPlayer* pPlayer ) :
// 			CNOTIFYMACHINESKILL ( pLayer, pPlayer )
// 		{
// 			UINT8 byEncode = EncodeOfPlayerFace & 0xF;
// 			INT8 Encode = ( INT8 ) ( EncodeOfPlayerFace >> 4 );
// 			if ( byEncode > -1 && byEncode < 8 && !pPlayer->IsPlayerYear ( PlayerID ) )
// 			{
// 				EncodeOfPlayerFace = ( UINT8 ) ( ( Encode << 4 ) + 9 );
// 			}
// 			if ( byEncode < 8 )
// 			{
// 				bool IsSkill;
// 				if ( isMachineSkill )
// 				{
// 					IsSkill = ( Encode == 0 );
// 				}
// 				else
// 				{
// 					IsSkill = ( Encode == 2 );
// 				}
// 				if ( !IsSkill )
// 				{
// 					EncodeOfPlayerFace = ( UINT8 ) ( ( Encode << 4 ) + 9 );
// 				}
// 			}
// 		}
// 	};
// 
// 	class CNOTIFYBOXEXPLODE :public CPACKAGEBASE
// 	{
// 		public:
// 		INT16 m_PlayerX;
// 		INT16 m_PlayerY;
// 		INT16 m_BoxID;
// 		INT32 m_PushBox;
// 		INT8 m_BoxX;
// 		INT8 m_BoxY;
// 		public:
// 		CNOTIFYBOXEXPLODE ( PPlyaer pPlayer )
// 		{
// 			m_PlayerID = pPlayer->GetIDFromClinet ( );
// 			m_GameTime = pPlayer->GetGameInfo ( )->GetGameTime ( );
// 			m_PlayerX = ( INT16 ) pPlayer->GetPlayerX ( );
// 			m_PlayerY = ( INT16 ) pPlayer->GetPlayerY ( );
// 		}
// 		void SetGameBox ( PGameBox pGamebox )
// 		{
// 			m_BoxID = pGamebox->GetBoxID ( );
// 			m_PushBox = pGamebox->GetPushBox ( );
// 			m_BoxX = pGamebox->GetLocation ( )->GetX ( );
// 			m_BoxY = pGamebox->GetLocation ( )->GetY ( );
// 		}
// 	};


// 	//机械大炮
// 	P2P_MACHINEARTILLERY = 0x10F3,
	class CMACHINEARTILLERY:public CPACKAGEBASE
	{
		public:
		INT8 m_BombSize;
		INT32 m_BombType;
		INT8 m_BombLength;
		INT8 m_BombY;
		INT8 m_BombX;
	};


// 	//踢泡泡
// 	P2P_PLAYBOMB = 0xFB4,
	class CPLAYBOMB
	{
		public:
		//0 1
		INT16 m_PlayerID;
		//2 3
		INT16 m_GameTime;
		// 4 5 6 7
		CLocation m_OldYX;
		//8 9 A B
		CLocation m_NewYX;
		//C
		UINT8 m_PlayerFace;
		//D E
		INT16 m_BomberID;
		//F 10 11 12
		INT32 m_BombTime;
		// 13
		INT8 m_BombPower;
	};

}


