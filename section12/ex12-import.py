# import gift_module as gm # alias 별칭 
from gift_module import gift, wedding

wedding_note = wedding
# gift_module.gift(wedding_note, '김일남', 100)
# gm.gift(wedding_note, '김일남', 100)
gift(wedding_note, '김이남', 500)

print(wedding_note)