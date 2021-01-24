all:
	@clang -S pcre_test.c -o pcre_test.s && as pcre_test.s -o pcre_test.o
	@# 需要修改下面两个lib库的文件路径到对应的地址，其中
	@# /usr/local/Cellar/pcre/8.44/lib/libpcre.1.dylib是pcre文件路径
	@# /usr/lib/libSystem.B.dylib是libc库文件路径
	@# 如何找到lib库文件路径： Mac下可以 find /usr/local/Cellar -name "libpcre*" 来找
	@ld pcre_test.o /usr/local/Cellar/pcre/8.44/lib/libpcre.1.dylib /usr/lib/libSystem.B.dylib  -o a.out
clean:
	@rm pcre_test.s pcre_test.o a.out
