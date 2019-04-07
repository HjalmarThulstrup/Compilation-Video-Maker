from moviepy.editor import VideoFileClip, concatenate_videoclips
import argparse, os

def import_clips(dir_path):
    clips = []
    for filename in os.listdir(dir_path):
        if filename.endswith('.webm'):
            clips.append(VideoFileClip(dir_path + filename))
    return clips


def make_compilation(clips, name):
    final_clip = concatenate_videoclips(clips, method='compose')
    try:
        final_clip.write_videofile(name)
        print("Compilation saved as " + name)
    except:
        print("Compilation failed")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A script that makes compilation videos from a directory of clips')
    parser.add_argument('-d', '--directory', help='The absolute path to the directory of clips you want to use.')
    parser.add_argument(
        '-n', '--name', help="The name and file extension you want to give the compilation video.")
    args = parser.parse_args()
    _dir = args.directory
    name = args.name
    if _dir != None:
        if _dir[-1:] != "/" or _dir[-1:] != "\\":
            _dir = _dir + "/"
    make_compilation(import_clips(_dir), name)