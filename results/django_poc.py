"""
django/utils/translation/template.py

(\s+.*context\s+((?:"[^"]*?")|(?:'[^']*?')))?\s*
(?:\s*\|\s*[^\s:]+(?::(?:[^\s'":]+|(?:"[^"]*?")|(?:'[^']*?')))?)*
"""
# 构造poc费劲

from django.utils.translation.template import templatize

templatize("{%1111%}")

a = r"""(\s+.*context\s+((?:"[^"]*?")|(?:'[^']*?')))?\s*"""
