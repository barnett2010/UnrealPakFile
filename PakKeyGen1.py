## Unreal Pak File Generation 1

import re
import sys
import codecs
import binascii
import os
import pyperclip
import json

## Array section
offsetArray = []
KeySectionList = []
##

## Pattern section <420
initPattern = b'\x48\x8D\x41\x1F\xC7\x45\xD8'
junkPattern = ["c745d4", "488d411fc745d8", "c745dc",
    "c745e0", "c745e4", "c745e8", "c745ec"]
##

## Pattern section 422
initPattern = b'\x48\x8D\x41\x1F\xC7\x45\xD8'
junkPattern = ["c741d4", "488d411fc745d8", "c745dc",
    "c745e0", "c745e4", "c745e8", "c745ec"]
##

## Error section
erGenKey = "[!] wrong, can't generate key."
erCryptoData = "[!] wrong, can't create Crypto.json ."
erB64toBytes = "[!] wrong, can't convert string to bytes."
erFile = "[!] provide a filename to proceed."
erData = "[!] File doesn't exist, proceed a valid file."
erOffset = "[!] Something wrong."
erDumpKey = "[!] wrong, can't dump ."

##


        ## Json pattern generation
        data = {}
        types = {}
        EncryptionKey = {}

        data['$types'] = types
        types['UnrealBuildTool.EncryptionAndSigning+CryptoSettings, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "1"
        types['UnrealBuildTool.EncryptionAndSigning+EncryptionKey, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "2"
        types['UnrealBuildTool.EncryptionAndSigning+SigningKeyPair, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "3"
        types['UnrealBuildTool.EncryptionAndSigning+SigningKey, UnrealBuildTool, Version=4.0.0.0, Culture=neutral, PublicKeyToken=null'] = "4"
        data['$type'] = "1"
        data['EncryptionKey'] = EncryptionKey
        EncryptionKey['$type'] = "2"
        EncryptionKey['Name'] = "null"
        EncryptionKey['Guid'] = "null"
        EncryptionKey['Key'] = b64
        data['SigningKey'] = "null"
        data['bEnablePakSigning'] = "true"
        data['bEnablePakIndexEncryption'] = "true"
        data['bEnablePakIniEncryption'] = "true"
        data['bEnablePakUAssetEncryption'] = "true"
        data['bEnablePakFullAssetEncryption'] = "false"
        data['bDataCryptoRequired'] = "true"
        data['PakEncryptionRequired'] = "true"
        data['PakSigningRequired'] = "true"
        data['SecondaryEncryptionKeys'] = "[ ]"
        ##
## Function section
