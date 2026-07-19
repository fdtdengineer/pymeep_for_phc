import math
import itertools


from pathlib import Path

script_dir = Path(__file__).resolve().parent
fig_dir = script_dir / "fig"
out_dir = script_dir / "out"
fig_dir.mkdir(exist_ok=True)
out_dir.mkdir(exist_ok=True)

#PhC 1ユニットを作る
def unit_1(a, nx, ny, x_offset, y_offset, layer, obj, cavity, barrier, wgi, hole_shift):
	x_shift = a*math.sqrt(3)/2 # 0.3464
	y_shift = a
	wgi_shift = (wgi-1)*a*math.sqrt(3)
	output = list()
	x_center = x_offset - nx * x_shift
	y_center = y_offset - ny * y_shift / 2

	for j in range(nx+1):
		for i in range(ny+1):
			if 2*j == nx and abs(2*i - ny ) <= cavity - 1: #中央のcavityを作製
				continue
			elif 2*j == nx - (barrier + 1) and 2*i <= ny - cavity - barrier - 6: #結合導波路 左（バリア領域の長さが奇数のとき）
				continue
			elif 2*j == nx + (barrier + 1) and 2*i >= ny + cavity + barrier + 6: #結合導波路 右（バリア領域の長さが奇数のとき）
				continue
			else:
				if 2*j == nx and abs(2*i - ny ) == cavity + 1: #両脇のcavityの穴シフト
					y = y_center + y_shift*i + hole_shift*a*(2*i - ny)/abs(2*i - ny)
				else:
					y = y_center + y_shift*i
				if 2*j < nx - (barrier + 1) and 2*i <= ny - cavity - barrier - 6 + 1: #結合導波路 左 を (wgi-1)だけ下にシフト
					x = x_center + 2*x_shift *j - wgi_shift
				elif 2*j > nx + (barrier + 1) and 2*i >= ny + cavity + barrier + 6 - 1:#結合導波路 右 を (wgi-1)だけ上にシフト
					x = x_center + 2*x_shift *j + wgi_shift
				else:
					x = x_center + 2*x_shift *j
#				print("-insert")
#				print(obj)
#				print("{:.4f},{:.4f}".format(x, y))
#				print("\n\n")
				output.append("-insert")
				output.append(obj)
				output.append("{:.4f},{:.4f}".format(x, y))
				output.append("\n\n")

	for j in range(nx):
		for i in range(ny):
			if 2*j == nx - (barrier + 2) and 2*i <= ny - cavity - barrier - 6: #結合導波路 左（バリア領域の長さが偶数のとき）
				continue
			elif 2*j == nx + barrier and 2*i >= ny + cavity + barrier + 4: #結合導波路 右（バリア領域の長さが偶数のとき）
				continue
			else:
				y = y_center + y_shift/2 + y_shift*i
				if 2*j < nx - (barrier + 2) and 2*i <= ny - cavity - barrier - 6 + 1: #結合導波路 左 を (wgi-1)だけ下にシフト
					x = x_center + x_shift + 2*x_shift *j - wgi_shift
				elif 2*j > nx + barrier and 2*i >= ny + cavity + barrier + 4 - 1:
					x = x_center + x_shift + 2*x_shift *j + wgi_shift
				else:
					x = x_center + x_shift + 2*x_shift *j
    #print("-insert")
    #print(obj)
    #print("{:.4f},{:.4f}".format(x, y))
    #print("\n\n")
				output.append("-insert")
				output.append(obj)
				output.append("{:.4f},{:.4f}".format(x, y))
				output.append("\n\n")
	return output


def unit(a, nx, ny, x_offset, y_offset, layer, obj, cavity, barrier, wgi, hole_shift):
	output = unit_1(a, nx, ny, x_offset, y_offset, layer, obj, cavity, barrier, wgi, hole_shift)
	lattice_const = str(int(a*1000))
	barrier_str = str(barrier)
	wgi_str = str(wgi)
	cavity_name = str(cavity)
	filename = "L" + cavity_name  + "_a" + lattice_const + "_c" + barrier_str + "_wgi" + wgi_str + ".scr"

	f = open(out_dir / filename, 'w') #ファイル書き出し
	for i in range(0,len(output)):
		f.write(output[i] + "\n")
	f.close()


#PhCを並べる
def arrange_photonic_crystal(a, nx, ny, layer, obj, cavity, barrier, wgi, num_units_x, num_units_y, x_shift, y_shift, x_offset, y_offset, hole_shift):
	output = list()
	for j in range(num_units_y):
		for i in range(num_units_x):
			unit_x_offset = x_offset + x_shift*i
			unit_y_offset = y_offset + y_shift*j
			output.append(unit_1(a, nx, ny, unit_x_offset, unit_y_offset, layer, obj, cavity, barrier, wgi, hole_shift))

	out = list(itertools.chain.from_iterable(output))

	lattice_const = str(int(a*1000))
	barrier_str = str(barrier)
	wgi_str = str(wgi)
	n_x = str(num_units_x)
	n_y = str(num_units_y)
	x_offset_str = str(x_offset)
	y_offset_str = str(y_offset)

	cname = str(cavity)
	filename = "L" + cname + "_a" + lattice_const + "_c" + barrier_str + "_wgi" + wgi_str + "_spoint[" + x_offset_str + "," + y_offset_str + "]_arrange[" + n_x + "," + n_y + "].scr"

	f = open(out_dir / filename, 'w') #ファイル書き出し
	for i in range(0,len(out)):
		f.write(out[i] + "\n")
	f.close()
