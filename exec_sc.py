import utils, gen_yahei_sc, gen_simsun_sc

if __name__ == '__main__':

    gen_yahei_sc.gen_yahei_regular_sc()
    gen_yahei_sc.gen_yahei_bold_sc()
    gen_yahei_sc.gen_yahei_light_sc()
    print('yahei sc successfully generated')

    gen_simsun_sc.gen_simsun_sc()
    gen_simsun_sc.gen_simsun_ext_sc()
    print('simsun sc successfully generated')


