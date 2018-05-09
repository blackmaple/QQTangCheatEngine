/************************************************************************/
/*
功能说明:预编译头文件
创建人:Maple
创建日期:2014年9月1日
修改日期:
*/
/************************************************************************/
#pragma once
#pragma pack(1)


#include <WinSDKVer.h>
//最低平台XP
#define _WIN32_WINNT _WIN32_WINNT_WINXP 
#include <SDKDDKVer.h>
//取消不常用的头文件
#define WIN32_LEAN_AND_MEAN

#include <windows.h>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <cassert>
using namespace std;

#include "QQTangEnum.hpp"
#include "EncodeMember.hpp"
#define PItemBySet CItemBySet*
//C# var - - C++ 11
#define var auto

namespace QQTangCheatEngine
{	
	//接口
	__interface IBaseClass
	{
		void* InitBase ( bool Destroy );
	};

	class CLocation
	{
		private:
		short m_y;
		short m_x;
		public:
		CLocation ( ) { }
		CLocation (INT16 x, INT16 y )
		{
			m_y = y;
			m_x = x;
		}
		short GetX ( )const
		{
			return m_x;
		}
		short GetY ( ) const
		{
			return m_y;
		}
		short GetPlayerX ()const
		{ 
			INT16 x = m_x * 4 + m_x;
			return x * 8 + 20;
		}
		short GetPlayerY ( )const
		{
			INT16 y = m_y * 4 + m_y;
			return y * 8 + 20;
		}
		void SetX ( INT16 x )
		{
			m_x = x;
		}
		void SetY ( INT16 y )
		{
			m_y = y;
		}
		CLocation& operator = ( CLocation& Location )
		{
			m_x = Location.GetX ( );
			m_y = Location.GetY ( );
			return *this;
		}
		 

	}; 

	template<class X>
	class CMapX
	{
		public:
		union 
		{
			X m_ID;
			X m_pInfo;
		};


	};
 
	template<class Y>
	class CMapY
	{
		public:
		CMapX<Y>*  m_MapX;
	};
 
 
	template<class T>
	class CVector
	{
		private:
		//好像从2012 vector size 优化变小了
#if _MSC_VER > 1600 
		INT32 m_value;
#endif
		vector<T> m_vecInfo;
		public:
		vector<T>* GetVecInfo ( )
		{
			return &m_vecInfo;
		}
	};
	enum 
	{
		CVectorSize = sizeof ( CVector <INT32>),
	};

	class CIpAddress
	{
		private:
		union 
		{
			UINT32 m_IP;
			struct 
			{
				UINT8 m_a;
				UINT8 m_b;
				UINT8 m_c;
				UINT8 m_d;
			};
		};
		public:
		UINT32 GetIP ( )const
		{
			return m_IP;
		}
		INT32 GetIP ( _Inout_ char* szIP )
		{
			return wsprintf ( szIP, "%d.%d.%d.%d", m_a, m_b, m_c, m_d );
		}
	};

	//注意 这里他是加密的
	class CItemBySet
	{
		private:
		CEncodeMember m_ItemID;
		CEncodeMember m_ItemSize;
		//eq -1?
		CEncodeMember m_ConstFF;
		public:
		CEncodeMember& GetItemID ( )
		{
			return m_ItemID;
		}
		CEncodeMember& GetItemSize ( )
		{
			return m_ItemSize;
		}

	};

	//注意 这里他妈不加密了 换码农了就这样
	class CItemByDrop
	{
		private:
		ItemByGame m_ItemID;
		union
		{
			INT32 m_ItemSizeInfo;
			struct
			{
				INT16 m_ItemSize;
				INT16 m_Alignment;
			};
		};
		public:

		ItemByGame GetItemID ( )
		{
			return m_ItemID;
		}
		INT16  GetItemSize ( )
		{
			return m_ItemSize;
		}

