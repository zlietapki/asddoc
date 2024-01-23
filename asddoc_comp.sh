#!/usr/bin/env bash

_asddoc_completion()
{
    local doc
    doc=$(cd ~/Dropbox/; find . -maxdepth 2 -not -name '.*' | grep -v index.md | cut -c 3- | sed 's/\.md$//' | sort | fzf --layout=reverse-list)
    if [[ -z $doc ]]; then
        return
    fi

    COMPREPLY=("$doc")
}

complete -F _asddoc_completion asddoc
