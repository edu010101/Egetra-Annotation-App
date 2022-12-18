def LoadCSS(CSSPath):
    ReadedFile = open(CSSPath,"r")
    QCSS = ReadedFile.read()
    return QCSS