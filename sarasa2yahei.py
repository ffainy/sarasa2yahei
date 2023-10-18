import get_latest_sarasa, gen_yahei, gen_simsun, prepare_fonts

if __name__ == '__main__':

    get_latest_sarasa.clear_dir(get_latest_sarasa.DOWNLOAD_DIR)
    print('已下载字体文件清理完成：' + get_latest_sarasa.DOWNLOAD_DIR)
    get_latest_sarasa.clear_dir(get_latest_sarasa.OUTPUT_DIR)
    print('已输出字体文件清理完成：' + get_latest_sarasa.OUTPUT_DIR)

    ver = get_latest_sarasa.get_latest_tag()
    print('更纱黑体最新版本：' + ver)

    url = get_latest_sarasa.get_latest_url()
    path = get_latest_sarasa.download_sarasa(url)
    print('下载到本地：' + path)

    get_latest_sarasa.unzip_sarasa(path)
    print('下载完成！')

    gen_yahei.gen_yahei_regular()
    gen_yahei.gen_yahei_bold()
    gen_yahei.gen_yahei_light()
    print('雅黑成功生成！')

    gen_simsun.gen_simsun()
    gen_simsun.gen_simsun_ext()
    print('宋体成功生成！')

    prepare_fonts.compress_files()
    print('字体文件打包完成！')
