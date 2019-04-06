from moviepy.editor import VideoFileClip, concatenate_videoclips
import argparse, os

def import_clips(dir_path):
    clips = []
    for (path, dirs, files) in os.walk(dir_path):
        for file in files:
            filename = os.path.join(path, file)
            clip = VideoFileClip(filename)
            if filename[:-4] == ".webm":
                clips.append(clip)
    return clips


def make_compilation(clips, name):
    final_clip = concatenate_videoclips(clips)
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
    make_compilation(import_clips(args.directory), args.name)