class Static:
    __module__ = __name__
    style = wgtstyle_static

class TWidget:
    __module__ = __name__
    type = 'WIDGET'

class TStatic:
    __module__ = __name__
    type = 'WIDGET'
    style = wgtstyle_static

class TCheck:
    __module__ = __name__
    type = 'CHECK'

class TStdCheck:
    __module__ = __name__
    type = 'CHECK'
    framescheme = [(-1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1,
      -1),
     (0,
      0,
      0,
      0,
      0,
      0,
      0,
      0)]
    rect = (0,
     0,
     40,
     16)
    bkimage = 'object/ui/common/btn_check.img'

class TDlg:
    __module__ = __name__
    type = 'DIALOG'

class TEdit:
    __module__ = __name__
    type = 'EDIT'
    editmethod = edit_normal
    drawcolor = (0,
     0,
     0,
     255)
    bkcolor = (255,
     255,
     255,
     0)
    focuscolor = (0,
     0,
     0,
     0)

class TStaticEdit(TEdit):
    __module__ = __name__
    style = wgtstyle_static

class TEditBox:
    __module__ = __name__
    type = 'EDIT'
    editable = 0
    textstyle = (dt_left + dt_center)
    drawcolor = (0,
     0,
     0,
     255)

class TEditPoint:
    __module__ = __name__
    type = 'EDIT'
    editmethod = edit_number
    editable = 0
    bkcolor = (255,
     255,
     255,
     0)
    drawcolor = (0,
     0,
     0,
     255)
    step = 1
    textstyle = 5
    minvalue = 0
    maxvalue = ui_initmaxpoint

class TEditNum:
    __module__ = __name__
    type = 'EDIT'
    editmethod = edit_number
    editable = 0
    bkcolor = (255,
     255,
     255,
     0)
    drawcolor = (0,
     0,
     0,
     255)
    step = 1
    textstyle = 5

class TEditCharNum:
    __module__ = __name__
    type = 'EDIT'
    editmethod = edit_charNumber
    editable = 0
    bkcolor = (255,
     255,
     255,
     0)
    drawcolor = (0,
     0,
     0,
     255)
    step = 1
    textstyle = 5

class TEditPassword:
    __module__ = __name__
    type = 'EDIT'
    editmethod = edit_coder
    drawcolor = (255,
     255,
     255,
     255)
    focuscolor = (0,
     0,
     0,
     255)
    maxchar = 16
    textsize = 12

class TEditID:
    __module__ = __name__
    type = 'EDIT'
    editmethod = edit_number
    drawcolor = (255,
     255,
     255,
     255)
    focuscolor = (0,
     0,
     0,
     255)
    maxchar = 10
    textsize = 12

class TKeyEdit:
    __module__ = __name__
    type = 'KEYEDIT'

class TLabel:
    __module__ = __name__
    type = 'LABEL'
    textsize = 12
    textstyle = (dt_left + dt_top)
    drawcolor = (0,
     0,
     0,
     255)

class TPicLabel:
    __module__ = __name__
    type = 'PICLABEL'
    textsize = 0

class TRadio:
    __module__ = __name__
    type = 'CHECK'
    groupid = 8
    extendstyle = ui_btn_style_radio

class TRichEdit:
    __module__ = __name__
    type = 'RICHEDIT'
    maxchar = 800
    drawcolor = (0,
     0,
     0,
     255)
    textsize = 12
    textfont = 1
    editmethod = edit_talk

class TSpinUp:
    __module__ = __name__
    type = 'SPIN'
    style = wgtstyle_primary

class TSpinDown:
    __module__ = __name__
    type = 'SPIN'

class TSpinInc:
    __module__ = __name__
    type = 'SPIN'
    style = wgtstyle_primary

class TSpinDec:
    __module__ = __name__
    type = 'SPIN'

class TSpinUpScroll(TSpinUp):
    __module__ = __name__
    rect = (0,
     0,
     16,
     16)
    textstyle = 1
    aligntype = (aligntype_father + aligntype_winrect)
    alignstyle = (alignstyle_top_out + alignstyle_hcenter)
    marginh = 0
    marginv = 0

class TSpinDownScroll(TSpinDown):
    __module__ = __name__
    rect = (0,
     0,
     16,
     16)
    aligntype = (aligntype_father + aligntype_winrect)
    alignstyle = (alignstyle_bottom_out + alignstyle_hcenter)
    marginh = 0
    marginv = 0

class TString:
    __module__ = __name__
    type = 'LABEL'
    visible = 0

class TPoser:
    __module__ = __name__
    type = 'POSER'
    style = wgtstyle_static
    rect = (0,
     0,
     800,
     600)

class TButton:
    __module__ = __name__
    type = 'BUTTON'

class THyperLink:
    __module__ = __name__
    type = 'HYPERLINK'

class TVScroll:
    __module__ = __name__
    type = 'SCROLLBAR'
    style = wgtstyle_vertical
    extendstyle = 2

class TScrollBtn:
    __module__ = __name__
    type = 'BUTTON'
    moveable = 1

class TTabWin:
    __module__ = __name__
    rect = (0,
     0,
     0,
     0)
    type = 'TABWIN'
    groupid = 0

class TStaticCheck:
    __module__ = __name__
    type = 'CHECK'
    style = wgtstyle_static


#+++ okay decompyling
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
