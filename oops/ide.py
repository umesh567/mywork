class Editor:
    def functionalities(self):
        self.funcs=["create file","execute","save"]

        return self.funcs

class pycharm(Editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["debug","version control"])
        return funcs

pyc=pycharm()
print(pyc.functionalities())