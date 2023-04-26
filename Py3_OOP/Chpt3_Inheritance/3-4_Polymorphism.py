'''Different behaviour happen depending on which subclass is being used,
without having to explicitly know what the subclass actually is.'''

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid file format')
        
        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('Playing {} as mp3'.format(self.filename))

class WaveFile(AudioFile):
    ext = 'wav'
    def play(self):
        print('Playing {} as wav'.format(self.filename))

class OggFile(AudioFile):
    ext = 'ogg'
    def play(self):
        print('Playing {} as ogg'.format(self.filename))

def main():
    file1 = MP3File('toba.mp3')
    file1.play()


if __name__ == '__main__':
    main()