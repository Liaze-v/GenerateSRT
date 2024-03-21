import os


def listOFFiles():
    filesToGenerate = []
    filesToGenerateOnlyName = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            endsuffix = ""
            if name.endswith(('.mp3', '.mp4','.ts','.mkv')):
                for suffix in ('.mp3', '.mp4','.ts','.mkv'):
                    if name.endswith(suffix):
                        endsuffix = suffix
                # print(os.path.join(root, name))
                filesToGenerate.append(os.path.join(root, name))
                # filesToGenerateOnlyName.append(name.removesuffix(endsuffix))
                filesToGenerateOnlyName.append(name.removesuffix(endsuffix))
    # print(filesToGenerate)
    return filesToGenerateOnlyName

lines = listOFFiles()


with open("list.txt ", "w", encoding="utf-8") as f:
        for line in lines:
            # print(line)
            f.write(line)
            f.write('\n')