class Engineer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool

class BuildTool:
    def __init__(self, name, building=False):
        self.name = name
        self.building = building

    def build(self):
        if self.building:
            return f'{self.name} is already being used...'
        
        self.building = True
        return f'{self.name} is being used...'

    def stop_build(self):
        if not self.building:
            return f'{self.name} is already not being used...'

        self.building = False
        return f'{self.name} is not being used...'


eng1 = Engineer('John')
build_tool = BuildTool('Hammer')
eng1.tool = build_tool
print(eng1.tool.build())
print(eng1.tool.build())
print(eng1.tool.stop_build())
print(eng1.tool.stop_build())

        
