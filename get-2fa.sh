#! /usr/bin/env osascript
tell application "System Events"
    if name of every process contains "FollowUpUI" then
        tell window 1 of process "FollowUpUI"
            click button "Allow"
            delay 2
            set code to value of static text 1 of group 1
            log (code)
            click button "Done"
        end tell
    else
        log ("Couldn't find 2FA window")
    end if
end tell
return