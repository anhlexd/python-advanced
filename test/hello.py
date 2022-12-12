def phan_tu_lon_nhat(danhsach):
    giatri = max(danhsach)
    soluong = danhsach.count(giatri)
    dsvitri = [ vt for vt in range(len(danhsach)) if danhsach[vt] == giatri]
    return giatri, soluong, dsvitri

danhsach = input().split()
danhSachSo = list(map(float, danhsach))
#Goi thuc thi ham va truyen tham so cho ham
giaTri, soLuong, dsViTri = phan_tu_lon_nhat(danhSachSo)
print(giaTri)
print(soLuong)
#Unpacking arguments1 
print(*dsViTri)


