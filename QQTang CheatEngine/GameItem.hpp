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
#pragma  pack(1)
#include "Maple.hpp"
#define PGameItem CGameItem*

namespace QQTangCheatEngine
{
	__interface IGameItemBase
	{
		void* InitBase ( bool Destroy );
		bool IsUsing ( );
	};

	class CGameItem :public IGameItemBase
	{
		private:
		INT32 m_LeftTime;
		INT32 m_0x8;
		ItemByGame m_ItemID;
		CLocation m_ItemXY;
		INT32 m_0x14;
		INT32 m_0x18;
		INT32 m_0x1C;
		INT32 m_0x20;
		INT32 m_0x24;
		INT32 m_0x2C;
		INT32 m_0x30;
		INT32 m_0x34;

		public:
		INT16 GetItemInMaxX ( )const
		{
			return m_ItemXY.GetX ( );
		}
		INT16 GetItemInMaxY ( )const
		{
			return m_ItemXY.GetY ( );
		}
		ItemByGame GetItemID ( )const
		{
			return m_ItemID;
		}
		INT16 GetItemInPlayerX ( )
		{
			INT16 x = m_ItemXY.GetX ( );
			x = x * 4 + x;
			return (x * 8 + 20);
		}
		INT16 GetItemInPlayerY ( )
		{
			INT16  y = m_ItemXY.GetY ( );
			y = y * 4 + y;
			return ( y * 8 + 20 );
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



		void* InitBase ( bool Destroy ) { }
		bool IsUsing ( ) { }
	};


}

