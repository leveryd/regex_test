# 运行前必读

2. 安装依赖

    Mac按照下面操作

    ```
    luarocks install lrexlib-PCRE  # 安装PCRE lua库
    lua -e "require 'rex_pcre'"   # 测试依赖库是否安装成功
    ```

3. 执行测试脚本

    lua test.lua

4. 预期的测试结果

    PCRE库api报告回溯次数超过限制，lrexlib-PCRE库抛出错误。

    报错信息如下
    ```
    lua: test_pcre.lua:5: error PCRE_ERROR_MATCHLIMIT
    stack traceback:
            [C]: in function 'rex_pcre.find'
            test_pcre.lua:5: in main chunk
            [C]: in ?
    ```



# lrexlib介绍

[项目地址](https://github.com/rrthomas/lrexlib)

lrexlib支持pcre、pcre2、gnu、posix等多个正则引擎的封装
