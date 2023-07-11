# play() is now static because @staticmethod was called above it, which means it can be called without an attached object, this breaks OOP principles, but can be useful
# stop(self)is not static and therefore cannot be called without an accompanying object, this is because (self) is attached which requires an object, if it was just stop() the method would call
class Music:
    
    @staticmethod
    def play():
        print("playing music")

    def stop(self):
      print("stop playing")

Music.play()
# Music.stop()

obj = Music()
obj.stop()