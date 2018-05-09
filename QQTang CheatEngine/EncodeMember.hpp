/************************************************************************/
/* 
功能说明:部分道具信息加解密
创建人:maple
创建日期:2014年9月2日
修改人:
修改日期:
*/
/************************************************************************/

#pragma once
#pragma pack(1)
#include "Maple.hpp"
#define  CEncodeMember CEncodeMemberEx<INT32>
#define  PEncodeMember CEncodeMemberEx<INT32>*
#define  CEncodeINT16 CEncodeMemberEx<INT16>
#define  PEncodeINT16 CEncodeMemberEx<INT16>*

namespace QQTangCheatEngine
{ 
	template<typename T>
	class CEncodeMemberEx
	{
		private:

		T m_EncodeMember;

		UINT8 m_EncodeEnable;

		T m_EncodeMemberKey;

		UINT8 m_bytes [ 0xB ];

		public:

		CEncodeMemberEx ( T EncodeMember, T  EncodeMemberKey )
		{
			m_EncodeMember = EncodeMember;
			m_EncodeMemberKey = EncodeMemberKey;
		}

		//结果大于0x1234 尝试xor 0x1234
		T GetValue ( _In_ BOOL XOR = FALSE )
		{
			T nEncode = m_EncodeMember;

			CQQTangClient::Algorithm (
				( const PINT8 ) &m_EncodeMemberKey,
				FALSE, ( PINT8 ) &nEncode, sizeof ( T ) );

			if ( XOR )
			{
				nEncode ^= 0x1234;
			}
			return nEncode;
		}

		void SetValue ( _In_ T Value, _In_ BOOL XOR = FALSE )
		{
			if ( XOR )
			{
				Value ^= 0x1234;
			}
			CQQTangClient::Algorithm (
				( const PINT8 ) &m_EncodeMemberKey,
				TRUE, ( PINT8 ) &Value, sizeof ( T ) );
			m_EncodeMember = Value;
		}

		operator T( )
		{
			return GetValue ( );
		}

		CEncodeMemberEx& operator = ( _In_ T value )
		{
			SetValue ( value );
			return *this;
		}

		T GetEncodeMember()
		{
			return m_EncodeMember;
		}

		UINT8 GetEncodeEnable()
		{
			return m_EncodeEnable;
		}

		T GetEncodeMemberKey()
		{
			return m_EncodeMemberKey;
		}

	};

	enum
	{
 		CEncodeMemberExSize = sizeof ( CEncodeMemberEx <INT32 >),
	};
	static_assert( CEncodeMemberExSize == 20, "CEncodeMemberExSize is Error" );
}