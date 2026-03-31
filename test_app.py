from AppOpener import open as appopen
import sys

def test():
    try:
        appopen("some_fake_app_name", match_closest=True, throw_error=True)
    except Exception as e:
        print("YES CAUGHT:", str(e))
    
    try:
        appopen("notepad", match_closest=True, throw_error=True)
        print("NOTEPAD OPENED")
    except Exception as e:
        print("FAILED TO OPEN NOTEPAD:", e)

test()
