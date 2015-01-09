#! /usr/bin/python

import os
import re
from mdparser import parse, getMarkDownFilePaths


#location of files:

pathToChapters = os.path.abspath('../chapters')         #path were the directory with all chapters is located
bibtex_file = '../references/test.bib'
csl_file = '../references/plos.csl'
outfile = '../compiled/thesis.pdf'
preParsedMarkdownPath = '../compiled/thesis.md'

markdownFiles = getMarkDownFilePaths(pathToChapters)

with open(preParsedMarkdownPath, 'w') as preParsedMarkdown:

    for markdownFile in markdownFiles:

        parse(markdownFile, preParsedMarkdown)


from subprocess import call


call(['pandoc', '-s', '--toc', '--chapters', preParsedMarkdownPath, '-o', outfile, '--bibliography=' + bibtex_file, '--csl', csl_file, '--latex-engine=xelatex', '--template=../template/simple_template.latex'])

#call(['pandoc', '-s', '--toc', '--chapters', preParsedMarkdownPath, '-o', outfile, '--bibliography=' + bibtex_file, '--csl', csl_file])

