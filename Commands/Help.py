class Help:
    def set_class_list(self, classes):
        self.__classes = classes

    def use(self, msg):
        msg = msg.content.split(" ")

        if len(msg) > 1:
            command = self.__classes.get(msg[1])
            if command: return f"```{command.helping()}```", False
        
        out = "\n".join(command.helping() for command in self.__classes.values())
        return f"```{out}```", False

    def get_keyword(self):
        return "help"

    def helping(self):
        return f"|{self.get_keyword()} [Command] - Tells you stuff about the commands"
