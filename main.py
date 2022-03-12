#!/usr/bin/env python3
import sys
import webview
user = sys.argv[1]
webview.create_window("H4Shop - Hadcl4 Games and Software", "/home/"+user+"/H4Shop/main.html")
webview.start()
