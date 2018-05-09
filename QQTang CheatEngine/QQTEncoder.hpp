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
#define PQQTEncoder CQQTEncoder*

namespace QQTangCheatEngine
{
	class CQQTEncoderBase
	{
		public:
		virtual void FunA ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void FunB ( INT32 a ) = 0;
		virtual void FunC ( INT32 a ) = 0;
		virtual DWORD FunD ( INT32 a, INT32 b ) = 0;
		virtual INT32 EnCoder (
			_In_ LPVOID pQQTEncoder,
			_In_ GameID gameid,
			_Out_ LPVOID pEnPackage,
			_Out_ LPDWORD pEncodeSize,
			_In_ LPVOID pDePackage,
			_In_ BOOL IsEncode ) = 0;

		virtual INT32 ToNetValue (
			_In_ LPVOID pQQTEncoder,
			_In_ GameID gameid,
			_Out_ LPVOID pEnPackage,
			_Out_ PDWORD pEncodeSize,
			_In_ LPVOID pDePackage,
			_In_ BOOL IsEncode ) = 0;

		virtual DWORD FunE ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) = 0;
	};

	class CQQTEncoder :public CQQTEncoderBase
	{
		public:
		void FunA ( INT32 a, INT32 b, INT32 c ) { }
		void FunB ( INT32 a ) { }
		void FunC ( INT32 a ) { }
		DWORD FunD ( INT32 a, INT32 b ) { }
		INT32 EnCoder (
			_In_ LPVOID pQQTEncoder,
			_In_ GameID gameid,
			_Out_ LPVOID pEnPackage,
			_Out_ LPDWORD pEncodeSize,
			_In_ LPVOID pDePackage,
			_In_ BOOL IsEncode )
		{
		}

		INT32 ToNetValue (
			_In_ LPVOID pQQTEncoder,
			_In_ GameID gameid,
			_Out_ LPVOID pEnPackage,
			_Out_ PDWORD pEncodeSize,
			_In_ LPVOID pDePackage,
			_In_ BOOL IsEncode )
		{
		}


		DWORD FunE ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) { }

	};

}