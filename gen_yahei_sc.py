import utils
import shutil as fs


def gen_yahei_regular_sc():
    fs.copy(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-regular.ttf', utils.DOWNLOAD_DIR + '/sarasa-ui-sc-regular-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_regular_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-regular-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_regular_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_SC + '/msyh.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_light_sc():
    fs.copy(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-light.ttf', utils.DOWNLOAD_DIR + '/sarasa-ui-sc-light-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-light.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_light_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-light-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_light_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_SC + '/msyhl.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_bold_sc():
    fs.copy(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-bold.ttf', utils.DOWNLOAD_DIR + '/sarasa-ui-sc-bold-ui.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-bold.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_bold_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-sc-bold-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_bold_ui_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_SC + '/msyhbd.ttc', font_ui, ttcflags = ('merge'), layer = 1)
