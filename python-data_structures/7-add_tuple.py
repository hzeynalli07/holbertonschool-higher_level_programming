#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər iki tuple-ı genişləndiririk: əgər az element varsa 0 əlavə edirik
    # Slicing [:2] bizə yalnız ilk iki elementi verir
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    res_1 = a[0] + b[0]
    res_2 = a[1] + b[1]
    
    return (res_1, res_2)
