# -*- mode: python ; coding: utf-8 -*-

a = Analysis(['Full Path of .py file which needs to be converted'],
                 pathex=['Full path of FOLDER in which the .py file is present'],
                 hiddenimports=[],
                 hookspath=None)
a.datas += [ ('ONLY THE ABSOLUTE NAME OF ICO FILE (for eg : download.ico)', 'Full Path to ICO File', 'DATA')]

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'Name of the Application'),
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='Full Path to ICO File')