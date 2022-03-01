

class Function():
    def __init__(self):
        # Vars
        self.vars = []

        # Add To Compile List
        self.COMP = []


    # Variables

    def Var(self, name, value):
        if type(value) == int:
            Check = False
            for var in self.vars:
                if var[0] == name:
                    print("Var Already Defined")
                    Check = True

            if Check == False:
                self.vars.append([name, value])
                self.COMP.append(["v", name, value])

        else:
            print("Var Not Defined Since Value Not Integer")

    def Get_Vars(self, var = None):
        if var == None:
            return self.vars
        else:
            for VAR in self.vars:
                if VAR[0] == var:
                    return VAR


    def Get_Var_Int(self, var):
        for VAR in self.vars:
            if VAR[0] == var:
                return VAR[1]

    # Opperations

    def Add(self, OutputVar, var1, var2): # Make Temp Vars For It
        for VAR in self.vars:
            if VAR[0] == var1:
                varA = VAR
            elif VAR[0] == var2:
                varB = VAR
            elif VAR[0] == OutputVar:
                varC = VAR
            else:
                pass

        i = self.vars.index(varC)
        NewVar = varA[1] + varB[1]
        self.vars.pop(i)
        self.vars.insert(i, [varC[0], NewVar])
        self.COMP.append(["m", "+=", varC[0], varA[0], varB[0]])


    def Minus(self, OutputVar, var1, var2): # Make Temp Vars For It
        for VAR in self.vars:
            if VAR[0] == var1:
                varA = VAR
            elif VAR[0] == var2:
                varB = VAR
            elif VAR[0] == OutputVar:
                varC = VAR
            else:
                pass

        i = self.vars.index(varC)
        NewVar = varA[1] - varB[1]
        self.vars.pop(i)
        self.vars.insert(i, [varC[0], NewVar])
        self.COMP.append(["m", "-=", varC[0], varA[0], varB[0]])


    def Times(self, OutputVar, var1, var2): # Make Temp Vars For It
        for VAR in self.vars:
            if VAR[0] == var1:
                varA = VAR
            elif VAR[0] == var2:
                varB = VAR
            elif VAR[0] == OutputVar:
                varC = VAR
            else:
                pass

        i = self.vars.index(varC)
        NewVar = varA[1] * varB[1]
        self.vars.pop(i)
        self.vars.insert(i, [varC[0], NewVar])
        self.COMP.append(["m", "*=", varC[0], varA[0], varB[0]])

    def Divide_Clean(self, OutputVar, var1, var2): # Make Temp Vars For It
        for VAR in self.vars:
            if VAR[0] == var1:
                varA = VAR
            elif VAR[0] == var2:
                varB = VAR
            elif VAR[0] == OutputVar:
                varC = VAR
            else:
                pass

        i = self.vars.index(varC)
        NewVar = varA[1] // varB[1]
        self.vars.pop(i)
        self.vars.insert(i, [varC[0], NewVar])
        self.COMP.append(["m", "/=", varC[0], varA[0], varB[0]])

    def SetVar(self,VarToSet, SetToVar):
        if type(SetToVar) == int:
            for VAR in self.vars:
                if VAR[0] == VarToSet:
                    varA = VAR

            i = self.vars.index(varA)
            self.vars.pop(i)
            self.vars.insert(i, [varA[0], SetToVar])

            self.COMP.append(["sv", "int", varA[0], SetToVar])

        else:
            for VAR in self.vars:
                if VAR[0] == VarToSet:
                    varA1 = VAR
                if VAR[0] == SetToVar:
                    varB1 = VAR

            x = self.vars.index(varA1)
            self.vars.pop(x)
            self.vars.insert(x, [varA1[0], varB1[1]])
            self.COMP.append(["sv", "var", varA1[0], varB1[0]])


    # Execute Commands (Oh God)

    def execute(self, As = "@s", Pos="~ ~ ~", Command = None):
        pass


    def Get_Function(self):
        return self.COMP










