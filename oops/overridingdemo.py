class parent:
    def properties(self) -> str:
        self.props={"mobile":"nokia","bike":"passion pro"}
        return self.props

class child(parent):
    def properties(self)->str:
