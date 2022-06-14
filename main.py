from cnn import train
from vigna_parser import aio_transform


if __name__ == '__main__':
    f_vigna = "/Users/andrejbavykin/Desktop/data/vigna-2021-v4-vqtl-all-utf-v2.h5"
    #f_vigna = "/Users/mariia/Desktop/data/vigna-2021-v4-vqtl-tr-val-utf.h5"
    f_weather = "/Users/andrejbavykin/Desktop/data/vigna-weather.h5"

    #aio_transform(f_vigna, f_weather)  #(28, 5, 3)
    train()


