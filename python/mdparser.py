
import os
import re

imageLinePattern = re.compile(r'(.*!\[.*\]\()(.*)(\).*)')

def getMarkDownFilePaths(allChapterDir):
    
    markdownFiles = []
    
    chapterDirs = sorted([directory for directory in os.listdir(allChapterDir) if directory.startswith('chapter')])

    for chapterDir in chapterDirs:
        
        relativePathToDir = allChapterDir + '/' + chapterDir + '/'
        #print relativePathToDir
        markdownFilesForChapter = sorted([relativePathToDir + fileName for fileName in os.listdir(relativePathToDir) if fileName.endswith('.md')])
    
        markdownFiles.extend(markdownFilesForChapter)
        
    return markdownFiles


def parse(markdownPath, writeFile):
    
    parentDirectory = os.path.dirname(markdownPath)
    
    with open(markdownPath, 'r') as markdownSource:
        
        for line in markdownSource:
            
            newLine = injectAbsolutePath(line, parentDirectory)
            writeFile.write(newLine)
            print newLine
            
 
def injectAbsolutePath(line, parentDirectory):
    
    newLine = line
    match = re.match(imageLinePattern, line)
    
    if match:
        relImagePath = match.group(2)
        absImagePath = os.path.abspath(os.path.join(parentDirectory, relImagePath))
        newLine = ''.join([match.group(1), absImagePath, match.group(3)])

    return newLine
