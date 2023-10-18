import shutil as fs
import fontforge as ff
import gen_yahei


DOWNLOAD_DIR = '/tmp'
OUTPUT_DIR = '/tmp/out'
COPYRIGHT = 'sarasa2yahei'


def set_simsun_names(font):
    font.fontname = 'SimSun'
    font.familyname = 'SimSun'
    font.fullname = 'SimSun'
    font.version = gen_yahei.get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'SimSun'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'SimSun'),
        ('English (US)', 'Fullname', 'SimSun'),
        ('English (US)', 'Version', gen_yahei.get_version(font)),
        ('English (US)', 'PostScriptName', 'SimSun'),
        ('Chinese (PRC)', 'Family', '宋体'),
        ('Chinese (PRC)', 'Fullname', '宋体')
    )

def set_new_simsun_names(font):
    font.fontname = 'NSimSun'
    font.familyname = 'NSimSun'
    font.fullname = 'NSimSun'
    font.version = gen_yahei.get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'NSimSun'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'NSimSun'),
        ('English (US)', 'Fullname', 'NSimSun'),
        ('English (US)', 'Version', gen_yahei.get_version(font)),
        ('English (US)', 'PostScriptName', 'NSimSun'),
        ('Chinese (PRC)', 'Family', '新宋体'),
        ('Chinese (PRC)', 'Fullname', '新宋体')
    )

def set_simsun_ext_names(font):
    font.fontname = 'SimSun-ExtB'
    font.familyname = 'SimSun-ExtB'
    font.fullname = 'SimSun-ExtB'
    font.version = gen_yahei.get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'SimSun-ExtB'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'SimSun-ExtB'),
        ('English (US)', 'Fullname', 'SimSun-ExtB'),
        ('English (US)', 'Version', gen_yahei.get_version(font)),
        ('English (US)', 'PostScriptName', 'SimSun-ExtB')
    )


def gen_simsun():
    fs.copy(DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf', DOWNLOAD_DIR + '/sarasa-ui-cl-regular-new.ttf')

    font = gen_yahei.open_font(DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf')
    gen_yahei.remove_gasp(font)
    gen_yahei.set_cleartype(font)
    set_simsun_names(font)

    font_ui = gen_yahei.open_font(DOWNLOAD_DIR + '/sarasa-ui-cl-regular-new.ttf')
    gen_yahei.remove_gasp(font_ui)
    gen_yahei.set_cleartype(font_ui)
    set_new_simsun_names(font_ui)

    font.generateTtc(OUTPUT_DIR + '/simsun.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_simsun_ext():
    font = gen_yahei.open_font(DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf')
    gen_yahei.remove_gasp(font)
    gen_yahei.set_cleartype(font)
    set_simsun_ext_names(font)

    font.generate(OUTPUT_DIR + '/simsunb.ttf')
