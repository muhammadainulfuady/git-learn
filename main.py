mahasiswa = {
    "nama":"Muhammad Ainul Fuady",
    "jurusan":"Teknik Mesin",
    "hobi":"Ngoding"
}



def searchKosonan(data):
    temp = []
    kosonan = "aiueoAIUEO"
    for dt in data:
        if dt in kosonan:
            temp.append(dt)
    return temp
print(searchKosonan("ainulfuady"))