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
	_In_ LPCTSTR lpName,			//��Դ��
	_In_ LPCTSTR lpType,			//��Դ����
	_In_ LPCTSTR strPassword,	//Ƥ����Կ
	_In_ int nHue,				//ɫ����	ȡֵ��Χ0-360, Ĭ��ֵ0
	_In_ int nSat,				//���Ͷȣ�	ȡֵ��Χ0-256, Ĭ��ֵ0
	_In_ int nBri				//���ȣ�	ȡֵ��Χ0-256, Ĭ��ֵ0
	);
