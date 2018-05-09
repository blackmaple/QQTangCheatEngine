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
#define PNPCItem CNPCItem*

namespace QQTangCheatEngine
{
	class CNPC;
	__interface I19CBase
	{
		public:
		void* InitBaseA ( bool Destroy );
		void* InitBaseB ( bool Destroy );
		void* InitBaseC ( bool Destroy );
		void* InitBaseD ( DWORD value );
		void* InitBaseE ( DWORD value );

	};
	__interface IItemInfoBase
	{
		public:
		void* InitBase ( bool Destroy );
		void InitBase ( );
		INT32 GetItem2B4 ( );
		INT32 SetHp ( INT32 value );
		void AddHp ( INT32 value );
		bool GetAvatar ( );
		void AddLayoutBomb ( INT16 value );
		INT32 GetBombPower ( );
		INT32 FunZeroB ( );
		INT32 FunZeroC ( INT32 value );
		void CalcBombSize ( );
	};

	class CItemInfo
	{
		private:
		CEncodeMember m_MinBomb;
		CEncodeMember m_MaxBomb;

		CEncodeMember m_MinPower;
		CEncodeMember m_MaxPower;

		CEncodeMember m_MinSpeed;
		CEncodeMember m_MaxSpeed;

		CEncodeMember m_PVESpeed;
		CEncodeMember m_PVEBomb;
		CEncodeMember m_PVEPower;

		// 不知道是什么
		CEncodeMember m_PVEITEMA;
		CEncodeMember m_PVEITEMB;

		CEncodeMember m_HP;

		CEncodeMember m_IsInvincible;

		INT32 m_108;

		CEncodeMember m_10C;

		INT32 m_120;

		CEncodeMember m_GetBomb;
		CEncodeMember m_GetPower;
		CEncodeMember m_GetSpeed;
		CEncodeMember m_AddBomb;
		CEncodeMember m_AddPower;
		CEncodeMember m_AddSpeed;

		class C19C :public I19CBase
		{
			private:
			INT32 m_200;
			CVector < CItemBySet > m_vecItemBySet;
			INT32 m_210;

			public:
			CVector<CItemBySet> *GetItemBySet ( )
			{
				return &m_vecItemBySet;
			}


			void* InitBaseA ( bool Destroy )
			{ }
			void* InitBaseB ( bool Destroy )
			{ }
			void* InitBaseC ( bool Destroy )
			{ }
			void* InitBaseD ( DWORD value )
			{ }
			void* InitBaseE ( DWORD value )
			{ }
		}m_19C;

		class C1B8 :public C19C
		{
			private:
			INT32 m_1C;
			CVector < LPVOID > m_vec20;
			CVector < LPVOID > m_vec30;

		}m_1B8;

		CEncodeMember m_KillSize;
		CEncodeMember m_DieSize;
		//连杀次数...double kill ^ ^
		CEncodeMember m_DoubleKillSize;
		CEncodeMember m_RedTreasure;
		CEncodeMember m_YellowTreasure;
		CEncodeMember m_GreenTreasure;
		INT32 m_BombType;
		INT32 m_BombEffect;
		INT32 m_EffectColor;
		CEncodeINT16 m_LayoutBomb;

		//0x28C
		CEncodeMember m_BombZero;

		INT32 m_bytes2A0;
		INT32 m_bytes2A4;
		INT32 m_bytes2A8;
		INT32 m_bytes2AC;

		//2B0
		union
		{
			UINT8 m_BunType;
			UINT8 m_SculptureColor;
		};
		INT8 m_bytes2B1 [ 3 ];

		CEncodeMember m_2B4;

		// 		INT32 m_2C8;
		//DropItem
		CVector < CItemByDrop > m_vecFirstItemByDrop;

		// 		INT32 m_2D8;
		//DropItem
		CVector<CItemByDrop>m_vecNextItemByDrop;

		CNPC* m_pNPC;
		INT32 m_ShowPVELevel;
		INT32 m_PVEAttack;
		INT32 m_ShowMaxBombA;
		INT32 m_2F8;
		INT32 m_ShowMaxHp;
		INT32 m_ShowMaxBombB;
		CEncodeMember m_LayoutBombTime;

		public:

		CEncodeMember* GetMinBomb ( )
		{
			return &m_MinBomb;
		}
		CEncodeMember* GetMaxBomb ( )
		{
			return &m_MaxBomb;
		}

		CEncodeMember* GetMinPower ( )
		{
			return &m_MinPower;
		}
		CEncodeMember* GetMaxPower ( )
		{
			return &m_MaxPower;
		}

		CEncodeMember* GetMinSpeed ( )
		{
			return &m_MinSpeed;
		}
		CEncodeMember* GetMaxSpeed ( )
		{
			return &m_MaxSpeed;
		}

