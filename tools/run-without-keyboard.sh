#!/bin/bash
set -e
cd /usr/share/amongus
ANDROID_AVD_HOME=/usr/share/amongus/avd ANDROID_SDK_ROOT=/usr/share/amongus/sdk sdk/emulator/emulator -avd amongus -no-snapshot &

adb wait-for-device
while [ "$(adb shell getprop sys.boot_completed | tr -d '\r')" != "1" ]
do
	sleep 2
done

adb shell am start -n com.innersloth.spacemafia/com.unity3d.player.UnityPlayerActivity