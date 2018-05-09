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
#define PQQTSection CQQTSection*


namespace QQTangCheatEngine
{
	class CQQTSectionBase
	{
		virtual void Fun_00 ( INT32 a ) = 0;
		virtual void SendDataToServer ( _In_ INT32 PackageSize, _In_ LPVOID pPackage ) = 0;
		virtual void Fun_02 ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void Fun_03 ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) = 0;
		virtual void Fun_04 ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void Fun_05 ( INT32 a ) = 0;
		virtual void Fun_06 ( INT32 a ) = 0;
		virtual void Fun_07 ( INT32 a ) = 0;
		virtual void Fun_08 ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) = 0;
		virtual void Fun_09 ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void Fun_10 ( INT32 a, INT32 b ) = 0;
		virtual void Fun_11 ( INT32 a, INT32 b ) = 0;
		virtual void Fun_12 ( INT32 a ) = 0;
		virtual void Fun_13 ( INT32 a, INT32 b ) = 0;
		virtual void Fun_14 ( INT32 a ) = 0;
		virtual void Fun_15 ( INT32 a ) = 0;
		virtual void Fun_16 ( INT32 a ) = 0;
		virtual void Fun_17 ( ) = 0;
		virtual void Fun_18 ( ) = 0;
		virtual void Fun_19 ( INT32 a ) = 0;
		virtual void Fun_20 ( INT32 a, INT32 b ) = 0;
		virtual void Fun_21 ( INT32 a ) = 0;
		virtual void Fun_22 ( ) = 0;
		virtual void Fun_23 ( INT32 a, INT32 b ) = 0;
		virtual void Fun_24 ( INT32 a, INT32 b ) = 0;
		virtual void Fun_25 ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void Fun_26 ( ) = 0;
   

	};

	class CQQTSection :public CQQTSectionBase
	{
		public:
		void Fun_00 ( INT32 a ) {}
		void SendDataToServer ( _In_ INT32 PackageSize, _In_ LPVOID pPackage ) { }
		void Fun_02 ( INT32 a, INT32 b, INT32 c ) {}
		void Fun_03 ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) {}
		void Fun_04 ( INT32 a, INT32 b, INT32 c ) {}
		void Fun_05 ( INT32 a ) {}
		void Fun_06 ( INT32 a ) {}
		void Fun_07 ( INT32 a ) {}
		void Fun_08 ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) {}
		void Fun_09 ( INT32 a, INT32 b, INT32 c ) {}
		void Fun_10 ( INT32 a, INT32 b ) {}
		void Fun_11 ( INT32 a, INT32 b ) {}
		void Fun_12 ( INT32 a ) {}
		void Fun_13 ( INT32 a, INT32 b ) {}
		void Fun_14 ( INT32 a ) {}
		void Fun_15 ( INT32 a ) {}
		void Fun_16 ( INT32 a ) {}
		void Fun_17 ( ) {}
		void Fun_18 ( ) {}
		void Fun_19 ( INT32 a ) {}
		void Fun_20 ( INT32 a, INT32 b ) {}
		void Fun_21 ( INT32 a ) {}
		void Fun_22 ( ) {}
		void Fun_23 ( INT32 a, INT32 b ) {}
		void Fun_24 ( INT32 a, INT32 b ) {}
		void Fun_25 ( INT32 a, INT32 b, INT32 c ) {}
		void Fun_26 ( ) {}
	};
}

