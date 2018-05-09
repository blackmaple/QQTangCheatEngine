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
#define PGameFloor CGameFloor*

namespace QQTangCheatEngine
{
	__interface IGameFloorBase
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
		  void LoadUIByMove ( INT16 X, INT16 Y, INT32 value ) ;
		  void SmashBox ( INT32 value ) ;

	};

	class CGameFloor :public IGameFloorBase
	{
		private:
		ItemByFloor m_FloorID;
		CLocation m_FloorXY;
		INT32 m_LifeTime;
		INT32 m_param1;
		LPVOID m_P1;
		LPVOID m_P2;
		LPVOID m_P3;
		LPVOID m_P4;
		LPVOID m_P5;
		LPVOID m_P6;
		LPVOID m_P7;
		LPVOID m_P8;
		LPVOID m_P9;

		public:
		CLocation* GetLocation ( )
		{
			return &m_FloorXY;
		}
		INT32 GetFloorID ( )
		{
			return m_FloorID;
		}
		INT32 GetLifeTime ( )
		{
			return m_LifeTime;
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
		INT32 GetGridAttr ( INT16 X, INT16 Y ) { }
		bool CanThrough ( INT16 X, INT16 Y, PlayerDirection Direction ) { }
		bool PowerThrough ( INT16 X, INT16 Y, UINT8 Direction ) { }
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
		CGameFloorSize = sizeof ( CGameFloor ),
	};

	//检测CGAMEBOX大小
	static_assert( CGameFloorSize == 56, "CGameFloorSize is Error" );

}
