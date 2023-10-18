import utils
import shutil as fs


def gen_yahei_regular_cl():
    fs.copy(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf', utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_regular_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_regular_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_CL + '/msyh.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_light_cl():
    fs.copy(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-light.ttf', utils.DOWNLOAD_DIR + '/sarasa-ui-cl-light-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-light.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_light_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-light-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_light_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_CL + '/msyhl.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_bold_cl():
    fs.copy(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-bold.ttf', utils.DOWNLOAD_DIR + '/sarasa-ui-cl-bold-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-bold.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_bold_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-bold-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_bold_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_CL + '/msyhbd.ttc', font_ui, ttcflags = ('merge'), layer = 1)