		CEncodeMember* GetPVESpeed ( )
		{
			return &m_PVESpeed;
		}
		CEncodeMember* GetPVEBomb ( )
		{
			return &m_PVEBomb;
		}
		CEncodeMember* GetPVEPower ( )
		{
			return &m_PVEPower;
		}

		CEncodeMember* GetHP ( )
		{
			return &m_HP;
		}

		CEncodeMember* GetIsInvincible ( )
		{
			return &m_IsInvincible;
		}

		CEncodeMember* GetGetBomb ( )
		{
			return &m_GetBomb;
		}
		CEncodeMember* GetGetPower ( )
		{
			return &m_GetPower;
		}
		CEncodeMember* GetGetSpeed ( )
		{
			return &m_GetSpeed;
		}
		CEncodeMember* GetAddBomb ( )
		{
			return &m_AddBomb;
		}
		CEncodeMember* GetAddPower ( )
		{
			return &m_AddPower;
		}
		CEncodeMember* GetAddSpeed ( )
		{
			return &m_AddSpeed;
		}

		CEncodeMember* GetKillSize ( )
		{
			return &m_KillSize;
		}
		CEncodeMember* GetDieSize ( )
		{
			return &m_DieSize;
		}
		//连杀次数...double kill ^ ^
		CEncodeMember* GetDoubleKillSize ( )
		{
			return &m_DoubleKillSize;
		}
		CEncodeMember* GetRedTreasure ( )
		{
			return &m_RedTreasure;
		}
		CEncodeMember* GetYellowTreasure ( )
		{
			return &m_YellowTreasure;
		}
		CEncodeMember* GetGreenTreasure ( )
		{
			return &m_GreenTreasure;
		}
		INT32 GetBombType ( )
		{
			return m_BombType;
		}
		INT32 GetBombEffect ( )
		{
			return m_BombEffect;
		}
		INT32 GetEffectColor ( )
		{
			return m_EffectColor;
		}
		CEncodeINT16* GetLayoutBomb ( )
		{
			return &m_LayoutBomb;
		}

		//0x28C
		CEncodeMember* GetBombZero ( )
		{
			return &m_BombZero;
		}

		//2B0

		UINT8 GetBunType ( )
		{
			return m_BunType;
		}
		UINT8 GetSculptureColor ( )
		{
			return m_SculptureColor;
		}



		//DropItem
		CVector < CItemByDrop > * GetvecFirstItemByDrop ( )
		{
			return &m_vecFirstItemByDrop;
		}

		// 		INT32 Get2D8;
		//DropItem
		CVector<CItemByDrop>* GetvecNextItemByDrop ( )
		{
			return &m_vecNextItemByDrop;
		}

		CNPC* GetpNPC ( )
		{
			return m_pNPC;
		}
		INT32 GetShowPVELevel ( )
		{
			return m_ShowPVELevel;
		}
		INT32 GetPVEAttack ( )
		{
			return m_PVEAttack;
		}
		INT32 GetShowMaxBombA ( )
		{
			return m_ShowMaxBombA;
		}
		INT32 GetShowMaxHp ( )
		{
			return m_ShowMaxHp;
		}
		INT32 GetShowMaxBombB ( )
		{
			return m_ShowMaxBombB;
		}
		CEncodeMember* GetLayoutBombTime ( )
		{
			return &m_LayoutBombTime;
		}


		void* InitBase ( bool Destroy )
		{ }
		void InitBase ( )
		{ }
		INT32 GetItem2B4 ( )
		{ }
		INT32 SetHp ( INT32 value )
		{ }
		void AddHp ( INT32 value )
		{ }
		bool GetAvatar ( )
		{ }
		void AddLayoutBomb ( INT16 value )
		{ }
		INT32 GetBombPower ( )
		{ }
		INT32 FunZeroB ( )
		{ }
		INT32 FunZeroC ( INT32 value )
		{ }
		void CalcBombSize ( )
		{ }


	};
	class CNPCItem :public IItemInfoBase
	{
		private:
		CItemInfo m_ItemInfo;
		public:
		CItemInfo* GetItemInfo ( )
		{
			return &m_ItemInfo;
		}

		CEncodeMember* GetMinBomb ( )
		{
			return m_ItemInfo.GetMinBomb ( );
		}
		CEncodeMember* GetMaxBomb ( )
		{
			return m_ItemInfo.GetMaxBomb ( );
		}

		CEncodeMember* GetMinPower ( )
		{
			return m_ItemInfo.GetMinPower ( );
		}
		CEncodeMember* GetMaxPower ( )
		{
			return m_ItemInfo.GetMaxPower ( );
		}

		CEncodeMember* GetMinSpeed ( )
		{
			return m_ItemInfo.GetMinSpeed ( );
		}
		CEncodeMember* GetMaxSpeed ( )
		{
			return m_ItemInfo.GetMaxSpeed ( );
		}

