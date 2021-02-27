/*
 * 代码基于 https://www.cnblogs.com/Leo-Forest/archive/2012/07/18/2597088.html 修改
 *
 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pcre.h>

int is_match (const char *src, const char *pattern)
{
    pcre *re;
    const char *error;
    int erroffset;
    int result;

    re = pcre_compile (pattern,       /* the pattern */
            0,       /* default options */
            &error,       /* for error message */
            &erroffset, /* for error offset */
            NULL);       /* use default character tables */

    /* Compilation failed: print the error message and exit */
    if (re == NULL) {
        printf ("PCRE compilation failed at offset %d: %s\n", erroffset, error);
        return -1;
    }

    result = pcre_exec (re,        /* the compiled pattern */
            NULL, /* no extra data - we didn't study the pattern */
            src, /* the src string */
            strlen (src), /* the length of the src */
            0,        /* start at offset 0 in the src */
            0,        /* default options */
            NULL, 0);

    /* If Matching failed: */
    // if (result < 0) {
    //     // printf("%s", error);
    //     // printf("%d\n", result);
    //     free (re);
    //     return -1;
    // }

    free (re);
    return result;
}


int main ( int argc, char *argv[] )
{
    int result;
    const char *pattern = "x(1.*)*y";

    char *src1 = "x111y";
    result = is_match(src1, pattern);

    // 匹配成功
    printf ("%d\n", result);   // 打印0

    char *src2 = "aaaa";
    result = is_match(src2, pattern);
    // 匹配不成功
    printf ("%d\n", result);   // 打印-1

    char *src3 = "x1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111";
    result = is_match(src3, pattern);
    // 匹配不成功，且应该有大量回溯
    printf ("%d\n", result);   // 打印-8

    return EXIT_SUCCESS;
}
