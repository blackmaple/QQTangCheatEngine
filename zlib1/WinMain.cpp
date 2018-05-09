
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
	_In_ LPCTSTR lpName,			//资源名
	_In_ LPCTSTR lpType,			//资源类型
	_In_ LPCTSTR strPassword,	//皮肤密钥
	_In_ int nHue,				//色调，	取值范围0-360, 默认值0
	_In_ int nSat,				//饱和度，	取值范围0-256, 默认值0
	_In_ int nBri				//亮度，	取值范围0-256, 默认值0
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