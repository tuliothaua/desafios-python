# This Program Calculates Total in USD.

#[VAR] :: Creating the Entry!
pesos = float(input("What do you have left in pesos? "))
soles = float(input("What do you have left in soles? "))
reais = float(input("What do you have left in reais? "))

#[FUNC] :: Converting to USD!
usd = (pesos * 0.045) + (soles * 0.30) + (reais * 0.19)

#[EXEC] :: Spittin on the Screen!
print(usd)