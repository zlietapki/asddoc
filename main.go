package main

import (
	"fmt"
	"os"
	"os/exec"
	"path"
	"strings"
)

const (
	BASEDIR = "~/Dropbox"
	VIEWER  = "code"
)

func resolvePath(doc string) string {
	if !strings.Contains(doc, "/") {
		return path.Join(BASEDIR, doc, doc+".md")
	}
	return path.Join(BASEDIR, doc+".md")
}

func main() {
	if len(os.Args) == 1 {
		showHelp()
	}

	docPath := resolvePath(os.Args[1])
	if _, err := exec.Command("bash", "-c", VIEWER+" "+docPath).Output(); err != nil {
		println(err)
	}
}

func showHelp() {
	fmt.Printf("Usage: %s <doc>\n", os.Args[0])
	os.Exit(0)
}
