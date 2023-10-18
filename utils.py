import fontforge as ff

DOWNLOAD_DIR = '/tmp'
OUTPUT_DIR = '/tmp/out'
COPYRIGHT = 'sarasa2yahei'


def open_font(path):
    return ff.open(path)

def remove_gasp(font):
    font.gasp = ()

def set_cleartype(font):
    font.head_optimized_for_cleartype = 1

def get_version(font):
    return font.version.split(';')[0]


def set_yahei_regular_names(font):
    font.fontname = 'MicrosoftYaHei'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'Fullname', 'Microsoft YaHei'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑')
    )

def set_yahei_regular_ui_names(font):
    font.fontname = 'MicrosoftYaHeiUI'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 UI'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 UI')
    )

def set_yahei_light_names(font):
    font.fontname = 'MicrosoftYaHeiLight'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei Light'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Light'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Light'),
        ('English (US)', 'SubFamily', 'Light'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Light')
    )

def set_yahei_light_ui_names(font):
    font.fontname = 'MicrosoftYaHeiUILight'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI Light'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Light'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Light'),
        ('English (US)', 'SubFamily', 'Light'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 UI'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 UI Light')
    )

def set_yahei_bold_names(font):
    font.fontname = 'MicrosoftYaHeiBold'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei Bold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Bold'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Bold'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Bold')
    )

def set_yahei_bold_ui_names(font):
    font.fontname = 'MicrosoftYaHeiUIBold'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI Bold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Bold'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Bold'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('Chinese (PRC)', 'Family', '微软雅黑 UI'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 UI Bold')
    )


def set_simsun_names(font):
    font.fontname = 'SimSun'
    font.familyname = 'SimSun'
    font.fullname = 'SimSun'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'SimSun'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'SimSun'),
        ('English (US)', 'Fullname', 'SimSun'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'PostScriptName', 'SimSun'),
        ('Chinese (PRC)', 'Family', '宋体'),
        ('Chinese (PRC)', 'Fullname', '宋体')
    )

def set_new_simsun_names(font):
    font.fontname = 'NSimSun'
    font.familyname = 'NSimSun'
    font.fullname = 'NSimSun'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'NSimSun'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'NSimSun'),
        ('English (US)', 'Fullname', 'NSimSun'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'PostScriptName', 'NSimSun'),
        ('Chinese (PRC)', 'Family', '新宋体'),
        ('Chinese (PRC)', 'Fullname', '新宋体')
    )

def set_simsun_ext_names(font):
    font.fontname = 'SimSun-ExtB'
    font.familyname = 'SimSun-ExtB'
    font.fullname = 'SimSun-ExtB'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'SimSun-ExtB'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'SimSun-ExtB'),
        ('English (US)', 'Fullname', 'SimSun-ExtB'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'PostScriptName', 'SimSun-ExtB')
    )
