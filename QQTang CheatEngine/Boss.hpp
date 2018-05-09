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
#include "NPC.hpp"
#define PBoss CBoss*

namespace QQTangCheatEngine
{
	class CBoss :
		public CNPC
	{
		public:

	};

	class CPVEBossInfo
	{
		private:
		INT32 m_IDFromClient;
		INT32 m_IDFromServer;
		BOOL m_IsShowHP;
		char m_szBossName [ 0x14 ];
		BossModle m_BossModle;
		INT32 m_BossFvck;
		INT32 m_BossDef;
		INT32 m_BossHP;
		INT32 m_BossSpeed;
		INT32 m_BossHurt;
		INT32 m_BossStatus;
		INT32 m_BossY;
		INT32 m_BossX;
		INT32 m_44;

		public:

		INT32 GetIDFromClient ( )
		{
			return m_IDFromClient;
		}

		INT32 GetIDFromServer ( )
		{
			return m_IDFromServer;
		}

		BOOL GetIsShowHP ( )
		{
			return m_IsShowHP;
		}

		char* GetszBossName ( )
		{
			return m_szBossName;
		}

		BossModle GetBossModle ( )
		{
			return m_BossModle;
		}

		INT32 GetBossFvck ( )
		{
			return m_BossFvck;
		}

		INT32 GetBossDef ( )
		{
			return m_BossDef;
		}

		INT32 GetBossHP ( )
		{
			return m_BossHP;
		}

		INT32 GetBossSpeed ( )
		{
			return m_BossSpeed;
		}

		INT32 GetBossHurt ( )
		{
			return m_BossHurt;
		}

		INT32 GetBossStatus ( )
		{
			return m_BossStatus;
		}

		INT32 GetBossY ( )
		{
			return m_BossY;
		}

		INT32 GetBossX ( )
		{
			return m_BossX;
		}

	};

	enum 
	{
		//0x48
		CPVEBossInfoSize = sizeof ( CPVEBossInfo ),
	};
	static_assert( CPVEBossInfoSize == 0x48, "CPVEBossInfoSize is error" );
}