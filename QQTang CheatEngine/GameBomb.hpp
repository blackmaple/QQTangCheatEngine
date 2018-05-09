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
#include "maple.hpp"
#define PGameBomb CGameBomb*

namespace QQTangCheatEngine
{
	__interface IGameBombBase
	{
		void* InitBase ( bool Destroy );
		bool CanBomb ( );
		void FUNA ( );
		bool CanBombEx ( );
		INT32 GetStatus ( );
		void Update ( INT32 Elapse );
		void SetBomb ( );
		void SetStatus ( );
	};
	class CGameBomb :public IGameBombBase
	{

		INT32 m_BombStyle;//0x4
		UINT32 m_pBombItemA;//0x8
		UINT32 m_pBombItemB;//0xC
		UINT32 m_pBombItemC;//0x10
		//?
		UINT32 m_pBombItemD;//0x14
		UINT32 m_pBombItemE;//0x18

		INT16 m_BomberID;//0x1C
		INT16 m_BombPower;//0x1e

		UINT32 m_pBombItemG;//0x20
		INT32 m_GameTime;//0x24
		CLocation m_BombXY;//0x28

		BombStatus m_Status;//0x2C
		INT32 m_ExplodeTime;//0x30
		UINT32 m_pBombItemL;//0x34
		UINT32 m_pBombItemM;//0x38
		UINT32 m_pBombItemN;//0x3C
		UINT32 m_pBombItemO;//0x40

		public:
		INT32 GetBombStyle ( ) const
		{
			return m_BombStyle;
		}
		INT16 GetBomberID ( )const
		{
			return m_BomberID;
		}
		INT16 GetBombPower ( ) const
		{
			return m_BombPower;
		}
		INT32 GetGameTime ( ) const
		{
			return m_GameTime;
		}
		CLocation* GetBombXY ( )
		{
			return &m_BombXY;
		}
		BombStatus GetBombStatus ( ) const
		{
			return ( BombStatus ) ( m_Status & 0x00000FF );
		}
		INT32 GetExplodeTime ( ) const
		{
			return m_ExplodeTime;
		}

		//虚函数
		void* InitBase ( _In_ bool Destroy )
		{ }
		bool CanBomb ( )
		{ }
		void FUNA ( )
		{ }
		bool CanBombEx ( )
		{ }
		INT32 GetStatus ( )
		{ }
		void Update ( _In_ INT32 Elapse )
		{ }
		void SetBomb ( )
		{ }
		void SetStatus ( )
		{ }

	};

	enum
	{
		CGameBombSize = sizeof ( CGameBomb ) ,
	};
	static_assert( CGameBombSize == 0x44 , "CGameBombSize is error" );
}
