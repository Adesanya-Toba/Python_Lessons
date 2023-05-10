'''Different behaviors happen depending on which subclass is being used,
without having to explicitly know what the subclass actually is.'''

from pathlib import Path

class AudioFile:
    ext:str
    def __init__(self, filepath:Path) -> None:
        if not filepath.suffix == self.ext:
            raise Exception('Invalid file format')
        self.filepath = filepath


class MP3File(AudioFile):
    ext = '.mp3'
    def play(self) -> None:
        print('Playing {} as mp3'.format(self.filepath))

class WaveFile(AudioFile):
    ext = '.wav'
    def play(self) -> None:
        print('Playing {} as wav'.format(self.filepath))

class OggFile(AudioFile):
    ext = '.ogg'
    def play(self) -> None:
        print('Playing {} as ogg'.format(self.filepath))

def main() -> None:
    file1 = MP3File(Path('toba.mp3'))
    file1.play()


if __name__ == '__main__':
    main()