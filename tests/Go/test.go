package main

import "regexp"
import "fmt"

func main(){
	reg := regexp.MustCompile(`(\(\s*(?:%s|%\(.+\)s)\s*(?:,\s*(?:%s|%\(.+\)s)\s*)*\))`)
	//api := reg.FindAllString("(%s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s,%(x)s", -1)
	api := reg.FindAllString("(%s)",-1)
	fmt.Println(api)
}
