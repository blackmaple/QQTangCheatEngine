#pragma once
#pragma pack(1)

#include "QQTangCheatEngine.hpp"
using namespace QQTangCheatEngine;

#include "SkinH.h"
 
#include <mbstring.h>
#pragma comment(lib, "Detours.lib")
#pragma comment(lib, "SkinH_ST.lib")
#include "resource.h"

BOOL WINAPI DllMain (
	_In_ HINSTANCE hInstance,
	_In_ DWORD fdwReason,
	_In_ LPVOID lpReserved );

BOOL CALLBACK WinMainProc ( _In_ HWND hWnd, _In_ UINT32 uMsg, _In_ WPARAM wParam, _In_ LPARAM lParam );

int  SkinH_AttachResExByDll (
	_In_ HINSTANCE hInstance,
	_In_ LPCTSTR lpName,			//资源名
	_In_ LPCTSTR lpType,			//资源类型
	_In_ LPCTSTR strPassword,	//皮肤密钥
	_In_ int nHue,				//色调，	取值范围0-360, 默认值0
	_In_ int nSat,				//饱和度，	取值范围0-256, 默认值0
	_In_ int nBri				//亮度，	取值范围0-256, 默认值0
	);
