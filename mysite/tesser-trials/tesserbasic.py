from tesserocr import PyTessBaseAPI

images = ['chocolate-1.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print (api.GetUTF8Text())
        print (api.AllWordConfidences())
# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.