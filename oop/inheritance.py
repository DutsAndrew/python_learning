# Super class because it will be inherited by sub classes
class App:
    def start(self):
        print("starting")

# is inheriting App as it is called as an argument
class Android(App):
    def get_version(self):
        print("Android version")

# is inheriting App as it is called as an argument
class iPhone(App):
    def get_version(self):
        print("iPhone version")

app = Android()
app.start()
app.get_version()
