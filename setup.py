from distutils.core import setup
setup(
  name = 'Admin_List_BETA_v01',         # How you named your package folder (MyLib)
  packages = ['Admin_List_BETA_v01'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'For administration things (wow I sound unprofessional)',   # Give a short description about your library
  author = 'ThusEndingTheStory',                   # Type in your name
  author_email = 'Not gonna give it',      # Type in your E-Mail
  url = '',   # Provide either the link to your github or to your website
  download_url = 'idk',    # I explain this later on - https://github.com/user/reponame/archive/v_01.tar.gz
  keywords = ['so wow', 'much cool', 'grammar doge'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
