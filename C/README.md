# 运行前必读

1. 需要安装pcre库

    Mac上可以执行下面命令安装
    ```
    brew install pcre
    ```

2. 运行前需要修改lib库到对应的位置

    Makefile中修改依赖lib的文件路径，方法可以看Makefile中注释

3. 执行 `make all`


# PCRE介绍

man pcre 查看介绍

* 大的版本分为 PCRE1、PCRE2 两个版本

* 版本中因为字符集编码，所以存在三套接口，如 libpcre libpcre16 libpcre32

man pcrematching 查看算法讨论

* 基于pcre有很多的包装，最有名的是google的c++ wrapper

* 两套算法实现
  * pcre_exec等接口使用NFA算法（标准算法）
  * pcre_dfa_exec等接口使用DFA算法  

# PCRE 回溯限制
man pcreapi 搜索 match_limit，可以看到介绍
* match_limit是pcre_extra结构体中的一个字段
* match_limit默认是 10 million
