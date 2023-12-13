from django.db import models

class Khoa(models.Model):
    ma_khoa = models.IntegerField(primary_key=True)
    ten_khoa = models.CharField(max_length=50)
    ma_truong_bo_mon = models.IntegerField()

    def __str__(self):
        return f"{self.ma_khoa} - {self.ten_khoa}"
    class Meta:
        db_table = 'khoa'


class Sinh_Vien(models.Model):
    mssv = models.IntegerField(primary_key=True)
    ho_ten = models.CharField(max_length=50)
    ngay_sinh = models.DateField()
    gioi_tinh = models.CharField(max_length=30)
    sdt = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    trang_thai = models.CharField(max_length=30)
    ma_khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE, db_column='ma_khoa')

    def __str__(self):
        return f"{self.mssv} - {self.ho_ten}"

    class Meta:
        db_table = 'sinh_vien'
    
class Giang_Vien(models.Model):
    mscb = models.IntegerField(primary_key=True)
    ho_ten = models.CharField(max_length=50)
    ngay_sinh = models.DateField()
    gioi_tinh = models.CharField(max_length=30)
    sdt = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    ma_khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE, db_column='ma_khoa')

    def __str__(self):
        return f"{self.mscb} - {self.ho_ten}"

    class Meta:
        db_table = 'giang_vien'
    
class Khoa_Hoc(models.Model):
    ma_khoa_hoc = models.CharField(max_length=30, primary_key=True)
    ten_khoa_hoc = models.CharField(max_length=50)
    mo_ta_khoa_hoc = models.CharField(max_length=100)
    hoc_ki = models.CharField(max_length=20)
    so_tin_chi = models.IntegerField()
    noi_dung = models.CharField(max_length=100)
    ma_khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE, db_column='ma_khoa')
    mscb = models.ForeignKey(Giang_Vien, on_delete=models.CASCADE, db_column='mscb')

    def __str__(self):
        return f"{self.ma_khoa_hoc} - {self.ten_khoa_hoc}"
    class Meta:
        db_table = 'khoa_hoc'

class De_Thi(models.Model):
    ma_de_thi = models.CharField(max_length=50, primary_key=True)
    ten_de_thi = models.CharField(max_length=50, blank=True, null=True)
    trang_thai_de_thi = models.CharField(max_length=20, blank=True, null=True)
    thoi_gian_bat_dau = models.DateField(blank=True, null=True)
    thoi_gian_ket_thuc = models.DateField(blank=True, null=True)
    hinh_thuc_de_thi = models.CharField(max_length=20, blank=True, null=True)
    huong_dan_lam_bai = models.CharField(max_length=100, blank=True, null=True)
    ma_khoa_hoc = models.ForeignKey('Khoa_Hoc', on_delete=models.CASCADE, db_column='ma_khoa_hoc')

    def __str__(self):
        return self.ma_de_thi
    
    class Meta:
        db_table = 'de_thi'

class Cau_Hoi(models.Model):
    ma_cau_hoi = models.CharField(max_length=30, primary_key=True)
    ma_de_thi = models.ForeignKey('De_Thi', on_delete=models.CASCADE, db_column='ma_de_thi')
    noi_dung_cau_hoi = models.CharField(max_length=100)
    dap_an = models.CharField(max_length=100)
    diem_so = models.IntegerField()

    def __str__(self):
        return self.ma_cau_hoi

    class Meta:
        db_table = 'cau_hoi'

class Diem(models.Model):
    ma_de_thi = models.ForeignKey('De_Thi', on_delete=models.CASCADE, db_column='ma_de_thi')
    mssv = models.ForeignKey('Sinh_Vien', on_delete=models.CASCADE, db_column='mssv')
    diem = models.IntegerField()
    trang_thai = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ma_de_thi} - {self.mssv}"
    
    class Meta:
        db_table = 'diem'
        unique_together = (('ma_de_thi', 'mssv'),)
    
class Dang_Ky(models.Model):
    id = models.AutoField(primary_key=True)
    mssv = models.ForeignKey('Sinh_Vien', on_delete=models.CASCADE, db_column='mssv')
    ma_khoa_hoc = models.ForeignKey('Khoa_Hoc', on_delete=models.CASCADE, db_column='ma_khoa_hoc')

    def __str__(self):
        return f"{self.mssv} - {self.ma_khoa_hoc}"

    class Meta:
        db_table = 'dang_ky'
        unique_together = (('mssv', 'ma_khoa_hoc'),)