        BOOL IsPropToServer ( )
        {
            switch ( m_ItemID )
            {
                //81
                case QQTangCheatEngine::GAME_TONGBI:
                {
                    return TRUE;
                }
                //82
                case QQTangCheatEngine::GAME_YINBI:
                {
                    return TRUE;
                }
                //83
                case QQTangCheatEngine::GAME_JINBI:
                {
                    return TRUE;
                }
                //84
                case QQTangCheatEngine::GAME_QIANDAI:
                {
                    return TRUE;
                }
                //85
                case QQTangCheatEngine::GAME_BAOXIANG1000TB:
                {
                    return TRUE;
                }
                //91
                case QQTangCheatEngine::GAME_HONGZUANSHI:
                {
                    return TRUE;
                }
                //92
                case QQTangCheatEngine::GAME_LANZUANSHI:
                {
                    return TRUE;
                }
                //211
                case QQTangCheatEngine::GAME_ZIZUANSHI:
                {
                    return TRUE;
                }
                //212
                case QQTangCheatEngine::GAME_XUEPINGZI:
                {
                    return TRUE;
                }
                //213
                case QQTangCheatEngine::GAME_HUANGLUOSI:
                {
                    return TRUE;
                }
                //93
                case QQTangCheatEngine::GAME_TANGBI1000:
                {
                    return TRUE;
                }
                //94
                case QQTangCheatEngine::GAME_TANGBI500:
                {
                    return TRUE;
                }
                //86
                case QQTangCheatEngine::GAME_JINGYAN20:
                {
                    return TRUE;
                }
                //87
                case QQTangCheatEngine::GAME_JINGYAN50:
                {
                    return TRUE;
                }
                //88
                case QQTangCheatEngine::GAME_JINGYAN100:
                {
                    return TRUE;
                }
                //89
                case QQTangCheatEngine::GAME_JINGYAN200:
                {
                    return TRUE;
                }
                //96
                case QQTangCheatEngine::GAME_MEIGUI1:
                {
                    return TRUE;
                }
                //97
                case QQTangCheatEngine::GAME_LVSHUIJING:
                {
                    return TRUE;
                }
                //98
                case QQTangCheatEngine::GAME_KUBI:
                {
                    return TRUE;
                }
                //150
                case QQTangCheatEngine::GAME_HONGBAOSHI:
                {
                    return TRUE;
                }
                //151
                case QQTangCheatEngine::GAME_HUANGBAOSHI:
                {
                    return TRUE;
                }
                //152
                case QQTangCheatEngine::GAME_LVBAOSHI:
                {
                    return TRUE;
                }
                //402
                case QQTangCheatEngine::GAME_MEIGUI2:
                {
                    return TRUE;
                }
                //403
                case QQTangCheatEngine::GAME_DIARY:
                {
                    return TRUE;
                }
            }

            if ( ( m_ItemID < 400 || m_ItemID > 1000 ) &&
                ( m_ItemID <= 24000 || m_ItemID >= 24500 ) &&
                ( m_ItemID <= 30000 || m_ItemID >= 32000 ) &&
                ( m_ItemID < 25001 || m_ItemID > 29000 ) &&
                ( m_ItemID < 9001 || m_ItemID > 9010 ) )
            {
                return FALSE;
            }
            return TRUE;
        }


	};

    BOOL IsPropToServer (ItemByGame PropID )
    {
        switch ( PropID )
        {
            //81
            case QQTangCheatEngine::GAME_TONGBI:
            {
                return TRUE;
            }
            //82
            case QQTangCheatEngine::GAME_YINBI:
            {
                return TRUE;
            }
            //83
            case QQTangCheatEngine::GAME_JINBI:
            {
                return TRUE;
            }
            //84
            case QQTangCheatEngine::GAME_QIANDAI:
            {
                return TRUE;
            }
            //85
            case QQTangCheatEngine::GAME_BAOXIANG1000TB:
            {
                return TRUE;
            }
            //91
            case QQTangCheatEngine::GAME_HONGZUANSHI:
            {
                return TRUE;
            }
            //92
            case QQTangCheatEngine::GAME_LANZUANSHI:
            {
                return TRUE;
            }
            //211
            case QQTangCheatEngine::GAME_ZIZUANSHI:
            {
                return TRUE;
            }
            //212
            case QQTangCheatEngine::GAME_XUEPINGZI:
            {
                return TRUE;
            }
            //213
            case QQTangCheatEngine::GAME_HUANGLUOSI:
            {
                return TRUE;
            }
            //93
            case QQTangCheatEngine::GAME_TANGBI1000:
            {
                return TRUE;
            }
            //94
            case QQTangCheatEngine::GAME_TANGBI500:
            {
                return TRUE;
            }
            //86
            case QQTangCheatEngine::GAME_JINGYAN20:
            {
                return TRUE;
            }
            //87
            case QQTangCheatEngine::GAME_JINGYAN50:
            {
                return TRUE;
            }
            //88
            case QQTangCheatEngine::GAME_JINGYAN100:
            {
                return TRUE;
            }
            //89
            case QQTangCheatEngine::GAME_JINGYAN200:
            {
                return TRUE;
            }
            //96
            case QQTangCheatEngine::GAME_MEIGUI1:
            {
                return TRUE;
            }
            //97
            case QQTangCheatEngine::GAME_LVSHUIJING:
            {
                return TRUE;
            }
            //98
            case QQTangCheatEngine::GAME_KUBI:
            {
                return TRUE;
            }
            //150
            case QQTangCheatEngine::GAME_HONGBAOSHI:
            {
                return TRUE;
            }
            //151
            case QQTangCheatEngine::GAME_HUANGBAOSHI:
            {
                return TRUE;
            }
            //152
            case QQTangCheatEngine::GAME_LVBAOSHI:
            {
                return TRUE;
            }
            //402
            case QQTangCheatEngine::GAME_MEIGUI2:
            {
                return TRUE;
            }
            //403
            case QQTangCheatEngine::GAME_DIARY:
            {
                return TRUE;
            }
        }

        if ( ( PropID < 400 || PropID > 1000 ) &&
            ( PropID <= 24000 || PropID >= 24500 ) &&
            ( PropID <= 30000 || PropID >= 32000 ) &&
            ( PropID < 25001 || PropID > 29000 ) &&
            ( PropID < 9001 || PropID > 9010 ) )
        {
            return FALSE;
        }
        return TRUE;
    }

}