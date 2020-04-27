#  正则匹配：从这个地址中取出fruits,地址可能是 /v1/fruits?name=1，或者/v1/fruits/1,或者/v1/fruits

import re

def fetch(contents):
    pat = re.compile(r'/v1/'+r'(.*?)(\?|\/|$)')
    pMatch = re.search(pat,contents)
    return pMatch.group(1)

print(fetch("/v1/fruits?name=1/"))
print(fetch("/v1/fruits/1"))
print(fetch("/v1/fruits"))

def fetch2(contents):
    pat = re.compile(r'(^|\?|\&)name='+r'(.*?)(&|$)')
    pMatch = re.search(pat,contents)
    return pMatch.group(2)

print(fetch2("name=hahah"))
print(fetch2("/v1/fruits?name=Im"))
print(fetch2("/v1/fruits?name=Ideh&age=2"))
print(fetch2("/v1/fruits?sex=1&name=zyx"))
print(fetch2("/v1/fruits?sex=1&name=gfc&age=2"))

# 从12324324Reetr432 中匹配出数字，结果是12324324432


str = "12324324Reetr432"
print(re.findall(r'(.+?)'+r'(.*?)'+r'(.+?)',str)) 

