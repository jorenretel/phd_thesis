
from os.path import join, exists, getmtime, splitext, abspath
from os import listdir, makedirs
from subprocess import call


def main():
    pathToChapters = abspath('../chapters')
    chapterDirs = sorted([join(pathToChapters, directory) for directory in listdir(pathToChapters) if directory.startswith('chapter')])
    figureDirs = [join(chapterDir, 'figures/') for chapterDir in chapterDirs]
    convert_all_svg_to_pdf(figureDirs)


def convert_all_svg_to_pdf(figure_dirs):

    for figure_dir in figure_dirs:

        converted_dir = join(figure_dir, 'convertedPDF/')

        for file_name in listdir(figure_dir):

            name, ext = splitext(file_name)
            if not ext == '.svg':
                continue

            if not exists(converted_dir):
                makedirs(converted_dir)

            svg_file = join(figure_dir, file_name)
            pdf_file = join(converted_dir, name + '.pdf')

            if not exists(pdf_file) or getmtime(svg_file) > getmtime(pdf_file):

                convert_svg_to_pdf(svg_file, pdf_file)


def convert_svg_to_pdf(svg_file, pdf_file):

    call(['inkscape', svg_file, '--export-pdf=' + pdf_file])


if __name__ == '__main__':
    main()
