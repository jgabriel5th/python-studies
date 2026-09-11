# Class Relationships: association, aggregation, and composition
# Association is a type of relationship which objects are linked
# within the system.
# That is the most common relationship between objects and it has subsets
# like agregation and composition.
# Usually, an association happens when an object has an attribute that references
# another object.
# The association does not specify how an object controls the life cycle of  
# another object.
class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool

class WritingTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing...'

writer = Writer('John')
pen = WritingTool('Expensive Pen')
writing_machine = WritingTool('Writing Machine')
writer.tool = writing_machine # Association
print(pen.write())
print(writer.tool.write())