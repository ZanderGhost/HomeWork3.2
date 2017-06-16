import requests


def translate_it(text, translate_lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': translate_lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def read_file(file_name):
    with open(file_name, 'r') as f:
        text_for_translate = f.read()
        return text_for_translate


def write_file(file_name, text_translate):
    file_name = 'out_' + file_name
    with open(file_name, 'w') as f:
        f.write(text_translate)
        print('файл переведён')


def main():
    in_file = input('Введите имя файла:')
    in_lang = input('Введите язык текста(возможные варианты: de, es, fr):')
    out_lang = input('Введите язык на который перевести(возможные варианты: de, es, fr, ru), по умолчанию ru:')
    if out_lang == '':
        translate_lang = in_lang + '-ru'
    else:
        translate_lang = in_lang + '-' + out_lang

    text = read_file(in_file)
    text_translate = translate_it(text, translate_lang)
    write_file(in_file, text_translate)


main()
