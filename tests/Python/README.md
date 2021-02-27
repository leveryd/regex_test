# Python re模块
1. 应该是自己实现的NFA算法，不是基于PCRE库
2. 存在ReDos，不像PHP、OpenResty有配置选项限制回源次数

# 测试代码
```
import re
rx = re.compile('(?:.*,)*[ \t]*([^ \t]+)[ \t]+')
rx.findall("basic " + ("," * 100) + "A")   # CPU占用100%
rx.findall("xxx, aaaa    bbb")  # 可以正常匹配 aaaa
```
