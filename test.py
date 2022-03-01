from McFc import mcfunction, compiler

mf = mcfunction.Function()

mf.Var("var1", 1)
mf.Var("var2", 2)
mf.Var("var3", 0)
mf.Var("var4", 10)

# Math Stuff

mf.Add("var3", "var1", "var2") # 3
print("Add")
mf.Minus("var1", "var2", "var3") # -1
print("Var1: ", mf.Get_Vars("var1"))
mf.Times("var1", "var2", "var3") # 6
print("Var2 * Var3: ", mf.Get_Var_Int("var1"))
mf.Divide_Clean("var2", "var1", "var3")# 2
print("All Vars: ", mf.Get_Vars("var2"))

# Other Stuff With Vars

mf.SetVar("var3", "var4")
print("Var3: ", mf.Get_Var_Int("var3"))

mf.execute("@e[type=player]", "~ ~ ~")

Function = mf.Get_Function()

comp = compiler.Compile()
comp.Normal(Function, "File")




