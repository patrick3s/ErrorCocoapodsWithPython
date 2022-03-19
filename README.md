# Automation of error cocoapods in python

## Solution for mac os Catalina 10.15.5

### A while ago I was installing cocoapods on my MacBook Pro running with OSX 10.15.5 (Mac Os Catalina) and after typing gem install cocoapods I get the error:


- Building native extensions.  This could take a while...
- ERROR:  Error installing cocoapods:
-    ERROR: Failed to build gem native extension.
-        "/usr/local/rvm/rubies/ruby-1.9.3-p194/bin/ruby" -rubygems /usr/local/rvm/gems/ruby-1.9.3-p194/gems/rake-10.1.1/bin/rake RUBYARCHDIR=/Users/rangreenberg/gems/gems/xcodeproj-0.14.1/ext RUBYLIBDIR=/Users/rangreenberg/gems/gems/xcodeproj-0.14.1/ext
- /usr/local/rvm/rubies/ruby-1.9.3-p194/bin/ruby extconf.rb
- checking for -std=c99 option to compiler... *** extconf.rb failed ***
- Could not create Makefile due to some reason, probably lack of
- necessary libraries and/or headers.  Check the mkmf.log file for more
- details.  You may need configuration options.

- Provided configuration options:
-    --with-opt-dir
-    --with-opt-include
-    --without-opt-include=${opt-dir}/include
-    --with-opt-lib
-    --without-opt-lib=${opt-dir}/lib
-    --with-make-prog
-    --without-make-prog
-    --srcdir=.
-    --curdir
-    --ruby=/usr/local/rvm/rubies/ruby-1.9.3-p194/bin/ruby
- /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf. rb:381:in `try_do': The compiler failed to generate an - executable file. (RuntimeError)
- You have to install development tools first.
-    from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:491:in `block in try_compile'
-    from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:443:in `with_werror'
-    from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:491:in `try_compile'
-    from extconf.rb:24:in `block in <main>'
-    from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:790:in `block in checking_for'
-    from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:284:in `block (2 levels) in postpone'
-    from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:254:in `open'
-    from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:284:in `block in postpone'
 -   from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:254:in `open'
 -   from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:280:in `postpone'
 -   from /usr/local/rvm/rubies/ruby-1.9.3-p194/lib/ruby/1.9.1/mkmf.rb:789:in `checking_for'
 -   from extconf.rb:23:in `<main>'
-rake aborted!
-Command failed with status (1): [/usr/local/rvm/rubies/ruby-1.9.3-p194/bin/...]

- Tasks: TOP => default => ext
- (See full trace by running task with --trace)


- Gem files will remain installed in /Users/rangreenberg/gems/gems/xcodeproj-0.14.1 for inspection.


And I ended up finding an article that helped me solve this error as follows:

## Check the version of Ruby

- ruby -v

### Also check the given path:

- which ruby

1. Use Homebrew to install the latest Ruby

- brew install ruby

### Binaries installed by gem will be placed into:

- /usr/local/lib/ruby/gems/2.7.0/bin

1. Add this to your PATH.
### If you need to have ruby first in your PATH run:

- echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> /Users/user_name/.bash_profile

1. For compilers to find ruby you may need to set:
- export LDFLAGS="-L/usr/local/opt/ruby/lib"
- export CPPFLAGS="-I/usr/local/opt/ruby/include"

1. Follow the below instructions to set PATH. Now you will go to see the installed Ruby.
- echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> /Users/user_name/.bash_profile

- echo 'export LDFLAGS="-L/usr/local/opt/ruby/lib"' >> ~/.bash_profile

- echo 'export CPPFLAGS="-I/usr/local/opt/ruby/include"' >> ~/.bash_profile

- source ~/.bash_profile

1. Finally, Make sure your PATH is in place.
- ruby -v

- which ruby

1. Make sure you install by specifying the save destination as follows.
- sudo gem install -n /usr/local/bin cocoapods


reference : https://dev.to/delightfullynerdy/error-error-installing-cocoapods-error-failed-to-build-gem-native-extension-1505

### So I created an automation that is responsible for executing all these commands for me.
- python3 main.py