		CEncodeMember* GetPVESpeed ( )
		{
			return m_ItemInfo.GetPVESpeed ( );
		}
		CEncodeMember* GetPVEBomb ( )
		{
			return m_ItemInfo.GetPVEBomb ( );
		}
		CEncodeMember* GetPVEPower ( )
		{
			return m_ItemInfo.GetPVEPower ( );
		}

		CEncodeMember* GetHP ( )
		{
			return m_ItemInfo.GetHP ( );
		}

		CEncodeMember* GetIsInvincible ( )
		{
			return m_ItemInfo.GetIsInvincible ( );
		}

		CEncodeMember* GetGetBomb ( )
		{
			return m_ItemInfo.GetGetBomb ( );
		}
		CEncodeMember* GetGetPower ( )
		{
			return m_ItemInfo.GetGetPower ( );
		}
		CEncodeMember* GetGetSpeed ( )
		{
			return m_ItemInfo.GetGetSpeed ( );
		}
		CEncodeMember* GetAddBomb ( )
		{
			return m_ItemInfo.GetAddBomb ( );
		}
		CEncodeMember* GetAddPower ( )
		{
			return m_ItemInfo.GetAddPower ( );
		}
		CEncodeMember* GetAddSpeed ( )
		{
			return m_ItemInfo.GetAddSpeed ( );
		}

		CEncodeMember* GetKillSize ( )
		{
			return m_ItemInfo.GetKillSize ( );
		}
		CEncodeMember* GetDieSize ( )
		{
			return m_ItemInfo.GetDieSize ( );
		}
		//连杀次数...double kill ^ ^
		CEncodeMember* GetDoubleKillSize ( )
		{
			return m_ItemInfo.GetDoubleKillSize ( );
		}
		CEncodeMember* GetRedTreasure ( )
		{
			return m_ItemInfo.GetRedTreasure ( );
		}
		CEncodeMember* GetYellowTreasure ( )
		{
			return m_ItemInfo.GetYellowTreasure ( );
		}
		CEncodeMember* GetGreenTreasure ( )
		{
			return m_ItemInfo.GetGreenTreasure ( );
		}
		INT32 GetBombType ( )
		{
			return m_ItemInfo.GetBombType ( );
		}
		INT32 GetBombEffect ( )
		{
			return m_ItemInfo.GetBombEffect ( );
		}
		INT32 GetEffectColor ( )
		{
			return m_ItemInfo.GetEffectColor ( );
		}
		CEncodeINT16* GetLayoutBomb ( )
		{
			return m_ItemInfo.GetLayoutBomb ( );
		}

		//0x28C
		CEncodeMember* GetBombZero ( )
		{
			return m_ItemInfo.GetBombZero ( );
		}

		//2B0

		UINT8 GetBunType ( )
		{
			return m_ItemInfo.GetBunType ( );
		}
		UINT8 GetSculptureColor ( )
		{
			return m_ItemInfo.GetSculptureColor ( );
		}



		//DropItem
		CVector<CItemByDrop>* GetvecFirstItemByDrop ( )
		{
			return m_ItemInfo.GetvecFirstItemByDrop ( );
		}

		// 		INT32 Get2D8;
		//DropItem
		CVector<CItemByDrop>* GetvecNextItemByDrop ( )
		{
			return m_ItemInfo.GetvecNextItemByDrop ( );
		}

		CNPC* GetpNPC ( )
		{
			return m_ItemInfo.GetpNPC ( );
		}
		INT32 GetShowPVELevel ( )
		{
			return m_ItemInfo.GetShowPVELevel ( );
		}
		INT32 GetPVEAttack ( )
		{
			return m_ItemInfo.GetPVEAttack ( );
		}
		INT32 GetShowMaxBombA ( )
		{
			return m_ItemInfo.GetShowMaxBombA ( );
		}
		INT32 GetShowMaxHp ( )
		{
			return m_ItemInfo.GetShowMaxHp ( );
		}
		INT32 GetShowMaxBombB ( )
		{
			return m_ItemInfo.GetShowMaxBombB ( );
		}
		CEncodeMember* GetLayoutBombTime ( )
		{
			return m_ItemInfo.GetLayoutBombTime ( );
		}



		//虚函数实现
		void* InitBase ( bool Destroy )
		{ }
		void InitBase ( )
		{ }
		INT32 GetItem2B4 ( )
		{ }
		INT32 SetHp ( INT32 value )
		{ }
		void AddHp ( INT32 value )
		{ }
		bool GetAvatar ( )
		{ }
		void AddLayoutBomb ( INT16 value )
		{ }
		INT32 GetBombPower ( )
		{ }
		INT32 FunZeroB ( )
		{ }
		INT32 FunZeroC ( INT32 value )
		{ }
		void CalcBombSize ( )
		{ }
	};

	enum
	{
		CNPCItemSize = sizeof ( CNPCItem ) ,
	};
	static_assert( CNPCItemSize == 0x318 , "CNPCItemSize is error" );
}


