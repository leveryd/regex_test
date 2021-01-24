-- 这里的lua正则表达式库基于pcre
local r=require 'rex_pcre'
local s=string.rep(",", 10000)
s="basic "..s.."A"
--print(s)
print(r.find(s,"(?:.*,)*[ \t]*([^ \t]+)[ \t]+"))
