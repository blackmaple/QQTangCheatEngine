#pragma once
#pragma pack(1)
#include "Maple.hpp"
namespace QQTangCheatEngine
{
	class CCall
	{
		private:
			
		public:
			void   CreateRoom()
			{
				typedef void(__cdecl *pCreateRoom)();
				pCreateRoom(g_QQTangClient.m_CreateRoom)();
			}
			void   StartGame()
			{
				typedef void(__cdecl *pStartGame)();
				pStartGame(g_QQTangClient.m_StartGame)();
			}

			void   UseObject(ItemByPVE ObjectID,INT32 PetID)
			{
				typedef void(__cdecl *pUseObject)(ItemByPVE ObjectID, INT32 PetID);
				pUseObject(g_QQTangClient.m_UseObject)(ObjectID, PetID);
			}

			void   SelRoomSpeak(INT32 nsize, char *szBuffer)
			{
				typedef void(__cdecl *pSelRoomSpeak)(INT32 nsize, char *szBuffer);
				pSelRoomSpeak(g_QQTangClient.m_SelRoomSpeak)(nsize, szBuffer);
			}

			void   RoomSpeak(INT32 nsize, char *szBuffer)
			{
				typedef void(__cdecl *pRoomSpeak)(INT32 nsize, char *szBuffer);
				pRoomSpeak(g_QQTangClient.m_RoomSpeak)(nsize, szBuffer);
			}

			void   SetRoomMsg(char* szInRoomName,char* szOutRoomName, char* szPassWord)
			{
				typedef void(__cdecl *pSetRoomMsg)(char*, char*, char*);
				pSetRoomMsg(g_QQTangClient.m_SetRoomMsg)(szInRoomName, szOutRoomName, szPassWord);
			}

			void   OperateDoor(INT32 Index, INT32 nsize)
			{
				typedef void(__cdecl *pOperateDoor)(INT32 Index, INT32 nsize);
				pOperateDoor(g_QQTangClient.m_OperateDoor)(Index, nsize);
			}

			void   SelMap(MapID MapId, GameModle nsize)
			{
				typedef void(__cdecl *pSelMap)(MapID MapId, GameModle nsize);
				pSelMap(g_QQTangClient.m_SelMap)(MapId, nsize);
			}

			void   SelRoomModal(RoomType nType)
			{
				typedef void(__cdecl *pSelRoomModal)(RoomType nType);
				pSelRoomModal(g_QQTangClient.m_SelRoomType)(nType);
			}

			void   EnterRoom(INT32 TotalRoomID,char* szPassword)
			{
				typedef void(__cdecl *pEnterRoom)(INT32 TotalRoomID, char* szPassword);
				pEnterRoom(g_QQTangClient.m_EnterRoom)(TotalRoomID, szPassword);
			}

			void   EnterSelRoom(INT32 temp,PinDao pindao,QuYu quyu,INT32 SelSect)
			{
				typedef void(__cdecl *pEnterSelRoom)(INT32, PinDao, QuYu, INT32);
				pEnterSelRoom(g_QQTangClient.m_EnterSelRoom)(temp, pindao, quyu, SelSect);
			}

			void   MsgBox(char* szText, char* szCaption)
			{
				typedef void(__cdecl *pMsgBox)(char* , char*);
				pMsgBox(g_QQTangClient.m_MsgBox)(szText,szCaption);
			}

			void   NoticeBoard(char* szText, char* szCaption)
			{
				typedef void(__cdecl *pNoticeBoard)(char*, char*);
				pNoticeBoard(g_QQTangClient.m_NoticeBoard)(szText, szCaption);
			}

			void   ReleasePet(INT32 PetID)
			{
				typedef void(__cdecl *pReleasePet)(INT32);
				pReleasePet(g_QQTangClient.m_ReleasePet)(PetID);
			}

			void   ModifyRoomID(INT32 NewRoomID)
			{
				typedef void(__cdecl *pModifyRoomID)(INT32);
				pModifyRoomID(g_QQTangClient.m_ModifyRoomID)(NewRoomID);
			}

			void   ModifyPlayModle(INT32 nsize,PlayerModle NewPlayModle)
			{
				typedef void(__cdecl *pModifyPlayModle)(INT32, PlayerModle);
				pModifyPlayModle(g_QQTangClient.m_ModifyPlayModle)(nsize, NewPlayModle);
			}

			void   EnterRandRoom()
			{
				typedef void(__cdecl *pEnterRandRoom)();
				pEnterRandRoom(g_QQTangClient.m_EnterRandRoom)();
			}

			void   LeaveRoom()
			{
				typedef void(__cdecl *pLeaveRoom)();
				pLeaveRoom(g_QQTangClient.m_LeaveRoom)();
			}

			void   LeaveGame()
			{
				typedef void(__cdecl *pLeaveGame)();
				pLeaveGame(g_QQTangClient.m_LeaveGame)();
			}

			void   LeaveSelRoom()
			{
				typedef void(__cdecl *pLeaveSelRoom)();
				pLeaveSelRoom(g_QQTangClient.m_LeaveSelRoom)();
			}

			void   QuitGame()
			{
				typedef void(__cdecl *pQuitGame)();
				pQuitGame(g_QQTangClient.m_QuitGame)();
			}

			void   CarryPet(INT32 PetID)
			{
				typedef void(__cdecl *pCarryPet)(INT32);
				pCarryPet(g_QQTangClient.m_CarryPet)(PetID);
			}

			void   StopCarryPet(INT32 PetID)
			{
				typedef void(__cdecl *pStopCarryPet)(INT32);
				pStopCarryPet(g_QQTangClient.m_StopCarryPet)(PetID);
			}

			void   ModifyColor(INT32 nsize, TeamColor color)
			{
				typedef void(__cdecl *pModifyColor)(INT32, TeamColor);
				pModifyColor(g_QQTangClient.m_ModifyColor)(nsize, color);
			}

			void   ModifyChatRoomMap(INT32 MapId)
			{
				typedef void(__cdecl *pModifyChatRoomMap)(INT32);
				pModifyChatRoomMap(g_QQTangClient.m_ModifyChatRoomMap)(MapId);
			}

			CCall(){}
	};

}