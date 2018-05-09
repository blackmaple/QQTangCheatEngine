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
#include "QQTEncoder.hpp"
#include "QQTangPackage.hpp"

#define PRoomInfo CRoomInfo*
#define PRoom CRoom*
namespace QQTangCheatEngine
{
	class CRoom4Base
	{
		//48 个fun
		virtual void Fun00 ( ) = 0;
		virtual void Fun01 ( ) = 0;
		virtual void Fun02 ( ) = 0;
		virtual void Fun03 ( ) = 0;
		virtual void Fun04 ( ) = 0;
		virtual void Fun05 ( ) = 0;
		virtual void Fun06 ( ) = 0;
		virtual void Fun07 ( ) = 0;
		virtual void Fun08 ( ) = 0;
		virtual void Fun09 ( ) = 0;

		virtual void Fun10 ( ) = 0;
		virtual void Fun11 ( ) = 0;
		virtual void Fun12 ( ) = 0;
		virtual void Fun13 ( ) = 0;
		virtual void Fun14 ( ) = 0;
		virtual void Fun15 ( ) = 0;
		virtual void Fun16 ( ) = 0;
		virtual void Fun17 ( ) = 0;
		virtual void Fun18 ( ) = 0;
		virtual void Fun19 ( ) = 0;

		virtual void Fun20 ( ) = 0;
		virtual void Fun21 ( ) = 0;
		virtual void Fun22 ( ) = 0;
		virtual void Fun23 ( ) = 0;
		virtual void Fun24 ( ) = 0;
		virtual void Fun25 ( ) = 0;
		virtual void Fun26 ( ) = 0;
		virtual void Fun27 ( ) = 0;
		virtual void Fun28 ( ) = 0;
		virtual void Fun29 ( ) = 0;

		virtual void Fun30 ( ) = 0;
		virtual void Fun31 ( ) = 0;
		virtual void Fun32 ( ) = 0;
		virtual void Fun33 ( ) = 0;
		virtual void Fun34 ( ) = 0;
		virtual void Fun35 ( ) = 0;
		virtual void Fun36 ( ) = 0;
		virtual void Fun37 ( ) = 0;
		virtual void Fun38 ( ) = 0;
		virtual void Fun39 ( ) = 0;

		virtual void Fun40 ( ) = 0;
		virtual void Fun41 ( ) = 0;
		virtual void Fun42 ( ) = 0;
		virtual void Fun43 ( ) = 0;
		virtual void Fun44 ( ) = 0;
		virtual void Fun45 ( ) = 0;
		virtual void Fun46 ( ) = 0;
		virtual void Fun47 ( ) = 0;

		public:
	};
	class CRoomInfoBase
	{
		public:
		virtual void FunA ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void FunB ( INT32 a ) = 0;
		virtual void FunC ( INT32 a ) = 0;
		virtual void FunD ( INT32 a, INT32 b ) = 0;

