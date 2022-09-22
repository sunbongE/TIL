from django.shortcuts import render
import random

# Create your views here.
def menu(request):

    imgs = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA1MjJfMTcz%2FMDAxNTkwMTIzNTIzMTY4.fNHJFXY-1gq_b1CAiTaAKU2SEOlzZlvx7v0PcdMjGsQg.imavZG-6Gevyx899KCF9GV3vkral_USf5O7HsFdQ5hsg.JPEG.dmswls6351%2Fvintz_.jpg&type=sc960_832',
    'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fcdn.crowdpic.net%2Fdetail-thumb%2Fthumb_d_51CA10C1F025E0DB85D63BF0F2FEF295.jpg&type=a340',
    'https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAyMDA2MjZfNjUg%2FMDAxNTkzMTM4NjM1NTkz.MOZNj_EU1KVknK6t00c7PP5ImQXRiVyBQXwv0E20u8Ig.Y8H6mWmzZrlFRgGeEGsRFy8tbhFWjWMayDUE2rL4hYsg.PNG%2Fpizza_PNG44032.png&type=a340',
    'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA2MDdfMjMg%2FMDAxNjU0NTMyMjAyNzIy.mnjtMD51pbYGMF6tg8znEOibi5ybOiSBZYQQTf8buOYg.DTLwWjjDerXE4Jp1sT8s_dP1BgAWysoZW_J0xmSzfyQg.JPEG.dongsin3642%2FCay8c1wjHxB12tp0yy%25A3%25DFW6Y1%25A3%25DFqoGeBio9tbVisigGiEo%25A3%25ADrpTyo9SbqCFIf1NoUy2mXz4%25A3%25DF2C2FVVyf.jpg&type=sc960_832',
    'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA4MzBfNzMg%2FMDAxNjYxODM0MTgwMzQ2.fzCYMhCCS3XN20fBiyvPK00unduvSqXOAgjenQV_ywwg.bXEimoxfBuMqd7Na2G15oYpG-PTq_59QrrntGvQLm0Ag.JPEG.flower6978%2F20220805%25A3%25DF122309.jpg&type=a340',
    'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA4MTBfOTIg%2FMDAxNjYwMTA2NzM1ODcx.rehJpBb_8S5gbS14yQzWhz3L5_n6SAOgnjGb71AqaC8g.yuBGI2OtcHKZduZB0P1PLafo6lRHl_oq02HW7rK5Vysg.JPEG.bububuks%2FIMG_3829.jpg&type=a340',
    'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8369739%2F83697394979.3.jpg&type=f372_372'
    ]

    menus = ['라면','파스타','피자','치킨','떡볶이','다이어트 도시락','쉐이크']
    
    foodimg = random.choice(imgs)
    ind = imgs.index(foodimg)
    recom = menus[ind]

    context = {
        'recom':recom,
        'img' : foodimg
    }

    return render(request,'index.html', context)