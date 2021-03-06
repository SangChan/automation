import os
import urllib2
import json

bundlecodes = {
"Base":"en",
"ar":"ar",
"de":"de",
"en":"en",
"es":"es",
"es-419":"es-CL",
"fr":"fr",
"id":"id-ID",
"it":"it",
"ja":"ja-JP",
"ko":"ko-KR",
"pt-BR":"pt-BR",
"pt":"pt-PT",
"ru":"ru",
"th":"th",
"tr":"tr-TR",
"vi":"vi",
"zh":"zh-CN",
"zh-Hant-HK":"zh-HK",
"zh-Hant-TW":"zh-TW"
}

blurbs = {
"694987":"UseWifiOnly",
"694985":"Version"
}

result = "rootplist"

os.makedirs(result)
os.chdir(result)

for bundlecode,culturecode in bundlecodes.items():
    bundlecodedir = bundlecode+".lproj"
    os.makedirs(bundlecodedir)
    os.chdir(bundlecodedir)
    f = open("Root.strings","w")
    for id,name in blurbs.items():
        url = "http://apollouat.englishtown.com/services/api/proxy/queryproxy?c=culturecode%3D"+culturecode+"&q=blurb!"+id
        u = urllib2.urlopen(url)
        data = u.read()
        j = json.loads(data)
        first = j[0]
        f.write("/* "+id+" */ \n")
        newblurb = "\""+name+"\" = \""+first["translation"]+"\";"
        f.write(newblurb.encode('utf-8'))
        f.write("\n\n")
    f.close()
    os.chdir("..")

