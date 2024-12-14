# Шифр Цезаря

Данный код позволяет шифровать и дешифровать сообщения с помощью шифра Цезаря. Также приложение позволяет взломать любое зашифрованное с помощью данного шифра сообщение, подсказав, какой шаг (сдвиг) был использован в его случае. Приложение работает с сообщениями на английском языке. (Знаю, очень много "шифр" в тексте, простите)

## Описание работы приложения

Шифрование
После запуска кода пользователю нужно ввести сообщение, которое он хочет зашифровать, и выбрать величину шага. После нажатия кнопки на фрейм выводится зашифрованное сообщение, которое можно скопировать и вставить в поле ввода для дешифрования в случае необходимости. Шифрование текста осуществляется путем сдвига каждой буквы на заданное количество позиций в алфавите.

Дешифрование
Не меняя величину шага, пользователь вставляет в поле ввода для дешифрования текст из буфера обмена (или вводит сам) и, нажимая на кнопку "расшифровать", получает дешифрованный текст.

Взлом
В случае взлома необходимо ввести/вставить зашифрованный текст в первое поле ввода и нажать "Взломать текст из первого поля ввода". Код, анализируя текст и сравнивая частоту употребления букв английского алфавита, сам подбирает наилучший вариант сдвига, расшифровывает сообщение и выводит его на фрейм вместе с величиной самого вероятного использованного шага. 

## Пример

# Текст:
This was not because he was cowardly and abject, quite the contrary; but for some time past he had been in an overstrained irritable condition, verging on hypochondria. He had become so completely absorbed in himself, and isolated from his fellows that he dreaded meeting, not only his landlady, but anyone at all. He was crushed by poverty, but the anxieties of his position had of late ceased to weigh upon him. He had given up attending to matters of practical importance; he had lost all desire to do so. Nothing that any landlady could do had a real terror for him. But to be stopped on the stairs, to be forced to listen to her trivial, irrelevant gossip, to pestering demands for payment, threats and complaints, and to rack his brains for excuses, to prevaricate, to lie—no, rather than that, he would creep down the stairs like a cat and slip out unseen.

# Сдвиг: 18

# Результат шифрования:
Lzak osk fgl twusmkw zw osk ugosjvdq sfv stbwul, imalw lzw ugfljsjq; tml xgj kgew laew hskl zw zsv twwf af sf gnwjkljsafwv ajjalstdw ugfvalagf, nwjyafy gf zqhguzgfvjas. Zw zsv twugew kg ugehdwlwdq stkgjtwv af zaekwdx, sfv akgdslwv xjge zak xwddgok lzsl zw vjwsvwv ewwlafy, fgl gfdq zak dsfvdsvq, tml sfqgfw sl sdd. Zw osk ujmkzwv tq hgnwjlq, tml lzw sfpawlawk gx zak hgkalagf zsv gx dslw uwskwv lg owayz mhgf zae. Zw zsv yanwf mh sllwfvafy lg esllwjk gx hjsulausd aehgjlsfuw; zw zsv dgkl sdd vwkajw lg vg kg. Fglzafy lzsl sfq dsfvdsvq ugmdv vg zsv s jwsd lwjjgj xgj zae. Tml lg tw klghhwv gf lzw klsajk, lg tw xgjuwv lg daklwf lg zwj ljanasd, ajjwdwnsfl ygkkah, lg hwklwjafy vwesfvk xgj hsqewfl, lzjwslk sfv ugehdsaflk, sfv lg jsuc zak tjsafk xgj wpumkwk, lg hjwnsjauslw, lg daw—fg, jslzwj lzsf lzsl, zw ogmdv ujwwh vgof lzw klsajk dacw s usl sfv kdah gml mfkwwf.

# Результат дешифрования:
This was not because he was cowardly and abject, quite the contrary; but for some time past he had been in an overstrained irritable condition, verging on hypochondria. He had become so completely absorbed in himself, and isolated from his fellows that he dreaded meeting, not only his landlady, but anyone at all. He was crushed by poverty, but the anxieties of his position had of late ceased to weigh upon him. He had given up attending to matters of practical importance; he had lost all desire to do so. Nothing that any landlady could do had a real terror for him. But to be stopped on the stairs, to be forced to listen to her trivial, irrelevant gossip, to pestering demands for payment, threats and complaints, and to rack his brains for excuses, to prevaricate, to lie—no, rather than that, he would creep down the stairs like a cat and slip out unseen.

# Текст для взлома:
Nbcm qum hin vywuomy by qum wiqulxfs uhx uvdywn, kocny nby wihnluls; von zil migy ncgy jumn by bux vyyh ch uh ipylmnluchyx cllcnuvfy wihxcncih, pylacha ih bsjiwbihxlcu. By bux vywigy mi wigjfynyfs uvmilvyx ch bcgmyfz, uhx cmifunyx zlig bcm zyffiqm nbun by xlyuxyx gyyncha, hin ihfs bcm fuhxfuxs, von uhsihy un uff. By qum wlombyx vs jipylns, von nby uhrcyncym iz bcm jimcncih bux iz funy wyumyx ni qycab ojih bcg. By bux acpyh oj unnyhxcha ni gunnylm iz jluwncwuf cgjilnuhwy; by bux fimn uff xymcly ni xi mi. Hinbcha nbun uhs fuhxfuxs wiofx xi bux u lyuf nyllil zil bcg. Von ni vy mnijjyx ih nby mnuclm, ni vy zilwyx ni fcmnyh ni byl nlcpcuf, cllyfypuhn aimmcj, ni jymnylcha xyguhxm zil jusgyhn, nblyunm uhx wigjfuchnm, uhx ni luwe bcm vluchm zil yrwomym, ni jlypulcwuny, ni fcy—hi, lunbyl nbuh nbun, by qiofx wlyyj xiqh nby mnuclm fcey u wun uhx mfcj ion ohmyyh.

# Результат взлома:
Лучший вариант (Шаг 20):
This was not because he was cowardly and abject, quite the contrary; but for some time past he had been in an overstrained irritable condition, verging on hypochondria. He had become so completely absorbed in himself, and isolated from his fellows that he dreaded meeting, not only his landlady, but anyone at all. He was crushed by poverty, but the anxieties of his position had of late ceased to weigh upon him. He had given up attending to matters of practical importance; he had lost all desire to do so. Nothing that any landlady could do had a real terror for him. But to be stopped on the stairs, to be forced to listen to her trivial, irrelevant gossip, to pestering demands for payment, threats and complaints, and to rack his brains for excuses, to prevaricate, to lie—no, rather than that, he would creep down the stairs like a cat and slip out unseen.
