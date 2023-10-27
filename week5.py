#1
vehicle = [
    'B 1111 DRF','Civic','2500cc','biru'
]

#2
vehicle_edited = vehicle = ['1 miliar', '4']
vehicle_edited.insert(2, 'Honda')
vehicle_edited.insert(3, 'Sedan')
print(vehicle_edited)

#3
pilihan = input("pilih opeerasi: ")
match pilihan :
        case '1':
            panjang = 15
            lebar = 20
            print(panjang*lebar)
        case '2':
            jarijari = 7
            print(22/7 * jarijari**2)
        case '3':
            alas = 15
            tinggi = 20
            print(0,5*tinggi*alas)
            
            