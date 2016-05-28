#! /usr/bin/python

import os
import re
import sys
from mdparser import parse, getMarkDownFilePaths
from convert_svg import convert_all_svg_to_pdf


#location of files:

#path were the directory with all chapters is located:
pathToChapters = os.path.abspath('../chapters')
bibtex_file = '../references/test.bib'
csl_file = '../references/plos.csl'
outfile = '../compiled/thesis.docx'
preParsedMarkdownPath = '../compiled/thesis.md'

normal_chapters = []

chapterDirs = sorted([os.path.join(pathToChapters, directory) for directory in os.listdir(pathToChapters) if directory.startswith('chapter')])
normal_chapters.extend([True]*(len(chapterDirs)-len(normal_chapters)))
chapterDirs.extend([os.path.join(pathToChapters, 'appendixA')])
                    #os.path.join(pathToChapters, 'acknowledgements'),
                    #os.path.join(pathToChapters, 'references')])
normal_chapters.extend([False]*(len(chapterDirs)-len(normal_chapters)))
figureDirs = [os.path.join(chapterDir, 'figures/') for chapterDir in chapterDirs if os.path.exists(os.path.join(chapterDir, 'figures/'))]
markdownFiles = getMarkDownFilePaths(chapterDirs)


def compile_document(biber=False, docx=False, html=False):

    if docx:
        outfile = '../compiled/thesis.docx'
    elif html:
        outfile = '../compiled/thesis.html'
    elif biber:
        outfile = '../compiled/thesis.tex'
    else:
        outfile = '../compiled/thesis.pdf'

    if not html:
        convert_all_svg_to_pdf(figureDirs)
        use_pdf_img = True
    else:
        use_pdf_img = False

    with open(preParsedMarkdownPath, 'w') as preParsedMarkdown:

        for markdownFile, normal_chapter in zip(markdownFiles, normal_chapters):

            parse(markdownFile, preParsedMarkdown, svg_to_pdf=use_pdf_img)

            if biber and normal_chapter:

                preParsedMarkdown.write('\n')
                preParsedMarkdown.write('\FloatBarrier')
                preParsedMarkdown.write(r'\addcontentsline{toc}{section}{References}')
                preParsedMarkdown.write('\n')
                preParsedMarkdown.write('\printbibliography[heading=subbibliography]')   #' \\normalsize ')
                preParsedMarkdown.write('\n')


    from subprocess import call
    if not biber:
        call(['pandoc', '-s', '--toc', '--chapters', '--smart', preParsedMarkdownPath, '../metadata.yaml', '-o', outfile, '--filter', 'pandoc-eqnos', '--filter','pandoc-fignos', '--filter', 'pandoc-tablenos', '--bibliography=' + bibtex_file, '--csl', csl_file, '--latex-engine=xelatex', '--template=../template/latex_template_pandoc116_modified.latex'])
    else:
        call(['pandoc', '-s', '--toc', '--chapters', '--smart', '--biblatex', preParsedMarkdownPath, '../metadata.yaml', '-o', outfile, '-B', '../chapters/acknowledgements/acknowledgements.tex', '--filter', 'pandoc-eqnos', '--filter','pandoc-fignos', '--filter', 'pandoc-tablenos', '--bibliography=' + bibtex_file, '--csl', csl_file, '--latex-engine=xelatex', '--template=../template/latex_template_pandoc116_modified.latex'])
        call(['xelatex', 'thesis'], cwd='../compiled')
        call(['biber', 'thesis'], cwd='../compiled')
        call(['xelatex', 'thesis'], cwd='../compiled')


if __name__ == '__main__':

    arguments = sys.argv
    if 'biber' in arguments:
        compile_document(biber=True)
    elif 'docx' in arguments:
        compile_document(docx=True)
    elif 'html' in arguments:
        compile_document(html=True)
    else:
        compile_document()