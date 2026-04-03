from setuptools import setup
import setup_translate

pkg = 'Extensions.Tetris'
setup(name='enigma2-plugin-extensions-tetris',
       version='3.0',
       description='Tetris-Clone HD/FHD modded by Lululla',
       package_dir={pkg: 'Tetris'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'keymap.xml', 'tetris.png', 'pic/*.jpg']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
