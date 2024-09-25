def index_text(text: str):
    """
    return list yang berisi dictionary dengan format {'char': '<character text>', 'index': '<index character>'}

    contoh: [{'char': 'a', 'index': 0}, {'char': 'k', 'index': '1'}]

    Yang perlu diperhatikan:

    html tag index adalah None. Jadi karakter <, > dan / yang ada di dalam kurung, serta huruf yang didalamnya harus None

    contoh: <b>a</b> c
    < None
    b None
    > None
    a 0
    < None
    / None
    b None
    > None
      1 <= ini indexnya spasi
    c 2

    Beberapa konsep yang membantu di dasar python:
    1. string bisa di loop, pakai for
    2. list dan bagaimana menambah item ke list
    3. increment variable
    4. dictionary, bagaimana cara buat dictionary

    """
    

    
    characters = []
    
    index = 0
    
   
    
    for huruf in text:
        huruf_dict = {'char': huruf, 'index': index}
       
    
        characters.append(huruf_dict)
        index += 1
      
        
        
    return characters
kalimat = "saya sedang belajar pyhton"
result = index_text(kalimat)
    
print(result)  
    # TODO: 1. loop text
    # TODO: 2. setiap character buat dictionary sementara dengan format: {'char': character, 'index': index}
    # TODO: 3. tambahkan dictionary sementara ke characters list
    # TODO: 4. naikkan 1 variable index. Maksudnya, kalau sekarang 0, maka nanti jadi 1 tiap kali tambah character
    # TODO: 5. return characters
    
def wrap_tag(indexedText, start, end):
    """
    Berbekal fungsi diatas. Kamu sudah mendapatkan start dan end index.
    Kamu hanya perlu mengubah text character nya.

    bila indexnya adalah start maka tambahkan sebelum characternya
    bila indexnya adalah end, maka tambahkan setelah characternya

    contoh start 0 end 1 dari kata 'aku'
    a 0
    k 1
    u 2

    start == 0, char adalah a. Maka hasilnya: <b>a
    end == 1, char adalah k. Maka hasilnya k</b>

    Hasil akhir dari kembalian fungsinya adalah

    [
    {'char': '<b>a', 'index': 0},
    {'char': 'k</b>', 'index': 1},
    {'char': 'u', 'index': 2},
    ]

    Beberapa konsep yang membantu:
    1. Loop
    2. Akses value dari dictionary
    3. mengubah valua dari dictionary
    4. Manipulasi text
    """
    # TODO: 1. loop indexedText (ini adalah kembalian dari fungsi index_text)
    # TODO: 2. check apakah index tiap item sama dengan start. Bila iya, maka bentuk char menjadi <b>{character}. Jadi misal character adalah 'a' maka jadi '<b>a'.
    # TODO: 3. check apakah index tiap item sama dengan end. Bila iya, maka bentuk char menjadi {character}</b>. Jadi misal character adalah 'b', maka jadi 'b</b>'
    # TODO: 4. return indexText lagi
    

    format_text = []

    for item in indexedText:
        index = item ['index']
        character = item ['char']
        
        
        if index == start:
            format_text.append({'char': f'<b>{character}', 'index': index})
        elif  index == end:
            format_text.append({'char': f'{character}</b>', 'index': index})
        else:
            format_text.append(item)
    return format_text

def main():
    text1 = "aku sedang belajar python"
    indexed_text = index_text(text1)
    final_chars = wrap_tag(indexed_text, 4, 9)
    expected1 = "aku <b>sedang</b> belajar python"
    assert expected1 == "".join([text["char"] for text in final_chars])

    # text2 = "aku <i>sedang</i> belajar python"
    # expected2 = "aku <i><b>sedang</b></i> belajar python"
    # indexed_text = index_text(text2)
    # final_chars = wrap_tag(indexed_text, 4, 9)
    # assert expected2 == "".join([text["char"] for text in final_chars])

    print(expected1)
if __name__ == "__main__":
    main()