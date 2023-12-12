# Mờ hóa tần suất tập luyện

so_lan_tap_luyen_moi_tuan_gan_day = 6 # lần
thoi_gian_tap_luyen_moi_buoi = 2 # giờ

thoi_gian_tap_trung_binh_moi_tuan = so_lan_tap_luyen_moi_tuan_gan_day * thoi_gian_tap_luyen_moi_buoi # giờ

print("Thời gian tập trung bình mỗi tuần: ", thoi_gian_tap_trung_binh_moi_tuan, " giờ")


# Định nghĩa số lượng hoạt động
so_lan_nhay_day = 10
so_lan_hit_dat = 20
so_km_chay_bo = 5
so_lan_keo_xa = 15
so_m_boi_duoc = 1000

# Định nghĩa calo tiêu thụ cho mỗi hoạt động
calo_nhay_day = 2
calo_hit_dat = 3
calo_chay_bo = 10
calo_keo_xa = 3
calo_boi = 2

# Tính lượng calo trung bình cho sức bền
calo_trung_binh = (1 * so_lan_nhay_day * calo_nhay_day + 2 * so_lan_hit_dat * calo_hit_dat + 3 * so_km_chay_bo * calo_chay_bo + 4 * so_lan_keo_xa * calo_keo_xa + 5 * so_m_boi_duoc * calo_boi) / (1 + 2 + 3 + 4 + 5)

print("Lượng calo trung bình cho sức bền: ", calo_trung_binh)