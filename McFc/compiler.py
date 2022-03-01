class Compile():
    def Normal(self, COMP, filename):
        self.compile_stack = COMP
        self.compiled = "scoreboard objectives add TEMP dummy \nscoreboard players set #McFc TEMP 0\n\n"

        for CHUNK in self.compile_stack:
            if CHUNK[0] == "v": # Define Vars
                self.compiled = self.compiled + "scoreboard objectives add " + CHUNK[1] + " dummy \nscoreboard players set #McFc " + CHUNK[1] + " " + str(CHUNK[2]) + "\n"

            if CHUNK[0] == "m": # + -
                if CHUNK[1] == "+=":
                    self.compiled = self.compiled + "scoreboard players set #McFc TEMP 0\nscoreboard players operation #McFc TEMP " + CHUNK[1] + " #McFc " + CHUNK[3] + "\nscoreboard players operation #McFc TEMP " + CHUNK[1] + " #McFc " + CHUNK[4] + "\nscoreboard players operation #McFc " + CHUNK[2] + " = #McFc TEMP\n"
                elif CHUNK[1] == "-=":
                    self.compiled = self.compiled + "scoreboard players set #McFc TEMP 0\nscoreboard players operation #McFc TEMP " + \
                                    "+=" + " #McFc " + CHUNK[3] + "\nscoreboard players operation #McFc TEMP " + \
                                    CHUNK[1] + " #McFc " + CHUNK[4] + "\nscoreboard players operation #McFc " + CHUNK[
                                        2] + " = #McFc TEMP\n"
                else:
                    self.compiled = self.compiled + "scoreboard players set #McFc TEMP 0\nscoreboard players operation #McFc TEMP " + \
                                    "+=" + " #McFc " + CHUNK[3] + "\nscoreboard players operation #McFc TEMP " + \
                                    CHUNK[1] + " #McFc " + CHUNK[4] + "\nscoreboard players operation #McFc " + CHUNK[
                                        2] + " = #McFc TEMP\n"


        print("Done")
        f = open(filename + ".txt", "w")
        f.write(self.compiled)
        f.close()