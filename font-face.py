import os
import glob
import argparse
from subprocess import Popen, PIPE


def make_font_face():
    directory_arg = 'directory'
    parser = argparse.ArgumentParser(description='Make font-face css / sccs.')
    parser.add_argument(directory_arg)
    args = parser.parse_args()

    for k, v in args.__dict__.items():
        print(k, v)

    print(args.__dict__[directory_arg])

    my_dir = args.__dict__[directory_arg]

    if my_dir.startswith('.'):
        new_dir = os.path.realpath(my_dir)
    else:
        new_dir = my_dir

    if not os.path.isdir(new_dir):
        new_dir = os.path.dirname(new_dir)

    p = os.getcwd()
    os.chdir(new_dir)

    text = ""
    merged_file_name = os.path.basename(os.path.normpath(new_dir)) + ".css"

    for file in os.listdir(new_dir):
        if file.endswith('.ttf'):
            process = Popen(['sfnt2woff', file], stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()
            print(output)

            process = Popen(['woff2_compress', file], stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()
            print(output)

            process = Popen(['convert2svgfont.pe', file], stdout=PIPE)
            (output, err) = process.communicate()
            process.wait()
            print(output)

            filename = file[:len(file) - 4]
            css = filename + '.css'
            template = """

@font-face {
    font-family: "%s";
    src: url('#{$path}/%s.woff2') format('woff2'),
         url('#{$path}/%s.woff') format('woff'),
         url('#{$path}/%s.svg#%s') format('svg'),
         url('#{$path}/%s.ttf') format('ttf');   
}
            

            """
            s= template % (filename, filename, filename, filename, filename, filename)
            text +=s
            css_file = open(os.path.join(new_dir, css), "w+")
            css_file.write(s)
            css_file.close()
    merged_file = open(os.path.join(new_dir, merged_file_name), "w+")
    merged_file.write(text)
    merged_file.close()
    os.chdir(p)


if __name__ == '__main__':
    make_font_face()
