# SampleSpec
A sample .spec file for converting a .py file (with icon) to .exe

- After Installation , open the file with notepad and replace the required data in the file (the instructions are given in the .spec file itself)
- Once you have put in the required details and saved the file , open cmd in the directory of the file (please note that the .ico and the .py file should be in the same directory as the spec)
- If your app is a console application change `console = False` to `console = True`
- In cmd , enter ```pyinstaller sample.spec```
- Let pyinstaller do its thing , and the application should be ready in the newly formed `dist` folder
- IT IS TO BE NOTED THAT WHILE RUNNING THE APPLICATION , THE ICO AND EXE FILE SHOULD BE IN THE SAME DIRECTORY 

### Here is an example of what the `sample.spec` file should look like :
```
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(['E:\\Python\\programmes\\Faster2PDF\\imgpdf.py'],
                 pathex=['E:\\Python\\programmes\\Faster2PDF'],
                 hiddenimports=[],
                 hookspath=None)
a.datas += [ ('download.ico', 'E:\\Python\\programmes\\Faster2PDF\\download.ico', 'DATA')]

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'Faster2PDF'),
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='E:\\Python\\programmes\\Faster2PDF\\download.ico')
```          
