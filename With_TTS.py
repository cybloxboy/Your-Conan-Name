from gtts import gTTS
import playsound

print('ชื่อตอนโคนันฉบับคุณ\n')

days = {
    'จันทร์': 'คดีฆาตกรรม',
    'อังคาร': 'คดีปริศนา',
    'พุธ': 'คดีลักพาตัว',
    'พฤหัสบดี': 'อาถรรพ์',
    'ศุกร์': 'คดีประหลาด',
    'เสาร์': 'โศกนาฏกรรม',
    'อาทิตย์': 'ปริศนา'
}
months = {
    1: 'เหนือน่านฟ้า',
    2: 'ในห้องปิดตาย',
    3: 'แห่งความตาย',
    4: 'มรณะ',
    5: 'ที่หายไป',
    6: 'ที่พิโรธ',
    7: 'ที่ถูกลืม',
    8: 'เจ้าปัญหา',
    9: 'ที่แสนพิลึก',
    10: 'แห่งศตวรรษ',
    11: 'กับองค์กรชุดดำ',
    12: 'ทรยศ'
}


def find_conan_name():
    day = input('คุณเกิดวันอะไร: วัน')
    food = input('สิ่งที่คุณกินล่าสุดคืออะไร: ')
    try:
        month = int(input('คุณเกิดเดือนอะไร (ใส่เป็นตัวเลข): '))
        if month <= 0 or month > 12:
            raise Exception
        else:
            if day in days and month in months:
                print('\nชื่อตอนโคนันของคุณก็คือ\n')
                print(days.get(day) + food + months.get(month))
                tts = gTTS(
                    text='ชื่อตอนโคนันของคุณก็คือ' + days.get(day) + food + months.get(month), lang='th'
                )
                tts.save('Speak.mp3')
                playsound.playsound('Speak.mp3', True)
            else:
                print('Nan: โปรดใส่ให้ถูกต้อง')
                find_conan_name()
    except:
        print('Nan: โปรดใส่ให้ถูกต้อง\n')
        find_conan_name()


find_conan_name()
