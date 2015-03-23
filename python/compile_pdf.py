#! /usr/bin/python

import os
import re
from mdparser import parse, getMarkDownFilePaths
from convert_svg import convert_all_svg_to_pdf


#location of files:

#path were the directory with all chapters is located:
pathToChapters = os.path.abspath('../chapters')
bibtex_file = '../references/test.bib'
csl_file = '../references/plos.csl'
outfile = '../compiled/thesis.pdf'
preParsedMarkdownPath = '../compiled/thesis.md'

chapterDirs = sorted([os.path.join(pathToChapters, directory) for directory in os.listdir(pathToChapters) if directory.startswith('chapter')])
figureDirs = [os.path.join(chapterDir, 'figures/') for chapterDir in chapterDirs]

markdownFiles = getMarkDownFilePaths(chapterDirs)

convert_all_svg_to_pdf(figureDirs)


with open(preParsedMarkdownPath, 'w') as preParsedMarkdown:

    for markdownFile in markdownFiles:

        parse(markdownFile, preParsedMarkdown)


from subprocess import call


call(['pandoc', '-s', '--toc', '--chapters', preParsedMarkdownPath, '-o', outfile, '--bibliography=' + bibtex_file, '--csl', csl_file, '--latex-engine=xelatex', '--template=../template/simple_template.latex'])

#call(['pandoc', '-s', '--toc', '--chapters', preParsedMarkdownPath, '-o', outfile, '--bibliography=' + bibtex_file, '--csl', csl_file])

