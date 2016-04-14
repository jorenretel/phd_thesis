
import os
import re

imageLinePattern = re.compile(r'(.*!\[.*\]\()(.*)(\).*)')

def getMarkDownFilePaths(chapterDirs):

    markdownFiles = []

    for chapterDir in chapterDirs:

        markdownFilesForChapter = sorted([os.path.join(chapterDir, fileName) for fileName in os.listdir(chapterDir) if fileName.endswith('.md')])
        markdownFiles.extend(markdownFilesForChapter)

    return markdownFiles


def parse(markdownPath, writeFile, svg_to_pdf=True):

    parentDirectory = os.path.dirname(markdownPath)

    with open(markdownPath, 'r') as markdownSource:

        for line in markdownSource:

            newLine = manipulate_image_paths(line, parentDirectory, svg_to_pdf=svg_to_pdf)
            writeFile.write(newLine)



def manipulate_image_paths(line, parentDirectory, svg_to_pdf=True):

    newLine = line
    match = re.match(imageLinePattern, line)

    if match:
        relImagePath = match.group(2)

        # Replace relative path by absolute path.
        absImagePath = os.path.abspath(os.path.join(parentDirectory, relImagePath))

        filePath, fileName = os.path.split(absImagePath)
        fileName, fileExtension = os.path.splitext(fileName)

        # All svg files are already pre-converted to pdf, so these are used.
        if fileExtension == '.svg' and svg_to_pdf:
            absImagePath = os.path.join(filePath, 'convertedPDF', fileName + '.pdf')

        newLine = ''.join([match.group(1), absImagePath, match.group(3)])

    return newLine
