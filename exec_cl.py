import utils, gen_yahei_cl, gen_simsun_cl

if __name__ == '__main__':

    gen_yahei_cl.gen_yahei_regular_cl()
    gen_yahei_cl.gen_yahei_bold_cl()
    gen_yahei_cl.gen_yahei_light_cl()
    print('yahei cl successfully generated')

    gen_simsun_cl.gen_simsun_cl()
    gen_simsun_cl.gen_simsun_ext_cl()
    print('simsun cl successfully generated')


