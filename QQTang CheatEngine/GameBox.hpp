/************************************************************************/
/* 
功能说明:墙壁
创建人:maple
创建日期:2014年9月7日
修改人:
修改日期:
*/
/************************************************************************/
#pragma once
#pragma  pack(1)
#include "Maple.hpp"
#define PGameBox CGameBox*

namespace QQTangCheatEngine
{
	__interface IGameBoxBase
	{
		void* DestroyBox ( bool Destroy ) ;
		bool InitBox ( ) ;
		bool InitFun ( ) ;
		void ExplodeBox ( ) ;
		INT32 GetBoxType ( ) ;
		LPVOID GetVoid ( ) ;
		char* GetName ( ) ;
		void UpDateBox ( INT32 Elapse ) ;
		void SetBoxXY ( INT16 x, INT16 y ) ;
		bool GetType ( INT32 value ) ;
		INT32 GetGridAttr ( INT32 X, INT32 Y ) ;
		bool CanThrough ( INT32 X, INT32 Y, PlayerDirection Direction ) ;
		bool PowerThrough ( INT32 X, INT32 Y, UINT8 Direction ) ;
		bool CanExplode ( ) ;
		bool CanMove ( ) ;
		void LoadUIByCreate ( ) ;
		void LoadUIByDestroy ( ) ;
		void LoadUIByMove ( INT16 X, INT16 Y,INT32 value ) ;
		void SmashBox ( INT32 value ) ;

	};

	class CGameBox :public IGameBoxBase
	{
		private:
		ItemByBox m_BoxID;
		CLocation m_BoxXY;
		INT32 m_LifeTime;

		INT32 m_0x10;
		INT32 m_0x14;
		INT32 m_0x18;
		INT32 m_0x1C;

		INT32 m_0x20;
		INT32 m_0x24;
		INT32 m_0x28;
		INT32 m_0x2C;

		INT32 m_0x30;
		INT32 m_0x34;
		INT32 m_0x38;
		INT32 m_0x3C;

		INT32 m_0x40;
		INT32 m_0x44;
		INT32 m_0x48;
		INT32 m_0x4C;

		INT32 m_0x50;
		INT32 m_0x54;
		INT32 m_0x58;
		INT32 m_0x5C;

		INT32  m_PushBox;
		INT32 m_0x64;
		INT32 m_0x68;
		INT32 m_0x6C;

		INT32 m_0x70;
		INT32 m_0x74;
		INT32 m_0x78;
		INT32 m_0x7C;




		public:
		CLocation* GetLocation ( )
		{
			return &m_BoxXY;
		}
		ItemByBox GetBoxID ( )
		{
			return m_BoxID;
		}
		INT32 GetLifeTime ( )
		{
			return m_LifeTime;
		}
		INT32 GetPushBox ( )
		{
			return m_PushBox;
		}
		//继承
		void* DestroyBox ( bool Destroy ){}
		bool InitBox ( ){}
		bool InitFun ( ){}
		void ExplodeBox ( ){}
		INT32 GetBoxType ( ){}
		LPVOID GetVoid ( ){}
		char* GetName ( ){}
		void UpDateBox ( INT32 Elapse ){}
		void SetBoxXY ( INT16 x, INT16 y ){}
		bool GetType ( INT32 value ){}		
		INT32 GetGridAttr ( INT32 X, INT32 Y ){}
		bool CanThrough ( INT32 X, INT32 Y, PlayerDirection Direction ){}
		bool PowerThrough ( INT32 X, INT32 Y, UINT8 Direction ){}
		bool CanExplode ( ){}
		bool CanMove ( ){}
		void LoadUIByCreate ( ){}
		void LoadUIByDestroy ( ){}
		void LoadUIByMove ( INT16 X, INT16 Y, INT32 value ){}
		void SmashBox ( INT32 value ){}
	};
	enum
	{
		//56
		CGameBoxSize = sizeof ( CGameBox ),
	};

	//检测CGAMEBOX大小
	static_assert( CGameBoxSize == 128, "CGameBoxSize is Error" );
}