		virtual void FunE ( INT32 a ) = 0;
		virtual void FunF ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f, INT32 g ) = 0;
		virtual void FunG ( INT32 a ) = 0;
		virtual void FunH ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) = 0;

		virtual void FunI ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void SendDataToClient ( LPVOID pRoomInfo, DWORD dwPackageSize, LPVOID pPackage, INT32 PackageType ) = 0;

		virtual void FunK ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f ) = 0;
		virtual void FunL ( INT32 a, INT32 b, INT32 c, INT32 d ) = 0;
		virtual void FunM ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void FunN ( INT32 a, INT32 b, INT32 c, INT32 e, INT32 f ) = 0;
		virtual void FunO ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f ) = 0;
		virtual void FunP ( INT32 a, INT32 b, INT32 c ) = 0;
		virtual void FunQ ( INT32 a, INT32 b ) = 0;
		virtual void FunR ( INT32 a ) = 0;
		virtual void FunS ( INT32 a, INT32 b, INT32 c, INT32 e, INT32 f ) = 0;

	};

	class CCBase
	{
		public:
		virtual void Fun_1 ( ) = 0;
		virtual void Fun_2 ( INT32 a ) = 0;
		virtual void Fun_3 ( INT32 A ) = 0;
		virtual void Fun_4 ( ) = 0;
		virtual void Fun_5 ( INT32 A ) = 0;
		virtual void Fun_6 ( ) = 0;
		virtual void Fun_7 ( ) = 0;
		virtual void Fun_8 ( ) = 0;
		virtual void Fun_9 ( ) = 0;
		virtual void Fun_A ( INT32 A ) = 0;
		virtual void Fun_B ( INT32 A ) = 0;
		virtual void Fun_C ( ) = 0;
		virtual void Fun_D ( ) = 0;
		virtual void Fun_E ( ) = 0;
		virtual void Fun_F ( INT32 A ) = 0;
		virtual void Fun_G ( ) = 0;
		virtual void Fun_H ( ) = 0;
		virtual void Fun_I ( ) = 0;

	};
	class C4Base
	{
		public:
		virtual void FunG ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) = 0;
		virtual void FunH ( ) = 0;
		virtual void FunI ( INT32 A ) = 0;
	};

	class CPlayerInfoInRoomBase
	{
		public:
		virtual void FunA ( ) = 0;
		virtual void FunB ( INT32 a, INT32 b ) = 0;
		virtual void FunC ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f, INT32 g ) = 0;
		virtual void FunD ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) = 0;
		virtual void FunE ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) = 0;
		virtual void FunF ( INT32 a ) = 0;
	};

	class CRoomInfo :public CRoomInfoBase
	{
		private:
		class CRoom4 :public CRoom4Base
		{
			private:
			INT32 m_0x8;
			INT32 m_0xC;
			INT32 m_0x10;
			INT32 m_0x14;
			INT32 m_0x18;
			INT32 m_0x1C;
			public:
			void Fun00 ( ) { }
			void Fun01 ( ) { }
			void Fun02 ( ) { }
			void Fun03 ( ) { }
			void Fun04 ( ) { }
			void Fun05 ( ) { }
			void Fun06 ( ) { }
			void Fun07 ( ) { }
			void Fun08 ( ) { }
			void Fun09 ( ) { }

			void Fun10 ( ) { }
			void Fun11 ( ) { }
			void Fun12 ( ) { }
			void Fun13 ( ) { }
			void Fun14 ( ) { }
			void Fun15 ( ) { }
			void Fun16 ( ) { }
			void Fun17 ( ) { }
			void Fun18 ( ) { }
			void Fun19 ( ) { }

			void Fun20 ( ) { }
			void Fun21 ( ) { }
			void Fun22 ( ) { }
			void Fun23 ( ) { }
			void Fun24 ( ) { }
			void Fun25 ( ) { }
			void Fun26 ( ) { }
			void Fun27 ( ) { }
			void Fun28 ( ) { }
			void Fun29 ( ) { }

			void Fun30 ( ) { }
			void Fun31 ( ) { }
			void Fun32 ( ) { }
			void Fun33 ( ) { }
			void Fun34 ( ) { }
			void Fun35 ( ) { }
			void Fun36 ( ) { }
			void Fun37 ( ) { }
			void Fun38 ( ) { }
			void Fun39 ( ) { }

			void Fun40 ( ) { }
			void Fun41 ( ) { }
			void Fun42 ( ) { }
			void Fun43 ( ) { }
			void Fun44 ( ) { }
			void Fun45 ( ) { }
			void Fun46 ( ) { }
			void Fun47 ( ) { }
		}m_Room4;
		class CRoom20
		{
			private:
			INT32 m_20;
			INT32 m_24;
			INT32 m_28;
			INT32 m_2C;
			INT32 m_30;
			INT32 m_34;
			INT32 m_38;

			INT32 m_3C;
			INT32 m_40;
			INT32 m_44;
			INT32 m_48;
			INT32 m_4C;
			INT32 m_50;
			INT32 m_54;
			INT32 m_58;
			INT32 m_5C;
			INT32 m_60;
			INT32 m_64;
			INT32 m_68;
			public:
		}m_Room20;
		class CPlayerInfoInRoom :public CPlayerInfoInRoomBase
		{
			private:
			class C4 :public C4Base
			{
				private:
				INT32 m_0x8;
				class CC :public CCBase
				{
					private:
					INT32 m_0x10;
					INT8 m_0x14 [ 0x400 ];
					INT16 m_0x414;
					INT16 m_0x416;
					INT32 m_0x418;
					INT32 m_0x41C;
					INT16 m_0x420;
					INT16 m_0x422;
					CIpAddress m_IP;
					INT16 m_Port;
					INT16 m_0x42A;


					public:
					void Fun_1 ( ) { }
					void Fun_2 ( INT32 a ) { }
					void Fun_3 ( INT32 A ) { }
					void Fun_4 ( ) { }
					void Fun_5 ( INT32 A ) { }
					void Fun_6 ( ) { }
					void Fun_7 ( ) { }
					void Fun_8 ( ) { }
					void Fun_9 ( ) { }
					void Fun_A ( INT32 A ) { }
					void Fun_B ( INT32 A ) { }
					void Fun_C ( ) { }
					void Fun_D ( ) { }
					void Fun_E ( ) { }
					void Fun_F ( INT32 A ) { }
					void Fun_G ( ) { }
					void Fun_H ( ) { }
					void Fun_I ( ) { }
					CIpAddress* GetIP ( )
					{
						return &m_IP;
					}
					INT16 GetPort ( )
					{
						return m_Port;
					}
				}m_0xC;
				INT32 m_0x42C;
				INT32 m_0x430;
				INT32 m_0x434;
				INT16 m_0x438;
				INT16 m_0x43A;
				public:
				void FunG ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) { }
				void FunH ( ) { }
				void FunI ( INT32 A ) { }
			}m_C4;
			INT32 m_0x43C;
			INT32 m_0x440;
			INT32 m_0x444;
			INT32 m_0x448;
			INT32 m_0x44C;
			INT32 m_0x450;
			INT32 m_0x454;
			INT32 m_0x458;
			INT16 m_0x45C;
			INT16 m_0x45E;
			INT32 m_0x460;
			INT32 m_0x464;
			INT32 m_0x468;
			INT32 m_0x46C;
			INT16 m_0x470;
			INT16 m_0x472;
			INT32 m_0x474;
			INT16 m_0x478;
			INT16 m_0x47A;
			INT32 m_0x47C;
			INT32 m_0x480;
			INT16 m_0x484;
			INT16 m_0x486;
			//0x488
			class C488
			{
				INT32 m_0x488;
				INT32 m_0x48C;

				INT32 m_0x490;
				INT32 m_0x494;
				INT32 m_0x498;
				INT32 m_0x49C;

				INT32 m_0x4A0;
				INT32 m_0x4A4;
				INT32 m_0x4A8;
				INT32 m_0x4AC;

				INT32 m_0x4B0;
				INT32 m_0x4B4;
				INT32 m_0x4B8;
				INT32 m_0x4BC;

				INT32 m_0x4C0;
				INT32 m_0x4C4;
				INT32 m_0x4C8;
				INT32 m_0x4CC;



				//0x4D0
				UINT32 m_PlayerQQ;
				//0x4D4
				INT16 m_IDFromServer;
				INT16 m_0x4D6;
				INT8 m_0x4D8 [ 0x3FB0 ];
				INT32 m_0x4000;
				INT32 m_0x4004;
				public:
				//0x4D0
				UINT32 GetPlayerQQ ( )
				{
					return m_PlayerQQ;
				}
				//0x4D4
				INT16 GetIDFromServer ( )
				{
					return m_IDFromServer;
				}
			}m_0x488;
			//0x4490
			class C4490
			{
				INT8 m_4490 [ 0x400 ];
				INT32 m_4890;
				INT16 m_4894;
				INT16 m_4896;

			}m_0x4490;

			INT32 m_0x4898;
			INT32 m_0x489C;
			INT16 m_0x48A0;
			INT8 m_0x48A2 [ 0x284 ];
			INT16 m_0x4B26;

			public:
			void FunA ( ) { }
			void FunB ( INT32 a, INT32 b ) { }
			void FunC ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f, INT32 g ) { }
			void FunD ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) { }
			void FunE ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) { }
			void FunF ( INT32 a ) { }

			template<typename T>
			void SendDataToPlayer ( _In_ T& Package )
			{
				typedef void ( __thiscall *pSendDataToPlayer )
					(
					_In_ CPlayerInfoInRoom* ThisClass,
					_In_ DWORD dwPackageSize,
					_In_ T& package
					);
				pSendDataToPlayer pToPlayer = ( pSendDataToPlayer ) ( g_QQTangClient.m_SendDataToPlayer );
				pToPlayer ( this, sizeof ( T ), Package );
			}

			template<typename T>
			void CheckDataToServer
				(
				_In_ T& CheckDataPackage,
				_In_ CALLPLAYERINFOINROOM&  AllPlayerInfoInRoom
				)
			{
				typedef void ( __thiscall *pCheckDataToServer )
					(
					_In_ CPlayerInfoInRoom* ThisClass,
					_In_ DWORD dwPackageSize,
					_In_ T& CkPackage,
					_In_ CAllPlayerInfoInRoom& AllPlayerPackage
					);

				pCheckDataToServer pToServer = ( pCheckDataToServer ) ( g_QQTangClient.m_CheckDataToServer );
				pToServer ( this, sizeof ( T ), CheckDataPackage, AllPlayerInfoInRoom );
			}
		}m_PlayerInfoInRoom [ 8 ];



		public:
		CPlayerInfoInRoom* GetPlayerInfoInRoom ( )
		{
			return m_PlayerInfoInRoom;
		}

		void FunA ( INT32 a, INT32 b, INT32 c ) { }
		void FunB ( INT32 a ) { }
		void FunC ( INT32 a ) { }
		void FunD ( INT32 a, INT32 b ) { }
		void FunE ( INT32 a ) { }
		void FunF ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f, INT32 g ) { }
		void FunG ( INT32 a ) { }
		void FunH ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e ) { }
		void FunI ( INT32 a, INT32 b, INT32 c ) { }
		void SendDataToClient ( LPVOID pRoomInfo, DWORD dwPackageSize, LPVOID pPackage, INT32 PackageType )
		{
		}

		void FunK ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f ) { }
		void FunL ( INT32 a, INT32 b, INT32 c, INT32 d ) { }
		void FunM ( INT32 a, INT32 b, INT32 c ) { }
		void FunN ( INT32 a, INT32 b, INT32 c, INT32 e, INT32 f ) { }
		void FunO ( INT32 a, INT32 b, INT32 c, INT32 d, INT32 e, INT32 f ) { }
		void FunP ( INT32 a, INT32 b, INT32 c ) { }
		void FunQ ( INT32 a, INT32 b ) { }
		void FunR ( INT32 a ) { }
		void FunS ( INT32 a, INT32 b, INT32 c, INT32 e, INT32 f ) { }
	};

	class CRoom :public IBaseClass
	{
		private:
		class CRoomHeader
		{
			private:
			UINT8  m_0x0 [ 0x230 ];
			LPVOID m_PlayerInfo [ 0x2E ];
			UINT8 m_MySelfNO;
			UINT8 m_bytes [ 3 ];
			DWORD m_2EC;
			DWORD m_2F0;
			DWORD m_2F4;
			DWORD m_2F8;
			DWORD m_2FC;
			DWORD m_300;
			DWORD m_304;
			DWORD m_308;
			PRoomInfo m_pRoomInfo;
			PQQTEncoder m_pQQTEncoder;
			public:
			PRoomInfo GetRoomInfo ( )
			{
				return m_pRoomInfo;
			}
			PQQTEncoder GetQQTEncoder ( )
			{
				return m_pQQTEncoder;
			}
			UINT8 GetMeSelfNO ( )
			{
				return m_MySelfNO;
			}
		}*m_RoomHeader;
		public:
		static CRoom* GetRoom ( )
		{
			return ( CRoom* ) ( *( PUINT32 ) ( g_QQTangClient.m_Room ) );
		}
		CRoomHeader* GetRoomHeader ( )
		{
			return m_RoomHeader;
		}
		PRoomInfo GetRoomInfo ( )
		{
			return m_RoomHeader->GetRoomInfo ( );
		}
		PQQTEncoder GetQQTEncoder ( )
		{
			return m_RoomHeader->GetQQTEncoder ( );
		}

		template<typename T>
		void SetDataToClientInRoom ( GameID gameid, T& GamePackage)
		{
			if ( GetQQTEncoder ( ) == 0 || GetRoomInfo ( ) == 0 )
			{
				return;
			}
			CSendPackageInRoom* pSendPackage = new CSendPackageInRoom ( );
			PUINT8 pPackage = new UINT8 [ 0x1000 ];
			if ( pSendPackage == NULL || pPackage == NULL )
			{
				return;
			}
			memset ( pSendPackage, NULL, sizeof ( CSendPackageInRoom ) );
			pSendPackage->m_GameID = ( INT16 ) gameid;
			pSendPackage->m_Length = sizeof(T);
			pSendPackage->m_GetTickCount = GetTickCount ( );
			pSendPackage->m_SendCount = 1;
			memcpy ( pSendPackage->m_byPackage, &GamePackage, sizeof ( T ) );
			
			DWORD PackageLength;
			if ( GetQQTEncoder ( )->EnCoder (
				GetQQTEncoder ( ), GameID::D2E_ENCODE, pPackage,
				&PackageLength, pSendPackage, TRUE ) < 0 )
			{
				return;
			}
			GetRoomInfo ( )->SendDataToClient ( GetRoomInfo ( ), PackageLength, pPackage, 2 );
			delete pSendPackage;
			delete [ ] pPackage;
		}

		template<typename T>
		void SetDataToClientInGame ( GameID gameid, T& GamePackage )
		{
			if ( GetQQTEncoder ( ) == 0 || GetRoomInfo ( ) == 0 )
			{
				return;
			}
		}
		void* InitBase ( bool Destroy ) { return NULL; }

	};



}

