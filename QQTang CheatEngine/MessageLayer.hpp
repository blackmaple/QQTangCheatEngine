/************************************************************************/
/* 
功能说明:消息层 通信
创建人:maple
创建日期:2014年9月3日
修改日期:
*/
/************************************************************************/
#pragma once
#pragma pack(1)
#include "Maple.hpp"
#include "QQTangClient.hpp"
#include "GameManager.hpp"
#include "QQTEncoder.hpp"
#include "QQTSection.hpp"
#define PMessageLayer CMessageLayer*

namespace QQTangCheatEngine
{
	class CToServerPackage
	{
		//size 3072
		public:
		GameID m_GameID;
		UINT8 m_byBuffer [ 0xBFC ];
		CToServerPackage ( _In_ GameID gameid )
		{
			m_GameID = gameid;
		}
	};

	class CMsg4Base
	{
		public:
		virtual void InitBaseA ( INT32 value ) = 0;
		virtual void InitBaseB ( INT32 value1, INT32 value2 ) = 0;
	};
 
	class CMessageLayerBase
	{
		public:

		virtual void InitFun1 ( LPVOID lpValue ) = 0;
		virtual void InitFun2 ( INT16 value1, INT16 value2 ) = 0;
		virtual void NotifyGameBegin ( LPVOID lpMsg ) = 0;
		virtual void GetDataFromServer ( DWORD dwMsgLength, LPVOID lpMsg ) = 0;
		virtual void GetDataFromPlayer ( DWORD dwMsgLength, LPVOID lpMsg ) = 0;
		virtual void InitFun3 ( INT32 value1, INT32 value2, INT32 vlaue3 ) = 0;
		virtual void UpdateUI ( ) = 0;
		virtual void AboutGame ( INT32 value1, INT32 value2 ) = 0;
		virtual void LoadMap ( MapID ID, INT32 value ) = 0;
		virtual void InitFun4 ( LPVOID lpValue ) = 0;
		virtual void InitMessageLayer ( bool value ) = 0;
		virtual void UpdateUIEx ( INT32 value ) = 0;
	};

	class CMessageLayer : public CMessageLayerBase
	{
		private:
		class CMsg4 : public CMsg4Base
		{
			private:
			UINT8 m_0x8 [ 0x5C0 ];

			public:
			void InitBaseA ( INT32 value )
			{
				return;
			}
			void InitBaseB ( INT32 value1, INT32 value2 )
			{
				return;
			}

		}m_Msg4;
		class CMsg5C8 :public IBaseClass
		{
			private:
			UINT8 m_0x5CC [ 0x17C ];
			//0x748
			INT32 m_TimeCount;
			public:
			void* InitBase ( bool Destroy ) { }
			INT32 GetTimeCount ( ) const
			{
				return m_TimeCount;
			}


		}m_Msg5C8;
		class CGameLayer :public IBaseClass
		{
			private:
			UINT8 m_0x750 [ 0x7C ];
			//0x7CC
			PQQTEncoder m_pQQTEncoder;
			//0x7D0
			PQQTSection m_pQQTSection;
			//0X7D4
			PGameManager m_pGameManager;

			INT32 m_0x7D8;

			public:
			void* InitBase ( bool Destroy ) { }

			PGameManager GetGameManager ( )
			{
				return m_pGameManager;
			}
			PQQTEncoder GetQQTEncoder ( )
			{
				return m_pQQTEncoder;
			}
			PQQTSection GetQQTSection ( )
			{
				return m_pQQTSection;
			}
		}m_GameLayer;
		class CMsg7DC :public IBaseClass
		{
			private:
			UINT8 m_7E0 [ 0x408 ];
			public:
			void* InitBase ( bool Destroy ) { }
		}m_Msg7DC [ 17 ];

		public:
		//继承
		void InitFun1 ( LPVOID lpValue ){}
		void InitFun2 ( INT16 value1, INT16 value2 ){}
		void NotifyGameBegin ( LPVOID lpMsg ){}
		void GetDataFromServer ( DWORD dwMsgLength, LPVOID lpMsg ){}
		void GetDataFromPlayer ( DWORD dwMsgLength, LPVOID lpMsg ){}
		void InitFun3 ( INT32 value1, INT32 value2, INT32 vlaue3 ){}
		void UpdateUI ( ){}
		void AboutGame ( INT32 value1, INT32 value2 ){}
		void LoadMap ( MapID ID, INT32 value ){}
		void InitFun4 ( LPVOID lpValue ){}
		void InitMessageLayer ( bool value ){}
		void UpdateUIEx ( INT32 value ){}

		//静态
		static PMessageLayer GetMessageLayer ( )
		{
			return ( PMessageLayer ) g_QQTangClient.m_MessageLayer;
		}

		PGameManager GetGameManager ( )
		{
			return m_GameLayer.GetGameManager ( );
		}

		template<typename T>
		void SetDataToServer ( _In_ GameID gameid, _In_ T& Package )
		{
			typedef void ( __thiscall *pSetDataToServer ) ( _In_ PMessageLayer ThisClass, _In_ GameID gameid, _In_ T& Package );
			pSetDataToServer pToServer = ( pSetDataToServer ) ( g_QQTangClient.m_DataToServer );
			pToServer ( this, gameid, Package );
		}

		 
		void SetDataToServerEx ( _In_ volatile GameID gameid, _In_ volatile LPVOID Package )
		{
			if ( NULL == this->m_GameLayer.GetQQTSection ( ) )
			{
				return;
			}

			CToServerPackage ToServerPackage ( gameid );

			DWORD dwPackageSize = 0;

			this->m_GameLayer.GetQQTEncoder ( )->EnCoder (
				this->m_GameLayer.GetQQTEncoder ( ),
				gameid, ToServerPackage.m_byBuffer,
				&dwPackageSize, Package, TRUE );

			this->m_GameLayer.GetQQTSection ( )->SendDataToServer ( dwPackageSize + 4, &ToServerPackage );
		}

		template<typename T>
		void SetDataToClient (_In_ GameID gameid,_In_ T& Package )
		{
			typedef void ( __thiscall * pSetDataToClient )( _In_ PMessageLayer ThisClass, _In_ GameID gameid, _In_ T& Package );
			pSetDataToClient pToPlayer = ( pSetDataToClient ) ( g_QQTangClient.m_DataToClient );
			pToPlayer ( this, gameid, Package );
		}

		UINT32 GetTimeSub ( )
		{
			typedef UINT32 ( __thiscall *pGetTimeSub )( CMsg5C8* ThisClass );
			pGetTimeSub  pGet = ( pGetTimeSub ) ( g_QQTangClient.m_GetTimeSub );
			return pGet ( &this->m_Msg5C8 );
		}

	};
	enum
	{
		//19624
		CMessageLayerSize = sizeof ( CMessageLayer )
	};
}
