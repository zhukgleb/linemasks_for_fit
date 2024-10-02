import numpy as np 
# Пока все еще не вычещается мусор полностью


find_element = "FeI"
fname = "a_com.lin"

# line_data = np.genfromtxt(fname, delimiter="  ", dtype=[("wavelenght", float), ("ion", 'U10')],  invalid_raise = False)
line_data = np.genfromtxt(fname, dtype=[("wavelenght", float), ("ion", 'U10')], delimiter=[7, 10])
el_indexes = []
print(line_data["ion"])
for i in range(len(line_data)):
    try:
        ion_name = str(line_data[i]["ion"])
        if ion_name[0].isnumeric():
            ion_name.replace(ion_name[0], "")
        pass
    except IndexError:
        print(f"Check the line number {i}")
        break  # Если не нужно, чтобы программа показывала на проблемы, а просто продолжала работу -- закомментировать
    
    if ion_name.find(find_element) != -1:
        el_indexes.append(i)
    line_data[i]["ion"] = ion_name.strip()
print(line_data["ion"])



line_data = line_data[el_indexes]
for x in range(len(line_data)):
    line_data[x]["ion"] = line_data[x]["ion"] + "\r"

line_data = line_data[line_data["wavelenght"].argsort()]
np.savetxt("rework_" + fname, line_data, fmt='%f %s')