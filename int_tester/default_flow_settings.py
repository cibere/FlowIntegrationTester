import json

default_flow_settings = json.dumps(
    {
        "Hotkey": "Alt \u002b Space",
        "OpenResultModifiers": "Alt",
        "ColorScheme": "System",
        "ShowOpenResultHotkey": True,
        "WindowSize": 580,
        "PreviewHotkey": "F1",
        "AutoCompleteHotkey": "Ctrl \u002b Tab",
        "AutoCompleteHotkey2": "",
        "SelectNextItemHotkey": "Tab",
        "SelectNextItemHotkey2": "",
        "SelectPrevItemHotkey": "Shift \u002b Tab",
        "SelectPrevItemHotkey2": "",
        "SelectNextPageHotkey": "PageUp",
        "SelectPrevPageHotkey": "PageDown",
        "OpenContextMenuHotkey": "Ctrl\u002bO",
        "SettingWindowHotkey": "Ctrl\u002bI",
        "CycleHistoryUpHotkey": "Alt \u002b Up",
        "CycleHistoryDownHotkey": "Alt \u002b Down",
        "Language": "en",
        "Theme": "Win11Light",
        "UseDropShadowEffect": True,
        "WindowHeightSize": 42,
        "ItemHeightSize": 58,
        "QueryBoxFontSize": 20,
        "ResultItemFontSize": 16,
        "ResultSubItemFontSize": 13,
        "QueryBoxFont": "Microsoft Sans Serif",
        "QueryBoxFontStyle": None,
        "QueryBoxFontWeight": None,
        "QueryBoxFontStretch": None,
        "ResultFont": "Microsoft Sans Serif",
        "ResultFontStyle": None,
        "ResultFontWeight": None,
        "ResultFontStretch": None,
        "ResultSubFont": "Microsoft Sans Serif",
        "ResultSubFontStyle": None,
        "ResultSubFontWeight": None,
        "ResultSubFontStretch": None,
        "UseGlyphIcons": True,
        "UseAnimation": True,
        "UseSound": True,
        "SoundVolume": 50,
        "UseClock": True,
        "UseDate": False,
        "TimeFormat": "hh:mm tt",
        "DateFormat": "MM\u0027/\u0027dd ddd",
        "FirstLaunch": False,
        "SettingWindowWidth": 1000,
        "SettingWindowHeight": 700,
        "SettingWindowTop": None,
        "SettingWindowLeft": None,
        "SettingWindowState": 0,
        "CustomExplorerIndex": 0,
        "CustomExplorerList": [
            {
                "Name": "Explorer",
                "Path": "explorer",
                "FileArgument": "/select, \u0022%f\u0022",
                "DirectoryArgument": "\u0022%d\u0022",
                "Editable": False,
            },
            {
                "Name": "Total Commander",
                "Path": "C:\\Program Files\\totalcmd\\TOTALCMD64.exe",
                "FileArgument": "/O /A /S /T \u0022%f\u0022",
                "DirectoryArgument": "/O /A /S /T \u0022%d\u0022",
                "Editable": True,
            },
            {
                "Name": "Directory Opus",
                "Path": "C:\\Program Files\\GPSoftware\\Directory Opus\\dopusrt.exe",
                "FileArgument": "/cmd Go \u0022%f\u0022 NEW",
                "DirectoryArgument": "/cmd Go \u0022%d\u0022 NEW",
                "Editable": True,
            },
            {
                "Name": "Files",
                "Path": "Files",
                "FileArgument": "-select \u0022%f\u0022",
                "DirectoryArgument": "-select \u0022%d\u0022",
                "Editable": True,
            },
        ],
        "CustomBrowserIndex": 0,
        "CustomBrowserList": [
            {
                "Name": "Default",
                "Path": "*",
                "PrivateArg": "",
                "EnablePrivate": False,
                "OpenInTab": True,
                "Editable": False,
            },
            {
                "Name": "Google Chrome",
                "Path": "chrome",
                "PrivateArg": "-incognito",
                "EnablePrivate": False,
                "OpenInTab": True,
                "Editable": False,
            },
            {
                "Name": "Mozilla Firefox",
                "Path": "firefox",
                "PrivateArg": "-private",
                "EnablePrivate": False,
                "OpenInTab": True,
                "Editable": False,
            },
            {
                "Name": "MS Edge",
                "Path": "msedge",
                "PrivateArg": "-inPrivate",
                "EnablePrivate": False,
                "OpenInTab": True,
                "Editable": False,
            },
        ],
        "ShouldUsePinyin": False,
        "AlwaysPreview": False,
        "AlwaysStartEn": False,
        "QuerySearchPrecision": "Regular",
        "AutoUpdates": False,
        "WindowLeft": 752,
        "WindowTop": 0,
        "CustomWindowLeft": 0,
        "CustomWindowTop": 0,
        "KeepMaxResults": False,
        "MaxResultsToShow": 5,
        "ActivateTimes": 0,
        "CustomPluginHotkeys": [],
        "CustomShortcuts": [],
        "DontPromptUpdateMsg": False,
        "EnableUpdateLog": False,
        "StartFlowLauncherOnSystemStartup": False,
        "HideOnStartup": True,
        "HideNotifyIcon": False,
        "LeaveCmdOpen": False,
        "HideWhenDeactivated": True,
        "SearchWindowScreen": "Cursor",
        "SearchWindowAlign": "Center",
        "CustomScreenNumber": 1,
        "IgnoreHotkeysOnFullscreen": False,
        "Proxy": {
            "Enabled": False,
            "Server": None,
            "Port": 0,
            "UserName": None,
            "Password": None,
        },
        "LastQueryMode": "Selected",
        "AnimationSpeed": "Medium",
        "CustomAnimationLength": 360,
        "PluginSettings": {
            "PythonExecutablePath": "",
            "NodeExecutablePath": "",
            "Plugins": {
                "0ECADE17459B49F587BF81DC3A125110": {
                    "ID": "0ECADE17459B49F587BF81DC3A125110",
                    "Name": "Browser Bookmarks",
                    "Version": "3.3.4",
                    "ActionKeywords": ["b"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "CEA0FDFC6D3B4085823D60DC76F28855": {
                    "ID": "CEA0FDFC6D3B4085823D60DC76F28855",
                    "Name": "Calculator",
                    "Version": "3.1.5",
                    "ActionKeywords": ["*"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "572be03c74c642baae319fc283e561a8": {
                    "ID": "572be03c74c642baae319fc283e561a8",
                    "Name": "Explorer",
                    "Version": "3.2.4",
                    "ActionKeywords": ["*", "doc:", "*", "*", "*"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "6A122269676E40EB86EB543B945932B9": {
                    "ID": "6A122269676E40EB86EB543B945932B9",
                    "Name": "Plugin Indicator",
                    "Version": "3.0.7",
                    "ActionKeywords": ["?"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "9f8f9b14-2518-4907-b211-35ab6290dee7": {
                    "ID": "9f8f9b14-2518-4907-b211-35ab6290dee7",
                    "Name": "Plugins Manager",
                    "Version": "3.2.4",
                    "ActionKeywords": ["pm"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "b64d0a79-329a-48b0-b53f-d658318a1bf6": {
                    "ID": "b64d0a79-329a-48b0-b53f-d658318a1bf6",
                    "Name": "Process Killer",
                    "Version": "3.0.8",
                    "ActionKeywords": ["kill"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "791FC278BA414111B8D1886DFE447410": {
                    "ID": "791FC278BA414111B8D1886DFE447410",
                    "Name": "Program",
                    "Version": "3.3.4",
                    "ActionKeywords": ["*"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "D409510CD0D2481F853690A07E6DC426": {
                    "ID": "D409510CD0D2481F853690A07E6DC426",
                    "Name": "Shell",
                    "Version": "3.2.5",
                    "ActionKeywords": ["\u003e"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "CEA08895D2544B019B2E9C5009600DF4": {
                    "ID": "CEA08895D2544B019B2E9C5009600DF4",
                    "Name": "System Commands",
                    "Version": "3.1.7",
                    "ActionKeywords": ["*"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "0308FD86DE0A4DEE8D62B9B535370992": {
                    "ID": "0308FD86DE0A4DEE8D62B9B535370992",
                    "Name": "URL",
                    "Version": "3.0.8",
                    "ActionKeywords": ["*"],
                    "Priority": 0,
                    "Disabled": False,
                },
                "565B73353DBF4806919830B9202EE3BF": {
                    "ID": "565B73353DBF4806919830B9202EE3BF",
                    "Name": "Web Searches",
                    "Version": "3.1.4",
                    "ActionKeywords": [
                        "*",
                        "sc",
                        "wiki",
                        "findicon",
                        "facebook",
                        "twitter",
                        "maps",
                        "translate",
                        "duckduckgo",
                        "github",
                        "gist",
                        "gmail",
                        "drive",
                        "wolframalpha",
                        "stackoverflow",
                        "lucky",
                        "image",
                        "youtube",
                        "bing",
                        "yahoo",
                        "bd",
                    ],
                    "Priority": 0,
                    "Disabled": False,
                },
                "5043CETYU6A748679OPA02D27D99677A": {
                    "ID": "5043CETYU6A748679OPA02D27D99677A",
                    "Name": "Windows Settings",
                    "Version": "4.0.12",
                    "ActionKeywords": ["s"],
                    "Priority": 0,
                    "Disabled": False,
                },
            },
        },
    }
)
