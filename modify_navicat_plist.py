import os
import plistlib

PLIST_PATH = "/Users/lingyin/Library/Preferences/com.navicat.NavicatPremium.plist"
NAVICAT_PATH = "/Users/lingyin/Library/Application Support/PremiumSoft CyberTech/Navicat CC/Navicat Premium/.A8474C90078797CD5D1F2FDE35735D31"
SPECIFIC_KEY = "B150F41ABDCF9BC7F3B1148FF6936E69"


def read(path):
    with open(path, 'rb') as fp:
        plist_data = plistlib.load(fp)
    return plist_data


def write(path, plist_data):
    with open(path, 'wb') as fp:
        plistlib.dump(plist_data, fp)


def delete_entry(plist_data):
    try:
        del plist_data[SPECIFIC_KEY]
    except:
        pass
    return plist_data


def delete_file():
    try:
        os.remove(NAVICAT_PATH)
    except:
        pass


if __name__ == "__main__":
    plist = read(PLIST_PATH)
    write(PLIST_PATH, delete_entry(plist))
    delete_file()
    print("试用期更新成功")
