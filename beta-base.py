# task_inp = str(input("What do you wanna do? Enter:"
#                      "\n Set operation point for transistor using voltage divider -- OPVD\n"
#                      "Count "))

beta = int(input("Enter h21e: "))
v_offs = float(input("Enter base offset voltage in volts: "))
v_be = float(input("Enter Base-Emitter voltage (usually 0.6-0.7V) in volts like showed: "))
# r_c = int(input("Enter collector resistance in Ohms: "))
r_e = int(input("Enter emitter resistance in Ohms: "))
v_sup = float(input("Enter supply voltage in volts: "))
c_v = v_sup / 2
i_c_max = (c_v / r_e)
p_c_max = c_v * i_c_max
i_c = float(input(
    "Maximum collector current is " + str(round((i_c_max * 1000), 2)) + " mA (" + str(round(p_c_max, 4)) + " W)\n" +
    " Enter collector ≈ emitter current in Amps (1mA = 0.001A): "))

# print(beta, v_offs, v_be, i_c, r_e, v_sup)

r_base = beta * abs(((v_offs - v_be) / i_c) - r_e)
r1 = r_base * (v_sup / v_offs)
r2 = 1 / ((1 / r_base) - (1 / r1))

if r_base >= 1000:
    print(str(round((r_base / 1000), 2)) + "K Base")
else:
    print(str(r_base) + " Ohms Base")

if r1 >= 1000:
    print(str(round((r1 / 1000), 2)) + "K R1")
else:
    print(str(r1) + " Ohms R1")

if r2 >= 1000:
    print(str(round((r2 / 1000), 2)) + "K R2")
else:
    print(str(r2) + " Ohms R2")
