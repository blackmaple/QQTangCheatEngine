
#include "WinMain.h"


BOOL WINAPI DllMain (
	_In_ HINSTANCE hInstance,
	_In_ DWORD fdwReason,
	_In_ LPVOID lpReserved )
{
	if ( fdwReason == DLL_PROCESS_ATTACH )
	{
		g_QQTangClient.CanOpenNext ( );
		SkinH_Init ( hInstance );
		SkinH_AttachResExByDll ( hInstance, MAKEINTRESOURCE ( IDR_SHE ), RT_RCDATA, NULL, 0, 0, 0 );
		CreateDialogParam ( hInstance, MAKEINTRESOURCE ( IDD_WinMain ), NULL, ( DLGPROC ) WinMainProc, NULL );
	}
	return TRUE;

	//skin 
	_mbsstr ( ( unsigned char * ) NULL, ( unsigned char * ) NULL );
	_mbscmp ( NULL, NULL );
}


int SkinH_AttachResExByDll (
	_In_ HINSTANCE hInstance,
	_In_ LPCTSTR lpName,			//��Դ��
	_In_ LPCTSTR lpType,			//��Դ����
	_In_ LPCTSTR strPassword,	//Ƥ����Կ
	_In_ int nHue,				//ɫ����	ȡֵ��Χ0-360, Ĭ��ֵ0
	_In_ int nSat,				//���Ͷȣ�	ȡֵ��Χ0-256, Ĭ��ֵ0
	_In_ int nBri				//���ȣ�	ȡֵ��Χ0-256, Ĭ��ֵ0
	)
{
	HRSRC hRsrc = FindResourceA ( hInstance, lpName, lpType );
	if ( hRsrc == 0 )
	{
		return SRET_ERROR_PARAM;
	}
	HGLOBAL hGlobal = LoadResource ( hInstance, hRsrc );
	LPVOID lpSHE = LockResource ( hGlobal );
	DWORD dwFileSize = SizeofResource ( hInstance, hRsrc );
	return SkinH_AttachRes ( ( LPBYTE ) lpSHE, dwFileSize, NULL, 0, 0, 0 );
}


BOOL CALLBACK WinMainProc ( _In_ HWND hWnd , _In_ UINT32 uMsg , _In_ WPARAM wParam , _In_ LPARAM lParam )
{
	switch ( uMsg )
	{
		case WM_INITDIALOG:
		{
			return TRUE;
		}
		case WM_COMMAND:
		{
			CQQTangCheatEngine Engine;
			switch ( wParam & 0xFFFF )
			{
				
				case IDC_btnTest:
				{
					Engine.FullScreenBoxExplode();
					break;
				}
				case IDC_btnBomb:
				{
					Engine.FullScreenBombExplode();
					break;
				}
				case IDC_btnProp:
				{
					Engine.FullScreenPropExplode();
					break;
				}
				case IDC_btnCreateBox:
				{
					Engine.FullScreenCreateBox ( ItemByBox::BOX_FIELD_02 );
					break;
				}
				case IDC_btnrelive:
				{
					Engine.FullScreenPlayBomb ( NPC_00 );
					break;
				}
				default:
					break;
			}
			return TRUE;
		}
		case WM_CLOSE:
		{
			SkinH_Free ( );
			EndDialog ( hWnd, NULL );
			return TRUE;
		}
		default:
		{ 
			return FALSE;
		}
	}
}